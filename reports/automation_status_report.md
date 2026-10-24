# Automation Status Report

- Generated at: 2026-10-25 06:36:38 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `f1dccf35`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [40123097421](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40123097421) / completed | [40123097421](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40123097421) / success | [40123097421](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40123097421) / 2026-10-25 02:59:03 +0800 | 3.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [40123182210](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40123182210) / completed | [40123182210](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40123182210) / success | [40123182210](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40123182210) / 2026-10-25 02:59:33 +0800 | 3.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [40123547893](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40123547893) / completed | [40123547893](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40123547893) / success | [40123547893](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40123547893) / 2026-10-25 03:04:04 +0800 | 3.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [40123619087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40123619087) / completed | [40123619087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40123619087) / success | [40123619087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40123619087) / 2026-10-25 03:04:59 +0800 | 3.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [40125017933](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40125017933) / completed | [40125017933](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40125017933) / success | [40125017933](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40125017933) / 2026-10-25 03:23:29 +0800 | 3.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [40125817949](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40125817949) / completed | [40125817949](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40125817949) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [40139268459](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40139268459) / in_progress | [40038738329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038738329) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / completed | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / success | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / 2026-10-19 03:37:05 +0800 | 147.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 145.1h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [40038817714](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038817714) / completed | [40038817714](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038817714) / success | [40038817714](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40038817714) / 2026-10-24 07:17:33 +0800 | 23.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [40125896295](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40125896295) / completed | [40125896295](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40125896295) / success | [40125896295](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40125896295) / 2026-10-25 03:34:22 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
