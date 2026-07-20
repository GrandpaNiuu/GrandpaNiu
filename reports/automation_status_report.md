# Automation Status Report

- Generated at: 2026-07-21 05:39:23 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `396ef5b9`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [29768092104](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29768092104) / completed | [29768092104](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29768092104) / success | [29768092104](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29768092104) / 2026-07-21 02:32:09 +0800 | 3.1h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29768114576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29768114576) / completed | [29768114576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29768114576) / success | [29768114576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29768114576) / 2026-07-21 02:32:27 +0800 | 3.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29769057755](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29769057755) / completed | [29769057755](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29769057755) / success | [29769057755](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29769057755) / 2026-07-21 02:45:09 +0800 | 2.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29769118634](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29769118634) / completed | [29769118634](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29769118634) / success | [29769118634](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29769118634) / 2026-07-21 02:45:49 +0800 | 2.9h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29770121522](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29770121522) / completed | [29770121522](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29770121522) / success | [29770121522](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29770121522) / 2026-07-21 03:00:13 +0800 | 2.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29770884302](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29770884302) / completed | [29770884302](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29770884302) / success | [29770884302](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29770884302) / 2026-07-21 03:12:02 +0800 | 2.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [29781006174](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29781006174) / in_progress | [29703952789](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29703952789) / success | [29703952789](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29703952789) / 2026-07-20 05:13:29 +0800 | 24.4h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / completed | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / success | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / 2026-07-20 02:33:21 +0800 | 27.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 121.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29703968655](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29703968655) / completed | [29703968655](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29703968655) / success | [29703968655](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29703968655) / 2026-07-20 05:14:09 +0800 | 24.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29770995016](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29770995016) / completed | [29770995016](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29770995016) / success | [29770995016](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29770995016) / 2026-07-21 03:12:16 +0800 | 2.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
