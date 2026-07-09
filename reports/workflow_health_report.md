# Workflow Health Report

- Generated at: 2026-07-10 03:16:25 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-07-09T19:15:26Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) | Run is not completed; check again after it finishes |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-07-09T18:21:50Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040380502) | passed |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Daily invalid rule audit and safe repair | manual / schedule | 2026-07-09T18:23:51Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040504976) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-07-09T18:29:41Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040858733) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | 2026-07-09T18:54:14Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042372852) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-07-09T19:01:16Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042810749) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-07-09T18:31:24Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040964440) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-07-08T21:38:23Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977562121) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-07-05T18:40:26Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) | passed |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | 2026-07-08T21:39:08Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977602081) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-07-09T19:03:02Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042918933) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
