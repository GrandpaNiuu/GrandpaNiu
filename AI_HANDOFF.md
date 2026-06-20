# GrandpaNiu AI Handoff

Last updated: 2026-06-20 11:58 +0800

## What This Project Is

GrandpaNiu is a Fusion-first Shadowrocket / Surge module factory with Android and Windows routing outputs. It builds advertising cleanup rules, rewrite layers, script layers, MITM hostnames, app modules, Web catalog files, and governance reports.

The project should be maintained as a high-risk network rules repository. Small changes can break user connectivity, app login, payment, video playback, or image/CDN loading.

## Recent Completed Work

- Fusion single public module strategy established.
- `Rewrite/Generator/Builder.py` wraps the existing build scripts.
- App sources were split into `Rewrite/Sources/Apps/`.
- Shared layers were added under `Rewrite/Sources/Misc/`.
- Android outputs were expanded across Mihomo, sing-box, AdGuard, and v2rayNG.
- Windows v2rayN custom routing output was added.
- Upstream app module sync was added through `Rewrite/Remotes/app-modules.json`.
- Script aggregation was introduced through `Scripts/generated/fusion-script-bundle.js`.
- Governance gates were added for:
  - script aggregation validation
  - script bundle sandbox testing
  - upstream app module risk gate
  - MITM scope reporting
  - rule overlap reporting
  - app-cleaner active reporting

## Recent Files Touched Before This Snapshot

- `scripts/build_module.py`
- `scripts/quality_gate.py`
- `scripts/check_report_freshness.py`
- `scripts/repository_health_check.py`
- `Rewrite/Generate.conf`
- `Rewrite/Generator/Generate.conf`
- `Rewrite/Registry.md`
- `Rewrite/Remotes/app-modules.json`
- `Scripts/generated/fusion-script-bundle.js`
- `tools/*`
- `reports/*`

## Current Risk Points

- Do not weaken the upstream risk gate to force in unsafe modules.
- Do not directly edit `Release/Ronghemokuai.sgmodule` or `Release/Module.sgmodule`; regenerate them.
- Do not casually change MITM hostnames for payment, bank, login, video playback, or image/CDN.
- Do not reintroduce multi-version public user routes unless the owner explicitly requests a version strategy change.
- Do not remove Android / Windows outputs while cleaning iOS module logic.

## Current Unfinished Tasks

- Keep reports current after every generator or rules change.
- Continue monitoring user-reported real app behavior manually.
- Use `reports/rule_overlap_report.md` as a guide for future dedupe, but do not auto-delete overlaps without risk review.
- Use `reports/mitm_scope_report.md` as a guide for narrowing MITM only when supported by breakage evidence.

## Files And Directories Not To Change Casually

- `Ronghemokuai.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Module.sgmodule`
- `Rewrite/Profiles/fusion.conf`
- `Rewrite/Generator/Builder.py`
- `Rewrite/Generator/Generate.conf`
- `Rewrite/Generate.conf`
- `Rewrite/Manifest.conf`
- `Rewrite/Remotes/app-modules.json`
- `Scripts/generated/fusion-script-bundle.js`
- `Scripts/generated/fusion-script-bundle.manifest.json`
- `.github/workflows/`
- `Android/`
- `Windows/v2rayN/`

Generated files may change through the builder; avoid hand-editing them.

## First Step For A New AI

1. Read `AGENTS.md`.
2. Read `PROJECT_STATE.md`.
3. Read this file.
4. Read `docs/ai/TASKS.md`, `docs/ai/DECISIONS.md`, `docs/ai/RISK_LOG.md`, and the latest entries in `docs/ai/WORKLOG.md`.
5. Run `git status` and `git branch --show-current`.
6. Only then decide whether to modify files.
