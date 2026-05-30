# 脚本去重与 app-cleaner active 迁移报告

生成时间：2026-05-31 06:38:45 +0800

## 本次迁移

- 迁移范围：QQ News + VGTime
- 新承接入口：`Scripts/app-cleaner-active.conf` / `app-cleaner-active-qqnews-vgtime`
- 新承接脚本：`Scripts/app-cleaner.js`
- 移除旧入口数量：3
- 新增 active 入口数量：1
- 净减少脚本入口：2
- 目标：Stable 脚本数从 104 降到 102。

## 移除的旧入口

### `cmp_block_097_ad`

- 说明：QQ News app2smile entry

```text
cmp_block_097_ad = type=http-response,pattern=^https?:\/\/(news\.ssp\.qq\.com\/app|r\.inews\.qq\.com\/(get(QQNewsUnreadList|TagFeedList)|gw\/page\/event_detail|news_feed\/hot_module_list)),script-path=https://raw.githubusercontent.com/app2smile/rules/master/js/qq-news.js,requires-body=1,timeout=60,script-update-interval=86400
```

### `cmp_block_098_vgtime`

- 说明：VGTime app2smile entry

```text
cmp_block_098_vgtime = type=http-response,pattern=^https?:\/\/app02\.vgtime\.com:8080\/vgtime-app\/api\/v2\/init\/ad\.json,script-path=https://raw.githubusercontent.com/app2smile/rules/master/js/vgtime.js,requires-body=1,timeout=60,script-update-interval=86400
```

### `cmp_allad_046_txnews`

- 说明：QQ News zirawell entry

```text
cmp_allad_046_txnews = type=http-response,pattern=^https?:\/\/r\.inews\.qq\.com\/gw\/page\/(?:event_detail|channel_feed),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/txnews.js,script-update-interval=86400
```


## 不变范围

- 不动 Spotify。
- 不动 YouTube。
- 不动知乎增强。
- 不动 Tieba JSON / proto。
- 不动登录、支付、验证码、银行相关条目。
