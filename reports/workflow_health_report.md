# Workflow Health Report

- Generated at: 2026-10-25 02:58:40 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-10-18T21:30:34Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-10-24T18:57:45Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40123097421) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-10-23T20:04:00Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016310139) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-10-23T20:06:33Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016645567) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-10-23T20:17:05Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40018016386) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-10-23T20:29:57Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40019674415) | open the run log and fix the failed step |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-10-23T20:06:55Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016692007) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-10-23T23:16:36Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038738329) | open the run log and fix the failed step |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-10-18T19:35:33Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-10-23T23:17:24Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038817714) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-10-23T23:17:35Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038834621) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
