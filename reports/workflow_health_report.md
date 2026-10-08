# Workflow Health Report

- Generated at: 2026-10-09 05:29:02 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-08-07T19:07:21Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-10-08T21:28:04Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37846975775) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-10-07T21:32:30Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690140010) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-10-07T21:37:52Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690764735) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-10-07T21:54:16Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37692621725) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-10-07T22:03:38Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37693674855) | open the run log and fix the failed step |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-10-07T21:38:04Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690788533) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-10-08T00:17:08Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37706949812) | open the run log and fix the failed step |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-10-04T20:22:44Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-10-08T00:17:52Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37707014129) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-10-08T00:18:02Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37707027319) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
