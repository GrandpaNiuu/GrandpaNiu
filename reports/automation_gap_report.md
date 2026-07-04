# Automation Gap Report

- Generated at: 2026-07-04 13:16:20 +0800
- Blocking gaps: 0

## Blocking Gaps

- none

## Covered Automation Areas

- Fusion public entries are byte-identical.
- App source files: 398; Release app modules: 398.
- Android branches checked: 4; Windows v2rayN output checked.
- Scheduled workflows checked: 7; writer workflows checked: 9.
- Pages deployment workflow checked for self-managed artifact deploy, maximum supported deployment timeout, serialized final deployment, and reduced trigger noise.
- Quality gate command tokens checked: 14.
- Required reports checked: 19; script aggregation cache checked.

## Intentional Non-CI Boundaries

- Real App end-to-end behavior is not a CI gate; it remains owner/device verified.
- Ad impression disappearance is not a CI gate; static checks prove syntax, wiring, and source traceability only.
- Upstream replacement scoring is intentionally not implemented in this pass.
- App feedback ingestion is intentionally not implemented in this pass.
- Android and Windows outputs are routing projections; iOS Script, MITM, Body Rewrite, and Map Local behavior cannot be fully projected.
