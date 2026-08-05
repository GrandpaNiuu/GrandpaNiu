# Automation Status Report

- Generated at: 2026-08-06 05:42:27 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `995701bb`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [31033274669](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033274669) / completed | [31033274669](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033274669) / success | [31033274669](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033274669) / 2026-08-06 02:09:03 +0800 | 3.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [31033340340](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033340340) / completed | [31033340340](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033340340) / success | [31033340340](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033340340) / 2026-08-06 02:09:30 +0800 | 3.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [31033548804](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033548804) / completed | [31033548804](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033548804) / success | [31033548804](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033548804) / 2026-08-06 02:12:03 +0800 | 3.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [31033606330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033606330) / completed | [31033606330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033606330) / success | [31033606330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033606330) / 2026-08-06 02:12:37 +0800 | 3.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [31035792585](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31035792585) / completed | [31035792585](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31035792585) / success | [31035792585](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31035792585) / 2026-08-06 02:40:28 +0800 | 3.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [31037122791](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31037122791) / completed | [31037122791](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31037122791) / success | [31037122791](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31037122791) / 2026-08-06 02:58:34 +0800 | 2.7h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [31049763932](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31049763932) / in_progress | [30953709032](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30953709032) / success | [30953709032](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30953709032) / 2026-08-05 05:46:34 +0800 | 23.9h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [30761407385](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) / completed | [30761407385](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) / success | [30761407385](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) / 2026-08-03 02:35:38 +0800 | 75.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 505.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [30953754947](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30953754947) / completed | [30953754947](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30953754947) / success | [30953754947](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30953754947) / 2026-08-05 05:47:17 +0800 | 23.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [31037259799](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31037259799) / completed | [31037259799](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31037259799) / success | [31037259799](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31037259799) / 2026-08-06 02:58:54 +0800 | 2.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
