# GrandpaNiu AI Handoff

Last updated: 2026-06-22 02:33 +0800

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
- Latest app expansion added 9 more overseas / international GitHub-backed app-service cleanup sources, bringing `Rewrite/Sources/Apps/` and `Release/Modules/` to 398 active modules.
- New app sync records are direct-commit enabled in `Rewrite/Remotes/app-modules.json`, so the added app modules are covered by the daily upstream app module sync workflow.
- `scripts/sync_upstream_app_modules.py` now filters `apd-pcdnwxlogin`, `msync-im`, and `ossgw.alicdn.com` out of imported REJECT / forced MITM lines.
- `scripts/sync_upstream_app_modules.py` also filters `dcapps.disney.go.com` and `seavideo-ak.espn.go.com` out of imported REJECT lines to avoid Go.com / Disney / ESPN playback-core false positives.

## Current Foreign App Expansion Pass

Scope:

- Added these GitHub-backed overseas / international sources from `fmz200/wool_scripts`:
  - AOL
  - Go.com
  - Lycos
  - MacKeeper
  - New Relic
  - Openmultimedia
  - Outlook
  - Sape
  - Yahoo
- Registered all 9 in `Rewrite/Remotes/app-modules.json` with `enabled=true` and `direct_commit=true`.
- Regenerated Fusion, Release Modules, Android, Windows v2rayN, Web catalog, checksums, and reports through the Builder.
- Did not add broad unsafe candidates containing activation/licensing, Safe Browsing, Microsoft CRL, Amazon AWS core service, VIP/member unlock, payment bypass, login bypass, or token/cookie rewriting behavior.

Validation:

- `python -m py_compile scripts/sync_upstream_app_modules.py scripts/build_release_modules.py Rewrite/Generator/Builder.py` passed.
- `python scripts/sync_upstream_app_modules.py --no-kelee --id ...` synced the 9 selected modules with 0 blocked modules and 0 errors.
- `python Rewrite/Generator/Builder.py --profile fusion --release --check` passed with 398 generated app modules and 0 empty modules.

## Previous App Expansion Pass

Scope:

- Added app-scoped sources from trusted GitHub upstreams:
  - `fmz200/wool_scripts`
  - `app2smile/rules`
  - `NobyDa/Script`
- Refreshed generated Fusion, Release Modules, Android, Windows v2rayN, Web catalog, checksums, and reports through the Builder.
- No VIP/member unlock, payment bypass, login bypass, token/cookie rewriting, or account-sharing modules were intentionally added.

Validation:

- `python -m py_compile scripts/sync_upstream_app_modules.py scripts/build_release_modules.py Rewrite/Generator/Builder.py` passed.
- `python Rewrite/Generator/Builder.py --profile fusion --release --check` passed with 389 generated app modules and 0 empty modules.

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

## Current CI Repair Pass

- Latest failed workflow checked: `Module Factory Build` run `27873963030`, commit `660d8aeb`.
- Failure was reproduced outside the main worktree with `python Rewrite/Generator/Builder.py --profile fusion --release --check`.
- Root cause was stale governance validation: `scripts/validate_governance_extensions.py` required the old `fusion-build-marker` workflow comment and rejected the new Builder entrypoint.
- Fix keeps the old marker/build command as a compatibility option and adds `Rewrite/Generator/Builder.py --profile fusion --release` as the preferred governance signal.
- Temporary worktree validation passed: Builder release check and full `scripts/quality_gate.py`.

## Current Risk Points

## Current App Source Syntax Hardening Pass

- Reproduced independent module syntax defects that the old Fusion-only validator did not see.
- Added an App source/release validator and connected it to both Generator configs, Builder `--check`, the full quality gate, repository health, report freshness, governance, and automated evidence.
- Re-synced only 17 affected App sources from their registered upstream URLs. High-risk RedNote, Weibo, and Zhihu sources were backed up under `backup/upstream-app-modules/` before replacement.
- The final source and Release scan covers 398 + 398 files with 3806 active entries on each side and reports 0 syntax errors.
- Main Fusion output has no duplicate script names or MITM hostnames and Root/Release/alias outputs are generated through Builder.
- Do not claim all Apps are device-verified. Static validation proves syntax/build consistency; runtime networking, login, payment, images, and video still require actual client evidence.

- Do not weaken the upstream risk gate to force in unsafe modules.
- Do not assume all newly added upstream snippets are device-verified; they passed syntax/build/governance checks, but real app behavior remains owner-tested.
- If one new app breaks login, images, video, or normal networking, disable or narrow that app source first rather than reverting the whole expansion.
- Do not directly edit `Release/Ronghemokuai.sgmodule` or `Release/Module.sgmodule`; regenerate them.
- Do not casually change MITM hostnames for payment, banking, login, video playback, or image/CDN.
- Do not reintroduce multi-version public user routes unless the owner explicitly requests a version strategy change.
- Do not remove Android or Windows outputs while cleaning iOS module logic.
- Do not collapse AI maintenance Markdown into long single-line text.
- Run the end-of-task self-review in `docs/ai/SELF_REVIEW.md` before final response, commit, or push.

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
7. Read `docs/ai/SELF_REVIEW.md`.
8. Read the latest entries in `docs/ai/WORKLOG.md`.
9. Run:

```bash
git status
git branch --show-current
```

10. Only then decide whether to modify files.

## Latest Automation Hardening Pass

### 2026-06-22 Cross-Workflow Writer Lock

- Today only `Daily invalid rule audit and safe repair` run `27913047570` failed; its audit and Fusion build passed, and only the publish step failed.
- Evidence shows GitHub delayed it into the same minute as Daily Module Update. Both started from `c15ff4f5`; Daily Module Update published `c96c5e53`, then the audit publisher refused a generated-output rebase conflict.
- All nine workflows that write `main` now call `tools/acquire_automation_lock.sh` before generation and `tools/release_automation_lock.sh` with `if: always()` after publishing.
- The lock uses an atomic remote ref, ownership-checked release, stale-lock recovery, and a fast-forward to current `origin/main` after acquisition.
- Keep the existing per-workflow GitHub concurrency groups. They prevent duplicate runs of one workflow; the remote lock handles collisions between different workflows without GitHub cancelling pending jobs.
- Do not move these helpers under lowercase `scripts/`: Windows cannot safely distinguish that path from the existing uppercase `Scripts/` directory when creating new files.
- Full quality gate passed with 21 tests. No traffic rules or public module content changed.

First check next time: confirm the next scheduled invalid-rule audit succeeds and that automation-failure Issue #249 closes automatically.

- Fixed a reproducible false-green quality gate: freshness reported blocking stale script reports while the command still exited successfully.
- Moved script aggregation validation and sandbox execution after the last profile rebuild and enabled strict freshness enforcement.
- Replaced duplicated workflow commit loops with `scripts/commit_generated_changes.sh`.
- All maintenance workflows use isolated `module-maintenance-${{ github.workflow }}-${{ github.ref }}` groups after remote run #555 proved that one global group cancels older pending workflows.
- `Module Factory Build` is the only push-validation entrypoint; daily audit and scheduled update remain schedule/manual workflows.
- Removed `git reset --hard` and broad `git add -A` from maintenance automation.
- Added tests for ordering, workflow safety contracts, and a real local push through the commit helper.
- Fixed `workflow-failure-issue.yml` so Markdown backticks and recovery commands are not erased by shell command substitution.
- No traffic rules or protected App paths were changed.

First check next time: inspect the GitHub Actions runs triggered by the automation-hardening commit, especially `Module Factory Build`.
