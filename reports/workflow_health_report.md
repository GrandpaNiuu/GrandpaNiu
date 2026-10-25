# Workflow Health Report

- Generated at: 2026-10-26 03:55:44 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-10-18T21:30:34Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-10-25T19:13:07Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40224972488) | passed |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-10-25T19:14:14Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225061156) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-10-25T19:17:22Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225318892) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-10-25T19:29:54Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40226303724) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-10-25T19:44:14Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40227433445) | open the run log and fix the failed step |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-10-25T19:19:27Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225481276) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-10-24T22:36:13Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40139268459) | open the run log and fix the failed step |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-10-25T19:54:27Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) | Run is not completed; check again after it finishes |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-10-24T22:37:05Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40139327080) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-10-25T19:45:47Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40227561404) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
