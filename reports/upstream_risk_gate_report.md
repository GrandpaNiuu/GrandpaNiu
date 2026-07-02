# Upstream Risk Gate Report

- Generated at: 2026-07-02 23:01:40 +0800
- Status: passed
- Records: 398
- Enabled: 390
- Direct commit: 390
- High risk enabled: 46

## Errors
- None

## Warnings
- None

## Policy

- Enabled direct-commit records must use HTTPS and trusted hosts.
- High-risk and core app records must keep backup enabled.
- Target paths must stay under `Rewrite/Sources/Apps/`.
- Clear VIP unlock, payment bypass, login bypass, purchase receipt and token rewrites are blocked.

## High Risk Enabled Records

- `123-net-work-disk` -> `Rewrite/Sources/Apps/123-net-work-disk.conf` (Kelee PluginHub)
- `12306` -> `Rewrite/Sources/Apps/12306.conf` (Kelee PluginHub)
- `360-child-guard` -> `Rewrite/Sources/Apps/360-child-guard.conf` (fmz200/wool_scripts)
- `ali-yun-drive` -> `Rewrite/Sources/Apps/ali-yun-drive.conf` (Kelee PluginHub)
- `baidu-map` -> `Rewrite/Sources/Apps/baidu-map.conf` (Kelee PluginHub)
- `baidu-net-disk` -> `Rewrite/Sources/Apps/baidu-net-disk.conf` (Kelee PluginHub)
- `baidupan` -> `Rewrite/Sources/Apps/baidupan.conf` (QingRex/LoonKissSurge)
- `bilibili` -> `Rewrite/Sources/Apps/bilibili.conf` (kokoryh/Sparkle)
- `bitqiu-pan` -> `Rewrite/Sources/Apps/bitqiu-pan.conf` (Kelee PluginHub)
- `china-unicom` -> `Rewrite/Sources/Apps/china-unicom.conf` (QingRex/LoonKissSurge)
- `dao-meng-kong-jian` -> `Rewrite/Sources/Apps/dao-meng-kong-jian.conf` (fmz200/wool_scripts)
- `di-di` -> `Rewrite/Sources/Apps/di-di.conf` (Kelee PluginHub)
- `dida-pinche-taxi` -> `Rewrite/Sources/Apps/dida-pinche-taxi.conf` (Kelee PluginHub)
- `didi` -> `Rewrite/Sources/Apps/didi.conf` (QingRex/LoonKissSurge)
- `ding-xiang-doctor` -> `Rewrite/Sources/Apps/ding-xiang-doctor.conf` (fmz200/wool_scripts)
- `ding-xiang-yuan` -> `Rewrite/Sources/Apps/ding-xiang-yuan.conf` (fmz200/wool_scripts)
- `fan-qie-novel` -> `Rewrite/Sources/Apps/fan-qie-novel.conf` (fmz200/wool_scripts)
- `gong-kao-lei-da` -> `Rewrite/Sources/Apps/gong-kao-lei-da.conf` (fmz200/wool_scripts)
- `goofish` -> `Rewrite/Sources/Apps/goofish.conf` (QingRex/LoonKissSurge)
- `kou-dai-xiao-yuan` -> `Rewrite/Sources/Apps/kou-dai-xiao-yuan.conf` (fmz200/wool_scripts)
- `le-cheng` -> `Rewrite/Sources/Apps/le-cheng.conf` (fmz200/wool_scripts)
- `lie-pin` -> `Rewrite/Sources/Apps/lie-pin.conf` (fmz200/wool_scripts)
- `lu-ban-dao-jia` -> `Rewrite/Sources/Apps/lu-ban-dao-jia.conf` (fmz200/wool_scripts)
- `ma-ma-wang-yun-yu` -> `Rewrite/Sources/Apps/ma-ma-wang-yun-yu.conf` (fmz200/wool_scripts)
- `mail-master` -> `Rewrite/Sources/Apps/mail-master.conf` (Kelee PluginHub)
- `mama` -> `Rewrite/Sources/Apps/mama.conf` (fmz200/wool_scripts)
- `mijia` -> `Rewrite/Sources/Apps/mijia.conf` (fmz200/wool_scripts)
- `mobile-clouds` -> `Rewrite/Sources/Apps/mobile-clouds.conf` (Kelee PluginHub)
- `netease-mail` -> `Rewrite/Sources/Apps/netease-mail.conf` (QingRex/LoonKissSurge)
- `qqbrowser` -> `Rewrite/Sources/Apps/qqbrowser.conf` (fmz200/wool_scripts)
- `railway12306` -> `Rewrite/Sources/Apps/railway12306.conf` (QingRex/LoonKissSurge)
- `shou-yin-tong-merchant` -> `Rewrite/Sources/Apps/shou-yin-tong-merchant.conf` (Kelee PluginHub)
- `sogou-input` -> `Rewrite/Sources/Apps/sogou-input.conf` (fmz200/wool_scripts)
- `spotify` -> `Rewrite/Sources/Apps/spotify.conf` (app2smile/rules)
- `taobao-travel` -> `Rewrite/Sources/Apps/taobao-travel.conf` (Kelee PluginHub)
- `taopiaopiao` -> `Rewrite/Sources/Apps/taopiaopiao.conf` (Kelee PluginHub)
- `tencent-games` -> `Rewrite/Sources/Apps/tencent-games.conf` (fmz200/wool_scripts)
- `tencent-games-community` -> `Rewrite/Sources/Apps/tencent-games-community.conf` (fmz200/wool_scripts)
- `tencent-mobile-manager` -> `Rewrite/Sources/Apps/tencent-mobile-manager.conf` (fmz200/wool_scripts)
- `tencent-sports` -> `Rewrite/Sources/Apps/tencent-sports.conf` (fmz200/wool_scripts)
- `terabox` -> `Rewrite/Sources/Apps/terabox.conf` (QingRex/LoonKissSurge)
- `tmall-genie` -> `Rewrite/Sources/Apps/tmall-genie.conf` (fmz200/wool_scripts)
- `ttvoice` -> `Rewrite/Sources/Apps/ttvoice.conf` (fmz200/wool_scripts)
- `wechat` -> `Rewrite/Sources/Apps/wechat.conf` (QingRex/LoonKissSurge)
- `weibo` -> `Rewrite/Sources/Apps/weibo.conf` (QingRex/LoonKissSurge)
- `zhihu` -> `Rewrite/Sources/Apps/zhihu.conf` (QingRex/LoonKissSurge)
