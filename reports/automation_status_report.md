# Automation Status Report

- Generated at: 2026-10-02 08:00:09 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `d7b8de1a`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [36927573214](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36927573214) / completed | [36927573214](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36927573214) / success | [36927573214](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36927573214) / 2026-10-02 05:18:18 +0800 | 2.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [36927909100](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36927909100) / completed | [36927909100](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36927909100) / success | [36927909100](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36927909100) / 2026-10-02 05:20:13 +0800 | 2.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [36928468379](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36928468379) / completed | [36928468379](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36928468379) / success | [36928468379](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36928468379) / 2026-10-02 05:25:02 +0800 | 2.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [36928533428](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36928533428) / completed | [36928533428](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36928533428) / success | [36928533428](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36928533428) / 2026-10-02 05:25:30 +0800 | 2.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [36930628818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36930628818) / completed | [36930628818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36930628818) / success | [36930628818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36930628818) / 2026-10-02 05:45:07 +0800 | 2.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / completed | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / success | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 2.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / in_progress | [36793978555](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36793978555) / success | [36793978555](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36793978555) / 2026-10-01 08:01:18 +0800 | 24.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / completed | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / success | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / 2026-09-28 04:21:38 +0800 | 99.6h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1324.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [36794043051](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36794043051) / completed | [36794043051](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36794043051) / success | [36794043051](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36794043051) / 2026-10-01 08:02:12 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [36931612833](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931612833) / completed | [36931612833](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931612833) / success | [36931612833](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931612833) / 2026-10-02 05:53:24 +0800 | 2.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
