# Automation Status Report

- Generated at: 2026-08-02 05:22:40 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `321df12b`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [30710712057](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30710712057) / completed | [30710712057](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30710712057) / success | [30710712057](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30710712057) / 2026-08-02 01:38:05 +0800 | 3.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [30710805988](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30710805988) / completed | [30710805988](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30710805988) / success | [30710805988](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30710805988) / 2026-08-02 01:39:53 +0800 | 3.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [30710983309](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30710983309) / completed | [30710983309](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30710983309) / success | [30710983309](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30710983309) / 2026-08-02 01:45:12 +0800 | 3.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [30711028300](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30711028300) / completed | [30711028300](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30711028300) / success | [30711028300](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30711028300) / 2026-08-02 01:46:00 +0800 | 3.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [30711712707](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30711712707) / completed | [30711712707](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30711712707) / success | [30711712707](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30711712707) / 2026-08-02 02:05:13 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [30712063447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30712063447) / completed | [30712063447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30712063447) / success | [30712063447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30712063447) / 2026-08-02 02:15:33 +0800 | 3.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [30718995980](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30718995980) / in_progress | [30667122845](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30667122845) / success | [30667122845](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30667122845) / 2026-08-01 05:36:18 +0800 | 23.8h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / completed | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / success | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / 2026-07-27 02:38:20 +0800 | 146.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 409.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [30667165127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30667165127) / completed | [30667165127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30667165127) / success | [30667165127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30667165127) / 2026-08-01 05:36:59 +0800 | 23.8h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [30712120436](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30712120436) / completed | [30712120436](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30712120436) / success | [30712120436](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30712120436) / 2026-08-02 02:15:42 +0800 | 3.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
