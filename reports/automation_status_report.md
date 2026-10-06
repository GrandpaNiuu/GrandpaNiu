# Automation Status Report

- Generated at: 2026-10-07 07:56:15 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `9cfdb341`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [37532096335](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37532096335) / completed | [37532096335](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37532096335) / success | [37532096335](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37532096335) / 2026-10-07 05:13:05 +0800 | 2.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [37532253142](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37532253142) / completed | [37532253142](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37532253142) / success | [37532253142](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37532253142) / 2026-10-07 05:13:43 +0800 | 2.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [37532664204](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37532664204) / completed | [37532664204](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37532664204) / success | [37532664204](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37532664204) / 2026-10-07 05:16:48 +0800 | 2.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [37532794471](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37532794471) / completed | [37532794471](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37532794471) / success | [37532794471](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37532794471) / 2026-10-07 05:17:43 +0800 | 2.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [37534683601](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37534683601) / completed | [37534683601](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37534683601) / success | [37534683601](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37534683601) / 2026-10-07 05:33:59 +0800 | 2.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [37535700176](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37535700176) / completed | [37535700176](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37535700176) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 122.1h | last success is stale (122.1h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [37549233341](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37549233341) / in_progress | [37398717919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37398717919) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 119.9h | last success is stale (119.9h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / completed | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / success | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / 2026-10-05 04:24:24 +0800 | 51.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1444.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [37398775306](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37398775306) / completed | [37398775306](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37398775306) / success | [37398775306](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37398775306) / 2026-10-06 09:21:58 +0800 | 22.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [37535878010](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37535878010) / completed | [37535878010](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37535878010) / success | [37535878010](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37535878010) / 2026-10-07 05:43:39 +0800 | 2.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
