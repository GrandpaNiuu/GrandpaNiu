# 脚本去重与 app-cleaner active 迁移报告

生成时间：2026-05-31 07:27:27 +0800

## 本次迁移

- 迁移范围：QQ News、VGTime、SQKB、163News、小黑盒、Manner、超格教育、SMZDM、淘宝、吉祥航空、叮咚买菜、掌上公交、快看漫画、闲鱼、喜马拉雅、滴滴
- 新承接入口：`Scripts/app-cleaner-active.conf` / `app-cleaner-active-json-clean`
- 新承接脚本：`Scripts/app-cleaner.js`
- 计划替换旧入口数量：17
- Scripts/app-clean.conf 本次移除旧入口数量：4
- 所有源文件合计本次移除旧入口数量：8
- 新增 active 入口数量：1
- 说明：这是批量低风险 JSON / 字段清理融合，不是全量脚本合并。

## 移除的旧入口

### `Scripts/app-clean.conf`

#### `cmp_allad_002_kkmh`

- 说明：KKMH JSON cleaner

```text
cmp_allad_002_kkmh = type=http-response,pattern=^https?:\/\/(cdn-)?api\.kkmh\.com\/v\d\/ironman\/discovery_v\d\/tab_list_v\d,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/kkmh.js,script-update-interval=86400
```

#### `cmp_allad_008_goofish`

- 说明：Goofish JSON cleaner

```text
cmp_allad_008_goofish = type=http-response,pattern=^https?:\/\/(g-)?acs\.m\.goofish\.com\/gw\/mtop\.taobao\.idle\.local\.home\/,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/goofish.js,script-update-interval=86400
```

#### `cmp_allad_009_xmly`

- 说明：XMly JSON cleaner

```text
cmp_allad_009_xmly = type=http-response,pattern=^https?:\/\/.*\.xima.*\.com\/discovery-feed\/v\d\/mix,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xmly.js,script-update-interval=86400
```

#### `cmp_allad_010_didi`

- 说明：Didi JSON cleaner

```text
cmp_allad_010_didi = type=http-response,pattern=^https?:\/\/common\.diditaxi\.com\.cn\/common\/v\d\/usercenter\/me,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/didi.js,script-update-interval=86400
```

### `Rewrite/Sources/Script.conf`

#### `cmp_allad_002_kkmh`

- 说明：KKMH JSON cleaner

```text
cmp_allad_002_kkmh = type=http-response,pattern=^https?:\/\/(cdn-)?api\.kkmh\.com\/v\d\/ironman\/discovery_v\d\/tab_list_v\d,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/kkmh.js,script-update-interval=86400
```

#### `cmp_allad_008_goofish`

- 说明：Goofish JSON cleaner

```text
cmp_allad_008_goofish = type=http-response,pattern=^https?:\/\/(g-)?acs\.m\.goofish\.com\/gw\/mtop\.taobao\.idle\.local\.home\/,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/goofish.js,script-update-interval=86400
```

#### `cmp_allad_009_xmly`

- 说明：XMly JSON cleaner

```text
cmp_allad_009_xmly = type=http-response,pattern=^https?:\/\/.*\.xima.*\.com\/discovery-feed\/v\d\/mix,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xmly.js,script-update-interval=86400
```

#### `cmp_allad_010_didi`

- 说明：Didi JSON cleaner

```text
cmp_allad_010_didi = type=http-response,pattern=^https?:\/\/common\.diditaxi\.com\.cn\/common\/v\d\/usercenter\/me,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/didi.js,script-update-interval=86400
```

## 不变范围

- 不动 Spotify。
- 不动 YouTube。
- 不动知乎增强与知乎 R-Store 条目。
- 不动 Tieba JSON / proto。
- 不动小红书、Cotti、RRTV、网易云音乐等复杂脚本。
- 不动登录、支付、验证码、银行相关条目。
- 不合并复杂加密、持久化配置、会员权益、binary-body 脚本。
