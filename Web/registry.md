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
| `Scripts/generated/fusion-script-bundle.js` | low-risk response cleanup script entries | `scripts/build_module.py` |
| `Scripts/generated/fusion-script-bundle.manifest.json` | script aggregation route/source manifest | `scripts/build_module.py` |
| `reports/script_bundle_sandbox_report.md` | generated script bundle runtime sandbox evidence | `tools/test_script_bundle_sandbox.py` |
| `reports/upstream_risk_gate_report.md` | direct-commit upstream app risk boundary | `tools/validate_upstream_risk_gate.py` |
| `reports/mitm_scope_report.md` | generated MITM hostname category report | `tools/generate_mitm_scope_report.py` |
| `reports/upstream_provenance_report.md` | upstream trust tier, source URL, license visibility, and sync mode ledger | `tools/generate_upstream_provenance_report.py` |
| `reports/platform_compatibility_matrix.md` | iOS / Android / Windows capability boundary matrix | `tools/generate_platform_compatibility_matrix.py` |
| `reports/protected_traffic_ledger.md` | login, payment, banking, playback, CDN, and HTTPDNS protection ledger | `tools/generate_protected_traffic_ledger.py` |
| `reports/false_positive_review_report.md` | false-positive review queue built from risk ledgers | `tools/generate_false_positive_review_report.py` |
| `reports/rule_overlap_report.md` | source rule overlap traceability | `tools/generate_rule_overlap_report.py` |
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
- App-scoped upstream sync is controlled by `Rewrite/Remotes/app-modules.json`; recent GitHub `.snippet` sources from `fmz200/wool_scripts` are converted before release builds.
- Current public App Modules count is 398. The latest foreign expansion added AOL, Go.com, Lycos, MacKeeper, New Relic, Openmultimedia, Outlook, Sape, and Yahoo from `fmz200/wool_scripts`.
- Broad platform candidates such as Adobe activation/licensing, Apple / Google Safe Browsing, Microsoft CRL, and Amazon AWS core service rules are intentionally not published as direct-sync app modules without targeted risk review.
- Protected login/message/CDN entries such as `apd-pcdnwxlogin`, `msync-im`, and `ossgw.alicdn.com` are filtered during upstream conversion instead of being published as REJECT or forced MITM lines.
- `Scripts/generated/fusion-script-bundle.js` and `Scripts/generated/fusion-script-bundle.manifest.json` are generated, not hand-maintained; they reduce visible script URLs while preserving core scripts as independent entries.
- Upstream direct-commit sync, generated script bundles, MITM scope and source rule overlap are checked by generated governance reports before release.
- Upstream provenance, platform compatibility, protected traffic, and false-positive review reports are generated governance evidence; they do not modify rules.
- Edit `Rewrite/Sources/Misc/` for shared protection and generic low-risk cleanup.
- Edit `Rewrite/Remotes/sources.json` only for low-risk remote rule sets.
- Treat `Release/` and most `Web/` catalog files as generated outputs.
