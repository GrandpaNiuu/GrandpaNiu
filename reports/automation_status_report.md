# Automation Status Report

- Generated at: 2026-08-26 01:08:53 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `4e46dbcc`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [32876068348](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32876068348) / in_progress | [32754868474](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32754868474) / success | [32754868474](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32754868474) / 2026-08-25 01:09:30 +0800 | 24.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [32755368195](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32755368195) / completed | [32755368195](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32755368195) / success | [32755368195](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32755368195) / 2026-08-25 01:14:02 +0800 | 23.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [32755726913](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32755726913) / completed | [32755726913](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32755726913) / success | [32755726913](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32755726913) / 2026-08-25 01:17:37 +0800 | 23.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [32755851318](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32755851318) / completed | [32755851318](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32755851318) / success | [32755851318](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32755851318) / 2026-08-25 01:18:51 +0800 | 23.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [32757652337](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32757652337) / completed | [32757652337](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32757652337) / success | [32757652337](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32757652337) / 2026-08-25 01:37:46 +0800 | 23.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [32758893770](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32758893770) / completed | [32758893770](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32758893770) / success | [32758893770](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32758893770) / 2026-08-25 01:52:26 +0800 | 23.3h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [32776724756](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32776724756) / completed | [32776724756](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32776724756) / success | [32776724756](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32776724756) / 2026-08-25 04:57:07 +0800 | 20.2h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / completed | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / success | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / 2026-08-24 01:52:11 +0800 | 47.3h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 430.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [32776802564](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32776802564) / completed | [32776802564](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32776802564) / success | [32776802564](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32776802564) / 2026-08-25 04:57:45 +0800 | 20.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [32776859986](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32776859986) / completed | [32776859986](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32776859986) / success | [32776859986](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32776859986) / 2026-08-25 04:57:57 +0800 | 20.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
