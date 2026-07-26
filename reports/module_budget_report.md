# Fusion Module Complexity Budget

- Generated at: `2026-07-26T18:37:51.735357Z`
- Status: `passed`
- Scope: generated Fusion complexity only; this validator does not rewrite module content.
- Module bytes: `2908098` / `3500000`
- Module lines: `2769` / `3300`
- Active lines: `2761`
- MITM tokens: `1189` / `1500`
- MITM wildcards: `34` / `60`

## Section Budgets

| Section | Active | Budget |
|---|---:|---:|
| `Rule` | 1194 | 1500 |
| `URL Rewrite` | 40 | 80 |
| `Header Rewrite` | 2 | 20 |
| `Body Rewrite` | 1435 | 1800 |
| `Map Local` | 37 | 80 |
| `Script` | 45 | 70 |
| `MITM` | 1 | 2 |

## Longest Active Lines

| Line | Section | Characters | Exception | SHA-256 | Prefix |
|---:|---|---:|---|---|---|
| 2688 | `Map Local` | 2269910 | `xiaojukeji-charge-map-local` | `1130e43c8c29` | `(?:^https://am\.didistatic\.com/static/am/cf-terminal/epower/epower-thanos-app/\d+\.\d+\.\d+/pages/people/index\.js$) da` |
| 2162 | `Body Rewrite` | 29975 | `-` | `150840c15f2a` | `http-response-jq (?:^https?:\/\/open-cms-api\.quark\.cn\/open-cms\?) 'delpaths([["result","cms_homepage_push_banner_conf` |
| 2705 | `Map Local` | 26300 | `-` | `47c6f638ca9a` | `(?:^https://ucmp(-static)?\.sf-express\.com/proxy/ccspBase/module-config/(login/)?query\?) data-type=json data="{\"versi` |
| 2769 | `MITM` | 22433 | `-` | `d37fca19d96f` | `hostname = %APPEND% spclient.wg.spotify.com,*.spclient.spotify.com,youtubei.googleapis.com,acs.m.goofish.com,acs.m.taoba` |
| 1233 | `URL Rewrite` | 5998 | `-` | `3c62a94e160c` | `(?:^https?:\/\/userapi\.qiekj\.com\/integralRecord\/integralDailStatistics$)\|(?:^https?:\/\/userapi\.qiekj\.com\/local-l` |
| 1218 | `URL Rewrite` | 5992 | `-` | `5bf53f7b6cb6` | `(?:^https?://gurd\.snssdk\.com/src/server/v3/package)\|(?:^https?://.+\.byteimg.com/tos-cn-i-1yzifmftcy/(.+)-jpeg\.jpeg)\|` |
| 1242 | `URL Rewrite` | 5988 | `-` | `170b8542b79a` | `(?:^https://htwkop\.xiaojukeji\.com/gateway\?api=hm\.fa\.mallRecommend)\|(?:^https://lawsonapi\.yorentown\.com/area/sh-la` |
| 1234 | `URL Rewrite` | 5987 | `-` | `e1f42522e8b5` | `(?:^https?:\/\/wx\.maoyan\.com\/maoyansh\/myshow\/ajax\/recommend\/performances)\|(?:^https?:\/\/wxs-weixin\.sd\.zhumangg` |
| 1224 | `URL Rewrite` | 5984 | `-` | `cb7db3b7e049` | `(?:^https?:\/\/(webboot\.zhangyue\.com\|ih2\.ireader\.com)\/zybk\/api\/pop\/index\?)\|(?:^https?:\/\/(webboot\.zhangyue\.c` |
| 1236 | `URL Rewrite` | 5984 | `-` | `bf1c226aadf1` | `(?:^https://app\.huashi6\.com/app/index/ad/)\|(?:^https://app\.huashi6\.com/app/works/relative$)\|(?:^https://app\.huashi6` |

## Errors

- None
