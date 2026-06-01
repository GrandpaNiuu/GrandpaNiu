# Contribution and Maintenance Rules

This repository is a personal Shadowrocket / Surge module factory. Changes must keep the project source-first, auditable, and reversible.

## Source-First

Do not maintain generated module files by hand. Update source files first:

- Rules: `Rules/*.list`
- Scripts: `Scripts/*.conf`
- Rewrite and MITM fragments: `Rewrite/Sources/*.conf`
- Profiles: `Rewrite/Profiles/*.conf`
- Remote sources and candidates: `Rewrite/Remotes/*.json`

Then rebuild and validate generated outputs.

## Stable Boundary

- `GrandpaNiu / Ronghemokuai.sgmodule` is the default Stable build.
- `Stable Plus` is a testing profile and must not be merged into Stable as a whole.
- `Lite` is for low-power use and troubleshooting.
- `Full` is for temporary gap checks only and should not be used long term.

Only one version should be enabled at a time.

## Rules

- Add low-risk rules to the appropriate source layer.
- High-risk rules involving images, CDN, HTTPDNS, login, payment, verification, banking, WeChat media, or mini-program resources must stay in manual review or Stable Plus testing first.
- Do not delete rules in bulk. Prefer comment, report, and rollbackable changes.
- Do not use short links, mirror sites, ghproxy, or unknown rule sources as formal sources.

## Scripts

- Unknown scripts are pending by default.
- Obfuscated scripts are blocked.
- Scripts that read or modify Cookie, Token, BoxJS, login state, payment state, member status, account entitlement, encrypted body, protobuf, or binary body require explicit review and manual testing.
- Do not place ordinary App cleanup scripts in Spotify, YouTube, or Zhihu-specific files.

## Required Checks

Run these before submitting changes:

```bash
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_repository.py
python3 scripts/check_report_freshness.py
python3 scripts/repository_health_check.py
```

If `Scripts/app-cleaner.js` changes, also run:

```bash
node --check Scripts/app-cleaner.js
```

## Reports

Update or generate reports that match the change:

- source, scope, affected App, rollback path
- whether Stable is affected
- whether manual device testing is required
- whether the result is tested, untested, or manual-review

Do not write "passed" unless there is a real manual test record.

## Prohibited Content

Do not add:

- membership unlocks or Premium bypasses
- payment bypasses
- login bypasses
- account entitlement spoofing
- Cookie / Token / BoxJS account tasks
- adult, gambling, or grey-market content
- unknown obfuscated scripts
- short links, ghproxy, or unverified mirrors
