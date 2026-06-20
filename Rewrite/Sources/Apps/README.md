# Rewrite Sources / Apps

This directory stores app-scoped source fragments used by the module factory. Current active app source files: **398**. `_TEMPLATE.conf` is a local authoring template and is not generated as an app module.

`Release/Modules/*.sgmodule` is generated from these files by `scripts/build_release_modules.py`. Do not edit generated files under `Release/Modules/` as the source of truth.

## Build behavior

1. Manual module specs are read from `Rewrite/Generate.conf` `[release_modules]`.
2. `Rewrite/Sources/Apps/*.conf` is scanned after manual specs are loaded.
3. If `<slug>.conf` is not manually registered, it is auto-discovered and generated with conservative keywords.
4. If a source file is missing for a manual spec, the builder falls back to extracting matching lines from `Release/Ronghemokuai.sgmodule`.
5. Empty modules are skipped unless `include_empty_modules = true` is set in `Rewrite/Generate.conf`.

## Upstream sync

- `Rewrite/Remotes/app-modules.json` records app upstream URLs and whether direct daily sync is enabled.
- `scripts/sync_upstream_app_modules.py` converts Surge/Loon/QuantumultX-style app fragments into GrandpaNiu source fragments.
- `.snippet` sources from `fmz200/wool_scripts` are supported and filtered to remove upstream example hosts before build.
- Protected login/message/CDN/video/core hosts such as `apd-pcdnwxlogin`, `msync-im`, `ossgw.alicdn.com`, `dcapps.disney.go.com`, and `seavideo-ak.espn.go.com` are filtered out when imported as REJECT or forced MITM entries.
- Do not add VIP unlock, payment bypass, login bypass, bank/payment rewrites, token/cookie rewriting, or account sharing modules.
- Broad platform candidates such as Adobe activation/licensing, Apple/Google Safe Browsing, Microsoft CRL, and Amazon AWS core service rules must stay out unless there is a targeted risk review.

## Active app source files

| Slug | Display | Sync | Registration |
|---|---|---|---|
| 123-net-work-disk | 123云盘 | auto: Kelee PluginHub | auto-discovered |
| 12306 | 12306 | auto: Kelee PluginHub | auto-discovered |
| 123pan | 123Pan | auto: QingRex/LoonKissSurge | auto-discovered |
| 17173-game | 17173（网络游戏门户网站） | auto: fmz200/wool_scripts | auto-discovered |
| 178-game | 178游戏网 | auto: fmz200/wool_scripts | auto-discovered |
| 18183-game | 18183游戏网 | auto: fmz200/wool_scripts | auto-discovered |
| 1905-movie-network | 1905电影网 | auto: fmz200/wool_scripts | auto-discovered |
| 21-economic-net | 21经济网 | auto: fmz200/wool_scripts | auto-discovered |
| 2345-weather-king | 2345天气王 | auto: fmz200/wool_scripts | auto-discovered |
| 2345-web-navigation | 2345网址导航 | auto: fmz200/wool_scripts | auto-discovered |
| 2bulu | 两步路户外助手 | auto: Kelee PluginHub | auto-discovered |
| 36-kr | 36氪 | auto: Kelee PluginHub | auto-discovered |
| 360-child-guard | 360儿童卫士 | auto: fmz200/wool_scripts | auto-discovered |
| 360-smart-camera | 360摄像机 | auto: Kelee PluginHub | auto-discovered |
| 365-calendar | 365日历 | auto: fmz200/wool_scripts | auto-discovered |
| 39-health | 39健康网 | auto: fmz200/wool_scripts | auto-discovered |
| 51-cto | 51CTO学堂 | auto: fmz200/wool_scripts | auto-discovered |
| 51-job | 前程无忧 | auto: Kelee PluginHub | auto-discovered |
| 555-dy | 555电影 | auto: Kelee PluginHub | auto-discovered |
| 58-auto | 58汽车 | auto: fmz200/wool_scripts | auto-discovered |
| 58-tong-cheng | 58同城 | auto: fmz200/wool_scripts | auto-discovered |
| 9-game | 九游 | auto: fmz200/wool_scripts | auto-discovered |
| 91160 | 健康160 | auto: Kelee PluginHub | auto-discovered |
| acfun | AcFun | auto: fmz200/wool_scripts | auto-discovered |
| ai-mei-ju | 爱美剧 | auto: fmz200/wool_scripts | auto-discovered |
| ai-pai | 爱拍 | auto: fmz200/wool_scripts | auto-discovered |
| ai-si-assistant | 爱思助手 | auto: fmz200/wool_scripts | auto-discovered |
| ai-yue-shu-xiang | 爱阅书香 | auto: fmz200/wool_scripts | auto-discovered |
| aiinquiry | 爱企查 | auto: Kelee PluginHub | auto-discovered |
| ali-yun-drive | 阿里云盘 | auto: Kelee PluginHub | auto-discovered |
| all-football | 懂球帝 | auto: fmz200/wool_scripts | auto-discovered |
| amap | Amap | auto: QingRex/LoonKissSurge | auto-discovered |
| aol | AOL | auto: fmz200/wool_scripts | auto-discovered |
| appso | AppSo | auto: fmz200/wool_scripts | auto-discovered |
| auto-home | 汽车之家 | auto: Kelee PluginHub | auto-discovered |
| baby-tree | 宝宝树孕育 | auto: Kelee PluginHub | auto-discovered |
| baby-tree-parenting | 宝宝树孕育 | auto: fmz200/wool_scripts | auto-discovered |
| bahamut-anime | Bahamut Anime | auto: NobyDa/Script | auto-discovered |
| baicizhan | 百词斩 | auto: fmz200/wool_scripts | auto-discovered |
| baidu | Baidu | auto: QingRex/LoonKissSurge | auto-discovered |
| baidu-input-method | 百度输入法 | auto: Kelee PluginHub | auto-discovered |
| baidu-map | 百度地图 | auto: Kelee PluginHub | auto-discovered |
| baidu-net-disk | 百度网盘 | auto: Kelee PluginHub | auto-discovered |
| baidu-photo | 一刻相册 | auto: Kelee PluginHub | auto-discovered |
| baidu-translation | 百度翻译 | auto: fmz200/wool_scripts | auto-discovered |
| baidu-wenku | Baidu Wenku | auto: QingRex/LoonKissSurge | auto-discovered |
| baidupan | BaiduPan | auto: QingRex/LoonKissSurge | auto-discovered |
| baixing | 百姓网 | auto: fmz200/wool_scripts | auto-discovered |
| ban-yue-tan | 半月谈 | auto: fmz200/wool_scripts | auto-discovered |
| bao-mi-hua | 爆米花 | auto: fmz200/wool_scripts | auto-discovered |
| baofeng-player | 暴风影音 | auto: fmz200/wool_scripts | auto-discovered |
| bbc | BBC | auto: fmz200/wool_scripts | auto-discovered |
| beike | 贝壳找房 | auto: Kelee PluginHub | auto-discovered |
| betty-kitchen | 贝太厨房 | auto: fmz200/wool_scripts | auto-discovered |
| bilibili | Bilibili Strong | auto: kokoryh/Sparkle | manual |
| bilibili-comic | 哔哩哔哩漫画 | auto: Kelee PluginHub | auto-discovered |
| bing | Bing | auto: fmz200/wool_scripts | auto-discovered |
| biquge | 笔趣阁 | auto: fmz200/wool_scripts | auto-discovered |
| bitqiu-pan | 比特球云盘 | auto: Kelee PluginHub | auto-discovered |
| blued | Blued | auto: fmz200/wool_scripts | auto-discovered |
| bo-luo-bao-light-novel | 菠萝包轻小说 | auto: fmz200/wool_scripts | auto-discovered |
| bodian-music | 波点音乐 | auto: Kelee PluginHub | auto-discovered |
| boo-hee | 薄荷健康 | auto: Kelee PluginHub | auto-discovered |
| cai-jing-za-zhi | 财经杂志 | auto: fmz200/wool_scripts | auto-discovered |
| cai-lian-she | 财联社 | auto: fmz200/wool_scripts | auto-discovered |
| cainiao | Cainiao | auto: QingRex/LoonKissSurge | auto-discovered |
| caixin-media | 财新 | auto: Kelee PluginHub | auto-discovered |
| caiyun-weather | Caiyun Weather | auto: QingRex/LoonKissSurge | auto-discovered |
| camera360 | Camera360 | auto: fmz200/wool_scripts | auto-discovered |
| cat-ear-fm | 猫耳FM | auto: Kelee PluginHub | auto-discovered |
| cclive | CC直播 | auto: Kelee PluginHub | auto-discovered |
| cece | 测测 | auto: Kelee PluginHub | auto-discovered |
| chao-ji-ke-cheng-biao | 超级课程表 | auto: fmz200/wool_scripts | auto-discovered |
| chao-xing-xue-xi-tong | 超星学习通 | auto: fmz200/wool_scripts | auto-discovered |
| che-lai-le | 车来了 | auto: fmz200/wool_scripts | auto-discovered |
| cheng-fen-miao | 成分喵 | auto: Kelee PluginHub | auto-discovered |
| china-unicom | China Unicom | auto: QingRex/LoonKissSurge | auto-discovered |
| chuzhan | 触站 | auto: Kelee PluginHub | auto-discovered |
| ci-wei-mao-yue-du | 刺猬猫阅读 | auto: fmz200/wool_scripts | auto-discovered |
| clicli | clicli | auto: fmz200/wool_scripts | auto-discovered |
| cnn | CNN | auto: fmz200/wool_scripts | auto-discovered |
| cool-apk | 酷安 | auto: Kelee PluginHub | auto-discovered |
| coolapk | 酷安 | auto: fmz200/wool_scripts | auto-discovered |
| crunchyroll | crunchyroll | auto: fmz200/wool_scripts | auto-discovered |
| csdn | CSDN | auto: fmz200/wool_scripts | auto-discovered |
| csg | 南网在线 | auto: Kelee PluginHub | auto-discovered |
| da-shi-xiong | 大师兄 | auto: fmz200/wool_scripts | auto-discovered |
| daily | 推栏 | auto: Kelee PluginHub | auto-discovered |
| damai | 大麦 | auto: Kelee PluginHub | auto-discovered |
| dang-dang | 当当网 | auto: fmz200/wool_scripts | auto-discovered |
| dang-dang-reading | 当当阅读 | auto: fmz200/wool_scripts | auto-discovered |
| dao-meng-kong-jian | 到梦空间 | auto: fmz200/wool_scripts | auto-discovered |
| dewu | 得物 | auto: Kelee PluginHub | auto-discovered |
| di-di | 滴滴出行 | auto: Kelee PluginHub | auto-discovered |
| di-duan-ying-shi | 低端影视 | auto: fmz200/wool_scripts | auto-discovered |
| dian-shi-jia | 电视家 | auto: fmz200/wool_scripts | auto-discovered |
| dida-pinche-taxi | 滴答出行 | auto: Kelee PluginHub | auto-discovered |
| didi | Didi | auto: QingRex/LoonKissSurge | auto-discovered |
| digital-heartbeat | 数字心动 | auto: Kelee PluginHub | auto-discovered |
| ding-xiang-doctor | 丁香医生 | auto: fmz200/wool_scripts | auto-discovered |
| ding-xiang-yuan | 丁香园 | auto: fmz200/wool_scripts | auto-discovered |
| dingdong-maicai | 叮咚买菜 | auto: Kelee PluginHub | auto-discovered |
| dlabel | Dlabel云标签 | auto: Kelee PluginHub | auto-discovered |
| dlabel-cloud-tag | DLabel云标签 | auto: fmz200/wool_scripts | auto-discovered |
| dong-hua-feng | 动画疯 | auto: fmz200/wool_scripts | auto-discovered |
| dou-ban | 豆瓣 | auto: Kelee PluginHub | auto-discovered |
| douban-read | 豆瓣阅读 | auto: Kelee PluginHub | auto-discovered |
| douyin | 抖音 | auto: fmz200/wool_scripts | auto-discovered |
| douyu | 斗鱼 | auto: Kelee PluginHub | auto-discovered |
| dragon-read | 番茄小说 | auto: Kelee PluginHub | auto-discovered |
| dreame | DREAME | auto: Kelee PluginHub | auto-discovered |
| dubbing-show | 配音秀 | auto: Kelee PluginHub | auto-discovered |
| dui-tang | 堆糖 | auto: Kelee PluginHub | auto-discovered |
| eastday | 东方网 | auto: fmz200/wool_scripts | auto-discovered |
| ecovacs-home | ECOVACS HOME | auto: Kelee PluginHub | auto-discovered |
| etouch-ecalendar | 中华万年历 | auto: Kelee PluginHub | auto-discovered |
| facebook | Facebook | auto: fmz200/wool_scripts | auto-discovered |
| fan-deng-reading | 樊登读书 | auto: fmz200/wool_scripts | auto-discovered |
| fan-qie-novel | 番茄小说 | auto: fmz200/wool_scripts | auto-discovered |
| fc-box | 丰巢 | auto: Kelee PluginHub | auto-discovered |
| fei-ke-cha-guan | 飞客茶馆 | auto: fmz200/wool_scripts | auto-discovered |
| fen-bi | 粉笔 | auto: Kelee PluginHub | auto-discovered |
| feng-huang-xiu | 凤凰秀 | auto: fmz200/wool_scripts | auto-discovered |
| ferris-wheel | 摩天轮 | auto: Kelee PluginHub | auto-discovered |
| finance-news | 华尔街见闻 | auto: Kelee PluginHub | auto-discovered |
| flea-market | 闲鱼 | auto: Kelee PluginHub | auto-discovered |
| flightradar24 | Flightradar24 | auto: fmz200/wool_scripts | auto-discovered |
| flyer-tea | 飞客 | auto: Kelee PluginHub | auto-discovered |
| foodie | Foodie | auto: Kelee PluginHub | auto-discovered |
| funshion | 风行网 | auto: fmz200/wool_scripts | auto-discovered |
| ganji | 赶集网 | auto: fmz200/wool_scripts | auto-discovered |
| gao-ding | 稿定设计 | auto: Kelee PluginHub | auto-discovered |
| go-com | Go.com | auto: fmz200/wool_scripts | auto-discovered |
| gong-kao-lei-da | 公考雷达 | auto: fmz200/wool_scripts | auto-discovered |
| goofish | Goofish | auto: QingRex/LoonKissSurge | auto-discovered |
| guide-rank | 盖得排行 | auto: Kelee PluginHub | auto-discovered |
| hanju-tv | 韩剧TV | auto: fmz200/wool_scripts | auto-discovered |
| hanting-hotels | 华住会 | auto: Kelee PluginHub | auto-discovered |
| hao-hao-zhu | 好好住 | auto: fmz200/wool_scripts | auto-discovered |
| hao-qi-xin-daily | 好奇心日报 | auto: fmz200/wool_scripts | auto-discovered |
| hao-you-kuai-bao | 好游快爆 | auto: fmz200/wool_scripts | auto-discovered |
| hao123 | Hao123 | auto: fmz200/wool_scripts | auto-discovered |
| he-feng-weather | 和风天气 | auto: fmz200/wool_scripts | auto-discovered |
| heartide-brain-wave | 小睡眠 | auto: Kelee PluginHub | auto-discovered |
| hkdou-yin | 香港抖音 | auto: Kelee PluginHub | auto-discovered |
| hong-ban-bao | 红版报 | auto: fmz200/wool_scripts | auto-discovered |
| hua-sheng-di-tie | 花生地铁 | auto: fmz200/wool_scripts | auto-discovered |
| huang-you-xiang-ji | 黄油相机 | auto: fmz200/wool_scripts | auto-discovered |
| hujiang-online-school | 沪江网校 | auto: fmz200/wool_scripts | auto-discovered |
| huo-mao | 火猫 | auto: fmz200/wool_scripts | auto-discovered |
| hupu | 虎扑 | auto: Kelee PluginHub | auto-discovered |
| huxiu | 虎嗅 | auto: Kelee PluginHub | auto-discovered |
| huya | Huya | disabled | manual |
| i-mai-cai | 小象超市 | auto: Kelee PluginHub | auto-discovered |
| i-qi-yi-video | 爱奇艺 | auto: Kelee PluginHub | auto-discovered |
| i-reader | 掌阅 | auto: Kelee PluginHub | auto-discovered |
| i-reader-dejian | 得间小说 | auto: Kelee PluginHub | auto-discovered |
| ithome | IT Home | auto: QingRex/LoonKissSurge | auto-discovered |
| jd | JD | auto: QingRex/LoonKissSurge | manual |
| jdreading | 京东读书 | auto: fmz200/wool_scripts | auto-discovered |
| jdwaimai | 京东外卖 | auto: Kelee PluginHub | auto-discovered |
| ji-he-wang | 机核网 | auto: fmz200/wool_scripts | auto-discovered |
| jia-kao-bao-dian | 驾考宝典 | auto: Kelee PluginHub | auto-discovered |
| jia-xiao-drive | 驾校一点通 | auto: Kelee PluginHub | auto-discovered |
| jia-xiao-yi-dian-tong | 驾校一点通 | auto: fmz200/wool_scripts | auto-discovered |
| jian-xun | 简讯 | auto: fmz200/wool_scripts | auto-discovered |
| jie-mian-news | 界面新闻 | auto: fmz200/wool_scripts | auto-discovered |
| jin-ri-shui-yin-camera | 今日水印相机 | auto: fmz200/wool_scripts | auto-discovered |
| jump | Jump | auto: Kelee PluginHub | auto-discovered |
| kan-dong-fang | 看东方（百视TV） | auto: fmz200/wool_scripts | auto-discovered |
| kan-li-xiang | 看理想 | auto: fmz200/wool_scripts | auto-discovered |
| kan-tian-xia | 看天下 | auto: fmz200/wool_scripts | auto-discovered |
| kebida-dushu | 帆书 | auto: Kelee PluginHub | auto-discovered |
| keep | Keep | auto: QingRex/LoonKissSurge | auto-discovered |
| kfc | 肯德基 | auto: fmz200/wool_scripts | auto-discovered |
| kgring | 酷狗铃声 | auto: Kelee PluginHub | auto-discovered |
| kingdee-my-money | 随手记 | auto: Kelee PluginHub | auto-discovered |
| kingsoft-power-word | 金山词霸 | auto: fmz200/wool_scripts | auto-discovered |
| kook | KOOK | auto: Kelee PluginHub | auto-discovered |
| kou-dai-xiao-yuan | 口袋校园 | auto: fmz200/wool_scripts | auto-discovered |
| ku-gou | 酷狗音乐 | auto: Kelee PluginHub | auto-discovered |
| ku-gou-music | 酷狗音乐 | auto: fmz200/wool_scripts | auto-discovered |
| ku-gou-youth | 酷狗概念版 | auto: Kelee PluginHub | auto-discovered |
| ku6 | 酷6网 | auto: fmz200/wool_scripts | auto-discovered |
| kua-ya-zip | 快压zip | auto: fmz200/wool_scripts | auto-discovered |
| kuai-di100 | 快递100 | auto: Kelee PluginHub | auto-discovered |
| kuai-dong-baike | 快懂百科 | auto: fmz200/wool_scripts | auto-discovered |
| kuai-dui-zuo-ye | 快对 | auto: Kelee PluginHub | auto-discovered |
| kuai-kan | 快看 | auto: fmz200/wool_scripts | auto-discovered |
| kuai-kan-comic | 快看漫画 | auto: Kelee PluginHub | auto-discovered |
| kuai-le-guang-bo | 快乐广播 | auto: fmz200/wool_scripts | auto-discovered |
| kuai-shou | 快手 | auto: Kelee PluginHub | auto-discovered |
| kuaishou | 快手 | auto: fmz200/wool_scripts | auto-discovered |
| kuro-bbs | 库街区 | auto: Kelee PluginHub | auto-discovered |
| kuwo | 酷我音乐 | auto: Kelee PluginHub | auto-discovered |
| kwai-videoeditor | 快影 | auto: Kelee PluginHub | auto-discovered |
| lai-dian | 来电 | auto: fmz200/wool_scripts | auto-discovered |
| lai-feng | 来疯 | auto: fmz200/wool_scripts | auto-discovered |
| lan-jie100 | 拦截100 | auto: fmz200/wool_scripts | auto-discovered |
| lan-ren-ting-shu | 懒人听书 | auto: fmz200/wool_scripts | auto-discovered |
| le-bo-screen-cast | 乐播投屏 | auto: fmz200/wool_scripts | auto-discovered |
| le-cheng | 乐橙 | auto: fmz200/wool_scripts | auto-discovered |
| le-eco | 乐视 | auto: fmz200/wool_scripts | auto-discovered |
| leju | 乐居 | auto: fmz200/wool_scripts | auto-discovered |
| lenovo-print | 联想至像打印 | auto: fmz200/wool_scripts | auto-discovered |
| lie-pin | 猎聘 | auto: fmz200/wool_scripts | auto-discovered |
| line | Line | auto: Kelee PluginHub | auto-discovered |
| linkedin | LinkedIn | auto: fmz200/wool_scripts | auto-discovered |
| live-lab | 纷玩岛 | auto: Kelee PluginHub | auto-discovered |
| lofter | lofter | auto: fmz200/wool_scripts | auto-discovered |
| lol-bible | 掌上英雄联盟 | auto: Kelee PluginHub | auto-discovered |
| lu-ban-dao-jia | 鲁班到家用户版 | auto: fmz200/wool_scripts | auto-discovered |
| luckin-coffee | 瑞幸咖啡 | auto: Kelee PluginHub | auto-discovered |
| lv-fa-shi-ying-di | 旅法师营地 | auto: fmz200/wool_scripts | auto-discovered |
| lv-tu-sui-shen-ting | 旅途随身听 | auto: fmz200/wool_scripts | auto-discovered |
| lycos | Lycos | auto: fmz200/wool_scripts | auto-discovered |
| ma-feng-wo | 马蜂窝 | auto: Kelee PluginHub | auto-discovered |
| ma-ka-long-wan-tu | 马卡龙玩图 | auto: fmz200/wool_scripts | auto-discovered |
| ma-ma-wang-yun-yu | 妈妈网孕育 | auto: fmz200/wool_scripts | auto-discovered |
| mac-keeper | MacKeeper | auto: fmz200/wool_scripts | auto-discovered |
| mai-dui-dui | 埋堆堆 | auto: fmz200/wool_scripts | auto-discovered |
| mai-mai | 脉脉 | auto: Kelee PluginHub | auto-discovered |
| mail-master | 网易邮箱大师 | auto: Kelee PluginHub | auto-discovered |
| mama | 妈妈网 | auto: fmz200/wool_scripts | auto-discovered |
| man-hua-ren | 漫画人 | auto: fmz200/wool_scripts | auto-discovered |
| meet-you | 美柚 | auto: Kelee PluginHub | auto-discovered |
| mei-ri-jing-xuan | 每日精选 | auto: fmz200/wool_scripts | auto-discovered |
| mei-shi-jie | 美食杰 | auto: Kelee PluginHub | auto-discovered |
| mei-tu | 美图秀秀 | auto: Kelee PluginHub | auto-discovered |
| mei-yan-xiang-ji | 美颜相机 | auto: fmz200/wool_scripts | auto-discovered |
| meitu-myxj | 美颜相机 | auto: Kelee PluginHub | auto-discovered |
| meituan | Meituan | disabled | auto-discovered |
| meizhixiuxing | 美丽修行 | auto: Kelee PluginHub | auto-discovered |
| mgtv | MGTV | auto: QingRex/LoonKissSurge | manual |
| mi-ho-yo-bbs | 米游社 | auto: Kelee PluginHub | auto-discovered |
| miao-pai | 秒拍 | auto: fmz200/wool_scripts | auto-discovered |
| miao-read | 小喵看书 | auto: Kelee PluginHub | auto-discovered |
| mijia | 米家 | auto: fmz200/wool_scripts | auto-discovered |
| mix | MIX | auto: fmz200/wool_scripts | auto-discovered |
| mkz | 漫客栈 | auto: Kelee PluginHub | auto-discovered |
| mobile-clouds | 中国移动云盘 | auto: Kelee PluginHub | auto-discovered |
| moe-girl-wiki | 萌娘百科 | auto: Kelee PluginHub | auto-discovered |
| moji-weather | Moji Weather | auto: QingRex/LoonKissSurge | auto-discovered |
| mop | 猫扑 (Mop) | auto: fmz200/wool_scripts | auto-discovered |
| mr-hema | 盒马 | auto: Kelee PluginHub | auto-discovered |
| nai-fei-ying-shi | 奈菲影视 | auto: fmz200/wool_scripts | auto-discovered |
| narwel-robots | 云鲸智能 | auto: Kelee PluginHub | auto-discovered |
| naver | Naver | auto: fmz200/wool_scripts | auto-discovered |
| net-ease-godlike | 网易大神 | auto: Kelee PluginHub | auto-discovered |
| netease-mail | Netease Mail | auto: QingRex/LoonKissSurge | auto-discovered |
| netease-music | Netease Music | auto: QingRex/LoonKissSurge | manual |
| netease-news | 网易新闻 | auto: Kelee PluginHub | auto-discovered |
| new-relic | New Relic | auto: fmz200/wool_scripts | auto-discovered |
| niu-ting-ting | 牛听听 | auto: fmz200/wool_scripts | auto-discovered |
| ntplay | NTPlay | auto: fmz200/wool_scripts | auto-discovered |
| omofun | omofun | auto: fmz200/wool_scripts | auto-discovered |
| on-the-way | 行者户外 | auto: Kelee PluginHub | auto-discovered |
| one | ONE | auto: fmz200/wool_scripts | auto-discovered |
| openmultimedia | Openmultimedia | auto: fmz200/wool_scripts | auto-discovered |
| oray-sunlogin | 向日葵 | auto: Kelee PluginHub | auto-discovered |
| oschina | 开源中国 | auto: fmz200/wool_scripts | auto-discovered |
| oupeng | Oupeng (欧朋) | auto: fmz200/wool_scripts | auto-discovered |
| outfit7 | Outfit7（会说话的汤姆猫） | auto: fmz200/wool_scripts | auto-discovered |
| outlook | Outlook | auto: fmz200/wool_scripts | auto-discovered |
| oxford-ald10th | 牛津高阶词典第十版 | auto: fmz200/wool_scripts | auto-discovered |
| pangguai-life | 胖乖生活 | auto: Kelee PluginHub | auto-discovered |
| pcauto | PCAuto | disabled | manual |
| perfect-world-esport | 完美世界电竞 | auto: Kelee PluginHub | auto-discovered |
| phoenix-new-media | 凤凰新媒体 | auto: fmz200/wool_scripts | auto-discovered |
| photoable | Photoable | auto: fmz200/wool_scripts | auto-discovered |
| pi-pi-gao-xiao | 皮皮搞笑 | auto: fmz200/wool_scripts | auto-discovered |
| pi-pi-xia | 皮皮虾 | auto: Kelee PluginHub | auto-discovered |
| picc-insurance | 中国人保 | auto: Kelee PluginHub | auto-discovered |
| pinduoduo | Pinduoduo | auto: QingRex/LoonKissSurge | manual |
| pinterest | Pinterest | auto: Kelee PluginHub | auto-discovered |
| pptv | PPTV | auto: fmz200/wool_scripts | auto-discovered |
| pu-pu-mall | 朴朴超市 | auto: Kelee PluginHub | auto-discovered |
| qi-dian | 起点读书 | auto: Kelee PluginHub | auto-discovered |
| qi-shui-music | 汽水音乐 | auto: fmz200/wool_scripts | auto-discovered |
| qi-xin-bao | 启信宝 | auto: Kelee PluginHub | auto-discovered |
| qilu | 齐鲁网 | auto: fmz200/wool_scripts | auto-discovered |
| qqbrowser | QQ浏览器 | auto: fmz200/wool_scripts | auto-discovered |
| qqksong | 全民K歌 | auto: Kelee PluginHub | auto-discovered |
| qqmusic | QQ Music | auto: QingRex/LoonKissSurge | auto-discovered |
| qqnews | QQ News | disabled | manual |
| qting-fm | 蜻蜓FM | auto: Kelee PluginHub | auto-discovered |
| quan-min-ge-ge | 全民K歌 | auto: fmz200/wool_scripts | auto-discovered |
| quan-neng-browser | 全能浏览器 | auto: fmz200/wool_scripts | auto-discovered |
| quark | Quark | auto: QingRex/LoonKissSurge | auto-discovered |
| quark-scan | 夸克扫描王 | auto: Kelee PluginHub | auto-discovered |
| railway12306 | Railway 12306 | auto: QingRex/LoonKissSurge | auto-discovered |
| reddit | Reddit | auto: QingRex/LoonKissSurge | auto-discovered |
| rednote | RedNote | auto: QingRex/LoonKissSurge | manual |
| reel-short | ReelShort | auto: Kelee PluginHub | auto-discovered |
| ri-ri-zhu | 日日煮 | auto: fmz200/wool_scripts | auto-discovered |
| risk-bird | 风鸟 | auto: Kelee PluginHub | auto-discovered |
| robo-taxi | 萝卜快跑 | auto: Kelee PluginHub | auto-discovered |
| roborock | Roborock | auto: Kelee PluginHub | auto-discovered |
| rqrun | RQrun | auto: Kelee PluginHub | auto-discovered |
| safety-home | 360智慧生活 | auto: Kelee PluginHub | auto-discovered |
| san-lian-zhong-du | 三联中读 | auto: fmz200/wool_scripts | auto-discovered |
| sape | Sape | auto: fmz200/wool_scripts | auto-discovered |
| seasun-jx3 | 剑网三无界 | auto: Kelee PluginHub | auto-discovered |
| seven-cat | 七猫小说 | auto: Kelee PluginHub | auto-discovered |
| sf-express | 顺丰速运 | auto: Kelee PluginHub | auto-discovered |
| shao-shu-pai | 少数派 | auto: fmz200/wool_scripts | auto-discovered |
| sheng-qu-games | 盛趣游戏 | auto: fmz200/wool_scripts | auto-discovered |
| shop-keeper-admin | 小店掌柜 | auto: Kelee PluginHub | auto-discovered |
| shou-yin-tong-merchant | 收银通商户端 | auto: Kelee PluginHub | auto-discovered |
| shu-qi-center-reader | 书旗小说 | auto: Kelee PluginHub | auto-discovered |
| si-ji-xian-shang-ying-shi | 四季線上影視 | auto: fmz200/wool_scripts | auto-discovered |
| skyworth | 创维 | auto: fmz200/wool_scripts | auto-discovered |
| snail-sleep | 蜗牛睡眠 | auto: Kelee PluginHub | auto-discovered |
| snapchat | Snapchat | auto: fmz200/wool_scripts | auto-discovered |
| snow-camera | B612咔叽 | auto: Kelee PluginHub | auto-discovered |
| snowball | 雪球 | auto: Kelee PluginHub | auto-discovered |
| soda-music | 汽水音乐 | auto: Kelee PluginHub | auto-discovered |
| sogou-input | 搜狗输入法 | auto: fmz200/wool_scripts | auto-discovered |
| soufun | 房天下 (Soufun) | auto: fmz200/wool_scripts | auto-discovered |
| soul | Soul | auto: QingRex/LoonKissSurge | auto-discovered |
| spotify | Spotify | auto: app2smile/rules | manual |
| su-zhou-citizen-card | 智慧苏州 | auto: Kelee PluginHub | auto-discovered |
| taobao | Taobao | auto: QingRex/LoonKissSurge | manual |
| taobao-travel | 飞猪旅行 | auto: Kelee PluginHub | auto-discovered |
| taopiaopiao | 淘票票 | auto: Kelee PluginHub | auto-discovered |
| tap-tap | TapTap | auto: fmz200/wool_scripts | auto-discovered |
| taqu | 他趣 | auto: Kelee PluginHub | auto-discovered |
| tencent-games | 腾讯游戏 | auto: fmz200/wool_scripts | auto-discovered |
| tencent-games-community | 腾讯游戏社区 | auto: fmz200/wool_scripts | auto-discovered |
| tencent-mobile-manager | 腾讯手机管家 | auto: fmz200/wool_scripts | auto-discovered |
| tencent-sports | 腾讯体育 | auto: fmz200/wool_scripts | auto-discovered |
| tencent-video | 腾讯视频 | auto: Kelee PluginHub | auto-discovered |
| terabox | TeraBox | auto: QingRex/LoonKissSurge | auto-discovered |
| the-paper-news | 澎湃新闻 | auto: fmz200/wool_scripts | auto-discovered |
| tian-shan-yun-tv | 天山云TV | auto: fmz200/wool_scripts | auto-discovered |
| tieba | Tieba | auto: QingRex/LoonKissSurge | auto-discovered |
| tmall-genie | 天猫精灵 | auto: fmz200/wool_scripts | auto-discovered |
| top-widget | Top Widgets | auto: fmz200/wool_scripts | auto-discovered |
| truth-social | TruthSocial | auto: fmz200/wool_scripts | auto-discovered |
| ttvoice | TT语音 | auto: fmz200/wool_scripts | auto-discovered |
| tu-guai-shou | 图怪兽 | auto: Kelee PluginHub | auto-discovered |
| tube-max | TubeMax | auto: Kelee PluginHub | auto-discovered |
| tui-lan | 推栏 | auto: fmz200/wool_scripts | auto-discovered |
| tumblr | Tumblr | auto: Kelee PluginHub | auto-discovered |
| tv-assistant | 乐播投屏 | auto: Kelee PluginHub | auto-discovered |
| twitch | Twitch | auto: fmz200/wool_scripts | auto-discovered |
| twitter | Twitter | auto: fmz200/wool_scripts | auto-discovered |
| txdocs | 腾讯文档 | auto: Kelee PluginHub | auto-discovered |
| uki | Uki | auto: Kelee PluginHub | auto-discovered |
| umetrip | Umetrip | auto: QingRex/LoonKissSurge | manual |
| valorant-bible | 掌上无畏契约 | auto: Kelee PluginHub | auto-discovered |
| vgtime | vgTime | auto: app2smile/rules | auto-discovered |
| video-go | 萤石云视频 | auto: Kelee PluginHub | auto-discovered |
| wa-cai-ji-zhang | 挖财记账 | auto: Kelee PluginHub | auto-discovered |
| wall-street-cn | 华尔街见闻 | auto: fmz200/wool_scripts | auto-discovered |
| walmart | 沃尔玛 | auto: Kelee PluginHub | auto-discovered |
| wasu-tv | 华数TV | auto: fmz200/wool_scripts | auto-discovered |
| wechat | WeChat | auto: QingRex/LoonKissSurge | manual |
| wechat-mini-programs | 微信小程序 | auto: Kelee PluginHub | auto-discovered |
| wechat-official-accounts | 微信公众号 | auto: Kelee PluginHub | auto-discovered |
| weibo | Weibo | auto: QingRex/LoonKissSurge | manual |
| weibo-intl | 微博轻享版 | auto: Kelee PluginHub | auto-discovered |
| weimai | 微脉圈 | auto: Kelee PluginHub | auto-discovered |
| weread | WeRead | auto: QingRex/LoonKissSurge | auto-discovered |
| wpforum | 威锋 | auto: Kelee PluginHub | auto-discovered |
| wps | WPS | auto: Kelee PluginHub | auto-discovered |
| wuta-camera | 无他相机 | auto: Kelee PluginHub | auto-discovered |
| xfuse | 磁力宅播放器 | auto: Kelee PluginHub | auto-discovered |
| xia-chu-fang | 下厨房 | auto: Kelee PluginHub | auto-discovered |
| xiao-can | 小蚕霸王餐 | auto: Kelee PluginHub | auto-discovered |
| xiao-hei-he | 小黑盒 | auto: Kelee PluginHub | auto-discovered |
| xiaojukeji-charge | 小桔充电 | auto: Kelee PluginHub | auto-discovered |
| xiaomi-speaker | 小米音箱 | auto: Kelee PluginHub | auto-discovered |
| xiaopeng | Xiaopeng | disabled | manual |
| xiaoyuzhou | Xiaoyuzhou | auto: QingRex/LoonKissSurge | auto-discovered |
| ximalaya | Ximalaya | auto: QingRex/LoonKissSurge | auto-discovered |
| xun-lei | 迅雷 | auto: Kelee PluginHub | auto-discovered |
| yahoo | Yahoo | auto: fmz200/wool_scripts | auto-discovered |
| yi-kao-bang | 医考帮 | auto: Kelee PluginHub | auto-discovered |
| yiche | Yiche | disabled | manual |
| yitian | 一甜相机 | auto: Kelee PluginHub | auto-discovered |
| youdao-dict | 网易有道词典 | auto: Kelee PluginHub | auto-discovered |
| youdao-note | 有道云笔记 | auto: Kelee PluginHub | auto-discovered |
| youdao-trans | 有道翻译官 | auto: Kelee PluginHub | auto-discovered |
| youku | Youku | auto: QingRex/LoonKissSurge | auto-discovered |
| youtube | YouTube | disabled | manual |
| yue-dan-ba | 省钱快报 | auto: Kelee PluginHub | auto-discovered |
| yueyou | 阅友 | auto: Kelee PluginHub | auto-discovered |
| yy-voice | YY | auto: Kelee PluginHub | auto-discovered |
| yyvoice-tool | YY语音 | auto: Kelee PluginHub | auto-discovered |
| zaker | ZAKER | auto: Kelee PluginHub | auto-discovered |
| zdm | ZDM | auto: QingRex/LoonKissSurge | auto-discovered |
| zhi-lian-zhao-pin | 智联招聘 | auto: Kelee PluginHub | auto-discovered |
| zhihu | Zhihu | auto: QingRex/LoonKissSurge | manual |
| zhuan-zhuan | 转转 | auto: Kelee PluginHub | auto-discovered |
| zong-heng | 纵横小说 | auto: Kelee PluginHub | auto-discovered |
| zui-you | 最右 | auto: Kelee PluginHub | auto-discovered |
| zuoyebang | Zuoyebang | disabled | auto-discovered |
