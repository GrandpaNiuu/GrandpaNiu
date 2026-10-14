# Automation Status Report

- Generated at: 2026-10-15 04:19:38 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `5f1207ea`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [38630927369](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38630927369) / in_progress | [38471046804](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38471046804) / success | [38471046804](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38471046804) / 2026-10-14 05:31:10 +0800 | 22.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [38631009854](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38631009854) / in_progress | [38471303280](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38471303280) / success | [38471303280](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38471303280) / 2026-10-14 05:32:19 +0800 | 22.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [38471605798](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38471605798) / completed | [38471605798](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38471605798) / success | [38471605798](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38471605798) / 2026-10-14 05:35:11 +0800 | 22.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [38471639254](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38471639254) / completed | [38471639254](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38471639254) / success | [38471639254](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38471639254) / 2026-10-14 05:35:34 +0800 | 22.7h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [38473134961](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38473134961) / completed | [38473134961](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38473134961) / success | [38473134961](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38473134961) / 2026-10-14 05:48:03 +0800 | 22.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [38473849019](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38473849019) / completed | [38473849019](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38473849019) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 310.4h | last success is stale (310.4h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [38486312243](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38486312243) / completed | [38486312243](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38486312243) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 308.3h | last success is stale (308.3h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / completed | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / success | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / 2026-10-12 05:03:52 +0800 | 71.3h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1633.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [38486375671](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38486375671) / completed | [38486375671](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38486375671) / success | [38486375671](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38486375671) / 2026-10-14 07:47:46 +0800 | 20.5h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [38486392323](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38486392323) / completed | [38486392323](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38486392323) / success | [38486392323](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38486392323) / 2026-10-14 07:47:58 +0800 | 20.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
