# Automation Status Report

- Generated at: 2026-07-03 03:05:20 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Overall status: `fail`
- Blocking findings: 1
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28612079280](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612079280) / completed | [28612079280](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612079280) / success | [28612079280](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612079280) / 2026-07-03 02:18:25 +0800 | 47m | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28612144710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612144710) / completed | [28612144710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612144710) / success | [28612144710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612144710) / 2026-07-03 02:20:08 +0800 | 45m | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28612258753](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612258753) / completed | [28612258753](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612258753) / success | [28612258753](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612258753) / 2026-07-03 02:20:52 +0800 | 44m | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28612269717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612269717) / completed | [28612269717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612269717) / success | [28612269717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612269717) / 2026-07-03 02:21:07 +0800 | 44m | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28613455296](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28613455296) / completed | [28613455296](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28613455296) / success | [28613455296](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28613455296) / 2026-07-03 02:40:53 +0800 | 24m | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [28614077411](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28614077411) / completed | [28614077411](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28614077411) / failure | [28541625184](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541625184) / 2026-07-02 03:15:05 +0800 | 23.8h | latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28550399745](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28550399745) / completed | [28550399745](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28550399745) / success | [28550399745](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28550399745) / 2026-07-02 05:57:38 +0800 | 21.1h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / completed | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / success | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / 2026-06-29 02:48:00 +0800 | 96.3h | ok |
| `module-factory-build.yml` | push/manual | observe | warn | [28614869369](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28614869369) / in_progress | [28614203884](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28614203884) / success | [28614203884](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28614203884) / 2026-07-03 02:54:17 +0800 | 11m | latest run is in_progress |
| `pages-deploy.yml` | workflow_run / manual / public-path push | observe | ok | [28614869290](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28614869290) / completed | [28614869290](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28614869290) / success | [28614869290](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28614869290) / 2026-07-03 03:04:56 +0800 | 0m | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28614265870](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28614265870) / completed | [28614265870](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28614265870) / success | [28614265870](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28614265870) / 2026-07-03 02:54:27 +0800 | 11m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
