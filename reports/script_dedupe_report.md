# 脚本去重与 app-cleaner active 迁移报告

生成时间：2026-05-31 07:03:08 +0800

## 本次迁移

- 迁移范围：QQ News、VGTime、SQKB、163News、小黑盒、Manner、超格教育
- 新承接入口：`Scripts/app-cleaner-active.conf` / `app-cleaner-active-json-clean`
- 新承接脚本：`Scripts/app-cleaner.js`
- Scripts/app-clean.conf 移除旧入口数量：5
- 所有源文件合计移除旧入口数量：10
- 新增 active 入口数量：1
- 说明：这是低风险 JSON 字段清理融合，不是全量脚本合并。

## 移除的旧入口

### `Scripts/app-clean.conf`

#### `cmp_allad_011_sqkb`

- 说明：SQKB JSON ad cleaner

```text
cmp_allad_011_sqkb = type=http-response,pattern=^https?:\/\/api\.17gwx\.com\/v\d\/history\/remind\/listV,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/sqkb.js,script-update-interval=86400
```

#### `cmp_allad_015_163news`

- 说明：163News JSON ad cleaner

```text
cmp_allad_015_163news = type=http-response,pattern=^https?:\/\/gw\.m\.163\.com\/nc\/api\/v\d\/search\/hot-word,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/163news.js,script-update-interval=86400
```

#### `cmp_allad_022_xiaoheihe`

- 说明：XiaoHeiHe JSON ad cleaner

```text
cmp_allad_022_xiaoheihe = type=http-response,pattern=^https?:\/\/api\.xiaoheihe\.cn\/bbs\/app\/feeds\/news,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xiaoheihe.js,script-update-interval=86400
```

#### `cmp_allad_043_manner`

- 说明：Manner JSON ad cleaner

```text
cmp_allad_043_manner = type=http-response,pattern=^https?:\/\/triangle\.wearemanner\.com\/mp-api\/v\d\/ads,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/manner.js,script-update-interval=86400
```

#### `cmp_allad_044_chaoge`

- 说明：Chaoge JSON ad cleaner

```text
cmp_allad_044_chaoge = type=http-response,pattern=^https?:\/\/mapi\.chaogejiaoyu\.com\/api\/outline\/getAppBanner,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/chaoge.js,script-update-interval=86400
```

### `Rewrite/Sources/Script.conf`

#### `cmp_allad_011_sqkb`

- 说明：SQKB JSON ad cleaner

```text
cmp_allad_011_sqkb = type=http-response,pattern=^https?:\/\/api\.17gwx\.com\/v\d\/history\/remind\/listV,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/sqkb.js,script-update-interval=86400
```

#### `cmp_allad_015_163news`

- 说明：163News JSON ad cleaner

```text
cmp_allad_015_163news = type=http-response,pattern=^https?:\/\/gw\.m\.163\.com\/nc\/api\/v\d\/search\/hot-word,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/163news.js,script-update-interval=86400
```

#### `cmp_allad_022_xiaoheihe`

- 说明：XiaoHeiHe JSON ad cleaner

```text
cmp_allad_022_xiaoheihe = type=http-response,pattern=^https?:\/\/api\.xiaoheihe\.cn\/bbs\/app\/feeds\/news,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xiaoheihe.js,script-update-interval=86400
```

#### `cmp_allad_043_manner`

- 说明：Manner JSON ad cleaner

```text
cmp_allad_043_manner = type=http-response,pattern=^https?:\/\/triangle\.wearemanner\.com\/mp-api\/v\d\/ads,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/manner.js,script-update-interval=86400
```

#### `cmp_allad_044_chaoge`

- 说明：Chaoge JSON ad cleaner

```text
cmp_allad_044_chaoge = type=http-response,pattern=^https?:\/\/mapi\.chaogejiaoyu\.com\/api\/outline\/getAppBanner,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/chaoge.js,script-update-interval=86400
```

## 不变范围

- 不动 Spotify。
- 不动 YouTube。
- 不动知乎增强与知乎 R-Store 条目。
- 不动 Tieba JSON / proto。
- 不动登录、支付、验证码、银行相关条目。
- 不合并复杂加密、持久化配置、会员权益、binary-body 脚本。
