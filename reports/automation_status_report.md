# Automation Status Report

- Generated at: 2026-11-27 11:00:13 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `f1f6d09b`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [45918657249](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45918657249) / completed | [45918657249](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45918657249) / success | [45918657249](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45918657249) / 2026-11-27 08:47:10 +0800 | 2.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [45918824229](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45918824229) / completed | [45918824229](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45918824229) / success | [45918824229](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45918824229) / 2026-11-27 08:48:19 +0800 | 2.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [45919016740](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45919016740) / completed | [45919016740](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45919016740) / success | [45919016740](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45919016740) / 2026-11-27 08:50:40 +0800 | 2.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [45919020148](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45919020148) / completed | [45919020148](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45919020148) / success | [45919020148](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45919020148) / 2026-11-27 08:50:11 +0800 | 2.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [45919857176](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45919857176) / completed | [45919857176](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45919857176) / success | [45919857176](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45919857176) / 2026-11-27 08:59:10 +0800 | 2.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [45920176170](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45920176170) / completed | [45920176170](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45920176170) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [45931548892](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45931548892) / in_progress | [45745768983](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45745768983) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / completed | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / success | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / 2026-11-23 06:45:10 +0800 | 100.3h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 941.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [45745844198](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45745844198) / completed | [45745844198](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45745844198) / success | [45745844198](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45745844198) / 2026-11-26 10:58:03 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [45920286984](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45920286984) / completed | [45920286984](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45920286984) / success | [45920286984](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45920286984) / 2026-11-27 09:03:05 +0800 | 2.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
