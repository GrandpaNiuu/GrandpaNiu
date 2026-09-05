# Fusion Module Complexity Budget

- Generated at: `2026-09-05T18:57:08.335140Z`
- Status: `passed`
- Scope: generated Fusion complexity only; this validator does not rewrite module content.
- Module bytes: `2911086` / `3500000`
- Module lines: `2780` / `3300`
- Active lines: `2772`
- MITM tokens: `1192` / `1500`
- MITM wildcards: `34` / `60`

## Section Budgets

| Section | Active | Budget |
|---|---:|---:|
| `Rule` | 1196 | 1500 |
| `URL Rewrite` | 40 | 80 |
| `Header Rewrite` | 2 | 20 |
| `Body Rewrite` | 1444 | 1800 |
| `Map Local` | 37 | 80 |
| `Script` | 45 | 70 |
| `MITM` | 1 | 2 |

## Longest Active Lines

| Line | Section | Characters | Exception | SHA-256 | Prefix |
|---:|---|---:|---|---|---|
| 2699 | `Map Local` | 2269910 | `xiaojukeji-charge-map-local` | `1130e43c8c29` | `(?:^https://am\.didistatic\.com/static/am/cf-terminal/epower/epower-thanos-app/\d+\.\d+\.\d+/pages/people/index\.js$) da` |
| 2173 | `Body Rewrite` | 29975 | `-` | `150840c15f2a` | `http-response-jq (?:^https?:\/\/open-cms-api\.quark\.cn\/open-cms\?) 'delpaths([["result","cms_homepage_push_banner_conf` |
| 2716 | `Map Local` | 26300 | `-` | `47c6f638ca9a` | `(?:^https://ucmp(-static)?\.sf-express\.com/proxy/ccspBase/module-config/(login/)?query\?) data-type=json data="{\"versi` |
| 2780 | `MITM` | 22504 | `-` | `0fcd7bc5ee77` | `hostname = %APPEND% spclient.wg.spotify.com,*.spclient.spotify.com,youtubei.googleapis.com,acs.m.goofish.com,acs.m.taoba` |
| 1235 | `URL Rewrite` | 5998 | `-` | `3c62a94e160c` | `(?:^https?:\/\/userapi\.qiekj\.com\/integralRecord\/integralDailStatistics$)\|(?:^https?:\/\/userapi\.qiekj\.com\/local-l` |
| 1240 | `URL Rewrite` | 5998 | `-` | `805168f99c27` | `(?:^https://(webboot\.zhangyue\.com\|ih2\.ireader\.com)/zyboot/activity/mytab\?)\|(?:https://(webboot\.zhangyue\.com\|ih2\.` |
| 1243 | `URL Rewrite` | 5993 | `-` | `61366dc2a55c` | `(?:^https://acs\.m\.taobao\.com/gw/mtop\.fliggy\.crm\.screen\.predict/)\|(?:^https://acs\.m\.taobao\.com/gw/mtop\.fliggy\` |
| 1220 | `URL Rewrite` | 5992 | `-` | `5bf53f7b6cb6` | `(?:^https?://gurd\.snssdk\.com/src/server/v3/package)\|(?:^https?://.+\.byteimg.com/tos-cn-i-1yzifmftcy/(.+)-jpeg\.jpeg)\|` |
| 1236 | `URL Rewrite` | 5987 | `-` | `e1f42522e8b5` | `(?:^https?:\/\/wx\.maoyan\.com\/maoyansh\/myshow\/ajax\/recommend\/performances)\|(?:^https?:\/\/wxs-weixin\.sd\.zhumangg` |
| 1242 | `URL Rewrite` | 5987 | `-` | `c0df5f9c00a2` | `(?:^https://magev6\.if\.qidian\.com/argus/api/v1/booksearch/hotWords\?)\|(?:^https://magev6\.if\.qidian\.com/argus/api/v1` |

## Errors

- None
