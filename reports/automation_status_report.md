# Automation Status Report

- Generated at: 2026-10-24 07:16:57 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `4f490225`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [40016237372](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016237372) / completed | [40016237372](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016237372) / success | [40016237372](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016237372) / 2026-10-24 04:06:20 +0800 | 3.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [40016310139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016310139) / completed | [40016310139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016310139) / success | [40016310139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016310139) / 2026-10-24 04:06:44 +0800 | 3.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [40016645567](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016645567) / completed | [40016645567](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016645567) / success | [40016645567](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016645567) / 2026-10-24 04:07:18 +0800 | 3.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [40016692007](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016692007) / completed | [40016692007](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016692007) / success | [40016692007](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016692007) / 2026-10-24 04:07:37 +0800 | 3.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [40018016386](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40018016386) / completed | [40018016386](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40018016386) / success | [40018016386](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40018016386) / 2026-10-24 04:17:56 +0800 | 3.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [40019674415](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40019674415) / completed | [40019674415](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40019674415) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [40038738329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038738329) / in_progress | [39872035264](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39872035264) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / completed | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / success | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / 2026-10-19 03:37:05 +0800 | 123.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 121.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [39872112686](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39872112686) / completed | [39872112686](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39872112686) / success | [39872112686](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39872112686) / 2026-10-23 07:29:31 +0800 | 23.8h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [40019862579](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40019862579) / completed | [40019862579](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40019862579) / success | [40019862579](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40019862579) / 2026-10-24 04:31:31 +0800 | 2.8h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
