# Workflow Health Report

- Generated at: 2026-06-25 02:21:34 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 10

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-06-21T18:37:56Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27913770402) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-06-24T18:21:02Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28120232890) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Daily invalid rule audit and safe repair | manual / schedule | 2026-06-24T18:21:12Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28120242728) | Run is not completed; check again after it finishes |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-06-23T18:33:53Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28048259893) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-06-23T19:12:05Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28050513410) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-06-23T19:21:26Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28051049687) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-06-23T18:56:14Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28049580262) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-06-23T21:54:43Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28059708334) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-06-21T19:04:17Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-06-23T21:55:00Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28059723100) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
