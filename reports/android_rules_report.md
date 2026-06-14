# Android rules build report

- generated: 2026-06-14 12:52:06 Asia/Shanghai
- app rule files: 22
- main Android rules: 616
- source: Android/mihomo/apps/*.yaml
- iOS common source: Rules/reject.list -> iOS-Compatible-Reject
- iOS app source: Rewrite/Sources/Apps/*.conf [Rule] REJECT -> iOS-App-Compatible-Reject
- iOS rewrite source: Rewrite/Sources URL Rewrite reject hostnames -> iOS-Rewrite-Compatible-Reject
- Android ad SDK source: Rules/aggressive-ads.list safe ad-network subset -> Android-Ad-SDK-Compatible-Reject (57)
- repo rule source: Rules/app-clean.list + Rules/web-ads.list + Rules/qingrex-miniapp-app-ad.list + Rules/wechat-ad.list -> Repo-Compatible-Reject
- exported formats: Mihomo / sing-box / AdGuard / v2rayNG
- sync branches: sing-box, AdGuard and v2rayNG are generated from the Mihomo source layer during the same build.
- safety: Script, MITM, Rewrite, DIRECT/PROXY and protected media/payment/login rules are not migrated.

| App | Rules | Outputs |
|---|---:|---|
| Android-Ad-SDK-Compatible-Reject | 57 | yes |
| Bilibili | 1 | yes |
| Domestic-Apps | 146 | yes |
| Douyin | 12 | yes |
| iOS-App-Compatible-Reject | 235 | yes |
| iOS-Compatible-Reject | 230 | yes |
| iOS-Rewrite-Compatible-Reject | 7 | yes |
| iQiyi | 2 | yes |
| Kugou | 4 | yes |
| MangoTV | 11 | yes |
| Meituan-Dianping | 11 | yes |
| NeteaseMusic | 5 | yes |
| Pinduoduo | 9 | yes |
| Repo-Compatible-Reject | 221 | yes |
| Spotify | 4 | yes |
| Taobao | 12 | yes |
| TencentMusic | 5 | yes |
| Weibo | 6 | yes |
| Xiaohongshu | 4 | yes |
| Ximalaya | 6 | yes |
| Youku | 8 | yes |
| YouTube | 15 | yes |

## iOS app source coverage

| Source app | Migrated reject rules |
|---|---:|
| 36-kr | 2 |
| 360-smart-camera | 2 |
| ali-yun-drive | 1 |
| amap | 3 |
| bilibili | 5 |
| caiyun-weather | 3 |
| di-di | 1 |
| didi | 1 |
| dingdong-maicai | 3 |
| douyu | 2 |
| dragon-read | 34 |
| etouch-ecalendar | 1 |
| foodie | 3 |
| huxiu | 1 |
| huya | 4 |
| i-qi-yi-video | 3 |
| i-reader | 1 |
| i-reader-dejian | 2 |
| jump | 7 |
| keep | 1 |
| ku-gou | 8 |
| kuai-dui-zuo-ye | 1 |
| kuai-kan-comic | 3 |
| kuwo | 1 |
| ma-feng-wo | 1 |
| meet-you | 2 |
| mei-tu | 1 |
| meitu-myxj | 1 |
| meituan | 11 |
| mgtv | 12 |
| pcauto | 5 |
| pinduoduo | 10 |
| qqksong | 27 |
| qqmusic | 11 |
| qting-fm | 2 |
| safety-home | 1 |
| seven-cat | 3 |
| shu-qi-center-reader | 1 |
| snail-sleep | 1 |
| snow-camera | 3 |
| soul | 11 |
| taobao | 4 |
| tencent-video | 7 |
| terabox | 1 |
| tube-max | 8 |
| wechat-mini-programs | 2 |
| weibo | 2 |
| xiaopeng | 2 |
| ximalaya | 5 |
| yiche | 2 |
| youku | 13 |
| yueyou | 1 |
| yy-voice | 3 |
| zdm | 1 |
| zhihu | 10 |
| zui-you | 1 |
| zuoyebang | 1 |

## iOS URL Rewrite source coverage

| Source file | Migrated reject host rules |
|---|---:|
| Rewrite/Sources/Apps/51-job.conf | 1 |
| Rewrite/Sources/Apps/auto-home.conf | 1 |
| Rewrite/Sources/Apps/douyu.conf | 1 |
| Rewrite/Sources/Apps/line.conf | 1 |
| Rewrite/Sources/Apps/wechat-mini-programs.conf | 3 |

## Repository rule source coverage

| Source file | Migrated reject rules |
|---|---:|
| app-clean.list | 54 |
| qingrex-miniapp-app-ad.list | 59 |
| web-ads.list | 92 |
| wechat-ad.list | 25 |
