# Automation Status Report

- Generated at: 2026-10-12 05:03:33 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `d3ec0cf6`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [38172590925](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172590925) / completed | [38172590925](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172590925) / success | [38172590925](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172590925) / 2026-10-12 04:33:07 +0800 | 30m | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [38172707683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172707683) / completed | [38172707683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172707683) / success | [38172707683](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172707683) / 2026-10-12 04:33:56 +0800 | 30m | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [38172950942](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172950942) / completed | [38172950942](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172950942) / success | [38172950942](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172950942) / 2026-10-12 04:37:24 +0800 | 26m | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [38172994770](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172994770) / completed | [38172994770](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172994770) / success | [38172994770](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38172994770) / 2026-10-12 04:37:59 +0800 | 26m | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [38174055902](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174055902) / completed | [38174055902](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174055902) / success | [38174055902](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174055902) / 2026-10-12 04:53:51 +0800 | 10m | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [38174460721](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174460721) / completed | [38174460721](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174460721) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 239.2h | last success is stale (239.2h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [38095897558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38095897558) / completed | [38095897558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38095897558) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 237.1h | last success is stale (237.1h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / in_progress | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / success | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / 2026-10-05 04:24:24 +0800 | 168.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1561.9h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [38095946572](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38095946572) / completed | [38095946572](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38095946572) / success | [38095946572](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38095946572) / 2026-10-11 07:42:29 +0800 | 21.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [38174559144](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174559144) / completed | [38174559144](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174559144) / success | [38174559144](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174559144) / 2026-10-12 05:00:36 +0800 | 3m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
