# GrandpaNiu AI Handoff

Last updated: 2026-07-16 00:15 +08:00

## 2026-07-15 Strict Equivalent MITM Compaction Handoff

- The owner approved reducing MITM hostname tokens only through strict semantic equivalence.
- `scripts/build_module.py` now enables `allow_equivalent_compaction` with matcher contract `shadowrocket-mitm-suffix-wildcard-v1` for the final Fusion output.
- The active optimization removes exact tokens covered by an existing canonical wildcard; it never synthesizes or removes a wildcard.
- Conservative exclusions remain in output:
  - root domains
  - force-keep tokens
  - positive tokens overlapping a negative hostname token
  - IPs, ports, partial wildcards, `?` patterns, and other non-exact tokens
- Final result is `1234 -> 1189` unique hostname tokens with wildcard count unchanged at `34`.
- Every removal records exact-token source and covering-wildcard source in `reports/mitm_optimization_report.json`.
- If contract validation fails, the compiler restores the complete unique baseline and records fallback; fallback tests verify the final removed count becomes zero.
- The independent validator reconstructs the baseline and force-keep set from Fusion sources and checks negative conflicts, exact-token eligibility, retained order, non-MITM fingerprints, and full fallback restoration.
- `tools/build_mitm_baseline.py` now reads only local MITM sources plus the generated module's effective feature sections; it does not run script aggregation or network-backed build stages.
- Full Builder `--release --check` and full quality gate passed; `398` App modules remain non-empty and Android / Windows generation remains healthy.
- Final repository test count is `57`.
- Remote confirmation: implementation commit `e5eec5a5`, successful Module Factory Build `29431450140`, successful Pages deploy `29431556288`, and synchronized generated follow-up `c8d043a8`.

Next AI must not add new broad wildcards to reduce token count. Further reduction requires another explicit contract and must retain fail-closed behavior.

## 2026-07-10 Conservative MITM Compiler Handoff

- Owner requested a conservative, provable, default automatic MITM optimization stage that coexists with existing automation.
- Implemented in `scripts/build_module.py` as final `[MITM]` compile behavior.
- The implementation does not rewrite `Script`, `URL Rewrite`, `Header Rewrite`, `Body Rewrite`, `Map Local`, or `Rule` sections.
- The implementation does not modify `Rewrite/Sources/` source fragments.
- Default output mode is `normalize`:
  - exact duplicate MITM hostname tokens are removed
  - normalized hostname set remains equal to baseline
  - wildcard-covered exact subdomains are not removed
  - hosts without parsed consumers are not removed
  - opaque dynamic dependencies keep their original MITM range
- Range reduction remains disabled unless all proof conditions are satisfied. The current report records `34` wildcards kept because matcher proof/reduction proof is insufficient for shrinking.
- New files:
  - `tools/build_mitm_baseline.py`
  - `tools/validate_mitm_coverage.py`
  - `tests/test_mitm_optimizer.py`
  - `reports/mitm_optimization_report.json`
  - `reports/mitm_optimization_report.md`
- Validation wiring was added to:
  - `scripts/quality_gate.py`
  - `scripts/check_report_freshness.py`
  - `scripts/validate_repository.py`
  - `scripts/repository_health_check.py`
  - `tools/generate_automation_gap_report.py`
  - `tools/generate_automated_quality_evidence.py`
- Important implementation detail: `tools/validate_mitm_coverage.py` validates the report against `Release/Ronghemokuai.sgmodule` and then marks the MITM reports as validated. This avoids Windows sub-second mtime ordering causing false stale freshness failures.
- Full `python scripts/quality_gate.py` passed.

Next AI should not interpret `baseline_uncovered_feature_count` as a new regression. It records pre-existing deep features whose extracted hosts were not covered by the baseline MITM set; the optimizer is required not to make that worse.

## 2026-07-06 Pages Deploy Retry Hardening Handoff

- Owner reported another red workflow after the 2026-07-04 Pages trigger-noise repair.
- Latest failed run inspected:
  - `Deploy GitHub Pages` run `28755590928`
  - Head SHA `8768cb715126b4cab41543962bacdf1266d80c22`
  - Beijing time 2026-07-06 05:32
  - Triggered by successful `Daily schedule watchdog` run `28755580529`
- Job steps showed:
  - `detect-pages-source`: success
  - checkout/configure/prepare/upload artifact: success
  - `Deploy to GitHub Pages`: failure
- Full logs were not accessible through the unauthenticated API because GitHub requires repository admin rights for job log download, but job-step metadata isolated the failure to the official Pages deployment action after a successful artifact upload.
- Repair:
  - `pages-deploy.yml` now retries Pages deployment up to three times.
  - Each retry waits and uploads a unique Pages artifact before calling `actions/deploy-pages@v5` again.
  - The job remains red only if all three attempts fail.
  - `validate_repository.py`, `repository_health_check.py`, and `generate_automation_gap_report.py` now require the retry structure.
  - `check_automation_status.py` and workflow health wording no longer mention direct/public-path push deploy.
- Validation:
  - Full `python scripts\quality_gate.py` passed after the change.
- Next AI should confirm the first post-push `Deploy GitHub Pages` run on the new commit. Older red runs on `8768cb7` remain historical evidence, not proof the new retry guard failed.

## 2026-07-04 Pages Deploy Red-Cross Repair Handoff

- Owner reported new red crosses after the previous repair.
- Latest failed runs were not module build failures; they were `Deploy GitHub Pages` failures during the daily maintenance window.
- Failing job logs showed:
  - Pages backend deployment failure after artifact upload.
  - duplicate `github-pages` artifacts when a workflow was rerun.
  - one cancellation from the Pages concurrency group.
- `pages-deploy.yml` was too broad: it listened to many high-frequency `workflow_run` completions in addition to push/manual triggers.
- Repair made Pages deployment less noisy:
  - keep workflow dispatch
  - keep workflow_run only for `Module Factory Build` and final `Daily schedule watchdog`
  - remove direct push deploy so a push and its generated-output follow-up do not create two Pages deployments
  - remove workflow_run triggers for daily module update, invalid rule audit, invalid source audit, scheduled module update, upstream app sync, upstream collect, and repository health
  - use `github-pages-${{ github.run_attempt }}` for upload/deploy artifact name
- Validation now fails if those high-frequency Pages triggers or direct push deploy are reintroduced.
- Full quality gate passed after the repair.
- Second-layer fix serializes Pages runs with `cancel-in-progress: false`.
- Next AI should verify the next remote `Deploy GitHub Pages` run for this new commit, and should not judge the repair by older red runs on previous SHAs.

## 2026-07-03 Pages Workflow Source Stabilization Handoff

- After the governance commit, `Module Factory Build` succeeded and generated follow-up commit `9e19eec6`.
- The repository still had legacy branch Pages publishing enabled, and the internal `pages build and deployment` failed on `9e19eec6`.
- The repository Pages setting was changed through GitHub API / CLI to `build_type=workflow`.
- Manual reruns against the same `9e19eec6` still failed because the Pages deployment ID/status was tied to that old pages build version.
- `.github/workflows/pages-deploy.yml` was updated to:
  - trigger on `docs/**`
  - use `actions/deploy-pages@v5`
- Next AI should confirm the Pages run on the next commit SHA, not the old `9e19eec6` deployment.

## 2026-07-03 GitHub Maintainer Lessons Implementation Handoff

- Owner asked to apply the recommendations from `reports/github_maintainer_lessons_report.md` into the repository.
- Implemented the safe, automation-friendly recommendations:
  - upstream provenance report
  - platform compatibility matrix
  - protected traffic ledger
  - false-positive review queue
  - converter fixture tests for source conversion compatibility
- New tools:
  - `tools/generate_upstream_provenance_report.py`
  - `tools/generate_platform_compatibility_matrix.py`
  - `tools/generate_protected_traffic_ledger.py`
  - `tools/generate_false_positive_review_report.py`
- New generated reports:
  - `reports/upstream_provenance_report.md`
  - `reports/platform_compatibility_matrix.md`
  - `reports/protected_traffic_ledger.md`
  - `reports/false_positive_review_report.md`
- New test:
  - `tests/test_converter_fixtures.py`
- The new reports are blocking freshness/health evidence now, not manual side notes.
- `quality_gate.py` passed after the new reports and tests were wired in.
- One remote-rule source emitted a transient SSL EOF warning during validation; it did not block the gate and should be treated as upstream/network availability unless repeated.
- Do not treat the false-positive review report or protected traffic ledger as automatic deletion instructions. They are triage maps for source-first, evidence-backed future changes.
- No traffic rules, App source fragments, MITM scopes, Android routing policy, Windows routing policy, workflow runtime behavior, or public module URLs were intentionally changed.

Next AI should first check whether the remote `Module Factory Build` run after this commit is green, then inspect the new governance reports before making any protected traffic changes.

## 2026-07-03 Report Encoding And MITM/REJECT Ledger Handoff

- Owner reported the newest `upstream-app-module-sync.yml` run is green and asked to fix report Chinese mojibake plus create a MITM/REJECT risk ledger.
- File-level UTF-8 checks showed generated reports are valid UTF-8 even when PowerShell displays Chinese as mojibake.
- Added `tools/check_report_encoding.py` and `reports/report_encoding_report.md`; the final scan reports `乱码命中数：0`.
- Added `tools/generate_mitm_reject_risk_ledger.py` and `reports/mitm_reject_risk_ledger.md`.
- The ledger is informational only: it lists source paths and risk categories without deleting, commenting, replacing, or widening rules.
- Added `reports/github_maintainer_lessons_report.md` with GitHub public-repo practices to learn from: upstream trust tiers, license/provenance, compatibility matrices, converter fixtures, and false-positive review loops.
- Wired the new reports into `scripts/quality_gate.py`, `scripts/check_report_freshness.py`, `scripts/repository_health_check.py`, `tools/generate_automation_gap_report.py`, `tools/generate_automated_quality_evidence.py`, and both `Rewrite/Generate.conf` files.
- Validation passed:
  - `python -m py_compile ...`
  - `node --check Scripts/generated/fusion-script-bundle.js`
  - `python tools/validate_script_aggregation.py`
  - `python tools/test_script_bundle_sandbox.py`
  - `python tools/generate_mitm_scope_report.py`
  - `python tools/generate_mitm_reject_risk_ledger.py`
  - `python scripts/generate_app_status_matrix.py`
  - `python tools/generate_automation_gap_report.py`
  - `python scripts/repository_health_check.py`
  - `python scripts/check_report_freshness.py --strict`
  - `python tools/check_report_encoding.py`
  - `python tools/generate_automated_quality_evidence.py`
  - `python scripts/validate_repository.py`
- Full `python scripts\quality_gate.py` passed after the focused validations.
- An earlier quality-gate run recorded one transient remote warning for `ACL4SSR BanAD`, but the final post-rebase full quality gate completed with 0 remote-rule warnings.
- Final report encoding scan passed after the full gate.
- Generated script bundle changed only in generation timestamp / manifest cache metadata because one Kelee script was recovered from cache after a transient SSL EOF.
- Next AI should not treat the new ledger as an instruction to delete rules. It is a review map.

## 2026-07-03 QuanX Converter Fallback Handoff

- `quality_gate.py` exposed that `scripts/convert_quanx_rules.py` could still fail daily automation on a transient zirawell SSL EOF.
- The converter now raises `FetchError` for fetch/read failures and keeps the existing converted output when it exists and is non-empty.
- Missing first-time converted output remains a hard failure.
- Added `tests/test_quanx_converter.py`.
- Full quality gate passed after the converter fallback.
- Next AI should treat this as an operational fallback only; conversion incompatibilities after a successful fetch should still fail.

## 2026-07-03 Pages Source-Mode Guard Handoff

- Push of `52efbde8` confirmed `Module Factory Build` success.
- The same push triggered two Pages paths:
  - GitHub default `pages build and deployment`: success
  - repository self-managed `Deploy GitHub Pages`: failure
- The self-managed Pages workflow now starts with a `detect-pages-source` job.
- It calls the GitHub Pages repository API and only runs `actions/deploy-pages` when `build_type` is `workflow`.
- If the repository remains in branch Pages mode or the Pages settings API cannot be read, the workflow skips self-managed deploy and relies on the default Pages deployment path.
- Next AI should not remove the Pages workflow. It is a guarded standby path for when repository Settings -> Pages is switched to GitHub Actions.

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

## Latest 2026-07-16 Maintenance Pass

- Added test-backed protected-route compilation in `scripts/build_module.py`.
- The first draft would have suppressed 95 REJECT rules because broad protection suffixes were treated as universal; it was rejected before publication.
- Final logic is deliberately narrow and suppresses 9 provable conflicts only: exact Amap image/config, Meituan layout, Baidu map location, and `wxs.qq.com` coverage duplicates.
- `Rules/direct.list` is the editable source for the four newly explicit protection contracts; generated Release files were refreshed only through Builder.
- Final module sections other than `[Rule]` are unchanged against the previous generated module.
- Daily invalid-rule automation now runs source-first repair, rebuilds Fusion, then performs a report-only final-output URL audit.
- Pages deployment failures now open/update the same automation-failure Issue flow as other core workflows.
- Local validation passed: 64 tests, Builder `--check`, full quality gate, 398/398 App modules, 0 empty, Android 952.
- Remote confirmation is complete: Module Factory `29435573074`, Pages `29435658218`, manually dispatched daily invalid-rule audit `29435750405`, and failure watcher `29435804401` all passed; no automation-failure Issue remains open.
