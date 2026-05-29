# Zhihu Enhanced Cleaning Report

Date: 2026-05-30

## Purpose

Add a conservative Zhihu enhanced ad-cleaning layer for native advertisement cards, promoted feed cards, recommendation ads, sponsored cards and commercial fields.

## Added files

```text
Scripts/zhihu-enhance.js
Scripts/zhihu-enhance.conf
```

## Updated files

```text
Rewrite/Profiles/stable.conf
```

## Build integration

`Rewrite/Profiles/stable.conf` now includes:

```text
zhihu_enhance = Scripts/zhihu-enhance.conf
```

The next module factory build will include `zhihu-enhance` in the generated `[Script]` section.

## Scope

The cleaner targets only advertisement-related keys and card markers such as:

```text
ad
ads
ad_info
advertisement
commercial
promotion
sponsor
sponsored
brand_ad
banner_ad
feed_ad
native_ad
推荐的广告
商业推广
品牌推广
```

## Safety boundary

The script is designed not to modify these categories:

```text
membership
premium
payment
wallet
account
login
auth
token
cookie
paid content
```

It does not unlock paid content, does not modify account identity, does not alter login, and does not bypass payment.

## Testing checklist

After running `Module Factory Build`, test in Shadowrocket:

1. Update module.
2. Update scripts.
3. Ensure HTTPS decryption is enabled and certificate is trusted.
4. Kill and reopen Zhihu.
5. Open article / answer pages where feed ads previously appeared.
6. Confirm normal login, comments, likes, follows and paid content visibility are not broken.

## Rollback

If Zhihu shows blank feed, loading errors, or account-related abnormal behavior, remove this line from `Rewrite/Profiles/stable.conf` and rebuild:

```text
zhihu_enhance = Scripts/zhihu-enhance.conf
```
