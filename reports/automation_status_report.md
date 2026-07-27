# Automation Status Report

- Generated at: 2026-07-28 02:09:53 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `ed13d8cc`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [30292467422](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30292467422) / in_progress | [30213001305](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30213001305) / success | [30213001305](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30213001305) / 2026-07-27 01:39:34 +0800 | 24.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [30213078114](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30213078114) / completed | [30213078114](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30213078114) / success | [30213078114](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30213078114) / 2026-07-27 01:41:04 +0800 | 24.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [30213277790](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30213277790) / completed | [30213277790](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30213277790) / success | [30213277790](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30213277790) / 2026-07-27 01:46:45 +0800 | 24.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [30213305732](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30213305732) / completed | [30213305732](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30213305732) / success | [30213305732](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30213305732) / 2026-07-27 01:47:22 +0800 | 24.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [30214002936](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30214002936) / completed | [30214002936](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30214002936) / success | [30214002936](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30214002936) / 2026-07-27 02:06:55 +0800 | 24.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [30214315513](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30214315513) / completed | [30214315513](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30214315513) / success | [30214315513](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30214315513) / 2026-07-27 02:16:09 +0800 | 23.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [30221006478](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30221006478) / completed | [30221006478](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30221006478) / success | [30221006478](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30221006478) / 2026-07-27 05:24:58 +0800 | 20.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / completed | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / success | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / 2026-07-27 02:38:20 +0800 | 23.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 286.1h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [30221026018](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30221026018) / completed | [30221026018](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30221026018) / success | [30221026018](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30221026018) / 2026-07-27 05:25:31 +0800 | 20.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [30221046039](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30221046039) / completed | [30221046039](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30221046039) / success | [30221046039](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30221046039) / 2026-07-27 05:25:40 +0800 | 20.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
