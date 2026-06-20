# AI Maintenance Tasks

Last updated: 2026-06-20 11:58 +0800

## Active Rules For Task Handling

- Keep Fusion as the only primary public iOS module.
- Prefer source-first edits under `Rules/`, `Rewrite/Sources/`, `Rewrite/Remotes/`, `Scripts/`, `Android/`, `Windows/v2rayN/`, and `tools/`.
- Do not directly edit generated Release outputs unless the task is explicitly about generated artifact repair and the source path is understood.
- Update AI records after each meaningful maintenance change.

## Current Open Tasks

- Monitor future user-reported app breakage and fix with targeted source changes.
- Keep upstream app module sync governed by `tools/validate_upstream_risk_gate.py`.
- Keep script aggregation governed by validation and sandbox reports.
- Use MITM and rule overlap reports for future narrowing or dedupe, but avoid automatic deletions without review.
- Keep Android and Windows outputs aligned with iOS source rules where technically possible.

## Backlog

- Improve documentation around which outputs are generated versus editable sources.
- Add more focused tests for protected traffic categories if stable fixtures become available.
- Add clearer report summaries for non-technical maintainers.
- Review empty or legacy rule files periodically, but avoid deleting compatibility files without tracing references.

## Done

- 2026-06-20: Initial AI maintenance record system created.
- 2026-06-20: Baseline project state and handoff captured.
- 2026-06-20: Private local log directory initialized outside the repository.
