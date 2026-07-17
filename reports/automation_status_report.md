# Automation Status Report

- Generated at: 2026-07-18 05:13:00 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `2344c81f`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [29601049046](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29601049046) / completed | [29601049046](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29601049046) / success | [29601049046](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29601049046) / 2026-07-18 01:43:17 +0800 | 3.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29601135299](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29601135299) / completed | [29601135299](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29601135299) / success | [29601135299](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29601135299) / 2026-07-18 01:43:59 +0800 | 3.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29601433409](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29601433409) / completed | [29601433409](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29601433409) / success | [29601433409](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29601433409) / 2026-07-18 01:48:28 +0800 | 3.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29601616482](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29601616482) / completed | [29601616482](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29601616482) / success | [29601616482](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29601616482) / 2026-07-18 01:51:21 +0800 | 3.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29602927090](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29602927090) / completed | [29602927090](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29602927090) / success | [29602927090](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29602927090) / 2026-07-18 02:12:34 +0800 | 3.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29603279745](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29603279745) / completed | [29603279745](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29603279745) / success | [29603279745](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29603279745) / 2026-07-18 02:18:57 +0800 | 2.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [29613941120](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29613941120) / in_progress | [29536300457](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29536300457) / success | [29536300457](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29536300457) / 2026-07-17 05:31:11 +0800 | 23.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / completed | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / success | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / 2026-07-13 02:31:34 +0800 | 122.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 49.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29536347221](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29536347221) / completed | [29536347221](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29536347221) / success | [29536347221](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29536347221) / 2026-07-17 05:31:49 +0800 | 23.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29603360572](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29603360572) / completed | [29603360572](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29603360572) / success | [29603360572](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29603360572) / 2026-07-18 02:19:08 +0800 | 2.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
