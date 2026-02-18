# PipeDL

<p align="left">
  <img src="docs/assets/pipedl-logo-bold.svg" alt="PipeDL logo" width="620" />
</p>

![Python](https://img.shields.io/badge/Python-3.10%2B-2563EB)
![Brave Extension](https://img.shields.io/badge/Brave-MV3-F97316)
![License](https://img.shields.io/badge/License-MIT-16A34A)
![Status](https://img.shields.io/badge/Status-Active-22C55E)

> **PipeDL** = `yt-dlp` + local web control center + Brave extension + YouTube in-page action menu.

---

## [LOG 00] Mission

### Added
- A full local GUI workflow for `yt-dlp`
- Brave popup control surface
- YouTube in-page download trigger

### Why this exists
- CLI power with GUI speed
- Queue-safe downloads instead of one-off command chaos
- Better visibility (logs, status, history)

---

## [LOG 01] Quick Start

### Added
- One-minute startup path via scripts

```powershell
git clone https://github.com/Giggl3z/pipedl.git
cd pipedl
.\setup.ps1
.\run.ps1
```

### Output
- Open `http://localhost:5000`

### Fallback
If scripts are blocked by policy:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup.ps1
powershell -ExecutionPolicy Bypass -File .\run.ps1
```

---

## [LOG 02] Feature Surface

### Added
- **Web App (`yt-dlp-gui`)**: full dashboard control
- **Brave Extension (`yt-dlp-brave-extension`)**: quick popup workflow
- **YouTube Action Button**: in-page format menu + one-click send

### Added — Download Modes
- Presets: Best / MP4 / WebM / MP3 / Opus / WAV
- Exact quality picker (`/api/formats`, `format_id` selection)
- Advanced flags: subtitles, metadata, thumbnails, retries, rate limits, cookies

### Added — Queue Ops
- Queued/running metrics
- Runtime concurrency control
- Per-task cancel
- Status + timing tooltips

---

## [LOG 03] First-Time Setup Flow

### Step 1 — Start backend
- Run `python app.py` inside `yt-dlp-gui` (or use `run.ps1`)

### Step 2 — Load extension in Brave
1. Open `brave://extensions`
2. Enable **Developer mode**
3. Click **Load unpacked**
4. Select `yt-dlp-brave-extension/`

### Step 3 — Validate on YouTube
1. Open a `/watch` or `/shorts` URL
2. Click **PipeDL** near Like/Share
3. Pick format and run

### Output path
- `C:\Users\<you>\Downloads\PipeDL`

---

## [LOG 04] API Index

### Added
- `POST /api/download`
- `POST /api/formats`
- `GET /api/status/<task_id>`
- `GET /api/tasks`
- `POST /api/cancel/<task_id>`
- `GET/POST /api/settings`
- `POST /api/open-downloads`

---

## [LOG 05] UI Modes

### Simple
- Minimal controls
- Fast path

### Pro
- Exact quality picker
- Queue controls (stats/concurrency/cancel)
- Advanced option panel

---

## [LOG 06] Install (Manual Path)

```powershell
cd yt-dlp-gui
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
```

---

## [LOG 07] Repo Map

```text
.
├─ yt-dlp-gui/                 # Flask backend + web UI
│  ├─ app.py
│  ├─ requirements.txt
│  └─ static/
├─ yt-dlp-brave-extension/     # Brave MV3 extension
│  ├─ manifest.json
│  ├─ popup.html
│  ├─ popup.js
│  ├─ youtube-button.js
│  ├─ options.html
│  └─ README.md
├─ docs/
│  ├─ SETUP.md
│  ├─ TROUBLESHOOTING.md
│  ├─ PUBLIC_RELEASE_CHECKLIST.md
│  └─ RELEASE_TEMPLATE.md
├─ CHANGELOG.md
└─ LICENSE
```

---

## [LOG 08] Docs Index

- Setup → [`docs/SETUP.md`](docs/SETUP.md)
- Troubleshooting → [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md)
- Changelog → [`CHANGELOG.md`](CHANGELOG.md)
- Release template → [`docs/RELEASE_TEMPLATE.md`](docs/RELEASE_TEMPLATE.md)
- Public release checklist → [`docs/PUBLIC_RELEASE_CHECKLIST.md`](docs/PUBLIC_RELEASE_CHECKLIST.md)
- Security notes → [`SECURITY.md`](SECURITY.md)

---

## [LOG 09] Constraints

### Known
- Browser extensions cannot execute `yt-dlp` directly (sandbox)
- Local backend must be running for popup/in-page actions

---

## [LOG 10] Contribution Notes

### Required
- Use issue templates for bug/feature reports
- Keep PRs focused and testable
- Avoid committing generated media or machine-specific artifacts

---

## [LOG 11] License + Responsible Use

- License: MIT (`LICENSE`)
- Use PipeDL in compliance with platform ToS and local law
