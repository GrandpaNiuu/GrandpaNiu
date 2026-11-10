# Automation Status Report

- Generated at: 2026-11-10 08:24:42 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `1edf1a4d`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [42727944684](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42727944684) / in_progress | [42521588276](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521588276) / success | [42521588276](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521588276) / 2026-11-09 04:44:51 +0800 | 27.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [42728052942](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42728052942) / in_progress | [42521692543](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521692543) / success | [42521692543](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521692543) / 2026-11-09 04:45:34 +0800 | 27.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [42521854368](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521854368) / completed | [42521854368](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521854368) / success | [42521854368](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521854368) / 2026-11-09 04:47:35 +0800 | 27.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [42521921605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521921605) / completed | [42521921605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521921605) / success | [42521921605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42521921605) / 2026-11-09 04:48:08 +0800 | 27.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [42523030623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42523030623) / completed | [42523030623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42523030623) / success | [42523030623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42523030623) / 2026-11-09 05:02:03 +0800 | 27.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [42524154642](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524154642) / completed | [42524154642](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524154642) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 242.8h | last success is stale (242.8h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [42537132870](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42537132870) / completed | [42537132870](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42537132870) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / completed | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / success | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / 2026-11-09 05:21:23 +0800 | 27.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 530.9h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [42537192154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42537192154) / completed | [42537192154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42537192154) / success | [42537192154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42537192154) / 2026-11-09 07:51:52 +0800 | 24.5h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [42537203755](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42537203755) / completed | [42537203755](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42537203755) / success | [42537203755](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42537203755) / 2026-11-09 07:52:02 +0800 | 24.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
