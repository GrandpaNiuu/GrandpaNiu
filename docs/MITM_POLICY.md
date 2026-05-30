# MITM Policy

The current MITM hostname list is already large. Growth must be controlled and documented.

## Hostname Levels

### core

Core hostnames support protected high-value features:

- Spotify playback protection.
- YouTube Enhance.
- Zhihu cleanup and enhancement.

Core entries must be preserved and tested after changes.

### app-clean

App-clean hostnames support common App cleanup for feeds, banners, popups, splash screens, and activity cards.

These entries require App-specific reasons and manual testing.

### extended

Extended hostnames are low-frequency App or high-risk testing entries.

They should not be added to stable without a clear test plan.

### blocked

Do not add MITM for:

- Banking.
- Payment.
- Verification code.
- Login.
- Certificate pinning or certificate validation.
- Account security.
- WeChat Pay, Alipay, and similar sensitive flows.

## Rules

- Do not append broad `*` wildcards without a documented reason.
- Prefer exact hostnames over suffix wildcards.
- If login or payment breaks, check MITM first.
- If a hostname is only needed for a test, keep it out of stable or document it as extended.
- Every new MITM hostname should include source context and affected App.

## Future Split Plan

The repository may later split MITM into:

```text
Rewrite/Sources/MITM-core.conf
Rewrite/Sources/MITM-app-clean.conf
Rewrite/Sources/MITM-extended.conf
```

This document only defines policy for now. It does not split existing files.
