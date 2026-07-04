# Automation Status Report

- Generated at: 2026-07-04 10:12:50 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `5cb4c037`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28676404378](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676404378) / completed | [28676404378](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676404378) / success | [28676404378](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676404378) / 2026-07-04 02:00:55 +0800 | 8.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28676433801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676433801) / completed | [28676433801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676433801) / success | [28676433801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676433801) / 2026-07-04 02:01:17 +0800 | 8.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28676533914](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676533914) / completed | [28676533914](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676533914) / success | [28676533914](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676533914) / 2026-07-04 02:03:38 +0800 | 8.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28676570699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676570699) / completed | [28676570699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676570699) / success | [28676570699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676570699) / 2026-07-04 02:04:30 +0800 | 8.1h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28677143825](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28677143825) / completed | [28677143825](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28677143825) / success | [28677143825](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28677143825) / 2026-07-04 02:19:07 +0800 | 7.9h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28678029048](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678029048) / completed | [28678029048](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678029048) / success | [28678029048](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678029048) / 2026-07-04 02:42:36 +0800 | 7.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28684457263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684457263) / completed | [28684457263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684457263) / success | [28684457263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684457263) / 2026-07-04 05:39:08 +0800 | 4.6h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / completed | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / success | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / 2026-06-29 02:48:00 +0800 | 127.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [28633173916](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28633173916) / completed | [28633173916](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28633173916) / success | [28633173916](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28633173916) / 2026-07-03 09:52:23 +0800 | 24.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual / public-path push | observe | ok | [28684473213](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684473213) / completed | [28684473213](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684473213) / success | [28684473213](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684473213) / 2026-07-04 05:39:42 +0800 | 4.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28684473227](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684473227) / completed | [28684473227](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684473227) / success | [28684473227](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684473227) / 2026-07-04 05:39:20 +0800 | 4.6h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
