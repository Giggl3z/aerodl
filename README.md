# PIPE DL

<p align="left">
  <img src="docs/assets/pipedl-logo-bold.svg" alt="PipeDL logo" width="620" />
</p>

![Python](https://img.shields.io/badge/Python-3.10%2B-2563EB)
![Brave Extension](https://img.shields.io/badge/Brave-MV3-F97316)
![License](https://img.shields.io/badge/License-MIT-16A34A)

**PipeDL is a bold, modern `yt-dlp` workflow toolkit with:**
- **Web app control panel**
- **Brave extension popup**
- **YouTube in-page action button**

---

## WHY PIPE DL

- **FAST START**: paste URL and download immediately
- **POWER MODE**: exact quality selection + advanced flags
- **QUEUE CONTROL**: queued/running visibility, concurrency, cancel
- **LIVE FEEDBACK**: real-time logs + task history

---

## PROJECT STRUCTURE

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

## INSTALL (GIT)

```bash
git clone https://github.com/Giggl3z/pipedl.git
cd pipedl
```

Update later:

```bash
git pull
```

---

## QUICK START

### 1) Setup once

```powershell
powershell -ExecutionPolicy Bypass -File .\setup.ps1
```

### 2) Run PipeDL

```powershell
powershell -ExecutionPolicy Bypass -File .\run.ps1
```

### 3) Open app

- **URL**: `http://localhost:5000`
- **Output folder**: `C:\Users\<you>\Downloads\PipeDL`

---

## BRAVE EXTENSION SETUP

1. Open `brave://extensions`
2. Enable **Developer mode**
3. Click **Load unpacked**
4. Select: `yt-dlp-brave-extension/`

Then on YouTube:
1. Open a video page (`/watch` or `/shorts`)
2. Click **PipeDL** near Like/Share
3. Choose format and download

---

## WEB UI MODES

### SIMPLE MODE
- Quick download flow
- Minimal options

### PRO MODE
- Advanced options
- Exact quality picker
- Queue controls (stats / concurrency / cancel)

### TASK STATUSES
- `queued`
- `running`
- `done`
- `error`
- `canceled`

---

## API

- `POST /api/download`
- `POST /api/formats`
- `GET /api/status/<task_id>`
- `GET /api/tasks`
- `POST /api/cancel/<task_id>`
- `GET/POST /api/settings`
- `POST /api/open-downloads`

---

## DOCS

- Setup: [`docs/SETUP.md`](docs/SETUP.md)
- Troubleshooting: [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md)
- Changelog: [`CHANGELOG.md`](CHANGELOG.md)
- Release template: [`docs/RELEASE_TEMPLATE.md`](docs/RELEASE_TEMPLATE.md)
- Public release checklist: [`docs/PUBLIC_RELEASE_CHECKLIST.md`](docs/PUBLIC_RELEASE_CHECKLIST.md)
- Security notes: [`SECURITY.md`](SECURITY.md)

---

## IMPORTANT LIMITATIONS

- Browser extensions cannot run `yt-dlp` directly (sandbox limitation).
- Local backend (`yt-dlp-gui`) must be running for extension actions.

---

## CONTRIBUTING

- Use issue templates for bug/feature reports
- Keep PRs focused and testable
- Do not commit generated media or machine-specific artifacts

---

## LICENSE

MIT — see [`LICENSE`](LICENSE)

## RESPONSIBLE USE

Use PipeDL in compliance with platform Terms of Service and applicable laws.
