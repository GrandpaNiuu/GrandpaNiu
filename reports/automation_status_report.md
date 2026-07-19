# Automation Status Report

- Generated at: 2026-07-20 02:33:06 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `cdda216c`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [29697178130](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29697178130) / completed | [29697178130](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29697178130) / success | [29697178130](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29697178130) / 2026-07-20 01:38:26 +0800 | 55m | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29697244882](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29697244882) / completed | [29697244882](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29697244882) / success | [29697244882](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29697244882) / 2026-07-20 01:39:39 +0800 | 53m | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29697390158](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29697390158) / completed | [29697390158](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29697390158) / success | [29697390158](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29697390158) / 2026-07-20 01:43:58 +0800 | 49m | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29697406776](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29697406776) / completed | [29697406776](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29697406776) / success | [29697406776](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29697406776) / 2026-07-20 01:44:21 +0800 | 49m | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29697968637](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29697968637) / completed | [29697968637](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29697968637) / success | [29697968637](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29697968637) / 2026-07-20 02:02:07 +0800 | 31m | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29698278489](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698278489) / completed | [29698278489](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698278489) / success | [29698278489](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698278489) / 2026-07-20 02:12:44 +0800 | 20m | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [29661146939](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29661146939) / completed | [29661146939](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29661146939) / success | [29661146939](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29661146939) / 2026-07-19 05:12:18 +0800 | 21.3h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / in_progress | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / success | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / 2026-07-13 02:31:34 +0800 | 168.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 94.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29661166012](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29661166012) / completed | [29661166012](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29661166012) / success | [29661166012](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29661166012) / 2026-07-19 05:12:55 +0800 | 21.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29698316992](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698316992) / completed | [29698316992](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698316992) / success | [29698316992](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698316992) / 2026-07-20 02:12:56 +0800 | 20m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
