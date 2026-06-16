# Build Refactor Report

Date: 2026-05-29

## Refactor Summary

The repository has been refactored from a transitional root-module extraction flow to a source-driven module build flow.

Daily source of truth:

- `Rules/*.list`
- `Scripts/*.conf`
- `Rewrite/Sources/*.conf`
- `Rewrite/Remotes/sources.json`
- `Rewrite/Profiles/stable.conf`

Build outputs:

- `Release/Ronghemokuai.sgmodule`
- `Ronghemokuai.sgmodule`

## Reworked Sections

- `[Rule]`: built from `Rules/`, enabled remotes in `Rewrite/Remotes/sources.json`, and compatibility rules in `Rewrite/Sources/Rule.conf`.
- `[URL Rewrite]`: built from `Rewrite/Sources/URL-Rewrite.conf`.
- `[Header Rewrite]`: built from `Rewrite/Sources/Header-Rewrite.conf`.
- `[Body Rewrite]`: built from `Rewrite/Sources/Body-Rewrite.conf`.
- `[Map Local]`: built from `Rewrite/Sources/Map-Local.conf`.
- `[Script]`: built from `Scripts/` and compatibility scripts in `Rewrite/Sources/Script.conf`.
- `[MITM]`: built from `Rewrite/Sources/MITM.conf`.

## Rule Migration

- Spotify DIRECT rules remain in `Rules/spotify-direct.list`.
- YouTube precise protection rules remain in `Rules/youtube-direct.list`.
- General DIRECT rules remain in `Rules/direct.list`.
- App-clean rules remain in `Rules/app-clean.list`.
- Web advertising and tracking rules remain in `Rules/web-ads.list`.
- General reject rules remain in `Rules/reject.list`.
- Remote `RULE-SET` / `DOMAIN-SET` entries are managed by `Rewrite/Remotes/sources.json`.

## Script Migration

- Spotify scripts remain in `Scripts/spotify.conf`.
- YouTube scripts remain in `Scripts/youtube.conf`.
- Tieba, QQ News, VGTime, app2smile non-Spotify scripts, fmz200 / wool_scripts scripts, and zirawell / R-Store app-clean scripts remain in `Scripts/app-clean.conf`.

## Removed Duplicates

- `scripts/build_module.py` now de-duplicates repeated active and comment/source-marker lines during assembly.
- Repeated build runs no longer accumulate duplicate comments or remote markers.
- Script names are validated as unique during build.

## Removed Invalid Items

- No confirmed invalid rule or script source was removed in this refactor.
- Invalid-source repair remains handled by `scripts/audit_repair_invalid_sources.py` after 2 consecutive confirmed failures.

## Preserved Core Items

- `spotify-json`
- `spotify-proto`
- `youtube.response`
- Spotify Header Rewrite
- Spotify DIRECT whitelist
- YouTube Enhance script
- `#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule`

## Backup and Rollback

- Pre-refactor backup: `backup/Ronghemokuai.before-factory-refactor.sgmodule`
- Current stable backup: `backup/Ronghemokuai.stable.sgmodule`

Rollback method:

1. Copy one of the backup module files over root `Ronghemokuai.sgmodule`.
2. Run core marker checks.
3. Commit the rollback with a clear reason.

## Validation Result

- Root and Release are identical after finalize: yes
- Root / Release diff lines: 0
- Spotify complete: yes
- YouTube complete: yes
- MITM uses `%APPEND%`: yes
- `Scripts/spotify.conf` contains no Tieba / QQ News / VGTime: yes
- `Scripts/youtube.conf` contains no ordinary App scripts: yes
- `Rules/spotify-direct.list` contains no REJECT rules: yes
- `README.md` maintenance links point to existing files: yes
- `docs/BUILD_FLOW.md` is the current source-driven build reference: yes

## Manual Test Items

- Import or update `Ronghemokuai.sgmodule` in Shadowrocket.
- Update modules and scripts.
- Test Spotify playback for skipping.
- Test YouTube playback and YouTube Enhance behavior.
- Test login, payment, verification code, WeChat, Alipay, and banking flows.
