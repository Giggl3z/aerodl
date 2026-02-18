# AeroDL Brave Extension (MV3)

This extension provides a Brave popup GUI for your local `yt-dlp` web backend.

## Important
A browser extension **cannot run yt-dlp directly** due to browser sandboxing.
It controls your already-running local backend (Flask app at `http://localhost:5000` by default).

## Folder
`C:\Users\KenPC\.openclaw\workspace\yt-dlp-brave-extension`

## Load in Brave
1. Open `brave://extensions`
2. Enable **Developer mode**
3. Click **Load unpacked**
4. Select this folder: `yt-dlp-brave-extension`

## Run backend first
In another terminal:

```bash
cd C:\Users\KenPC\.openclaw\workspace\yt-dlp-gui
python app.py
```

## Features
- Start download tasks
- Format selection
- Core toggles (subs/metadata/thumbnail/auto-open)
- Task history + console view
- Theme switcher
- Open downloads folder button
- Options page for backend URL
