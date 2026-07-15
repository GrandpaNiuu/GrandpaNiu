# Workflow Health Report

- Generated at: 2026-07-16 02:53:44 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Workflows checked: 11

| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | Build Release and sync Root | manual / push | unconfirmed | unconfirmed | unconfirmed | - | config exists; check Builder, profile, source merge, Root/Release sync |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | Daily module date, build, report and validation | manual / schedule | unconfirmed | unconfirmed | unconfirmed | - | config exists; check date refresh, Builder, validation, rebase retry |
| Daily invalid rule audit and safe repair | `.github/workflows/daily-audit-and-repair.yml` | Report-only generated module integrity audit | manual / schedule | unconfirmed | unconfirmed | unconfirmed | - | config exists; check current Release validation, report-only generated-module audit, rebase retry |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | Daily invalid source audit and repair | manual / schedule | unconfirmed | unconfirmed | unconfirmed | - | config exists; check network fetch, invalid history, conservative source repair |
| Scheduled Module Factory Update | `.github/workflows/scheduled-module-update.yml` | Scheduled module factory build and publish | manual / schedule | unconfirmed | unconfirmed | unconfirmed | - | config exists; check Builder.py --profile fusion --release, commit, rebase retry |
| Upstream app module sync | `.github/workflows/upstream-app-module-sync.yml` | Sync upstream app modules and validate build | manual / schedule | unconfirmed | unconfirmed | unconfirmed | - | config exists; check app-modules.json, upstream fetch, rollback on failed build |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | Collect trusted upstream candidates | manual / schedule | unconfirmed | unconfirmed | unconfirmed | - | config exists; check candidates.json, risk filters, trusted repositories |
| Daily schedule watchdog | `.github/workflows/daily-schedule-watchdog.yml` | Recover the daily module refresh if GitHub drops a scheduled run | manual / schedule | unconfirmed | unconfirmed | unconfirmed | - | config exists; check module update-date, recovery build, rebase retry |
| Repository Health Check | `.github/workflows/repository-health.yml` | Repository governance health check | manual / schedule | unconfirmed | unconfirmed | unconfirmed | - | config exists; check governance files, duplicate scripts, duplicate MITM, report freshness |
| Deploy GitHub Pages | `.github/workflows/pages-deploy.yml` | Publish the static Pages artifact with serialized deploy retries | manual / workflow_run | unconfirmed | unconfirmed | unconfirmed | - | config exists; check Pages artifact scope, deploy-pages timeout, deployment retry guard |
| Workflow failure issue | `.github/workflows/workflow-failure-issue.yml` | Create or update issues for failed Actions | workflow_run | unconfirmed | unconfirmed | unconfirmed | - | config exists; check workflow_run permissions, issue creation/update |

## Notes

- Only `success` is treated as a fully passing latest run.
- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.
- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.
- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.
