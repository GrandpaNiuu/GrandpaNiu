# Automation Status Report

- Generated at: 2026-08-01 05:35:52 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `3168cbb8`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [30653871663](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30653871663) / completed | [30653871663](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30653871663) / success | [30653871663](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30653871663) / 2026-08-01 02:08:14 +0800 | 3.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [30653952897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30653952897) / completed | [30653952897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30653952897) / success | [30653952897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30653952897) / 2026-08-01 02:08:48 +0800 | 3.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [30654125244](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30654125244) / completed | [30654125244](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30654125244) / success | [30654125244](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30654125244) / 2026-08-01 02:11:10 +0800 | 3.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [30654166060](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30654166060) / completed | [30654166060](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30654166060) / success | [30654166060](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30654166060) / 2026-08-01 02:11:51 +0800 | 3.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [30655073551](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30655073551) / completed | [30655073551](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30655073551) / success | [30655073551](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30655073551) / 2026-08-01 02:25:50 +0800 | 3.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [30656576463](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30656576463) / completed | [30656576463](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30656576463) / success | [30656576463](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30656576463) / 2026-08-01 02:49:00 +0800 | 2.8h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [30667122845](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30667122845) / in_progress | [30584298928](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30584298928) / success | [30584298928](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30584298928) / 2026-07-31 05:40:55 +0800 | 23.9h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / completed | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / success | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / 2026-07-27 02:38:20 +0800 | 123.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 385.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [30584352622](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30584352622) / completed | [30584352622](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30584352622) / success | [30584352622](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30584352622) / 2026-07-31 05:41:27 +0800 | 23.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [30656669955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30656669955) / completed | [30656669955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30656669955) / success | [30656669955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30656669955) / 2026-08-01 02:49:15 +0800 | 2.8h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
