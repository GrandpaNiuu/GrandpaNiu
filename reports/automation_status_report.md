# Automation Status Report

- Generated at: 2026-10-13 07:12:13 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `a19ed015`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [38320781932](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38320781932) / in_progress | [38172590925](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172590925) / success | [38172590925](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172590925) / 2026-10-12 04:33:07 +0800 | 26.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [38172707683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172707683) / completed | [38172707683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172707683) / success | [38172707683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172707683) / 2026-10-12 04:33:56 +0800 | 26.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [38172950942](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172950942) / completed | [38172950942](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172950942) / success | [38172950942](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172950942) / 2026-10-12 04:37:24 +0800 | 26.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [38172994770](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172994770) / completed | [38172994770](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172994770) / success | [38172994770](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172994770) / 2026-10-12 04:37:59 +0800 | 26.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [38174055902](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174055902) / completed | [38174055902](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174055902) / success | [38174055902](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174055902) / 2026-10-12 04:53:51 +0800 | 26.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [38174460721](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174460721) / completed | [38174460721](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174460721) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 265.3h | last success is stale (265.3h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [38185628650](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38185628650) / completed | [38185628650](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38185628650) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 263.2h | last success is stale (263.2h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / completed | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / success | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / 2026-10-12 05:03:52 +0800 | 26.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1588.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [38185676530](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38185676530) / completed | [38185676530](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38185676530) / success | [38185676530](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38185676530) / 2026-10-12 07:48:57 +0800 | 23.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [38185685346](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38185685346) / completed | [38185685346](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38185685346) / success | [38185685346](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38185685346) / 2026-10-12 07:49:05 +0800 | 23.4h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
