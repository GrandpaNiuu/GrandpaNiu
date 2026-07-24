# Automation Status Report

- Generated at: 2026-07-25 05:34:55 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `f2e1aaa6`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [30115412145](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30115412145) / completed | [30115412145](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30115412145) / success | [30115412145](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30115412145) / 2026-07-25 02:04:16 +0800 | 3.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [30115451787](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30115451787) / completed | [30115451787](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30115451787) / success | [30115451787](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30115451787) / 2026-07-25 02:04:38 +0800 | 3.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [30115576473](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30115576473) / completed | [30115576473](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30115576473) / success | [30115576473](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30115576473) / 2026-07-25 02:06:04 +0800 | 3.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [30115645611](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30115645611) / completed | [30115645611](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30115645611) / success | [30115645611](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30115645611) / 2026-07-25 02:07:07 +0800 | 3.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [30116756637](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30116756637) / completed | [30116756637](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30116756637) / success | [30116756637](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30116756637) / 2026-07-25 02:24:34 +0800 | 3.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [30118453896](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30118453896) / completed | [30118453896](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30118453896) / success | [30118453896](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30118453896) / 2026-07-25 02:51:35 +0800 | 2.7h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [30128205171](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30128205171) / in_progress | [30046630536](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30046630536) / success | [30046630536](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30046630536) / 2026-07-24 05:33:43 +0800 | 24.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / completed | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / success | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / 2026-07-20 02:33:21 +0800 | 123.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 217.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [30046670681](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30046670681) / completed | [30046670681](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30046670681) / success | [30046670681](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30046670681) / 2026-07-24 05:34:17 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [30118557953](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30118557953) / completed | [30118557953](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30118557953) / success | [30118557953](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30118557953) / 2026-07-25 02:51:46 +0800 | 2.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
