# Automation Status Report

- Generated at: 2026-11-04 05:57:41 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `67510582`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [41726303561](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41726303561) / in_progress | [41547145538](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41547145538) / success | [41547145538](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41547145538) / 2026-11-03 07:41:16 +0800 | 22.3h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [41547227134](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41547227134) / completed | [41547227134](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41547227134) / success | [41547227134](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41547227134) / 2026-11-03 07:41:41 +0800 | 22.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [41547452284](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41547452284) / completed | [41547452284](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41547452284) / success | [41547452284](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41547452284) / 2026-11-03 07:43:12 +0800 | 22.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [41547458744](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41547458744) / completed | [41547458744](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41547458744) / success | [41547458744](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41547458744) / 2026-11-03 07:42:50 +0800 | 22.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [41548371009](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41548371009) / completed | [41548371009](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41548371009) / success | [41548371009](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41548371009) / 2026-11-03 07:50:32 +0800 | 22.1h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [41549001132](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41549001132) / completed | [41549001132](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41549001132) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 96.4h | last success is stale (96.4h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [41566462099](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41566462099) / completed | [41566462099](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41566462099) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / completed | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / success | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / 2026-11-02 05:22:24 +0800 | 48.6h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 384.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [41566544355](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41566544355) / completed | [41566544355](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41566544355) / success | [41566544355](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41566544355) / 2026-11-03 10:30:50 +0800 | 19.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [41566586581](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41566586581) / completed | [41566586581](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41566586581) / success | [41566586581](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41566586581) / 2026-11-03 10:31:08 +0800 | 19.4h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
