# Workflow Health Report

- Generated at: 2026-09-20 02:50:37 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-08-07T19:07:21Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-09-19T18:49:47Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462438135) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-09-18T19:10:38Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35384451890) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-09-18T19:13:52Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35384759702) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-09-18T19:30:11Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35386284503) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-09-18T19:42:40Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35387451425) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-09-18T19:14:08Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35384786329) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-09-18T22:42:31Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35402727925) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-09-13T19:42:16Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-09-18T22:43:19Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35402785466) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-09-18T22:43:59Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35402829952) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
