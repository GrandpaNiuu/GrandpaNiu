# Automation Status Report

- Generated at: 2026-08-29 10:51:52 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `56ed0be0`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [33224171970](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33224171970) / completed | [33224171970](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33224171970) / success | [33224171970](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33224171970) / 2026-08-29 08:40:49 +0800 | 2.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [33224259016](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33224259016) / completed | [33224259016](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33224259016) / success | [33224259016](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33224259016) / 2026-08-29 08:41:42 +0800 | 2.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [33224343860](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33224343860) / completed | [33224343860](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33224343860) / success | [33224343860](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33224343860) / 2026-08-29 08:43:24 +0800 | 2.1h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [33224420337](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33224420337) / completed | [33224420337](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33224420337) / success | [33224420337](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33224420337) / 2026-08-29 08:44:51 +0800 | 2.1h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [33224980509](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33224980509) / completed | [33224980509](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33224980509) / success | [33224980509](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33224980509) / 2026-08-29 08:56:57 +0800 | 1.9h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [33225139311](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33225139311) / completed | [33225139311](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33225139311) / success | [33225139311](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33225139311) / 2026-08-29 09:01:19 +0800 | 1.8h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [33229979924](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33229979924) / in_progress | [33141710320](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33141710320) / success | [33141710320](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33141710320) / 2026-08-28 12:25:03 +0800 | 22.4h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / completed | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / success | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / 2026-08-24 01:52:11 +0800 | 129.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 511.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [33141750097](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33141750097) / completed | [33141750097](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33141750097) / success | [33141750097](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33141750097) / 2026-08-28 12:25:40 +0800 | 22.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [33225244871](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33225244871) / completed | [33225244871](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33225244871) / success | [33225244871](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33225244871) / 2026-08-29 09:01:30 +0800 | 1.8h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
