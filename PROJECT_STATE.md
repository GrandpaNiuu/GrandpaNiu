# GrandpaNiu Project State

Last updated: 2026-06-20 22:12 +0800

## Project Purpose

GrandpaNiu is a rule construction and advertising cleanup repository for Shadowrocket / Surge style iOS modules, Android rule formats, and Windows v2rayN routing.

The main output is a Fusion `.sgmodule` plus derived Android, Windows, Web, and report artifacts.

This repository is high risk. Rule, script, MITM, or routing mistakes can break:

- app login
- payment or banking flows
- captcha and verification
- video playback
- image and CDN loading
- normal domestic or overseas app connectivity

## Current Main Functions

- Build one public iOS Fusion module.
- Maintain app-scoped rewrite, rule, and script fragments under `Rewrite/Sources/Apps/`.
- Maintain shared protection and cleanup layers under `Rewrite/Sources/Misc/` and `Rules/`.
- Aggregate compatible scripts into `Scripts/generated/fusion-script-bundle.js`.
- Sync eligible upstream app modules through `Rewrite/Remotes/app-modules.json`.
- Generate Android outputs for Mihomo, sing-box, AdGuard, and v2rayNG.
- Generate Windows v2rayN custom routing output.
- Generate Web catalog and GitHub Pages entry files.
- Generate governance reports for script aggregation, MITM scope, rule overlap, upstream risk, repository health, and workflow health.

## Public Entries

Primary public iOS entries:

- `Ronghemokuai.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Module.sgmodule`

Public Web and catalog entries:

- `import.html`
- `redirect.html`
- `android.html`
- `Web/index.html`
- `Web/catalog.md`
- `Web/release-links.json`

Android and Windows public outputs:

- `Release/Android/`
- `Android/mihomo/`
- `Android/sing-box/`
- `Android/adguard/`
- `Android/v2rayng/`
- `Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json`

## Version Strategy

The current strategy is Fusion single-module first.

Do not reintroduce Stable, Lite, Full, Aggressive, or similar public user-facing variants unless the owner explicitly changes the strategy.

Legacy profiles may remain for compatibility or history, but README, import pages, default workflows, health checks, and release reports should point to Fusion as the main public route.

## Important Directory Structure

- `Rules/`: source rule lists and converted remote lists.
- `Scripts/`: JavaScript scripts, script configs, and generated script bundle.
- `Rewrite/Generator/`: wrapper builder and generator config.
- `Rewrite/Sources/`: editable module source fragments.
- `Rewrite/Sources/Apps/`: app-scoped source fragments.
- `Rewrite/Sources/Misc/`: shared source layers for generic ads, CDN/direct protection, finance protection, video protection, analytics, and HTTPDNS.
- `Rewrite/Remotes/`: upstream source registry and app module sync registry.
- `Rewrite/Profiles/fusion.conf`: default build profile.
- `Android/`: editable Android rule source outputs and app branches.
- `Windows/v2rayN/`: v2rayN-specific routing output and docs.
- `Release/`: generated release outputs; do not edit directly unless proven non-generated.
- `Web/`: generated/static GitHub Pages catalog and entry docs.
- `reports/`: generated health, validation, and governance reports.
- `tools/`: governance and validation tools.
- `.github/workflows/`: automation for build, daily update, health, upstream sync, and issue reporting.

## Build Method

Preferred build command:

```bash
python Rewrite/Generator/Builder.py --profile fusion --release --check
```

Full quality gate:

```bash
python scripts/quality_gate.py
```

Useful targeted checks:

```bash
python scripts/validate_repository.py
python scripts/repository_health_check.py
python tools/validate_script_aggregation.py
python tools/test_script_bundle_sandbox.py
python tools/validate_upstream_risk_gate.py
python scripts/android_format_check.py
```

## Testing Method

Use local validation for syntax, generated output consistency, repository health, workflow text, Android format, script aggregation, and upstream risk gate.

Real app end-to-end testing is currently performed manually by the owner and is not automated.

## Known Risks

- Broad MITM hostnames can affect login, payment, banking, captcha, image/CDN, and media playback.
- Aggressive reject rules can break domestic and overseas app connectivity.
- Upstream module auto-sync can import incompatible rewrites if the risk gate is weakened.
- Script aggregation can cause blank pages or hangs if `$done` handling regresses.
- Future rule changes should be evidence-led: use real app abnormal behavior, logs, captures, or another reproducible signal before source-first single-rule adjustments.
- Android formats cannot fully reproduce iOS Rewrite / MITM / Script behavior.
- Generated files under `Release/`, `Web/`, `reports/`, and `Scripts/generated/` can be overwritten by the builder.
- AI maintenance documents must stay readable; collapsed Markdown can cause future agents to misunderstand safety rules.

## Recent Stable State

- Current branch during this formatting pass: `repair/upstream-app-sync`.
- Working tree before this task: clean.
- Current public strategy: Fusion single public module.
- Recent CI observed before this task: Module Factory Build and Pages were green after the previous AI maintenance record commit.
- Approximate scale from the initial snapshot: 297 app source files and 295 generated app module outputs.

## Latest Maintenance Note

2026-06-20 22:12 +0800:

- Current worktree was clean before this pass.
- Local branch was ahead of `origin/main` by 1 commit before this pass.
- A read-only repository health review was completed before editing.
- Legacy four-version documentation was rewritten or marked as deprecated / legacy reference.
- Workflow commit staging was narrowed from broad `git add -A` to explicit path lists.
- Several workflow build paths were moved toward `Rewrite/Generator/Builder.py --profile fusion --release`.
- No rule files, generated Release files, Android outputs, Windows outputs, Web catalog files, reports, or script implementation files were intentionally changed.
- Evidence-first rule maintenance was recorded: future rule changes need real app abnormal behavior, logs, captures, or another reproducible signal.
- Lightweight validation passed: `git diff --check`, workflow text scan, Python compile of validation scripts and Builder, and `python scripts/validate_repository.py`.

2026-06-20 21:40 +0800:

- This pass only formats AI maintenance records and `.gitignore`.
- No business code, rule files, generated outputs, Android outputs, Windows outputs, Web files, reports, or workflow logic are intentionally changed.
- The current worktree diff was checked and only includes `.gitignore`, `AGENTS.md`, `PROJECT_STATE.md`, `AI_HANDOFF.md`, and `docs/ai/*`.
- Validation was run in a repository-external temporary copy under `../_codex_private_logs/GrandpaNiu/` to avoid persisting generated Release/report changes in the main worktree.
- `python scripts/quality_gate.py`, `python scripts/validate_repository.py`, and `python scripts/repository_health_check.py` passed in that temporary copy.

## Next Recommendations

- Keep AI maintenance records updated on every change.
- Keep Markdown files readable with normal headings, lists, tables, and fenced command blocks.
- Prefer source-first fixes instead of direct Release edits.
- Keep Fusion public entry stable.
- Continue using risk reports before narrowing or expanding MITM.
- Treat user-reported app breakage as evidence for targeted rollback or protection rules.
