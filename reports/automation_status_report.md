# Automation Status Report

- Generated at: 2026-07-04 05:38:50 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `0ca00c99`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28676404378](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676404378) / completed | [28676404378](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676404378) / success | [28676404378](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676404378) / 2026-07-04 02:00:55 +0800 | 3.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28676433801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676433801) / completed | [28676433801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676433801) / success | [28676433801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676433801) / 2026-07-04 02:01:17 +0800 | 3.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28676533914](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676533914) / completed | [28676533914](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676533914) / success | [28676533914](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676533914) / 2026-07-04 02:03:38 +0800 | 3.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28676570699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676570699) / completed | [28676570699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676570699) / success | [28676570699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676570699) / 2026-07-04 02:04:30 +0800 | 3.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28677143825](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28677143825) / completed | [28677143825](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28677143825) / success | [28677143825](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28677143825) / 2026-07-04 02:19:07 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28678029048](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678029048) / completed | [28678029048](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678029048) / success | [28678029048](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678029048) / 2026-07-04 02:42:36 +0800 | 2.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | warn | [28684457263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684457263) / in_progress | [28623373028](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28623373028) / success | [28623373028](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28623373028) / 2026-07-03 05:41:53 +0800 | 23.9h | latest run is in_progress |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / completed | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / success | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / 2026-06-29 02:48:00 +0800 | 122.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [28633173916](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28633173916) / completed | [28633173916](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28633173916) / success | [28633173916](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28633173916) / 2026-07-03 09:52:23 +0800 | 19.8h | ok |
| `pages-deploy.yml` | workflow_run / manual / public-path push | observe | ok | [28678085233](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678085233) / completed | [28678085233](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678085233) / success | [28678085233](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678085233) / 2026-07-04 02:43:07 +0800 | 2.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28678085221](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678085221) / completed | [28678085221](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678085221) / success | [28678085221](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678085221) / 2026-07-04 02:42:45 +0800 | 2.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
