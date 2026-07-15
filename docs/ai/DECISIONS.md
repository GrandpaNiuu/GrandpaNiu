# AI Maintenance Decisions

Last updated: 2026-07-16 03:42 +08:00

### 2026-07-16 - Module Complexity Is Budgeted Without Automatic Feature Reduction

The generated Fusion module must pass explicit byte, line, section, Script, MITM token, wildcard, and oversized-line budgets. Budget enforcement is read-only and must never delete or rewrite traffic behavior to make a build pass.

The existing Xiaojukeji Charge Map Local payload remains embedded because no repository evidence proves that an external resource form is Shadowrocket-equivalent. It is allowed only by an explicit section/marker exception with independent size and match-count limits.

Build summaries distinguish `unchanged`, `metadata-only`, and `module-semantic-changed`. This classification covers module configuration text only and must not be presented as proof of client runtime behavior or unchanged remote content.

Reason: the module's principal maintainability risk is byte and single-line growth rather than duplicate final entries. A conservative regression budget detects accidental expansion without trading away App functionality.

### 2026-07-15 - Existing Wildcards May Compact Redundant Exact MITM Tokens

GrandpaNiu may remove an exact final-output MITM hostname when all of the following are true:

- an already-declared canonical `*.example.com` wildcard covers it under matcher contract `shadowrocket-mitm-suffix-wildcard-v1`
- the wildcard remains in the output
- the exact token is not force-kept
- no negative hostname token overlaps it
- it is a plain hostname rather than an IP, port, partial wildcard, `?` pattern, or other complex token
- independent validation confirms the optimized set is a strict baseline subset, all wildcard tokens are unchanged, and all removed exact hosts remain covered

This decision supersedes only the earlier default prohibition on removing exact hosts under wildcard coverage. It does not authorize creating broader wildcards, removing wildcards, deleting no-consumer hosts, changing source fragments, or enabling wildcard range reduction.

Reason: removing a singleton exact matcher already contained in a retained wildcard does not change the matcher coverage union under the approved repository contract, while reducing final client configuration size. Unproven cases remain untouched and validation failure falls back to baseline.

### 2026-07-10 - MITM Optimization Defaults To Strict Equivalent Normalize

GrandpaNiu may optimize generated Fusion `[MITM]` output only in the final compiler stage.

Required behavior:

- Do not rewrite `Script`, `URL Rewrite`, `Header Rewrite`, `Body Rewrite`, `Map Local`, or `Rule` sections.
- Do not edit `Rewrite/Sources/` as part of MITM optimization.
- Default mode may split, normalize, and exact-dedupe hostname tokens only.
- Default mode must preserve the normalized hostname token set.
- Do not remove exact hosts merely because a wildcard appears to cover them.
- Do not remove hosts without a statically parsed consumer.
- Do not shrink wildcard ranges unless matcher semantics, dependency parsing, opaque absence, and coverage are all machine-proven.
- If validation fails, publish the baseline unique MITM output and record fallback instead of emitting a partial optimized result.

Reason: MITM scopes are high-risk for login, payment, video, images/CDN, and app APIs. Exact duplicate removal is safe as configuration normalization; range shrinking is not safe without proof.

Current status:

- Default normalize is enabled.
- Range reduction has zero active reductions.
- `tools/validate_mitm_coverage.py` is part of the quality gate.

### 2026-07-06 - Pages Deployment Must Retry Before Failing The Workflow

GrandpaNiu Pages deployment should tolerate transient GitHub Pages backend failures after a successful artifact upload.

Required behavior:

- `Deploy GitHub Pages` keeps the reduced trigger set:
  - `workflow_dispatch`
  - `workflow_run` from `Module Factory Build`
  - `workflow_run` from `Daily schedule watchdog`
- The workflow must not deploy directly on push.
- Pages deployment must attempt `actions/deploy-pages` up to three times before failing the workflow.
- Retry attempts must use unique artifact names so reruns or retries do not collide with the first `github-pages` artifact.
- Validation must block removing the retry structure.

Reason: run `28755590928` showed that even a single final Pages deployment can fail inside `actions/deploy-pages` after artifact upload. Trigger reduction fixed deployment bursts, but retry is still needed for transient platform failures.

### 2026-07-04 - Pages Deploy Must Not Listen To Every Daily Workflow

GrandpaNiu Pages deployment should be triggered only by final or deliberate publishing signals, not every maintenance workflow.

Required behavior:

- `Deploy GitHub Pages` may run on:
  - `workflow_dispatch`
  - `workflow_run` from `Module Factory Build`
  - `workflow_run` from `Daily schedule watchdog`
- `Deploy GitHub Pages` must not run directly on push.
- Pages concurrency should queue runs with `cancel-in-progress: false` instead of cancelling a run into a red status.
- `Deploy GitHub Pages` must not listen directly to high-frequency daily maintenance workflows:
  - `Daily Module Update`
  - `Daily invalid rule audit and safe repair`
  - `Daily invalid source audit and repair`
  - `Scheduled Module Factory Update`
  - `Upstream app module sync`
  - `Upstream candidate collect`
  - `Repository Health Check`
- Pages artifact names should include `${{ github.run_attempt }}` to avoid duplicate artifact collisions on reruns.

Reason: GitHub Pages deployments are stateful and can fail when multiple deployments are created for nearby commits in a short window. Direct push deploy plus a generated-output workflow-run deploy caused duplicate deployments for the same change. Module Factory and the daily watchdog are safer final publishing signals.

### 2026-07-03 - GitHub Pages Publishing Should Use Workflow Mode

GrandpaNiu should use the repository self-managed `Deploy GitHub Pages` workflow as the intended Pages publisher.

Required behavior:

- Repository Pages `build_type` should be `workflow`.
- `.github/workflows/pages-deploy.yml` should stay available and deploy the constrained `_site` artifact.
- The workflow should publish after final workflow-run signals, not directly on every public artifact push.
- The workflow should use current `actions/deploy-pages@v5`.

Reason: running both legacy branch Pages publishing and a self-managed Pages workflow can create duplicate deployments and red failures that are unrelated to module correctness.

### 2026-07-03 - GitHub Maintainer Lessons Become Generated Governance Evidence

GrandpaNiu should convert safe lessons from comparable public rule-module repositories into generated, checked evidence instead of keeping them as one-time prose.

Required behavior:

- Keep upstream provenance visible through `reports/upstream_provenance_report.md`.
- Keep platform capability boundaries visible through `reports/platform_compatibility_matrix.md`.
- Keep protected traffic sources visible through `reports/protected_traffic_ledger.md`.
- Keep potential false-positive review items visible through `reports/false_positive_review_report.md`.
- Keep converter compatibility locked with fixture tests.
- Wire all generated reports into quality gate, freshness, repository validation, repository health, automation gap, and automated evidence paths.

Reason: this repository is high risk and long-lived. Maintainer lessons should become repeatable guardrails, not memory or chat context.

Boundary:

- These reports are governance and triage evidence. They do not authorize broad automatic rule deletion, VIP/payment/login bypass logic, or protected traffic changes without real runtime evidence.

### 2026-07-03 - Generated Reports Must Pass UTF-8 Mojibake Guard

GrandpaNiu should keep a generated report encoding guard in the quality gate.

Required behavior:

- `tools/check_report_encoding.py` scans `reports/*.md` as UTF-8 text.
- Common mojibake markers cause a blocking failure.
- PowerShell display mojibake is not treated as file corruption; the UTF-8 read result is the source of truth.
- If the guard fails, fix the generator script first rather than hand-editing generated reports.

Reason: reports are part of the public maintenance evidence. Garbled Chinese makes workflow failures and risk reports hard to understand.

### 2026-07-03 - MITM / REJECT Ledger Is Informational Only

The MITM / REJECT ledger should be generated and kept fresh, but it must not modify rules.

Required behavior:

- List source path, risk category, risk level, and marker reason.
- Do not delete, comment, replace, or auto-protect any rule.
- Use the ledger as a review map before making source-first single-rule changes.

Reason: the owner wants visibility into high-risk MITM and REJECT scopes, but rule changes still require real App symptoms, logs, packet captures, or another concrete signal.

## Decisions

### 2026-07-03 - Converted QuanX Rule Fetch Failures May Keep Existing Outputs

`scripts/convert_quanx_rules.py` should keep a previously generated converted output when the upstream fetch or UTF-8 read fails temporarily.

Required behavior:

- If `Rules/converted/<name>.list` exists and is non-empty, keep it and print a warning.
- If no existing converted output exists, fail rather than silently publishing a missing rule set.
- If upstream content is fetched but cannot be converted safely, continue to fail.

Reason: daily automation should not red-cross on a transient upstream SSL EOF when the repository already has a valid converted output.

### 2026-07-03 - Self-Managed Pages Deploy Must Respect Repository Pages Source

The self-managed `pages-deploy.yml` workflow should run `actions/deploy-pages` only when the repository's Pages `build_type` is `workflow`.

Required behavior:

- Keep default branch Pages deployment as the active publisher when repository settings are not switched to GitHub Actions.
- Keep the self-managed workflow as a guarded standby path.
- Do not let the self-managed workflow auto-fail on push or workflow-run events when Pages settings still use branch deployment.

Reason: the push after `52efbde8` showed default Pages deployment succeeding while the self-managed Pages workflow failed. Code cannot switch repository Pages settings without admin access, so the workflow must detect the source mode and avoid a conflicting deployment.

### 2026-07-03 - Upstream App Sync Treats Transient Fetch Failures As Retryable

Daily App upstream sync should not fail the entire repository when one remote source has a transient SSL EOF, timeout, or conversion fetch issue.

Required behavior:

- If the target source already exists, keep publishing the existing local source and retry on the next scheduled run.
- If the target source does not exist yet, disable that first-import record and clear direct commit until a later discovery pass can fetch it successfully.
- Keep unsafe upstream content, VIP/payment/login bypass patterns, and risk-gate blocks as hard failures.
- Keep known upstream syntax repairs in the converter when they are deterministic and narrow, such as the KFC `.cn` regex escape.

Reason: the daily sync should be resilient to temporary remote availability problems without hiding genuinely unsafe upstream content.

### 2026-07-03 - Use A Self-Managed GitHub Pages Deploy Workflow

GrandpaNiu should publish GitHub Pages through `.github/workflows/pages-deploy.yml` instead of relying on the default branch-root Pages deployment path.

Required behavior:

- Build a constrained `_site` static artifact from public repository outputs.
- Use `.nojekyll`.
- Deploy with `actions/deploy-pages`.
- Set `timeout: 600000`, GitHub's supported maximum for `actions/deploy-pages`, and rely on concurrency cancellation to prevent stale queued deployments from blocking the newest deployment.
- Use a dedicated Pages concurrency group with `cancel-in-progress: true` so stale deploys do not block the newest public module/site update.
- Keep validation guards in `validate_repository.py`, `repository_health_check.py`, and `generate_automation_gap_report.py`.

Reason: a Pages deployment stayed in `deployment_queued` until the default `actions/deploy-pages` timeout cancelled it. Generated-output repositories push often, so Pages needs explicit queue control and a longer deploy wait.

Operational note: GitHub repository Pages settings should use **Source: GitHub Actions**. If the repository remains configured for branch deployment, GitHub can still launch the old default Pages deployment workflow.

### 2026-07-02 - Use Conservative Rewrite Compaction For Fusion Size

The main iOS Fusion module may compact generated rewrite sections when `compact_rewrite_sections = true`.

Allowed compaction:

- URL Rewrite lines may be merged only when they are pure `pattern - reject*` lines with the same action suffix.
- Body Rewrite lines may be merged only when verb and body operation are identical.
- Map Local lines may be merged only when embedded response operation is identical.

Disallowed compaction:

- Do not merge redirects, header rewrites, script-path rules, or mixed operations.
- Do not remove rules merely to reduce line count.
- Do not change the compact network split tail.

Reason: the owner wants the public Fusion module closer to 3000 lines without losing ad-cleaning behavior or creating network instability.

### 2026-07-02 - Main Fusion Uses Compact China / Overseas Routing

The main iOS Fusion module uses a compact network split instead of zero routing and instead of many scattered protection routes.

Generated `[Rule]` behavior:

- Strip scattered source `DIRECT` / `PROXY` rules from the public Fusion output.
- Append `GEOIP,CN,DIRECT`.
- Append `FINAL,PROXY`.

Reason: after removing all `DIRECT` and `PROXY`, the owner reported real network errors. The compact split keeps the module easier to manage while restoring a clear China-direct and overseas-proxy path.

Validation must allow only these two routing rules in the main Fusion `[Rule]` section and require them as the final two active rules.

### 2026-07-02 - Main Fusion Output Strips DIRECT And PROXY Rules

Superseded by the compact China / overseas routing decision above.

The main iOS Fusion module still strips scattered `DIRECT` and `PROXY` policies from generated `[Rule]` output when `Rewrite/Profiles/fusion.conf` has `strip_direct_proxy_rules = true`, but it now appends the managed compact split when `compact_network_split = true`.

Source files are preserved. Android and Windows outputs are not part of this policy change.

Reason: the owner wants the public iOS Fusion module to avoid embedded routing/protection/proxy split rules and keep only ad-cleaning rule policies in the main module output.

Validation must keep blocking future `DIRECT` or `PROXY` policies in the generated root Fusion `[Rule]` section.

### 2026-07-02 - Automation Gap Report Is A Blocking Contract

`tools/generate_automation_gap_report.py` must stay in the quality gate and repository validation path.

It checks generated-output parity, scheduled workflow wiring, writer lock/staging safety, app module source/release counts, Android/Windows projection presence, required automation reports, and script aggregation cache files.

It must not pretend to replace real App testing, ad-impression verification, upstream replacement scoring, or App feedback ingestion.

Reason: the repository already has many individual checks. The new report makes the remaining maintainability coverage explicit and blocks release when automation wiring drifts.

### 2026-06-26 - Watchdog Must Check Scheduled Workflow Freshness

The daily schedule watchdog must generate `reports/automation_status_report.md` and run `scripts/check_automation_status.py --strict --no-write` after any missed-date recovery check.

Reason: GitHub scheduled workflows can be delayed or dropped without a failing workflow run. A fresh module date alone does not prove that invalid-source repair, upstream sync, candidate collection, or health checks have run successfully.

### 2026-06-26 - Script Aggregation Must Survive Transient Upstream Fetch Failures

Low-risk script aggregation should cache fetched upstream JavaScript in `Scripts/generated/fusion-script-bundle.cache.json` and recover from the previous committed bundle/manifest before dropping a route from the public bundle.

Reason: temporary SSL/timeouts from upstream script hosts should not change the public module shape or increase Shadowrocket script URLs. Hard failures without cache remain visible in reports.

### 2026-06-26 - Full Builder Publishers Must Stage Android And Windows

Any workflow that runs `Rewrite/Generator/Builder.py --profile fusion --release` and commits generated outputs must stage `Android/` and `Windows/` together with `Release/`, `Web/`, reports, and the root module.

Reason: the Builder refreshes Android source outputs, Windows v2rayN output, and `Release/Android/`. If a workflow commits only `Release/Android/`, the published release layer can drift from the source Android layer.

### 2026-06-26 - Quality Gate Must Use The Unified Builder Release Pipeline

`scripts/quality_gate.py` should call `Rewrite/Generator/Builder.py --profile fusion --release` rather than manually chaining only a subset of release scripts.

Reason: partial release regeneration can leave `Release/Module.sgmodule`, `Release/Rules.conf`, per-App modules, Android, Windows, Web, or checksums stale even when the quality gate exits green.

### 2026-06-20 - Use Repository Records As AI Source Of Truth

Any AI or new conversation must read `AGENTS.md`, `PROJECT_STATE.md`, `AI_HANDOFF.md`, and `docs/ai/*` before modifying the repository.

Reason: this repository has many generated files, risk gates, upstream sync paths, and public entry points. Chat context alone is not reliable enough.

### 2026-06-20 - Keep Fusion Single Public Module Strategy

The public iOS strategy remains one Fusion module.

Stable, Lite, Full, Stable Plus, Aggressive, or similar routes should not return as public user choices without explicit owner approval.

Reason: earlier multi-version logic caused workflow, validation, README, and release-report drift.

### 2026-06-20 - Source-First Maintenance

Business changes should start from source files and registries, not generated release files.

Reason: `Release/`, `Web/`, `reports/`, and `Scripts/generated/` are largely builder outputs and can be overwritten.

### 2026-06-20 - Protect Sensitive Traffic Categories

Login, payment, banking, captcha, video playback, and image/CDN rules require risk notes before modification.

Reason: these paths are the most likely to cause app unusability when over-blocked or MITM-scoped incorrectly.

### 2026-06-20 - Keep Upstream Direct Commit Behind Risk Gate

Upstream app modules may sync automatically only while `tools/validate_upstream_risk_gate.py` remains active and passing.

Reason: automatic upstream replacement is useful but can accidentally import unsafe unlock or bypass logic.

### 2026-06-20 - Keep AI Maintenance Markdown Readable

AI maintenance Markdown files must keep normal headings, lists, tables, and fenced command blocks.

Reason: collapsed single-line records can make future AI or human maintainers misread safety rules.

### 2026-06-20 - Treat Old Four Profiles As Legacy Reference Only

Fusion is the only public iOS module strategy. Old Stable / Stable Plus / Lite / Full files may remain only as deprecated compatibility or rollback references.

Reason: public multi-version routing previously caused README, workflow, validation, and release-report drift.

### 2026-06-20 - Avoid Broad Workflow Staging

Automation should use explicit `git add` path lists instead of `git add -A`.

Reason: generated workflows can refresh many files; explicit staging reduces accidental commits outside the intended output set.

### 2026-06-20 - Require Evidence Before Rule Changes

Rule changes that touch app behavior must be based on real app breakage, Shadowrocket/client logs, packet-capture evidence, or another reproducible signal. Do not change high-risk rules only because a report looks suspicious.

Reason: this repository protects many login, payment, bank, captcha, video, image/CDN, and core API paths. Guess-based broad rule edits can create worse breakage than the original ad issue.

### 2026-06-20 - Governance Checks Accept Builder Entrypoint

Workflow governance validation should recognize `Rewrite/Generator/Builder.py --profile fusion --release` as the preferred Fusion build signal, while remaining backward-compatible with old `build_module.py --build --profile fusion` markers.

Reason: the repository is moving to the Builder entrypoint; requiring old marker comments can break CI even when the workflow is correct.

### 2026-06-20 - Require End-Of-Task AI Self-Review

Every meaningful AI maintenance task must include a short self-review before final response, commit, or push.

Reason: recent work showed that process drift, stale validation assumptions, and incomplete final checks are easier to prevent when the agent explicitly records what was not good enough and how the next pass should start.

### 2026-06-21 - Bulk App Upstream Imports Need Protected Host Filtering

GitHub app module imports may be added as direct-commit upstream records, but the converter must filter known protected login, message, and CDN entries before publishing them into source fragments.

Current protected additions include:

- `apd-pcdnwxlogin`
- `msync-im`
- `ossgw.alicdn.com`

Reason: bulk imports are useful for coverage, but upstream ad snippets can contain over-broad REJECT or MITM lines. Filtering high-risk host patterns at conversion time reduces the chance that future daily syncs reintroduce the same breakage.

### 2026-06-21 - Foreign Expansion Must Skip Broad Platform Core Rules

Overseas / international app coverage can be expanded from trusted GitHub upstreams, but broad platform rules that touch activation/licensing, Safe Browsing, certificate revocation, AWS/cloud core services, payment, login, or account authorization paths must stay out of direct sync unless a targeted risk review approves them.

Current skipped examples:

- Adobe activation / licensing hosts
- Apple / Google Safe Browsing hosts
- Microsoft CRL and system service hosts
- Amazon AWS core service hosts

Current added Go.com protection examples:

- `dcapps.disney.go.com`
- `seavideo-ak.espn.go.com`

Reason: foreign coverage is useful, but broad platform rules can break normal app access, security checks, playback, or system connectivity. App expansion should favor narrow ad / telemetry endpoints and converter-level protection.

### 2026-06-21 - Isolate And Centralize Generated Output Publishing

All maintenance workflows that write generated outputs use isolated `module-maintenance-${{ github.workflow }}-${{ github.ref }}` groups and `scripts/commit_generated_changes.sh`.

Only `Module Factory Build` validates pushes. Scheduled maintenance workflows use schedule/manual triggers so one workflow-file change does not launch several generated-output writers.

The helper must:

- accept explicit paths only
- refuse broad staging
- retry push after fetch and rebase
- stop on rebase conflict instead of overwriting files

Reason: one global GitHub concurrency group cancels older pending runs when several workflows start together, as demonstrated by cancelled Module Factory Build run #555. Isolated workflow locks preserve every run, while staggered schedules and the safe rebase helper control write races without destructive resets.

### 2026-06-21 - Freshness Is A Blocking Quality Contract

Non-self-refresh governance reports marked blocking must be fresh when the quality gate finishes. Script aggregation and sandbox reports must be generated after the final profile build, and `check_report_freshness.py` must run with `--strict`.

Reason: a report that says blocking stale while CI exits successfully is false evidence and must not be published as a green gate.

### 2026-06-21 - Generate Failure Issue Markdown Outside Shell Expansion

`workflow-failure-issue.yml` writes its Markdown body with Python reading environment variables. Do not use an unquoted shell heredoc for Markdown containing backticks.

Reason: Bash treats backticks in an expanding heredoc as command substitution. Issue #248 proved that this erased status names and all recovery commands from the automated failure report.

### 2026-06-22 - Serialize Cross-Workflow Writers With A Remote Lock

Keep the per-workflow GitHub concurrency group, and additionally require every workflow that writes generated output to acquire the repository remote maintenance lock before generation.

The lock must:

- be acquired atomically through a dedicated remote ref
- fast-forward the checkout to current `origin/main` after acquisition
- record ownership locally
- release only when the remote ref still matches the recorded owner
- run release under `if: always()`
- recover locks older than the configured stale threshold using an exact SHA lease

Reason: GitHub may delay different schedules into the same minute. Isolated concurrency groups do not serialize different workflows, while one shared GitHub concurrency group can cancel older pending runs. Run `27913047570` proved that two valid builders can otherwise collide only at publish time.

The helpers live in `tools/` because Windows case-insensitive filesystems cannot reliably create new lowercase `scripts/` files alongside the existing uppercase `Scripts/` directory.

### 2026-07-02 - Governance Validation Must Follow Fusion-Only Policy

`validate_governance_extensions.py` must validate the active Fusion-only contract: `Rewrite/Profiles/fusion.conf`, the Builder release command, the three public Fusion entries, and independent App modules.

Old Stable / Stable Plus / Lite / Full names may appear only as retired-history references. Governance checks must not require old active Full/Stable policy text after the files are intentionally removed.

Reason: stale governance tokens caused the Builder and quality gate to fail even though the generated Fusion module and required scheduled automation were otherwise healthy.

## 2026-07-16 - Exact Protection Contracts Survive Compact Routing Compilation

The public Fusion output continues to strip scattered `DIRECT` / `PROXY` lines and keeps the compact China/overseas split. Before those routing lines are stripped, the compiler now uses explicit protection sources as a narrow no-REJECT contract.

Decision boundaries:

- Exact protected `DOMAIN` entries block an exact REJECT and any reject suffix that provably covers that exact host.
- A broad protected `DOMAIN-SUFFIX` does not automatically suppress narrower exact App ad endpoints.
- Compound `AND`, User-Agent, regex, and other contextual rules are retained unless an existing dedicated safety rule handles them.
- The compiler changes generated output only; source REJECT entries remain traceable for upstream comparison and rollback.

Reason: compact routing previously removed the precedence that protection lines had over later REJECT rules. Restoring that safety contract must not become a broad ad-block bypass.

## 2026-07-16 - Generated Module URL Audit Is Report-Only

`audit_and_repair_module.py` no longer edits `Ronghemokuai.sgmodule`. Editable-source repair runs first through `audit_repair_invalid_sources.py`; Builder then regenerates all outputs; the final module audit only validates and reports links.

Reason: editing a generated module before Builder regeneration produced non-persistent repairs and could make reports claim a repair that was immediately overwritten.

## 2026-07-16 - Daily Maintenance Workflows Have Distinct Owners

The invalid-rule audit validates generated output and writes reports only. Invalid-source repair owns source edits. Upstream collection owns candidate discovery. A source-maintenance workflow may invoke the full Builder only when its source step reports a real change.

Source-change detection must use `git status --porcelain` over explicit source paths so newly created untracked files are included. `git diff --quiet` is insufficient for this decision.

Reason: running the same repair, collection, and full-build stages in several daily workflows increases write contention, runtime, and contradictory reports without adding coverage.

## 2026-07-16 - App Module Capability Is A Static Classification

Release and Web catalogs classify App modules by their generated sections: deep, rewrite, rule, or MITM-only. The classification is documentation and automation evidence, not a runtime-effectiveness or device-test claim.

MITM-only compatibility fragments remain visible rather than receiving unrelated or paid-feature scripts merely to appear functional.

Reason: a non-empty `.sgmodule` can still contain only a hostname declaration. Users and maintainers need that distinction without unsafe source expansion.

## 2026-07-16 - Risk Ledgers Trace Source Findings To Final Output

MITM and REJECT risk reports record exact final presence, equivalent MITM wildcard coverage, or source-only / compiler-filtered status. The tooling must not infer that a source rule is unnecessary merely because it is absent from the generated Fusion output.

Reason: source-first compilers legitimately deduplicate, normalize, or filter entries. A useful risk ledger must distinguish those states while preserving the evidence boundary.

## 2026-07-16 - Collector Allowlist And Commit Paths Are One Contract

Every target in `ALLOWED_LOCAL_TARGETS` and `ALLOWED_SCRIPT_TARGETS` must be explicitly staged by `upstream-collect.yml`. Repository validation imports those sets and fails if workflow staging drifts.

Reason: committing generated output without the collector's source edit creates a non-reproducible release that disappears on the next build.

## 2026-07-16 - Quality-Gate Workflows Use Authenticated Actions Status

Every workflow that runs the complete quality gate or strict automation status must grant `actions: read` and expose the repository-scoped `GITHUB_TOKEN` to the status checker.

Reason: anonymous GitHub API limits can turn useful status evidence into `unknown` or make a strict watchdog fragile even when the repository token is already available.

## 2026-07-16 - Change Impact Report Describes A Committed Range

The change-impact report intentionally analyzes `HEAD~1..HEAD` because CI runs after a commit exists. Its mode label must state that committed range explicitly; a local pre-commit report is not represented as the current working-tree diff.
