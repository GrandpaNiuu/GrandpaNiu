# Automation Status Report

- Generated at: 2026-07-17 05:30:49 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `3b63b80c`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [29521298802](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29521298802) / completed | [29521298802](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29521298802) / success | [29521298802](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29521298802) / 2026-07-17 01:49:43 +0800 | 3.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29521376240](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29521376240) / completed | [29521376240](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29521376240) / success | [29521376240](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29521376240) / 2026-07-17 01:50:12 +0800 | 3.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29521727623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29521727623) / completed | [29521727623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29521727623) / success | [29521727623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29521727623) / 2026-07-17 01:55:05 +0800 | 3.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29521791354](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29521791354) / completed | [29521791354](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29521791354) / success | [29521791354](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29521791354) / 2026-07-17 01:55:59 +0800 | 3.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29523019642](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29523019642) / completed | [29523019642](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29523019642) / success | [29523019642](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29523019642) / 2026-07-17 02:13:30 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29524508021](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29524508021) / completed | [29524508021](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29524508021) / success | [29524508021](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29524508021) / 2026-07-17 02:35:53 +0800 | 2.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [29536300457](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29536300457) / in_progress | [29452032621](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29452032621) / success | [29452032621](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29452032621) / 2026-07-16 05:28:46 +0800 | 24.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / completed | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / success | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / 2026-07-13 02:31:34 +0800 | 99.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 25.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29452072342](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29452072342) / completed | [29452072342](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29452072342) / success | [29452072342](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29452072342) / 2026-07-16 05:29:16 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29524600159](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29524600159) / completed | [29524600159](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29524600159) / success | [29524600159](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29524600159) / 2026-07-17 02:36:05 +0800 | 2.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
