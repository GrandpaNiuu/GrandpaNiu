# 脚本瘦身回滚报告

生成时间：2026-05-31 08:56:22 +0800

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
cmp_allad_057_douyu = type=http-response,pattern=^https?:\/\/apiv2\.douyucdn\.cn\/japi\/entrance\/roomRes\/nc\/m\/list,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/douyu.js,script-update-interval=86400
```

```text
cmp_allad_058_sptcc = type=http-response,pattern=^https?:\/\/online\.sptcc\.com:\d+\/handapp_update\/AppInfo,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/sptcc.js,script-update-interval=86400
```

```text
cmp_block_090_ad = type=http-response,pattern=^https:\/\/(h3\.)?open\.taou\.com\/maimai\/feed\/v6\/detail_recommend_feeds\?,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/maimai/maimai_ads.js,requires-body=1,timeout=60,script-update-interval=86400
```

```text
cmp_block_099_ad = type=http-response,pattern=^https?:\/\/dict\.youdao\.com\/(homepage\/promotion|course\/tab\/home|homepage\/tile),script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/youdao/dict-youdao-ad.js,requires-body=1,timeout=60,script-update-interval=86400
```

### `Rewrite/Sources/Script.conf`

```text
cmp_allad_057_douyu = type=http-response,pattern=^https?:\/\/apiv2\.douyucdn\.cn\/japi\/entrance\/roomRes\/nc\/m\/list,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/douyu.js,script-update-interval=86400
```

```text
cmp_allad_058_sptcc = type=http-response,pattern=^https?:\/\/online\.sptcc\.com:\d+\/handapp_update\/AppInfo,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/sptcc.js,script-update-interval=86400
```

```text
cmp_block_090_ad = type=http-response,pattern=^https:\/\/(h3\.)?open\.taou\.com\/maimai\/feed\/v6\/detail_recommend_feeds\?,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/maimai/maimai_ads.js,requires-body=1,timeout=60,script-update-interval=86400
```

```text
cmp_block_099_ad = type=http-response,pattern=^https?:\/\/dict\.youdao\.com\/(homepage\/promotion|course\/tab\/home|homepage\/tile),script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/youdao/dict-youdao-ad.js,requires-body=1,timeout=60,script-update-interval=86400
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
