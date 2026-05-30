# Contribution and Maintenance Rules

This repository is source-driven. Do not maintain `Ronghemokuai.sgmodule` by hand as the only source of truth.

Human maintainers and automated assistants must follow the same source-first rules below.

## Where Changes Go

- New trusted remote rules go to `Rewrite/Remotes/candidates.json` first.
- Stable remote rules are registered in `Rewrite/Remotes/sources.json` only after validation.
- Local rules go to `Rules/*.list`.
- Rewrite, body rewrite, map local, and MITM fragments go to `Rewrite/Sources/*.conf`.
- New scripts must stay pending until reviewed.

## Script Rules

- Scripts must not directly enter stable without review.
- Do not add unknown obfuscated scripts.
- Do not add scripts that modify membership, payment, login, account entitlement, Cookie, Token, paid content, or verification flows.
- Choose the smallest script target: `app-clean`, `spotify`, `youtube`, or `zhihu`.

## Forbidden Content

Do not add:

- Membership or Premium unlocks.
- Payment bypass.
- Login bypass.
- Account entitlement spoofing.
- Cookie, Token, or BoxJS account tasks.
- Adult, gambling, or gray-market content.
- Short links, `ghproxy`, mirrors, or unverifiable script sources.

## Required Commands

Run these after changes:

```text
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

For governance or reporting changes, also run the relevant report generator.

## Required Change Notes

Every change should explain:

- Which source files changed.
- Which App or service may be affected.
- Whether scripts, MITM, Body Rewrite, or remote sources changed.
- What report was updated.
- How to roll back.

## Rollback

Prefer reverting the commit. If the module output is broken, use:

- `backup/Ronghemokuai.stable.sgmodule`
- `backup/Ronghemokuai.before-factory-refactor.sgmodule`

Then rebuild, sync, validate, and regenerate health reports.
