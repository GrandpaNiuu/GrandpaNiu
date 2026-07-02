# Android rules build report

- generated: 2026-07-02 23:01:39 Asia/Shanghai
- app rule files: 22
- main Android rules: 952
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
| iOS-App-Compatible-Reject | 682 | yes |
| iOS-Compatible-Reject | 91 | yes |
| iOS-Rewrite-Compatible-Reject | 10 | yes |
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
| 17173-game | 5 |
| 178-game | 2 |
| 18183-game | 3 |
| 1905-movie-network | 4 |
| 2345-web-navigation | 11 |
| 36-kr | 2 |
| 360-smart-camera | 2 |
| 365-calendar | 1 |
| 39-health | 4 |
| 51-cto | 3 |
| 58-auto | 2 |
| 58-tong-cheng | 17 |
| 9-game | 1 |
| ai-pai | 3 |
| ali-yun-drive | 1 |
| all-football | 1 |
| amap | 3 |
| aol | 5 |
| baicizhan | 2 |
| baixing | 6 |
| bao-mi-hua | 3 |
| baofeng-player | 44 |
| bbc | 1 |
| bilibili | 15 |
| bing | 2 |
| biquge | 3 |
| caiyun-weather | 3 |
| camera360 | 3 |
| che-lai-le | 3 |
| cnn | 5 |
| csdn | 5 |
| dang-dang | 3 |
| di-di | 1 |
| didi | 1 |
| dingdong-maicai | 3 |
| douyin | 1 |
| douyu | 2 |
| dragon-read | 10 |
| eastday | 6 |
| etouch-ecalendar | 1 |
| facebook | 3 |
| fan-qie-novel | 14 |
| foodie | 3 |
| funshion | 11 |
| ganji | 6 |
| go-com | 7 |
| hao-you-kuai-bao | 1 |
| hao123 | 3 |
| hkdou-yin | 1 |
| huang-you-xiang-ji | 3 |
| hujiang-online-school | 1 |
| huxiu | 1 |
| huya | 4 |
| i-qi-yi-video | 3 |
| i-reader | 1 |
| i-reader-dejian | 2 |
| jia-xiao-yi-dian-tong | 3 |
| jump | 6 |
| keep | 1 |
| kingsoft-power-word | 8 |
| ku-gou | 8 |
| ku-gou-music | 55 |
| ku6 | 7 |
| kua-ya-zip | 1 |
| kuai-dong-baike | 2 |
| kuai-dui-zuo-ye | 1 |
| kuai-kan-comic | 3 |
| kuai-le-guang-bo | 7 |
| kuaishou | 4 |
| kuwo | 1 |
| le-bo-screen-cast | 3 |
| le-eco | 19 |
| leju | 3 |
| linkedin | 1 |
| lycos | 10 |
| ma-feng-wo | 1 |
| mac-keeper | 5 |
| mama | 1 |
| meet-you | 2 |
| mei-tu | 1 |
| mei-yan-xiang-ji | 2 |
| meitu-myxj | 1 |
| meituan | 11 |
| mgtv | 12 |
| mijia | 1 |
| mop | 2 |
| naver | 4 |
| new-relic | 3 |
| openmultimedia | 1 |
| oupeng | 6 |
| outfit7 | 5 |
| outlook | 3 |
| pcauto | 5 |
| phoenix-new-media | 17 |
| photoable | 2 |
| pinduoduo | 10 |
| pptv | 14 |
| qilu | 2 |
| qqksong | 27 |
| qqmusic | 11 |
| qting-fm | 2 |
| safety-home | 1 |
| sape | 4 |
| seven-cat | 3 |
| sheng-qu-games | 1 |
| shu-qi-center-reader | 1 |
| skyworth | 3 |
| snail-sleep | 1 |
| snapchat | 2 |
| snow-camera | 3 |
| sogou-input | 1 |
| soufun | 2 |
| soul | 11 |
| taobao | 4 |
| tencent-video | 7 |
| terabox | 1 |
| the-paper-news | 5 |
| tube-max | 8 |
| twitch | 2 |
| twitter | 6 |
| wasu-tv | 8 |
| wechat-mini-programs | 2 |
| weibo | 2 |
| xiaopeng | 2 |
| ximalaya | 5 |
| yahoo | 41 |
| yiche | 2 |
| youdao-dict | 1 |
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
| Rewrite/Sources/Apps/chao-ji-ke-cheng-biao.conf | 1 |
| Rewrite/Sources/Apps/douyu.conf | 1 |
| Rewrite/Sources/Apps/line.conf | 1 |
| Rewrite/Sources/Apps/qi-shui-music.conf | 1 |
| Rewrite/Sources/Apps/shao-shu-pai.conf | 1 |
| Rewrite/Sources/Apps/wechat-mini-programs.conf | 3 |

## Repository rule source coverage

| Source file | Migrated reject rules |
|---|---:|
| app-clean.list | 54 |
| qingrex-miniapp-app-ad.list | 59 |
| web-ads.list | 92 |
| wechat-ad.list | 25 |
