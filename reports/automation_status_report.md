# Automation Status Report

- Generated at: 2026-08-30 06:42:47 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `121fae99`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [33270984810](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33270984810) / completed | [33270984810](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33270984810) / success | [33270984810](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33270984810) / 2026-08-30 03:30:30 +0800 | 3.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [33271010102](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271010102) / completed | [33271010102](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271010102) / success | [33271010102](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271010102) / 2026-08-30 03:30:48 +0800 | 3.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [33271071848](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271071848) / completed | [33271071848](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271071848) / success | [33271071848](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271071848) / 2026-08-30 03:31:49 +0800 | 3.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [33271089591](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271089591) / completed | [33271089591](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271089591) / success | [33271089591](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271089591) / 2026-08-30 03:32:05 +0800 | 3.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [33271430218](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271430218) / completed | [33271430218](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271430218) / success | [33271430218](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271430218) / 2026-08-30 03:39:56 +0800 | 3.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [33271783087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271783087) / completed | [33271783087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271783087) / success | [33271783087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271783087) / 2026-08-30 03:49:07 +0800 | 2.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [33279246810](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33279246810) / in_progress | [33229979924](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33229979924) / success | [33229979924](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33229979924) / 2026-08-29 10:52:16 +0800 | 19.8h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / completed | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / success | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / 2026-08-24 01:52:11 +0800 | 148.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 531.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [33230004387](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33230004387) / completed | [33230004387](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33230004387) / success | [33230004387](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33230004387) / 2026-08-29 10:52:48 +0800 | 19.8h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [33271851709](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271851709) / completed | [33271851709](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271851709) / success | [33271851709](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33271851709) / 2026-08-30 03:49:22 +0800 | 2.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
