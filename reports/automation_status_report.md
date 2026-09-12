# Automation Status Report

- Generated at: 2026-09-13 06:26:23 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `11c6eadf`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [34711995391](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34711995391) / completed | [34711995391](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34711995391) / success | [34711995391](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34711995391) / 2026-09-13 02:43:24 +0800 | 3.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [34712098475](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34712098475) / completed | [34712098475](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34712098475) / success | [34712098475](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34712098475) / 2026-09-13 02:44:51 +0800 | 3.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [34712292727](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34712292727) / completed | [34712292727](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34712292727) / success | [34712292727](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34712292727) / 2026-09-13 02:48:55 +0800 | 3.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [34712321103](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34712321103) / completed | [34712321103](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34712321103) / success | [34712321103](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34712321103) / 2026-09-13 02:49:22 +0800 | 3.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [34713249738](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34713249738) / completed | [34713249738](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34713249738) / success | [34713249738](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34713249738) / 2026-09-13 03:08:52 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [34714164358](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34714164358) / completed | [34714164358](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34714164358) / success | [34714164358](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34714164358) / 2026-09-13 03:27:40 +0800 | 3.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [34722738932](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34722738932) / in_progress | [34655097856](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34655097856) / success | [34655097856](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34655097856) / 2026-09-12 06:42:16 +0800 | 23.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / completed | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / success | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / 2026-09-07 03:28:25 +0800 | 147.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 867.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [34655148793](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34655148793) / completed | [34655148793](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34655148793) / success | [34655148793](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34655148793) / 2026-09-12 06:42:55 +0800 | 23.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [34714237620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34714237620) / completed | [34714237620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34714237620) / success | [34714237620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34714237620) / 2026-09-13 03:27:51 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
