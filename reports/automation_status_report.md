# Automation Status Report

- Generated at: 2026-10-18 02:47:45 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `a1ca5993`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [39059591413](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059591413) / in_progress | [38956639589](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38956639589) / success | [38956639589](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38956639589) / 2026-10-17 03:41:53 +0800 | 23.1h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [38956753587](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38956753587) / completed | [38956753587](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38956753587) / success | [38956753587](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38956753587) / 2026-10-17 03:42:07 +0800 | 23.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [38956968206](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38956968206) / completed | [38956968206](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38956968206) / success | [38956968206](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38956968206) / 2026-10-17 03:43:36 +0800 | 23.1h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [38957002850](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38957002850) / completed | [38957002850](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38957002850) / success | [38957002850](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38957002850) / 2026-10-17 03:43:51 +0800 | 23.1h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [38958051378](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38958051378) / completed | [38958051378](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38958051378) / success | [38958051378](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38958051378) / 2026-10-17 03:52:53 +0800 | 22.9h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [38958840053](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38958840053) / completed | [38958840053](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38958840053) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 380.9h | last success is stale (380.9h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [38978603720](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38978603720) / completed | [38978603720](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38978603720) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 378.8h | last success is stale (378.8h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / completed | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / success | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / 2026-10-12 05:03:52 +0800 | 141.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1703.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [38978682931](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38978682931) / completed | [38978682931](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38978682931) / success | [38978682931](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38978682931) / 2026-10-17 06:56:44 +0800 | 19.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [38978695527](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38978695527) / completed | [38978695527](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38978695527) / success | [38978695527](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38978695527) / 2026-10-17 06:56:53 +0800 | 19.8h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
