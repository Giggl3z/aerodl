# 🚢 Public Release Checklist

Use this before marking the repo public.

## Repository Hygiene

- [ ] `git status` is clean
- [ ] No personal/local files are tracked
- [ ] No downloaded media files are tracked (`.mp4`, `.wav`, etc.)
- [ ] `.gitignore` excludes generated content

## Docs

- [ ] Root README is clear and up-to-date
- [ ] Setup guide works from a fresh machine
- [ ] Troubleshooting doc covers common errors
- [ ] License is present
- [ ] Security/Privacy note is present

## Runtime Safety

- [ ] Backend bound for local usage expectations
- [ ] No hardcoded secrets/tokens
- [ ] Extension host permissions are minimal
- [ ] Download path behavior documented

## Functional Tests

- [ ] Start backend (`python app.py`) works
- [ ] Web UI can start downloads
- [ ] Extension popup can start downloads
- [ ] YouTube in-page AeroDL button appears and works
- [ ] Error states show useful messages

## Release

- [ ] Tag a version (optional)
- [ ] Create first release notes
- [ ] Add screenshots/gif (optional but recommended)
