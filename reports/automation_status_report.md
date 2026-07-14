# Automation Status Report

- Generated at: 2026-07-15 05:28:50 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `d1225e9b`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [29354970352](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29354970352) / completed | [29354970352](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29354970352) / success | [29354970352](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29354970352) / 2026-07-15 01:45:03 +0800 | 3.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29355038894](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355038894) / completed | [29355038894](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355038894) / success | [29355038894](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355038894) / 2026-07-15 01:45:30 +0800 | 3.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29355378346](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355378346) / completed | [29355378346](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355378346) / success | [29355378346](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355378346) / 2026-07-15 01:50:15 +0800 | 3.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29355488700](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355488700) / completed | [29355488700](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355488700) / success | [29355488700](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355488700) / 2026-07-15 01:52:08 +0800 | 3.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29356798709](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29356798709) / completed | [29356798709](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29356798709) / success | [29356798709](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29356798709) / 2026-07-15 02:11:33 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29358315602](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29358315602) / completed | [29358315602](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29358315602) / success | [29358315602](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29358315602) / 2026-07-15 02:34:30 +0800 | 2.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | warn | [29369660755](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29369660755) / in_progress | [29286380982](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286380982) / success | [29286380982](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286380982) / 2026-07-14 05:27:36 +0800 | 24.0h | latest run is in_progress |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / completed | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / success | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / 2026-07-13 02:31:34 +0800 | 51.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / completed | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / success | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / 2026-07-10 03:16:51 +0800 | 122.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29286420311](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286420311) / completed | [29286420311](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286420311) / success | [29286420311](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29286420311) / 2026-07-14 05:28:08 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29358416976](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29358416976) / completed | [29358416976](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29358416976) / success | [29358416976](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29358416976) / 2026-07-15 02:34:41 +0800 | 2.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
