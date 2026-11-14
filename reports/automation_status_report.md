# Automation Status Report

- Generated at: 2026-11-14 08:56:58 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `49705e6e`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [43516579050](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43516579050) / completed | [43516579050](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43516579050) / success | [43516579050](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43516579050) / 2026-11-14 06:08:24 +0800 | 2.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [43516908513](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43516908513) / completed | [43516908513](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43516908513) / success | [43516908513](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43516908513) / 2026-11-14 06:10:07 +0800 | 2.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [43517469600](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43517469600) / completed | [43517469600](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43517469600) / success | [43517469600](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43517469600) / 2026-11-14 06:13:52 +0800 | 2.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [43517689540](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43517689540) / completed | [43517689540](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43517689540) / success | [43517689540](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43517689540) / 2026-11-14 06:15:19 +0800 | 2.7h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [43519514980](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43519514980) / completed | [43519514980](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43519514980) / success | [43519514980](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43519514980) / 2026-11-14 06:28:59 +0800 | 2.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [43521417760](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43521417760) / completed | [43521417760](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43521417760) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 339.4h | last success is stale (339.4h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [43537454520](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43537454520) / in_progress | [43343788179](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43343788179) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / completed | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / success | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / 2026-11-09 05:21:23 +0800 | 123.6h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 627.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [43343887948](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43343887948) / completed | [43343887948](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43343887948) / success | [43343887948](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43343887948) / 2026-11-13 09:18:21 +0800 | 23.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [43521582999](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43521582999) / completed | [43521582999](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43521582999) / success | [43521582999](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43521582999) / 2026-11-14 06:43:39 +0800 | 2.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
