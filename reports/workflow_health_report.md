# Workflow Health Report

- Generated at: 2026-08-13 01:36:05 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-08-07T19:07:21Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-08-12T17:35:07Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31623358631) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-08-11T17:36:39Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31518439235) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-08-11T17:43:24Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31519014658) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-08-11T18:00:29Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31520479722) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-08-11T18:09:27Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31521254986) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-08-11T17:43:58Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31519063710) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-08-11T21:12:05Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536747702) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-08-09T18:01:34Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-08-11T21:12:48Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536807139) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-08-11T21:13:26Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536855812) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
