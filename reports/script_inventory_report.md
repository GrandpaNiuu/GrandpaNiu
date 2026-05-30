# 脚本清单与瘦身分析报告

生成时间：2026-05-31 07:27:29 +0800

本报告只做静态分析，不删除、不合并、不禁用任何脚本。减少脚本前必须先完成真机测试和回滚准备。

## 总体统计

- 脚本入口总数：87
- 识别到的 App / 服务方向数量：24
- 重复脚本名：0
- 多入口共用同一 script-path：0

## 分类统计

- 必须独立保留：6
- 可合并候选：74
- 可改规则候选：5
- 需要人工复核：2

## 来源统计

- zirawell R-Store：67
- fmz200 wool_scripts：12
- app2smile：4
- local：2
- raw.githubusercontent.com：1
- Maasea：1

## 文件分布

- `Scripts/app-clean.conf`：82
- `Scripts/spotify.conf`：2
- `Scripts/app-cleaner-active.conf`：1
- `Scripts/youtube.conf`：1
- `Scripts/zhihu-enhance.conf`：1

## 重复脚本名

- 无

## 多入口共用同一 script-path

- 无

## 可合并候选摘要

- zirawell R-Store：61 个，可考虑进入统一 `app-cleaner.js` 的配置化处理
- fmz200 wool_scripts：12 个，可考虑进入统一 `app-cleaner.js` 的配置化处理
- app2smile：1 个，可考虑进入统一 `app-cleaner.js` 的配置化处理

## 可改规则候选摘要

- `cmp_allad_024_12306`：未识别 / 通用，不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite
- `cmp_allad_027_airchina`：未识别 / 通用，不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite
- `cmp_allad_070_sogou`：未识别 / 通用，不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite
- `cmp_allad_074_adunion`：淘宝，不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite
- `cmp_allad_075_umetrip`：未识别 / 通用，不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite

## 全量脚本清单

| 脚本名 | 位置 | App / 服务 | 类型 | requires-body | 来源 | 分类 | 原因 | pattern 摘要 | script-path |
|---|---|---|---|---|---|---|---|---|---|
| `cmp_block_084_json` | Scripts/app-clean.conf:2 | 贴吧 | http-response | 1 | app2smile | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^http(s:\/\/tiebac\|:\/\/c\.tieba)\.baidu\.com\/(c\/(s\/sync\|f\/(ad\/getSplashAd\|frs\/(page` | `https://raw.githubusercontent.com/app2smile/rules/master/js/tieba-json.js` |
| `cmp_block_085_proto` | Scripts/app-clean.conf:3 | 贴吧 | http-response | 1 | app2smile | 必须独立保留 | 二进制 body / protobuf 类处理，不能简单合并 | `^http(s:\/\/tiebac\|:\/\/c\.tieba)\.baidu\.com\/c\/(b\/ad\/adBid\|f\/(frs\/(page\|threadlist\|` | `https://raw.githubusercontent.com/app2smile/rules/master/js/tieba-proto.js` |
| `cmp_allad_001_weibo` | Scripts/app-clean.conf:4 | 微博 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/api\.weibo\.cn\/2\/groups\/allgroups\/v2\?` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/weibo.js` |
| `cmp_allad_003_keep` | Scripts/app-clean.conf:5 | Keep | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/api\.gotokeep\.com\/nuocha\/course\/v\d/\w+\/preview` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/keep.js` |
| `cmp_allad_004_soul` | Scripts/app-clean.conf:6 | Soul | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/gateway-mobile-gray\.soulapp\.cn\/mobile\/app\/version\/queryIos` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/soul.js` |
| `cmp_allad_005_mgtv` | Scripts/app-clean.conf:7 | 芒果 TV | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/mob-st\.bz\.mgtv\.com\/odin\/c\d\/channel\/index\?` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/cntv.js` |
| `cmp_allad_006_tflj` | Scripts/app-clean.conf:8 | 铁路/出行类 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/tf02\.istrongcloud\.com\/member\/v[0-9.]+\/home` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/tflj.js` |
| `cmp_allad_007_cotti` | Scripts/app-clean.conf:9 | 库迪咖啡 | http-request | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/gateway\.cotticoffee\.com\/cotti-capi\/customer\/position\/list$` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/cotti.js` |
| `cmp_allad_012_dushu365` | Scripts/app-clean.conf:10 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/g(.*)\.dushu365\.com\/task-orchestration\/taskCenter\/api\/v101\/taskList` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/dushu365.js` |
| `cmp_allad_017_xiaohongshu` | Scripts/app-clean.conf:11 | 小红书 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/edith\.xiaohongshu\.com\/api\/sns\/v\d+\/interaction\/comment\/video\/download` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xiaohongshu.js` |
| `cmp_allad_018_coolapk` | Scripts/app-clean.conf:12 | 酷安 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/api\.coolapk\.com\/v\d\/main\/(?:dataList\|indexV\|init)` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/coolapk.js` |
| `cmp_allad_019_zhihu` | Scripts/app-clean.conf:13 | 知乎 | http-response | 1 | zirawell R-Store | 必须独立保留 | 核心专项脚本，合并风险高 | `^https?:\/\/api\.zhihu\.com\/(v\d\/)?questions\/\d+\/(feeds\|answers)\?` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/zhihu.js` |
| `cmp_allad_023_dianping` | Scripts/app-clean.conf:14 | 大众点评 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/ddplus\.meituan\.net\/v\d\/mss_\w+\/picassovc` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/dianping.js` |
| `cmp_allad_024_12306` | Scripts/app-clean.conf:15 | 未识别 / 通用 | http-response | 0 | zirawell R-Store | 可改规则候选 | 不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite | `^https?:\/\/mobile\.12306\.cn\/otsmobile\/app\/mgs\/mgw\.htm$` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/mgw.js` |
| `cmp_allad_025_rrtv` | Scripts/app-clean.conf:16 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/api\.rr\.tv\/drama\/app\/get_combined_drama_detail` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/rrtv.js` |
| `cmp_allad_026_163music` | Scripts/app-clean.conf:17 | 网易云音乐 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/interface\d?\.music\.163\.com\/w?e?api\/song\/play\/more\/list\/v\d` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/163music.js` |
| `cmp_allad_027_airchina` | Scripts/app-clean.conf:18 | 未识别 / 通用 | http-response | 0 | zirawell R-Store | 可改规则候选 | 不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite | `^https?:\/\/m\.airchina\.com\.cn\/airchina\/gateway\/v\d(\.\d)*\/api\/services` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/airchina.js` |
| `cmp_allad_028_xmgtv` | Scripts/app-clean.conf:19 | 芒果 TV | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/mgesq\.api\.mgtv\.com\/dsl\/index\.+` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xmgtv.js` |
| `cmp_allad_029_amap` | Scripts/app-clean.conf:20 | 高德地图 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/m\d\.amap\.com\/ws\/shield\/search_business\/process\/marketingOperationStruct` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/amap.js` |
| `cmp_allad_030_babytree` | Scripts/app-clean.conf:21 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/go\.babytree\.com\/go_pregnancy\/api\/(?:app_index\|cms_column)` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/babytree.js` |
| `cmp_allad_031_baidutieba` | Scripts/app-clean.conf:22 | 贴吧 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/c\.tieba\.baidu\.com\/c\/s\/sync$` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/tiebaJson.js` |
| `cmp_allad_032_mafengwo` | Scripts/app-clean.conf:23 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/mapi\.mafengwo\.cn\/user\/profile\/get_(?:list\|profile)` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/mafengwo.js` |
| `cmp_allad_033_gaoding` | Scripts/app-clean.conf:24 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/www\.gaoding\.com\/api\/v\d\/oc\/exhibitions\/template\/resources$` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/gaoding.js` |
| `cmp_allad_034_pdd` | Scripts/app-clean.conf:25 | 拼多多 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/api\.pinduoduo\.com\/api\/oak\/integration\/render` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/pdd.js` |
| `cmp_allad_035_qidian` | Scripts/app-clean.conf:26 | 起点 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/mage(v\d)?\.if\.qidian\.com\/argus\/api\/v\d\/(deeplink\/geturl\|client\/getcon` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/qidian.js` |
| `cmp_allad_036_kuaishou` | Scripts/app-clean.conf:27 | 快手 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/open\.e\.kuaishou\.com\/rest\/e\/v\d\/open\/univ$` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/adsense.js` |
| `cmp_allad_037_freshippo` | Scripts/app-clean.conf:28 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/acs\.m\.shyhhema\.com\/h5\/mtop\.wdk\.render\.query(?:index\|my)page` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/freshippo.js` |
| `cmp_allad_038_xunlei` | Scripts/app-clean.conf:29 | 迅雷 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/conf-m-ssl\.xunlei\.com\/external\/` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xunlei.js` |
| `cmp_allad_039_cainiao` | Scripts/app-clean.conf:30 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/cn-acs\.m\.cainiao\.com\/gw\/mtop\.cainiao\.nbpresentation\.(pickup\.empty\.pa` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/cainiao.js` |
| `cmp_allad_040_zhuanzhuan` | Scripts/app-clean.conf:31 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/app\.zhuanzhuan\.com\/zz\/v\d\/zzlogic\/mywxcontinenthomepage` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/zhuanzhuan.js` |
| `cmp_allad_041_baidumap` | Scripts/app-clean.conf:32 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/newclient\.map\.baidu\.com\/client\/phpui2\/\?qt=ads` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/baiduMap.js` |
| `cmp_allad_042_ehaier` | Scripts/app-clean.conf:33 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/zj\.haier\.net\/omsappapi\/resource\/v\d\/get\/resourceBag$` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/haier.js` |
| `cmp_allad_045_xiaoyuzhoufm` | Scripts/app-clean.conf:34 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/api\.xiaoyuzhoufm\.com\/v\d\/discovery-feed\/list` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xiaoyuzhoufm.js` |
| `cmp_allad_047_peiyinxiu` | Scripts/app-clean.conf:35 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/iosapi\.peiyinxiu\.com\/Api\/Film\/GetConfigValue` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/peiyinxiu.js` |
| `cmp_allad_048_jd` | Scripts/app-clean.conf:36 | 京东 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/api\.m\.jd\.com\/client\.action\?functionId=(?:deliverLayer\|getTabHomeInfo\|myO` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/jd.js` |
| `cmp_allad_049_meituan` | Scripts/app-clean.conf:37 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/p\d\.meituan\.net\/linglong\/` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/meituan.js` |
| `cmp_allad_050_reddit` | Scripts/app-clean.conf:38 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/gql(-fed)?\.reddit\.com` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/reddit.js` |
| `cmp_allad_051_boohee` | Scripts/app-clean.conf:39 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/api\.boohee\.com\/open-interface\/v\d\/string\/market_page\?title=metabolism_c` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/boohee.js` |
| `cmp_allad_052_360cam` | Scripts/app-clean.conf:40 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/jia\.360\.cn\/conf\/v\d\.json` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/360cam.js` |
| `cmp_allad_053_fliggy` | Scripts/app-clean.conf:41 | 淘宝 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/acs\.m\.taobao\.com\/gw\/mtop\.fliggy\.ssif\.pattern\.home` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/fliggy.js` |
| `cmp_allad_054_1314zhilv` | Scripts/app-clean.conf:42 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/www\.1314zhilv\.com\/ltsstnew\/(common\/getJGQIconNew\|city\/getAllBannelByCity` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/ltsst.js` |
| `cmp_allad_055_adunion` | Scripts/app-clean.conf:43 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/g\.alicdn\.com\/.*o2o-ad` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/alicdn.js` |
| `cmp_allad_056_ppx` | Scripts/app-clean.conf:44 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/.+\.pipix\.com\/bds\/feed\/channel_list\/` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/ppx.js` |
| `cmp_allad_057_douyu` | Scripts/app-clean.conf:45 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/apiv2\.douyucdn\.cn\/japi\/entrance\/roomRes\/nc\/m\/list` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/douyu.js` |
| `cmp_allad_058_sptcc` | Scripts/app-clean.conf:46 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/online\.sptcc\.com:\d+\/handapp_update\/AppInfo` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/sptcc.js` |
| `cmp_allad_059_quda` | Scripts/app-clean.conf:47 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/iqushangwang\.8quan\.com\/index\.php\/i\/index\/index` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/quda.js` |
| `cmp_allad_060_maimai` | Scripts/app-clean.conf:48 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/(h3\.)?open\.taou\.com\/maimai\/(feed\|gossip)\/v\d\/(?:focus_feed\|gossip_detai` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/maimai.js` |
| `cmp_allad_061_foliday` | Scripts/app-clean.conf:49 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/apis\.folidaymall\.com\/online\/capi\/component\/getPageComponents` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/foliday.js` |
| `cmp_allad_062_tuhu` | Scripts/app-clean.conf:50 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/(cl-)?gateway\.tuhu\.cn(\/cl)?\/cl-common-api\/api\/personalCenter\/getCmsModu` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/tuhu.js` |
| `cmp_allad_063_163youdao` | Scripts/app-clean.conf:51 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/dict\.youdao\.com\/(homepage\/promotion\|course\/tab\/home\|homepage\/tile)` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/163youdao.js` |
| `cmp_allad_064_ys7` | Scripts/app-clean.conf:52 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/\w+\.ys7\.com\/v\d\/valueadded\/operation\/config\/master\/station` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/ys7.js` |
| `cmp_allad_065_flyert` | Scripts/app-clean.conf:53 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/www\.flyert(rip)?\.com(\.cn)?\/.*plugin` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/flyert.js` |
| `cmp_allad_066_wjx` | Scripts/app-clean.conf:54 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/kaoshi\.wjx\.top\/wjx\/join\/completemobile` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/wjx.js` |
| `cmp_allad_067_guiderank` | Scripts/app-clean.conf:55 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/zone\.guiderank-app\.com\/guiderank-web\/app\/home\/getHomePageV` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/guiderank.js` |
| `cmp_allad_068_mishop` | Scripts/app-clean.conf:56 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/api\.m\.mi\.com\/v\d\/order\/expressView` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/mishop.js` |
| `cmp_allad_069_qbb` | Scripts/app-clean.conf:57 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/webapi\.qbb6\.com\/h5\/api\/lib\/internal\/append\/get` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/qbb.js` |
| `cmp_allad_070_sogou` | Scripts/app-clean.conf:58 | 未识别 / 通用 | http-response | 0 | zirawell R-Store | 可改规则候选 | 不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite | `^https?:\/\/sec\.sginput\.qq\.com\/q` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/sougou.js` |
| `cmp_allad_071_51cto` | Scripts/app-clean.conf:59 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/edu\.51cto\.com\/app\.php\?$` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/51cto.js` |
| `cmp_allad_072_baidutieba` | Scripts/app-clean.conf:60 | 贴吧 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/c\.tieba\.baidu\.com\/c\/f\/(excellent\/personalized\|frs\/(?:generalTabList\|pa` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/tiebaProto.js` |
| `cmp_allad_073_meituanwm` | Scripts/app-clean.conf:61 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/web\.meituan\.com\/api\/miniprogram\/tabbar\/all\/query` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/meituanwm.js` |
| `cmp_allad_074_adunion` | Scripts/app-clean.conf:62 | 淘宝 | http-response | 0 | zirawell R-Store | 可改规则候选 | 不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite | `^https?:\/\/amdc\.m\.taobao\.com\/amdc\/mobileDispatch$` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/amdc.js` |
| `cmp_allad_075_umetrip` | Scripts/app-clean.conf:63 | 未识别 / 通用 | http-response | 0 | zirawell R-Store | 可改规则候选 | 不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite | `^https?:\/\/(bkclient\|umerp\|home)\.umetrip\.com(\.cn){0` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/umetrip.js` |
| `cmp_allad_076_ithome` | Scripts/app-clean.conf:64 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/napi\.ithome\.com\/api\/(news\/index\|topmenu\/getfeeds)` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/ithome.js` |
| `cmp_allad_077_eleme` | Scripts/app-clean.conf:65 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/waimai-guide\.ele\.me\/(gw\|h5)\/mtop\.alsc\.eleme\.miniapp\.homepage` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/eleme.js` |
| `cmp_allad_078_duitang` | Scripts/app-clean.conf:66 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/(www\|api)\.duitang\.com\/napi\/settings\/` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/duitang.js` |
| `cmp_allad_079_51job` | Scripts/app-clean.conf:67 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/cupid\.51job(app)?\.com\/open\/my-page\/` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/51job.js` |
| `cmp_allad_080_yunda` | Scripts/app-clean.conf:68 | 未识别 / 通用 | http-request | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/mbpxapi\.yundasys\.com(:\d+)?\/gateway\/interface` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/yunda.js` |
| `cmp_allad_081_usmile` | Scripts/app-clean.conf:69 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/www\.myusmile\.online\/user\/plaqueTopic\/selectByType` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/usmile.js` |
| `cmp_block_082_12306` | Scripts/app-clean.conf:70 | 未识别 / 通用 | http-request | 1 | raw.githubusercontent.com | 需要人工复核 | 无法静态判断，需结合脚本内容和真机测试 | `^https?:\/\/ad\.12306\.cn\/ad\/ser\/getAdList` | `https://raw.githubusercontent.com/kokoryh/Script/master/js/12306.js` |
| `cmp_block_083_ad` | Scripts/app-clean.conf:71 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/[\d\.]+\/3f1\/cards\.iqiyi\.com\/(views_home\/3\.0\/qy_home\|waterfall\/3\.0\/f` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/cnftp.js` |
| `cmp_block_086_ad` | Scripts/app-clean.conf:72 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/gg\.caixin\.com\/s\?z=caixin&op=1&c=3362` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/caixin/caixinAd.js` |
| `cmp_block_087_ad` | Scripts/app-clean.conf:73 | 滴滴 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/ct\.xiaojukeji\.com\/agent\/v3\/feeds` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/didi/didiAds.js` |
| `cmp_block_088_ad` | Scripts/app-clean.conf:74 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^http?:\/\/(114\.115\.217\.129)\|(home\.umetrip\.com)\/gateway\/api\/umetrip\/native$` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/umetrip/umetrip_ads.js` |
| `cmp_block_089_ad` | Scripts/app-clean.conf:75 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https:\/\/lawsonapi\.yorentown\.com\/portal\/app\/globalLaunch\/listAdvert` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/lawson.js` |
| `cmp_block_090_ad` | Scripts/app-clean.conf:76 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https:\/\/(h3\.)?open\.taou\.com\/maimai\/feed\/v6\/detail_recommend_feeds\?` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/maimai/maimai_ads.js` |
| `cmp_block_091_app` | Scripts/app-clean.conf:77 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https:\/\/config-service\.seeyouyima\.com\/api\/configs\/batch\?` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/meiyou/meiyou_ads.js` |
| `cmp_block_092_ad` | Scripts/app-clean.conf:78 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/display-sc\.miguvideo\.com\/display\/v3\/static\/PERSONAL_CENTER$` | `https://raw.githubusercontent.com/fmz200/wool_scripts/refs/heads/main/Scripts/miguvideo/miguvideo_ads.js` |
| `cmp_block_093_ad` | Scripts/app-clean.conf:79 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https:\/\/j1\.pupuapi\.com\/client\/search\/hot_keywords\/v3` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/PupuSplashAds.js` |
| `cmp_block_094_ad` | Scripts/app-clean.conf:80 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/(?:webapi\|miniapp)\.qmai\.cn\/web\/catering([0-9]-apiserver)?\/advertising\/ad` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/qmai.js` |
| `cmp_block_095_rrtv_json` | Scripts/app-clean.conf:81 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/api\.rr\.tv\/ad\/getAll` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/rrtv_json.js` |
| `cmp_block_096_ad` | Scripts/app-clean.conf:82 | 什么值得买 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/haojia\.m\.smzdm\.com\/detail_modul\/user_related_modul\?` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/smzdm/smzdm_ads.js` |
| `cmp_block_099_ad` | Scripts/app-clean.conf:83 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/dict\.youdao\.com\/(homepage\/promotion\|course\/tab\/home\|homepage\/tile)` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/youdao/dict-youdao-ad.js` |
| `app-cleaner-active-json-clean` | Scripts/app-cleaner-active.conf:7 | VGTime / 快看漫画 / 闲鱼 | http-response | 1 | local | 需要人工复核 | 无法静态判断，需结合脚本内容和真机测试 | `^https?:\/\/.*(qq\.com\|vgtime\.com\|17gwx\.com\|163\.com\|xiaoheihe\.cn\|wearemanner\.com\|chao` | `https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Scripts/app-cleaner.js` |
| `spotify-json` | Scripts/spotify.conf:2 | Spotify | http-request | 0 | app2smile | 必须独立保留 | 核心专项脚本，合并风险高 | `^https:\/\/(spclient\.wg\.spotify\.com\|.*-spclient\.spotify\.com(:443)?)\/(artistview\/v1\` | `https://raw.githubusercontent.com/app2smile/rules/master/js/spotify-json.js` |
| `spotify-proto` | Scripts/spotify.conf:3 | Spotify | http-response | 1 | app2smile | 必须独立保留 | 核心专项脚本，合并风险高 | `^https:\/\/(spclient\.wg\.spotify\.com\|.*-spclient\.spotify\.com(:443)?)\/(bootstrap\/v1\/` | `https://raw.githubusercontent.com/app2smile/rules/master/js/spotify-proto.js` |
| `youtube.response` | Scripts/youtube.conf:2 | YouTube | http-response | 1 | Maasea | 必须独立保留 | 核心专项脚本，合并风险高 | `^https:\/\/youtubei\.googleapis\.com\/(youtubei\/v1\/(browse\|next\|player\|search\|reel\/reel` | `https://raw.githubusercontent.com/Maasea/sgmodule/master/Script/Youtube/youtube.response.js` |
| `zhihu-enhance` | Scripts/zhihu-enhance.conf:4 | 知乎 | http-response | 1 | local | 必须独立保留 | 核心专项脚本，合并风险高 | `^https?:\/\/api\.zhihu\.com\/(topstory\|moments\|feed\|notifications\|v\d+\/questions\/\d+\/(f` | `https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Scripts/zhihu-enhance.js` |

## 下一步建议

1. 第一阶段只处理重复 script-path 和明显普通 JSON 清理脚本，不动 Spotify、YouTube、知乎。
2. 先设计统一 `app-cleaner.js` 和配置表，不直接删除旧入口。
3. 通过 `stable-plus` 做灰度验证，确认无异常后再减少入口。
4. 能用 Rule / URL Rewrite 解决的静态广告接口，应从脚本迁移到规则层。
5. 每次减少脚本后都要重新生成四个 Release 版本，并更新测试记录。
