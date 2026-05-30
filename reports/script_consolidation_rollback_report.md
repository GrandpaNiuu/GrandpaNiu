# 脚本瘦身回滚报告

生成时间：2026-05-31 06:44:36 +0800

## 回滚条件

如果 QQ News 或 VGTime 在 Stable 中出现页面异常、广告残留加重、JSON 解析异常、加载失败，应回滚本次迁移。

## 回滚步骤

1. 从 `Rewrite/Profiles/stable.conf` 移除 `app_cleaner_active = Scripts/app-cleaner-active.conf`。
2. 从 `Rewrite/Profiles/stable-plus.conf` 移除 `app_cleaner_active = Scripts/app-cleaner-active.conf`。
3. 将下方旧入口恢复到对应文件。
4. 重新运行 build / finalize / build_release_variants / validate。

## 需要恢复的旧入口

### `Scripts/app-clean.conf`

- 当前脚本运行时没有新移除旧入口；如需回滚，请从 Git 历史恢复旧入口。

### `Rewrite/Sources/Script.conf`

```text
cmp_block_097_ad = type=http-response,pattern=^https?:\/\/(news\.ssp\.qq\.com\/app|r\.inews\.qq\.com\/(get(QQNewsUnreadList|TagFeedList)|gw\/page\/event_detail|news_feed\/hot_module_list)),script-path=https://raw.githubusercontent.com/app2smile/rules/master/js/qq-news.js,requires-body=1,timeout=60,script-update-interval=86400
```

```text
cmp_block_098_vgtime = type=http-response,pattern=^https?:\/\/app02\.vgtime\.com:8080\/vgtime-app\/api\/v2\/init\/ad\.json,script-path=https://raw.githubusercontent.com/app2smile/rules/master/js/vgtime.js,requires-body=1,timeout=60,script-update-interval=86400
```

```text
legacy_safe_qqnews = type=http-response,pattern=^https?:\/\/(news\.ssp\.qq\.com\/app|r\.inews\.qq\.com\/(get(QQNewsUnreadList|TagFeedList)|news_feed\/hot_module_list)),script-path=https://raw.githubusercontent.com/app2smile/rules/master/js/qq-news.js,requires-body=1,timeout=60,script-update-interval=86400
```

```text
cmp_allad_046_txnews = type=http-response,pattern=^https?:\/\/r\.inews\.qq\.com\/gw\/page\/(?:event_detail|channel_feed),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/txnews.js,script-update-interval=86400
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
