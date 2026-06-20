# AI Maintenance Decisions

Last updated: 2026-06-20 22:12 +0800

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
