# Repository Cleanup Report

Date: 2026-05-29

## Current Structure Status

- Root import module: `Ronghemokuai.sgmodule`
- Generated release module: `Release/Ronghemokuai.sgmodule`
- Active build profile: `Rewrite/Profiles/stable.conf`
- Remote source registry: `Rewrite/Remotes/sources.json`
- Local rule sources: `Rules/`
- Script sources: `Scripts/`
- Compatibility source fragments: `Rewrite/Sources/`
- Factory scripts: `scripts/build_module.py`, `scripts/factory_finalize.py`
- Factory workflow: `.github/workflows/module-factory-build.yml`
- Factory documentation: `docs/FACTORY_FLOW.md`

## Removed Redundant Files

- Removed `reports/repository_audit_report.md` because it referenced deleted transitional paths such as `Web/`, `Rewrite/Generator/`, and `docs/PROJECT_STRUCTURE.md`.

## Core Files Kept

- `Ronghemokuai.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Rewrite/Profiles/stable.conf`
- `Rewrite/Remotes/sources.json`
- `Rewrite/Sources/`
- `Rules/`
- `Scripts/`
- `scripts/build_module.py`
- `scripts/factory_finalize.py`
- `.github/workflows/module-factory-build.yml`
- `docs/FACTORY_FLOW.md`
- `README.md`
- `import.html`
- `redirect.html`
- `backup/`
- `reports/`

## Flow Fixes

- Refactored the factory into a source-driven build path.
- Ran `scripts/build_module.py --build --profile stable`.
- Ran `scripts/factory_finalize.py --sync-root`.
- Regenerated `Release/Ronghemokuai.sgmodule`.
- Synchronized `Release/Ronghemokuai.sgmodule` back to root `Ronghemokuai.sgmodule`.
- Updated `docs/FACTORY_FLOW.md` as the single factory-flow reference.
- Updated `README.md` maintenance links to include the source-driven factory reports.
- Updated `Rewrite/Profiles/README.md` so it no longer suggests inactive `full.conf` or `test.conf` profiles.
- Fixed `scripts/build_module.py` merge deduplication so repeated factory runs do not accumulate duplicate comment/source marker lines.
- Reserved `--extract-from-root` for initialization or recovery only.

## Scripts Classification

- `Scripts/spotify.conf` contains only Spotify / spclient scripts.
- `Scripts/youtube.conf` contains only YouTube / Maasea scripts.
- `Scripts/app-clean.conf` contains Tieba, QQ News, VGTime, app2smile non-Spotify scripts, fmz200 / wool_scripts scripts, and zirawell / R-Store app-clean scripts.

## Rules Classification

- `Rules/spotify-direct.list` keeps Spotify playback protection separate from reject rules.
- `Rules/youtube-direct.list` keeps only narrow YouTube protection entries.
- `Rules/direct.list` keeps general DIRECT entries.
- `Rules/reject.list`, `Rules/app-clean.list`, and `Rules/web-ads.list` remain separated by purpose.
- No new bulk unverified rule source was added.

## README Link Check

- README maintenance entries point to existing repository files.
- Removed-file entries are not present.
- Install button, fallback import page, raw module URL, GitHub Pages module URL, and usage instructions remain present.

## Workflow Check

- `module-factory-build.yml`, `daily-module-update.yml`, and `daily-invalid-source-repair.yml` all have `permissions: contents: write`.
- The three write workflows share `concurrency.group: module-maintenance`.
- `module-factory-build.yml` compiles the factory scripts, builds from source inputs, finalizes with `--sync-root`, validates Root/Release equality, and commits generated factory output.
- `daily-module-update.yml` remains limited to date and report updates.
- `daily-invalid-source-repair.yml` keeps the 2-day confirmed failure threshold and protected core item checks.

## Root / Release Check

- Root and Release are identical after `factory_finalize.py`.
- Diff lines after sync: `0`.
- Required markers are present: `[Rule]`, `[Script]`, `[MITM]`, `spotify-json`, `spotify-proto`, `youtube.response`, and the expected `update-url`.

## Manual Test Items

- Import `Ronghemokuai.sgmodule` in Shadowrocket.
- Update module and scripts in Shadowrocket.
- Test Spotify playback for skipping or loading issues.
- Test YouTube playback and YouTube Enhance behavior.
- Test login, payment, verification code, banking, WeChat, and Alipay flows with the module enabled.
- Review `reports/module_factory_report.md`, `reports/module_factory_diff_report.md`, and `reports/factory_finalize_report.md` after the first GitHub Actions factory run.
