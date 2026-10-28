# Workflow Health Report

- Generated at: 2026-10-29 05:17:52 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-10-18T21:30:34Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-10-28T21:16:48Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40770615277) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-10-27T20:57:39Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40582634412) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-10-27T20:59:41Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40582917859) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-10-27T21:11:41Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40584693936) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-10-27T21:22:15Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40586213739) | open the run log and fix the failed step |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-10-27T20:59:55Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40582951320) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-10-27T23:52:53Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40605105963) | open the run log and fix the failed step |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-10-25T19:54:27Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-10-27T23:53:47Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40605205870) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-10-27T23:53:59Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40605227206) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
