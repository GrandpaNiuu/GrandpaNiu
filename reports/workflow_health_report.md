# Workflow Health Report

- Generated at: 2026-09-18 03:50:15 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-08-07T19:07:21Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-09-17T19:49:19Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267138751) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-09-17T19:50:05Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267212957) | Run is not completed; check again after it finishes |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-09-16T19:44:20Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35142357985) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-09-16T19:57:46Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35143677724) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-09-16T20:13:36Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35145266887) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-09-16T19:45:20Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35142459005) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-09-16T23:05:51Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160752453) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-09-13T19:42:16Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-09-16T23:06:36Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160814955) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-09-16T23:07:07Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160853717) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
