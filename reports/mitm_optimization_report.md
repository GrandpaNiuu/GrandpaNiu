# MITM Optimization Report

- Scope: final Fusion `[MITM]` compile output only.
- Guarantee: exact duplicates are removed, and exact tokens may be compacted only when an existing canonical wildcard preserves the same matcher coverage.
- Boundary: Script, URL Rewrite, Header Rewrite, Body Rewrite, Map Local and Rule sections are not rewritten by this stage.
- Reduction policy: no wildcard is created or removed; wildcard range reduction remains disabled.

## Summary

- generated_at: `2026-07-29T02:20:39.225108+08:00`
- mode: `equivalent`
- baseline hostname tokens: `2059`
- baseline unique hostname tokens: `1234`
- normalized hostname tokens: `1189`
- same normalized hostname set: `False`
- same MITM coverage under matcher contract: `True`
- matcher contract: `shadowrocket-mitm-suffix-wildcard-v1`
- non-MITM semantic fingerprint: `2fcb294f7fcc22db2dc5cf22863a61b9b08562873564692d769009ae9ec22432`
- non-MITM fingerprint lines: `2753`
- wildcard count before: `34`
- wildcard count after: `34`
- strict duplicate tokens removed: `825`
- proved wildcard reductions: `0`
- attempted wildcard reductions: `0`
- semantically redundant exact tokens removed: `45`
- attempted semantically redundant removals: `45`
- opaque retained count: `169`
- reductions disabled by missing matcher proof: `0`
- wildcard range reductions kept disabled: `34`
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

- Full per-host source trace and compiled-section feature fingerprints are written to `reports/mitm_optimization_report.json`.
- Equivalent compaction evidence records both the exact-token source and the covering-wildcard source in the JSON report.
- This report does not claim every client behavior is globally proven; it states equivalence under the named repository matcher contract.
- Any hostname or dependency that cannot be proven safe is kept in the output.
