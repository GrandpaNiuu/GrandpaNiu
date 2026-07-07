# Automation Status Report

- Generated at: 2026-07-08 02:34:23 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `ea972812`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | warn | [28889621052](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28889621052) / in_progress | [28814059801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28814059801) / success | [28814059801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28814059801) / 2026-07-07 02:29:33 +0800 | 24.1h | latest run is in_progress |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28814132403](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28814132403) / completed | [28814132403](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28814132403) / success | [28814132403](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28814132403) / 2026-07-07 02:29:54 +0800 | 24.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28814370933](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28814370933) / completed | [28814370933](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28814370933) / success | [28814370933](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28814370933) / 2026-07-07 02:33:53 +0800 | 24.0h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28815220053](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28815220053) / completed | [28815220053](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28815220053) / success | [28815220053](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28815220053) / 2026-07-07 02:47:44 +0800 | 23.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28816071348](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28816071348) / completed | [28816071348](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28816071348) / success | [28816071348](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28816071348) / 2026-07-07 03:02:00 +0800 | 23.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28816594368](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28816594368) / completed | [28816594368](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28816594368) / success | [28816594368](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28816594368) / 2026-07-07 03:11:41 +0800 | 23.4h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28825832207](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825832207) / completed | [28825832207](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825832207) / success | [28825832207](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825832207) / 2026-07-07 05:53:49 +0800 | 20.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / completed | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / success | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / 2026-07-06 02:41:30 +0800 | 47.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [28756366178](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28756366178) / completed | [28756366178](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28756366178) / success | [28756366178](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28756366178) / 2026-07-06 06:03:23 +0800 | 44.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [28825852901](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825852901) / completed | [28825852901](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825852901) / success | [28825852901](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825852901) / 2026-07-07 05:54:19 +0800 | 20.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28825853015](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825853015) / completed | [28825853015](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825853015) / success | [28825853015](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825853015) / 2026-07-07 05:54:00 +0800 | 20.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
