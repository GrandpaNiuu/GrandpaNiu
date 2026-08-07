# Automation Status Report

- Generated at: 2026-08-08 03:09:09 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `a59b93eb`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [31202448001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31202448001) / completed | [31202448001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31202448001) / success | [31202448001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31202448001) / 2026-08-08 01:29:50 +0800 | 1.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [31202571630](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31202571630) / completed | [31202571630](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31202571630) / success | [31202571630](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31202571630) / 2026-08-08 01:30:27 +0800 | 1.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [31203012279](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31203012279) / completed | [31203012279](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31203012279) / success | [31203012279](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31203012279) / 2026-08-08 01:36:42 +0800 | 1.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [31203018047](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31203018047) / completed | [31203018047](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31203018047) / success | [31203018047](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31203018047) / 2026-08-08 01:36:49 +0800 | 1.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [31204375344](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31204375344) / completed | [31204375344](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31204375344) / success | [31204375344](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31204375344) / 2026-08-08 01:54:04 +0800 | 1.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [31205363518](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31205363518) / completed | [31205363518](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31205363518) / success | [31205363518](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31205363518) / 2026-08-08 02:07:01 +0800 | 1.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [31209978268](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31209978268) / completed | [31209978268](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31209978268) / success | [31209978268](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31209978268) / 2026-08-08 03:06:58 +0800 | 2m | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31210016455](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210016455) / completed | [31210016455](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210016455) / success | [31210016455](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210016455) / 2026-08-08 03:08:10 +0800 | 1m | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / in_progress | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 551.1h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [31210038683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210038683) / completed | [31210038683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210038683) / success | [31210038683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210038683) / 2026-08-08 03:07:33 +0800 | 2m | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [31210125897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210125897) / completed | [31210125897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210125897) / success | [31210125897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210125897) / 2026-08-08 03:08:23 +0800 | 1m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
