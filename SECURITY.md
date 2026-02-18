# Security & Privacy

## Supported Versions

This project is currently maintained on the latest `master` branch.

## Reporting a Vulnerability

If you discover a security issue, please open a private report first (if possible) before creating a public issue.
Include:

- Affected component (`yt-dlp-gui` or `yt-dlp-brave-extension`)
- Reproduction steps
- Potential impact
- Suggested mitigation (optional)

## Security Notes

- The Brave extension **does not run yt-dlp directly**. It sends requests to a local backend.
- The backend is intended for local use (`localhost` / `127.0.0.1`) and should not be exposed publicly without additional hardening.
- Cookies paths and other optional inputs are user-provided; review before sharing logs/screenshots publicly.
- Downloaded files are stored on local machine (`Downloads/AeroDL` by default).

## Hardening Recommendations

- Keep Python and dependencies updated.
- Keep `yt-dlp` updated.
- If you expose backend beyond localhost, add authentication and strict network controls.
- Do not commit downloaded media or secrets into git.
