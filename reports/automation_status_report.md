# Automation Status Report

- Generated at: 2026-11-19 07:05:40 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `ce09aede`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [44417527780](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44417527780) / in_progress | [44201053538](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44201053538) / success | [44201053538](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44201053538) / 2026-11-18 07:39:25 +0800 | 23.4h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [44201110709](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44201110709) / completed | [44201110709](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44201110709) / success | [44201110709](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44201110709) / 2026-11-18 07:39:37 +0800 | 23.4h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [44201337238](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44201337238) / completed | [44201337238](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44201337238) / success | [44201337238](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44201337238) / 2026-11-18 07:40:25 +0800 | 23.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [44201360174](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44201360174) / completed | [44201360174](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44201360174) / success | [44201360174](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44201360174) / 2026-11-18 07:40:33 +0800 | 23.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [44202505104](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44202505104) / completed | [44202505104](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44202505104) / success | [44202505104](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44202505104) / 2026-11-18 07:48:45 +0800 | 23.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [44203070632](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44203070632) / completed | [44203070632](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44203070632) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 457.5h | last success is stale (457.5h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [44223601486](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44223601486) / completed | [44223601486](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44223601486) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / completed | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / success | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / 2026-11-16 06:02:31 +0800 | 73.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 745.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [44223690124](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44223690124) / completed | [44223690124](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44223690124) / success | [44223690124](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44223690124) / 2026-11-18 10:30:04 +0800 | 20.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [44223715933](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44223715933) / completed | [44223715933](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44223715933) / success | [44223715933](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44223715933) / 2026-11-18 10:30:15 +0800 | 20.6h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
