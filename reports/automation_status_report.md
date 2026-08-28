# Automation Status Report

- Generated at: 2026-08-28 12:24:33 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `c526ab6c`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [33131786351](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33131786351) / completed | [33131786351](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33131786351) / success | [33131786351](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33131786351) / 2026-08-28 09:06:48 +0800 | 3.3h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [33131866611](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33131866611) / completed | [33131866611](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33131866611) / success | [33131866611](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33131866611) / 2026-08-28 09:07:48 +0800 | 3.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [33132007913](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33132007913) / completed | [33132007913](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33132007913) / success | [33132007913](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33132007913) / 2026-08-28 09:10:25 +0800 | 3.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [33132036914](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33132036914) / completed | [33132036914](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33132036914) / success | [33132036914](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33132036914) / 2026-08-28 09:10:55 +0800 | 3.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [33132762235](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33132762235) / completed | [33132762235](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33132762235) / success | [33132762235](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33132762235) / 2026-08-28 09:25:17 +0800 | 3.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [33133110684](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33133110684) / completed | [33133110684](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33133110684) / success | [33133110684](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33133110684) / 2026-08-28 09:32:41 +0800 | 2.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [33141710320](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33141710320) / in_progress | [33024913095](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33024913095) / success | [33024913095](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33024913095) / 2026-08-27 07:54:59 +0800 | 28.5h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / completed | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / success | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / 2026-08-24 01:52:11 +0800 | 106.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 489.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [33024950287](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33024950287) / completed | [33024950287](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33024950287) / success | [33024950287](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33024950287) / 2026-08-27 07:55:31 +0800 | 28.5h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [33133184013](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33133184013) / completed | [33133184013](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33133184013) / success | [33133184013](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33133184013) / 2026-08-28 09:32:56 +0800 | 2.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
