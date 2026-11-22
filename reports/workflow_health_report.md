# Workflow Health Report

- Generated at: 2026-11-23 05:59:15 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-10-18T21:30:34Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-11-22T21:58:31Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45075041907) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-11-21T21:51:46Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953718624) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-11-21T21:55:00Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953989121) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-11-21T22:06:35Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44954997663) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-11-21T22:12:49Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44955562178) | open the run log and fix the failed step |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-11-21T21:55:53Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44954060263) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-11-22T00:32:42Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967138718) | open the run log and fix the failed step |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-11-15T22:01:11Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-11-22T00:33:32Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967205869) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-11-22T00:33:45Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967222578) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
