# GrandpaNiu AI Handoff

Last updated: 2026-07-03 04:13 +08:00

## 2026-07-03 Upstream App Sync Automation Repair Handoff

- Current automation failure focus: `upstream-app-module-sync.yml`.
- Other required daily workflows were reported successful in the latest local automation status report; the remaining blocking workflow was upstream App module sync.
- Root causes reproduced locally:
  - transient upstream fetch failures were hard failures
  - KFC upstream emitted an invalid `.\cn` regex escape
  - first-import Kelee records could stay enabled without a generated source file
- The synchronizer now skips transient fetch/convert failures without failing the whole daily run:
  - existing local source present: publish the existing source unchanged and retry later
  - target source missing: mark the record disabled / not direct-commit and retry later through Kelee fill modes
  - risk-gate blocks still fail the run
- A temporary worktree reproduced the exact daily sync command chain successfully after the fix, including the Builder `--check` path.
- `check_automation_status.py` now avoids blocking the repository on an already-fixed older-commit failure when there is a fresh successful run and the current commit is newer. It still blocks failures on the current commit.
- Next AI should not claim the remote `upstream-app-module-sync.yml` is green until a new GitHub Actions run after this commit is observed. The local workflow reproduction is green.

## 2026-07-03 Pages Deploy Queue Repair Handoff

- The screenshot failure was a Pages deployment queue timeout: `deployment_queued` repeated until `actions/deploy-pages` hit its 10 minute timeout and cancelled the deployment.
- The repository now has `.github/workflows/pages-deploy.yml` as an explicit self-managed GitHub Pages deployment workflow.
- The workflow builds a constrained `_site` artifact instead of relying on the default branch-root Pages deployment.
- It sets `actions/deploy-pages` inputs:
  - `timeout: 600000`
  - `reporting_interval: 10000`
  - `error_count: 30`
- It uses `concurrency: pages-deploy-main` with `cancel-in-progress: true`, so older Pages deploy attempts do not keep the latest deploy queued.
- Validation now checks the Pages workflow through:
  - `scripts/validate_repository.py`
  - `scripts/repository_health_check.py`
  - `tools/generate_automation_gap_report.py`
  - `scripts/generate_workflow_health_report.py`
  - `scripts/check_automation_status.py`
- No Rules, Rewrite sources, MITM scopes, script behavior, Android routing policy, Windows routing policy, or public module URLs were intentionally changed.
- Operational follow-up: if GitHub Settings -> Pages still says "Deploy from a branch", switch it to **GitHub Actions** so the old default Pages deployment stops running.

## 2026-07-03 Full Repository Health Refresh Handoff

- Latest local base before this pass: `b2606a4f Build module factory outputs [skip ci]`.
- Full local quality gate passed and refreshed generated outputs to `# update-date: 2026-07-03`.
- Main Fusion remains `2775` lines with the final rule tail:
  - `GEOIP,CN,DIRECT`
  - `FINAL,PROXY`
- App module coverage remains `398` source files and `398` generated Release modules with `0` empty modules.
- The standalone strict freshness check can fail if it is run immediately after only `Rewrite/Generator/Builder.py --profile fusion --release --check`; the full `scripts/quality_gate.py` refreshes App status and automation gap reports in the correct order and then passes.
- Local `gh run list --limit 12` failed with a timeout to `198.18.0.26:443`, so remote Actions could not be confirmed from this machine.
- No rule source, MITM scope, script logic, Android routing policy, Windows routing policy, workflow, or Builder logic was intentionally changed in this pass.
- Next AI should start by checking whether remote Actions are reachable, then use `python scripts/quality_gate.py` for any generated-output refresh.

## 2026-07-02 Fusion Rewrite Compaction Handoff

- Main Fusion line count is now `2775`.
- Compaction lives in `scripts/build_module.py` and is controlled by `Rewrite/Profiles/fusion.conf` with `compact_rewrite_sections = true`.
- Do not hand-edit compressed output; change source fragments or generator behavior, then rebuild.
- The compressor intentionally does not merge `302`, `307`, `header`, script-path, or mixed-operation rewrite lines.
- Body Rewrite compaction only merges URL patterns when the body operation is byte-identical.
- Map Local compaction only merges URL patterns when the payload/status/header operation is byte-identical.
- `scripts/validate_module_integrity.py` compiles generated regex patterns and should remain in the quality gate.
- `tests/test_module_compaction.py` protects against losing the URL Rewrite ` - reject` suffix.
- A KFC source regex typo was fixed at `Rewrite/Sources/Apps/kfc.conf`.

## 2026-07-02 Compact Network Split Handoff

- Owner reported real network errors after the previous no-routing main Fusion policy.
- Current main iOS Fusion policy:
  - strip scattered `DIRECT` / `PROXY` source rules from generated output
  - append only `GEOIP,CN,DIRECT`
  - append only `FINAL,PROXY`
- This is implemented source-first:
  - `Rewrite/Profiles/fusion.conf`: `strip_direct_proxy_rules = true` and `compact_network_split = true`
  - `scripts/build_module.py`: strips old route policies, then appends compact network split
  - `scripts/validate_repository.py`: only allows those two routing lines and requires them as the final two active `[Rule]` entries
- Main iOS public entries now contain 1 `DIRECT` and 1 `PROXY` policy, both at the end of `[Rule]`.
- Do not re-add the old scattered protection lines unless owner requests a more granular policy. If a Chinese App still fails, check whether `GEOIP,CN,DIRECT` is insufficient for a domain-first route; if an overseas App still fails, check the user's Shadowrocket policy group named `PROXY`.

## 2026-07-02 Main Fusion Routing Strip Handoff

- Owner explicitly confirmed: remove `DIRECT` and `PROXY` rules from the main Fusion module, keep ad-blocking rules, and do not change Android/Windows.
- Implementation is source-first:
  - `Rewrite/Profiles/fusion.conf`: `strip_direct_proxy_rules = true`
  - `scripts/build_module.py`: strips `DIRECT` / `PROXY` rule policies from generated Fusion `[Rule]`
  - `scripts/validate_repository.py`: fails if generated root Fusion `[Rule]` contains `DIRECT` or `PROXY`
- Source protection files are not deleted. Examples that remain as sources:
  - `Rules/direct.list`
  - `Rules/protect-login.list`
  - `Rules/protect-payment.list`
  - `Rules/protect-video.list`
  - `Rules/protect-cdn.list`
  - `Rewrite/Sources/Misc/*`
- Android and Windows generated outputs were intentionally not touched by this policy change.
- Current iOS public entries have no `DIRECT` or `PROXY` policy in `[Rule]`.
- Risk boundary: this can reduce stability for login, payment, banking, video playback, image/CDN loading, HTTPDNS, and overseas services. If runtime breakage appears, restore by disabling `strip_direct_proxy_rules` or adding a narrower generated-output exception.

## 2026-07-02 Automation Gap Closeout Handoff

- Local worktree was synchronized with `origin/main`; latest remote commit is `5d80bf41 Build module factory outputs [skip ci]`.
- The automation gap guard commit is published as `54a5421f codex: add automation gap guard`.
- The follow-up generated-output commit `5d80bf41` was created by automation after the guard landed.
- `Module Factory Build` run `28565310634` is green:
  - job `build`: `completed / success`
  - `Run full automated quality gate`: `success`
  - `Commit generated files`: `success`
  - `Release cross-workflow maintenance lock`: `success`
- Current `origin/main` reports:
  - `reports/automation_gap_report.md`: `Blocking gaps: 0`
  - `reports/repository_health_report.md`: `Blocking issues: 0`
- This closeout intentionally changed only AI maintenance records.
- Next AI should start from `origin/main` and avoid re-running the full Builder unless a business change or generated-output check requires it.

## 2026-07-02 Automation Gap Hardening Handoff

- Added a new blocking automation gap report at `reports/automation_gap_report.md`.
- The script lives in `tools/generate_automation_gap_report.py`, not `scripts/`, because this Windows worktree has both `Scripts/` and `scripts/`; creating new lowercase `scripts/` files can land in the wrong directory on case-insensitive filesystems.
- The check is wired into:
  - `Rewrite/Generator/Generate.conf`
  - `Rewrite/Generate.conf`
  - `scripts/quality_gate.py`
  - `scripts/check_report_freshness.py`
  - `scripts/validate_repository.py`
  - `scripts/repository_health_check.py`
  - `tools/generate_automated_quality_evidence.py`
- Full `python scripts/quality_gate.py` passed after the `tools/` path fix.
- Remote rule checks produced transient SSL EOF warnings during validation, but no blocking syntax failure.
- This pass intentionally did not implement upstream replacement scoring or App feedback ingestion.
- No traffic-policy source files were intentionally changed.

## 2026-07-02 Automation Repair Handoff

- Reproduced the current automation failure locally with `python Rewrite/Generator/Builder.py --profile fusion --release --check`.
- Fixed stale Fusion governance validation in `scripts/validate_governance_extensions.py`.
- Rewrote `docs/PROFILE_POLICY.md` to match the current Fusion-only release strategy and generated-output boundaries.
- Full local quality gate now passes.
- Required scheduled workflows are reported `ok` in `reports/automation_status_report.md`; the latest push-validation failure predates this repair and should be rechecked after push.
- No traffic-policy source files were intentionally changed.

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

- 2026-06-26: Added unattended automation status checks and hardened script aggregation against transient upstream JS fetch failures.
- `scripts/check_automation_status.py` writes `reports/automation_status_report.md` and checks required scheduled workflows for recent successful runs.
- `daily-schedule-watchdog.yml` now always writes the automation status report and runs strict stale/failure validation, even when the Fusion module date is already fresh.
- `scripts/quality_gate.py`, `scripts/check_report_freshness.py`, `scripts/validate_repository.py`, `scripts/repository_health_check.py`, automated evidence, and tests now know about the automation status check.
- `scripts/build_module.py` now caches low-risk aggregated JS sources in `Scripts/generated/fusion-script-bundle.cache.json` and can recover sources from the previously committed bundle/manifest before reaching out to upstreams.
- `tools/validate_script_aggregation.py` validates the script source cache so transient upstream failures do not silently shrink the public script bundle.
- 2026-06-26: Repaired generated-output synchronization after a current-state self-check.
- `scheduled-module-update.yml`, `upstream-app-module-sync.yml`, and `daily-schedule-watchdog.yml` now stage `Android/` and `Windows/` whenever they run the full Builder.
- `upstream-app-module-sync.yml` rollback now restores `Android/` and `Windows/` in addition to iOS, Release, Web, and reports.
- `scripts/quality_gate.py` now calls the unified Builder release pipeline instead of partially rebuilding release artifacts by hand.
- `scripts/validate_repository.py` now blocks a stale `Release/Module.sgmodule` alias and blocks full-Builder workflows that do not commit Android/Windows outputs.
- `scripts/repository_health_check.py` reports and blocks Release alias drift.
- Validation confirmed: root iOS module, Release iOS module, and Release alias are identical; Android source and Release branch manifests are identical; 398 App sources generate 398 Release modules; Windows v2rayN output is generated from Android v2rayNG.
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
- `Scripts/generated/fusion-script-bundle.cache.json`
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

Remote confirmation is complete: Module Factory Build `27913770402` and invalid-rule audit rerun `27913813597` succeeded, Pages succeeded, Issue #249 closed automatically, and no lock ref remained.

First check next time: inspect the next naturally scheduled writer set for successful lock waiting when GitHub delays multiple schedules together.

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
