# Automation Status Report

- Generated at: 2026-11-23 08:59:47 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `72a5fe89`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [45075041907](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45075041907) / completed | [45075041907](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45075041907) / success | [45075041907](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45075041907) / 2026-11-23 05:59:31 +0800 | 3.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [45075153081](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45075153081) / completed | [45075153081](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45075153081) / success | [45075153081](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45075153081) / 2026-11-23 06:00:24 +0800 | 3.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [45076026176](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45076026176) / completed | [45076026176](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45076026176) / success | [45076026176](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45076026176) / 2026-11-23 06:09:08 +0800 | 2.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [45076080369](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45076080369) / completed | [45076080369](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45076080369) / success | [45076080369](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45076080369) / 2026-11-23 06:09:38 +0800 | 2.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [45077335466](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45077335466) / completed | [45077335466](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45077335466) / success | [45077335466](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45077335466) / 2026-11-23 06:23:04 +0800 | 2.6h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [45078196887](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45078196887) / completed | [45078196887](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45078196887) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [45091967892](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45091967892) / in_progress | [44967138718](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967138718) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / completed | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / success | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / 2026-11-23 06:45:10 +0800 | 2.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 843.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [44967205869](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967205869) / completed | [44967205869](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967205869) / success | [44967205869](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44967205869) / 2026-11-22 08:33:41 +0800 | 24.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [45079456002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079456002) / completed | [45079456002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079456002) / success | [45079456002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079456002) / 2026-11-23 06:45:17 +0800 | 2.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
