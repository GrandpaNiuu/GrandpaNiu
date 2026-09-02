# Automation Status Report

- Generated at: 2026-09-03 06:44:25 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `26f7f792`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [33673504402](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33673504402) / completed | [33673504402](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33673504402) / success | [33673504402](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33673504402) / 2026-09-03 03:29:56 +0800 | 3.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [33673594494](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33673594494) / completed | [33673594494](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33673594494) / success | [33673594494](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33673594494) / 2026-09-03 03:30:24 +0800 | 3.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [33673765452](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33673765452) / completed | [33673765452](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33673765452) / success | [33673765452](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33673765452) / 2026-09-03 03:31:31 +0800 | 3.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [33673786142](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33673786142) / completed | [33673786142](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33673786142) / success | [33673786142](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33673786142) / 2026-09-03 03:31:55 +0800 | 3.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [33674735476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33674735476) / completed | [33674735476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33674735476) / success | [33674735476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33674735476) / 2026-09-03 03:41:31 +0800 | 3.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [33675758786](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33675758786) / completed | [33675758786](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33675758786) / success | [33675758786](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33675758786) / 2026-09-03 03:52:39 +0800 | 2.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [33691813363](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33691813363) / in_progress | [33567558651](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33567558651) / success | [33567558651](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33567558651) / 2026-09-02 06:42:33 +0800 | 24.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / completed | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / success | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / 2026-08-31 04:00:57 +0800 | 74.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 627.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [33567610108](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33567610108) / completed | [33567610108](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33567610108) / success | [33567610108](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33567610108) / 2026-09-02 06:43:06 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [33675928401](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33675928401) / completed | [33675928401](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33675928401) / success | [33675928401](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33675928401) / 2026-09-03 03:52:52 +0800 | 2.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
