# Automation Status Report

- Generated at: 2026-06-30 05:50:13 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28394164970](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28394164970) / completed | [28394164970](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28394164970) / success | [28394164970](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28394164970) / 2026-06-30 02:33:11 +0800 | 3.3h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28394169601](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28394169601) / completed | [28394169601](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28394169601) / success | [28394169601](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28394169601) / 2026-06-30 02:33:35 +0800 | 3.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28395348517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28395348517) / completed | [28395348517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28395348517) / success | [28395348517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28395348517) / 2026-06-30 02:53:53 +0800 | 2.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28395386293](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28395386293) / completed | [28395386293](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28395386293) / success | [28395386293](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28395386293) / 2026-06-30 02:54:26 +0800 | 2.9h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28396153463](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28396153463) / completed | [28396153463](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28396153463) / success | [28396153463](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28396153463) / 2026-06-30 03:08:33 +0800 | 2.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28396641424](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28396641424) / completed | [28396641424](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28396641424) / success | [28396641424](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28396641424) / 2026-06-30 03:17:59 +0800 | 2.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | warn | [28404980325](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28404980325) / in_progress | [28336775405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28336775405) / success | [28336775405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28336775405) / 2026-06-29 05:36:17 +0800 | 24.2h | latest run is in_progress |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / completed | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / success | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / 2026-06-29 02:48:00 +0800 | 27.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / completed | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / success | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / 2026-06-26 22:24:31 +0800 | 79.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28396694729](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28396694729) / completed | [28396694729](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28396694729) / success | [28396694729](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28396694729) / 2026-06-30 03:18:10 +0800 | 2.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
