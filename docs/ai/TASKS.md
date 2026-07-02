# AI Maintenance Tasks

Last updated: 2026-07-03 04:13 +08:00

## Current Upstream App Sync Automation Repair Task

Status: locally implemented and fully validated; pending commit, push, and remote Actions confirmation.

Scope:

- Repair failing daily automation without changing App ad rules, MITM scopes, Android routing, Windows routing, or public module entries.
- Focus on `upstream-app-module-sync.yml`, because the latest automation status report showed that workflow as the only required daily blocker.
- Keep risk-gated upstream modules blocking when truly unsafe; only downgrade transient fetch/convert failures to retryable skips.

Validation:

- `python -m unittest tests.test_app_source_conversion tests.test_automation_status` passed with 11 tests.
- `python -m py_compile scripts\sync_upstream_app_modules.py scripts\check_automation_status.py tests\test_app_source_conversion.py tests\test_automation_status.py` passed.
- Temporary worktree exact workflow reproduction passed:
  - `python scripts\sync_upstream_app_modules.py`
  - `python scripts\protect_douyin_connectivity_sources.py`
  - `python Rewrite\Generator\Builder.py --profile fusion --release --check`
- `python scripts\quality_gate.py` passed in the main worktree.

Next check:

- Commit and push the repair.
- Confirm the next `upstream-app-module-sync.yml` run after the repair commit is green.
- If it fails again, inspect whether it is a new risk-gate block, a new converter syntax defect, or GitHub/network availability.

## Current Pages Deploy Queue Repair Task

Status: locally implemented and fully validated; local commit prepared; pending remote Pages deployment confirmation.

Scope:

- Fix the GitHub Pages deploy failure shown in the screenshot where deployment remained `deployment_queued` until timeout.
- Do not change ad rules, App sources, MITM scopes, scripts, Android routing policy, Windows routing policy, or public module URLs.
- Add a self-managed Pages deployment workflow with a smaller static artifact, maximum supported deploy timeout, and stale deploy cancellation.
- Add validation so the Pages deployment guard cannot silently disappear.

Validation:

- Python compile passed for changed scripts.
- Workflow YAML parsed successfully.
- `python scripts/validate_repository.py` passed.
- `python scripts/repository_health_check.py` passed.
- `python tools/generate_automation_gap_report.py` passed.
- `python scripts/quality_gate.py` passed.

Next check:

- Push the repair and confirm the new `Deploy GitHub Pages` workflow runs.
- If the old default Pages deployment still appears, switch repository Settings -> Pages -> Source to **GitHub Actions**.

## Current Full Repository Health Refresh Task

Status: committed and pushed as `5f0545f1`; remote Actions visibility was limited by local GitHub API timeout during that pass.

Scope:

- Run a broad repository and module syntax/build health check.
- Do not add new App modules or broad new rules.
- Do not change rule sources, MITM scopes, script behavior, Android routing policy, Windows routing policy, workflows, or Builder logic unless a real failure is reproduced.
- Refresh generated outputs only through the normal Builder / quality gate.
- Repair stale AI maintenance records found during the pass.

Validation:

- Python compile passed through `compileall` for `scripts/`, `tools/`, and `Rewrite/Generator/Builder.py`.
- `node --check Scripts/app-cleaner.js` passed.
- `node --check Scripts/generated/fusion-script-bundle.js` passed.
- `python -m unittest discover -s tests` passed with 28 tests.
- `python scripts/validate_module_integrity.py` passed.
- `python scripts/validate_app_sources.py` passed for 398 source files and 398 release modules.
- `python Rewrite/Generator/Builder.py --profile fusion --release --check` passed.
- `python scripts/quality_gate.py` passed.

Known limitation:

- `gh run list --limit 12` failed locally with a timeout to `198.18.0.26:443`; remote Actions status still needs confirmation when GitHub API access works.

## Current Fusion Rewrite Compaction Task

Status: complete and published. Local generated-output follow-up is currently refreshed again by the 2026-07-03 quality gate.

Scope:

- Reduce main Fusion line count toward roughly 3000 while preserving ad-cleaning behavior and the compact China/overseas network split.
- Do not remove functional rules to hit the target.
- Use conservative equivalent compaction:
  - same URL Rewrite reject action suffix
  - same Body Rewrite operation
  - same Map Local response operation

Validation:

- `python -m py_compile scripts\build_module.py scripts\validate_module_integrity.py tests\test_module_compaction.py` passed.
- `python -m unittest tests.test_module_compaction` passed.
- `python Rewrite\Generator\Builder.py --profile fusion --release --check` passed.
- `python scripts\quality_gate.py` passed.
- Main public iOS entries are `2775` lines and keep final rules `GEOIP,CN,DIRECT` / `FINAL,PROXY`.

Next check:

- Watch for real Shadowrocket runtime issues with combined rewrite regexes.
- If an App-specific rewrite stops matching, inspect the relevant combined line before changing source rules.

## Current Compact Network Split Task

Status: complete and published. Local generated-output follow-up is currently refreshed again by the 2026-07-03 quality gate.

Scope:

- Restore stable network routing in the main iOS Fusion module after real user-reported network errors.
- Keep ad-blocking rules first.
- Do not restore scattered protection / routing lists into the public module.
- Use one compact split:
  - `GEOIP,CN,DIRECT`
  - `FINAL,PROXY`

Validation:

- `python -m py_compile scripts\build_module.py scripts\validate_repository.py scripts\validate_module_integrity.py scripts\validate_app_sources.py` passed.
- `python scripts\build_module.py --build --profile fusion` passed.
- `python scripts\factory_finalize.py --sync-root` passed.
- `python scripts\build_release_aliases.py --config Rewrite\Generator\Generate.conf` passed.
- `python scripts\validate_module_integrity.py` passed.
- `python scripts\validate_app_sources.py` passed.
- `python scripts\validate_repository.py` passed.
- `python scripts\repository_health_check.py` passed.
- `python scripts\check_report_freshness.py --strict` passed.
- Main iOS public entries have exactly 1 `DIRECT` and 1 `PROXY` policy, as the final two active rules.

Next check:

- If a Chinese App still fails, check whether it uses overseas CDN/IPs that fall through to `FINAL,PROXY`.
- If an overseas App still fails, confirm the user's Shadowrocket `PROXY` policy group exists and works.

## Current Main Fusion Routing Strip Task

Status: superseded by the compact network split after real network errors were reported.

Scope:

- Remove `DIRECT` and `PROXY` rule policies from the generated main iOS Fusion module only.
- Keep source protection files intact for rollback and non-iOS projections.
- Keep Android and Windows unchanged by policy.
- Preserve `REJECT`, rewrite, script, Map Local, and MITM ad-cleaning behavior.

Validation:

- `python -m py_compile scripts\build_module.py scripts\validate_repository.py` passed.
- `python scripts\build_module.py --build --profile fusion` passed.
- `python scripts\factory_finalize.py --sync-root` passed.
- `python scripts\build_release_aliases.py --config Rewrite\Generator\Generate.conf` passed.
- `python scripts\validate_module_integrity.py` passed.
- `python scripts\validate_repository.py` passed.
- `python scripts\repository_health_check.py` passed.
- `python scripts\check_report_freshness.py --strict` passed.
- Main iOS public entries have 0 `DIRECT` and 0 `PROXY` policies in `[Rule]`.

Next check:

- Confirm the next `Module Factory Build` run is green after publishing.

## Current Automation Gap Hardening Task

Status: complete and remotely confirmed.

Scope:

- Add a blocking automation gap report for generated-output synchronization, workflow writer wiring, platform parity, app module coverage, script aggregation cache presence, and report availability.
- Wire the report into Builder `--check`, the full quality gate, report freshness, repository validation, repository health, and automated quality evidence.
- Keep upstream replacement scoring and App feedback ingestion out of this pass per owner instruction.
- Do not change traffic rules, App source rules, MITM scopes, Android routing policy, Windows routing policy, or public entry names.

Validation:

- `python Rewrite/Generator/Builder.py --profile fusion --release --check` passed.
- `python scripts/quality_gate.py` passed.
- `python scripts/validate_repository.py` passed.
- Commit `54a5421f codex: add automation gap guard` was pushed to `main`.
- Automation generated follow-up commit `5d80bf41 Build module factory outputs [skip ci]`.
- `Module Factory Build` run `28565310634` completed successfully.

Closed with:

- `reports/automation_gap_report.md`: `Blocking gaps: 0`
- `reports/repository_health_report.md`: `Blocking issues: 0`

## Current Automation Repair Task

Status: complete and remotely confirmed.

Scope:

- Align governance validation with the current Fusion-only policy.
- Remove stale policy wording that made `quality_gate.py` fail after old multi-profile artifacts were retired.
- Keep traffic rules, App sources, Android, Windows, and public module entries unchanged except for generated outputs refreshed by the Builder.

Validation:

- `python Rewrite/Generator/Builder.py --profile fusion --release --check` passed.
- `python scripts/quality_gate.py` passed.
- `python scripts/validate_repository.py` passed.
- `python scripts/repository_health_check.py` passed.
- Published repair is on `main`; the later `Module Factory Build` run `28565310634` succeeded.

Closed with:

- Required scheduled workflows are `ok` in the latest automation status report.
- Push validation is green on the confirmed `Module Factory Build` run.

## Active Rules For Task Handling

- Keep Fusion as the only primary public iOS module.
- Prefer source-first edits under `Rules/`, `Rewrite/Sources/`, `Rewrite/Remotes/`, `Scripts/`, `Android/`, `Windows/v2rayN/`, and `tools/`.
- Do not directly edit generated Release outputs unless the task is explicitly about generated artifact repair and the source path is understood.
- Update AI records after each meaningful maintenance change.
- Keep AI maintenance Markdown readable; do not collapse headings, lists, tables, or command blocks into single-line text.
- Before final response, commit, or push, run the self-review checklist in `docs/ai/SELF_REVIEW.md`.

## Current Open Tasks

- Watch the next `Daily schedule watchdog` run. It should publish `reports/automation_status_report.md` and fail only for real stale/failed required scheduled workflows.
- Watch the next full Builder run on GitHub Actions and confirm `Scripts/generated/fusion-script-bundle.cache.json` keeps script aggregation stable when upstream JS fetches are flaky.
- Watch the next scheduled update and upstream app sync runs. They should now publish `Android/` and `Windows/` together with `Release/`.
- If a future check reports Release alias drift, inspect whether a script bypassed `Rewrite/Generator/Builder.py --profile fusion --release`.
- Monitor the next naturally delayed group of scheduled writers and confirm waiting jobs acquire the lock in sequence.

- Monitor future user-reported app breakage and fix with targeted source changes.
- Keep upstream app module sync governed by `tools/validate_upstream_risk_gate.py`.
- Keep script aggregation governed by validation and sandbox reports.
- Use MITM and rule overlap reports for future narrowing or dedupe, but avoid automatic deletions without review.
- Keep Android and Windows outputs aligned with iOS source rules where technically possible.
- Preserve local-only logging rules in `.gitignore`.
- Review the high-risk REJECT checklist before changing any login, payment, banking, CDN, video, or domestic core API rules.
- Only perform source-first single-rule adjustments when real app abnormal behavior, logs, captures, or another reproducible signal exists; then run the full quality gate.
- Continue moving workflow build steps toward `Rewrite/Generator/Builder.py --profile fusion --release`.
- Keep the AI self-review checklist current when new process weaknesses are found.
- For newly added GitHub app modules, fix future breakage by disabling or narrowing the specific `Rewrite/Sources/Apps/<slug>.conf` and its `Rewrite/Remotes/app-modules.json` record first.
- For future foreign app expansion, keep rejecting broad platform rules that touch activation/licensing, Safe Browsing, certificate revocation, AWS/cloud core services, payment, login, or account authorization paths.

## Current App Source Syntax Hardening Task

Status: locally implemented and fully validated; pending commit, push, and CI confirmation.

Scope:

- Validate all App source fragments and generated per-App modules, not only the final Fusion module.
- Fix reproducible conversion defects at `scripts/sync_upstream_app_modules.py`.
- Keep Release outputs generated by Builder.
- Expand invalid-source audit coverage without making the daily job serial or unbounded.

Validation:

- 14 unit tests passed.
- `python scripts/validate_app_sources.py` passed for 398 source files and 398 release modules.
- `python Rewrite/Generator/Builder.py --profile fusion --release --check` passed with 398 modules and 0 empty modules.
- `python scripts/quality_gate.py` passed.

Remaining runtime boundary:

- Do not change connectivity rules without a real App failure, Shadowrocket log, packet capture, or another reproducible runtime signal.

## Current Foreign App Expansion Task

Status: locally generated and validated; pending commit, push, and CI confirmation.

Scope:

- Added 9 overseas / international app-service sources from `fmz200/wool_scripts`.
- Registered the new sources for daily direct upstream sync.
- Added converter-level protection for Go.com Disney / ESPN video-core false positives.
- Regenerated Fusion, Release, Android, Windows, Web, and reports through the Builder.

Validation:

- `python -m py_compile scripts/sync_upstream_app_modules.py scripts/build_release_modules.py Rewrite/Generator/Builder.py` passed.
- `python Rewrite/Generator/Builder.py --profile fusion --release --check` passed with 398 generated app modules and 0 empty modules.

## Current Self-Review Process Task

Status: validated; pending commit and push.

Scope:

- Add a reusable end-of-task self-review checklist.
- Require future worklogs to include what was not good enough, what was improved, and what should be checked first next time.
- Do not modify business rules, generated outputs, Android, Windows, Web, or workflow runtime logic.

Validation:

- `git diff --check` passed.
- `python scripts/validate_repository.py` passed.

## Current CI Repair Task

Status: fixed locally and validated; pending commit and push.

Scope:

- Repair the failed `Module Factory Build` caused by stale governance workflow-token validation.
- Do not modify rules, app sources, generated outputs, Android, Windows, Web, or reports in the main worktree.

Validation:

- `python -m py_compile scripts/validate_governance_extensions.py scripts/validate_repository.py scripts/repository_health_check.py Rewrite/Generator/Builder.py` passed.
- `python scripts/validate_governance_extensions.py` passed.
- `python scripts/validate_repository.py` passed.
- In the repository-external worktree, `python Rewrite/Generator/Builder.py --profile fusion --release --check` passed.
- In the repository-external worktree, `python scripts/quality_gate.py` passed.

## Current Formatting Task

Status: committed locally in `225817bb`; not yet pushed to remote when this pass started.

Scope:

- Restore readable Markdown structure for AI maintenance records.
- Restore `.gitignore` to normal multi-line ignore rules.
- Do not modify rules, scripts, generated outputs, Android, Windows, Web, reports, or workflows.
- Do not commit unless the owner explicitly asks.

Validation:

- `python scripts/quality_gate.py` passed in a repository-external temporary copy.
- `python scripts/validate_repository.py` passed in a repository-external temporary copy.
- `python scripts/repository_health_check.py` passed in a repository-external temporary copy.
- Main worktree diff still only contains `.gitignore` and AI maintenance records.

## Current Documentation And Workflow Cleanup

Status: validated; owner approved commit and push.

Scope:

- Mark old four-version docs as Fusion-first with deprecated / legacy references only.
- Document the current read-only health review result.
- Convert broad workflow `git add -A` usage to explicit path lists.
- Move selected workflow build steps to the Builder entrypoint.
- Do not modify rules or generated outputs in this pass.

Pending risk review checklist is recorded in `docs/ai/RISK_LOG.md`.

Validation:

- `git diff --check` passed.
- Workflow text scan found no `git add -A` and confirmed Builder usage where expected.
- `python -m py_compile scripts/validate_repository.py scripts/repository_health_check.py Rewrite/Generator/Builder.py` passed.
- `python scripts/validate_repository.py` passed.
- Full build was not run in the main worktree because this pass intentionally avoids refreshing generated outputs.

## Backlog

- Improve documentation around which outputs are generated versus editable sources.
- Add more focused tests for protected traffic categories if stable fixtures become available.
- Add clearer report summaries for non-technical maintainers.
- Review empty or legacy rule files periodically, but avoid deleting compatibility files without tracing references.
- Add a future report that groups app modules by upstream project and highlights modules that have not been device-tested yet.

## Current Automation Hardening Task

Status: locally implemented and fully validated; pending commit, push, and remote Actions confirmation.

Completed scope:

- Make report freshness blocking in the actual quality-gate exit status.
- Validate the final generated script bundle instead of an earlier intermediate bundle.
- Isolate generated-output workflow concurrency by workflow/ref so unrelated jobs cannot cancel each other.
- Keep one push-validation entrypoint in `Module Factory Build`.
- Centralize explicit-path commit and fetch/rebase/retry behavior.
- Remove destructive reset and broad staging from maintenance automation.
- Add regression and local Git integration tests.
- Preserve Markdown and recovery commands in automatically created failure Issues.

Validation:

- 20 unit/integration tests passed.
- All 10 workflow YAML files parsed successfully.
- `bash -n scripts/commit_generated_changes.sh` passed.
- `python Rewrite/Generator/Builder.py --profile fusion --release --check` passed.
- `python scripts/quality_gate.py` passed with strict freshness.
- 398 App modules generated; 0 empty modules; 17 remote sources checked with 0 warnings.

## Done

- 2026-06-26: Added scheduled workflow freshness/status reporting and strict watchdog validation.
- 2026-06-26: Added script aggregation source caching/fallback so transient upstream JS failures do not shrink the public bundle.
- 2026-06-26: Fixed Android/Release generated-output drift by staging Android and Windows in all full-Builder scheduled publishing workflows.
- 2026-06-26: Updated the quality gate to use the unified Builder release pipeline and added regression checks for Release alias and Android/Windows workflow staging.
- 2026-06-20: Initial AI maintenance record system created.
- 2026-06-20: Baseline project state and handoff captured.
- 2026-06-20: Private local log directory initialized outside the repository.
- 2026-06-21: Added 94 GitHub-backed app ad cleanup modules and regenerated Fusion/Release/Web/Android/Windows outputs.
- 2026-06-21: Hardened freshness enforcement and serialized safe generated-output publishing.
- 2026-06-22: Added an ownership-checked remote maintenance lock to serialize all nine generated-output writers across workflows; full quality gate passed with 21 tests.
- 2026-06-22: Remote Module Factory Build and invalid-rule audit rerun passed; Issue #249 closed automatically and no stale lock remained.
