# 🧩 AeroDL Brave Extension (MV3)

Brave extension UI for controlling the local AeroDL backend.

---

## ⚠️ Important

A browser extension **cannot run `yt-dlp` directly** (sandbox restriction).
It sends commands to your local backend (default: `http://localhost:5000`).

---

## 📁 Folder

`C:\Users\KenPC\.openclaw\workspace\yt-dlp-brave-extension`

---

## 🚀 Load in Brave

1. Open `brave://extensions`
2. Enable **Developer mode**
3. Click **Load unpacked**
4. Select folder: `yt-dlp-brave-extension`

---

## ▶️ Run backend first

In another terminal:

```bash
cd C:\Users\KenPC\.openclaw\workspace\yt-dlp-gui
python app.py
```

---

## ✨ Features

- ▶️ Start download tasks
- 🎚 Format selection
- ⚙ Core toggles (subs / metadata / thumbnail / auto-open)
- 🧾 Task history + console view
- 🎨 Theme switcher
- 📂 Open downloads folder
- 🛠 Options page for backend URL
- ▶️ YouTube in-page **AeroDL** action-row button + menu
