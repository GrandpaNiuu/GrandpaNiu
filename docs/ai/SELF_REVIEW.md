# AI Self-Review Checklist

Last updated: 2026-06-20 22:58 +0800

## Purpose

Every AI maintenance pass must end with a short self-review before the final reply, commit, or push.

The goal is to catch avoidable mistakes early, especially in this repository where workflow, rule, MITM, script, Android, Windows, and generated-output changes can easily affect public users.

## Required End-Of-Task Review

Before finishing, answer these questions:

1. Did I follow the newest user request instead of an older conversation goal?
2. Did I read `AGENTS.md`, `PROJECT_STATE.md`, `AI_HANDOFF.md`, `docs/ai/TASKS.md`, `docs/ai/DECISIONS.md`, `docs/ai/RISK_LOG.md`, and recent `docs/ai/WORKLOG.md` entries?
3. Did I run `git status` and `git branch --show-current` before editing?
4. Did I preserve user changes and avoid unrelated refactors?
5. Did I touch only the intended source layer?
6. If I touched rules, MITM, scripts, Android, Windows, or workflows, did I have a concrete failure signal or owner instruction?
7. If protected traffic could be affected, did I record the risk and avoid guess-based changes?
8. Did I avoid directly editing generated outputs unless the source/generator path was understood?
9. Did I run the narrowest meaningful validation, and did I explain any skipped validation?
10. Did I update AI records with what changed, why, validation, risks, and next steps?
11. Did I check `git diff --stat`, `git diff`, and `git diff --check` where appropriate?
12. If committing or pushing, did I stage only intended files and use fetch/rebase/retry for remote updates?

## Self-Critique Format

Record a short section in `docs/ai/WORKLOG.md` for meaningful work:

```text
### Self-Review

- What was not good enough:
- What I changed to reduce that risk:
- What I would check first next time:
```

If no code or repository file changed, include the same points in the final reply instead.

## Common Weak Spots To Watch

- Assuming a workflow failed for the same reason as a previous run without reproducing it.
- Treating generated reports as commands to delete rules instead of evidence for targeted review.
- Forgetting that `Release/`, `Web/`, `reports/`, and `Scripts/generated/` are often generated outputs.
- Letting validation scripts lag behind the current Builder workflow.
- Running full builders in the main worktree when a temporary worktree would avoid generated-output noise.
- Forgetting to update AI records after a real maintenance change.
- Saying "fixed" before confirming the GitHub Actions run that actually failed.

## Default Improvement Rule

When a task reveals a process weakness, prefer adding a narrow guardrail, checklist item, or validation rule so the same mistake is less likely next time.
