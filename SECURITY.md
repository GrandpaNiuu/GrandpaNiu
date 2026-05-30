# Security Policy

GrandpaNiu is a personal Shadowrocket / Surge cleanup module factory. Security fixes must be source-first: update `Rules/`, `Scripts/`, `Rewrite/Sources/`, `Rewrite/Remotes/`, or `Rewrite/Profiles/`, then rebuild and sync the generated module.

## Security Boundary

Allowed scope:

- Ad blocking and cleanup.
- Splash, popup, banner, feed, recommendation, and activity-card cleanup.
- Spotify playback protection.
- YouTube Enhance preservation.
- Zhihu cleanup and enhancement without account or entitlement changes.
- Trusted remote rule maintenance.
- Reversible build, report, and rollback workflows.

Forbidden scope:

- Membership or Premium unlocks.
- Payment bypass.
- Login bypass.
- Account entitlement spoofing.
- Certificate bypass.
- Cookie, Token, or BoxJS account tasks.
- Adult, gambling, or gray-market content.
- Short-link scripts.
- Unknown obfuscated scripts.
- `ghproxy`, mirror sites, or unverified third-party script sources.

## Reporting High-Risk Rule Sources

Open an issue or maintenance note with:

- Source URL.
- Repository owner and file path.
- Why it is risky.
- Whether it touches login, payment, verification, banking, WeChat, Alipay, Spotify, YouTube, or Zhihu.
- Suggested rollback or disable action.

Do not replace a source with `ghproxy`, mirrors, short links, or unrelated third-party files.

## Login, Payment, and Verification False Positives

If login, payment, verification code, banking, WeChat, or Alipay breaks:

1. Disable the module to confirm whether the module is involved.
2. Check recent changes to `Scripts/`, `Rewrite/Sources/MITM.conf`, `Body-Rewrite.conf`, `URL-Rewrite.conf`, and `Map-Local.conf`.
3. Prefer narrow allowlist or rollback over broad deletion.
4. Rebuild through the factory and run validation.

## Suspected Malicious Scripts

Treat a script as high risk if it:

- Reads or writes Cookie, Token, Authorization, account, payment, membership, or entitlement fields.
- Is obfuscated or minified without a trusted upstream reason.
- Uses broad patterns that match login, payment, verification, banking, WeChat, or Alipay APIs.
- Comes from an unknown source.

New scripts must stay pending until reviewed.

## External Link Failures

External links are handled by reports and history first. Do not delete or replace a source because of a single failed check. Protected Spotify, YouTube, Zhihu, install, import, and update links require manual confirmation.

## Core App Exceptions

For Spotify, YouTube, and Zhihu issues:

- Keep `spotify-json`, `spotify-proto`, `youtube.response`, and `zhihu-enhance`.
- Check DIRECT rules and MITM hostnames before deleting scripts.
- Prefer source-first rollback or narrow rules.

Security reports and fixes should always end with:

```text
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```
