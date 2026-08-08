# Automation Status Report

- Generated at: 2026-08-09 04:56:12 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `6d206d53`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [31268556534](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31268556534) / completed | [31268556534](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31268556534) / success | [31268556534](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31268556534) / 2026-08-09 01:06:43 +0800 | 3.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [31268586069](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31268586069) / completed | [31268586069](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31268586069) / success | [31268586069](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31268586069) / 2026-08-09 01:07:08 +0800 | 3.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [31268912521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31268912521) / completed | [31268912521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31268912521) / success | [31268912521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31268912521) / 2026-08-09 01:14:29 +0800 | 3.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [31268963252](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31268963252) / completed | [31268963252](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31268963252) / success | [31268963252](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31268963252) / 2026-08-09 01:15:32 +0800 | 3.7h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [31269891664](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31269891664) / completed | [31269891664](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31269891664) / success | [31269891664](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31269891664) / 2026-08-09 01:38:15 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [31270405251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31270405251) / completed | [31270405251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31270405251) / success | [31270405251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31270405251) / 2026-08-09 01:51:17 +0800 | 3.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [31278090405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31278090405) / in_progress | [31218743766](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31218743766) / success | [31218743766](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31218743766) / 2026-08-08 05:07:51 +0800 | 23.8h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31210016455](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210016455) / completed | [31210016455](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210016455) / success | [31210016455](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210016455) / 2026-08-08 03:08:10 +0800 | 25.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 25.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [31218797109](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31218797109) / completed | [31218797109](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31218797109) / success | [31218797109](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31218797109) / 2026-08-08 05:08:31 +0800 | 23.8h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [31270461576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31270461576) / completed | [31270461576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31270461576) / success | [31270461576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31270461576) / 2026-08-09 01:51:28 +0800 | 3.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
