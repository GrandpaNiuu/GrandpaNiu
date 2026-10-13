# Automation Status Report

- Generated at: 2026-10-14 05:30:47 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `33d18912`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [38471046804](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38471046804) / in_progress | [38320781932](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38320781932) / success | [38320781932](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38320781932) / 2026-10-13 07:12:30 +0800 | 22.3h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [38320895552](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38320895552) / completed | [38320895552](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38320895552) / success | [38320895552](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38320895552) / 2026-10-13 07:12:54 +0800 | 22.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [38321139577](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38321139577) / completed | [38321139577](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38321139577) / success | [38321139577](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38321139577) / 2026-10-13 07:15:53 +0800 | 22.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [38321236366](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38321236366) / completed | [38321236366](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38321236366) / success | [38321236366](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38321236366) / 2026-10-13 07:16:39 +0800 | 22.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [38322793994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38322793994) / completed | [38322793994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38322793994) / success | [38322793994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38322793994) / 2026-10-13 07:34:38 +0800 | 21.9h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [38323209621](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38323209621) / completed | [38323209621](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38323209621) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 287.6h | last success is stale (287.6h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [38335527983](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38335527983) / completed | [38335527983](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38335527983) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 285.5h | last success is stale (285.5h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / completed | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / success | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / 2026-10-12 05:03:52 +0800 | 48.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1610.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [38335593880](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38335593880) / completed | [38335593880](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38335593880) / success | [38335593880](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38335593880) / 2026-10-13 10:10:15 +0800 | 19.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [38335608939](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38335608939) / completed | [38335608939](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38335608939) / success | [38335608939](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38335608939) / 2026-10-13 10:10:26 +0800 | 19.3h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
