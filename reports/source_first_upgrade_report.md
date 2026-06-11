# Source-first Upgrade Report

Date: 2026-05-30

## Completed changes

- Added `scripts/validate_repository.py` as the unified repository validator.
- Reworked `scripts/audit_repair_invalid_sources.py` into a source-first invalid source audit and repair tool.
- Updated `.github/workflows/daily-invalid-source-repair.yml` to repair source files first, rebuild Release, sync root, and run the validator.
- Updated `.github/workflows/module-factory-build.yml` to use `scripts/validate_repository.py`.
- Updated `.github/workflows/upstream-collect.yml` to use `scripts/validate_repository.py`.
- Rewrote `docs/MAINTENANCE.md` for the source-driven factory workflow.
- Expanded `Rewrite/Remotes/candidates.json` with additional low-risk remote rule candidates while keeping scripts pending.

## Source-first invalid repair model

The invalid-source repair now audits and repairs these source locations first:

```text
Rewrite/Remotes/sources.json
Rewrite/Remotes/candidates.json
Rules/*.list
Scripts/*.conf
Rewrite/Sources/*.conf
```

After repairs, the workflow runs:

```text
python3 scripts/build_module.py --build --profile fusion
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
```

This prevents root-only edits from being overwritten by the next factory build.

## Unified validation coverage

`validate_repository.py` checks:

- Root and Release are identical.
- Required module sections exist.
- `spotify-json`, `spotify-proto`, and `youtube.response` exist.
- `update-url` is correct.
- `sources.json` and `candidates.json` are schema-valid enough for maintenance use.
- Remote URLs are HTTPS and avoid short links, proxies, and mirrors.
- `Scripts/spotify.conf` does not contain ordinary App scripts.
- `Scripts/youtube.conf` does not contain ordinary App scripts.
- `Rules/spotify-direct.list` contains no `REJECT` rules.
- MITM hostname entries are not duplicated.
- README local links resolve to existing files.
- `.claude` and `CLAUDE.md` are absent.

## Candidate pool changes

Added or kept enabled low-risk remote-rule candidates:

- blackmatrix7 Advertising Lite
- blackmatrix7 Hijacking
- blackmatrix7 Privacy
- blackmatrix7 Privacy Lite
- blackmatrix7 Advertising MiTV
- ACL4SSR BanProgramAD
- ACL4SSR BanEasyListChina

Kept scripts pending / disabled:

- app2smile Tieba script
- Maasea YouTube Enhance reference

Kept disabled to avoid duplicates or risk flags:

- Loyalsoldier reject domain set
- Cats-Team AdRules DNS list

## Manual follow-up

Run these workflows once from GitHub Actions:

```text
Module Factory Build
Upstream candidate collect
Daily invalid source audit and repair
```

Then confirm:

- `reports/module_factory_diff_report.md` says diff lines are `0`.
- `reports/upstream_collect_report.md` shows only safe candidates added or skipped.
- `reports/invalid_sources_report.md` says source-first mode.
- Shadowrocket can update the module and scripts normally.
