# 今日头条 / Toutiao crash safe-mode report

## Summary

This change stabilizes Toutiao-related usage by adding a dedicated safe-mode module instead of deleting the module family. The safe-mode module keeps stability as the first priority and only retains exact ad/log domain rejects.

## Files found during repository search

Search terms used: `toutiao`, `今日头条`, `snssdk`, `bytedance`, `news_article`, `pangolin`, `pglstatp`, `byteimg`, `ttwebview`.

Relevant files found:

- `Rewrite/Sources/URL-Rewrite.conf`
- `Rewrite/Sources/Apps/seven-cat.conf`
- `Rewrite/Sources/Apps/tube-max.conf`
- `Release/Modules/seven-cat.sgmodule`
- `Release/Modules/tube-max.sgmodule`
- `Rules/aggressive-ads.list`
- `Ronghemokuai.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Module.sgmodule`
- `Release/Stable/Module.sgmodule`
- Android generated rule outputs under `Android/` and `Release/Android/`
- Converted rule outputs under `Rules/converted/`

No existing dedicated `toutiao.conf` or `Release/Modules/toutiao.sgmodule` was found before this safe-mode addition.

## Crash-risk rules identified

The highest-risk active patterns are in global URL rewrite / generated fusion artifacts, especially rules matching ByteDance/Toutiao infrastructure through MITM-style URL rewrite behavior:

- `pglstatp-toutiao.com` broad URL rewrite rejects, including whole-host style matches.
- `byteimg.com` URL rewrite rejects, because ByteDance image/CDN hosts can carry non-ad content required by feeds, article pages, startup UI, and embedded cards.
- `snssdk.com` URL rewrite rejects, even when the path contains `/api/ad/`, because broad matching around `snssdk` can be risky when API routing or response formats change.
- `pangolin-sdk-toutiao.com` SDK ad API rewrites are lower risk than core API rewrites but still should stay exact and domain-scoped.
- Any Body Rewrite / JQ / JS touching Toutiao startup, account, device, security, feed, article, or passport endpoints would be high risk. No dedicated Toutiao JQ/JS file was found in this pass.

## Files modified

- Added `Rewrite/Sources/Apps/toutiao.conf`
- Added `Release/Modules/toutiao.sgmodule`
- Added this report: `reports/toutiao-crash-fix.md`

## Rules disabled or intentionally omitted in safe mode

The new Toutiao safe-mode module intentionally omits these sections completely:

- `[URL Rewrite]`
- `[Body Rewrite]`
- `http-response-jq`
- JS rewrite/script handlers
- `[MITM]`

This means the safe module does not decrypt or modify Toutiao traffic and does not touch launch, config, settings, passport, security, device, feed, article, account, payment, membership, identity, or permission-related responses.

## Advertising / telemetry rules kept in safe mode

Only exact domains were retained:

- `pangolin.snssdk.com`
- `pangolin-sdk-toutiao.com`
- `pglstatp-toutiao.com`
- `ads.toutiao.com`
- `ad.byted.org`
- `log.snssdk.com`
- `mon.snssdk.com`

No broad `DOMAIN-SUFFIX` rule was added for:

- `snssdk.com`
- `toutiao.com`
- `bytedance.com`
- `byteimg.com`
- `pglstatp-toutiao.com`

## What was not changed

Generated fusion artifacts and large global rule files still contain historical third-party matches for ByteDance/Toutiao-related infrastructure. They were not mass-deleted in this pass because the requested stability target is better served first by a dedicated safe module and because large generated artifacts should be rebuilt through the repository generator to avoid source/release drift.

Recommended follow-up is to run the generator and, if necessary, move unsafe global URL rewrite lines into a rejected/archived source bucket so regenerated fusion artifacts no longer include them.

## Validation / build command

Preferred repository command from `Rewrite/Generator/README.md`:

```bash
python Rewrite/Generator/Builder.py --profile fusion --release --check
```

I could not run the full repository build inside the current execution environment because direct `git clone`/GitHub network access from the container failed with DNS resolution for `github.com`. The GitHub connector was used for repository reads/writes instead.

After pulling locally, run:

```bash
git pull
python Rewrite/Generator/Builder.py --profile fusion --release --check
```

Then verify:

```bash
grep -RniE "toutiao|snssdk|bytedance|news_article|pangolin|pglstatp|byteimg|ttwebview" Rewrite/Sources Release/Modules Rules Scripts Release
```

## If Toutiao still crashes

1. Disable the fusion module and enable only `Release/Modules/toutiao.sgmodule`.
2. Confirm there is no MITM hostname for `*.snssdk.com`, `*.toutiao.com`, `*.bytedance.com`, `*.byteimg.com`, `api*.snssdk.com`, `passport.snssdk.com`, or `security.snssdk.com`.
3. Re-enable one retained exact ad/log domain at a time.
4. If crash happens only under the fusion module, remove or comment the global URL Rewrite rules for `pglstatp-toutiao`, `byteimg`, and `snssdk` from `Rewrite/Sources/URL-Rewrite.conf`, then rebuild.
5. Check whether the response is JSON before using JQ; never apply JQ to protobuf, gzip, binary, or non-standard JSON responses.

## Rollback

Rollback the safe-mode addition with:

```bash
git revert <commit-that-added-Rewrite/Sources/Apps/toutiao.conf>
git revert <commit-that-added-Release/Modules/toutiao.sgmodule>
git revert <commit-that-added-this-report>
```

Or remove these files manually and commit:

```bash
git rm Rewrite/Sources/Apps/toutiao.conf Release/Modules/toutiao.sgmodule reports/toutiao-crash-fix.md
git commit -m "revert: remove toutiao safe mode"
```
