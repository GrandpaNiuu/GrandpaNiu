# Workflow Health Report

- Generated at: 2026-06-26 21:52:23 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 10

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-06-26T13:51:25Z | pending | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28242413401) | Run is not completed; check again after it finishes |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-06-25T18:35:23Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28192190034) | passed |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Daily invalid rule audit and safe repair | manual / schedule | 2026-06-25T18:36:58Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28192279630) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-06-25T18:57:32Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28193460653) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-06-25T19:08:25Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28194089805) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-06-25T19:18:33Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28194648635) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-06-25T19:01:50Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28193714015) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-06-25T21:58:24Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28203104967) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-06-21T19:04:17Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-06-26T13:38:14Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28241684914) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
