# Automation Status Report

- Generated at: 2026-11-25 11:37:35 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `a08f2f86`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [45522591777](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45522591777) / completed | [45522591777](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45522591777) / success | [45522591777](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45522591777) / 2026-11-25 09:02:40 +0800 | 2.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [45522812040](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45522812040) / completed | [45522812040](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45522812040) / success | [45522812040](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45522812040) / 2026-11-25 09:03:41 +0800 | 2.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [45523321946](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45523321946) / completed | [45523321946](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45523321946) / success | [45523321946](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45523321946) / 2026-11-25 09:07:43 +0800 | 2.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [45523349299](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45523349299) / completed | [45523349299](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45523349299) / success | [45523349299](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45523349299) / 2026-11-25 09:07:49 +0800 | 2.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [45524800506](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45524800506) / completed | [45524800506](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45524800506) / success | [45524800506](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45524800506) / 2026-11-25 09:19:30 +0800 | 2.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [45525906729](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45525906729) / completed | [45525906729](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45525906729) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [45541219724](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45541219724) / in_progress | [45329435557](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45329435557) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / completed | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / success | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / 2026-11-23 06:45:10 +0800 | 52.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 894.1h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [45329538229](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45329538229) / completed | [45329538229](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45329538229) / success | [45329538229](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45329538229) / 2026-11-24 12:54:06 +0800 | 22.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [45526074874](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45526074874) / completed | [45526074874](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45526074874) / success | [45526074874](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45526074874) / 2026-11-25 09:29:12 +0800 | 2.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
