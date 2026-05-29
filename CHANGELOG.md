# Changelog

## 2026-05-29

- Refactored the module factory into a source-driven build: `Rules/`, `Scripts/`, `Rewrite/Sources/`, `Rewrite/Remotes/sources.json`, and `Rewrite/Profiles/stable.conf` are now the maintained inputs.
- Updated `scripts/build_module.py` so the default daily path builds from source inputs instead of extracting from the root module.
- Updated `scripts/factory_finalize.py` so the default path validates `Release/Ronghemokuai.sgmodule` and syncs it to the root module without rewriting source files.
- Updated `.github/workflows/module-factory-build.yml` to compile scripts, build from sources, finalize with `--sync-root`, and verify Root/Release equality.
- Preserved Spotify playback protection, Spotify header rewrite, YouTube Enhance, and the GitHub Pages update URL.
- Moved misplaced app ad reject rules out of `Rules/spotify-direct.list` and into `Rules/app-clean.list`.
- Added `backup/Ronghemokuai.before-factory-refactor.sgmodule` as a pre-refactor rollback point.
- Added `reports/factory_refactor_report.md`.

## 2026-05-28

- Completed the long-term maintenance file set and verified README maintenance links point to existing files.
- Added the daily invalid-source repair system with a 2-day confirmed failure threshold.
- Added stable backup files under `backup/`.
- Added `docs/COVERAGE.md` and `docs/SCOPE.md`.

## 2026-05-25

- Added one-click import buttons, `redirect.html`, and `import.html`.
- Added the daily module update workflow.
- Added maintenance and troubleshooting documentation.
- Added Spotify whitelist handling and Spotify / YouTube core checks.
- Registered trusted remote sources such as Remote AdBlock Hub, blackmatrix7, Cats-Team, zirawell/R-Store, fmz200/wool_scripts, and app2smile references.
- Added legacy selected-rule migration and reports.
- Added safe module refinement scripts for duplicate checks, script grouping, and core marker validation.
