# Automation Status Report

- Generated at: 2026-11-09 04:44:34 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `9a0b46e2`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [42521588276](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521588276) / in_progress | [42411133604](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42411133604) / success | [42411133604](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42411133604) / 2026-11-08 04:28:49 +0800 | 24.3h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [42411232695](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42411232695) / completed | [42411232695](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42411232695) / success | [42411232695](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42411232695) / 2026-11-08 04:29:19 +0800 | 24.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [42411540173](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42411540173) / completed | [42411540173](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42411540173) / success | [42411540173](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42411540173) / 2026-11-08 04:32:55 +0800 | 24.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [42411614551](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42411614551) / completed | [42411614551](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42411614551) / success | [42411614551](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42411614551) / 2026-11-08 04:33:43 +0800 | 24.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [42412643562](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42412643562) / completed | [42412643562](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42412643562) / success | [42412643562](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42412643562) / 2026-11-08 04:47:14 +0800 | 24.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [42413524505](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42413524505) / completed | [42413524505](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42413524505) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 215.2h | last success is stale (215.2h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [42426619869](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42426619869) / completed | [42426619869](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42426619869) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / completed | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / success | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / 2026-11-02 05:22:24 +0800 | 167.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 503.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [42426672971](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42426672971) / completed | [42426672971](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42426672971) / success | [42426672971](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42426672971) / 2026-11-08 07:45:32 +0800 | 21.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [42426685424](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42426685424) / completed | [42426685424](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42426685424) / success | [42426685424](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42426685424) / 2026-11-08 07:45:41 +0800 | 21.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
