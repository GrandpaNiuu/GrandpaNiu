# 上游来源、许可证与可信分层报告

- 生成时间：2026-08-31 03:53:13 +0800
- App 同步记录：398
- 远程规则 / 参考模块记录：40
- 未记录 license 的来源：438

## 分层定义

- `trusted`：已启用、直接同步、风险较低，并通过当前风险门禁。
- `observe`：可以同步，但需要备份或人工观察，常见于核心 App、高风险 App、未知风险来源。
- `reference_only`：仅作参考或已禁用，不直接写入正式模块。
- `blocked`：同步模式或来源文本命中高危绕过/解锁/凭证类信号，不应直接进入正式模块。

## 总览

| 范围 | trusted | observe | reference_only | blocked |
|---|---:|---:|---:|---:|
| App modules | 0 | 390 | 8 | 0 |
| Remote sources | 2 | 12 | 26 | 0 |

## 上游项目分布

| upstream_project | module_count | sample |
| --- | --- | --- |
| fmz200/wool_scripts | 176 | 17173-game, 178-game, 18183-game, 1905-movie-network, 21-economic-net, 2345-weather-king, 2345-web-navigation, 360-child-guard, 365-calendar, 39-health, 51-cto, 58-auto, 58-tong-ch |
| Kelee PluginHub | 174 | 123-net-work-disk, 12306, 2bulu, 36-kr, 360-smart-camera, 51-job, 555-dy, 91160, aiinquiry, ali-yun-drive, auto-home, baby-tree, baidu-input-method, baidu-map, baidu-net-disk, baid |
| QingRex/LoonKissSurge | 36 | 123pan, amap, baidu, baidu-wenku, baidupan, cainiao, caiyun-weather, china-unicom, didi, goofish, ithome, jd, keep, mgtv, moji-weather, netease-mail, netease-music, pinduoduo, qqmu |
| unknown | 6 | huya, meituan, pcauto, xiaopeng, yiche, zuoyebang |
| app2smile/rules | 3 | qqnews, spotify, vgtime |
| NobyDa/Script | 1 | bahamut-anime |
| kokoryh/Sparkle | 1 | bilibili |
| Maasea/sgmodule | 1 | youtube |

## App 模块来源台账

| id | name | tier | risk | enabled | direct_commit | backup | upstream_project | license | last_sync_mode | target | source_url |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 123-net-work-disk | 123云盘 | observe | high | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/123-net-work-disk.conf | https://kelee.one/Tool/Loon/Lpx/123NetWorkDisk_remove_ads.lpx |
| 12306 | 12306 | observe | high | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/12306.conf | https://kelee.one/Tool/Loon/Lpx/12306_remove_ads.lpx |
| 123pan | 123Pan | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/123pan.conf | QingRex/LoonKissSurge raw |
| 17173-game | 17173（网络游戏门户网站） | observe | medium | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/17173-game.conf | fmz200/wool_scripts raw |
| 178-game | 178游戏网 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/178-game.conf | fmz200/wool_scripts raw |
| 18183-game | 18183游戏网 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/18183-game.conf | fmz200/wool_scripts raw |
| 1905-movie-network | 1905电影网 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/1905-movie-network.conf | fmz200/wool_scripts raw |
| 21-economic-net | 21经济网 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/21-economic-net.conf | fmz200/wool_scripts raw |
| 2345-weather-king | 2345天气王 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/2345-weather-king.conf | fmz200/wool_scripts raw |
| 2345-web-navigation | 2345网址导航 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/2345-web-navigation.conf | fmz200/wool_scripts raw |
| 2bulu | 两步路户外助手 | observe | medium | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/2bulu.conf | https://kelee.one/Tool/Loon/Lpx/2bulu_remove_ads.lpx |
| 36-kr | 36氪 | observe | medium | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/36-kr.conf | https://kelee.one/Tool/Loon/Lpx/36Kr_remove_ads.lpx |
| 360-child-guard | 360儿童卫士 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/360-child-guard.conf | fmz200/wool_scripts raw |
| 360-smart-camera | 360摄像机 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/360-smart-camera.conf | https://kelee.one/Tool/Loon/Lpx/360SmartCamera_remove_ads.lpx |
| 365-calendar | 365日历 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/365-calendar.conf | fmz200/wool_scripts raw |
| 39-health | 39健康网 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/39-health.conf | fmz200/wool_scripts raw |
| 51-cto | 51CTO学堂 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/51-cto.conf | fmz200/wool_scripts raw |
| 51-job | 前程无忧 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/51-job.conf | https://kelee.one/Tool/Loon/Lpx/51Job_remove_ads.lpx |
| 555-dy | 555电影 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/555-dy.conf | https://kelee.one/Tool/Loon/Lpx/555DY_remove_ads.lpx |
| 58-auto | 58汽车 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/58-auto.conf | fmz200/wool_scripts raw |
| 58-tong-cheng | 58同城 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/58-tong-cheng.conf | fmz200/wool_scripts raw |
| 9-game | 九游 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/9-game.conf | fmz200/wool_scripts raw |
| 91160 | 健康160 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/91160.conf | https://kelee.one/Tool/Loon/Lpx/91160_remove_ads.lpx |
| acfun | AcFun | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/acfun.conf | fmz200/wool_scripts raw |
| ai-mei-ju | 爱美剧 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ai-mei-ju.conf | fmz200/wool_scripts raw |
| ai-pai | 爱拍 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ai-pai.conf | fmz200/wool_scripts raw |
| ai-si-assistant | 爱思助手 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ai-si-assistant.conf | fmz200/wool_scripts raw |
| ai-yue-shu-xiang | 爱阅书香 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ai-yue-shu-xiang.conf | fmz200/wool_scripts raw |
| aiinquiry | 爱企查 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/aiinquiry.conf | https://kelee.one/Tool/Loon/Lpx/Aiinquiry_remove_ads.lpx |
| ali-yun-drive | 阿里云盘 | observe | high | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/ali-yun-drive.conf | https://kelee.one/Tool/Loon/Lpx/AliYunDrive_remove_ads.lpx |
| all-football | 懂球帝 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/all-football.conf | fmz200/wool_scripts raw |
| amap | Amap | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/amap.conf | QingRex/LoonKissSurge raw |
| aol | AOL | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/aol.conf | fmz200/wool_scripts raw |
| appso | AppSo | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/appso.conf | fmz200/wool_scripts raw |
| auto-home | 汽车之家 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/auto-home.conf | https://kelee.one/Tool/Loon/Lpx/AutoHome_remove_ads.lpx |
| baby-tree | 宝宝树孕育 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/baby-tree.conf | https://kelee.one/Tool/Loon/Lpx/BabyTree_remove_ads.lpx |
| baby-tree-parenting | 宝宝树孕育 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/baby-tree-parenting.conf | fmz200/wool_scripts raw |
| bahamut-anime | Bahamut Anime | observe | medium | True | True | False | NobyDa/Script | 未记录 | unchanged | Rewrite/Sources/Apps/bahamut-anime.conf | NobyDa/Script raw |
| baicizhan | 百词斩 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/baicizhan.conf | fmz200/wool_scripts raw |
| baidu | Baidu | observe | medium | True | True | True | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/baidu.conf | QingRex/LoonKissSurge raw |
| baidu-input-method | 百度输入法 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/baidu-input-method.conf | https://kelee.one/Tool/Loon/Lpx/Baidu_input_method_remove_ads.lpx |
| baidu-map | 百度地图 | observe | high | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/baidu-map.conf | https://kelee.one/Tool/Loon/Lpx/BaiduMap_remove_ads.lpx |
| baidu-net-disk | 百度网盘 | observe | high | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/baidu-net-disk.conf | https://kelee.one/Tool/Loon/Lpx/BaiduNetDisk_remove_ads.lpx |
| baidu-photo | 一刻相册 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/baidu-photo.conf | https://kelee.one/Tool/Loon/Lpx/BaiduPhoto_remove_ads.lpx |
| baidu-translation | 百度翻译 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/baidu-translation.conf | fmz200/wool_scripts raw |
| baidu-wenku | Baidu Wenku | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/baidu-wenku.conf | QingRex/LoonKissSurge raw |
| baidupan | BaiduPan | observe | high | True | True | True | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/baidupan.conf | QingRex/LoonKissSurge raw |
| baixing | 百姓网 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/baixing.conf | fmz200/wool_scripts raw |
| ban-yue-tan | 半月谈 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ban-yue-tan.conf | fmz200/wool_scripts raw |
| bao-mi-hua | 爆米花 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/bao-mi-hua.conf | fmz200/wool_scripts raw |
| baofeng-player | 暴风影音 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/baofeng-player.conf | fmz200/wool_scripts raw |
| bbc | BBC | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/bbc.conf | fmz200/wool_scripts raw |
| beike | 贝壳找房 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/beike.conf | https://kelee.one/Tool/Loon/Lpx/Beike_remove_ads.lpx |
| betty-kitchen | 贝太厨房 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/betty-kitchen.conf | fmz200/wool_scripts raw |
| bilibili | Bilibili Strong | observe | high | True | True | True | kokoryh/Sparkle | 未记录 | unchanged | Rewrite/Sources/Apps/bilibili.conf | kokoryh/Sparkle raw |
| bilibili-comic | 哔哩哔哩漫画 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/bilibili-comic.conf | https://kelee.one/Tool/Loon/Lpx/BiliComic_remove_ads.lpx |
| bing | Bing | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/bing.conf | fmz200/wool_scripts raw |
| biquge | 笔趣阁 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/biquge.conf | fmz200/wool_scripts raw |
| bitqiu-pan | 比特球云盘 | observe | high | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/bitqiu-pan.conf | https://kelee.one/Tool/Loon/Lpx/BitqiuPan_remove_ads.lpx |
| blued | Blued | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/blued.conf | fmz200/wool_scripts raw |
| bo-luo-bao-light-novel | 菠萝包轻小说 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/bo-luo-bao-light-novel.conf | fmz200/wool_scripts raw |
| bodian-music | 波点音乐 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/bodian-music.conf | https://kelee.one/Tool/Loon/Lpx/BodianMusic_remove_ads.lpx |
| boo-hee | 薄荷健康 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/boo-hee.conf | https://kelee.one/Tool/Loon/Lpx/BooHee_remove_ads.lpx |
| cai-jing-za-zhi | 财经杂志 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/cai-jing-za-zhi.conf | fmz200/wool_scripts raw |
| cai-lian-she | 财联社 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/cai-lian-she.conf | fmz200/wool_scripts raw |
| cainiao | Cainiao | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/cainiao.conf | QingRex/LoonKissSurge raw |
| caixin-media | 财新 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/caixin-media.conf | https://kelee.one/Tool/Loon/Lpx/CaixinMedia_remove_ads.lpx |
| caiyun-weather | Caiyun Weather | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/caiyun-weather.conf | QingRex/LoonKissSurge raw |
| camera360 | Camera360 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/camera360.conf | fmz200/wool_scripts raw |
| cat-ear-fm | 猫耳FM | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/cat-ear-fm.conf | https://kelee.one/Tool/Loon/Lpx/CatEarFM_remove_ads.lpx |
| cclive | CC直播 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/cclive.conf | https://kelee.one/Tool/Loon/Lpx/CCLive_remove_ads.lpx |
| cece | 测测 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/cece.conf | https://kelee.one/Tool/Loon/Lpx/Cece_remove_ads.lpx |
| chao-ji-ke-cheng-biao | 超级课程表 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/chao-ji-ke-cheng-biao.conf | fmz200/wool_scripts raw |
| chao-xing-xue-xi-tong | 超星学习通 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/chao-xing-xue-xi-tong.conf | fmz200/wool_scripts raw |
| che-lai-le | 车来了 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/che-lai-le.conf | fmz200/wool_scripts raw |
| cheng-fen-miao | 成分喵 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/cheng-fen-miao.conf | https://kelee.one/Tool/Loon/Lpx/ChengFenMiao_remove_ads.lpx |
| china-unicom | China Unicom | observe | high | True | True | True | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/china-unicom.conf | QingRex/LoonKissSurge raw |
| chuzhan | 触站 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/chuzhan.conf | https://kelee.one/Tool/Loon/Lpx/Chuzhan_remove_ads.lpx |
| ci-wei-mao-yue-du | 刺猬猫阅读 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ci-wei-mao-yue-du.conf | fmz200/wool_scripts raw |
| clicli | clicli | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/clicli.conf | fmz200/wool_scripts raw |
| cnn | CNN | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/cnn.conf | fmz200/wool_scripts raw |
| cool-apk | 酷安 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/cool-apk.conf | https://kelee.one/Tool/Loon/Lpx/CoolApk_remove_ads.lpx |
| coolapk | 酷安 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/coolapk.conf | fmz200/wool_scripts raw |
| crunchyroll | crunchyroll | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/crunchyroll.conf | fmz200/wool_scripts raw |
| csdn | CSDN | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/csdn.conf | fmz200/wool_scripts raw |
| csg | 南网在线 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/csg.conf | https://kelee.one/Tool/Loon/Lpx/CSG_remove_ads.lpx |
| da-shi-xiong | 大师兄 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/da-shi-xiong.conf | fmz200/wool_scripts raw |
| daily | 推栏 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/daily.conf | https://kelee.one/Tool/Loon/Lpx/Daily_remove_ads.lpx |
| damai | 大麦 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/damai.conf | https://kelee.one/Tool/Loon/Lpx/Damai_remove_ads.lpx |
| dang-dang | 当当网 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/dang-dang.conf | fmz200/wool_scripts raw |
| dang-dang-reading | 当当阅读 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/dang-dang-reading.conf | fmz200/wool_scripts raw |
| dao-meng-kong-jian | 到梦空间 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/dao-meng-kong-jian.conf | fmz200/wool_scripts raw |
| dewu | 得物 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/dewu.conf | https://kelee.one/Tool/Loon/Lpx/Dewu_remove_ads.lpx |
| di-di | 滴滴出行 | observe | high | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/di-di.conf | https://kelee.one/Tool/Loon/Lpx/DiDi_remove_ads.lpx |
| di-duan-ying-shi | 低端影视 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/di-duan-ying-shi.conf | fmz200/wool_scripts raw |
| dian-shi-jia | 电视家 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/dian-shi-jia.conf | fmz200/wool_scripts raw |
| dida-pinche-taxi | 滴答出行 | observe | high | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/dida-pinche-taxi.conf | https://kelee.one/Tool/Loon/Lpx/DidaPincheTaxi_remove_ads.lpx |
| didi | Didi | observe | high | True | True | True | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/didi.conf | QingRex/LoonKissSurge raw |
| digital-heartbeat | 数字心动 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/digital-heartbeat.conf | https://kelee.one/Tool/Loon/Lpx/DigitalHeartbeat_remove_ads.lpx |
| ding-xiang-doctor | 丁香医生 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ding-xiang-doctor.conf | fmz200/wool_scripts raw |
| ding-xiang-yuan | 丁香园 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ding-xiang-yuan.conf | fmz200/wool_scripts raw |
| dingdong-maicai | 叮咚买菜 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/dingdong-maicai.conf | https://kelee.one/Tool/Loon/Lpx/DingdongMaicai_remove_ads.lpx |
| dlabel | Dlabel云标签 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/dlabel.conf | https://kelee.one/Tool/Loon/Lpx/Dlabel_remove_ads.lpx |
| dlabel-cloud-tag | DLabel云标签 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/dlabel-cloud-tag.conf | fmz200/wool_scripts raw |
| dong-hua-feng | 动画疯 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/dong-hua-feng.conf | fmz200/wool_scripts raw |
| dou-ban | 豆瓣 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/dou-ban.conf | https://kelee.one/Tool/Loon/Lpx/DouBan_remove_ads.lpx |
| douban-read | 豆瓣阅读 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/douban-read.conf | https://kelee.one/Tool/Loon/Lpx/DoubanRead_remove_ads.lpx |
| douyin | 抖音 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | updated | Rewrite/Sources/Apps/douyin.conf | fmz200/wool_scripts raw |
| douyu | 斗鱼 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/douyu.conf | https://kelee.one/Tool/Loon/Lpx/Douyu_remove_ads.lpx |
| dragon-read | 番茄小说 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | updated | Rewrite/Sources/Apps/dragon-read.conf | https://kelee.one/Tool/Loon/Lpx/DragonRead_remove_ads.lpx |
| dreame | DREAME | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/dreame.conf | https://kelee.one/Tool/Loon/Lpx/DREAME_remove_ads.lpx |
| dubbing-show | 配音秀 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/dubbing-show.conf | https://kelee.one/Tool/Loon/Lpx/DubbingShow_remove_ads.lpx |
| dui-tang | 堆糖 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/dui-tang.conf | https://kelee.one/Tool/Loon/Lpx/DuiTang_remove_ads.lpx |
| eastday | 东方网 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/eastday.conf | fmz200/wool_scripts raw |
| ecovacs-home | ECOVACS HOME | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/ecovacs-home.conf | https://kelee.one/Tool/Loon/Lpx/EcovacsHome_remove_ads.lpx |
| etouch-ecalendar | 中华万年历 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/etouch-ecalendar.conf | https://kelee.one/Tool/Loon/Lpx/EtouchEcalendar_remove_ads.lpx |
| facebook | Facebook | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/facebook.conf | fmz200/wool_scripts raw |
| fan-deng-reading | 樊登读书 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/fan-deng-reading.conf | fmz200/wool_scripts raw |
| fan-qie-novel | 番茄小说 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/fan-qie-novel.conf | fmz200/wool_scripts raw |
| fc-box | 丰巢 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/fc-box.conf | https://kelee.one/Tool/Loon/Lpx/FC_Box_remove_ads.lpx |
| fei-ke-cha-guan | 飞客茶馆 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/fei-ke-cha-guan.conf | fmz200/wool_scripts raw |
| fen-bi | 粉笔 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/fen-bi.conf | https://kelee.one/Tool/Loon/Lpx/FenBi_remove_ads.lpx |
| feng-huang-xiu | 凤凰秀 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/feng-huang-xiu.conf | fmz200/wool_scripts raw |
| ferris-wheel | 摩天轮 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/ferris-wheel.conf | https://kelee.one/Tool/Loon/Lpx/FerrisWheel_remove_ads.lpx |
| finance-news | 华尔街见闻 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/finance-news.conf | https://kelee.one/Tool/Loon/Lpx/FinanceNews_remove_ads.lpx |
| flea-market | 闲鱼 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/flea-market.conf | https://kelee.one/Tool/Loon/Lpx/FleaMarket_remove_ads.lpx |
| flightradar24 | Flightradar24 | observe | medium | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/flightradar24.conf | fmz200/wool_scripts raw |
| flyer-tea | 飞客 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/flyer-tea.conf | https://kelee.one/Tool/Loon/Lpx/FlyerTea_remove_ads.lpx |
| foodie | Foodie | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/foodie.conf | https://kelee.one/Tool/Loon/Lpx/Foodie_remove_ads.lpx |
| funshion | 风行网 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/funshion.conf | fmz200/wool_scripts raw |
| ganji | 赶集网 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ganji.conf | fmz200/wool_scripts raw |
| gao-ding | 稿定设计 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/gao-ding.conf | https://kelee.one/Tool/Loon/Lpx/GaoDing_remove_ads.lpx |
| go-com | Go.com | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/go-com.conf | fmz200/wool_scripts raw |
| gong-kao-lei-da | 公考雷达 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/gong-kao-lei-da.conf | fmz200/wool_scripts raw |
| goofish | Goofish | observe | high | True | True | True | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/goofish.conf | QingRex/LoonKissSurge raw |
| guide-rank | 盖得排行 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/guide-rank.conf | https://kelee.one/Tool/Loon/Lpx/GuideRank_remove_ads.lpx |
| hanju-tv | 韩剧TV | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/hanju-tv.conf | fmz200/wool_scripts raw |
| hanting-hotels | 华住会 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/hanting-hotels.conf | https://kelee.one/Tool/Loon/Lpx/HantingHotels_remove_ads.lpx |
| hao-hao-zhu | 好好住 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/hao-hao-zhu.conf | fmz200/wool_scripts raw |
| hao-qi-xin-daily | 好奇心日报 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/hao-qi-xin-daily.conf | fmz200/wool_scripts raw |
| hao-you-kuai-bao | 好游快爆 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/hao-you-kuai-bao.conf | fmz200/wool_scripts raw |
| hao123 | Hao123 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/hao123.conf | fmz200/wool_scripts raw |
| he-feng-weather | 和风天气 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/he-feng-weather.conf | fmz200/wool_scripts raw |
| heartide-brain-wave | 小睡眠 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/heartide-brain-wave.conf | https://kelee.one/Tool/Loon/Lpx/HeartideBrainWave_remove_ads.lpx |
| hkdou-yin | 香港抖音 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | updated | Rewrite/Sources/Apps/hkdou-yin.conf | https://kelee.one/Tool/Loon/Lpx/HKDouYin_remove_ads.lpx |
| hong-ban-bao | 红版报 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/hong-ban-bao.conf | fmz200/wool_scripts raw |
| hua-sheng-di-tie | 花生地铁 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/hua-sheng-di-tie.conf | fmz200/wool_scripts raw |
| huang-you-xiang-ji | 黄油相机 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/huang-you-xiang-ji.conf | fmz200/wool_scripts raw |
| hujiang-online-school | 沪江网校 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/hujiang-online-school.conf | fmz200/wool_scripts raw |
| huo-mao | 火猫 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/huo-mao.conf | fmz200/wool_scripts raw |
| hupu | 虎扑 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/hupu.conf | https://kelee.one/Tool/Loon/Lpx/HUPU_remove_ads.lpx |
| huxiu | 虎嗅 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/huxiu.conf | https://kelee.one/Tool/Loon/Lpx/Huxiu_remove_ads.lpx |
| huya | Huya | reference_only | medium | False | False | False | unknown | 未记录 | missing-upstream-source | Rewrite/Sources/Apps/huya.conf |  |
| i-mai-cai | 小象超市 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/i-mai-cai.conf | https://kelee.one/Tool/Loon/Lpx/iMaiCai_remove_ads.lpx |
| i-qi-yi-video | 爱奇艺 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/i-qi-yi-video.conf | https://kelee.one/Tool/Loon/Lpx/iQiYi_Video_remove_ads.lpx |
| i-reader | 掌阅 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/i-reader.conf | https://kelee.one/Tool/Loon/Lpx/iReader_remove_ads.lpx |
| i-reader-dejian | 得间小说 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/i-reader-dejian.conf | https://kelee.one/Tool/Loon/Lpx/iReaderDejian_remove_ads.lpx |
| ithome | IT Home | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/ithome.conf | QingRex/LoonKissSurge raw |
| jd | JD | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/jd.conf | QingRex/LoonKissSurge raw |
| jdreading | 京东读书 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/jdreading.conf | fmz200/wool_scripts raw |
| jdwaimai | 京东外卖 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/jdwaimai.conf | https://kelee.one/Tool/Loon/Lpx/JDWaimai_remove_ads.lpx |
| ji-he-wang | 机核网 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ji-he-wang.conf | fmz200/wool_scripts raw |
| jia-kao-bao-dian | 驾考宝典 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/jia-kao-bao-dian.conf | https://kelee.one/Tool/Loon/Lpx/JiaKaoBaoDian_remove_ads.lpx |
| jia-xiao-drive | 驾校一点通 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/jia-xiao-drive.conf | https://kelee.one/Tool/Loon/Lpx/JiaXiaoDrive_remove_ads.lpx |
| jia-xiao-yi-dian-tong | 驾校一点通 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/jia-xiao-yi-dian-tong.conf | fmz200/wool_scripts raw |
| jian-xun | 简讯 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/jian-xun.conf | fmz200/wool_scripts raw |
| jie-mian-news | 界面新闻 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/jie-mian-news.conf | fmz200/wool_scripts raw |
| jin-ri-shui-yin-camera | 今日水印相机 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/jin-ri-shui-yin-camera.conf | fmz200/wool_scripts raw |
| jump | Jump | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/jump.conf | https://kelee.one/Tool/Loon/Lpx/Jump_remove_ads.lpx |
| kan-dong-fang | 看东方（百视TV） | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/kan-dong-fang.conf | fmz200/wool_scripts raw |
| kan-li-xiang | 看理想 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/kan-li-xiang.conf | fmz200/wool_scripts raw |
| kan-tian-xia | 看天下 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/kan-tian-xia.conf | fmz200/wool_scripts raw |
| kebida-dushu | 帆书 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/kebida-dushu.conf | https://kelee.one/Tool/Loon/Lpx/KebidaDushu_remove_ads.lpx |
| keep | Keep | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/keep.conf | QingRex/LoonKissSurge raw |
| kfc | 肯德基 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/kfc.conf | fmz200/wool_scripts raw |
| kgring | 酷狗铃声 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/kgring.conf | https://kelee.one/Tool/Loon/Lpx/KGRing_remove_ads.lpx |
| kingdee-my-money | 随手记 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/kingdee-my-money.conf | https://kelee.one/Tool/Loon/Lpx/KingdeeMyMoney_remove_ads.lpx |
| kingsoft-power-word | 金山词霸 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/kingsoft-power-word.conf | fmz200/wool_scripts raw |
| kook | KOOK | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/kook.conf | https://kelee.one/Tool/Loon/Lpx/KOOK_remove_ads.lpx |
| kou-dai-xiao-yuan | 口袋校园 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/kou-dai-xiao-yuan.conf | fmz200/wool_scripts raw |
| ku-gou | 酷狗音乐 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/ku-gou.conf | https://kelee.one/Tool/Loon/Lpx/KuGou_remove_ads.lpx |
| ku-gou-music | 酷狗音乐 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ku-gou-music.conf | fmz200/wool_scripts raw |
| ku-gou-youth | 酷狗概念版 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/ku-gou-youth.conf | https://kelee.one/Tool/Loon/Lpx/KuGouYouth_remove_ads.lpx |
| ku6 | 酷6网 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ku6.conf | fmz200/wool_scripts raw |
| kua-ya-zip | 快压zip | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/kua-ya-zip.conf | fmz200/wool_scripts raw |
| kuai-di100 | 快递100 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/kuai-di100.conf | https://kelee.one/Tool/Loon/Lpx/KuaiDi100_remove_ads.lpx |
| kuai-dong-baike | 快懂百科 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/kuai-dong-baike.conf | fmz200/wool_scripts raw |
| kuai-dui-zuo-ye | 快对 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/kuai-dui-zuo-ye.conf | https://kelee.one/Tool/Loon/Lpx/KuaiDuiZuoYe_remove_ads.lpx |
| kuai-kan | 快看 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/kuai-kan.conf | fmz200/wool_scripts raw |
| kuai-kan-comic | 快看漫画 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/kuai-kan-comic.conf | https://kelee.one/Tool/Loon/Lpx/KuaiKanComic_remove_ads.lpx |
| kuai-le-guang-bo | 快乐广播 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/kuai-le-guang-bo.conf | fmz200/wool_scripts raw |
| kuai-shou | 快手 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/kuai-shou.conf | https://kelee.one/Tool/Loon/Lpx/KuaiShou_remove_ads.lpx |
| kuaishou | 快手 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/kuaishou.conf | fmz200/wool_scripts raw |
| kuro-bbs | 库街区 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/kuro-bbs.conf | https://kelee.one/Tool/Loon/Lpx/KuroBBS_remove_ads.lpx |
| kuwo | 酷我音乐 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/kuwo.conf | https://kelee.one/Tool/Loon/Lpx/Kuwo_remove_ads.lpx |
| kwai-videoeditor | 快影 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/kwai-videoeditor.conf | https://kelee.one/Tool/Loon/Lpx/KwaiVideoeditor_remove_ads.lpx |
| lai-dian | 来电 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/lai-dian.conf | fmz200/wool_scripts raw |
| lai-feng | 来疯 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/lai-feng.conf | fmz200/wool_scripts raw |
| lan-jie100 | 拦截100 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/lan-jie100.conf | fmz200/wool_scripts raw |
| lan-ren-ting-shu | 懒人听书 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/lan-ren-ting-shu.conf | fmz200/wool_scripts raw |
| le-bo-screen-cast | 乐播投屏 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/le-bo-screen-cast.conf | fmz200/wool_scripts raw |
| le-cheng | 乐橙 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/le-cheng.conf | fmz200/wool_scripts raw |
| le-eco | 乐视 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/le-eco.conf | fmz200/wool_scripts raw |
| leju | 乐居 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/leju.conf | fmz200/wool_scripts raw |
| lenovo-print | 联想至像打印 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/lenovo-print.conf | fmz200/wool_scripts raw |
| lie-pin | 猎聘 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/lie-pin.conf | fmz200/wool_scripts raw |
| line | Line | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/line.conf | https://kelee.one/Tool/Loon/Lpx/Line_remove_ads.lpx |
| linkedin | LinkedIn | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/linkedin.conf | fmz200/wool_scripts raw |
| live-lab | 纷玩岛 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/live-lab.conf | https://kelee.one/Tool/Loon/Lpx/LiveLab_remove_ads.lpx |
| lofter | lofter | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/lofter.conf | fmz200/wool_scripts raw |
| lol-bible | 掌上英雄联盟 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/lol-bible.conf | https://kelee.one/Tool/Loon/Lpx/LOL_Bible_remove_ads.lpx |
| lu-ban-dao-jia | 鲁班到家用户版 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/lu-ban-dao-jia.conf | fmz200/wool_scripts raw |
| luckin-coffee | 瑞幸咖啡 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/luckin-coffee.conf | https://kelee.one/Tool/Loon/Lpx/LuckinCoffee_remove_ads.lpx |
| lv-fa-shi-ying-di | 旅法师营地 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/lv-fa-shi-ying-di.conf | fmz200/wool_scripts raw |
| lv-tu-sui-shen-ting | 旅途随身听 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/lv-tu-sui-shen-ting.conf | fmz200/wool_scripts raw |
| lycos | Lycos | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/lycos.conf | fmz200/wool_scripts raw |
| ma-feng-wo | 马蜂窝 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/ma-feng-wo.conf | https://kelee.one/Tool/Loon/Lpx/MaFengWo_remove_ads.lpx |
| ma-ka-long-wan-tu | 马卡龙玩图 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ma-ka-long-wan-tu.conf | fmz200/wool_scripts raw |
| ma-ma-wang-yun-yu | 妈妈网孕育 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ma-ma-wang-yun-yu.conf | fmz200/wool_scripts raw |
| mac-keeper | MacKeeper | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/mac-keeper.conf | fmz200/wool_scripts raw |
| mai-dui-dui | 埋堆堆 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/mai-dui-dui.conf | fmz200/wool_scripts raw |
| mai-mai | 脉脉 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/mai-mai.conf | https://kelee.one/Tool/Loon/Lpx/MaiMai_remove_ads.lpx |
| mail-master | 网易邮箱大师 | observe | high | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/mail-master.conf | https://kelee.one/Tool/Loon/Lpx/MailMaster_remove_ads.lpx |
| mama | 妈妈网 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/mama.conf | fmz200/wool_scripts raw |
| man-hua-ren | 漫画人 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/man-hua-ren.conf | fmz200/wool_scripts raw |
| meet-you | 美柚 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/meet-you.conf | https://kelee.one/Tool/Loon/Lpx/MeetYou_remove_ads.lpx |
| mei-ri-jing-xuan | 每日精选 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/mei-ri-jing-xuan.conf | fmz200/wool_scripts raw |
| mei-shi-jie | 美食杰 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/mei-shi-jie.conf | https://kelee.one/Tool/Loon/Lpx/MeiShiJie_remove_ads.lpx |
| mei-tu | 美图秀秀 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/mei-tu.conf | https://kelee.one/Tool/Loon/Lpx/MeiTu_remove_ads.lpx |
| mei-yan-xiang-ji | 美颜相机 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/mei-yan-xiang-ji.conf | fmz200/wool_scripts raw |
| meitu-myxj | 美颜相机 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/meitu-myxj.conf | https://kelee.one/Tool/Loon/Lpx/MeituMYXJ_remove_ads.lpx |
| meituan | Meituan | reference_only | medium | False | False | False | unknown | 未记录 | missing-upstream-source | Rewrite/Sources/Apps/meituan.conf |  |
| meizhixiuxing | 美丽修行 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/meizhixiuxing.conf | https://kelee.one/Tool/Loon/Lpx/Meizhixiuxing_remove_ads.lpx |
| mgtv | MGTV | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/mgtv.conf | QingRex/LoonKissSurge raw |
| mi-ho-yo-bbs | 米游社 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/mi-ho-yo-bbs.conf | https://kelee.one/Tool/Loon/Lpx/miHoYoBBS_remove_ads.lpx |
| miao-pai | 秒拍 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/miao-pai.conf | fmz200/wool_scripts raw |
| miao-read | 小喵看书 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/miao-read.conf | https://kelee.one/Tool/Loon/Lpx/MiaoRead_remove_ads.lpx |
| mijia | 米家 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/mijia.conf | fmz200/wool_scripts raw |
| mix | MIX | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/mix.conf | fmz200/wool_scripts raw |
| mkz | 漫客栈 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/mkz.conf | https://kelee.one/Tool/Loon/Lpx/MKZ_remove_ads.lpx |
| mobile-clouds | 中国移动云盘 | observe | high | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/mobile-clouds.conf | https://kelee.one/Tool/Loon/Lpx/mobileClouds_remove_ads.lpx |
| moe-girl-wiki | 萌娘百科 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/moe-girl-wiki.conf | https://kelee.one/Tool/Loon/Lpx/MoeGirlWiki_remove_ads.lpx |
| moji-weather | Moji Weather | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/moji-weather.conf | QingRex/LoonKissSurge raw |
| mop | 猫扑 (Mop) | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/mop.conf | fmz200/wool_scripts raw |
| mr-hema | 盒马 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/mr-hema.conf | https://kelee.one/Tool/Loon/Lpx/MrHema_remove_ads.lpx |
| nai-fei-ying-shi | 奈菲影视 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/nai-fei-ying-shi.conf | fmz200/wool_scripts raw |
| narwel-robots | 云鲸智能 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/narwel-robots.conf | https://kelee.one/Tool/Loon/Lpx/NarwelRobots_remove_ads.lpx |
| naver | Naver | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/naver.conf | fmz200/wool_scripts raw |
| net-ease-godlike | 网易大神 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/net-ease-godlike.conf | https://kelee.one/Tool/Loon/Lpx/NetEaseGodlike_remove_ads.lpx |
| netease-mail | Netease Mail | observe | high | True | True | True | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/netease-mail.conf | QingRex/LoonKissSurge raw |
| netease-music | Netease Music | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/netease-music.conf | QingRex/LoonKissSurge raw |
| netease-news | 网易新闻 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/netease-news.conf | https://kelee.one/Tool/Loon/Lpx/NeteaseNews_remove_ads.lpx |
| new-relic | New Relic | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/new-relic.conf | fmz200/wool_scripts raw |
| niu-ting-ting | 牛听听 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/niu-ting-ting.conf | fmz200/wool_scripts raw |
| ntplay | NTPlay | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ntplay.conf | fmz200/wool_scripts raw |
| omofun | omofun | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/omofun.conf | fmz200/wool_scripts raw |
| on-the-way | 行者户外 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/on-the-way.conf | https://kelee.one/Tool/Loon/Lpx/OnTheWay_remove_ads.lpx |
| one | ONE | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/one.conf | fmz200/wool_scripts raw |
| openmultimedia | Openmultimedia | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/openmultimedia.conf | fmz200/wool_scripts raw |
| oray-sunlogin | 向日葵 | observe | medium | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/oray-sunlogin.conf | https://kelee.one/Tool/Loon/Lpx/OraySunlogin_remove_ads.lpx |
| oschina | 开源中国 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/oschina.conf | fmz200/wool_scripts raw |
| oupeng | Oupeng (欧朋) | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/oupeng.conf | fmz200/wool_scripts raw |
| outfit7 | Outfit7（会说话的汤姆猫） | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/outfit7.conf | fmz200/wool_scripts raw |
| outlook | Outlook | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/outlook.conf | fmz200/wool_scripts raw |
| oxford-ald10th | 牛津高阶词典第十版 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/oxford-ald10th.conf | fmz200/wool_scripts raw |
| pangguai-life | 胖乖生活 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/pangguai-life.conf | https://kelee.one/Tool/Loon/Lpx/PangguaiLife_remove_ads.lpx |
| pcauto | PCAuto | reference_only | medium | False | False | False | unknown | 未记录 | missing-upstream-source | Rewrite/Sources/Apps/pcauto.conf |  |
| perfect-world-esport | 完美世界电竞 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/perfect-world-esport.conf | https://kelee.one/Tool/Loon/Lpx/PerfectWorldEsport_remove_ads.lpx |
| phoenix-new-media | 凤凰新媒体 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/phoenix-new-media.conf | fmz200/wool_scripts raw |
| photoable | Photoable | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/photoable.conf | fmz200/wool_scripts raw |
| pi-pi-gao-xiao | 皮皮搞笑 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/pi-pi-gao-xiao.conf | fmz200/wool_scripts raw |
| pi-pi-xia | 皮皮虾 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/pi-pi-xia.conf | https://kelee.one/Tool/Loon/Lpx/PiPiXia_remove_ads.lpx |
| picc-insurance | 中国人保 | observe | medium | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/picc-insurance.conf | https://kelee.one/Tool/Loon/Lpx/PICC_Insurance_remove_ads.lpx |
| pinduoduo | Pinduoduo | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/pinduoduo.conf | QingRex/LoonKissSurge raw |
| pinterest | Pinterest | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/pinterest.conf | https://kelee.one/Tool/Loon/Lpx/Pinterest_remove_ads.lpx |
| pptv | PPTV | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/pptv.conf | fmz200/wool_scripts raw |
| pu-pu-mall | 朴朴超市 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/pu-pu-mall.conf | https://kelee.one/Tool/Loon/Lpx/PuPuMall_remove_ads.lpx |
| qi-dian | 起点读书 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/qi-dian.conf | https://kelee.one/Tool/Loon/Lpx/QiDian_remove_ads.lpx |
| qi-shui-music | 汽水音乐 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/qi-shui-music.conf | fmz200/wool_scripts raw |
| qi-xin-bao | 启信宝 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/qi-xin-bao.conf | https://kelee.one/Tool/Loon/Lpx/QiXinBao_remove_ads.lpx |
| qilu | 齐鲁网 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/qilu.conf | fmz200/wool_scripts raw |
| qqbrowser | QQ浏览器 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/qqbrowser.conf | fmz200/wool_scripts raw |
| qqksong | 全民K歌 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/qqksong.conf | https://kelee.one/Tool/Loon/Lpx/QQKSong_remove_ads.lpx |
| qqmusic | QQ Music | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/qqmusic.conf | QingRex/LoonKissSurge raw |
| qqnews | QQ News | reference_only | medium | False | False | False | app2smile/rules | 未记录 | missing-upstream-source | Rewrite/Sources/Apps/qqnews.conf |  |
| qting-fm | 蜻蜓FM | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/qting-fm.conf | https://kelee.one/Tool/Loon/Lpx/QtingFM_remove_ads.lpx |
| quan-min-ge-ge | 全民K歌 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/quan-min-ge-ge.conf | fmz200/wool_scripts raw |
| quan-neng-browser | 全能浏览器 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/quan-neng-browser.conf | fmz200/wool_scripts raw |
| quark | Quark | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/quark.conf | QingRex/LoonKissSurge raw |
| quark-scan | 夸克扫描王 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/quark-scan.conf | https://kelee.one/Tool/Loon/Lpx/QuarkScanking_remove_ads.lpx |
| railway12306 | Railway 12306 | observe | high | True | True | True | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/railway12306.conf | QingRex/LoonKissSurge raw |
| reddit | Reddit | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/reddit.conf | QingRex/LoonKissSurge raw |
| rednote | RedNote | observe | medium | True | True | True | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/rednote.conf | QingRex/LoonKissSurge raw |
| reel-short | ReelShort | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/reel-short.conf | https://kelee.one/Tool/Loon/Lpx/ReelShort_remove_ads.lpx |
| ri-ri-zhu | 日日煮 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ri-ri-zhu.conf | fmz200/wool_scripts raw |
| risk-bird | 风鸟 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/risk-bird.conf | https://kelee.one/Tool/Loon/Lpx/RiskBird_remove_ads.lpx |
| robo-taxi | 萝卜快跑 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/robo-taxi.conf | https://kelee.one/Tool/Loon/Lpx/RoboTaxi_remove_ads.lpx |
| roborock | Roborock | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/roborock.conf | https://kelee.one/Tool/Loon/Lpx/Roborock_remove_ads.lpx |
| rqrun | RQrun | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/rqrun.conf | https://kelee.one/Tool/Loon/Lpx/RQrun_remove_ads.lpx |
| safety-home | 360智慧生活 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/safety-home.conf | https://kelee.one/Tool/Loon/Lpx/SafetyHome_remove_ads.lpx |
| san-lian-zhong-du | 三联中读 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/san-lian-zhong-du.conf | fmz200/wool_scripts raw |
| sape | Sape | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/sape.conf | fmz200/wool_scripts raw |
| seasun-jx3 | 剑网三无界 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/seasun-jx3.conf | https://kelee.one/Tool/Loon/Lpx/SeasunJX3_remove_ads.lpx |
| seven-cat | 七猫小说 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/seven-cat.conf | https://kelee.one/Tool/Loon/Lpx/SevenCat_remove_ads.lpx |
| sf-express | 顺丰速运 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/sf-express.conf | https://kelee.one/Tool/Loon/Lpx/SF-Express_remove_ads.lpx |
| shao-shu-pai | 少数派 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/shao-shu-pai.conf | fmz200/wool_scripts raw |
| sheng-qu-games | 盛趣游戏 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/sheng-qu-games.conf | fmz200/wool_scripts raw |
| shop-keeper-admin | 小店掌柜 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/shop-keeper-admin.conf | https://kelee.one/Tool/Loon/Lpx/ShopKeeperAdmin_remove_ads.lpx |
| shou-yin-tong-merchant | 收银通商户端 | observe | high | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/shou-yin-tong-merchant.conf | https://kelee.one/Tool/Loon/Lpx/ShouYinTongMerchant_remove_ads.lpx |
| shu-qi-center-reader | 书旗小说 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/shu-qi-center-reader.conf | https://kelee.one/Tool/Loon/Lpx/ShuQiCenterReader_remove_ads.lpx |
| si-ji-xian-shang-ying-shi | 四季線上影視 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/si-ji-xian-shang-ying-shi.conf | fmz200/wool_scripts raw |
| skyworth | 创维 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/skyworth.conf | fmz200/wool_scripts raw |
| snail-sleep | 蜗牛睡眠 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/snail-sleep.conf | https://kelee.one/Tool/Loon/Lpx/SnailSleep_remove_ads.lpx |
| snapchat | Snapchat | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/snapchat.conf | fmz200/wool_scripts raw |
| snow-camera | B612咔叽 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/snow-camera.conf | https://kelee.one/Tool/Loon/Lpx/SnowCamera_remove_ads.lpx |
| snowball | 雪球 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/snowball.conf | https://kelee.one/Tool/Loon/Lpx/Snowball_remove_ads.lpx |
| soda-music | 汽水音乐 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/soda-music.conf | https://kelee.one/Tool/Loon/Lpx/SodaMusic_remove_ads.lpx |
| sogou-input | 搜狗输入法 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/sogou-input.conf | fmz200/wool_scripts raw |
| soufun | 房天下 (Soufun) | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/soufun.conf | fmz200/wool_scripts raw |
| soul | Soul | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/soul.conf | QingRex/LoonKissSurge raw |
| spotify | Spotify | observe | high | True | True | True | app2smile/rules | 未记录 | unchanged | Rewrite/Sources/Apps/spotify.conf | app2smile/rules raw |
| su-zhou-citizen-card | 智慧苏州 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/su-zhou-citizen-card.conf | https://kelee.one/Tool/Loon/Lpx/SuZhouCitizenCard_remove_ads.lpx |
| taobao | Taobao | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/taobao.conf | QingRex/LoonKissSurge raw |
| taobao-travel | 飞猪旅行 | observe | high | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/taobao-travel.conf | https://kelee.one/Tool/Loon/Lpx/TaobaoTravel_remove_ads.lpx |
| taopiaopiao | 淘票票 | observe | high | True | True | True | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/taopiaopiao.conf | https://kelee.one/Tool/Loon/Lpx/Taopiaopiao_remove_ads.lpx |
| tap-tap | TapTap | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/tap-tap.conf | fmz200/wool_scripts raw |
| taqu | 他趣 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/taqu.conf | https://kelee.one/Tool/Loon/Lpx/Taqu_remove_ads.lpx |
| tencent-games | 腾讯游戏 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/tencent-games.conf | fmz200/wool_scripts raw |
| tencent-games-community | 腾讯游戏社区 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/tencent-games-community.conf | fmz200/wool_scripts raw |
| tencent-mobile-manager | 腾讯手机管家 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/tencent-mobile-manager.conf | fmz200/wool_scripts raw |
| tencent-sports | 腾讯体育 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/tencent-sports.conf | fmz200/wool_scripts raw |
| tencent-video | 腾讯视频 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/tencent-video.conf | https://kelee.one/Tool/Loon/Lpx/Tencent_Video_remove_ads.lpx |
| terabox | TeraBox | observe | high | True | True | True | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/terabox.conf | QingRex/LoonKissSurge raw |
| the-paper-news | 澎湃新闻 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/the-paper-news.conf | fmz200/wool_scripts raw |
| tian-shan-yun-tv | 天山云TV | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/tian-shan-yun-tv.conf | fmz200/wool_scripts raw |
| tieba | Tieba | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/tieba.conf | QingRex/LoonKissSurge raw |
| tmall-genie | 天猫精灵 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/tmall-genie.conf | fmz200/wool_scripts raw |
| top-widget | Top Widgets | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/top-widget.conf | fmz200/wool_scripts raw |
| truth-social | TruthSocial | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/truth-social.conf | fmz200/wool_scripts raw |
| ttvoice | TT语音 | observe | high | True | True | True | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/ttvoice.conf | fmz200/wool_scripts raw |
| tu-guai-shou | 图怪兽 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/tu-guai-shou.conf | https://kelee.one/Tool/Loon/Lpx/TuGuaiShou_remove_ads.lpx |
| tube-max | TubeMax | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/tube-max.conf | https://kelee.one/Tool/Loon/Lpx/TubeMax_remove_ads.lpx |
| tui-lan | 推栏 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/tui-lan.conf | fmz200/wool_scripts raw |
| tumblr | Tumblr | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/tumblr.conf | https://kelee.one/Tool/Loon/Lpx/Tumblr_remove_ads.lpx |
| tv-assistant | 乐播投屏 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/tv-assistant.conf | https://kelee.one/Tool/Loon/Lpx/TV_Assistant_remove_ads.lpx |
| twitch | Twitch | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/twitch.conf | fmz200/wool_scripts raw |
| twitter | Twitter | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/twitter.conf | fmz200/wool_scripts raw |
| txdocs | 腾讯文档 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/txdocs.conf | https://kelee.one/Tool/Loon/Lpx/TXDocs_remove_ads.lpx |
| uki | Uki | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/uki.conf | https://kelee.one/Tool/Loon/Lpx/Uki_remove_ads.lpx |
| umetrip | Umetrip | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/umetrip.conf | QingRex/LoonKissSurge raw |
| valorant-bible | 掌上无畏契约 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/valorant-bible.conf | https://kelee.one/Tool/Loon/Lpx/ValorantBible_remove_ads.lpx |
| vgtime | vgTime | observe | medium | True | True | False | app2smile/rules | 未记录 | unchanged | Rewrite/Sources/Apps/vgtime.conf | app2smile/rules raw |
| video-go | 萤石云视频 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/video-go.conf | https://kelee.one/Tool/Loon/Lpx/VideoGo_remove_ads.lpx |
| wa-cai-ji-zhang | 挖财记账 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/wa-cai-ji-zhang.conf | https://kelee.one/Tool/Loon/Lpx/WaCaiJiZhang_remove_ads.lpx |
| wall-street-cn | 华尔街见闻 | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/wall-street-cn.conf | fmz200/wool_scripts raw |
| walmart | 沃尔玛 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/walmart.conf | https://kelee.one/Tool/Loon/Lpx/Walmart_remove_ads.lpx |
| wasu-tv | 华数TV | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/wasu-tv.conf | fmz200/wool_scripts raw |
| wechat | WeChat | observe | high | True | True | True | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/wechat.conf | QingRex/LoonKissSurge raw |
| wechat-mini-programs | 微信小程序 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/wechat-mini-programs.conf | https://kelee.one/Tool/Loon/Lpx/WexinMiniPrograms_Remove_ads.lpx |
| wechat-official-accounts | 微信公众号 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/wechat-official-accounts.conf | https://kelee.one/Tool/Loon/Lpx/Weixin_Official_Accounts_remove_ads.lpx |
| weibo | Weibo | observe | high | True | True | True | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/weibo.conf | QingRex/LoonKissSurge raw |
| weibo-intl | 微博轻享版 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/weibo-intl.conf | https://kelee.one/Tool/Loon/Lpx/Weibo_intl_remove_ads.lpx |
| weimai | 微脉圈 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/weimai.conf | https://kelee.one/Tool/Loon/Lpx/Weimai_remove_ads.lpx |
| weread | WeRead | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/weread.conf | QingRex/LoonKissSurge raw |
| wpforum | 威锋 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/wpforum.conf | https://kelee.one/Tool/Loon/Lpx/WPForum_remove_ads.lpx |
| wps | WPS | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/wps.conf | https://kelee.one/Tool/Loon/Lpx/WPS_Documents_remove_ads.lpx |
| wuta-camera | 无他相机 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/wuta-camera.conf | https://kelee.one/Tool/Loon/Lpx/WutaCamera_remove_ads.lpx |
| xfuse | 磁力宅播放器 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/xfuse.conf | https://kelee.one/Tool/Loon/Lpx/XFuse_remove_ads.lpx |
| xia-chu-fang | 下厨房 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/xia-chu-fang.conf | https://kelee.one/Tool/Loon/Lpx/XiaChuFang_remove_ads.lpx |
| xiao-can | 小蚕霸王餐 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/xiao-can.conf | https://kelee.one/Tool/Loon/Lpx/XiaoCan_remove_ads.lpx |
| xiao-hei-he | 小黑盒 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/xiao-hei-he.conf | https://kelee.one/Tool/Loon/Lpx/XiaoHeiHe_remove_ads.lpx |
| xiaojukeji-charge | 小桔充电 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/xiaojukeji-charge.conf | https://kelee.one/Tool/Loon/Lpx/XiaojukejiCharge_remove_ads.lpx |
| xiaomi-speaker | 小米音箱 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/xiaomi-speaker.conf | https://kelee.one/Tool/Loon/Lpx/XiaomiSpeaker_remove_ads.lpx |
| xiaopeng | Xiaopeng | reference_only | medium | False | False | False | unknown | 未记录 | missing-upstream-source | Rewrite/Sources/Apps/xiaopeng.conf |  |
| xiaoyuzhou | Xiaoyuzhou | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/xiaoyuzhou.conf | QingRex/LoonKissSurge raw |
| ximalaya | Ximalaya | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/ximalaya.conf | QingRex/LoonKissSurge raw |
| xun-lei | 迅雷 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/xun-lei.conf | https://kelee.one/Tool/Loon/Lpx/XunLei_remove_ads.lpx |
| yahoo | Yahoo | observe | medium | True | True | False | fmz200/wool_scripts | 未记录 | unchanged | Rewrite/Sources/Apps/yahoo.conf | fmz200/wool_scripts raw |
| yi-kao-bang | 医考帮 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/yi-kao-bang.conf | https://kelee.one/Tool/Loon/Lpx/YiKaoBang_remove_ads.lpx |
| yiche | Yiche | reference_only | medium | False | False | False | unknown | 未记录 | missing-upstream-source | Rewrite/Sources/Apps/yiche.conf |  |
| yitian | 一甜相机 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/yitian.conf | https://kelee.one/Tool/Loon/Lpx/Yitian_remove_ads.lpx |
| youdao-dict | 网易有道词典 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/youdao-dict.conf | https://kelee.one/Tool/Loon/Lpx/YoudaoDict_remove_ads.lpx |
| youdao-note | 有道云笔记 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/youdao-note.conf | https://kelee.one/Tool/Loon/Lpx/YoudaoNote_remove_ads.lpx |
| youdao-trans | 有道翻译官 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/youdao-trans.conf | https://kelee.one/Tool/Loon/Lpx/YoudaoTrans_remove_ads.lpx |
| youku | Youku | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/youku.conf | QingRex/LoonKissSurge raw |
| youtube | YouTube | reference_only | high | False | False | True | Maasea/sgmodule | 未记录 | remote-script-only | Rewrite/Sources/Apps/youtube.conf | Maasea/sgmodule raw |
| yue-dan-ba | 省钱快报 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/yue-dan-ba.conf | https://kelee.one/Tool/Loon/Lpx/YueDanBa_remove_ads.lpx |
| yueyou | 阅友 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/yueyou.conf | https://kelee.one/Tool/Loon/Lpx/Yueyou_remove_ads.lpx |
| yy-voice | YY | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/yy-voice.conf | https://kelee.one/Tool/Loon/Lpx/YY_Voice_remove_ads.lpx |
| yyvoice-tool | YY语音 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/yyvoice-tool.conf | https://kelee.one/Tool/Loon/Lpx/YYVoiceTool_remove_ads.lpx |
| zaker | ZAKER | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/zaker.conf | https://kelee.one/Tool/Loon/Lpx/ZAKER_remove_ads.lpx |
| zdm | ZDM | observe | medium | True | True | False | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/zdm.conf | QingRex/LoonKissSurge raw |
| zhi-lian-zhao-pin | 智联招聘 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/zhi-lian-zhao-pin.conf | https://kelee.one/Tool/Loon/Lpx/ZhiLianZhaoPin_remove_ads.lpx |
| zhihu | Zhihu | observe | high | True | True | True | QingRex/LoonKissSurge | 未记录 | unchanged | Rewrite/Sources/Apps/zhihu.conf | QingRex/LoonKissSurge raw |
| zhuan-zhuan | 转转 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/zhuan-zhuan.conf | https://kelee.one/Tool/Loon/Lpx/ZhuanZhuan_remove_ads.lpx |
| zong-heng | 纵横小说 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/zong-heng.conf | https://kelee.one/Tool/Loon/Lpx/ZongHeng_remove_ads.lpx |
| zui-you | 最右 | observe | medium | True | True | False | Kelee PluginHub | 未记录 | unchanged | Rewrite/Sources/Apps/zui-you.conf | https://kelee.one/Tool/Loon/Lpx/ZuiYou_remove_ads.lpx |
| zuoyebang | Zuoyebang | reference_only | medium | False | False | False | unknown | 未记录 | missing-upstream-source | Rewrite/Sources/Apps/zuoyebang.conf |  |

## 远程规则与参考模块台账

| kind | name | tier | enabled | protected | type | policy | upstream_project | license | purpose | url |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rule_set | blackmatrix7 Advertising | trusted | True | True | RULE-SET | REJECT | blackmatrix7/ios_rule_script | 未记录 | general advertising rules | blackmatrix7/ios_rule_script raw |
| rule_set | Cats-Team AdRules | trusted | True | True | DOMAIN-SET | REJECT | Cats-Team/AdRules | 未记录 | domain advertising rules | Cats-Team/AdRules raw |
| rule_set | anti-AD Surge | observe | True | False | DOMAIN-SET | REJECT | privacy-protection-tools/anti-AD | 未记录 | domain-set advertising supplement | privacy-protection-tools/anti-AD raw |
| rule_set | ACL4SSR BanAD | observe | True | False | RULE-SET | REJECT | ACL4SSR/ACL4SSR | 未记录 | advertising supplement | ACL4SSR/ACL4SSR raw |
| rule_set | Loyalsoldier reject | observe | True | False | DOMAIN-SET | REJECT | Loyalsoldier/surge-rules | 未记录 | domain-set advertising supplement | Loyalsoldier/surge-rules raw |
| rule_set | 217heidai adblockfilters | observe | True | False | DOMAIN-SET | REJECT | 217heidai/adblockfilters | 未记录 | domain-set advertising supplement | 217heidai/adblockfilters raw |
| rule_set | blackmatrix7 Advertising Lite | observe | True | False | RULE-SET | REJECT | blackmatrix7/ios_rule_script | 未记录 | trusted same-upstream advertising candidate enabled for conservative collection | blackmatrix7/ios_rule_script raw |
| rule_set | blackmatrix7 Hijacking | observe | True | False | RULE-SET | REJECT | blackmatrix7/ios_rule_script | 未记录 | trusted anti-hijacking rule candidate enabled for conservative collection | blackmatrix7/ios_rule_script raw |
| rule_set | blackmatrix7 Privacy | observe | True | False | RULE-SET | REJECT | blackmatrix7/ios_rule_script | 未记录 | trusted privacy and tracker rule candidate enabled for conservative collection | blackmatrix7/ios_rule_script raw |
| rule_set | ACL4SSR BanProgramAD | observe | True | False | RULE-SET | REJECT | ACL4SSR/ACL4SSR | 未记录 | trusted program advertising rule candidate enabled for conservative collection | ACL4SSR/ACL4SSR raw |
| rule_set | ACL4SSR BanEasyListChina | observe | True | False | RULE-SET | REJECT | ACL4SSR/ACL4SSR | 未记录 | trusted China advertising supplement enabled for conservative collection | ACL4SSR/ACL4SSR raw |
| rule_set | blackmatrix7 Advertising MiTV | observe | True | False | RULE-SET | REJECT | blackmatrix7/ios_rule_script | 未记录 | trusted TV advertising rule enabled for conservative collection | blackmatrix7/ios_rule_script raw |
| rule_set | zirawell App AdBlock aggressive | reference_only | False | False | RULE-SET | REJECT | zirawell/R-Store | 未记录 | disabled in default remotes; use Rules/aggressive-ad-sources.list through testing profiles only | zirawell/R-Store raw |
| rule_set | zirawell All AdBlock aggressive | reference_only | False | False | RULE-SET | REJECT | zirawell/R-Store | 未记录 | disabled in default remotes; use Rules/aggressive-ad-sources.list through testing profiles only | zirawell/R-Store raw |
| rule_set | ACL4SSR BanEasyList | observe | True | False | RULE-SET | REJECT | ACL4SSR/ACL4SSR | 未记录 | trusted EasyList advertising supplement enabled for conservative collection | ACL4SSR/ACL4SSR raw |
| rule_set | ACL4SSR BanEasyPrivacy | observe | True | False | RULE-SET | REJECT | ACL4SSR/ACL4SSR | 未记录 | trusted EasyPrivacy tracker supplement enabled for conservative collection | ACL4SSR/ACL4SSR raw |
| reference_module | app2smile Spotify module | reference_only | False | True | module | reference | app2smile/rules | 未记录 | reference/source for Spotify app module; synced through Rewrite/Remotes/app-modules.json | app2smile/rules raw |
| reference_module | app2smile Qidian module | reference_only | False | True | module | reference | app2smile/rules | 未记录 | reference only; extract source-first into Stable Plus after manual review | app2smile/rules raw |
| reference_module | app2smile Bilibili module | reference_only | False | True | module | reference | app2smile/rules | 未记录 | reference only; extract source-first into Stable Plus after manual review | app2smile/rules raw |
| reference_module | app2smile Tieba module | reference_only | False | True | module | reference | app2smile/rules | 未记录 | reference only; extract source-first into Stable Plus after manual review | app2smile/rules raw |
| reference_module | app2smile QQ News module | reference_only | False | True | module | reference | app2smile/rules | 未记录 | reference only; extract source-first into Stable Plus after manual review | app2smile/rules raw |
| reference_module | app2smile VGTime module | reference_only | False | True | module | reference | app2smile/rules | 未记录 | reference only; extract source-first into Stable Plus after manual review | app2smile/rules raw |
| reference_module | app2smile YouTube module | reference_only | False | True | module | reference | app2smile/rules | 未记录 | reference only; never replace existing YouTube core entries without manual testing | app2smile/rules raw |
| reference_module | app2smile Zhihu module | reference_only | False | True | module | reference | app2smile/rules | 未记录 | reference only; never replace existing Zhihu entries without manual testing | app2smile/rules raw |
| reference_module | app2smile Baidu Map module | reference_only | False | True | module | reference | app2smile/rules | 未记录 | reference only; extract source-first into Stable Plus after manual review | app2smile/rules raw |
| reference_module | app2smile Adsense module | reference_only | False | True | module | reference | app2smile/rules | 未记录 | reference only; extract source-first into Stable Plus after manual review | app2smile/rules raw |
| reference_module | app2smile Baidu no redirect module | reference_only | False | True | module | reference | app2smile/rules | 未记录 | reference only; redirect behavior must be manually reviewed before activation | app2smile/rules raw |
| reference_module | Maasea sgmodule | reference_only | False | True | module | reference | Maasea/sgmodule | 未记录 | YouTube Enhance reference source | https://github.com/Maasea/sgmodule |
| reference_module | zirawell Taobao module | reference_only | False | False | module | reference | zirawell/R-Store | 未记录 | reference for Taobao aggressive source-first extraction | zirawell/R-Store raw |
| reference_module | zirawell JD module | reference_only | False | False | module | reference | zirawell/R-Store | 未记录 | reference for JD aggressive source-first extraction | zirawell/R-Store raw |
| reference_module | zirawell Pinduoduo module | reference_only | False | False | module | reference | zirawell/R-Store | 未记录 | reference for Pinduoduo aggressive source-first extraction | zirawell/R-Store raw |
| reference_module | zirawell Xiaohongshu module | reference_only | False | False | module | reference | zirawell/R-Store | 未记录 | reference for Xiaohongshu aggressive source-first extraction | zirawell/R-Store raw |
| reference_module | zirawell Zhihu module | reference_only | False | False | module | reference | zirawell/R-Store | 未记录 | reference for Zhihu aggressive source-first extraction | zirawell/R-Store raw |
| reference_module | fmz200 Taobao module | reference_only | False | False | module | reference | fmz200/wool_scripts | 未记录 | secondary Taobao reference for comparison | fmz200/wool_scripts raw |
| reference_module | fmz200 JD module | reference_only | False | False | module | reference | fmz200/wool_scripts | 未记录 | secondary JD reference for comparison | fmz200/wool_scripts raw |
| reference_module | fmz200 Pinduoduo module | reference_only | False | False | module | reference | fmz200/wool_scripts | 未记录 | secondary Pinduoduo reference for comparison | fmz200/wool_scripts raw |
| reference_module | fmz200 Bilibili module | reference_only | False | False | module | reference | fmz200/wool_scripts | 未记录 | secondary Bilibili reference for comparison | fmz200/wool_scripts raw |
| reference_module | fmz200 Xiaohongshu module | reference_only | False | False | module | reference | fmz200/wool_scripts | 未记录 | secondary Xiaohongshu reference for comparison | fmz200/wool_scripts raw |
| reference_module | fmz200 Zhihu module | reference_only | False | False | module | reference | fmz200/wool_scripts | 未记录 | secondary Zhihu reference for comparison | fmz200/wool_scripts raw |
| reference_module | zirawell App AdBlock module | reference_only | False | False | module | reference | zirawell/R-Store | 未记录 | broad aggressive app ad block module reference for domestic app residual ads | zirawell/R-Store raw |

## 维护要求

- 新增直接同步 App 前，必须能在本报告中看到 `source_url`、`risk`、`backup`、`direct_commit` 和上游项目。
- `license = 未记录` 不会阻断构建，但公开使用前应优先补来源许可或在文档中说明未知。
- `observe` 不是错误；它表示需要保留备份、风险说明和回滚路径。
- `blocked` 记录不得绕过风险门禁加入正式模块。
