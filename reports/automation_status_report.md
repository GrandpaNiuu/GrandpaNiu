# Automation Status Report

- Generated at: 2026-07-05 01:38:48 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `e1988022`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | warn | [28714307591](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28714307591) / in_progress | [28676404378](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676404378) / success | [28676404378](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676404378) / 2026-07-04 02:00:55 +0800 | 23.6h | latest run is in_progress |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28676433801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676433801) / completed | [28676433801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676433801) / success | [28676433801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676433801) / 2026-07-04 02:01:17 +0800 | 23.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28676533914](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676533914) / completed | [28676533914](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676533914) / success | [28676533914](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676533914) / 2026-07-04 02:03:38 +0800 | 23.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28676570699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676570699) / completed | [28676570699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676570699) / success | [28676570699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28676570699) / 2026-07-04 02:04:30 +0800 | 23.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28677143825](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28677143825) / completed | [28677143825](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28677143825) / success | [28677143825](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28677143825) / 2026-07-04 02:19:07 +0800 | 23.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28678029048](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678029048) / completed | [28678029048](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678029048) / success | [28678029048](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28678029048) / 2026-07-04 02:42:36 +0800 | 22.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28684457263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684457263) / completed | [28684457263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684457263) / success | [28684457263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28684457263) / 2026-07-04 05:39:08 +0800 | 20.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28695947613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28695947613) / completed | [28695947613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28695947613) / success | [28695947613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28695947613) / 2026-07-04 13:16:27 +0800 | 12.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [28692446521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28692446521) / completed | [28692446521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28692446521) / success | [28692446521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28692446521) / 2026-07-04 10:43:05 +0800 | 14.9h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual / public-path push | observe | ok | [28692481885](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28692481885) / completed | [28692481885](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28692481885) / success | [28692481885](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28692481885) / 2026-07-04 10:43:37 +0800 | 14.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28695973094](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28695973094) / completed | [28695973094](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28695973094) / success | [28695973094](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28695973094) / 2026-07-04 13:16:37 +0800 | 12.4h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
