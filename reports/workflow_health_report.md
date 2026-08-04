# Workflow Health Report

- Generated at: 2026-08-05 02:15:35 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-07-15T20:01:53Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-08-04T18:14:44Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30937700344) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | 2026-08-03T18:23:40Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30841064463) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-08-03T18:28:35Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30841434545) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-08-03T18:53:46Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30843311923) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-08-03T18:59:24Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30843740958) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-08-03T18:28:53Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30841457449) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-08-03T21:37:13Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30855392320) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-08-02T18:34:05Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-08-03T21:38:04Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30855448884) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-08-03T21:38:45Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30855495089) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
