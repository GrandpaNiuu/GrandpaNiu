# Automation Status Report

- Generated at: 2026-08-26 04:53:19 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `b2cb4e19`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [32876068348](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32876068348) / completed | [32876068348](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32876068348) / success | [32876068348](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32876068348) / 2026-08-26 01:09:19 +0800 | 3.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [32876560778](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32876560778) / completed | [32876560778](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32876560778) / success | [32876560778](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32876560778) / 2026-08-26 01:13:36 +0800 | 3.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [32876951074](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32876951074) / completed | [32876951074](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32876951074) / success | [32876951074](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32876951074) / 2026-08-26 01:17:32 +0800 | 3.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [32877044467](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32877044467) / completed | [32877044467](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32877044467) / success | [32877044467](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32877044467) / 2026-08-26 01:18:17 +0800 | 3.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [32878968670](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32878968670) / completed | [32878968670](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32878968670) / success | [32878968670](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32878968670) / 2026-08-26 01:38:12 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [32880041578](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32880041578) / completed | [32880041578](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32880041578) / success | [32880041578](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32880041578) / 2026-08-26 01:50:49 +0800 | 3.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [32897907188](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32897907188) / in_progress | [32776724756](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32776724756) / success | [32776724756](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32776724756) / 2026-08-25 04:57:07 +0800 | 23.9h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / completed | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / success | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / 2026-08-24 01:52:11 +0800 | 51.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 433.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [32776802564](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32776802564) / completed | [32776802564](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32776802564) / success | [32776802564](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32776802564) / 2026-08-25 04:57:45 +0800 | 23.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [32880285581](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32880285581) / completed | [32880285581](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32880285581) / success | [32880285581](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32880285581) / 2026-08-26 01:50:59 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
