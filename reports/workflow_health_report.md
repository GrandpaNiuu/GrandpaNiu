# Workflow Health Report

- Generated at: 2026-07-16 01:10:30 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-07-15T16:16:30Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29431720426) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-07-14T17:43:43Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29354970352) | passed |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Daily invalid rule audit and safe repair | manual / schedule | 2026-07-14T17:44:43Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355038894) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-07-14T17:49:44Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355378346) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-07-14T18:10:45Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29356798709) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-07-14T18:33:07Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29358315602) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-07-14T17:51:19Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355488700) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-07-14T21:28:35Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29369660755) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-07-12T18:30:20Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-07-15T16:17:54Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29431817066) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-07-15T16:17:54Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29431817214) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
