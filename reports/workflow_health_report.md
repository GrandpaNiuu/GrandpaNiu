# Workflow Health Report

- Generated at: 2026-10-10 05:13:34 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-08-07T19:07:21Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-10-09T21:12:26Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37992003387) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-10-08T21:29:07Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37847097727) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-10-08T21:32:59Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37847562936) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-10-08T21:58:03Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37850394890) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-10-08T22:10:37Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37851787746) | open the run log and fix the failed step |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-10-08T21:33:48Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37847656608) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-10-09T00:30:58Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37865174275) | open the run log and fix the failed step |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-10-04T20:22:44Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-10-09T00:31:40Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37865233851) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-10-09T00:31:51Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37865249335) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
