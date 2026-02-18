# 🖥️ PipeDL GUI (`yt-dlp-gui`)

Local web backend + modern website UI for running `yt-dlp` with a clean interface.

---

## ✨ Features

- 🎬 Preset formats (Best, MP4, WebM, MP3, Opus, WAV)
- ⚙️ Advanced flags (subs, metadata, thumbnail, retries, rate limit, output template)
- 📜 Live console output
- 🧾 Task history API
- 📂 Open downloads folder endpoint

---

## ▶️ Run

```bash
python -m pip install flask yt-dlp
python app.py
```

Open in browser: `http://localhost:5000`

---

## 🔌 API Endpoints

- `POST /api/download`
- `GET /api/status/<task_id>`
- `GET /api/tasks`
- `POST /api/open-downloads`

---

## 📂 Download Location

`C:\Users\<you>\Downloads\PipeDL`

---

## 🛠 Notes

- Uses `python -m yt_dlp` internally
- Keep this backend running while using the Brave extension
