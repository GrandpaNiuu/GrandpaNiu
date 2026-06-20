# AI Maintenance Decisions

Last updated: 2026-06-21 02:58 +0800

## Decisions

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

### 2026-06-21 - Serialize And Centralize Generated Output Publishing

All maintenance workflows that write generated outputs use the shared `module-maintenance` concurrency group and `scripts/commit_generated_changes.sh`.

The helper must:

- accept explicit paths only
- refuse broad staging
- retry push after fetch and rebase
- stop on rebase conflict instead of overwriting files

Reason: workflow-specific locks did not prevent different maintenance jobs from racing each other, and duplicated reset/regenerate loops could hide conflicts or drift apart.

### 2026-06-21 - Freshness Is A Blocking Quality Contract

Non-self-refresh governance reports marked blocking must be fresh when the quality gate finishes. Script aggregation and sandbox reports must be generated after the final profile build, and `check_report_freshness.py` must run with `--strict`.

Reason: a report that says blocking stale while CI exits successfully is false evidence and must not be published as a green gate.
