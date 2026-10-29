# Automation Status Report

- Generated at: 2026-10-30 05:23:59 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `cafa39db`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [40957324434](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957324434) / in_progress | [40770615277](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40770615277) / success | [40770615277](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40770615277) / 2026-10-29 05:18:17 +0800 | 24.1h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [40770799316](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40770799316) / completed | [40770799316](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40770799316) / success | [40770799316](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40770799316) / 2026-10-29 05:18:40 +0800 | 24.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [40771227822](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40771227822) / completed | [40771227822](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40771227822) / success | [40771227822](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40771227822) / 2026-10-29 05:22:05 +0800 | 24.0h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [40771306951](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40771306951) / completed | [40771306951](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40771306951) / success | [40771306951](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40771306951) / 2026-10-29 05:22:16 +0800 | 24.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [40773234199](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40773234199) / completed | [40773234199](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40773234199) / success | [40773234199](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40773234199) / 2026-10-29 05:36:34 +0800 | 23.8h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [40774208460](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40774208460) / completed | [40774208460](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40774208460) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [40791959388](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40791959388) / completed | [40791959388](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40791959388) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / completed | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / success | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / 2026-10-26 03:56:06 +0800 | 97.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 263.9h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [40792040889](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40792040889) / completed | [40792040889](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40792040889) / success | [40792040889](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40792040889) / 2026-10-29 08:08:19 +0800 | 21.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [40792061036](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40792061036) / completed | [40792061036](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40792061036) / success | [40792061036](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40792061036) / 2026-10-29 08:08:29 +0800 | 21.3h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
