# Workflow Health Report

- Generated at: 2026-07-01 02:21:43 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 10

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-06-26T14:22:44Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-06-30T18:21:05Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28466573892) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Daily invalid rule audit and safe repair | manual / schedule | 2026-06-29T18:32:08Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28394169601) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-06-29T18:53:30Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28395348517) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-06-29T19:08:04Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28396153463) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-06-29T19:17:01Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28396641424) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-06-29T18:54:09Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28395386293) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-06-29T21:50:02Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28404980325) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-06-28T18:46:55Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-06-29T21:50:33Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28405006821) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
