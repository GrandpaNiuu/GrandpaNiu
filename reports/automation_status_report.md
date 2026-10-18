# Automation Status Report

- Generated at: 2026-10-19 02:53:12 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `728224b5`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [39156151388](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156151388) / in_progress | [39059591413](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059591413) / success | [39059591413](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059591413) / 2026-10-18 02:48:05 +0800 | 24.1h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [39059677683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059677683) / completed | [39059677683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059677683) / success | [39059677683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059677683) / 2026-10-18 02:48:32 +0800 | 24.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [39059969348](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059969348) / completed | [39059969348](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059969348) / success | [39059969348](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39059969348) / 2026-10-18 02:52:31 +0800 | 24.0h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [39060025436](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39060025436) / completed | [39060025436](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39060025436) / success | [39060025436](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39060025436) / 2026-10-18 02:53:04 +0800 | 24.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [39061342237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39061342237) / completed | [39061342237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39061342237) / success | [39061342237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39061342237) / 2026-10-18 03:11:45 +0800 | 23.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [39062616430](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39062616430) / completed | [39062616430](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39062616430) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 405.0h | last success is stale (405.0h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [39075269715](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39075269715) / completed | [39075269715](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39075269715) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 402.9h | last success is stale (402.9h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / completed | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / success | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / 2026-10-12 05:03:52 +0800 | 165.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1727.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [39075314998](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39075314998) / completed | [39075314998](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39075314998) / success | [39075314998](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39075314998) / 2026-10-18 06:30:07 +0800 | 20.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [39075327310](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39075327310) / completed | [39075327310](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39075327310) / success | [39075327310](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39075327310) / 2026-10-18 06:30:16 +0800 | 20.4h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
