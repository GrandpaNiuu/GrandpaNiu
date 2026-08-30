# Workflow Health Report

- Generated at: 2026-08-31 04:00:37 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-08-07T19:07:21Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-08-30T19:24:40Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33330791741) | passed |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-08-30T19:25:37Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33330835812) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-08-30T19:29:11Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33330989806) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-08-30T19:42:53Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33331632871) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-08-30T19:51:43Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332036664) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-08-30T19:29:58Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33331022710) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-08-29T22:42:32Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33279246810) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-08-30T19:59:41Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) | Run is not completed; check again after it finishes |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-08-29T22:43:07Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33279267497) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-08-30T19:53:23Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332110612) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
