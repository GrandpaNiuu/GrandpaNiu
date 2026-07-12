# Workflow Health Report

- Generated at: 2026-07-13 01:39:29 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-07-09T19:15:26Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-07-12T17:38:42Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202375935) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Daily invalid rule audit and safe repair | manual / schedule | 2026-07-11T17:38:24Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29161978793) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-07-11T17:41:38Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162077227) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-07-11T17:59:05Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162608775) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-07-11T18:10:19Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162955905) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-07-11T17:41:33Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162074721) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-07-11T21:12:34Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168396768) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-07-05T18:40:26Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-07-11T21:13:05Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168411983) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-07-11T21:13:05Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168411981) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
