# Automation Status Report

- Generated at: 2026-10-03 07:54:09 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `7d82f990`
- Overall status: `fail`
- Blocking findings: 1
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [37063711548](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37063711548) / completed | [37063711548](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37063711548) / success | [37063711548](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37063711548) / 2026-10-03 04:57:30 +0800 | 2.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [37063850438](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37063850438) / completed | [37063850438](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37063850438) / success | [37063850438](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37063850438) / 2026-10-03 04:57:45 +0800 | 2.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [37064347837](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37064347837) / completed | [37064347837](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37064347837) / success | [37064347837](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37064347837) / 2026-10-03 05:02:39 +0800 | 2.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [37064435265](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37064435265) / completed | [37064435265](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37064435265) / success | [37064435265](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37064435265) / 2026-10-03 05:03:14 +0800 | 2.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [37065717753](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37065717753) / completed | [37065717753](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37065717753) / success | [37065717753](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37065717753) / 2026-10-03 05:16:07 +0800 | 2.6h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [37066285253](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37066285253) / completed | [37066285253](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37066285253) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 26.0h | latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [37079701411](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37079701411) / in_progress | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / success | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 23.9h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / completed | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / success | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / 2026-09-28 04:21:38 +0800 | 123.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1348.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [36943769496](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943769496) / completed | [36943769496](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943769496) / success | [36943769496](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943769496) / 2026-10-02 08:01:01 +0800 | 23.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [37066425124](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37066425124) / completed | [37066425124](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37066425124) / success | [37066425124](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37066425124) / 2026-10-03 05:22:27 +0800 | 2.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
