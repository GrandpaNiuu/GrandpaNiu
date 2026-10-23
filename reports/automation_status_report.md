# Automation Status Report

- Generated at: 2026-10-24 04:06:01 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `585a1f10`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [40016237372](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016237372) / in_progress | [39847335605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39847335605) / success | [39847335605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39847335605) / 2026-10-23 04:17:27 +0800 | 23.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [40016310139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40016310139) / in_progress | [39847460829](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39847460829) / success | [39847460829](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39847460829) / 2026-10-23 04:17:41 +0800 | 23.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [39847809240](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39847809240) / completed | [39847809240](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39847809240) / success | [39847809240](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39847809240) / 2026-10-23 04:19:52 +0800 | 23.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [39847844684](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39847844684) / completed | [39847844684](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39847844684) / success | [39847844684](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39847844684) / 2026-10-23 04:20:12 +0800 | 23.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [39849053985](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39849053985) / completed | [39849053985](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39849053985) / success | [39849053985](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39849053985) / 2026-10-23 04:28:34 +0800 | 23.6h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [39850205490](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39850205490) / completed | [39850205490](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39850205490) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [39872035264](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39872035264) / completed | [39872035264](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39872035264) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / completed | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / success | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / 2026-10-19 03:37:05 +0800 | 120.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 118.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [39872112686](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39872112686) / completed | [39872112686](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39872112686) / success | [39872112686](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39872112686) / 2026-10-23 07:29:31 +0800 | 20.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [39872128105](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39872128105) / completed | [39872128105](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39872128105) / success | [39872128105](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39872128105) / 2026-10-23 07:29:42 +0800 | 20.6h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
