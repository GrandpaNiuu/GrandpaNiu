# Automation Status Report

- Generated at: 2026-10-25 02:58:43 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `b87f4215`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [40123097421](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40123097421) / in_progress | [40016237372](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016237372) / success | [40016237372](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016237372) / 2026-10-24 04:06:20 +0800 | 22.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [40016310139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016310139) / completed | [40016310139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016310139) / success | [40016310139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016310139) / 2026-10-24 04:06:44 +0800 | 22.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [40016645567](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016645567) / completed | [40016645567](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016645567) / success | [40016645567](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016645567) / 2026-10-24 04:07:18 +0800 | 22.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [40016692007](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016692007) / completed | [40016692007](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016692007) / success | [40016692007](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016692007) / 2026-10-24 04:07:37 +0800 | 22.9h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [40018016386](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40018016386) / completed | [40018016386](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40018016386) / success | [40018016386](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40018016386) / 2026-10-24 04:17:56 +0800 | 22.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [40019674415](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40019674415) / completed | [40019674415](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40019674415) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [40038738329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038738329) / completed | [40038738329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038738329) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / completed | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / success | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / 2026-10-19 03:37:05 +0800 | 143.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 141.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [40038817714](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038817714) / completed | [40038817714](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038817714) / success | [40038817714](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038817714) / 2026-10-24 07:17:33 +0800 | 19.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [40038834621](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038834621) / completed | [40038834621](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038834621) / success | [40038834621](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038834621) / 2026-10-24 07:17:43 +0800 | 19.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
