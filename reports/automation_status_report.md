# Automation Status Report

- Generated at: 2026-10-15 07:20:18 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `75ba74a2`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [38630927369](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38630927369) / completed | [38630927369](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38630927369) / success | [38630927369](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38630927369) / 2026-10-15 04:19:58 +0800 | 3.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [38631009854](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38631009854) / completed | [38631009854](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38631009854) / success | [38631009854](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38631009854) / 2026-10-15 04:20:28 +0800 | 3.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [38631205808](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38631205808) / completed | [38631205808](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38631205808) / success | [38631205808](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38631205808) / 2026-10-15 04:21:03 +0800 | 3.0h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [38631284878](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38631284878) / completed | [38631284878](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38631284878) / success | [38631284878](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38631284878) / 2026-10-15 04:21:24 +0800 | 3.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [38632999018](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38632999018) / completed | [38632999018](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38632999018) / success | [38632999018](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38632999018) / 2026-10-15 04:33:44 +0800 | 2.8h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [38634693726](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38634693726) / completed | [38634693726](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38634693726) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 313.5h | last success is stale (313.5h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [38653403801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38653403801) / in_progress | [38486312243](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38486312243) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 311.3h | last success is stale (311.3h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / completed | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / success | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / 2026-10-12 05:03:52 +0800 | 74.3h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1636.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [38486375671](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38486375671) / completed | [38486375671](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38486375671) / success | [38486375671](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38486375671) / 2026-10-14 07:47:46 +0800 | 23.5h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [38634882772](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38634882772) / completed | [38634882772](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38634882772) / success | [38634882772](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38634882772) / 2026-10-15 04:46:36 +0800 | 2.6h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
