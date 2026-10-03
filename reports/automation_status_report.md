# Automation Status Report

- Generated at: 2026-10-04 07:13:32 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `68ae6add`
- Overall status: `fail`
- Blocking findings: 2
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [37147643136](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37147643136) / completed | [37147643136](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37147643136) / success | [37147643136](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37147643136) / 2026-10-04 03:23:39 +0800 | 3.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [37147703108](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37147703108) / completed | [37147703108](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37147703108) / success | [37147703108](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37147703108) / 2026-10-04 03:24:05 +0800 | 3.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [37148190307](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37148190307) / completed | [37148190307](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37148190307) / success | [37148190307](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37148190307) / 2026-10-04 03:31:56 +0800 | 3.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [37148181710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37148181710) / completed | [37148181710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37148181710) / success | [37148181710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37148181710) / 2026-10-04 03:31:31 +0800 | 3.7h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [37149031801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37149031801) / completed | [37149031801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37149031801) / success | [37149031801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37149031801) / 2026-10-04 03:45:55 +0800 | 3.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [37149859872](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37149859872) / completed | [37149859872](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37149859872) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 49.3h | last success is stale (49.3h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | warn | [37161055313](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37161055313) / in_progress | [37079701411](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37079701411) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 47.2h | latest completed run is failure on older commit 7d82f990; current commit 68ae6add will be checked by the next run |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / completed | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / success | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / 2026-09-28 04:21:38 +0800 | 146.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1372.1h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [37079758824](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37079758824) / completed | [37079758824](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37079758824) / success | [37079758824](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37079758824) / 2026-10-03 07:54:46 +0800 | 23.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [37149943397](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37149943397) / completed | [37149943397](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37149943397) / success | [37149943397](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37149943397) / 2026-10-04 04:00:24 +0800 | 3.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
