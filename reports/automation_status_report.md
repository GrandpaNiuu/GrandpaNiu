# Automation Status Report

- Generated at: 2026-11-23 05:59:17 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `9ecbb656`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [45075041907](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45075041907) / in_progress | [44953640001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953640001) / success | [44953640001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953640001) / 2026-11-22 05:51:53 +0800 | 24.1h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [44953718624](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953718624) / completed | [44953718624](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953718624) / success | [44953718624](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953718624) / 2026-11-22 05:52:24 +0800 | 24.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [44953989121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953989121) / completed | [44953989121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953989121) / success | [44953989121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953989121) / 2026-11-22 05:55:31 +0800 | 24.1h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [44954060263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44954060263) / completed | [44954060263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44954060263) / success | [44954060263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44954060263) / 2026-11-22 05:56:22 +0800 | 24.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [44954997663](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44954997663) / completed | [44954997663](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44954997663) / success | [44954997663](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44954997663) / 2026-11-22 06:07:18 +0800 | 23.9h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [44955562178](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44955562178) / completed | [44955562178](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44955562178) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [44967138718](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967138718) / completed | [44967138718](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967138718) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / completed | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / success | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / 2026-11-16 06:02:31 +0800 | 167.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 840.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [44967205869](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967205869) / completed | [44967205869](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967205869) / success | [44967205869](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967205869) / 2026-11-22 08:33:41 +0800 | 21.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [44967222578](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967222578) / completed | [44967222578](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967222578) / success | [44967222578](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967222578) / 2026-11-22 08:33:52 +0800 | 21.4h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
