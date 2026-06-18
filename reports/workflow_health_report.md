# Workflow Health Report

- Generated at: 2026-06-19 02:34:04 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 9

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-06-18T16:23:49Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27773789337) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-06-18T18:33:45Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27781111570) | Run is not completed; check again after it finishes |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Daily invalid rule audit and safe repair | manual / schedule / push | 2026-06-18T18:33:54Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27781120164) | Run is not completed; check again after it finishes |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-06-17T17:30:10Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27707564669) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule / push | 2026-06-17T17:57:02Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27709107004) | passed |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-06-17T19:07:47Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27713132706) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-06-17T17:29:05Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27707501055) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | 2026-06-15T19:36:18Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27571392238) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-06-18T16:24:23Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27773822465) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
