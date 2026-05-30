# Script Review Checklist

Use this checklist before moving any script from candidate or pending status into stable.

## Source

- Source is trusted and public.
- URL is HTTPS and preferably a raw GitHub URL.
- Repository owner and file path are clear.
- No short link, `ghproxy`, mirror, or unknown host is used.

## Code Safety

- No unknown obfuscated code.
- No Cookie or Token collection.
- No Authorization header harvesting.
- No membership, Premium, payment, login, account entitlement, or paid-content rewriting.
- No adult, gambling, or gray-market behavior.

## Request Scope

- `pattern` is narrow and App-specific.
- Login, payment, verification code, banking, WeChat, Alipay, and certificate-check APIs are not matched.
- `requires-body` is necessary.
- `max-size` is reasonable for the endpoint.
- Binary body mode is used only when required.

## MITM Scope

- Hostnames are minimized.
- No broad wildcard unless there is a documented reason.
- Bank, payment, login, verification, and account-security hosts are blocked from MITM expansion.

## Placement

- Spotify scripts go to `Scripts/spotify.conf`.
- YouTube scripts go to `Scripts/youtube.conf`.
- Zhihu scripts go to `Scripts/zhihu-enhance.conf` or related Zhihu review path.
- Ordinary App cleanup scripts go to `Scripts/app-clean.conf`.
- New scripts start as pending unless explicitly approved.

## Testing

- Confirm Root and Release diff lines are `0`.
- Run `validate_repository.py`.
- Run `repository_health_check.py`.
- Test affected App flows manually.
- Test Spotify, YouTube, Zhihu, login, payment, and verification flows if the script uses MITM or response-body rewriting.
- Document rollback steps.
