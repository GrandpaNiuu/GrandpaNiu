# Automation Status Report

- Generated at: 2026-11-22 08:33:06 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `0df5c739`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [44953640001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953640001) / completed | [44953640001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953640001) / success | [44953640001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953640001) / 2026-11-22 05:51:53 +0800 | 2.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [44953718624](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953718624) / completed | [44953718624](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953718624) / success | [44953718624](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953718624) / 2026-11-22 05:52:24 +0800 | 2.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [44953989121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953989121) / completed | [44953989121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953989121) / success | [44953989121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953989121) / 2026-11-22 05:55:31 +0800 | 2.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [44954060263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44954060263) / completed | [44954060263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44954060263) / success | [44954060263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44954060263) / 2026-11-22 05:56:22 +0800 | 2.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [44954997663](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44954997663) / completed | [44954997663](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44954997663) / success | [44954997663](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44954997663) / 2026-11-22 06:07:18 +0800 | 2.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [44955562178](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44955562178) / completed | [44955562178](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44955562178) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [44967138718](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967138718) / in_progress | [44851260725](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44851260725) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / completed | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / success | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / 2026-11-16 06:02:31 +0800 | 146.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 819.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [44851336883](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44851336883) / completed | [44851336883](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44851336883) / success | [44851336883](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44851336883) / 2026-11-21 09:38:20 +0800 | 22.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [44955680203](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44955680203) / completed | [44955680203](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44955680203) / success | [44955680203](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44955680203) / 2026-11-22 06:14:21 +0800 | 2.3h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
