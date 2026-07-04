# Workflow Health Report

- Generated at: 2026-07-04 10:12:20 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-07-03T01:51:04Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28633173916) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-07-03T18:00:10Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676404378) | passed |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Daily invalid rule audit and safe repair | manual / schedule | 2026-07-03T18:00:49Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676433801) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-07-03T18:03:15Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676533914) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-07-03T18:18:35Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28677143825) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-07-03T18:41:14Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678029048) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-07-03T18:04:07Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676570699) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-07-03T21:38:39Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684457263) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-06-28T18:46:55Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with stale deployment cancellation | manual / push / workflow_run | 2026-07-03T21:39:10Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684473213) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-07-03T21:39:10Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684473227) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
