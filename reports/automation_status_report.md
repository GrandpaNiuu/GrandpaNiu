# Automation Status Report

- Generated at: 2026-08-08 01:29:28 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `15dbff09`
- Overall status: `fail`
- Blocking findings: 12
- Warnings: 2

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | fail | [31202448001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31202448001) / in_progress | [31125455414](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31125455414) / failure | [31033274669](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033274669) / 2026-08-06 02:09:03 +0800 | 47.3h | last success is stale (47.3h > 40h)<br>latest completed run is failure |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | fail | [31125486713](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31125486713) / completed | [31125486713](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31125486713) / failure | [31033340340](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033340340) / 2026-08-06 02:09:30 +0800 | 47.3h | last success is stale (47.3h > 40h)<br>latest completed run is failure |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | fail | [31125678821](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31125678821) / completed | [31125678821](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31125678821) / failure | [31033548804](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033548804) / 2026-08-06 02:12:03 +0800 | 47.3h | last success is stale (47.3h > 40h)<br>latest completed run is failure |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | fail | [31125672578](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31125672578) / completed | [31125672578](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31125672578) / failure | [31033606330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31033606330) / 2026-08-06 02:12:37 +0800 | 47.3h | last success is stale (47.3h > 40h)<br>latest completed run is failure |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | fail | [31126104917](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31126104917) / completed | [31126104917](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31126104917) / failure | [31035792585](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31035792585) / 2026-08-06 02:40:28 +0800 | 46.8h | last success is stale (46.8h > 40h)<br>latest completed run is failure |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [31126263570](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31126263570) / completed | [31126263570](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31126263570) / failure | [31037122791](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31037122791) / 2026-08-06 02:58:34 +0800 | 46.5h | last success is stale (46.5h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | warn | [31136346831](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31136346831) / completed | [31136346831](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31136346831) / failure | [31049763932](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31049763932) / 2026-08-06 05:42:46 +0800 | 43.8h | latest completed run is failure on older commit c002c3ff; current commit 15dbff09 will be checked by the next run |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [30761407385](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) / completed | [30761407385](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) / success | [30761407385](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) / 2026-08-03 02:35:38 +0800 | 118.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 549.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [31136461751](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31136461751) / completed | [31136461751](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31136461751) / success | [31136461751](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31136461751) / 2026-08-07 08:58:22 +0800 | 16.5h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [31136472234](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31136472234) / completed | [31136472234](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31136472234) / success | [31136472234](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31136472234) / 2026-08-07 08:58:34 +0800 | 16.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
