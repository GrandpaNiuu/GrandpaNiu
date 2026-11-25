# Automation Status Report

- Generated at: 2026-11-25 09:02:22 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `ef0f64a1`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [45522591777](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45522591777) / in_progress | [45316471316](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45316471316) / success | [45316471316](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45316471316) / 2026-11-24 11:01:55 +0800 | 22.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [45316580226](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45316580226) / completed | [45316580226](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45316580226) / success | [45316580226](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45316580226) / 2026-11-24 11:02:22 +0800 | 22.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [45316775732](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45316775732) / completed | [45316775732](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45316775732) / success | [45316775732](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45316775732) / 2026-11-24 11:04:04 +0800 | 22.0h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [45316796767](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45316796767) / completed | [45316796767](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45316796767) / success | [45316796767](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45316796767) / 2026-11-24 11:04:15 +0800 | 22.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [45318013838](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45318013838) / completed | [45318013838](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45318013838) / success | [45318013838](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45318013838) / 2026-11-24 11:14:38 +0800 | 21.8h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [45318916047](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45318916047) / completed | [45318916047](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45318916047) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [45329435557](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45329435557) / completed | [45329435557](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45329435557) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / completed | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / success | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / 2026-11-23 06:45:10 +0800 | 50.3h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 891.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [45329538229](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45329538229) / completed | [45329538229](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45329538229) / success | [45329538229](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45329538229) / 2026-11-24 12:54:06 +0800 | 20.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [45329563371](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45329563371) / completed | [45329563371](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45329563371) / success | [45329563371](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45329563371) / 2026-11-24 12:54:18 +0800 | 20.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
