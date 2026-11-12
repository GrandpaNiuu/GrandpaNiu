# Workflow Health Report

- Generated at: 2026-11-13 06:26:23 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-10-18T21:30:34Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-11-12T22:25:35Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43319774270) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-11-12T22:26:09Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43319868210) | Run is not completed; check again after it finishes |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-11-11T23:06:23Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43117208448) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-11-11T23:23:52Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43119502219) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-11-11T23:29:52Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43120253256) | open the run log and fix the failed step |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-11-11T23:07:13Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43117318577) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-11-12T01:56:59Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43137972889) | open the run log and fix the failed step |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-11-08T21:19:48Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-11-12T01:57:43Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43138051802) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-11-12T01:57:54Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43138071896) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
