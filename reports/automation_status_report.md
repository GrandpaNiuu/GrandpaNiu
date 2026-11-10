# Automation Status Report

- Generated at: 2026-11-10 10:49:48 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `36e49c8f`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [42727944684](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42727944684) / completed | [42727944684](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42727944684) / success | [42727944684](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42727944684) / 2026-11-10 08:25:01 +0800 | 2.4h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [42728052942](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42728052942) / completed | [42728052942](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42728052942) / success | [42728052942](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42728052942) / 2026-11-10 08:25:21 +0800 | 2.4h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [42728380744](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42728380744) / completed | [42728380744](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42728380744) / success | [42728380744](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42728380744) / 2026-11-10 08:27:38 +0800 | 2.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [42728434509](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42728434509) / completed | [42728434509](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42728434509) / success | [42728434509](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42728434509) / 2026-11-10 08:27:48 +0800 | 2.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [42729740791](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42729740791) / completed | [42729740791](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42729740791) / success | [42729740791](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42729740791) / 2026-11-10 08:38:32 +0800 | 2.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [42730453814](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42730453814) / completed | [42730453814](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42730453814) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 245.2h | last success is stale (245.2h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [42745357396](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42745357396) / in_progress | [42537132870](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42537132870) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / completed | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / success | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / 2026-11-09 05:21:23 +0800 | 29.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 533.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [42537192154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42537192154) / completed | [42537192154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42537192154) / success | [42537192154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42537192154) / 2026-11-09 07:51:52 +0800 | 27.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [42730622677](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42730622677) / completed | [42730622677](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42730622677) / success | [42730622677](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42730622677) / 2026-11-10 08:44:49 +0800 | 2.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
