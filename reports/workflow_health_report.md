# Workflow Health Report

- Generated at: 2026-06-22 02:08:55 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 10

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-06-20T23:43:34Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27887472503) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-06-21T18:08:17Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27913034831) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Daily invalid rule audit and safe repair | manual / schedule | 2026-06-21T18:08:48Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27913047570) | Run is not completed; check again after it finishes |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-06-20T18:01:37Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27879388762) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-06-20T23:27:47Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27887130054) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-06-20T18:50:19Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27880579296) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-06-20T18:01:55Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27879396857) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-06-20T21:45:30Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27884814585) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-06-15T19:36:18Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27571392238) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-06-21T00:29:14Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27888461055) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
