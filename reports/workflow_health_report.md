# Workflow Health Report

- Generated at: 2026-07-06 01:41:15 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-07-04T02:41:32Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28692446521) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-07-05T17:40:36Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749304568) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Daily invalid rule audit and safe repair | manual / schedule | 2026-07-04T17:40:54Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28714376809) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-07-04T17:47:32Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28714545821) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-07-04T18:08:54Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28715114234) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-07-04T18:15:17Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28715283606) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-07-04T17:48:51Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28714578935) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-07-04T21:26:07Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720143746) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-07-04T05:15:25Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28695947613) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with stale deployment cancellation | manual / workflow_run | 2026-07-04T21:26:29Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720153795) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-07-04T21:26:29Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720153793) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
