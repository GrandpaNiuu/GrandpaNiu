# Workflow Health Report

- Generated at: 2026-10-19 03:36:44 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-08-07T19:07:21Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-10-18T18:52:20Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156151388) | passed |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-10-18T18:54:00Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156272947) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-10-18T18:58:49Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156630091) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-10-18T19:21:49Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39158418720) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-10-18T19:27:44Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39158870897) | open the run log and fix the failed step |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-10-18T18:59:52Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156705265) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-10-17T22:29:21Z | completed | failure | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39075269715) | open the run log and fix the failed step |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-10-18T19:35:33Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) | Run is not completed; check again after it finishes |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-10-17T22:30:00Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39075314998) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-10-18T19:29:48Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159020754) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
