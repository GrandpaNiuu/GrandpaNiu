# GrandpaNiu AI Handoff

Last updated: 2026-06-20 22:12 +0800

## What This Project Is

GrandpaNiu is a Fusion-first Shadowrocket / Surge module factory with Android and Windows routing outputs.

It builds advertising cleanup rules, rewrite layers, script layers, MITM hostnames, app modules, Web catalog files, and governance reports.

Maintain it as a high-risk network rules repository. Small changes can break user connectivity, app login, payment, video playback, or image/CDN loading.

## Current Public Strategy

- iOS public strategy: one Fusion module.
- Primary public entries:
  - `Ronghemokuai.sgmodule`
  - `Release/Ronghemokuai.sgmodule`
  - `Release/Module.sgmodule`
- Do not restore Stable, Lite, Full, Aggressive, or other public multi-version choices without explicit owner approval.

## Recent Completed Work

- Fusion single public module strategy established.
- `Rewrite/Generator/Builder.py` wraps the existing build scripts.
- App sources were split into `Rewrite/Sources/Apps/`.
- Shared layers were added under `Rewrite/Sources/Misc/`.
- Android outputs were expanded across Mihomo, sing-box, AdGuard, and v2rayNG.
- Windows v2rayN custom routing output was added.
- Upstream app module sync was added through `Rewrite/Remotes/app-modules.json`.
- Script aggregation was introduced through `Scripts/generated/fusion-script-bundle.js`.
- Governance gates were added for script aggregation, script bundle sandbox testing, upstream app module risk, MITM scope, rule overlap, and app-cleaner active state.
- AI maintenance records were added and then reformatted for readability.

## Current Formatting Pass

The earlier formatting pass was documentation-only and passed validation in a repository-external temporary copy.

Allowed files for this pass:

- `.gitignore`
- `AGENTS.md`
- `PROJECT_STATE.md`
- `AI_HANDOFF.md`
- `docs/ai/TASKS.md`
- `docs/ai/DECISIONS.md`
- `docs/ai/RISK_LOG.md`
- `docs/ai/WORKLOG.md`

Do not touch business logic as part of this pass.

Validation commands run in the temporary copy:

```bash
python scripts/quality_gate.py
python scripts/validate_repository.py
python scripts/repository_health_check.py
```

All three commands passed. The main worktree remains limited to `.gitignore` and AI maintenance records.

## Current Maintenance Pass

Scope:

- AI records updated to note the completed read-only health review.
- Old four-version docs now state Fusion single-module strategy and mark legacy variants as deprecated / reference only.
- Workflow staging was narrowed from `git add -A` to explicit paths.
- Selected workflows now call `Rewrite/Generator/Builder.py --profile fusion --release` instead of manually chaining `build_module.py`, `factory_finalize.py`, and `build_release_variants.py`.
- Rule files are intentionally untouched.
- Lightweight validation passed for this pass: `git diff --check`, workflow text scan, Python compile of validation scripts and Builder, and `python scripts/validate_repository.py`.

Important: `reject_risk_report.md` still lists bank/payment, CDN, and domestic core API REJECT risks. These are documented in `docs/ai/RISK_LOG.md` as pending review; do not change them without Shadowrocket logs or owner-confirmed app behavior.

Rule maintenance rule: only make source-first single-rule changes when there is real app abnormal behavior, client logs, packet captures, or another reproducible signal. Follow every such change with the full quality gate.

## Current Risk Points

- Do not weaken the upstream risk gate to force in unsafe modules.
- Do not directly edit `Release/Ronghemokuai.sgmodule` or `Release/Module.sgmodule`; regenerate them.
- Do not casually change MITM hostnames for payment, banking, login, video playback, or image/CDN.
- Do not reintroduce multi-version public user routes unless the owner explicitly requests a version strategy change.
- Do not remove Android or Windows outputs while cleaning iOS module logic.
- Do not collapse AI maintenance Markdown into long single-line text.

## Current Unfinished Tasks

- Keep reports current after every generator or rules change.
- Continue monitoring user-reported real app behavior manually.
- Use `reports/rule_overlap_report.md` as a guide for future dedupe, but do not auto-delete overlaps without risk review.
- Use `reports/mitm_scope_report.md` as a guide for narrowing MITM only when supported by breakage evidence.
- Keep `.gitignore` protecting local private logs and local-only notes.

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
4. Read `docs/ai/TASKS.md`.
5. Read `docs/ai/DECISIONS.md`.
6. Read `docs/ai/RISK_LOG.md`.
7. Read the latest entries in `docs/ai/WORKLOG.md`.
8. Run:

```bash
git status
git branch --show-current
```

9. Only then decide whether to modify files.
