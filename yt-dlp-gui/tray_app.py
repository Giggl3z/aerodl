import os
import sys
import time
import threading
import subprocess
from urllib.request import urlopen
from urllib.error import URLError
import tkinter as tk
from tkinter import ttk

import pystray
from PIL import Image, ImageDraw

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVER_CMD = [sys.executable, "app.py", "--no-debug"]
SERVER_URL = "http://127.0.0.1:5000/api/settings"
WEB_URL = "http://127.0.0.1:5000"
LOG_PATH = os.path.join(BASE_DIR, "pipedl-server.log")

BG = "#0b1220"
PANEL = "#121c2f"
TEXT = "#e6eefc"
MUTED = "#8ea4c8"
ACCENT = "#6ed4ff"
GOOD = "#4ade80"
BAD = "#fb7185"
WARN = "#fbbf24"


class PipeDLTrayApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("pipedl-server")
        self.root.geometry("460x300")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)
        self.root.configure(bg=BG)

        self.server_proc = None
        self.server_log_handle = None
        self.icon = None
        self.running = True

        self.status_var = tk.StringVar(value="Checking server...")
        self.toggle_var = tk.StringVar(value="Start Server")

        self._apply_theme()
        self._build_ui()

    def _apply_theme(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")

        style.configure("Root.TFrame", background=BG)
        style.configure("Card.TFrame", background=PANEL)

        style.configure("Title.TLabel", background=PANEL, foreground=TEXT, font=("Segoe UI", 17, "bold"))
        style.configure("Sub.TLabel", background=PANEL, foreground=MUTED, font=("Segoe UI", 10))
        style.configure("Info.TLabel", background=PANEL, foreground=TEXT, font=("Segoe UI", 10, "bold"))

        style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), padding=(12, 7), foreground=TEXT, background="#1b2b4a")
        style.map("Primary.TButton", background=[("active", "#243a63")])

        style.configure("Ghost.TButton", font=("Segoe UI", 10), padding=(10, 7), foreground=TEXT, background="#16243f")
        style.map("Ghost.TButton", background=[("active", "#21355a")])

        style.configure("Danger.TButton", font=("Segoe UI", 10, "bold"), padding=(10, 7), foreground=TEXT, background="#4b1f2e")
        style.map("Danger.TButton", background=[("active", "#5e2439")])

    def _build_ui(self):
        root_frame = ttk.Frame(self.root, style="Root.TFrame", padding=14)
        root_frame.pack(fill="both", expand=True)

        card = ttk.Frame(root_frame, style="Card.TFrame", padding=14)
        card.pack(fill="both", expand=True)

        ttk.Label(card, text="pipedl-server", style="Title.TLabel").pack(anchor="w")
        ttk.Label(card, text="Tray server controller", style="Sub.TLabel").pack(anchor="w", pady=(0, 12))

        status_row = ttk.Frame(card, style="Card.TFrame")
        status_row.pack(fill="x", pady=(0, 12))

        self.status_dot = tk.Canvas(status_row, width=10, height=10, bg=PANEL, highlightthickness=0)
        self.status_dot.pack(side="left", padx=(0, 8))
        self.status_dot_id = self.status_dot.create_oval(1, 1, 9, 9, fill=WARN, outline="")

        ttk.Label(status_row, textvariable=self.status_var, style="Info.TLabel").pack(side="left")

        actions = ttk.Frame(card, style="Card.TFrame")
        actions.pack(fill="x", pady=(0, 10))

        self.toggle_btn = ttk.Button(actions, textvariable=self.toggle_var, command=self.toggle_server, style="Primary.TButton")
        self.toggle_btn.pack(side="left", padx=(0, 8))

        ttk.Button(actions, text="Open Web UI", command=self.open_web, style="Ghost.TButton").pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="View Logs", command=self.open_logs_window, style="Ghost.TButton").pack(side="left")

        bottom = ttk.Frame(card, style="Card.TFrame")
        bottom.pack(fill="x", side="bottom", pady=(14, 0))

        ttk.Button(bottom, text="Hide to Tray", command=self.hide_window, style="Ghost.TButton").pack(side="left")
        ttk.Button(bottom, text="Exit", command=self.exit_app, style="Danger.TButton").pack(side="right")

    def create_icon_image(self):
        img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.rounded_rectangle((4, 4, 60, 60), radius=14, fill=(11, 18, 32, 255), outline=(110, 212, 255, 255), width=2)
        draw.text((20, 16), "P", fill=(110, 212, 255, 255))
        return img

    def create_tray_icon(self):
        menu = pystray.Menu(
            pystray.MenuItem("Show", self.show_window),
            pystray.MenuItem("Open Web UI", self.open_web),
            pystray.MenuItem("Start/Stop Server", self.toggle_server),
            pystray.MenuItem("Exit", self.exit_app),
        )
        self.icon = pystray.Icon("pipedl-server", self.create_icon_image(), "pipedl-server", menu)
        threading.Thread(target=self.icon.run, daemon=True).start()

    def is_server_up(self):
        try:
            with urlopen(SERVER_URL, timeout=1.5) as r:
                return r.status == 200
        except URLError:
            return False
        except Exception:
            return False

    def start_server(self):
        if self.server_proc and self.server_proc.poll() is None:
            return
        if self.is_server_up():
            return

        self.server_log_handle = open(LOG_PATH, "a", encoding="utf-8")
        self.server_proc = subprocess.Popen(
            SERVER_CMD,
            cwd=BASE_DIR,
            stdout=self.server_log_handle,
            stderr=subprocess.STDOUT,
            text=True,
        )

    def stop_server(self):
        if not self.server_proc:
            return
        if self.server_proc.poll() is None:
            try:
                self.server_proc.terminate()
                self.server_proc.wait(timeout=5)
            except Exception:
                try:
                    self.server_proc.kill()
                except Exception:
                    pass

        self.server_proc = None
        if self.server_log_handle:
            try:
                self.server_log_handle.close()
            except Exception:
                pass
            self.server_log_handle = None

    def toggle_server(self, *args):
        managed_running = self.server_proc and self.server_proc.poll() is None
        external_running = self.is_server_up() and not managed_running

        if managed_running:
            self.stop_server()
        elif external_running:
            self.show_window()
        else:
            self.start_server()

        self.update_status_once()

    def _set_status_visual(self, color):
        self.status_dot.itemconfig(self.status_dot_id, fill=color)

    def update_status_once(self):
        up = self.is_server_up()
        managed_running = self.server_proc and self.server_proc.poll() is None

        if up and managed_running:
            self.status_var.set("Server online (managed by tray)")
            self.toggle_var.set("Shutdown Server")
            self.toggle_btn.configure(state="normal")
            self._set_status_visual(GOOD)
        elif up:
            self.status_var.set("Server online (external instance)")
            self.toggle_var.set("External server active")
            self.toggle_btn.configure(state="disabled")
            self._set_status_visual(WARN)
        else:
            self.status_var.set("Server offline")
            self.toggle_var.set("Start Server")
            self.toggle_btn.configure(state="normal")
            self._set_status_visual(BAD)

    def poll_status_loop(self):
        while self.running:
            self.root.after(0, self.update_status_once)
            time.sleep(2)

    def open_web(self, *args):
        import webbrowser
        webbrowser.open(WEB_URL)

    def open_logs_window(self):
        win = tk.Toplevel(self.root)
        win.title("pipedl-server logs")
        win.geometry("820x500")
        win.configure(bg=BG)

        text = tk.Text(
            win,
            wrap="word",
            font=("Consolas", 10),
            bg="#070d18",
            fg="#dbe7ff",
            insertbackground="#dbe7ff",
            relief="flat",
        )
        text.pack(fill="both", expand=True, padx=10, pady=(10, 0))

        def refresh():
            try:
                with open(LOG_PATH, "r", encoding="utf-8", errors="ignore") as f:
                    data = f.read()
            except FileNotFoundError:
                data = "No log file yet. Start the server first."

            text.delete("1.0", "end")
            text.insert("1.0", data[-30000:])
            text.see("end")

        btn_row = ttk.Frame(win, style="Root.TFrame", padding=(10, 8))
        btn_row.pack(fill="x")
        ttk.Button(btn_row, text="Refresh", command=refresh, style="Ghost.TButton").pack(side="right")
        refresh()

    def hide_window(self, *args):
        self.root.withdraw()

    def show_window(self, *args):
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()

    def exit_app(self, *args):
        self.running = False
        self.stop_server()
        if self.icon:
            self.icon.stop()
        self.root.quit()

    def run(self):
        self.create_tray_icon()
        self.start_server()
        self.update_status_once()
        threading.Thread(target=self.poll_status_loop, daemon=True).start()
        self.root.mainloop()


if __name__ == "__main__":
    PipeDLTrayApp().run()
