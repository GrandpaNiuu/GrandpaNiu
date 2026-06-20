# GrandpaNiu Project State

Last updated: 2026-06-20 11:58 +0800

## Project Purpose

GrandpaNiu is a rule construction and advertising cleanup repository for Shadowrocket / Surge style iOS modules, Android rule formats, and Windows v2rayN routing. Its main output is a Fusion `.sgmodule` plus derived Android, Windows, Web, and report artifacts.

The repository is high risk: rule or MITM mistakes can break app login, payment, banking, captcha, video playback, image loading, CDN access, or normal network connectivity.

## Current Main Functions

- Build one public iOS Fusion module.
- Maintain app-scoped rewrite/rule/script source fragments under `Rewrite/Sources/Apps/`.
- Maintain common protection and cleanup layers under `Rewrite/Sources/Misc/` and `Rules/`.
- Aggregate compatible scripts into `Scripts/generated/fusion-script-bundle.js`.
- Sync eligible upstream app modules through `Rewrite/Remotes/app-modules.json`.
- Generate Android outputs for Mihomo / sing-box / AdGuard / v2rayNG.
- Generate Windows v2rayN custom routing output.
- Generate Web catalog and GitHub Pages entry files.
- Generate governance reports for script aggregation, MITM scope, rule overlap, upstream risk, repository health, and workflow health.

## Public Entries

Primary public iOS entries:

- `Ronghemokuai.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Module.sgmodule`

Public Web and catalog entries:

- `import.html`
- `redirect.html`
- `android.html`
- `Web/index.html`
- `Web/catalog.md`
- `Web/release-links.json`

Android and Windows public outputs:

- `Release/Android/`
- `Android/mihomo/`
- `Android/sing-box/`
- `Android/adguard/`
- `Android/v2rayng/`
- `Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json`

## Version Strategy

The current strategy is Fusion single-module first. Do not reintroduce Stable / Lite / Full / Aggressive as public user-facing choices unless the owner explicitly changes the strategy.

Legacy profiles may remain for compatibility or history, but README, import pages, default workflows, health checks, and release reports should point to Fusion as the main public route.

## Important Directory Structure

- `Rules/`: source rule lists and converted remote lists.
- `Scripts/`: JavaScript scripts, script configs, and generated script bundle.
- `Rewrite/Generator/`: wrapper builder and generator config.
- `Rewrite/Sources/`: editable module source fragments.
- `Rewrite/Sources/Apps/`: app-scoped source fragments.
- `Rewrite/Sources/Misc/`: shared source layers for generic ads, CDN/direct protection, finance protection, video protection, analytics, and HTTPDNS.
- `Rewrite/Remotes/`: upstream source registry and app module sync registry.
- `Rewrite/Profiles/fusion.conf`: default build profile.
- `Android/`: editable Android rule source outputs and app branches.
- `Windows/v2rayN/`: v2rayN-specific routing output and docs.
- `Release/`: generated release outputs; do not edit directly unless proven non-generated.
- `Web/`: generated/static GitHub Pages catalog and entry docs.
- `reports/`: generated health, validation, and governance reports.
- `tools/`: governance and validation tools.
- `.github/workflows/`: automation for build, daily update, health, upstream sync, and issue reporting.

## Build Method

Preferred build command:

```bash
python Rewrite/Generator/Builder.py --profile fusion --release --check
```

Full quality gate:

```bash
python scripts/quality_gate.py
```

Useful targeted checks:

```bash
python scripts/validate_repository.py
python scripts/repository_health_check.py
python tools/validate_script_aggregation.py
python tools/test_script_bundle_sandbox.py
python tools/validate_upstream_risk_gate.py
python scripts/android_format_check.py
```

## Testing Method

Use local validation for syntax, generated output consistency, repository health, workflow text, Android format, script aggregation, and upstream risk gate. Real app end-to-end testing is currently performed manually by the owner and is not automated.

## Known Risks

- Broad MITM hostnames can affect login, payment, banking, captcha, image/CDN, and media playback.
- Aggressive reject rules can break domestic and overseas app connectivity.
- Upstream module auto-sync can import incompatible rewrites if the risk gate is weakened.
- Script aggregation can cause blank pages or hangs if `$done` handling regresses.
- Android formats cannot fully reproduce iOS Rewrite / MITM / Script behavior.
- Generated files under `Release/`, `Web/`, `reports/`, and `Scripts/generated/` can be overwritten by the builder.

## Recent Stable State

Initial snapshot baseline:

- Branch: `repair/upstream-app-sync`
- Remote `main` / local HEAD before this record initialization: `661b7205d696cccd518cbdcea97cbd4022bc550e`
- Recent CI observed green: Module Factory Build, Pages deployment, Workflow failure issue automation.
- Working tree before creating AI records: clean.
- Approximate scale: 297 app source files and 295 generated app module outputs.

## Next Recommendations

- Keep AI maintenance records updated on every change.
- Prefer source-first fixes instead of direct Release edits.
- Keep Fusion public entry stable.
- Continue using risk reports before narrowing or expanding MITM.
- Add automation only when it improves repeatability and does not bypass safety gates.
- Treat user-reported app breakage as evidence for targeted rollback or protection rules.
