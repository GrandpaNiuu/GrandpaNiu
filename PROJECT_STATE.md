# GrandpaNiu Project State

Last updated: 2026-07-16 02:47 +08:00

## 2026-07-16 Maintenance Stabilization Snapshot

- Daily automation ownership is now explicit:
  - `daily-audit-and-repair.yml` validates the generated Fusion module and writes audit reports only.
  - `daily-invalid-source-repair.yml` owns editable invalid-source repair.
  - `upstream-collect.yml` owns candidate collection.
  - source-maintenance workflows run the full Builder only when their source step reports a real source change.
- Candidate collection commits every target allowed by `collect_upstreams.py`; validation imports the allowed target sets so workflow staging cannot drift from collector capability.
- Workflows that run the quality gate or strict automation status now provide authenticated Actions API access through `GITHUB_TOKEN` and `actions: read`.
- Repository validation and the automation-gap report enforce those ownership boundaries so duplicate repair/build stages cannot silently return.
- Release App-module documentation now reports static capability tiers instead of treating every non-empty module as equally functional:
  - deep: `171`
  - rewrite: `153`
  - rule: `72`
  - MITM-only compatibility fragments: `2`
  - total modules: `398`; empty modules: `0`
- Capability tiers describe generated section depth only. They do not claim that an upstream script still works at runtime or that an App has been device-tested.
- `crunchyroll` and `flightradar24` are the two MITM-only compatibility fragments. No paid-feature or unlock script was imported to make them appear active.
- The MITM / REJECT risk ledger now records whether each source risk is present exactly in the final module, covered by an equivalent final MITM wildcard, or remains source-only / compiler-filtered. Source-only status is not interpreted as proof that a rule is unnecessary.
- The previously corrupted 2026-06-20 through 2026-06-22 WORKLOG block was restored verbatim from clean Git commit `8f8b3029`; later records were preserved.
- Stable is documented as a deprecated compatibility mirror of Fusion. Beta and Canary remain reserved placeholders, not public version choices.
- No `Rules/`, `Rewrite/Sources/`, App scripts, MITM declarations, Android routing policy, Windows routing policy, or public Fusion URL was manually changed in this pass.
- Local validation passed:
  - `78` unit/integration tests
  - Builder `--profile fusion --release --check`
  - full `python scripts/quality_gate.py`
  - Fusion output: `2769` lines
  - App modules: `398/398`, `0` empty
  - Android main rules: `952`
  - automation status: `ok`, `0` blockers, `0` warnings

Local unauthenticated Actions status refresh hit the GitHub API rate limit and correctly degraded to `unknown` without blocking static validation. Remote authenticated confirmation is complete: Module Factory Build `29442515323`, generated follow-up `b15aab68`, Pages `29442610625`, and workflow-failure monitors all passed. The remote automation report is `ok` with `0` blockers and `0` warnings.

## 2026-07-15 Strict Equivalent MITM Compaction Snapshot

- The final Fusion MITM compiler now supports owner-approved semantic-equivalent compaction under the repository matcher contract `shadowrocket-mitm-suffix-wildcard-v1`.
- The compiler removes an exact hostname only when an already-declared canonical `*.example.com` wildcard covers it under the verified contract.
- It does not create, remove, broaden, or narrow wildcard tokens.
- It preserves root domains, force-keep entries, negative hostname conflicts, IP literals, ports, and complex wildcard or pattern tokens.
- No `Rules/`, `Rewrite/Sources/`, App script, Rewrite, Map Local, Android rule policy, Windows routing policy, or public module URL was changed by hand.
- Current generated result:
  - raw hostname declarations: `2059`
  - normalized unique baseline: `1234`
  - final optimized hostname tokens: `1189`
  - exact duplicates removed: `825`
  - semantically redundant exact tokens removed: `45`
  - wildcard count before / after: `34 / 34`
  - fallback: `False`
  - coverage contract: passed
- `tools/validate_mitm_coverage.py` independently rebuilds the baseline and force-keep set from Fusion source files, then verifies every removal, conservative exclusion, source trace, retained order, wildcard set, deep-feature coverage, non-MITM fingerprint, fallback completeness, and generated Release output.
- `tools/build_mitm_baseline.py` is local-only and no longer invokes script aggregation, network access, or unrelated generated writes.
- Full `python scripts/quality_gate.py` passed with `57` tests.
- Published as commit `e5eec5a5`; Module Factory Build `29431450140` and Pages deploy `29431556288` both passed. Generated follow-up `c8d043a8` is synchronized locally.

Boundary: equivalence is asserted under the named repository matcher contract, not as a universal proof of every undocumented client implementation. Any item outside that contract is retained.

## 2026-07-10 Conservative MITM Compiler Snapshot

- Added a conservative final-output MITM compiler stage for the Fusion module.
- Scope is only the generated `[MITM]` hostname output in the final module.
- No `Rules/`, `Rewrite/Sources/Apps/`, `Rewrite/Sources/Misc/`, App scripts, rewrite rules, map-local rules, Android routing policy, Windows routing policy, or public module URL was intentionally changed.
- Default mode is strict equivalent normalization:
  - split `hostname =` lines into tokens
  - normalize case, whitespace, and separators
  - remove exact duplicate tokens only
  - keep wildcard hosts
  - keep exact subdomains even if covered by a wildcard
  - keep hosts without a statically parsed consumer
  - preserve first-seen order
- Wildcard range reduction remains effectively disabled unless matcher semantics and all finite dependencies are machine-proven.
- Fail-closed behavior is implemented: if MITM coverage validation fails, the build falls back to the baseline unique MITM output instead of publishing a partial optimized result.
- New maintained evidence:
  - `reports/mitm_optimization_report.json`
  - `reports/mitm_optimization_report.md`
- New tools:
  - `tools/build_mitm_baseline.py`
  - `tools/validate_mitm_coverage.py`
- New tests:
  - `tests/test_mitm_optimizer.py`
- Current report snapshot:
  - baseline hostname tokens: `2059`
  - baseline unique hostname tokens: `1234`
  - normalized hostname tokens: `1234`
  - exact duplicates removed: `825`
  - wildcard count before / after: `34 / 34`
  - proved wildcard reductions: `0`
  - opaque features retained: `169`
  - baseline-uncovered deep features recorded: `45`
  - fallback: `False`
- Full `python scripts/quality_gate.py` passed after the implementation.

Boundary: this pass reduces duplicated MITM host declarations from accumulated sources. It does not prove every client runtime behavior globally equivalent; it proves the repository's static MITM output contract for parsed features and preserves anything that cannot be proven safe to narrow.

## 2026-07-06 Pages Deploy Retry Hardening Snapshot

- Observed latest red workflow:
  - `Deploy GitHub Pages` run `28755590928`
  - Commit `8768cb715126b4cab41543962bacdf1266d80c22`
  - Beijing time: 2026-07-06 05:32
  - Trigger: `workflow_run` after `Daily schedule watchdog`
- Related daily automation status:
  - `Daily schedule watchdog` succeeded.
  - The generated commit was created successfully.
  - Pages artifact upload succeeded.
  - Only official `actions/deploy-pages` failed.
- Root cause class: GitHub Pages deployment action / backend can still fail transiently even after trigger noise was reduced. The repository was no longer creating many Pages deploys for the same batch, but a single transient Pages deploy failure still made the workflow red.
- Repair:
  - `.github/workflows/pages-deploy.yml` now performs up to three deployment attempts.
  - Attempt 2 and attempt 3 wait before retrying.
  - Retry attempts re-upload `_site` under unique artifact names:
    - `github-pages-${{ github.run_attempt }}-retry-2`
    - `github-pages-${{ github.run_attempt }}-retry-3`
  - The workflow fails only if all deployment attempts fail.
  - Validation scripts now require the retry guard so the workflow cannot silently regress to one fragile deploy attempt.
- Validation:
  - `python -m py_compile ...` passed for touched workflow validation scripts.
  - `python scripts\validate_repository.py` passed.
  - `python tools\generate_automation_gap_report.py` passed.
  - `python scripts\repository_health_check.py` passed.
  - `python scripts\generate_workflow_health_report.py` passed.
  - Full `python scripts\quality_gate.py` passed.
- No Rules, App sources, MITM behavior, routing policy, Android/Windows policy, or public module entry URL was intentionally changed.

## 2026-07-04 Pages Deploy Red-Cross Repair Snapshot

- Observed failure pattern from GitHub Actions:
  - `Deploy GitHub Pages` failed after several Beijing 00:00-02:30 daily workflows.
  - Module factory and daily maintenance workflows themselves were successful.
  - Failure logs showed:
    - `Deployment failed, try again later.`
    - `Multiple artifacts named "github-pages" were unexpectedly found for this workflow run.`
    - one cancellation from Pages deployment concurrency.
- Root cause: `pages-deploy.yml` listened to too many `workflow_run` completions, so a daily maintenance batch could trigger several Pages deployments for nearby commits within minutes.
- Repair:
  - Pages `workflow_run` now listens only to:
    - `Module Factory Build`
    - `Daily schedule watchdog`
  - High-frequency daily workflows no longer trigger Pages deploy directly.
  - Pages artifact names now include `${{ github.run_attempt }}` to prevent duplicate `github-pages` artifact collisions when rerunning a workflow.
  - Validation scripts now block reintroducing the noisy Pages workflow triggers.
- Validation:
  - `python -m py_compile ...` passed for touched validation scripts.
  - `python scripts\generate_workflow_health_report.py` passed.
  - `python tools\generate_automation_gap_report.py` passed.
  - `python scripts\validate_repository.py` passed.
  - `python scripts\repository_health_check.py` passed.
  - Full `python scripts\quality_gate.py` passed.
- No `Rules/`, `Rewrite/Sources/Apps/`, MITM source behavior, Android routing policy, Windows routing policy, or public module URL was intentionally changed.

## 2026-07-03 Pages Workflow Source Stabilization Snapshot

- The repository Pages API was updated from legacy branch Pages publishing to GitHub Actions publishing:
  - previous `build_type`: `legacy`
  - current `build_type`: `workflow`
- This removes the old branch-based `pages build and deployment` path from being the intended publisher.
- `.github/workflows/pages-deploy.yml` now also triggers on `docs/**`, because the Pages artifact includes `docs/`.
- `.github/workflows/pages-deploy.yml` now uses `actions/deploy-pages@v5`.
- No public Pages URL, module URL, rule source, App source, MITM scope, Android output, or Windows output was intentionally changed.

Operational note: a deployment for the old generated commit `9e19eec6` remained failed because GitHub Pages stores the deployment status by pages build version. The next commit should create a new Pages deployment version.

## 2026-07-03 GitHub Maintainer Lessons Implementation Snapshot

- The GitHub maintainer lessons report is no longer just advisory; its safe governance recommendations have been implemented as repository checks.
- Added generated upstream provenance evidence:
  - `tools/generate_upstream_provenance_report.py`
  - `reports/upstream_provenance_report.md`
- Added generated platform compatibility evidence:
  - `tools/generate_platform_compatibility_matrix.py`
  - `reports/platform_compatibility_matrix.md`
- Added generated protected-traffic source ledger:
  - `tools/generate_protected_traffic_ledger.py`
  - `reports/protected_traffic_ledger.md`
- Added generated false-positive review queue:
  - `tools/generate_false_positive_review_report.py`
  - `reports/false_positive_review_report.md`
- Added converter fixture tests at `tests/test_converter_fixtures.py` for upstream module conversion behavior including arguments, loose QuanX rewrite syntax, Loon binary body scripts, Map Local, JQ body rewrite, and Header Rewrite.
- Wired the new reports into:
  - `scripts/quality_gate.py`
  - `scripts/check_report_freshness.py`
  - `scripts/repository_health_check.py`
  - `scripts/validate_repository.py`
  - `tools/generate_automation_gap_report.py`
  - `tools/generate_automated_quality_evidence.py`
  - `Rewrite/Generate.conf`
  - `Rewrite/Generator/Generate.conf`
  - `Web/registry.md`
- `reports/github_maintainer_lessons_report.md` now records the implementation status of these lessons.
- No `Rules/`, `Rewrite/Sources/Apps/`, MITM source behavior, Android routing policy, Windows routing policy, workflow behavior, or public module URL was intentionally changed.
- Full `python scripts\quality_gate.py` passed after implementation.
- Quality gate refreshed:
  - Fusion module: `2775` lines.
  - App sources: `398`.
  - Release App modules: `398`.
  - Empty App modules: `0`.
  - Android main rules: `952`.
  - Remote syntax report: `15` sources, `1` transient upstream warning, `0` normalization files.

Traffic-policy boundary: this pass improves provenance, platform documentation, protected-traffic review, false-positive triage, and converter regression coverage. It does not directly change ad-blocking rules or protected app traffic.

## 2026-07-03 Report Encoding And Risk Ledger Snapshot

- Owner confirmed the latest `upstream-app-module-sync.yml` run is green.
- Added a generated report encoding guard at `tools/check_report_encoding.py`.
- New report `reports/report_encoding_report.md` scans `reports/*.md` through UTF-8 reads and blocks common mojibake markers.
- Added informational MITM / REJECT risk ledger generator at `tools/generate_mitm_reject_risk_ledger.py`.
- New report `reports/mitm_reject_risk_ledger.md` records source path, risk class, risk level, and reason only; it does not change rules.
- Added `reports/github_maintainer_lessons_report.md` summarizing public GitHub repositories and maintainability practices worth learning from.
- Wired the new encoding and MITM/REJECT ledger reports into the local quality gate, freshness checks, repository health, automation-gap report, and automated evidence.
- No `Rules/`, `Rewrite/Sources/Apps/`, MITM source behavior, Android routing, Windows routing, workflows, or public module URLs were intentionally changed.
- Full `python scripts\quality_gate.py` passed after wiring the new reports.
- Final `python tools\check_report_encoding.py` passed with `乱码命中数：0`.

Current generated risk ledger snapshot:

- Source MITM hostnames scanned: `805`.
- MITM risk items marked: `172`.
- REJECT / rewrite reject entries scanned: `4218`.
- REJECT risk items marked: `2817`.
- High-risk items: `73`.
- Medium-risk items: `2916`.

Known documentation issue:

- Historical note: older `docs/ai/WORKLOG.md` entries were once mojibake; the affected block was restored from clean Git history on 2026-07-16.

## 2026-07-03 QuanX Converted Rule Fallback Snapshot

- Full `python scripts\quality_gate.py` initially exposed another automation fragility: `scripts/convert_quanx_rules.py` failed the whole gate when the zirawell upstream returned a transient SSL EOF.
- The converted outputs already existed under `Rules/converted/`, so a temporary upstream fetch failure should not break daily automation.
- `scripts/convert_quanx_rules.py` now keeps existing converted outputs when fetch/UTF-8 read fails and a non-empty local converted file exists.
- If there is no existing converted output, the script still fails, preventing a silently missing rule set.
- Added `tests/test_quanx_converter.py` to protect both fallback and no-existing-output failure behavior.
- Full `python scripts\quality_gate.py` passed after this fix.

Traffic-policy boundary: this preserves existing converted rule outputs during upstream fetch failure; it does not add, remove, or rewrite app rules.

## 2026-07-03 Pages Deploy Source-Mode Guard Snapshot

- After the upstream sync repair was pushed, `Module Factory Build` succeeded on commit `52efbde8`.
- The same push showed `pages build and deployment` success, but the self-managed `Deploy GitHub Pages` workflow failed.
- This means GitHub Pages is still effectively being published by the default branch Pages deployment path, while the self-managed deploy workflow is not safe to auto-run unless repository Pages source is set to GitHub Actions.
- `.github/workflows/pages-deploy.yml` now detects the repository Pages `build_type` first:
  - `build_type == workflow`: run the self-managed `actions/deploy-pages` job
  - any other value or API read failure: skip self-managed deploy and let default branch Pages deployment publish the site
- Validation passed:
  - workflow YAML parse
  - `python scripts\validate_repository.py`
  - `python scripts\repository_health_check.py`
  - `python tools\generate_automation_gap_report.py`
  - `python scripts\generate_workflow_health_report.py`

Traffic-policy boundary: no module rules, App sources, MITM, scripts, Android, Windows, or public import URLs were changed.

## 2026-07-03 Upstream App Sync Automation Repair Snapshot

- Observed current automation failure: `upstream-app-module-sync.yml` failed while other required daily workflows were recently successful.
- Local reproduction in a temporary worktree showed three concrete failure classes:
  - transient upstream SSL EOF / fetch errors were treated as hard sync errors even when a local source file already existed
  - KFC upstream reintroduced an invalid regex escape, `res\.kfc\.com.\cn`, which broke generated rewrite regex validation
  - a newly discovered Kelee module could remain enabled after first-import fetch failure even though its target source file did not exist
- `scripts/sync_upstream_app_modules.py` now:
  - keeps existing local App sources when an upstream fetch or conversion fails temporarily
  - disables first-import records when the target source does not exist yet, then retries them on a later Kelee merge
  - repairs the known KFC `.cn` regex escape during conversion
  - keeps upstream risk blocks as hard failures
- `scripts/check_automation_status.py` now treats a latest failed required run on an older commit as a warning when a fresh success still exists and the current commit is newer. Failures on the current commit remain blocking.
- Validation passed:
  - `python -m unittest tests.test_app_source_conversion tests.test_automation_status`
  - `python -m py_compile scripts\sync_upstream_app_modules.py scripts\check_automation_status.py tests\test_app_source_conversion.py tests\test_automation_status.py`
  - exact workflow reproduction in a temporary worktree: `sync_upstream_app_modules.py` -> `protect_douyin_connectivity_sources.py` -> `Rewrite\Generator\Builder.py --profile fusion --release --check`
  - `python scripts\quality_gate.py`
- Traffic-policy boundary: no App rule source, MITM hostname, login/payment/banking/video/CDN rule, Android routing policy, Windows routing policy, or public module URL was intentionally changed.

## 2026-07-03 GitHub Pages Deploy Queue Repair Snapshot

- Observed failure: GitHub Pages deploy job stayed at `deployment_queued` until `actions/deploy-pages` reached its 10 minute timeout and cancelled the deployment.
- Repository code previously had no explicit `.github/workflows/pages-deploy.yml`; Pages deployment was left to GitHub's default branch-based Pages deployment flow.
- Added a self-managed `Deploy GitHub Pages` workflow:
  - packages only the public static site artifact under `_site`
  - publishes Fusion, Release, Web, Android, Windows, Rules, Scripts, Rewrite/Remotes, docs, and reports
  - uses `.nojekyll`
  - uses `actions/deploy-pages`
  - sets the Pages deploy timeout explicitly to GitHub's supported maximum of `600000` ms
  - uses `pages-deploy-main` concurrency with `cancel-in-progress: true` so stale queued deploys do not block the latest one
- Added validation guards so future checks require the Pages workflow, artifact upload, Pages permissions, and extended deploy timeout.
- Important operational note: GitHub repository Pages settings should use **Source: GitHub Actions**. If Settings -> Pages still uses branch deployment, GitHub can continue launching the old default Pages deployment workflow.
- Validation passed:
  - workflow YAML parse
  - `python scripts/validate_repository.py`
  - `python scripts/repository_health_check.py`
  - `python tools/generate_automation_gap_report.py`
  - `python scripts/quality_gate.py`

## Project Purpose

GrandpaNiu is a source-first rule and module factory for advertising cleanup and routing outputs.

It publishes:

- iOS Shadowrocket / Surge compatible Fusion module output.
- Android rule outputs for Mihomo / Clash Meta, sing-box, AdGuard, and v2rayNG.
- Windows v2rayN custom routing output.
- Per-App release modules.
- Web catalog and GitHub Pages entry files.
- Governance, freshness, risk, coverage, and automation reports.

Treat this repository as high risk. Small rule, rewrite, MITM, script, Android, Windows, or workflow changes can affect login, payment, captcha, video playback, images/CDN, or normal app networking.

## Current Public Entries

Primary iOS public entries:

- `Ronghemokuai.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Module.sgmodule`

Android and Windows outputs remain generated projections:

- `Android/`
- `Release/Android/`
- `Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json`

## Version Strategy

- iOS uses one public Fusion module.
- Stable / Stable Plus / Lite / Full are deprecated legacy references only.
- Do not reintroduce multi-version public routes without explicit owner approval.
- Generated channel aliases under `Release/Stable`, `Release/Beta`, and `Release/Canary` are managed by the Builder and are not a return to old user-facing multi-version selection.

## Editable Source Layers

Prefer source-first edits under:

- `Rules/`
- `Scripts/`
- `Rewrite/Sources/`
- `Rewrite/Remotes/`
- `Rewrite/Profiles/fusion.conf`
- `Android/`
- `Windows/v2rayN/`
- `tools/`
- `.github/workflows/`

Do not directly hand-edit generated outputs unless the source or generator path is understood.

## Generated Layers

Generated or mostly generated outputs include:

- `Ronghemokuai.sgmodule`
- `Release/`
- `Web/`
- `reports/`
- `Scripts/generated/`

Use the Builder or quality gate to refresh these.

## Build Commands

Preferred full release build:

```bash
python Rewrite/Generator/Builder.py --profile fusion --release
```

Preferred full release build plus configured checks:

```bash
python Rewrite/Generator/Builder.py --profile fusion --release --check
```

Full quality gate:

```bash
python scripts/quality_gate.py
```

Important focused checks:

```bash
python scripts/validate_module_integrity.py
python scripts/validate_app_sources.py
python scripts/validate_repository.py
python scripts/repository_health_check.py
python scripts/check_report_freshness.py --strict
```

## Current Stable State

As of 2026-07-03:

- Branch: `repair/upstream-app-sync`, tracking `origin/main`.
- Latest synchronized commit before this pass: `b2606a4f Build module factory outputs [skip ci]`.
- Main iOS Fusion module: `2775` lines.
- App source files: `398`.
- Release App modules: `398`.
- Empty App modules: `0`.
- Aggregated script routes: `52`.
- Main Fusion final routing tail:
  - `GEOIP,CN,DIRECT`
  - `FINAL,PROXY`
- Main iOS public entries are synchronized by the Builder:
  - `Ronghemokuai.sgmodule`
  - `Release/Ronghemokuai.sgmodule`
  - `Release/Module.sgmodule`

## Recent Validation

The 2026-07-03 full local health refresh passed:

```bash
python -c "import compileall, sys; ok=True; ok &= compileall.compile_dir('scripts', quiet=1); ok &= compileall.compile_dir('tools', quiet=1); ok &= compileall.compile_file('Rewrite/Generator/Builder.py', quiet=1); sys.exit(0 if ok else 1)"
node --check Scripts/app-cleaner.js
node --check Scripts/generated/fusion-script-bundle.js
python -m unittest discover -s tests
python tools/validate_script_aggregation.py
python tools/test_script_bundle_sandbox.py
python scripts/validate_module_integrity.py
python scripts/validate_app_sources.py
python Rewrite/Generator/Builder.py --profile fusion --release --check
python scripts/validate_repository.py
python scripts/repository_health_check.py
python scripts/validate_profiles.py
python scripts/validate_remote_rule_syntax.py
python scripts/validate_governance_extensions.py
python scripts/quality_gate.py
```

`python scripts/check_report_freshness.py --strict` failed immediately after a standalone Builder run because `app_status_matrix` and `automation_gap` had not yet been refreshed in quality-gate order. The full `python scripts/quality_gate.py` run refreshed them and passed strict freshness.

Local GitHub API access failed during:

```bash
gh run list --limit 12
```

The failure was a timeout to `198.18.0.26:443`, so remote Actions status could not be confirmed from this machine during the pass.

## Recent Important Changes

### 2026-07-02 Fusion Rewrite Compaction

- Main iOS Fusion module was compacted from `5953` lines to `2775` lines.
- `Rewrite/Profiles/fusion.conf` enables `compact_rewrite_sections = true`.
- `scripts/build_module.py` performs conservative equivalent compaction:
  - URL Rewrite: only pure `- reject*` lines with identical action suffix.
  - Body Rewrite: only identical verb and body operation.
  - Map Local: only identical response operation.
- `scripts/validate_module_integrity.py` compiles generated rewrite regexes.
- `tests/test_module_compaction.py` protects URL Rewrite suffix and grouping behavior.

### 2026-07-02 Compact China / Overseas Network Split

- Main iOS Fusion keeps ad-blocking rules first and appends:
  - `GEOIP,CN,DIRECT`
  - `FINAL,PROXY`
- `strip_direct_proxy_rules = true` strips old scattered route/protection rules from the generated main module.
- `compact_network_split = true` appends the centralized split.
- Validation requires those two routing rules to be the final two active `[Rule]` entries.

### 2026-07-02 Automation Gap Guard

- `tools/generate_automation_gap_report.py` is a blocking automation coverage check.
- It verifies Fusion entry parity, App source/module counts, Android source/release parity, Windows v2rayN tail rules, scheduled workflow wiring, explicit staging, quality gate wiring, and script aggregation cache presence.
- It is wired into Builder `--check`, full quality gate, freshness checks, repository validation, repository health, and automated evidence.

## Known Risks

- Python regex validation is not a perfect Shadowrocket runtime simulation.
- Long combined OR regexes can behave differently on older clients, although chunking limits generated regex line length.
- `GEOIP,CN,DIRECT` is IP-geography based, not a perfect Chinese-App classifier.
- `FINAL,PROXY` requires the user's Shadowrocket configuration to have a usable `PROXY` policy or group.
- Real App end-to-end behavior is owner-tested manually; CI proves syntax, generation, and governance only.

## Protected Areas

Do not change these without concrete evidence and a risk note:

- Login and account APIs.
- Payment, order, and banking flows.
- Captcha and verification flows.
- Video playback domains and scripts.
- Image and static CDN domains.
- Authorization, Cookie, Token, or receipt logic.
- Broad MITM hostname scopes.
- Public module entry names or URLs.

## Next Recommendations

- Keep using `python scripts/quality_gate.py` as the final local gate for generated-output refreshes.
- If a real App breaks, fix the smallest source layer first and run the full quality gate.
- Keep watching scheduled workflow freshness from GitHub Actions when network access to GitHub API is available.
- Do not add more App modules or remote sources unless they are compatible with the upstream risk gate and do not include unlock, payment bypass, login bypass, or credential/token logic.

## 2026-07-16 Protected-Route Compiler And Audit Automation

- The Fusion rule compiler now treats explicit exact `DOMAIN` protection declarations as a no-REJECT contract.
- Broad protection suffixes do not automatically suppress narrower App ad endpoints; only an exact protected host, or a reject suffix that provably covers an exact protected host, is filtered.
- Four exact map/UI endpoints are registered in `Rules/direct.list` as compiler protection contracts.
- The generated Fusion module removed 9 conflicting REJECT lines and otherwise kept every non-Rule section unchanged.
- Final routing remains `GEOIP,CN,DIRECT` followed by `FINAL,PROXY`.
- `daily-audit-and-repair.yml` now repairs editable sources before Builder generation and audits the final module in report-only mode afterward.
- `Deploy GitHub Pages` failures are now observed by the workflow failure Issue automation.
- Local Builder `--check` and the complete quality gate passed with 398 App modules, 0 empty modules, and 952 Android rules.
- Remote confirmation passed: Module Factory `29435573074`, Pages `29435658218`, source-first daily audit `29435750405`, and failure watcher `29435804401` all completed successfully; open automation-failure Issues: 0.
