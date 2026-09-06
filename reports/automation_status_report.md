# Automation Status Report

- Generated at: 2026-09-07 02:37:21 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `4351ec5f`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [34052254702](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052254702) / in_progress | [33984400171](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33984400171) / success | [33984400171](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33984400171) / 2026-09-06 02:33:53 +0800 | 24.1h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [34052294366](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052294366) / in_progress | [33984438042](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33984438042) / success | [33984438042](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33984438042) / 2026-09-06 02:34:11 +0800 | 24.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [33984532618](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33984532618) / completed | [33984532618](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33984532618) / success | [33984532618](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33984532618) / 2026-09-06 02:35:59 +0800 | 24.0h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [33984572849](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33984572849) / completed | [33984572849](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33984572849) / success | [33984572849](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33984572849) / 2026-09-06 02:36:30 +0800 | 24.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [33985600871](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33985600871) / completed | [33985600871](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33985600871) / success | [33985600871](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33985600871) / 2026-09-06 02:57:29 +0800 | 23.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [33986076236](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33986076236) / completed | [33986076236](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33986076236) / success | [33986076236](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33986076236) / 2026-09-06 03:07:20 +0800 | 23.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [33995021545](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33995021545) / completed | [33995021545](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33995021545) / success | [33995021545](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33995021545) / 2026-09-06 06:08:32 +0800 | 20.5h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / completed | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / success | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / 2026-08-31 04:00:57 +0800 | 166.6h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 719.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [33995048597](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33995048597) / completed | [33995048597](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33995048597) / success | [33995048597](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33995048597) / 2026-09-06 06:09:04 +0800 | 20.5h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [33995075339](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33995075339) / completed | [33995075339](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33995075339) / success | [33995075339](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33995075339) / 2026-09-06 06:09:14 +0800 | 20.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
