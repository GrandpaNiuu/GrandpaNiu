# Workflow Health Report

- Generated at: 2026-07-02 10:53:13 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 10

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-07-02T02:52:28Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28561960172) | Run is not completed; check again after it finishes |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-07-01T18:28:26Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539092511) | passed |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Daily invalid rule audit and safe repair | manual / schedule | 2026-07-01T18:29:14Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539136602) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-07-01T18:32:03Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539292954) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-07-01T19:03:31Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541038955) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-07-01T19:14:06Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541625184) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-07-01T18:51:31Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28540371201) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-07-01T21:57:15Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28550399745) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-06-28T18:46:55Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-07-02T00:49:40Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28557660528) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
