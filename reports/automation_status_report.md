# Automation Status Report

- Generated at: 2026-07-03 04:16:31 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `64e1ebd1`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 2

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28612079280](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612079280) / completed | [28612079280](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612079280) / success | [28612079280](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612079280) / 2026-07-03 02:18:25 +0800 | 2.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28612144710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612144710) / completed | [28612144710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612144710) / success | [28612144710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612144710) / 2026-07-03 02:20:08 +0800 | 1.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28612258753](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612258753) / completed | [28612258753](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612258753) / success | [28612258753](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612258753) / 2026-07-03 02:20:52 +0800 | 1.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28612269717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612269717) / completed | [28612269717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612269717) / success | [28612269717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612269717) / 2026-07-03 02:21:07 +0800 | 1.9h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28613455296](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28613455296) / completed | [28613455296](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28613455296) / success | [28613455296](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28613455296) / 2026-07-03 02:40:53 +0800 | 1.6h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | warn | [28615317616](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28615317616) / completed | [28615317616](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28615317616) / failure | [28541625184](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541625184) / 2026-07-02 03:15:05 +0800 | 25.0h | latest completed run is failure on older commit 3927b602; current commit 64e1ebd1 will be checked by the next run |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28550399745](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28550399745) / completed | [28550399745](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28550399745) / success | [28550399745](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28550399745) / 2026-07-02 05:57:38 +0800 | 22.3h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / completed | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / success | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / 2026-06-29 02:48:00 +0800 | 97.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [28614869369](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28614869369) / completed | [28614869369](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28614869369) / success | [28614869369](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28614869369) / 2026-07-03 03:05:33 +0800 | 1.2h | ok |
| `pages-deploy.yml` | workflow_run / manual / public-path push | observe | warn | [28615372856](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28615372856) / completed | [28615372856](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28615372856) / skipped | [28614929829](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28614929829) / 2026-07-03 03:06:03 +0800 | 1.2h | latest completed run is skipped |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28615372818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28615372818) / completed | [28615372818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28615372818) / success | [28615372818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28615372818) / 2026-07-03 03:13:46 +0800 | 1.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
