# Automation Status Report

- Generated at: 2026-08-01 02:07:53 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `1769d397`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [30653871663](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30653871663) / in_progress | [30568452790](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30568452790) / success | [30568452790](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30568452790) / 2026-07-31 02:00:52 +0800 | 24.1h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [30568564923](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30568564923) / completed | [30568564923](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30568564923) / success | [30568564923](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30568564923) / 2026-07-31 02:01:36 +0800 | 24.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [30568769349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30568769349) / completed | [30568769349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30568769349) / success | [30568769349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30568769349) / 2026-07-31 02:04:23 +0800 | 24.1h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [30568827943](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30568827943) / completed | [30568827943](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30568827943) / success | [30568827943](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30568827943) / 2026-07-31 02:05:12 +0800 | 24.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [30570157869](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30570157869) / completed | [30570157869](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30570157869) / success | [30570157869](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30570157869) / 2026-07-31 02:23:47 +0800 | 23.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [30572177744](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30572177744) / completed | [30572177744](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30572177744) / success | [30572177744](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30572177744) / 2026-07-31 02:52:37 +0800 | 23.3h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [30584298928](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30584298928) / completed | [30584298928](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30584298928) / success | [30584298928](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30584298928) / 2026-07-31 05:40:55 +0800 | 20.4h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / completed | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / success | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / 2026-07-27 02:38:20 +0800 | 119.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 382.1h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [30584352622](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30584352622) / completed | [30584352622](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30584352622) / success | [30584352622](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30584352622) / 2026-07-31 05:41:27 +0800 | 20.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [30584389999](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30584389999) / completed | [30584389999](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30584389999) / success | [30584389999](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30584389999) / 2026-07-31 05:41:37 +0800 | 20.4h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
