# Automation Status Report

- Generated at: 2026-07-03 09:52:04 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `ed1905c9`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28612079280](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612079280) / completed | [28612079280](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612079280) / success | [28612079280](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612079280) / 2026-07-03 02:18:25 +0800 | 7.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28612144710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612144710) / completed | [28612144710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612144710) / success | [28612144710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612144710) / 2026-07-03 02:20:08 +0800 | 7.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28612258753](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612258753) / completed | [28612258753](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612258753) / success | [28612258753](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612258753) / 2026-07-03 02:20:52 +0800 | 7.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28612269717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612269717) / completed | [28612269717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612269717) / success | [28612269717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28612269717) / 2026-07-03 02:21:07 +0800 | 7.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28613455296](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28613455296) / completed | [28613455296](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28613455296) / success | [28613455296](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28613455296) / 2026-07-03 02:40:53 +0800 | 7.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28628442431](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28628442431) / completed | [28628442431](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28628442431) / success | [28628442431](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28628442431) / 2026-07-03 07:39:28 +0800 | 2.2h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28623373028](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28623373028) / completed | [28623373028](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28623373028) / success | [28623373028](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28623373028) / 2026-07-03 05:41:53 +0800 | 4.2h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / completed | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / success | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / 2026-06-29 02:48:00 +0800 | 103.1h | ok |
| `module-factory-build.yml` | push/manual | observe | warn | [28633173916](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28633173916) / in_progress | [28632613926](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28632613926) / success | [28632613926](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28632613926) / 2026-07-03 09:35:36 +0800 | 16m | latest run is in_progress |
| `pages-deploy.yml` | workflow_run / manual / public-path push | observe | ok | [28633173915](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28633173915) / completed | [28633173915](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28633173915) / success | [28633173915](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28633173915) / 2026-07-03 09:51:38 +0800 | 0m | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28632648150](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28632648150) / completed | [28632648150](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28632648150) / success | [28632648150](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28632648150) / 2026-07-03 09:35:45 +0800 | 16m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
