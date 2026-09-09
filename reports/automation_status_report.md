# Automation Status Report

- Generated at: 2026-09-10 06:39:48 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `34ca910e`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [34395149692](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34395149692) / completed | [34395149692](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34395149692) / success | [34395149692](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34395149692) / 2026-09-10 03:29:03 +0800 | 3.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [34395237281](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34395237281) / completed | [34395237281](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34395237281) / success | [34395237281](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34395237281) / 2026-09-10 03:29:27 +0800 | 3.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [34395482121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34395482121) / completed | [34395482121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34395482121) / success | [34395482121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34395482121) / 2026-09-10 03:31:14 +0800 | 3.1h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [34395510954](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34395510954) / completed | [34395510954](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34395510954) / success | [34395510954](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34395510954) / 2026-09-10 03:31:34 +0800 | 3.1h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [34396436506](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34396436506) / completed | [34396436506](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34396436506) / success | [34396436506](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34396436506) / 2026-09-10 03:41:03 +0800 | 3.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [34397412323](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34397412323) / completed | [34397412323](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34397412323) / success | [34397412323](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34397412323) / 2026-09-10 03:52:55 +0800 | 2.8h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [34413298861](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34413298861) / in_progress | [34287812368](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34287812368) / success | [34287812368](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34287812368) / 2026-09-09 06:50:31 +0800 | 23.8h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / completed | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / success | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / 2026-09-07 03:28:25 +0800 | 75.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 795.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [34287876629](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34287876629) / completed | [34287876629](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34287876629) / success | [34287876629](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34287876629) / 2026-09-09 06:51:07 +0800 | 23.8h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [34397696372](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34397696372) / completed | [34397696372](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34397696372) / success | [34397696372](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34397696372) / 2026-09-10 03:53:06 +0800 | 2.8h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
