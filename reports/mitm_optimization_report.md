# MITM Optimization Report

- Scope: final Fusion `[MITM]` compile output only.
- Guarantee: default mode normalizes and de-duplicates exact hostname tokens without changing the normalized hostname set.
- Boundary: Script, URL Rewrite, Header Rewrite, Body Rewrite, Map Local and Rule sections are not rewritten by this stage.
- Reduction policy: wildcard range reduction is disabled unless matcher evidence and static dependency proof are both present.

## Summary

- generated_at: `2026-07-11T02:13:39.957278+08:00`
- mode: `normalize`
- baseline hostname tokens: `2059`
- baseline unique hostname tokens: `1234`
- normalized hostname tokens: `1234`
- same normalized hostname set: `True`
- wildcard count before: `34`
- wildcard count after: `34`
- strict duplicate tokens removed: `825`
- proved wildcard reductions: `0`
- opaque retained count: `169`
- reductions disabled by missing matcher proof: `34`
- fallback: `False`
- fallback reason: `none`

## Coverage Validation

- passed: `True`
- deep features: `1559`
- resolvable features: `1390`
- opaque features: `169`
- baseline uncovered features: `45`
- reasons: `none`

## Source Trace

- Full per-host source trace and per-feature fingerprints are written to `reports/mitm_optimization_report.json`.
- This report does not claim every client behavior is globally proven; it only states the static MITM coverage contract for parsed rules and verified matcher semantics.
- Any hostname or dependency that cannot be proven safe is kept in the output.
