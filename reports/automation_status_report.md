# Automation Status Report

- Generated at: 2026-08-10 05:01:08 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `85207f78`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [31325546683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31325546683) / completed | [31325546683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31325546683) / success | [31325546683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31325546683) / 2026-08-10 01:08:11 +0800 | 3.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [31325605258](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31325605258) / completed | [31325605258](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31325605258) / success | [31325605258](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31325605258) / 2026-08-10 01:08:41 +0800 | 3.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [31325955301](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31325955301) / completed | [31325955301](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31325955301) / success | [31325955301](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31325955301) / 2026-08-10 01:16:47 +0800 | 3.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [31325982712](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31325982712) / completed | [31325982712](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31325982712) / success | [31325982712](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31325982712) / 2026-08-10 01:17:13 +0800 | 3.7h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [31326933573](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31326933573) / completed | [31326933573](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31326933573) / success | [31326933573](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31326933573) / 2026-08-10 01:39:04 +0800 | 3.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [31327490785](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327490785) / completed | [31327490785](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327490785) / success | [31327490785](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327490785) / 2026-08-10 01:52:39 +0800 | 3.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [31335718929](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31335718929) / in_progress | [31278090405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31278090405) / success | [31278090405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31278090405) / 2026-08-09 04:56:35 +0800 | 24.1h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / completed | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / success | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / 2026-08-10 02:02:48 +0800 | 3.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 49.9h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [31278113617](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31278113617) / completed | [31278113617](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31278113617) / success | [31278113617](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31278113617) / 2026-08-09 04:57:12 +0800 | 24.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [31328011319](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31328011319) / completed | [31328011319](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31328011319) / success | [31328011319](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31328011319) / 2026-08-10 02:02:57 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
