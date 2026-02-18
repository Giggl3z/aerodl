# Changelog

All notable changes to this project will be documented in this file.

Format inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- Changelog policy: every meaningful change should be recorded here.

## [2026-02-18]

### Added
- Public release readiness docs:
  - `LICENSE` (MIT)
  - `SECURITY.md`
  - `docs/PUBLIC_RELEASE_CHECKLIST.md`
  - `docs/RELEASE_TEMPLATE.md`
  - `setup.ps1` and `run.ps1`
  - GitHub issue templates (`bug_report`, `feature_request`)
- Brave YouTube in-page AeroDL/PipeDL action button and styled dropdown menu.
- Keyboard support in menu (Arrow keys, Enter, Escape).
- PipeDL one-line quick-start commands in README.

### Changed
- Project renamed from **AeroDL** to **PipeDL** across app, extension, and docs.
- GitHub repository renamed from `aerodl` to `pipedl`.
- Download output path changed to local machine folder (`Downloads/PipeDL`).
- Root README redesigned/polished for public-facing usage.
- YouTube button icon refined to YouTube-like stroke style.
- Main web UI slightly modernized (subtle glass/grid polish).
- Release template updated with explicit release date fields.

### Fixed
- Removed PC-specific absolute paths from docs.
- Stopped tracking Python cache artifact (`__pycache__/app.cpython-312.pyc`).
- Improved YouTube menu positioning/overflow handling to avoid off-screen clipping.

---

## Changelog workflow

- Add entries under **[Unreleased]** as work happens.
- On release, move items into a dated section (e.g. `## [YYYY-MM-DD]`).
- Keep entries short and user-visible (Added/Changed/Fixed).
