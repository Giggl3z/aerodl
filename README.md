# PipeDL

A minimal `yt-dlp` toolkit with:
- local web app (`yt-dlp-gui`)
- Brave extension (`yt-dlp-brave-extension`)
- YouTube in-page action button

## Quick Start

```powershell
git clone https://github.com/Giggl3z/pipedl.git
cd pipedl
.\setup.ps1
.\run.ps1
```

Open: `http://localhost:5000`

## Install Options

### Recommended

```powershell
.\setup.ps1
.\run.ps1
```

If scripts are blocked:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup.ps1
powershell -ExecutionPolicy Bypass -File .\run.ps1
```

### Manual

```powershell
cd yt-dlp-gui
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
```

## First-Time Setup

1. Start backend (`python app.py` or `run.ps1`)
2. Open `brave://extensions`
3. Enable **Developer mode**
4. Click **Load unpacked**
5. Select `yt-dlp-brave-extension/`

Default output folder:
- `C:\Users\<you>\Downloads\PipeDL`

## Features

- Presets: Best / MP4 / WebM / MP3 / Opus / WAV
- Exact quality picker
- Queue + concurrency controls
- Cancel queued/running tasks
- Retry failed tasks
- Live logs + task history

## API

- `POST /api/download`
- `POST /api/formats`
- `GET /api/status/<task_id>`
- `GET /api/tasks`
- `POST /api/cancel/<task_id>`
- `POST /api/retry-failed`
- `GET/POST /api/settings`
- `POST /api/open-downloads`

## Project Structure

```text
.
├─ yt-dlp-gui/
│  ├─ app.py
│  ├─ requirements.txt
│  └─ static/
├─ yt-dlp-brave-extension/
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

## Documentation

- `docs/SETUP.md`
- `docs/TROUBLESHOOTING.md`
- `CHANGELOG.md`
- `SECURITY.md`

## Limitations

- Browser extensions cannot execute `yt-dlp` directly.
- Local backend must be running for extension actions.

## License

MIT — see `LICENSE`

## Responsible Use

Use PipeDL in compliance with platform Terms of Service and local laws.
