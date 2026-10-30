# Automation Status Report

- Generated at: 2026-10-31 07:55:45 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `42ee5b18`
- Overall status: `fail`
- Blocking findings: 2
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [41127594080](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41127594080) / completed | [41127594080](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41127594080) / success | [41127594080](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41127594080) / 2026-10-31 05:01:27 +0800 | 2.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [41127758730](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41127758730) / completed | [41127758730](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41127758730) / success | [41127758730](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41127758730) / 2026-10-31 05:01:48 +0800 | 2.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [41128609466](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41128609466) / completed | [41128609466](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41128609466) / success | [41128609466](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41128609466) / 2026-10-31 05:07:58 +0800 | 2.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [41128635893](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41128635893) / completed | [41128635893](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41128635893) / success | [41128635893](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41128635893) / 2026-10-31 05:08:14 +0800 | 2.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [41130882715](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41130882715) / completed | [41130882715](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41130882715) / success | [41130882715](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41130882715) / 2026-10-31 05:25:52 +0800 | 2.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / completed | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / success | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 2.3h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [41147286206](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41147286206) / in_progress | [40976956919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40976956919) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / completed | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / success | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / 2026-10-26 03:56:06 +0800 | 124.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 290.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [40977046261](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40977046261) / completed | [40977046261](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40977046261) / success | [40977046261](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40977046261) / 2026-10-30 08:02:04 +0800 | 23.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [41132182713](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132182713) / completed | [41132182713](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132182713) / success | [41132182713](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132182713) / 2026-10-31 05:35:38 +0800 | 2.3h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
