# GrandpaNiu Project State

Last updated: 2026-06-26 12:17 +0800

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
- Every meaningful maintenance task now requires an end-of-task AI self-review before final response, commit, or push.

## Recent Stable State

- Current branch during this formatting pass: `repair/upstream-app-sync`.
- Working tree before this task: clean.
- Current public strategy: Fusion single public module.
- Recent CI observed before this task: Module Factory Build and Pages were green after the previous AI maintenance record commit.
- Current scale after the latest GitHub app expansion: 398 active app source files and 398 generated app module outputs. `Rewrite/Sources/Apps/_TEMPLATE.conf` is an authoring template and is not generated.

## Latest Maintenance Note

2026-06-26 12:17 +0800:

- Synced the local branch to the latest `origin/main` before checking the current repository state.
- Found a real generated-output drift: `scheduled-module-update.yml` and `upstream-app-module-sync.yml` ran the full Builder but did not stage `Android/` and `Windows/`, allowing `Release/Android/branches.json` to diverge from `Android/branches.json`.
- Added `Android` and `Windows` to the generated-output commit paths for scheduled update, upstream app module sync, and watchdog recovery. Upstream app sync rollback now also restores Android and Windows generated outputs.
- Found a second process weakness: `scripts/quality_gate.py` manually rebuilt only part of the release pipeline and could leave `Release/Module.sgmodule` out of sync with `Release/Ronghemokuai.sgmodule`.
- Updated `scripts/quality_gate.py` to use the unified `Rewrite/Generator/Builder.py --profile fusion --release` release pipeline instead of partial manual release steps.
- Added validation so full-Builder workflows must commit Android and Windows outputs, and `Release/Module.sgmodule` must match `Release/Ronghemokuai.sgmodule`.
- Current synchronization check: 398 App sources, 398 Release modules, 0 missing modules, Android canonical rules 957, Android/Release branch manifests identical, and Windows v2rayN routes generated from Android v2rayNG.
- Full quality gate passed. No App rule, MITM, login, payment, banking, captcha, video, or CDN traffic policy was intentionally changed.

2026-06-22 02:33 +0800:

- Audited all Actions runs created on 2026-06-22. Daily Module Update, invalid source repair, upstream candidate collect, Pages, and the failure watcher succeeded.
- Daily invalid rule audit run `27913047570` completed its audit and Fusion build successfully, then failed while publishing because GitHub delayed two scheduled writers into the same minute. The other writer advanced `main`, and the safe rebase correctly refused conflicting generated reports.
- Added a remote cross-workflow maintenance lock under `tools/`. Every workflow that writes generated output now acquires the lock before generation, fast-forwards to current `origin/main`, and releases the lock with ownership verification under `if: always()`.
- Added stale-lock recovery and an integration test using a real local bare Git remote. The test proves a second writer is blocked, then fast-forwards after the first writer publishes and releases the lock.
- Lock helpers live in `tools/`, not `scripts/`, because this repository also contains `Scripts/`; Windows case folding would otherwise create a Linux-only path failure.
- No Rules, App sources, MITM scopes, protected traffic policies, or public module contents were changed. Generated reports and metadata were refreshed by the full quality gate.
- Final validation passed: 21 tests, 398 App modules, 0 empty modules, 17 remote sources with 0 warnings, 14 fresh governance reports, and 0 repository-health blocking issues.
- Remote confirmation passed: Module Factory Build `27913770402`, invalid-rule audit rerun `27913813597`, Pages, and the failure watcher all completed successfully. Issue #249 closed automatically and the lock ref was absent after completion.

2026-06-21 02:58 +0800:

- Added 9 additional GitHub-backed overseas / international app-service cleanup sources from `fmz200/wool_scripts`: AOL, Go.com, Lycos, MacKeeper, New Relic, Openmultimedia, Outlook, Sape, and Yahoo.
- These records are enabled in `Rewrite/Remotes/app-modules.json` with `direct_commit=true`, so daily upstream app module sync will keep them refreshed.
- Added converter protection for `dcapps.disney.go.com` and `seavideo-ak.espn.go.com` so Go.com sync does not publish Disney / ESPN video-core style REJECT lines.
- Intentionally skipped broad high-risk foreign candidates such as Adobe activation/licensing, Apple / Google Safe Browsing, Microsoft CRL, and Amazon AWS core-service rules.
- Build validation passed with `python Rewrite/Generator/Builder.py --profile fusion --release --check`: 398 app modules generated, 0 empty modules, repository validation, profile validation, script aggregation validation, upstream risk gate, Android format check, and governance checks passed.

2026-06-21 00:22 +0800:

- Added 94 GitHub-backed app ad cleanup sources to `Rewrite/Sources/Apps/`.
- New upstream records were added to `Rewrite/Remotes/app-modules.json` so the modules continue to follow daily upstream sync.
- Sources came primarily from `fmz200/wool_scripts`, with `vgtime` from `app2smile/rules` and `bahamut-anime` from `NobyDa/Script`.
- The upstream converter now filters protected login/message/CDN entries `apd-pcdnwxlogin`, `msync-im`, and `ossgw.alicdn.com` when imported as REJECT or forced MITM entries.
- Build validation passed with `python Rewrite/Generator/Builder.py --profile fusion --release --check`: 389 app modules generated, 0 empty modules, repository validation, profile validation, script aggregation validation, upstream risk gate, Android format check, and governance checks passed.

2026-06-20 22:58 +0800:

- Added an AI self-review checklist at `docs/ai/SELF_REVIEW.md`.
- Updated `AGENTS.md` so future agents must review the checklist before final response, commit, or push.
- The self-review requires recording what was not good enough, what was changed to reduce risk, and what should be checked first next time.
- This is a process/documentation-only change; no business rules, generated outputs, Android, Windows, Web, or workflow runtime logic were changed.
- Validation passed: `git diff --check` and `python scripts/validate_repository.py`.

2026-06-20 22:41 +0800:

- Checked current GitHub Actions state after the workflow cleanup push.
- Found the latest `Module Factory Build` failure at commit `660d8aeb`.
- Reproduced the failure in a repository-external worktree under `../_codex_private_logs/GrandpaNiu/`.
- Root cause: `scripts/validate_governance_extensions.py` still required the old `fusion-build-marker: scripts/build_module.py --build --profile fusion` workflow marker and did not accept the new Builder entrypoint.
- Fixed the governance validation to accept `Rewrite/Generator/Builder.py --profile fusion --release` while keeping compatibility with the old marker/build command.
- No rule files, app sources, generated Release files, Android outputs, Windows outputs, Web catalog files, or report outputs were changed in the main worktree.
- Validation passed in the temporary worktree: `python Rewrite/Generator/Builder.py --profile fusion --release --check` and `python scripts/quality_gate.py`.

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

## 2026-06-21 App Source Syntax Hardening

- Added `scripts/validate_app_sources.py` to validate all 398 App source fragments and all 398 generated `Release/Modules/*.sgmodule` files.
- The validator now blocks unsupported sections/actions, malformed rules, duplicate script names, duplicate MITM hostnames, duplicate active lines, remote `data-path`, duplicate status codes, and unescaped Map Local JSON.
- Fixed the upstream converter instead of hand-editing Release outputs. Confirmed fixes cover mixed Rule/rewrite input, Loon redirect ordering, `header-replace-regex`, bare domains, Map Local JSON/status normalization, remote response-body embedding, and duplicate script names.
- Expanded invalid-source discovery to `Rewrite/Sources/Apps/*.conf` while limiting App scanning to actionable source/script URLs and checking unique URLs with bounded concurrency.
- Latest local Builder result: 398 App modules, 0 empty modules, 6097-line Fusion output, 941 Android main rules, and all Builder checks passed.
- Latest full quality gate passed. Static/build checks do not prove every App's runtime behavior; real Shadowrocket device behavior remains owner-tested and must drive any future traffic-rule change.

- Keep AI maintenance records updated on every change.
- Keep Markdown files readable with normal headings, lists, tables, and fenced command blocks.
- Prefer source-first fixes instead of direct Release edits.
- Keep Fusion public entry stable.
- Continue using risk reports before narrowing or expanding MITM.
- Treat user-reported app breakage as evidence for targeted rollback or protection rules.

## 2026-06-21 Automation Hardening

- The quality gate now runs script aggregation and bundle sandbox checks after the final profile rebuild.
- Report freshness is enforced with `--strict`; a blocking stale report can no longer be published behind a successful exit code.
- All nine maintenance workflows use isolated `module-maintenance-${{ github.workflow }}-${{ github.ref }}` concurrency groups so unrelated jobs cannot cancel each other.
- Push validation is owned by `Module Factory Build`; scheduled maintenance workflows no longer duplicate that push trigger.
- Generated commits are handled by `scripts/commit_generated_changes.sh` with explicit paths and fetch/rebase/retry.
- Maintenance automation no longer uses `git reset --hard` or `git add -A`.
- The commit helper has a local bare-repository integration test proving that unstaged unrelated files are not published.
- Failure Issue Markdown is generated by Python instead of an expanding shell heredoc, preserving backticks and recovery commands.
- Latest validation: 20 tests passed, 398 App modules built with 0 empty modules, 17 remote sources checked with 0 warnings, and the full quality gate passed.
