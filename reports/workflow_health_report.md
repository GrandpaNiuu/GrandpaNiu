# Workflow Health Report

- Generated at: 2026-07-27 02:37:56 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-07-15T20:01:53Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-07-26T17:38:32Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30213001305) | passed |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-07-26T17:40:42Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30213078114) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-07-26T17:46:14Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30213277790) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-07-26T18:06:18Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30214002936) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-07-26T18:14:59Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30214315513) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-07-26T17:47:03Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30213305732) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-07-25T21:22:55Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30175523980) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-07-26T18:36:57Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) | Run is not completed; check again after it finishes |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-07-25T21:23:44Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30175549608) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-07-26T18:16:11Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30214361166) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
