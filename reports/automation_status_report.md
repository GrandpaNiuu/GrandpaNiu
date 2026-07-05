# Automation Status Report

- Generated at: 2026-07-06 01:41:18 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `c87c715e`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | warn | [28749304568](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749304568) / in_progress | [28714307591](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28714307591) / success | [28714307591](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28714307591) / 2026-07-05 01:39:01 +0800 | 24.0h | latest run is in_progress |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28714376809](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28714376809) / completed | [28714376809](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28714376809) / success | [28714376809](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28714376809) / 2026-07-05 01:41:15 +0800 | 24.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28714545821](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28714545821) / completed | [28714545821](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28714545821) / success | [28714545821](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28714545821) / 2026-07-05 01:48:03 +0800 | 23.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28714578935](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28714578935) / completed | [28714578935](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28714578935) / success | [28714578935](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28714578935) / 2026-07-05 01:49:16 +0800 | 23.9h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28715114234](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28715114234) / completed | [28715114234](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28715114234) / success | [28715114234](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28715114234) / 2026-07-05 02:09:27 +0800 | 23.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28715283606](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28715283606) / completed | [28715283606](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28715283606) / success | [28715283606](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28715283606) / 2026-07-05 02:16:15 +0800 | 23.4h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28720143746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720143746) / completed | [28720143746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720143746) / success | [28720143746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720143746) / 2026-07-05 05:26:27 +0800 | 20.2h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28695947613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28695947613) / completed | [28695947613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28695947613) / success | [28695947613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28695947613) / 2026-07-04 13:16:27 +0800 | 36.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [28692446521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28692446521) / completed | [28692446521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28692446521) / success | [28692446521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28692446521) / 2026-07-04 10:43:05 +0800 | 39.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual / public-path push | observe | ok | [28720153795](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720153795) / completed | [28720153795](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720153795) / success | [28720153795](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720153795) / 2026-07-05 05:27:03 +0800 | 20.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28720153793](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720153793) / completed | [28720153793](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720153793) / success | [28720153793](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720153793) / 2026-07-05 05:26:36 +0800 | 20.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
