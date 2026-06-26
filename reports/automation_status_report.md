# Automation Status Report

- Generated at: 2026-06-26 13:18:28 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28192190034](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28192190034) / completed | [28192190034](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28192190034) / success | [28192190034](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28192190034) / 2026-06-26 02:36:20 +0800 | 10.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28192279630](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28192279630) / completed | [28192279630](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28192279630) / success | [28192279630](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28192279630) / 2026-06-26 02:37:23 +0800 | 10.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28193460653](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28193460653) / completed | [28193460653](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28193460653) / success | [28193460653](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28193460653) / 2026-06-26 02:58:02 +0800 | 10.3h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28193714015](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28193714015) / completed | [28193714015](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28193714015) / success | [28193714015](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28193714015) / 2026-06-26 03:02:21 +0800 | 10.3h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28194089805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28194089805) / completed | [28194089805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28194089805) / success | [28194089805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28194089805) / 2026-06-26 03:08:55 +0800 | 10.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28194648635](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28194648635) / completed | [28194648635](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28194648635) / success | [28194648635](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28194648635) / 2026-06-26 03:19:35 +0800 | 10.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28203104967](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28203104967) / completed | [28203104967](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28203104967) / success | [28203104967](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28203104967) / 2026-06-26 05:58:37 +0800 | 7.3h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [27914441205](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) / completed | [27914441205](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) / success | [27914441205](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) / 2026-06-22 03:04:56 +0800 | 106.2h | ok |
| `module-factory-build.yml` | push/manual | observe | warn | [28218786548](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28218786548) / in_progress | [28216901206](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28216901206) / success | [28216901206](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28216901206) / 2026-06-26 12:21:38 +0800 | 57m | latest run is in_progress |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28216936440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28216936440) / completed | [28216936440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28216936440) / success | [28216936440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28216936440) / 2026-06-26 12:21:49 +0800 | 57m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
