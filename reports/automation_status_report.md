# Automation Status Report

- Generated at: 2026-07-14 02:20:07 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `e8c27dbc`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 2

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | warn | [29273976206](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29273976206) / in_progress | [29202375935](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202375935) / success | [29202375935](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202375935) / 2026-07-13 01:39:51 +0800 | 24.7h | latest run is in_progress |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | warn | [29274015647](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29274015647) / in_progress | [29202430654](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202430654) / success | [29202430654](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202430654) / 2026-07-13 01:41:01 +0800 | 24.7h | latest run is in_progress |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29202563704](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202563704) / completed | [29202563704](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202563704) / success | [29202563704](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202563704) / 2026-07-13 01:45:06 +0800 | 24.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29202594423](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202594423) / completed | [29202594423](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202594423) / success | [29202594423](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202594423) / 2026-07-13 01:46:09 +0800 | 24.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29203139469](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203139469) / completed | [29203139469](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203139469) / success | [29203139469](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203139469) / 2026-07-13 02:03:37 +0800 | 24.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29203412814](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203412814) / completed | [29203412814](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203412814) / success | [29203412814](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203412814) / 2026-07-13 02:12:57 +0800 | 24.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [29209213979](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29209213979) / completed | [29209213979](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29209213979) / success | [29209213979](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29209213979) / 2026-07-13 05:14:04 +0800 | 21.1h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / completed | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / success | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / 2026-07-13 02:31:34 +0800 | 23.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / completed | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / success | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / 2026-07-10 03:16:51 +0800 | 95.1h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29209243884](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29209243884) / completed | [29209243884](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29209243884) / success | [29209243884](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29209243884) / 2026-07-13 05:14:39 +0800 | 21.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29209243779](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29209243779) / completed | [29209243779](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29209243779) / success | [29209243779](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29209243779) / 2026-07-13 05:14:14 +0800 | 21.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
