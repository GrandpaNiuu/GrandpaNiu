# Automation Status Report

- Generated at: 2026-11-22 05:51:39 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `12cee798`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [44953640001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44953640001) / in_progress | [44831781646](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44831781646) / success | [44831781646](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44831781646) / 2026-11-21 06:48:22 +0800 | 23.1h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [44831904160](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44831904160) / completed | [44831904160](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44831904160) / success | [44831904160](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44831904160) / 2026-11-21 06:48:56 +0800 | 23.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [44832092003](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44832092003) / completed | [44832092003](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44832092003) / success | [44832092003](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44832092003) / 2026-11-21 06:50:11 +0800 | 23.0h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [44832188091](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44832188091) / completed | [44832188091](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44832188091) / success | [44832188091](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44832188091) / 2026-11-21 06:50:55 +0800 | 23.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [44833494080](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44833494080) / completed | [44833494080](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44833494080) / success | [44833494080](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44833494080) / 2026-11-21 07:01:26 +0800 | 22.8h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [44834729540](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44834729540) / completed | [44834729540](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44834729540) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [44851260725](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44851260725) / completed | [44851260725](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44851260725) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / completed | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / success | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / 2026-11-16 06:02:31 +0800 | 143.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 816.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [44851336883](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44851336883) / completed | [44851336883](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44851336883) / success | [44851336883](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44851336883) / 2026-11-21 09:38:20 +0800 | 20.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [44851355121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44851355121) / completed | [44851355121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44851355121) / success | [44851355121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44851355121) / 2026-11-21 09:38:38 +0800 | 20.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
