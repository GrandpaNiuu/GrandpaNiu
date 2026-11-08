# Automation Status Report

- Generated at: 2026-11-09 05:21:03 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `11f6ad2f`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [42521588276](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521588276) / completed | [42521588276](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521588276) / success | [42521588276](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521588276) / 2026-11-09 04:44:51 +0800 | 36m | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [42521692543](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521692543) / completed | [42521692543](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521692543) / success | [42521692543](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521692543) / 2026-11-09 04:45:34 +0800 | 35m | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [42521854368](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521854368) / completed | [42521854368](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521854368) / success | [42521854368](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521854368) / 2026-11-09 04:47:35 +0800 | 33m | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [42521921605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521921605) / completed | [42521921605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521921605) / success | [42521921605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521921605) / 2026-11-09 04:48:08 +0800 | 33m | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [42523030623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42523030623) / completed | [42523030623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42523030623) / success | [42523030623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42523030623) / 2026-11-09 05:02:03 +0800 | 19m | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [42524154642](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524154642) / completed | [42524154642](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524154642) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 215.8h | last success is stale (215.8h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [42426619869](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42426619869) / completed | [42426619869](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42426619869) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / in_progress | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / success | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / 2026-11-02 05:22:24 +0800 | 168.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 503.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [42426672971](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42426672971) / completed | [42426672971](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42426672971) / success | [42426672971](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42426672971) / 2026-11-08 07:45:32 +0800 | 21.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [42524271948](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524271948) / completed | [42524271948](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524271948) / success | [42524271948](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524271948) / 2026-11-09 05:15:28 +0800 | 6m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
