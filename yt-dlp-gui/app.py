import os
import re
import sys
import subprocess
import threading
import uuid
from datetime import datetime
from urllib.parse import urlparse

from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

LOG_MAX_LINES = 700
MAX_TASKS = 120
# Save downloads to local machine Downloads folder (outside workspace)
DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Downloads", "PipeDL")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

TASKS = {}
TASKS_LOCK = threading.Lock()

ALLOWED_FORMATS = {
    "best_video",
    "mp4",
    "webm",
    "audio_best",
    "audio_opus",
    "audio_wav",
}


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def is_probably_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)
    except Exception:
        return False


def trim_tasks_if_needed() -> None:
    with TASKS_LOCK:
        if len(TASKS) <= MAX_TASKS:
            return
        # Remove oldest finished/error first
        ordered = sorted(TASKS.items(), key=lambda kv: kv[1].get("created_at", ""))
        for task_id, task in ordered:
            if len(TASKS) <= MAX_TASKS:
                break
            if task.get("status") in ("done", "error"):
                TASKS.pop(task_id, None)
        # if still too many, remove oldest regardless
        while len(TASKS) > MAX_TASKS:
            oldest_id = min(TASKS, key=lambda tid: TASKS[tid].get("created_at", ""))
            TASKS.pop(oldest_id, None)


def append_log(task: dict, line: str) -> None:
    task["log"].append(line)
    if len(task["log"]) > LOG_MAX_LINES:
        del task["log"][0 : len(task["log"]) - LOG_MAX_LINES]


def to_rate_limit(rate: str) -> str:
    # Accept values like 500K, 2M, 1.5M
    rate = (rate or "").strip().upper()
    if not rate:
        return ""
    if re.fullmatch(r"\d+(\.\d+)?[KMG]?", rate):
        return rate
    return ""


def build_command(url: str, fmt: str, options: dict) -> list[str]:
    base_cmd = [sys.executable, "-m", "yt_dlp"]

    if fmt == "best_video":
        cmd = base_cmd + ["-f", "bestvideo+bestaudio/best"]
    elif fmt == "mp4":
        cmd = base_cmd + ["-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"]
    elif fmt == "webm":
        cmd = base_cmd + ["-f", "bestvideo[ext=webm]+bestaudio/best[ext=webm]/best"]
    elif fmt == "audio_best":
        cmd = base_cmd + ["-f", "bestaudio/best", "-x", "--audio-format", "mp3"]
    elif fmt == "audio_opus":
        cmd = base_cmd + ["-f", "bestaudio/best", "-x", "--audio-format", "opus"]
    elif fmt == "audio_wav":
        cmd = base_cmd + ["-f", "bestaudio/best", "-x", "--audio-format", "wav"]
    else:
        cmd = base_cmd

    output_template = (options.get("outputTemplate") or "").strip()
    if output_template:
        cmd += ["-o", output_template]

    if bool(options.get("writeSubs")):
        cmd += ["--write-auto-sub", "--sub-langs", "all"]

    if bool(options.get("embedMetadata")):
        cmd += ["--embed-metadata"]

    if bool(options.get("embedThumbnail")):
        cmd += ["--embed-thumbnail"]

    cookies_path = (options.get("cookiesPath") or "").strip()
    if cookies_path:
        cmd += ["--cookies", cookies_path]

    rate_limit = to_rate_limit(options.get("rateLimit") or "")
    if rate_limit:
        cmd += ["--limit-rate", rate_limit]

    retries = str(options.get("retries") or "").strip()
    if retries.isdigit():
        cmd += ["--retries", retries]

    cmd += [url]
    return cmd


def run_yt_dlp(task_id: str, url: str, fmt: str, options: dict):
    with TASKS_LOCK:
        task = TASKS[task_id]

    cmd = build_command(url, fmt, options)
    append_log(task, f"$ {' '.join(cmd)}")

    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            cwd=DOWNLOAD_DIR,
        )

        with TASKS_LOCK:
            task["pid"] = proc.pid

        assert proc.stdout is not None
        for line in proc.stdout:
            append_log(task, line.rstrip("\n"))

        proc.wait()

        with TASKS_LOCK:
            if proc.returncode == 0:
                task["status"] = "done"
                task["finished_at"] = now_iso()
                append_log(task, "")
                append_log(task, "Download finished successfully.")
            else:
                task["status"] = "error"
                task["finished_at"] = now_iso()
                append_log(task, "")
                append_log(task, f"yt-dlp exited with code {proc.returncode}.")

        if proc.returncode == 0 and bool(options.get("autoOpenFolder", True)) and sys.platform.startswith("win"):
            try:
                os.startfile(DOWNLOAD_DIR)
            except Exception as e:
                append_log(task, f"Could not open download folder: {e}")

    except Exception as e:
        with TASKS_LOCK:
            task["status"] = "error"
            task["finished_at"] = now_iso()
            append_log(task, "")
            append_log(task, f"Error running yt-dlp: {e}")


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/api/download", methods=["POST"])
def api_download():
    data = request.get_json(force=True) or {}
    url = (data.get("url") or "").strip()
    fmt = (data.get("format") or "best_video").strip()
    options = data.get("options") or {}

    if not url or not is_probably_url(url):
        return jsonify({"error": "Valid URL is required"}), 400

    if fmt not in ALLOWED_FORMATS:
        fmt = "best_video"

    task_id = str(uuid.uuid4())
    task = {
        "task_id": task_id,
        "status": "running",
        "log": [],
        "url": url,
        "format": fmt,
        "created_at": now_iso(),
        "finished_at": None,
        "pid": None,
        "options": {
            "writeSubs": bool(options.get("writeSubs")),
            "embedMetadata": bool(options.get("embedMetadata")),
            "embedThumbnail": bool(options.get("embedThumbnail")),
            "autoOpenFolder": bool(options.get("autoOpenFolder", True)),
            "outputTemplate": (options.get("outputTemplate") or "").strip(),
            "cookiesPath": (options.get("cookiesPath") or "").strip(),
            "rateLimit": (options.get("rateLimit") or "").strip(),
            "retries": str(options.get("retries") or "").strip(),
        },
    }

    with TASKS_LOCK:
        TASKS[task_id] = task

    trim_tasks_if_needed()

    t = threading.Thread(target=run_yt_dlp, args=(task_id, url, fmt, task["options"]), daemon=True)
    t.start()

    return jsonify({"task_id": task_id})


@app.route("/api/status/<task_id>", methods=["GET"])
def api_status(task_id):
    with TASKS_LOCK:
        task = TASKS.get(task_id)
        if not task:
            return jsonify({"error": "Task not found"}), 404
        return jsonify(
            {
                "task_id": task["task_id"],
                "status": task["status"],
                "log": task["log"],
                "url": task["url"],
                "format": task["format"],
                "created_at": task["created_at"],
                "finished_at": task["finished_at"],
                "pid": task["pid"],
            }
        )


@app.route("/api/tasks", methods=["GET"])
def api_tasks():
    with TASKS_LOCK:
        items = list(TASKS.values())

    items.sort(key=lambda t: t.get("created_at", ""), reverse=True)
    return jsonify(
        [
            {
                "task_id": t["task_id"],
                "status": t["status"],
                "url": t["url"],
                "format": t["format"],
                "created_at": t["created_at"],
                "finished_at": t["finished_at"],
            }
            for t in items[:40]
        ]
    )


@app.route("/api/open-downloads", methods=["POST"])
def api_open_downloads():
    if not sys.platform.startswith("win"):
        return jsonify({"error": "Open folder is currently implemented for Windows only"}), 400
    try:
        os.startfile(DOWNLOAD_DIR)
        return jsonify({"ok": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
