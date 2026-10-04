# Automation Status Report

- Generated at: 2026-10-05 07:22:56 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `b5755468`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [37229580261](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37229580261) / completed | [37229580261](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37229580261) / success | [37229580261](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37229580261) / 2026-10-05 03:48:13 +0800 | 3.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [37229608369](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37229608369) / completed | [37229608369](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37229608369) / success | [37229608369](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37229608369) / 2026-10-05 03:48:39 +0800 | 3.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [37229694173](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37229694173) / completed | [37229694173](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37229694173) / success | [37229694173](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37229694173) / 2026-10-05 03:49:18 +0800 | 3.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [37229714054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37229714054) / completed | [37229714054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37229714054) / success | [37229714054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37229714054) / 2026-10-05 03:49:35 +0800 | 3.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [37230500192](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37230500192) / completed | [37230500192](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37230500192) / success | [37230500192](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37230500192) / 2026-10-05 04:02:16 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [37231271675](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231271675) / completed | [37231271675](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231271675) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 73.5h | last success is stale (73.5h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [37243530161](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37243530161) / in_progress | [37161055313](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37161055313) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 71.4h | last success is stale (71.4h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / completed | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / success | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / 2026-10-05 04:24:24 +0800 | 3.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1396.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [37161095884](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37161095884) / completed | [37161095884](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37161095884) / success | [37161095884](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37161095884) / 2026-10-04 07:14:04 +0800 | 24.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [37231969264](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231969264) / completed | [37231969264](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231969264) / success | [37231969264](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231969264) / 2026-10-05 04:24:42 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
