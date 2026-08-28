# Repository Health Report

- Generated at: 2026-08-28 09:06:41 +0800
- Blocking issues: 0
- Root and Release identical: yes
- Release alias identical: yes
- Fusion profile finalized: yes
- validate_repository.py: passed
- automated quality evidence: passed
- node --check Scripts/app-cleaner.js: passed
- Script entries: 26
- MITM hostnames: 1189

## Section Counts

- [Rule]: 1194
- [URL Rewrite]: 40
- [Header Rewrite]: 2
- [Body Rewrite]: 1435
- [Map Local]: 37
- [Script]: 45
- [MITM]: 1

## Blocking Issues

- none

## Missing Files

- none

## Missing Workflows

- none

## Pages Deploy Workflow Findings

- none

## Missing Fusion Markers

- none

## Duplicate Script Names

- none

## Duplicate MITM Hostnames

- none

## Workflow Summary

- `.github/workflows/module-factory-build.yml`: contents: write; isolated concurrency; fusion; safe commit helper; cross-workflow lock; rebase retry
- `.github/workflows/daily-module-update.yml`: contents: write; isolated concurrency; fusion; safe commit helper; cross-workflow lock; rebase retry
- `.github/workflows/daily-audit-and-repair.yml`: contents: write; isolated concurrency; missing fusion build; safe commit helper; cross-workflow lock; rebase retry
- `.github/workflows/daily-invalid-source-repair.yml`: contents: write; isolated concurrency; fusion; safe commit helper; cross-workflow lock; rebase retry
- `.github/workflows/scheduled-module-update.yml`: contents: write; isolated concurrency; fusion; safe commit helper; cross-workflow lock; rebase retry
- `.github/workflows/upstream-app-module-sync.yml`: contents: write; isolated concurrency; fusion; safe commit helper; cross-workflow lock; rebase retry
- `.github/workflows/upstream-collect.yml`: contents: write; isolated concurrency; fusion; safe commit helper; cross-workflow lock; rebase retry
- `.github/workflows/daily-schedule-watchdog.yml`: contents: write; isolated concurrency; fusion; safe commit helper; cross-workflow lock; rebase retry
- `.github/workflows/repository-health.yml`: contents: write; isolated concurrency; fusion; safe commit helper; cross-workflow lock; rebase retry
- `pages-deploy.yml`: self-managed Pages deploy; artifact upload; maximum supported deploy timeout; serialized final deploys; deploy retry guard

## validate_repository.py Output

```text
Repository validation passed.
```

## automated quality evidence Output

```text
Automated quality evidence written to ./reports/automated_quality_evidence.md
```

## node --check Output

```text
no output
```
