# Workflow Health Report

- Generated at: 2026-07-03 08:14:38 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | 2026-07-02T20:38:28Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28620051086) | passed |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | 2026-07-02T18:17:13Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612079280) | passed |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Daily invalid rule audit and safe repair | manual / schedule | 2026-07-02T18:18:21Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612144710) | passed |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | 2026-07-02T18:20:21Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612258753) | passed |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | unconfirmed | unconfirmed | unconfirmed | - | config exists; check Builder.py --profile fusion --release, commit, rebase retry |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | 2026-07-02T23:38:22Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28628442431) | passed |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | 2026-07-02T18:20:32Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612269717) | passed |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | 2026-07-02T21:41:30Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28623373028) | passed |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | unconfirmed | unconfirmed | unconfirmed | - | config exists; check governance files, duplicate scripts, duplicate MITM, report freshness |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with stale deployment cancellation | manual / push / workflow_run | 2026-07-02T23:39:30Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28628484084) | passed |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | 2026-07-02T23:39:30Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28628484098) | passed |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
