# App Cleaner Active Report

- Generated at: 2026-08-21 01:04:15 +0800
- Active entry file: `Scripts/app-cleaner-active.conf`
- Cleaner script: `Scripts/app-cleaner.js`
- Cleaner version: `2026-05-31-dispatcher-v3-safe-generic`
- Config mode: `shadow`
- Config groups: 1
- Default action: `passThrough`
- Active entries: 1

## Active Entries

| Name | Type | Requires body | Pattern alternatives | Script path |
|---|---|---:|---:|---|
| `app-cleaner-active-json-clean` | `http-response` | 1 | 67 | `https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Scripts/app-cleaner.js` |

## Safety Contract

- Unknown URLs, invalid JSON, media URLs and unexpected bodies pass through unchanged.
- Login, token, payment, bank, captcha and membership keywords stay in the forbidden keyword list.
- This report is generated; update source files or generator logic instead of editing the report.
