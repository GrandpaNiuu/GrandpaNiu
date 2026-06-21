# Workflow Health Report

- Generated at: 2026-06-22 02:38:38 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 10

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-06-21T18:37:56Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27913770402) | Run is not completed; check again after it finishes |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-06-21T18:08:17Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27913034831) | passed |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Daily invalid rule audit and safe repair | manual / schedule | 2026-06-21T18:08:48Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27913047570) | open the run log and fix the failed step |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-06-21T18:10:29Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27913090735) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-06-21T18:24:03Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27913422677) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-06-20T18:50:19Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27880579296) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-06-21T18:11:26Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27913112880) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-06-20T21:45:30Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27884814585) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-06-15T19:36:18Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27571392238) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-06-21T18:24:39Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27913437731) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
