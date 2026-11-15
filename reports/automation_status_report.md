# Automation Status Report

- Generated at: 2026-11-15 08:00:23 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `bf6f836b`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [43639910009](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43639910009) / completed | [43639910009](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43639910009) / success | [43639910009](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43639910009) / 2026-11-15 04:55:13 +0800 | 3.1h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [43639977479](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43639977479) / completed | [43639977479](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43639977479) / success | [43639977479](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43639977479) / 2026-11-15 04:55:32 +0800 | 3.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [43640213461](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43640213461) / completed | [43640213461](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43640213461) / success | [43640213461](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43640213461) / 2026-11-15 04:58:07 +0800 | 3.0h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [43640268091](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43640268091) / completed | [43640268091](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43640268091) / success | [43640268091](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43640268091) / 2026-11-15 04:58:42 +0800 | 3.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [43641969666](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43641969666) / completed | [43641969666](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43641969666) / success | [43641969666](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43641969666) / 2026-11-15 05:17:38 +0800 | 2.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [43643476395](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43643476395) / completed | [43643476395](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43643476395) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 362.4h | last success is stale (362.4h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [43655982120](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43655982120) / in_progress | [43537454520](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43537454520) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / completed | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / success | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / 2026-11-09 05:21:23 +0800 | 146.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 650.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [43537536424](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43537536424) / completed | [43537536424](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43537536424) / success | [43537536424](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43537536424) / 2026-11-14 08:57:29 +0800 | 23.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [43643582576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43643582576) / completed | [43643582576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43643582576) / success | [43643582576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43643582576) / 2026-11-15 05:35:08 +0800 | 2.4h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
