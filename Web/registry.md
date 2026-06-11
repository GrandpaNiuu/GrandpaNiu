# Module Factory Registry

This page mirrors the master source index from `Rewrite/Registry.md` for Web-side navigation.

## Public production path

```text
Rewrite/Sources/
Rewrite/Sources/Apps/
Rewrite/Remotes/
Rules/
Scripts/
Android/
        ↓
Rewrite/Generate.conf
        ↓
Rewrite/Generator/Builder.py
        ↓
Release/
        ↓
Web/
```

## Key public outputs

| Output | Source | Builder |
|---|---|---|
| `Ronghemokuai.sgmodule` | `Release/Ronghemokuai.sgmodule` | `scripts/factory_finalize.py` |
| `Release/Ronghemokuai.sgmodule` | `Rewrite/Sources/`, `Rules/`, `Scripts/` | `scripts/build_module.py` |
| `Release/Rules.conf` | `Release/Ronghemokuai.sgmodule` | `scripts/build_release_rules.py` |
| `Release/RulesGroup.conf` | `Release/Ronghemokuai.sgmodule` | `scripts/build_release_rules.py` |
| `Release/Modules/` | `Rewrite/Sources/Apps/` | `scripts/build_release_modules.py` |
| `Release/Android/` | `Android/` | `scripts/build_release_android.py` |
| `Web/catalog.md` | `Release/Modules/README.md` | `scripts/build_web_catalog.py` |
| `Web/remotes.md` | `Rewrite/Remotes/sources.json` | `scripts/build_web_catalog.py` |

## Source of truth

The full registry is maintained in `Rewrite/Registry.md`.
