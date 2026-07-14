# Automation Status Report

- Generated at: 2026-07-15 01:44:41 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `e39fac54`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | warn | [29354970352](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29354970352) / in_progress | [29273976206](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29273976206) / success | [29273976206](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29273976206) / 2026-07-14 02:20:33 +0800 | 23.4h | latest run is in_progress |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29274015647](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29274015647) / completed | [29274015647](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29274015647) / success | [29274015647](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29274015647) / 2026-07-14 02:20:59 +0800 | 23.4h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29274174671](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29274174671) / completed | [29274174671](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29274174671) / success | [29274174671](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29274174671) / 2026-07-14 02:22:47 +0800 | 23.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29274227923](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29274227923) / completed | [29274227923](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29274227923) / success | [29274227923](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29274227923) / 2026-07-14 02:23:29 +0800 | 23.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29275829866](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29275829866) / completed | [29275829866](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29275829866) / success | [29275829866](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29275829866) / 2026-07-14 02:47:19 +0800 | 23.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29276173626](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29276173626) / completed | [29276173626](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29276173626) / success | [29276173626](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29276173626) / 2026-07-14 02:53:03 +0800 | 22.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [29286380982](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286380982) / completed | [29286380982](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286380982) / success | [29286380982](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286380982) / 2026-07-14 05:27:36 +0800 | 20.3h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / completed | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / success | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / 2026-07-13 02:31:34 +0800 | 47.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / completed | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / success | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / 2026-07-10 03:16:51 +0800 | 118.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29286420311](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286420311) / completed | [29286420311](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286420311) / success | [29286420311](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286420311) / 2026-07-14 05:28:08 +0800 | 20.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29286420711](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286420711) / completed | [29286420711](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286420711) / success | [29286420711](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286420711) / 2026-07-14 05:27:50 +0800 | 20.3h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
