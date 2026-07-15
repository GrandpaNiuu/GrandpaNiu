# AI Maintenance Risk Log

Last updated: 2026-07-16 00:06 +08:00

## 2026-07-15 Strict Equivalent MITM Compaction Risk Note

Risk level: medium MITM compiler risk, low source-policy risk.

Authorized change:

- Reduce final Fusion MITM hostname count without changing Script, Rewrite, Map Local, Rule, App source, Android policy, or Windows routing behavior.
- Use only existing canonical wildcard coverage; do not create or remove wildcards.

Mitigations:

- Root domains, force-keep hosts, negative conflicts, IPs, ports, and complex patterns are retained.
- All `34` wildcard tokens remain unchanged.
- Each of the `45` removed exact tokens has exact-source and wildcard-source evidence.
- The independent validator reconstructs source baseline and force-keep data, rejects negative conflicts and complex-token removals, verifies deep features and non-MITM fingerprints, and checks the final Release host list.
- A deliberately inconsistent matcher test proves validation failure restores the `1234`-host unique baseline and reports zero final removals.
- Full Builder and full quality gate passed with `57` tests.

Remaining risk:

- The matcher contract is a repository compatibility contract approved by the owner; it is not a universal proof for every undocumented client version.
- Static deep-feature parsing still records `169` opaque features and `45` pre-existing baseline-uncovered features. This task does not delete, expand, or reinterpret them.
- Any real client regression should disable only `allow_equivalent_compaction` first; source MITM declarations remain available for immediate rebuild and rollback.

## 2026-07-10 Conservative MITM Compiler Risk Note

Risk level: medium MITM compiler risk, low traffic-policy change risk.

Owner request:

- Add a conservative, provable, default automatic MITM optimization stage.
- Keep Script, Rewrite, Map Local, Rule, and source fragments functionally unchanged.
- Do not rely on app testing or network requests as proof.
- Fail closed to baseline MITM output if validation fails.

Mitigations:

- Optimization is limited to final generated `[MITM]` output.
- Default mode removes exact duplicate hostname tokens only after normalization.
- The normalized hostname set must remain equal to baseline in normalize mode.
- Wildcard-covered exact subdomains remain in output.
- Hostnames without parsed consumers remain in output.
- Opaque dynamic URL, complex regex, variable, or remote-script dependencies prevent range shrinking.
- `tools/validate_mitm_coverage.py` checks the generated report against `Release/Ronghemokuai.sgmodule`.
- `tests/test_mitm_optimizer.py` covers duplicate dedupe, set equality, matcher semantics, opaque no-shrink, optional proven shrink behavior, fallback, and deterministic output.

Current evidence:

- Baseline MITM tokens: `2059`.
- Normalized unique tokens: `1234`.
- Exact duplicates removed: `825`.
- Wildcards before / after: `34 / 34`.
- Proved wildcard reductions: `0`.
- Opaque features retained: `169`.
- Baseline-uncovered deep features: `45`.
- Fallback: `False`.

Traffic risk boundary:

- No rule source, App source, script behavior, rewrite behavior, map-local response, Android routing, Windows routing, public URL, login, payment, bank, captcha, video, or image/CDN source policy was intentionally changed.

Remaining risk:

- Static hostname extraction is not a complete Shadowrocket runtime proof.
- The report's `baseline_uncovered_feature_count` records pre-existing baseline coverage gaps and must not be treated as permission to delete or expand MITM scopes automatically.
- Wildcard range reduction should remain disabled until a future task proves matcher semantics and complete finite dependencies.

## 2026-07-06 Pages Deploy Retry Hardening Risk Note

Risk level: low traffic-policy risk, medium deployment-automation risk.

Observed signal:

- `Deploy GitHub Pages` run `28755590928` failed on 2026-07-06 05:32 Beijing time.
- The triggering `Daily schedule watchdog` run succeeded.
- Pages source detection, checkout, Pages configuration, artifact preparation, and artifact upload all succeeded.
- Only the official `actions/deploy-pages` step failed.

Mitigation:

- Added up to three deployment attempts in `.github/workflows/pages-deploy.yml`.
- Retry attempts wait before retrying and re-upload `_site` with retry-specific artifact names.
- Validation now requires the retry guard.

Traffic risk boundary:

- This repair changes only deployment automation and generated reports refreshed by the quality gate.
- It does not change rule sources, App source fragments, MITM hostnames, JavaScript behavior, Android routing, Windows routing, login, payment, banking, captcha, video, image/CDN policy, or public module URLs.

Remaining risk:

- GitHub Pages can still have a longer outage. If all three attempts fail, the workflow should stay red because the public Pages update truly did not publish.
- Remote confirmation is required on the first post-push commit.

## 2026-07-04 Pages Deploy Red-Cross Repair Risk Note

Risk level: low traffic-policy risk, medium deployment-automation risk.

Observed signals:

- Multiple `Deploy GitHub Pages` runs failed during the daily maintenance window.
- Logs showed Pages backend failures after successful artifact upload.
- One rerun failed because `actions/deploy-pages` found multiple artifacts named `github-pages`.
- One run was cancelled by the Pages deployment concurrency group.

Mitigations:

- Reduced Pages `workflow_run` triggers to only `Module Factory Build` and `Daily schedule watchdog`.
- Kept manual dispatch.
- Removed direct push deploy so a push waits for Module Factory or the daily watchdog before Pages publishes.
- Changed Pages concurrency to queue instead of cancel.
- Added run-attempt-specific artifact names for upload and deploy.
- Added validation guardrails so high-frequency daily workflow triggers and direct push deploy cannot be silently reintroduced.

Traffic risk boundary:

- No rule source, App source, MITM hostname, JavaScript module behavior, Android routing, Windows routing, login, payment, banking, captcha, video, or image/CDN policy was changed.

Remaining risk:

- GitHub Pages can still occasionally return a backend deployment failure. The reduced trigger set lowers the likelihood by avoiding duplicate push plus workflow-run deployments and daily workflow bursts.
- Older red Pages runs remain in history; confirmation must use the new commit SHA.

## 2026-07-03 Pages Workflow Source Stabilization Risk Note

Risk level: low traffic-policy risk, medium deployment-configuration risk.

Observed signals:

- `Module Factory Build` succeeded after the governance commit.
- A generated-output follow-up commit was created.
- The old internal branch-based `pages build and deployment` failed on that generated commit while the repository was still in legacy Pages mode.
- Manual self-managed deploy attempts against the same failed pages build version also reported `Deployment failed, try again later`.

Mitigations:

- Changed repository Pages publishing mode to `workflow`.
- Updated Pages workflow to use `actions/deploy-pages@v5`.
- A later repair removed direct push deployment entirely; Pages now publishes after final workflow-run signals.

Traffic risk boundary:

- This does not change rules, App sources, MITM scopes, scripts, Android routing, Windows routing, or public module import URLs.

Remaining risk:

- The old `9e19eec6` Pages deployment remains failed historically.
- Confirmation must be done on the next commit SHA after this workflow update.

## 2026-07-03 GitHub Maintainer Lessons Implementation Risk Note

Risk level: low traffic-policy risk, medium governance/process risk.

Observed signals:

- The repository had a public GitHub maintainer lessons report, but several useful recommendations were still prose-only.
- Provenance, platform compatibility boundaries, protected traffic inventory, false-positive review queues, and upstream converter fixtures are the kinds of maintenance checks that should be repeatable.

Mitigations:

- Added generated provenance, platform compatibility, protected traffic, and false-positive review reports.
- Wired those reports into quality gate, freshness, repository validation, repository health, automation gap, and automated quality evidence.
- Added converter fixture tests so future upstream-format changes are checked before reaching generated modules.
- Reordered the false-positive report generation after `scripts/audit_reject_risk.py` so it consumes fresh risk data.

Traffic risk boundary:

- No ad rule source, App source, MITM hostname, JavaScript runtime behavior, Android routing policy, Windows routing policy, workflow runtime behavior, login, payment, banking, captcha, video, or image/CDN policy was intentionally changed.

Remaining risk:

- Provenance report currently shows many upstream records with missing license metadata. This is now visible but not yet solved.
- False-positive and protected-traffic reports are heuristic triage maps, not device/runtime proof.
- One remote-rule source had a transient SSL EOF warning during the final quality gate; the gate still passed and should be monitored in future scheduled runs.

## 2026-07-03 Report Encoding And Risk Ledger Risk Note

Risk level: low traffic-policy risk, medium governance visibility risk.

Observed signals:

- The user saw report Chinese mojibake and asked for it to be fixed.
- PowerShell output can display UTF-8 Chinese as mojibake even when files are valid.
- MITM and REJECT scopes are broad enough that maintainers need a clear source/risk review map before any future changes.

Mitigations:

- Added `tools/check_report_encoding.py` and `reports/report_encoding_report.md` to verify generated reports through UTF-8 reads.
- Added `tools/generate_mitm_reject_risk_ledger.py` and `reports/mitm_reject_risk_ledger.md`.
- Wired both into the quality evidence / freshness / health path.
- The ledger is read-only and does not alter any rule, MITM hostname, script, Android output, Windows output, or public module URL.

Remaining risk:

- The ledger marks risks by token heuristics, not real App runtime proof.
- Some marked entries may be intentional ad-cleaning rules. Do not remove or protect them without a concrete App symptom or log evidence.
- Historical mojibake text remains in older `docs/ai/WORKLOG.md` sections and should be cleaned in a separate docs-only pass.
- Full quality gate passed. An earlier run saw one transient SSL EOF warning for `ACL4SSR BanAD`; the final post-rebase full quality gate completed with 0 remote-rule warnings.

## 2026-07-03 QuanX Converted Rule Fallback Risk Note

Risk level: low traffic-policy risk, medium automation freshness risk.

Observed signal:

- `python scripts\quality_gate.py` failed when `scripts/convert_quanx_rules.py` could not fetch zirawell `allAdBlock.list` due to SSL EOF.
- A valid previous converted file already existed under `Rules/converted/`.

Mitigation:

- The converter now keeps existing converted outputs on fetch/read failure.
- It still fails if no local converted output exists.
- It still fails on successful fetch plus unsupported conversion content.

Remaining risk:

- A kept converted output may lag the upstream until the next successful fetch.
- This is preferred to publishing no rule set or failing all daily automation because of one transient upstream error.

## 2026-07-03 Pages Source-Mode Guard Risk Note

Risk level: low traffic-policy risk, medium deployment-automation risk.

Observed signal:

- Push of `52efbde8` triggered `Module Factory Build` successfully.
- GitHub default `pages build and deployment` succeeded.
- The self-managed `Deploy GitHub Pages` workflow failed, indicating repository Pages settings are not yet aligned with self-managed GitHub Actions Pages deployment.

Mitigation:

- Added a source-mode preflight to `.github/workflows/pages-deploy.yml`.
- Self-managed Pages deployment now runs only when the repository Pages API reports `build_type=workflow`.
- Otherwise the workflow reports a notice and skips the deploy job, leaving the currently successful default branch Pages deployment in charge.

Remaining risk:

- If the owner wants the self-managed workflow to be the active Pages publisher, repository Settings -> Pages still needs to be switched to GitHub Actions.
- Until then, the default `pages build and deployment` workflow is the real Pages publisher.
- This does not affect module content or runtime ad-cleaning behavior.

## 2026-07-03 Upstream App Sync Automation Repair Risk Note

Risk level: low traffic-policy risk, medium automation-publishing risk.

Observed signals:

- `upstream-app-module-sync.yml` failed while other required daily workflows had recent successful runs.
- Local reproduction showed transient SSL EOF fetch failures from multiple upstream App sources.
- The same reproduction also found an upstream KFC regex typo, `res\.kfc\.com.\cn`, that generated an invalid combined rewrite regex.
- A newly discovered Kelee module could stay enabled after first-import fetch failure even though `Rewrite/Sources/Apps/<id>.conf` did not exist.

Mitigations:

- Existing local App sources are retained when their upstream fetch or conversion temporarily fails.
- First-import modules with no local source are disabled until a future successful fetch fills them.
- KFC conversion repairs the deterministic `.cn` regex typo before generation.
- `check_automation_status.py` no longer blocks the repository on an older-commit failed run once a newer repair commit exists and a fresh success is available.
- Risk-gate blocks remain hard failures.

Traffic risk boundary:

- No App ad source, MITM hostname, login, payment, banking, captcha, video playback, image/CDN rule, Android routing policy, Windows routing policy, or public module URL was intentionally changed.
- Real App behavior is not changed by this pass; the repair targets automation resilience and generated syntax validity.

Remaining risk:

- Remote GitHub Actions still needs a post-push confirmation run.
- Future upstream sources can introduce new syntax defects; the converter should fix narrow deterministic defects and let risk gates block unsafe content.

## 2026-07-03 Pages Deploy Queue Repair Risk Note

Risk level: low traffic-policy risk, medium operational deployment risk.

Observed signal:

- The GitHub Actions screenshot shows `Deploy to GitHub Pages` repeatedly reporting `Current status: deployment_queued`, then failing with `Timeout reached, aborting!` and cancelling the deployment.

Likely cause:

- The repository had no explicit Pages deployment workflow, so GitHub's default Pages deployment path used the default `actions/deploy-pages` 10 minute timeout.
- Generated-output repositories can produce frequent pushes and queued deployments; old queued deploys can delay the latest static site update.

Mitigations:

- Added a self-managed `Deploy GitHub Pages` workflow.
- Publishes a constrained `_site` artifact with the repository's public static outputs instead of relying on the implicit branch-root deployment path.
- Uses `timeout: 600000`, `reporting_interval: 10000`, and `error_count: 30` for `actions/deploy-pages`.
- Uses `pages-deploy-main` concurrency with `cancel-in-progress: true` to avoid stale deploys blocking the newest deploy.
- Added validation in repository, health, automation gap, workflow health, and automation status checks.

Remaining risk:

- The repository Pages setting may still need to be switched to **GitHub Actions** in GitHub Settings -> Pages. If it remains on branch deployment, GitHub can continue running the old default Pages deployment.
- GitHub Pages service-side outages or long platform queues can still delay deployment, but the repository now avoids keeping stale queued runs and uses the maximum supported action timeout.
- This pass does not affect ad-rule runtime behavior.

## 2026-07-03 Full Repository Health Refresh Risk Note

Risk level: low traffic-policy risk, medium operational visibility risk.

Observed signals:

- Local strict freshness failed when run immediately after a standalone Builder check because not every governance report is regenerated by that command in quality-gate order.
- Full `python scripts/quality_gate.py` regenerated the required reports and passed strict freshness.
- Local GitHub API access through `gh run list --limit 12` timed out to `198.18.0.26:443`, so remote Actions status could not be confirmed from this machine.

Mitigations:

- No rule source, MITM scope, script behavior, Android routing policy, Windows routing policy, workflow, or Builder logic was changed.
- Generated outputs were refreshed through the normal quality gate.
- AI records now state that `quality_gate.py` is the final local gate for generated-output refreshes.

Remaining risk:

- Remote GitHub Actions status still needs confirmation when GitHub API access is available.
- Static checks cannot prove real App ad removal or runtime login/video/payment behavior; those remain device-tested by the owner.

## 2026-07-02 Fusion Rewrite Compaction Risk Note

Risk level: medium to high rewrite behavior risk, mitigated by conservative grouping and validation.

Changed behavior:

- Many generated URL Rewrite, Body Rewrite, and Map Local lines are now represented as combined OR regex groups.
- The rule action or response operation is preserved exactly.
- The public module is smaller, but some individual lines are longer.

Mitigations:

- URL Rewrite compaction only merges pure `- reject*` rules with the same suffix.
- Body Rewrite compaction only merges byte-identical operations.
- Map Local compaction only merges byte-identical payload/status/header operations.
- Generated rewrite regexes are compiled by `scripts/validate_module_integrity.py`.
- Unit tests cover the most important syntax boundary: preserving `pattern - reject` grammar.

Remaining risk:

- Python regex validation is not a perfect Shadowrocket engine simulation.
- Very long OR regex lines can behave differently on older clients. Current chunking limits each generated regex line to roughly 6000 characters.
- If an App-specific rewrite stops matching, inspect the relevant combined line before changing source rules.

## 2026-07-02 Compact China / Overseas Network Split Risk Note

Risk level: high runtime routing impact, owner-requested after real network errors.

Observed signal:

- Owner reported network errors after the previous main Fusion module removed all `DIRECT` and `PROXY` routing policies.

Changed behavior:

- Main iOS Fusion `[Rule]` now keeps ad-blocking rules first.
- It strips scattered source `DIRECT` / `PROXY` policies from the public output.
- It appends only:
  - `GEOIP,CN,DIRECT`
  - `FINAL,PROXY`

Potential runtime impact:

- Chinese Apps should generally avoid proxy routing by IP geography, but some Chinese services using overseas Anycast/CDN IPs may still hit `FINAL,PROXY`.
- Overseas Apps should generally use the proxy fallback, but overseas Apps using China CDN IPs may hit `GEOIP,CN,DIRECT`.
- `FINAL,PROXY` assumes the user's Shadowrocket configuration has a usable policy or group named `PROXY`.

Mitigation:

- Validation requires these two rules to be the only routing rules in the main Fusion `[Rule]` section and requires them to be the final two active rules.
- Old scattered protection source files remain available for rollback or a future granular mode.
- If runtime issues continue, first verify the user's Shadowrocket policy group name and then consider a small, explicit domain-based China/overseas list rather than restoring many protection routes.

## 2026-07-02 Main Fusion Routing Strip Risk Note

Risk level: high runtime stability risk, intentional owner-approved policy change.

Owner confirmation:

- Remove `DIRECT` and `PROXY` rules from the main Fusion module.
- Keep ad-blocking rules.
- Do not change Android or Windows for this pass.

Changed behavior:

- The generated main iOS Fusion `[Rule]` no longer contains `DIRECT` or `PROXY` policy lines.
- Source protection files remain in the repository for rollback and non-iOS projections.

Potential runtime impact:

- Login and OAuth pages may rely on previously protected routing.
- Banking, payment, order, and captcha endpoints may no longer be explicitly protected by module rules.
- Image/CDN and video playback domains may no longer be explicitly direct-protected in the main iOS module.
- Google, YouTube, Telegram, Instagram, Discord, Reddit, Netflix, and similar services no longer receive explicit `PROXY` policy from the module.

Mitigation:

- `scripts/validate_repository.py` now blocks accidental reintroduction of `DIRECT` or `PROXY` in the main Fusion `[Rule]`.
- If real App breakage appears, first consider disabling `strip_direct_proxy_rules` in `Rewrite/Profiles/fusion.conf` or adding a narrow output exception instead of broad source deletion.
- Android and Windows outputs remain available for their existing routing projections.

## 2026-07-02 Automation Gap Hardening Risk Note

Risk level: low traffic-policy risk, medium operational risk.

Observed weakness:

- Existing checks covered many separate areas, but there was no single blocking report that said whether automation wiring itself was complete after generated-output, Android, Windows, report, and workflow changes.

Mitigations:

- Added `tools/generate_automation_gap_report.py`.
- The report blocks when public Fusion entries drift, app source/module counts differ, Android source and Release manifests diverge, Windows v2rayN tail rules are missing, writer workflows lose locks or explicit staging, quality gate wiring drops required checks, required reports are missing, or script aggregation cache files are invalid.
- The report is wired into Builder `--check`, full quality gate, freshness checking, repository health, repository validation, and automated evidence.
- The script was placed in `tools/` to avoid Windows `Scripts/` versus `scripts/` case-collision problems.

Traffic risk boundary:

- No Rules, App sources, MITM hostnames, script behavior, Android routing policy, Windows routing policy, login, payment, banking, captcha, video, or image/CDN policy was intentionally changed.
- Upstream replacement scoring and App feedback ingestion were intentionally excluded by owner instruction.

Remaining risk:

- GitHub Actions still needs a remote run confirmation after push.
- Real App behavior remains owner-tested manually and is not a CI gate.

## Standing High-Risk Areas

| Area | Risk | Required Handling |
|---|---|---|
| Public iOS entries | Users import these URLs directly; breakage affects everyone | Do not rename, remove, or repoint without explicit approval |
| Fusion version strategy | Reintroducing multi-version routes can break CI and docs | Keep Fusion as the primary public strategy |
| `Release/` outputs | Generated by builder; manual edits are overwritten | Fix sources or builder first |
| MITM hostnames | Can break login, payment, video, image/CDN, or app APIs | Review source and write a risk note before narrowing or expanding |
| Login / auth / token / cookies | Can lock users out or break sessions | Avoid rewrites unless clearly safe and sourced |
| Payment / banking / orders | Can break financial flows | Prefer DIRECT/protection, not REJECT or body rewrite |
| Captcha / verification | Can break account access | Avoid aggressive blocking |
| Video playback | Can cause no network, black screen, or skipping | Prefer protection rules for playback domains |
| Image / static CDN | Can cause blank feeds or broken pages | Prefer DIRECT/protection for known CDN domains |
| Upstream auto-sync | Can import unsafe or incompatible modules | Keep risk gate and backups enabled for high-risk records |
| Script aggregation | Bad `$done` behavior can cause white screens or hangs | Keep sandbox validation active |
| Script aggregation upstream fetch | Temporary upstream JS fetch failures can shrink aggregation or increase public script URLs | Use generated cache fallback and validate cache integrity |
| Scheduled GitHub Actions | GitHub may delay/drop schedules without a failing run | Use the daily schedule watchdog and automation status report |
| Android outputs | Cannot fully mirror iOS Rewrite/MITM/Script behavior | Document limitations and avoid promising full parity |
| Windows v2rayN routing | Routing-only, no iOS-style rewrite scripts | Keep docs clear and JSON valid |
| AI maintenance Markdown | Collapsed records can hide safety rules or combine commands | Keep headings, lists, tables, and command blocks readable |
| `.gitignore` format | A collapsed comment line can disable ignore rules | Keep one ignore pattern per line |

## Initial Snapshot Notes

- Current manual real app testing is performed by the owner.
- Automated checks cover syntax, generation, repository health, script aggregation, upstream risk, Android format, and reports.
- Rule overlap is known and reported; overlap is not automatically a bug because sources can intentionally reinforce coverage.
- MITM scope is broad and must be changed carefully.

## Current Task Risk

Current risk for the 2026-06-26 unattended automation hardening is low to medium and operational, not traffic-policy related.

Observed signals:

- The previous daily schedule watchdog exited early when `# update-date` was already fresh, so it did not check whether other daily workflows had recently succeeded.
- Local validation showed transient SSL EOF failures while fetching remote JavaScript and remote rule sources.
- Before the cache hardening, transient script fetch failures could reduce script aggregation from 52 routes and push individual script URLs back into the public module.

Mitigations:

- Added `scripts/check_automation_status.py` and `reports/automation_status_report.md`.
- The watchdog now writes the automation status report and runs strict scheduled-workflow stale/failure checks after the date-recovery logic.
- `scripts/build_module.py` now caches low-risk script sources and recovers from the committed bundle/manifest when upstream fetches fail.
- `tools/validate_script_aggregation.py` validates cache integrity.
- Full quality gate passed after the change with 398 App modules, 0 empty modules, 52 aggregated script routes, and 0 hard script fetch failures.

Remaining risk:

- Local GitHub API calls can fail because of network/proxy/SSL issues; strict stale/failure enforcement is expected to run inside GitHub Actions with `GITHUB_TOKEN`.
- Real app runtime behavior is unchanged by this pass and remains owner-tested.

Current risk for the 2026-06-26 sync self-check is low to medium and operational, not traffic-policy related.

Observed signals:

- `Android/branches.json` and `Release/Android/branches.json` differed only by generated timestamp after a scheduled update path.
- Running the previous `quality_gate.py` could leave `Release/Module.sgmodule` out of sync with `Release/Ronghemokuai.sgmodule`.

Mitigations:

- Full-Builder workflows now stage `Android/` and `Windows/` generated outputs.
- Upstream app sync rollback restores `Android/` and `Windows/` generated outputs.
- The quality gate uses the unified Builder release path.
- Repository validation blocks Release alias drift and full-Builder workflow staging omissions.
- No App source rules, MITM hostnames, login, payment, banking, captcha, video, or image/CDN protection policies were intentionally changed.

Remaining risk:

- The next natural scheduled runs should be monitored to confirm the repaired staging paths publish cleanly on GitHub Actions.

The latest foreign app expansion is medium operational risk because it adds 9 overseas / international app-service cleanup sources and regenerates public outputs.

Mitigations:

- Added only app ad-cleaning sources from trusted GitHub upstreams already compatible with the sync framework.
- Kept every new record under `Rewrite/Remotes/app-modules.json` daily direct sync.
- Added converter protection for `dcapps.disney.go.com` and `seavideo-ak.espn.go.com` before syncing Go.com, preventing Disney / ESPN video-core style REJECT lines from entering the module.
- Skipped broad high-risk foreign candidates:
  - Adobe activation / licensing hosts
  - Apple / Google Safe Browsing hosts
  - Microsoft CRL and system service hosts
  - Amazon AWS core-service hosts
- Did not intentionally add VIP/member unlock, payment bypass, login bypass, token/cookie rewrite, receipt forgery, or account-sharing modules.
- Preserved daily upstream tracking through `Rewrite/Remotes/app-modules.json`.
- Kept existing protected import filters for `apd-pcdnwxlogin`, `msync-im`, and `ossgw.alicdn.com`.
- Ran Builder release check with repository validation, upstream risk gate, script aggregation validation, script bundle sandbox, Android format check, and governance validation.

Remaining risk:

- Real App end-to-end behavior is still owner-tested manually.
- Some imported App modules use broad ad network hostnames. If a specific App breaks login, video, images, or normal networking, disable or narrow that single App source first.
- Yahoo includes an exact MITM scope for `m.yap.yahoo.com`; if Yahoo pages show abnormal behavior, narrow or disable `Rewrite/Sources/Apps/yahoo.conf` first.

## Pending REJECT Risk Review Checklist

## App Source Syntax Hardening Risk Note

Risk level: medium.

Observed failure signal:

- The former quality gate validated only the final Fusion module, allowing malformed independent App modules to remain unnoticed.
- Reproduced defects included a rewrite line inside `[Rule]`, an unsupported Header Rewrite action, a bare domain rule, duplicate script names, duplicate Map Local status codes, unescaped JSON, and a remote `data-path` unsupported by the repository syntax contract.

Mitigations:

- Fixed conversion logic at the source synchronizer and re-synced only affected records from their existing registered upstreams.
- Embedded the Xiaoju charging response resource as base64 instead of retaining a remote `data-path`.
- Preserved high-risk rollback copies for RedNote, Weibo, and Zhihu.
- Added blocking validation for every source fragment and every generated App module.
- Did not add or broaden login, payment, banking, captcha, video playback, or image/CDN policies.

Remaining risk:

- Normalized App modules can still have upstream behavioral regressions that static syntax checks cannot detect.
- Device/runtime behavior must be diagnosed one App and one source rule at a time from real evidence.

Source: `reports/reject_risk_report.md` generated at 2026-06-20 12:04:12 +0800.

Do not change these rules without Shadowrocket logs, user-confirmed breakage, or targeted source-first review.

Evidence requirement: only make a source-first single-rule change when there is real app abnormal behavior or log/capture evidence. Every such change must be followed by the full quality gate.

### Bank / Payment

- `DOMAIN,iisp-oidea.mbs.boc.cn,REJECT,pre-matching`
- `DOMAIN,iisp.mbs.boc.cn,REJECT,pre-matching`

### Image / CDN

- `DOMAIN,cd-1.pddpic.com,REJECT,pre-matching`
- `DOMAIN,cdl-1.pddpic.com,REJECT,pre-matching`
- `DOMAIN,cdl-p2.pddpic.com,REJECT,pre-matching`
- `DOMAIN,hudong.alicdn.com,REJECT,pre-matching`
- `DOMAIN,layout.meituan.net,REJECT,pre-matching`
- `DOMAIN,nbsdk-baichuan.alicdn.com,REJECT,pre-matching`
- `DOMAIN,ossgw.alicdn.com,REJECT,pre-matching`

### Domestic Core API

- `DOMAIN,afdconf.baidu.com,REJECT,pre-matching`
- `DOMAIN,amap-aos-info-nogw.amap.com,REJECT,pre-matching`
- `DOMAIN,dpmtpush.dianping.com,REJECT,pre-matching`
- `DOMAIN,free-aos-cdn-image.amap.com,REJECT,pre-matching`
- `DOMAIN,hlx.meituan.com,REJECT,pre-matching`
- `DOMAIN,layout.meituan.net,REJECT,pre-matching`
- `DOMAIN,lc.map.baidu.com,REJECT,pre-matching`
- `DOMAIN,lx0.meituan.com,REJECT,pre-matching`
- `DOMAIN,r.dianping.com,REJECT,pre-matching`

### Review Guidance

- Prefer exact `DIRECT,pre-matching` protection only when logs prove a false positive.
- Prefer commenting or narrowing one rule at a time over batch deletion.
- Do not use broad suffix allow rules such as `DOMAIN-SUFFIX,qq.com,DIRECT`.
- Rebuild and validate after any future source-first rule change.

## 2026-06-21 Automation Hardening Risk Note

Risk level: medium operational, low traffic-policy risk.

Observed signals:

- The quality gate exited successfully while its freshness report contained blocking stale script reports.
- The first hardening attempt used one global concurrency group; remote run #555 proved that GitHub cancels older pending workflows when several jobs share that group.
- Several workflows and the commit helper used `git reset --hard`, contrary to repository safety policy.
- Automated failure Issue #248 lost backticked status names and recovery commands because an expanding shell heredoc performed command substitution.

Mitigations:

- Enforced strict report freshness after the final bundle rebuild and runtime sandbox.
- Isolated concurrency by workflow/ref and retained staggered schedules, so unrelated maintenance jobs cannot cancel each other.
- Kept `Module Factory Build` as the single push-validation entrypoint.
- Centralized explicit-path staging and fetch/rebase/retry in one tested helper.
- Rebase conflicts now stop the workflow instead of force-overwriting generated files.
- Failure Issue Markdown is generated without shell expansion, preserving diagnostic commands.

Traffic risk boundary:

- No Rules, App source, MITM, login, payment, banking, captcha, playback, or CDN policy was changed.
- Real App behavior remains device-tested by the owner; static automation cannot certify every App network path.

## 2026-06-22 Cross-Workflow Writer Lock Risk Note

Risk level: medium operational, no traffic-policy impact.

Observed signal:

- Scheduled invalid-rule audit run `27913047570` passed audit and Fusion build, then failed in the publish step.
- It and Daily Module Update started from the same `main` snapshot after GitHub delayed their schedules into the same minute.
- Daily Module Update advanced `main`; the audit publisher then refused a generated-output rebase conflict as designed.

Mitigations:

- Every generated-output writer acquires one atomic remote lock before running maintenance commands.
- The lock holder fast-forwards to current `origin/main` before changing files.
- Release verifies the exact lock owner SHA and is executed under `if: always()`.
- A one-hour stale threshold prevents an abandoned ref from blocking maintenance forever.
- A real bare-Git integration test covers contention, refusal, release, reacquisition, and waiter fast-forward behavior.
- Validation scripts now require lock acquisition and unconditional release in every writer workflow.

Remaining risk:

- A job running longer than the stale threshold could have its lock reclaimed. Current maintenance jobs normally finish well inside one hour; investigate before increasing job scope substantially.
- The repaired path was remotely confirmed by Module Factory Build `27913770402` and invalid-rule audit rerun `27913813597`; Issue #249 closed automatically.
- No Rules, App sources, MITM, login, payment, banking, captcha, video, or CDN policy changed in this repair.

## 2026-07-02 Automation Governance Repair Risk Note

Risk level: low traffic-policy risk, medium operational risk.

Observed signal:

- Builder `--check` failed at `scripts/validate_governance_extensions.py` because the script still required old multi-profile policy wording.
- `quality_gate.py` then failed on a stale policy phrase in `docs/PROFILE_POLICY.md`.

Mitigations:

- Updated governance validation to check the current Fusion-only policy contract.
- Rewrote `docs/PROFILE_POLICY.md` to describe active Fusion publishing, generated-output boundaries, validation, and rollback rules.
- Ran the full Builder check and full quality gate successfully.

Traffic risk boundary:

- No Rules, App source, MITM, script behavior, Android routing policy, Windows routing policy, login, payment, banking, captcha, video, or image/CDN policy was intentionally changed.
- Generated reports and checksums were refreshed by the Builder and quality gate.

## 2026-07-16 Protected-Route Compilation And Automation Repair Risk Note

Risk level: medium traffic-policy risk, medium operational risk.

Observed signals:

- Fusion strips source `DIRECT` / `PROXY` lines before appending the compact `GEOIP,CN,DIRECT` / `FINAL,PROXY` split.
- Protection sources are merged before ad rules, but stripping their routing lines can expose later `REJECT` rules that the protection sources previously shadowed.
- The builder has a manually maintained protected-token list, so protection sources and generated filtering can drift apart.
- `daily-audit-and-repair.yml` audits and edits the generated root module before Builder regeneration, which can discard a generated-only repair.
- `workflow-failure-issue.yml` does not currently observe `Deploy GitHub Pages` failures.

Planned safeguards before changing protected traffic behavior:

- Add unit tests before implementation.
- Derive reject-conflict filtering only from explicit source `DIRECT` / `PROXY` protection declarations; do not infer protection from domain names.
- Keep unrelated ad `REJECT` rules unchanged.
- Keep the final compact network split unchanged.
- Make invalid-source repair source-first and keep final-module URL inspection report-only.
- Add Pages to the existing failure watcher without changing deployment behavior.

Rollback boundary:

- If source-derived protection removes an unrelated ad rule or causes a quality-gate regression, revert the compiler filter while retaining the tests and report evidence.
- No Script, Rewrite, MITM, payment bypass, login bypass, membership, or account behavior is authorized by this change.
