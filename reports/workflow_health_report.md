# Workflow Health Report

- Generated at: 2026-09-05 03:07:00 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-08-07T19:07:21Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-09-04T19:05:50Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33909358330) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-09-03T19:25:21Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33796336572) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-09-03T19:27:56Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33796582540) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-09-03T19:42:28Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33798005033) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-09-03T19:55:23Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33799241571) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-09-03T19:28:20Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33796620954) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-09-03T22:41:10Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33814214450) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-08-30T19:59:41Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-09-03T22:41:58Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33814272087) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-09-03T22:42:33Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33814316413) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
