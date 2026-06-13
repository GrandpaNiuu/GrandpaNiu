# Rewrite Sources / Misc

This directory stores shared, non-app-specific source fragments for the fusion module.

`scripts/build_module.py` scans `Rewrite/Sources/Misc/*.conf` during the main fusion build. Protection files are merged before normal blocking rules so payment, login, image CDN, and video playback paths stay reachable.

## Active misc source files

| File | Purpose | Default behavior |
|---|---|---|
| `generic-ads.conf` | Common advertising domains and keywords | REJECT |
| `android-compatible-ads.conf` | Low-risk Android branch ad/tracking gaps merged back into Fusion | REJECT |
| `httpdns.conf` | HTTPDNS safety layer | DIRECT |
| `analytics.conf` | Low-risk ad analytics and crash-reporting endpoints | REJECT |
| `cdn-direct.conf` | Image, video, and static CDN protection | DIRECT |
| `finance-protect.conf` | Banking, payment, login, and order-flow protection | DIRECT |
| `video-protect.conf` | Video and music playback protection | DIRECT |

## Maintenance policy

- Keep broad protection as DIRECT, not REJECT.
- Do not place app-specific ads here if they clearly belong in `Rewrite/Sources/Apps/`.
- Do not block payment, bank, login, captcha, video playback, or image CDN paths.
- Raw upstream modules belong in `Rewrite/Remotes/` first; only reviewed fragments should enter this directory.
