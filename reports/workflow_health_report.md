# Workflow Health Report

- Generated at: 2026-07-22 01:56:12 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-07-15T20:01:53Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-07-21T17:55:23Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29854996689) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-07-20T18:31:28Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29768114576) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-07-20T18:44:38Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29769057755) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-07-20T18:59:35Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29770121522) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-07-20T19:10:27Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29770884302) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-07-20T18:45:27Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29769118634) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-07-20T21:39:09Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29781006174) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-07-19T18:32:19Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-07-20T21:39:56Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29781054824) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-07-20T21:40:36Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29781099632) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
