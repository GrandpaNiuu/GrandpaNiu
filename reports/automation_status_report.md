# Automation Status Report

- Generated at: 2026-07-23 01:51:11 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `609f59b3`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [29944067764](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29944067764) / in_progress | [29854996689](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29854996689) / success | [29854996689](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29854996689) / 2026-07-22 01:56:35 +0800 | 23.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29855103435](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29855103435) / completed | [29855103435](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29855103435) / success | [29855103435](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29855103435) / 2026-07-22 01:57:22 +0800 | 23.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29855408502](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29855408502) / completed | [29855408502](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29855408502) / success | [29855408502](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29855408502) / 2026-07-22 02:01:26 +0800 | 23.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29855509980](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29855509980) / completed | [29855509980](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29855509980) / success | [29855509980](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29855509980) / 2026-07-22 02:02:47 +0800 | 23.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29856747761](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29856747761) / completed | [29856747761](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29856747761) / success | [29856747761](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29856747761) / 2026-07-22 02:20:43 +0800 | 23.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29858428933](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29858428933) / completed | [29858428933](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29858428933) / success | [29858428933](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29858428933) / 2026-07-22 02:44:59 +0800 | 23.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [29870703999](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29870703999) / completed | [29870703999](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29870703999) / success | [29870703999](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29870703999) / 2026-07-22 05:38:08 +0800 | 20.2h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / completed | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / success | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / 2026-07-20 02:33:21 +0800 | 71.3h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 165.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29870741955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29870741955) / completed | [29870741955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29870741955) / success | [29870741955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29870741955) / 2026-07-22 05:38:41 +0800 | 20.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29870777740](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29870777740) / completed | [29870777740](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29870777740) / success | [29870777740](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29870777740) / 2026-07-22 05:38:51 +0800 | 20.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
