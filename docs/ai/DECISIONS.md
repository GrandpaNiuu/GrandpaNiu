# AI Maintenance Decisions

Last updated: 2026-07-03 02:35 +08:00

## Decisions

### 2026-07-03 - Use A Self-Managed GitHub Pages Deploy Workflow

GrandpaNiu should publish GitHub Pages through `.github/workflows/pages-deploy.yml` instead of relying on the default branch-root Pages deployment path.

Required behavior:

- Build a constrained `_site` static artifact from public repository outputs.
- Use `.nojekyll`.
- Deploy with `actions/deploy-pages`.
- Set `timeout: 1800000` so queued deployments are not aborted at the default 10 minute mark.
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
