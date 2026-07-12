# Automation Status Report

- Generated at: 2026-07-13 02:31:16 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `74b60630`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [29202375935](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202375935) / completed | [29202375935](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202375935) / success | [29202375935](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202375935) / 2026-07-13 01:39:51 +0800 | 51m | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29202430654](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202430654) / completed | [29202430654](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202430654) / success | [29202430654](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202430654) / 2026-07-13 01:41:01 +0800 | 50m | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29202563704](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202563704) / completed | [29202563704](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202563704) / success | [29202563704](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202563704) / 2026-07-13 01:45:06 +0800 | 46m | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29202594423](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202594423) / completed | [29202594423](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202594423) / success | [29202594423](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202594423) / 2026-07-13 01:46:09 +0800 | 45m | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29203139469](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203139469) / completed | [29203139469](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203139469) / success | [29203139469](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203139469) / 2026-07-13 02:03:37 +0800 | 28m | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29203412814](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203412814) / completed | [29203412814](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203412814) / success | [29203412814](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203412814) / 2026-07-13 02:12:57 +0800 | 18m | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [29168396768](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168396768) / completed | [29168396768](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168396768) / success | [29168396768](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168396768) / 2026-07-12 05:13:03 +0800 | 21.3h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | warn | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / in_progress | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / success | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / 2026-07-06 02:41:30 +0800 | 167.8h | latest run is in_progress |
| `module-factory-build.yml` | push/manual | observe | ok | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / completed | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / success | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / 2026-07-10 03:16:51 +0800 | 71.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29168411983](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168411983) / completed | [29168411983](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168411983) / success | [29168411983](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168411983) / 2026-07-12 05:13:42 +0800 | 21.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29203453421](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203453421) / completed | [29203453421](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203453421) / success | [29203453421](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203453421) / 2026-07-13 02:13:06 +0800 | 18m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
