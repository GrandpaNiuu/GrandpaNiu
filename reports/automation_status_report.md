# Automation Status Report

- Generated at: 2026-06-26 21:37:59 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28192190034](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28192190034) / completed | [28192190034](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28192190034) / success | [28192190034](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28192190034) / 2026-06-26 02:36:20 +0800 | 19.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28192279630](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28192279630) / completed | [28192279630](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28192279630) / success | [28192279630](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28192279630) / 2026-06-26 02:37:23 +0800 | 19.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28193460653](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28193460653) / completed | [28193460653](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28193460653) / success | [28193460653](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28193460653) / 2026-06-26 02:58:02 +0800 | 18.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28193714015](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28193714015) / completed | [28193714015](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28193714015) / success | [28193714015](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28193714015) / 2026-06-26 03:02:21 +0800 | 18.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28194089805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28194089805) / completed | [28194089805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28194089805) / success | [28194089805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28194089805) / 2026-06-26 03:08:55 +0800 | 18.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28194648635](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28194648635) / completed | [28194648635](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28194648635) / success | [28194648635](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28194648635) / 2026-06-26 03:19:35 +0800 | 18.3h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28203104967](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28203104967) / completed | [28203104967](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28203104967) / success | [28203104967](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28203104967) / 2026-06-26 05:58:37 +0800 | 15.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [27914441205](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) / completed | [27914441205](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) / success | [27914441205](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) / 2026-06-22 03:04:56 +0800 | 114.6h | ok |
| `module-factory-build.yml` | push/manual | observe | warn | [28241639287](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28241639287) / in_progress | [28241560771](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28241560771) / success | [28241560771](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28241560771) / 2026-06-26 21:36:48 +0800 | 1m | latest run is in_progress |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28241609761](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28241609761) / completed | [28241609761](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28241609761) / success | [28241609761](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28241609761) / 2026-06-26 21:36:58 +0800 | 1m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
