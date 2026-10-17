# Automation Status Report

- Generated at: 2026-10-18 06:29:39 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `0aeb895b`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [39059591413](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059591413) / completed | [39059591413](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059591413) / success | [39059591413](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059591413) / 2026-10-18 02:48:05 +0800 | 3.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [39059677683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059677683) / completed | [39059677683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059677683) / success | [39059677683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059677683) / 2026-10-18 02:48:32 +0800 | 3.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [39059969348](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059969348) / completed | [39059969348](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059969348) / success | [39059969348](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059969348) / 2026-10-18 02:52:31 +0800 | 3.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [39060025436](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39060025436) / completed | [39060025436](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39060025436) / success | [39060025436](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39060025436) / 2026-10-18 02:53:04 +0800 | 3.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [39061342237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39061342237) / completed | [39061342237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39061342237) / success | [39061342237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39061342237) / 2026-10-18 03:11:45 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [39062616430](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39062616430) / completed | [39062616430](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39062616430) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 384.6h | last success is stale (384.6h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [39075269715](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39075269715) / in_progress | [38978603720](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38978603720) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 382.5h | last success is stale (382.5h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / completed | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / success | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / 2026-10-12 05:03:52 +0800 | 145.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1707.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [38978682931](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38978682931) / completed | [38978682931](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38978682931) / success | [38978682931](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38978682931) / 2026-10-17 06:56:44 +0800 | 23.5h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [39062689483](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39062689483) / completed | [39062689483](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39062689483) / success | [39062689483](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39062689483) / 2026-10-18 03:29:44 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
