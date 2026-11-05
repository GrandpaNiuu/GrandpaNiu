# Automation Status Report

- Generated at: 2026-11-05 08:57:52 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `7bfe7998`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 2

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | warn | [41922546670](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41922546670) / completed | [41922546670](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41922546670) / failure | [41726303561](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41726303561) / 2026-11-04 05:58:05 +0800 | 27.0h | latest completed run is failure on older commit e4b14f74; current commit 7bfe7998 will be checked by the next run |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [41922832621](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41922832621) / completed | [41922832621](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41922832621) / success | [41922832621](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41922832621) / 2026-11-05 06:10:43 +0800 | 2.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [41923558553](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41923558553) / completed | [41923558553](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41923558553) / success | [41923558553](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41923558553) / 2026-11-05 06:15:57 +0800 | 2.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [41923576251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41923576251) / completed | [41923576251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41923576251) / success | [41923576251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41923576251) / 2026-11-05 06:16:14 +0800 | 2.7h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [41925829315](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41925829315) / completed | [41925829315](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41925829315) / success | [41925829315](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41925829315) / 2026-11-05 06:31:10 +0800 | 2.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [41927298948](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41927298948) / completed | [41927298948](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41927298948) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 123.4h | last success is stale (123.4h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [41945132815](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41945132815) / in_progress | [41748989472](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41748989472) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / completed | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / success | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / 2026-11-02 05:22:24 +0800 | 75.6h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 411.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [41749099196](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41749099196) / completed | [41749099196](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41749099196) / success | [41749099196](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41749099196) / 2026-11-04 08:44:48 +0800 | 24.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [41927557273](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41927557273) / completed | [41927557273](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41927557273) / success | [41927557273](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41927557273) / 2026-11-05 06:42:22 +0800 | 2.3h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
