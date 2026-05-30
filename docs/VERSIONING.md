# Versioning Policy

GrandpaNiu uses date-based module metadata plus semantic repository versions.

## Two Tracks

- Module metadata may keep a date in `#!desc`.
- Repository governance and release notes use semantic versions in `CHANGELOG.md`.

## Version Milestones

- `v1.0 stable factory`: source-driven factory is stable.
- `v1.1 zhihu enhance`: Zhihu enhancement is added and validated.
- `v1.2 governance`: security, contribution, script review, and MITM policies are added.
- `v1.3 health reports`: repository health, coverage, impact, and workflow reports are added.
- `v1.4 mitm policy`: MITM growth control and future split policy are documented.

## Upgrade Rules

- `patch`: documentation, report, validation, or non-functional fixes.
- `minor`: new trusted rule source, light script addition, profile addition, or report generator.
- `major`: main module structure rewrite, large MITM change, or major script-system change.

## Release Checklist

Before a release:

1. Update `CHANGELOG.md`.
2. Build with `stable`.
3. Sync Root from Release.
4. Run repository validation and health check.
5. Confirm Root and Release diff lines are `0`.
6. Test Spotify, YouTube, Zhihu, login, payment, and verification flows when relevant.
