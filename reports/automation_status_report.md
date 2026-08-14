# Automation Status Report

- Generated at: 2026-08-15 04:53:57 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `8e3b2861`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [31824512688](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31824512688) / completed | [31824512688](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31824512688) / success | [31824512688](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31824512688) / 2026-08-15 01:34:26 +0800 | 3.3h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [31824681886](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31824681886) / completed | [31824681886](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31824681886) / success | [31824681886](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31824681886) / 2026-08-15 01:35:49 +0800 | 3.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [31825031731](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31825031731) / completed | [31825031731](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31825031731) / success | [31825031731](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31825031731) / 2026-08-15 01:40:31 +0800 | 3.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [31825107477](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31825107477) / completed | [31825107477](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31825107477) / success | [31825107477](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31825107477) / 2026-08-15 01:41:21 +0800 | 3.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [31826353258](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31826353258) / completed | [31826353258](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31826353258) / success | [31826353258](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31826353258) / 2026-08-15 01:57:37 +0800 | 2.9h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [31827291897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31827291897) / completed | [31827291897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31827291897) / success | [31827291897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31827291897) / 2026-08-15 02:10:45 +0800 | 2.7h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [31839997885](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31839997885) / in_progress | [31744516125](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31744516125) / success | [31744516125](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31744516125) / 2026-08-14 05:12:19 +0800 | 23.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / completed | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / success | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / 2026-08-10 02:02:48 +0800 | 122.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 169.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [31744569287](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31744569287) / completed | [31744569287](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31744569287) / success | [31744569287](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31744569287) / 2026-08-14 05:12:50 +0800 | 23.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [31827436375](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31827436375) / completed | [31827436375](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31827436375) / success | [31827436375](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31827436375) / 2026-08-15 02:10:55 +0800 | 2.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
