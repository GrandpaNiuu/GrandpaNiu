# Workflow Health Report

- Generated at: 2026-08-03 01:39:21 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-07-15T20:01:53Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-08-02T17:38:35Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30759327798) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-08-01T17:39:32Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30710805988) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-08-01T17:44:30Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30710983309) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-08-01T18:04:38Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30711712707) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-08-01T18:14:07Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30712063447) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-08-01T17:45:42Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30711028300) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-08-01T21:22:26Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30718995980) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-07-26T18:36:57Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-08-01T21:22:59Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30719015521) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-08-01T21:23:40Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30719038762) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
