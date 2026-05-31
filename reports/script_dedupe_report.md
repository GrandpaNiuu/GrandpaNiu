# 脚本去重与 app-cleaner active 迁移报告

生成时间：2026-05-31 08:56:22 +0800

## 本次迁移

- 迁移范围：Batch 1-6 低风险 JSON / 字段清理融合
- 新承接入口：`Scripts/app-cleaner-active.conf` / `app-cleaner-active-json-clean`
- 新承接脚本：`Scripts/app-cleaner.js`
- 计划替换旧入口数量：71
- Scripts/app-clean.conf 本次移除旧入口数量：4
- 所有源文件合计本次移除旧入口数量：8
- 新增 active 入口数量：1
- 说明：这是大批量融合，但保留高风险和复杂脚本独立运行。

## 移除的旧入口

### `Scripts/app-clean.conf`

#### `cmp_allad_057_douyu`

- 说明：Douyu JSON cleaner

```text
cmp_allad_057_douyu = type=http-response,pattern=^https?:\/\/apiv2\.douyucdn\.cn\/japi\/entrance\/roomRes\/nc\/m\/list,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/douyu.js,script-update-interval=86400
```

#### `cmp_allad_058_sptcc`

- 说明：SPTCC JSON cleaner

```text
cmp_allad_058_sptcc = type=http-response,pattern=^https?:\/\/online\.sptcc\.com:\d+\/handapp_update\/AppInfo,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/sptcc.js,script-update-interval=86400
```

#### `cmp_block_090_ad`

- 说明：Maimai JSON cleaner

```text
cmp_block_090_ad = type=http-response,pattern=^https:\/\/(h3\.)?open\.taou\.com\/maimai\/feed\/v6\/detail_recommend_feeds\?,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/maimai/maimai_ads.js,requires-body=1,timeout=60,script-update-interval=86400
```

#### `cmp_block_099_ad`

- 说明：Youdao Dict JSON cleaner

```text
cmp_block_099_ad = type=http-response,pattern=^https?:\/\/dict\.youdao\.com\/(homepage\/promotion|course\/tab\/home|homepage\/tile),script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/youdao/dict-youdao-ad.js,requires-body=1,timeout=60,script-update-interval=86400
```

### `Rewrite/Sources/Script.conf`

#### `cmp_allad_057_douyu`

- 说明：Douyu JSON cleaner

```text
cmp_allad_057_douyu = type=http-response,pattern=^https?:\/\/apiv2\.douyucdn\.cn\/japi\/entrance\/roomRes\/nc\/m\/list,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/douyu.js,script-update-interval=86400
```

#### `cmp_allad_058_sptcc`

- 说明：SPTCC JSON cleaner

```text
cmp_allad_058_sptcc = type=http-response,pattern=^https?:\/\/online\.sptcc\.com:\d+\/handapp_update\/AppInfo,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/sptcc.js,script-update-interval=86400
```

#### `cmp_block_090_ad`

- 说明：Maimai JSON cleaner

```text
cmp_block_090_ad = type=http-response,pattern=^https:\/\/(h3\.)?open\.taou\.com\/maimai\/feed\/v6\/detail_recommend_feeds\?,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/maimai/maimai_ads.js,requires-body=1,timeout=60,script-update-interval=86400
```

#### `cmp_block_099_ad`

- 说明：Youdao Dict JSON cleaner

```text
cmp_block_099_ad = type=http-response,pattern=^https?:\/\/dict\.youdao\.com\/(homepage\/promotion|course\/tab\/home|homepage\/tile),script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/youdao/dict-youdao-ad.js,requires-body=1,timeout=60,script-update-interval=86400
```

## 不变范围

- 不动 Spotify。
- 不动 YouTube。
- 不动知乎增强与知乎 R-Store 条目。
- 不动 Tieba JSON / proto。
- 不动微博、Keep、Soul、Cotti、RRTV、网易云音乐、12306、航旅纵横、搜狗输入法、韵达等复杂或高风险条目。
- 不动登录、支付、验证码、银行相关条目。
- 不合并复杂加密、持久化配置、会员权益、binary-body 脚本。
