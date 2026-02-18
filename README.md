# 🚀 AeroDL

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Brave Extension](https://img.shields.io/badge/Brave-MV3-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

> A modern `yt-dlp` toolkit with a full web UI + Brave extension controls.

AeroDL makes `yt-dlp` easier to use with a clean interface, quick presets, and YouTube-integrated actions.

---

## ✨ Highlights

- 🎬 Format presets: Best / MP4 / WebM / MP3 / Opus / WAV
- ⚙️ Advanced `yt-dlp` options (subs, metadata, thumbnail, retries, rate limit)
- 📜 Live console output
- 🧾 Task history
- ▶️ YouTube action-row **AeroDL** button with quick menu
- 🧩 Brave popup controller + options page

---

## 🧱 Project Structure

```text
.
├─ yt-dlp-gui/                 # Flask backend + full website UI
│  ├─ app.py
│  ├─ README.md
│  └─ static/
├─ yt-dlp-brave-extension/     # Brave MV3 extension
│  ├─ manifest.json
│  ├─ popup.html
│  ├─ popup.js
│  ├─ youtube-button.js
│  ├─ options.html
│  └─ README.md
└─ docs/
   ├─ SETUP.md
   └─ TROUBLESHOOTING.md
```

---

## ⚡ Quick Start

### 1) One-time setup (recommended) — one-liner

```powershell
powershell -ExecutionPolicy Bypass -File .\setup.ps1
```

### 2) Start AeroDL backend — one-liner

```powershell
powershell -ExecutionPolicy Bypass -File .\run.ps1
```

Manual alternative (one-liner):

```powershell
cd yt-dlp-gui; python -m pip install flask yt-dlp; python app.py
```

- 🌐 GUI URL: `http://localhost:5000`
- 📂 Download path: `C:\Users\<you>\Downloads\AeroDL`

### 3) Load Brave extension

1. Open `brave://extensions`
2. Enable **Developer mode**
3. Click **Load unpacked**
4. Select folder: `yt-dlp-brave-extension/`

### 4) Download from YouTube

1. Open a YouTube video page
2. Click **AeroDL** near Like/Share buttons
3. Pick a format and press **Download**

---

## 📚 Docs

- 🛠 Setup guide → [`docs/SETUP.md`](docs/SETUP.md)
- 🩺 Troubleshooting → [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md)
- ✅ Public release checklist → [`docs/PUBLIC_RELEASE_CHECKLIST.md`](docs/PUBLIC_RELEASE_CHECKLIST.md)
- 🧾 Release notes template → [`docs/RELEASE_TEMPLATE.md`](docs/RELEASE_TEMPLATE.md)
- 🧩 Extension notes → [`yt-dlp-brave-extension/README.md`](yt-dlp-brave-extension/README.md)
- 🖥 GUI notes → [`yt-dlp-gui/README.md`](yt-dlp-gui/README.md)
- 🔐 Security/Privacy → [`SECURITY.md`](SECURITY.md)

---

## 🧠 Pro Tips

- Keep backend running while using extension.
- If YouTube button disappears after update, reload extension + refresh tab.
- Avoid committing media files (`.mp4`, `.wav`, etc.) to GitHub.

---

## ⚠️ Limitations

- The Brave extension cannot execute `yt-dlp` directly due to browser sandboxing.
- A local backend (`yt-dlp-gui`) must be running for extension actions.

## 🤝 Contributing

- Open bugs with the built-in issue templates.
- Keep PRs focused and include reproduction/test notes.
- Avoid committing generated media or local machine artifacts.

## ⚖️ License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE).

## ⚠️ Legal / Responsible Use

Use AeroDL responsibly and in compliance with platform Terms of Service and your local laws.
