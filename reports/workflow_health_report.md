# Workflow Health Report

- Generated at: 2026-08-07 08:57:26 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-07-15T20:01:53Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-08-06T18:13:55Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31125455414) | open the run log and fix the failed step |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-08-06T18:14:30Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31125486713) | open the run log and fix the failed step |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-08-06T18:18:21Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31125678821) | open the run log and fix the failed step |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-08-06T18:35:45Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31126104917) | open the run log and fix the failed step |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-08-06T18:42:44Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31126263570) | open the run log and fix the failed step |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-08-06T18:18:14Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31125672578) | open the run log and fix the failed step |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-08-07T00:56:08Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31136346831) | Run is not completed; check again after it finishes |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-08-02T18:34:05Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-08-05T21:42:48Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31049804838) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-08-06T20:10:41Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31127412354) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
