# Profile Validation Report

Generated: 2026-07-13 02:12:48 +0800

This script validates the single public Fusion profile only.

| Profile | Build | Required markers | Scripts | MITM | Usage | Publishable |
|---|---|---|---:|---:|---|---|
| fusion | yes | passed | 45 | 1234 | single Fusion release | yes |

## Rules

- fusion is the only public build profile.
- Default workflows must build with fusion.
- Legacy stable/stable-plus/lite/full files are not public entry points.
- Required markers confirm module structure and core script entries.
