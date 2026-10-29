# Automation Status Report

- Generated at: 2026-10-29 08:07:49 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `cca3c055`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [40770615277](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40770615277) / completed | [40770615277](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40770615277) / success | [40770615277](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40770615277) / 2026-10-29 05:18:17 +0800 | 2.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [40770799316](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40770799316) / completed | [40770799316](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40770799316) / success | [40770799316](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40770799316) / 2026-10-29 05:18:40 +0800 | 2.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [40771227822](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40771227822) / completed | [40771227822](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40771227822) / success | [40771227822](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40771227822) / 2026-10-29 05:22:05 +0800 | 2.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [40771306951](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40771306951) / completed | [40771306951](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40771306951) / success | [40771306951](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40771306951) / 2026-10-29 05:22:16 +0800 | 2.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [40773234199](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40773234199) / completed | [40773234199](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40773234199) / success | [40773234199](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40773234199) / 2026-10-29 05:36:34 +0800 | 2.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [40774208460](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40774208460) / completed | [40774208460](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40774208460) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [40791959388](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40791959388) / in_progress | [40605105963](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40605105963) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / completed | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / success | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / 2026-10-26 03:56:06 +0800 | 76.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 242.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [40605205870](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40605205870) / completed | [40605205870](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40605205870) / success | [40605205870](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40605205870) / 2026-10-28 07:53:56 +0800 | 24.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [40774491124](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40774491124) / completed | [40774491124](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40774491124) / success | [40774491124](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40774491124) / 2026-10-29 05:45:06 +0800 | 2.4h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
