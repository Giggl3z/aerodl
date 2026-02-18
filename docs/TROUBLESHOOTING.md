# PipeDL Troubleshooting

Common issues and quick fixes.

---

## Extension says server offline

Symptoms:
- popup chip shows `server: offline`
- download/open/refresh controls are disabled

Fix:
1. Start backend (`.\run.ps1`) or start `pipedl-server` (`.\run-tray.ps1`)
2. Verify `http://localhost:5000` opens in browser
3. Ensure extension backend URL is correct in options

---

## pipedl-server shows ONLINE (external instance)

Meaning:
- backend is running, but not launched by `pipedl-server`

Behavior:
- status is accurate
- tray app won’t stop unmanaged process

If you want full tray control:
1. stop external backend process
2. click start inside `pipedl-server`

---

## PipeDL button missing on YouTube

- Confirm extension is enabled in `brave://extensions`
- Reload extension and refresh YouTube page
- Test on valid routes: `/watch` or `/shorts`

---

## Task stuck in queued

- Increase concurrency from web UI
- Cancel hung running task
- Retry failed tasks (`Retry Failed` button)
- Restart backend if needed

---

## Download starts but fails

- Update yt-dlp:

```powershell
cd yt-dlp-gui
python -m pip install --upgrade yt-dlp
```

- Re-run backend and try again
- Check cookies path if target requires login

---

## Scripts blocked by PowerShell policy

Use explicit bypass:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup.ps1
powershell -ExecutionPolicy Bypass -File .\run.ps1
```

---

## Startup task didn’t install

Run as the same user who will use PipeDL and retry:

```powershell
.\install-tray-autostart.ps1
```

To remove:

```powershell
.\uninstall-tray-autostart.ps1
```

---

## Wrong output folder

Default:
`C:\Users\<you>\Downloads\PipeDL`

To change it, edit `yt-dlp-gui/app.py` (`DOWNLOAD_DIR`) and restart.
