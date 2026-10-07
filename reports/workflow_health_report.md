# Workflow Health Report

- Generated at: 2026-10-08 05:32:31 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-08-07T19:07:21Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-10-07T21:31:24Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690010487) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-10-07T21:32:30Z | queued | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690140010) | Run is not completed; check again after it finishes |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-10-06T21:16:11Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37532664204) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-10-06T21:33:05Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37534683601) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-10-06T21:41:55Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37535700176) | open the run log and fix the failed step |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-10-06T21:17:16Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37532794471) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-10-06T23:55:54Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37549233341) | open the run log and fix the failed step |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-10-04T20:22:44Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-10-06T23:56:44Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37549305906) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-10-06T23:57:30Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37549370820) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
