# Automation Status Report

- Generated at: 2026-10-29 05:17:55 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `8ede36c1`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [40770615277](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40770615277) / in_progress | [40582281127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40582281127) / success | [40582281127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40582281127) / 2026-10-28 04:56:48 +0800 | 24.4h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [40582634412](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40582634412) / completed | [40582634412](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40582634412) / success | [40582634412](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40582634412) / 2026-10-28 04:58:17 +0800 | 24.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [40582917859](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40582917859) / completed | [40582917859](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40582917859) / success | [40582917859](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40582917859) / 2026-10-28 05:00:23 +0800 | 24.3h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [40582951320](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40582951320) / completed | [40582951320](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40582951320) / success | [40582951320](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40582951320) / 2026-10-28 05:00:46 +0800 | 24.3h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [40584693936](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40584693936) / completed | [40584693936](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40584693936) / success | [40584693936](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40584693936) / 2026-10-28 05:12:41 +0800 | 24.1h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [40586213739](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40586213739) / completed | [40586213739](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40586213739) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [40605105963](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40605105963) / completed | [40605105963](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40605105963) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / completed | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / success | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / 2026-10-26 03:56:06 +0800 | 73.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 239.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [40605205870](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40605205870) / completed | [40605205870](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40605205870) / success | [40605205870](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40605205870) / 2026-10-28 07:53:56 +0800 | 21.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [40605227206](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40605227206) / completed | [40605227206](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40605227206) / success | [40605227206](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40605227206) / 2026-10-28 07:54:08 +0800 | 21.4h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
