# 脚本瘦身回滚报告

生成时间：2026-05-31 07:03:08 +0800

## 回滚条件

如果本批 App 在 Stable 中出现页面异常、广告残留加重、JSON 解析异常、加载失败，应回滚本次迁移。

## 回滚步骤

1. 从 `Rewrite/Profiles/stable.conf` 移除 `app_cleaner_active = Scripts/app-cleaner-active.conf`。
2. 从 `Rewrite/Profiles/stable-plus.conf` 移除 `app_cleaner_active = Scripts/app-cleaner-active.conf`。
3. 将下方旧入口恢复到对应文件。
4. 重新运行 build / finalize / build_release_variants / validate。

## 需要恢复的旧入口

### `Scripts/app-clean.conf`

```text
cmp_allad_011_sqkb = type=http-response,pattern=^https?:\/\/api\.17gwx\.com\/v\d\/history\/remind\/listV,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/sqkb.js,script-update-interval=86400
```

```text
cmp_allad_015_163news = type=http-response,pattern=^https?:\/\/gw\.m\.163\.com\/nc\/api\/v\d\/search\/hot-word,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/163news.js,script-update-interval=86400
```

```text
cmp_allad_022_xiaoheihe = type=http-response,pattern=^https?:\/\/api\.xiaoheihe\.cn\/bbs\/app\/feeds\/news,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xiaoheihe.js,script-update-interval=86400
```

```text
cmp_allad_043_manner = type=http-response,pattern=^https?:\/\/triangle\.wearemanner\.com\/mp-api\/v\d\/ads,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/manner.js,script-update-interval=86400
```

```text
cmp_allad_044_chaoge = type=http-response,pattern=^https?:\/\/mapi\.chaogejiaoyu\.com\/api\/outline\/getAppBanner,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/chaoge.js,script-update-interval=86400
```

### `Rewrite/Sources/Script.conf`

```text
cmp_allad_011_sqkb = type=http-response,pattern=^https?:\/\/api\.17gwx\.com\/v\d\/history\/remind\/listV,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/sqkb.js,script-update-interval=86400
```

```text
cmp_allad_015_163news = type=http-response,pattern=^https?:\/\/gw\.m\.163\.com\/nc\/api\/v\d\/search\/hot-word,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/163news.js,script-update-interval=86400
```

```text
cmp_allad_022_xiaoheihe = type=http-response,pattern=^https?:\/\/api\.xiaoheihe\.cn\/bbs\/app\/feeds\/news,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xiaoheihe.js,script-update-interval=86400
```

```text
cmp_allad_043_manner = type=http-response,pattern=^https?:\/\/triangle\.wearemanner\.com\/mp-api\/v\d\/ads,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/manner.js,script-update-interval=86400
```

```text
cmp_allad_044_chaoge = type=http-response,pattern=^https?:\/\/mapi\.chaogejiaoyu\.com\/api\/outline\/getAppBanner,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/chaoge.js,script-update-interval=86400
```

## 验证命令

```bash
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_repository.py
python3 scripts/validate_profiles.py
python3 scripts/repository_health_check.py
```
