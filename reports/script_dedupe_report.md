# 脚本去重与 app-cleaner active 迁移报告

生成时间：2026-05-31 07:15:09 +0800

## 本次迁移

- 迁移范围：QQ News、VGTime、SQKB、163News、小黑盒、Manner、超格教育、SMZDM、淘宝、吉祥航空、叮咚买菜、掌上公交
- 新承接入口：`Scripts/app-cleaner-active.conf` / `app-cleaner-active-json-clean`
- 新承接脚本：`Scripts/app-cleaner.js`
- 计划替换旧入口数量：13
- Scripts/app-clean.conf 本次移除旧入口数量：5
- 所有源文件合计本次移除旧入口数量：10
- 新增 active 入口数量：1
- 说明：这是批量低风险 JSON / 字段清理融合，不是全量脚本合并。

## 移除的旧入口

### `Scripts/app-clean.conf`

#### `cmp_allad_013_smzdm`

- 说明：SMZDM detail module cleaner

```text
cmp_allad_013_smzdm = type=http-response,pattern=^https?:\/\/haojia\.m\.smzdm\.com\/detail_modul\/user_related_modul\?,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/smzdm.js,script-update-interval=86400
```

#### `cmp_allad_014_taobao`

- 说明：Taobao poplayer cleaner

```text
cmp_allad_014_taobao = type=http-response,pattern=^https?:\/\/poplayer\.template\.alibaba\.com\/\w+\.json,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/taobao.js,script-update-interval=86400
```

#### `cmp_allad_016_juneyaoair`

- 说明：JuneYaoAir popup cleaner

```text
cmp_allad_016_juneyaoair = type=http-response,pattern=^https?:\/\/hoapp\.juneyaoair\.com\/data\/index\/getPictureList,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/juneyaoair.js,script-update-interval=86400
```

#### `cmp_allad_020_ddxq`

- 说明：DDXQ user page cleaner

```text
cmp_allad_020_ddxq = type=http-response,pattern=^https?:\/\/user\.api\.ddxq\.mobi\/userportal-service\/api\/v\d\/user\/queryMyPage,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/ddxq.js,script-update-interval=86400
```

#### `cmp_allad_021_mygolbs`

- 说明：ZSGJ text replacement cleaner

```text
cmp_allad_021_mygolbs = type=http-response,pattern=^https?:\/\/wx\.mygolbs\.com\/WxBusServer\/ApiData\.do,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/zsgj.js,script-update-interval=86400
```

### `Rewrite/Sources/Script.conf`

#### `cmp_allad_013_smzdm`

- 说明：SMZDM detail module cleaner

```text
cmp_allad_013_smzdm = type=http-response,pattern=^https?:\/\/haojia\.m\.smzdm\.com\/detail_modul\/user_related_modul\?,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/smzdm.js,script-update-interval=86400
```

#### `cmp_allad_014_taobao`

- 说明：Taobao poplayer cleaner

```text
cmp_allad_014_taobao = type=http-response,pattern=^https?:\/\/poplayer\.template\.alibaba\.com\/\w+\.json,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/taobao.js,script-update-interval=86400
```

#### `cmp_allad_016_juneyaoair`

- 说明：JuneYaoAir popup cleaner

```text
cmp_allad_016_juneyaoair = type=http-response,pattern=^https?:\/\/hoapp\.juneyaoair\.com\/data\/index\/getPictureList,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/juneyaoair.js,script-update-interval=86400
```

#### `cmp_allad_020_ddxq`

- 说明：DDXQ user page cleaner

```text
cmp_allad_020_ddxq = type=http-response,pattern=^https?:\/\/user\.api\.ddxq\.mobi\/userportal-service\/api\/v\d\/user\/queryMyPage,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/ddxq.js,script-update-interval=86400
```

#### `cmp_allad_021_mygolbs`

- 说明：ZSGJ text replacement cleaner

```text
cmp_allad_021_mygolbs = type=http-response,pattern=^https?:\/\/wx\.mygolbs\.com\/WxBusServer\/ApiData\.do,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/zsgj.js,script-update-interval=86400
```

## 不变范围

- 不动 Spotify。
- 不动 YouTube。
- 不动知乎增强与知乎 R-Store 条目。
- 不动 Tieba JSON / proto。
- 不动登录、支付、验证码、银行相关条目。
- 不合并复杂加密、持久化配置、会员权益、binary-body 脚本。
