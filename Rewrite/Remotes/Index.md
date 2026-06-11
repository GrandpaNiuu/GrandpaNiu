# Remote Sources Index

This directory stores trusted remote rule sources, disabled reference modules, and conservative upstream candidates.

## Files

- `sources.json`: active rule-set and reference-module registry.
- `candidates.json`: candidate source registry for conservative upstream collection.
- `Catalog.md`: generated human-readable catalog of active and reference sources.
- `Index.md`: this policy index.

## Active Sources

Active generated remote rules are registered in `sources.json`. Enabled entries are used by `scripts/build_module.py` to generate `RULE-SET` / `DOMAIN-SET` lines.

Current principles:

- Use HTTPS only.
- Use public and trusted upstream repositories.
- Keep each entry schema-complete: `name`, `type`, `url`, `policy`, `enabled`, `protected`, and `purpose`.
- Do not register short links, proxy URLs, mirror hosts, unknown sources, unlock sources, or payment/login bypass sources.
- Keep Spotify, YouTube, install, import, and module update references protected.

## Reference Modules

Reference modules are not public import entries. They are disabled by default and used only for manual source-first comparison before selected fragments are moved into `Rewrite/Sources/Apps/` or `Rewrite/Sources/Misc/`.

## Candidate Sources

Candidate sources are registered in `candidates.json`. The weekly collector reads only that file and never searches the web.

Candidate rules:

- Default state is disabled or pending.
- Scripts are not auto-added unless explicitly approved and trusted.
- Candidates must pass reachability, format, risk-keyword, trusted-repository, and duplicate checks.
- Spotify and YouTube core references are report-only and are not auto-replaced.

Generated catalogs:

- `Rewrite/Remotes/Catalog.md`
- `Web/remotes.md`

Collector report: `reports/upstream_collect_report.md`.
