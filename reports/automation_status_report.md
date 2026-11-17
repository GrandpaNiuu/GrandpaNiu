# Automation Status Report

- Generated at: 2026-11-17 08:28:12 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `3830d347`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [43987709154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43987709154) / in_progress | [43762398292](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43762398292) / success | [43762398292](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43762398292) / 2026-11-16 05:13:38 +0800 | 27.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [43987809117](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43987809117) / in_progress | [43762621180](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43762621180) / success | [43762621180](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43762621180) / 2026-11-16 05:15:39 +0800 | 27.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [43763105199](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43763105199) / completed | [43763105199](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43763105199) / success | [43763105199](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43763105199) / 2026-11-16 05:20:38 +0800 | 27.1h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [43763218837](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43763218837) / completed | [43763218837](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43763218837) / success | [43763218837](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43763218837) / 2026-11-16 05:21:48 +0800 | 27.1h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [43764750792](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43764750792) / completed | [43764750792](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43764750792) / success | [43764750792](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43764750792) / 2026-11-16 05:38:38 +0800 | 26.8h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [43766113107](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766113107) / completed | [43766113107](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766113107) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 410.9h | last success is stale (410.9h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [43778357363](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43778357363) / completed | [43778357363](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43778357363) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / completed | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / success | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / 2026-11-16 06:02:31 +0800 | 26.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 698.9h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [43778437861](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43778437861) / completed | [43778437861](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43778437861) / success | [43778437861](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43778437861) / 2026-11-16 08:07:06 +0800 | 24.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [43778459315](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43778459315) / completed | [43778459315](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43778459315) / success | [43778459315](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43778459315) / 2026-11-16 08:07:15 +0800 | 24.3h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
