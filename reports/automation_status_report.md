# Automation Status Report

- Generated at: 2026-11-11 08:44:47 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `931ac468`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [42909658005](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42909658005) / completed | [42909658005](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42909658005) / success | [42909658005](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42909658005) / 2026-11-11 05:56:52 +0800 | 2.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [42909834251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42909834251) / completed | [42909834251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42909834251) / success | [42909834251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42909834251) / 2026-11-11 05:57:21 +0800 | 2.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [42910172472](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42910172472) / completed | [42910172472](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42910172472) / success | [42910172472](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42910172472) / 2026-11-11 05:59:13 +0800 | 2.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [42910194659](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42910194659) / completed | [42910194659](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42910194659) / success | [42910194659](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42910194659) / 2026-11-11 05:59:37 +0800 | 2.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [42912760520](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42912760520) / completed | [42912760520](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42912760520) / success | [42912760520](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42912760520) / 2026-11-11 06:15:51 +0800 | 2.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [42914330361](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42914330361) / completed | [42914330361](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42914330361) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 267.2h | last success is stale (267.2h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [42933705885](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42933705885) / in_progress | [42745357396](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42745357396) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / completed | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / success | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / 2026-11-09 05:21:23 +0800 | 51.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 555.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [42745441573](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42745441573) / completed | [42745441573](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42745441573) / success | [42745441573](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42745441573) / 2026-11-10 10:50:19 +0800 | 21.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [42914592034](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42914592034) / completed | [42914592034](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42914592034) / success | [42914592034](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42914592034) / 2026-11-11 06:26:42 +0800 | 2.3h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
