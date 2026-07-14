# Workflow Health Report

- Generated at: 2026-07-15 01:44:38 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-07-09T19:15:26Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-07-14T17:43:43Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29354970352) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Daily invalid rule audit and safe repair | manual / schedule | 2026-07-13T18:19:46Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29274015647) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-07-13T18:22:10Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29274174671) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-07-13T18:46:35Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29275829866) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-07-13T18:51:46Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29276173626) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-07-13T18:23:00Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29274227923) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-07-13T21:27:00Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286380982) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-07-12T18:30:20Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-07-13T21:27:38Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286420311) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-07-13T21:27:38Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286420711) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
