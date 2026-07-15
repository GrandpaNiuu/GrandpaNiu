# Automation Status Report

- Generated at: 2026-07-16 00:06:04 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `a8eeaf7d`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [29354970352](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29354970352) / completed | [29354970352](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29354970352) / success | [29354970352](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29354970352) / 2026-07-15 01:45:03 +0800 | 22.4h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29355038894](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355038894) / completed | [29355038894](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355038894) / success | [29355038894](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355038894) / 2026-07-15 01:45:30 +0800 | 22.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29355378346](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355378346) / completed | [29355378346](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355378346) / success | [29355378346](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355378346) / 2026-07-15 01:50:15 +0800 | 22.3h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29355488700](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355488700) / completed | [29355488700](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355488700) / success | [29355488700](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29355488700) / 2026-07-15 01:52:08 +0800 | 22.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29356798709](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29356798709) / completed | [29356798709](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29356798709) / success | [29356798709](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29356798709) / 2026-07-15 02:11:33 +0800 | 21.9h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29358315602](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29358315602) / completed | [29358315602](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29358315602) / success | [29358315602](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29358315602) / 2026-07-15 02:34:30 +0800 | 21.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [29369660755](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29369660755) / completed | [29369660755](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29369660755) / success | [29369660755](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29369660755) / 2026-07-15 05:29:09 +0800 | 18.6h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / completed | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / success | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / 2026-07-13 02:31:34 +0800 | 69.6h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / completed | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / success | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / 2026-07-10 03:16:51 +0800 | 140.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29369696746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29369696746) / completed | [29369696746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29369696746) / success | [29369696746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29369696746) / 2026-07-15 05:29:45 +0800 | 18.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29369696765](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29369696765) / completed | [29369696765](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29369696765) / success | [29369696765](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29369696765) / 2026-07-15 05:29:20 +0800 | 18.6h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
