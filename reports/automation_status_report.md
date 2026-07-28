# Automation Status Report

- Generated at: 2026-07-29 02:01:19 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `6dadca60`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [30385455438](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385455438) / in_progress | [30292467422](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30292467422) / success | [30292467422](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30292467422) / 2026-07-28 02:10:16 +0800 | 23.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [30292630209](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30292630209) / completed | [30292630209](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30292630209) / success | [30292630209](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30292630209) / 2026-07-28 02:11:32 +0800 | 23.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [30292871454](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30292871454) / completed | [30292871454](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30292871454) / success | [30292871454](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30292871454) / 2026-07-28 02:14:57 +0800 | 23.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [30292889963](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30292889963) / completed | [30292889963](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30292889963) / success | [30292889963](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30292889963) / 2026-07-28 02:15:17 +0800 | 23.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [30294808866](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30294808866) / completed | [30294808866](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30294808866) / success | [30294808866](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30294808866) / 2026-07-28 02:41:00 +0800 | 23.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [30295580187](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30295580187) / completed | [30295580187](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30295580187) / success | [30295580187](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30295580187) / 2026-07-28 02:52:11 +0800 | 23.2h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [30307518208](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30307518208) / completed | [30307518208](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30307518208) / success | [30307518208](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30307518208) / 2026-07-28 05:36:30 +0800 | 20.4h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / completed | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / success | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / 2026-07-27 02:38:20 +0800 | 47.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 310.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [30307567631](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30307567631) / completed | [30307567631](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30307567631) / success | [30307567631](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30307567631) / 2026-07-28 05:37:09 +0800 | 20.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [30307611138](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30307611138) / completed | [30307611138](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30307611138) / success | [30307611138](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30307611138) / 2026-07-28 05:37:18 +0800 | 20.4h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
