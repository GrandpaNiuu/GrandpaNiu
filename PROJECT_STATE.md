# GrandpaNiu Project State

Last updated: 2026-07-03 02:35 +08:00

## 2026-07-03 GitHub Pages Deploy Queue Repair Snapshot

- Observed failure: GitHub Pages deploy job stayed at `deployment_queued` until `actions/deploy-pages` reached its 10 minute timeout and cancelled the deployment.
- Repository code previously had no explicit `.github/workflows/pages-deploy.yml`; Pages deployment was left to GitHub's default branch-based Pages deployment flow.
- Added a self-managed `Deploy GitHub Pages` workflow:
  - packages only the public static site artifact under `_site`
  - publishes Fusion, Release, Web, Android, Windows, Rules, Scripts, Rewrite/Remotes, docs, and reports
  - uses `.nojekyll`
  - uses `actions/deploy-pages`
  - sets the Pages deploy timeout explicitly to GitHub's supported maximum of `600000` ms
  - uses `pages-deploy-main` concurrency with `cancel-in-progress: true` so stale queued deploys do not block the latest one
- Added validation guards so future checks require the Pages workflow, artifact upload, Pages permissions, and extended deploy timeout.
- Important operational note: GitHub repository Pages settings should use **Source: GitHub Actions**. If Settings -> Pages still uses branch deployment, GitHub can continue launching the old default Pages deployment workflow.
- Validation passed:
  - workflow YAML parse
  - `python scripts/validate_repository.py`
  - `python scripts/repository_health_check.py`
  - `python tools/generate_automation_gap_report.py`
  - `python scripts/quality_gate.py`

## Project Purpose

GrandpaNiu is a source-first rule and module factory for advertising cleanup and routing outputs.

It publishes:

- iOS Shadowrocket / Surge compatible Fusion module output.
- Android rule outputs for Mihomo / Clash Meta, sing-box, AdGuard, and v2rayNG.
- Windows v2rayN custom routing output.
- Per-App release modules.
- Web catalog and GitHub Pages entry files.
- Governance, freshness, risk, coverage, and automation reports.

Treat this repository as high risk. Small rule, rewrite, MITM, script, Android, Windows, or workflow changes can affect login, payment, captcha, video playback, images/CDN, or normal app networking.

## Current Public Entries

Primary iOS public entries:

- `Ronghemokuai.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Module.sgmodule`

Android and Windows outputs remain generated projections:

- `Android/`
- `Release/Android/`
- `Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json`

## Version Strategy

- iOS uses one public Fusion module.
- Stable / Stable Plus / Lite / Full are deprecated legacy references only.
- Do not reintroduce multi-version public routes without explicit owner approval.
- Generated channel aliases under `Release/Stable`, `Release/Beta`, and `Release/Canary` are managed by the Builder and are not a return to old user-facing multi-version selection.

## Editable Source Layers

Prefer source-first edits under:

- `Rules/`
- `Scripts/`
- `Rewrite/Sources/`
- `Rewrite/Remotes/`
- `Rewrite/Profiles/fusion.conf`
- `Android/`
- `Windows/v2rayN/`
- `tools/`
- `.github/workflows/`

Do not directly hand-edit generated outputs unless the source or generator path is understood.

## Generated Layers

Generated or mostly generated outputs include:

- `Ronghemokuai.sgmodule`
- `Release/`
- `Web/`
- `reports/`
- `Scripts/generated/`

Use the Builder or quality gate to refresh these.

## Build Commands

Preferred full release build:

```bash
python Rewrite/Generator/Builder.py --profile fusion --release
```

Preferred full release build plus configured checks:

```bash
python Rewrite/Generator/Builder.py --profile fusion --release --check
```

Full quality gate:

```bash
python scripts/quality_gate.py
```

Important focused checks:

```bash
python scripts/validate_module_integrity.py
python scripts/validate_app_sources.py
python scripts/validate_repository.py
python scripts/repository_health_check.py
python scripts/check_report_freshness.py --strict
```

## Current Stable State

As of 2026-07-03:

- Branch: `repair/upstream-app-sync`, tracking `origin/main`.
- Latest synchronized commit before this pass: `b2606a4f Build module factory outputs [skip ci]`.
- Main iOS Fusion module: `2775` lines.
- App source files: `398`.
- Release App modules: `398`.
- Empty App modules: `0`.
- Aggregated script routes: `52`.
- Main Fusion final routing tail:
  - `GEOIP,CN,DIRECT`
  - `FINAL,PROXY`
- Main iOS public entries are synchronized by the Builder:
  - `Ronghemokuai.sgmodule`
  - `Release/Ronghemokuai.sgmodule`
  - `Release/Module.sgmodule`

## Recent Validation

The 2026-07-03 full local health refresh passed:

```bash
python -c "import compileall, sys; ok=True; ok &= compileall.compile_dir('scripts', quiet=1); ok &= compileall.compile_dir('tools', quiet=1); ok &= compileall.compile_file('Rewrite/Generator/Builder.py', quiet=1); sys.exit(0 if ok else 1)"
node --check Scripts/app-cleaner.js
node --check Scripts/generated/fusion-script-bundle.js
python -m unittest discover -s tests
python tools/validate_script_aggregation.py
python tools/test_script_bundle_sandbox.py
python scripts/validate_module_integrity.py
python scripts/validate_app_sources.py
python Rewrite/Generator/Builder.py --profile fusion --release --check
python scripts/validate_repository.py
python scripts/repository_health_check.py
python scripts/validate_profiles.py
python scripts/validate_remote_rule_syntax.py
python scripts/validate_governance_extensions.py
python scripts/quality_gate.py
```

`python scripts/check_report_freshness.py --strict` failed immediately after a standalone Builder run because `app_status_matrix` and `automation_gap` had not yet been refreshed in quality-gate order. The full `python scripts/quality_gate.py` run refreshed them and passed strict freshness.

Local GitHub API access failed during:

```bash
gh run list --limit 12
```

The failure was a timeout to `198.18.0.26:443`, so remote Actions status could not be confirmed from this machine during the pass.

## Recent Important Changes

### 2026-07-02 Fusion Rewrite Compaction

- Main iOS Fusion module was compacted from `5953` lines to `2775` lines.
- `Rewrite/Profiles/fusion.conf` enables `compact_rewrite_sections = true`.
- `scripts/build_module.py` performs conservative equivalent compaction:
  - URL Rewrite: only pure `- reject*` lines with identical action suffix.
  - Body Rewrite: only identical verb and body operation.
  - Map Local: only identical response operation.
- `scripts/validate_module_integrity.py` compiles generated rewrite regexes.
- `tests/test_module_compaction.py` protects URL Rewrite suffix and grouping behavior.

### 2026-07-02 Compact China / Overseas Network Split

- Main iOS Fusion keeps ad-blocking rules first and appends:
  - `GEOIP,CN,DIRECT`
  - `FINAL,PROXY`
- `strip_direct_proxy_rules = true` strips old scattered route/protection rules from the generated main module.
- `compact_network_split = true` appends the centralized split.
- Validation requires those two routing rules to be the final two active `[Rule]` entries.

### 2026-07-02 Automation Gap Guard

- `tools/generate_automation_gap_report.py` is a blocking automation coverage check.
- It verifies Fusion entry parity, App source/module counts, Android source/release parity, Windows v2rayN tail rules, scheduled workflow wiring, explicit staging, quality gate wiring, and script aggregation cache presence.
- It is wired into Builder `--check`, full quality gate, freshness checks, repository validation, repository health, and automated evidence.

## Known Risks

- Python regex validation is not a perfect Shadowrocket runtime simulation.
- Long combined OR regexes can behave differently on older clients, although chunking limits generated regex line length.
- `GEOIP,CN,DIRECT` is IP-geography based, not a perfect Chinese-App classifier.
- `FINAL,PROXY` requires the user's Shadowrocket configuration to have a usable `PROXY` policy or group.
- Real App end-to-end behavior is owner-tested manually; CI proves syntax, generation, and governance only.

## Protected Areas

Do not change these without concrete evidence and a risk note:

- Login and account APIs.
- Payment, order, and banking flows.
- Captcha and verification flows.
- Video playback domains and scripts.
- Image and static CDN domains.
- Authorization, Cookie, Token, or receipt logic.
- Broad MITM hostname scopes.
- Public module entry names or URLs.

## Next Recommendations

- Keep using `python scripts/quality_gate.py` as the final local gate for generated-output refreshes.
- If a real App breaks, fix the smallest source layer first and run the full quality gate.
- Keep watching scheduled workflow freshness from GitHub Actions when network access to GitHub API is available.
- Do not add more App modules or remote sources unless they are compatible with the upstream risk gate and do not include unlock, payment bypass, login bypass, or credential/token logic.
