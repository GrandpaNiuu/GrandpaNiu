# Module Factory Registry

This page mirrors the source-first factory model from `Rewrite/Registry.md` for public Web navigation.

## Public production path

```text
Rewrite/Sources/
Rewrite/Sources/Apps/
Rewrite/Sources/Misc/
Rewrite/Remotes/
Rules/
Scripts/
Android/
Windows/
  -> Rewrite/Generate.conf
  -> Rewrite/Generator/Builder.py
  -> Release/
  -> Web/
```

## Key public outputs

| Output | Source | Builder |
|---|---|---|
| `Ronghemokuai.sgmodule` | `Release/Ronghemokuai.sgmodule` | `scripts/factory_finalize.py` |
| `Release/Ronghemokuai.sgmodule` | `Rewrite/Sources/`, `Rules/`, `Scripts/`, `Rewrite/Sources/Misc/` | `scripts/build_module.py` |
| `Release/Rules.conf` | `Release/Ronghemokuai.sgmodule` | `scripts/build_release_rules.py` |
| `Release/RulesGroup.conf` | `Release/Ronghemokuai.sgmodule` | `scripts/build_release_rules.py` |
| `Release/Modules/` | `Rewrite/Sources/Apps/` plus auto-discovery | `scripts/build_release_modules.py` |
| `Release/Android/` | `Android/` | `scripts/build_release_android.py` |
| `Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json` | `Android/v2rayng/GrandpaNiu-v2rayng-routing.json` | `scripts/build_windows_v2rayn.py` |
| `Web/catalog.md` | `Release/Modules/README.md` | `scripts/build_web_catalog.py` |
| `Web/release-links.json` | `Release/Modules/README.md` | `scripts/build_web_catalog.py` |
| `Web/remotes.md` | `Rewrite/Remotes/sources.json` | `scripts/build_web_catalog.py` |

## Source of truth

- Edit `Rewrite/Sources/Apps/` for app-scoped module rules.
- Edit `Rewrite/Sources/Misc/` for shared protection and generic low-risk cleanup.
- Edit `Rewrite/Remotes/sources.json` only for low-risk remote rule sets.
- Treat `Release/` and most `Web/` catalog files as generated outputs.
