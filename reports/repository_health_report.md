# Repository Health Report

- Generated at: 2026-06-23 03:56:44 +0800
- Blocking issues: 0
- Root and Release identical: yes
- Fusion profile finalized: yes
- validate_repository.py: passed
- automated quality evidence: passed
- node --check Scripts/app-cleaner.js: passed
- Script entries: 26
- MITM hostnames: 1235

## Section Counts

- [Rule]: 1390
- [URL Rewrite]: 2692
- [Header Rewrite]: 2
- [Body Rewrite]: 1652
- [Map Local]: 352
- [Script]: 44
- [MITM]: 1

## Blocking Issues

- none

## Missing Files

- none

## Missing Workflows

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
- `.github/workflows/daily-audit-and-repair.yml`: contents: write; isolated concurrency; fusion; safe commit helper; cross-workflow lock; rebase retry
- `.github/workflows/daily-invalid-source-repair.yml`: contents: write; isolated concurrency; fusion; safe commit helper; cross-workflow lock; rebase retry
- `.github/workflows/scheduled-module-update.yml`: contents: write; isolated concurrency; fusion; safe commit helper; cross-workflow lock; rebase retry
- `.github/workflows/upstream-app-module-sync.yml`: contents: write; isolated concurrency; fusion; safe commit helper; cross-workflow lock; rebase retry
- `.github/workflows/upstream-collect.yml`: contents: write; isolated concurrency; fusion; safe commit helper; cross-workflow lock; rebase retry
- `.github/workflows/daily-schedule-watchdog.yml`: contents: write; isolated concurrency; fusion; safe commit helper; cross-workflow lock; rebase retry
- `.github/workflows/repository-health.yml`: contents: write; isolated concurrency; fusion; safe commit helper; cross-workflow lock; rebase retry

## validate_repository.py Output

```text
Repository validation passed.
./scripts/validate_repository.py:272: SyntaxWarning: invalid escape sequence '//'
  normalized = lowered.replace("//", "/")
```

## automated quality evidence Output

```text
Automated quality evidence written to ./reports/automated_quality_evidence.md
```

## node --check Output

```text
no output
```
