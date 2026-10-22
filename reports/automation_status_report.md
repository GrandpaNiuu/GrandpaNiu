# Automation Status Report

- Generated at: 2026-10-23 04:17:05 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `96d7269d`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [39847335605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39847335605) / in_progress | [39669334045](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39669334045) / success | [39669334045](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39669334045) / 2026-10-22 04:21:14 +0800 | 23.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [39847460829](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39847460829) / in_progress | [39669476248](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39669476248) / success | [39669476248](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39669476248) / 2026-10-22 04:21:29 +0800 | 23.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [39669732589](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39669732589) / completed | [39669732589](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39669732589) / success | [39669732589](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39669732589) / 2026-10-22 04:23:01 +0800 | 23.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [39669766488](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39669766488) / completed | [39669766488](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39669766488) / success | [39669766488](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39669766488) / 2026-10-22 04:23:13 +0800 | 23.9h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [39670876086](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39670876086) / completed | [39670876086](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39670876086) / success | [39670876086](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39670876086) / 2026-10-22 04:31:25 +0800 | 23.8h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [39672424056](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39672424056) / completed | [39672424056](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39672424056) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [39693702106](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39693702106) / completed | [39693702106](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39693702106) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / completed | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / success | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / 2026-10-19 03:37:05 +0800 | 96.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 94.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [39693777349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39693777349) / completed | [39693777349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39693777349) / success | [39693777349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39693777349) / 2026-10-22 07:29:54 +0800 | 20.8h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [39693796498](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39693796498) / completed | [39693796498](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39693796498) / success | [39693796498](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39693796498) / 2026-10-22 07:30:03 +0800 | 20.8h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
