# Workflow Health Report

- Generated at: 2026-10-04 03:23:17 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-08-07T19:07:21Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-10-03T19:22:19Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37147643136) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-10-02T20:57:17Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37063850438) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-10-02T21:02:00Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37064347837) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-10-02T21:15:17Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37065717753) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-10-02T21:20:52Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37066285253) | open the run log and fix the failed step |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-10-02T21:02:50Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37064435265) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-10-02T23:53:49Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37079701411) | open the run log and fix the failed step |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-09-27T20:20:33Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-10-02T23:54:37Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37079758824) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-10-02T23:54:48Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37079772031) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
