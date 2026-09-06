# 脚本清单与瘦身分析报告

生成时间：2026-09-07 02:37:18 +0800

本报告只做静态分析，不删除、不合并、不禁用任何脚本。减少脚本前必须先完成自动化验证和回滚准备。

## 总体统计

- 脚本入口总数：26
- 识别到的 App / 服务方向数量：15
- 重复脚本名：0
- 多入口共用同一 script-path：0

## 分类统计

- 必须独立保留：6
- 可合并候选：7
- 可改规则候选：2
- 需要人工复核：11

## 来源统计

- zirawell R-Store：15
- app2smile：5
- fmz200 wool_scripts：3
- local：2
- Maasea：1

## 文件分布

- `Scripts/app-clean.conf`：20
- `Scripts/spotify.conf`：2
- `Scripts/app-cleaner-active.conf`：1
- `Scripts/app2smile-qqnews-stable-plus.conf`：1
- `Scripts/youtube.conf`：1
- `Scripts/zhihu-enhance.conf`：1

## 重复脚本名

- 无

## 多入口共用同一 script-path

- 无

## 可合并候选摘要

- zirawell R-Store：3 个，可考虑进入统一 `app-cleaner.js` 的配置化处理
- app2smile：2 个，可考虑进入统一 `app-cleaner.js` 的配置化处理
- fmz200 wool_scripts：2 个，可考虑进入统一 `app-cleaner.js` 的配置化处理

## 可改规则候选摘要

- `cmp_allad_027_airchina`：未识别 / 通用，不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite
- `cmp_allad_074_adunion`：淘宝，不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite

## 全量脚本清单

| 脚本名 | 位置 | App / 服务 | 类型 | requires-body | 来源 | 分类 | 原因 | pattern 摘要 | script-path |
|---|---|---|---|---|---|---|---|---|---|
| `cmp_block_084_json` | Scripts/app-clean.conf:2 | 贴吧 | http-response | 1 | app2smile | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^http(s:\/\/tiebac\|:\/\/c\.tieba)\.baidu\.com\/(c\/(s\/sync\|f\/(ad\/getSplashAd\|frs\/(page` | `https://raw.githubusercontent.com/app2smile/rules/master/js/tieba-json.js` |
| `cmp_block_085_proto` | Scripts/app-clean.conf:3 | 贴吧 | http-response | 1 | app2smile | 必须独立保留 | 二进制 body / protobuf 类处理，不能简单合并 | `^http(s:\/\/tiebac\|:\/\/c\.tieba)\.baidu\.com\/c\/(b\/ad\/adBid\|f\/(frs\/(page\|threadlist\|` | `https://raw.githubusercontent.com/app2smile/rules/master/js/tieba-proto.js` |
| `cmp_allad_001_weibo` | Scripts/app-clean.conf:4 | 微博 | http-response | 1 | zirawell R-Store | 需要人工复核 | 脚本逻辑较大或涉及深层结构，不能仅凭入口判断为低风险 | `^https?:\/\/api\.weibo\.cn\/2\/groups\/allgroups\/v2\?` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/weibo.js` |
| `cmp_allad_003_keep` | Scripts/app-clean.conf:5 | Keep | http-response | 1 | zirawell R-Store | 需要人工复核 | 脚本逻辑较大或涉及深层结构，不能仅凭入口判断为低风险 | `^https?:\/\/api\.gotokeep\.com\/nuocha\/course\/v\d/\w+\/preview` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/keep.js` |
| `cmp_allad_005_mgtv` | Scripts/app-clean.conf:6 | 芒果 TV | http-response | 1 | zirawell R-Store | 需要人工复核 | 脚本逻辑较大或涉及深层结构，不能仅凭入口判断为低风险 | `^https?:\/\/mob-st\.bz\.mgtv\.com\/odin\/c\d\/channel\/index\?` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/cntv.js` |
| `cmp_allad_006_tflj` | Scripts/app-clean.conf:7 | 铁路/出行类 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/tf02\.istrongcloud\.com\/member\/v[0-9.]+\/home` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/tflj.js` |
| `cmp_allad_007_cotti` | Scripts/app-clean.conf:8 | 库迪咖啡 | http-request | 1 | zirawell R-Store | 必须独立保留 | request-body 类处理风险较高，不能并入 response JSON cleaner | `^https?:\/\/gateway\.cotticoffee\.com\/cotti-capi\/customer\/position\/list$` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/cotti.js` |
| `cmp_allad_012_dushu365` | Scripts/app-clean.conf:9 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/g(.*)\.dushu365\.com\/task-orchestration\/taskCenter\/api\/v101\/taskList` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/dushu365.js` |
| `cmp_allad_017_xiaohongshu` | Scripts/app-clean.conf:10 | 小红书 | http-response | 1 | zirawell R-Store | 需要人工复核 | 脚本逻辑较大或涉及深层结构，不能仅凭入口判断为低风险 | `^https?:\/\/edith\.xiaohongshu\.com\/api\/sns\/v\d+\/interaction\/comment\/video\/download` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xiaohongshu.js` |
| `cmp_allad_025_rrtv` | Scripts/app-clean.conf:11 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 需要人工复核 | 脚本逻辑较大或涉及深层结构，不能仅凭入口判断为低风险 | `^https?:\/\/api\.rr\.tv\/drama\/app\/get_combined_drama_detail` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/rrtv.js` |
| `cmp_allad_026_163music` | Scripts/app-clean.conf:12 | 网易云音乐 | http-response | 1 | zirawell R-Store | 需要人工复核 | 脚本逻辑较大或涉及深层结构，不能仅凭入口判断为低风险 | `^https?:\/\/interface\d?\.music\.163\.com\/w?e?api\/song\/play\/more\/list\/v\d` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/163music.js` |
| `cmp_allad_027_airchina` | Scripts/app-clean.conf:13 | 未识别 / 通用 | http-response | 0 | zirawell R-Store | 可改规则候选 | 不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite | `^https?:\/\/m\.airchina\.com\.cn\/airchina\/gateway\/v\d(\.\d)*\/api\/services` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/airchina.js` |
| `cmp_allad_028_xmgtv` | Scripts/app-clean.conf:14 | 芒果 TV | http-response | 1 | zirawell R-Store | 需要人工复核 | 脚本逻辑较大或涉及深层结构，不能仅凭入口判断为低风险 | `^https?:\/\/mgesq\.api\.mgtv\.com\/dsl\/index\.+` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xmgtv.js` |
| `cmp_allad_066_wjx` | Scripts/app-clean.conf:15 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/kaoshi\.wjx\.top\/wjx\/join\/completemobile` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/wjx.js` |
| `cmp_allad_070_sogou` | Scripts/app-clean.conf:16 | 未识别 / 通用 | http-response | 0 | zirawell R-Store | 需要人工复核 | 脚本逻辑较大或涉及深层结构，不能仅凭入口判断为低风险 | `^https?:\/\/sec\.sginput\.qq\.com\/q` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/sougou.js` |
| `cmp_allad_074_adunion` | Scripts/app-clean.conf:17 | 淘宝 | http-response | 0 | zirawell R-Store | 可改规则候选 | 不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite | `^https?:\/\/amdc\.m\.taobao\.com\/amdc\/mobileDispatch$` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/amdc.js` |
| `cmp_allad_080_yunda` | Scripts/app-clean.conf:18 | 未识别 / 通用 | http-request | 1 | zirawell R-Store | 必须独立保留 | request-body 类处理风险较高，不能并入 response JSON cleaner | `^https?:\/\/mbpxapi\.yundasys\.com(:\d+)?\/gateway\/interface` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/yunda.js` |
| `cmp_block_083_ad` | Scripts/app-clean.conf:19 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/[\d\.]+\/3f1\/cards\.iqiyi\.com\/(views_home\/3\.0\/qy_home\|waterfall\/3\.0\/f` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/cnftp.js` |
| `cmp_block_087_ad` | Scripts/app-clean.conf:20 | 滴滴 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/ct\.xiaojukeji\.com\/agent\/v3\/feeds` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/didi/didiAds.js` |
| `cmp_block_095_rrtv_json` | Scripts/app-clean.conf:21 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 需要人工复核 | 脚本逻辑较大或涉及深层结构，不能仅凭入口判断为低风险 | `^https?:\/\/api\.rr\.tv\/ad\/getAll` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/rrtv_json.js` |
| `app-cleaner-active-json-clean` | Scripts/app-cleaner-active.conf:10 | VGTime / 快看漫画 / 闲鱼 | http-response | 1 | local | 需要人工复核 | 无法静态判断，需结合脚本内容和自动化验证 | `^https?:\/\/.*(news\.ssp\.qq\.com\|r\.inews\.qq\.com\|vgtime\.com\|17gwx\.com\|gw\.m\.163\.com` | `https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Scripts/app-cleaner.js` |
| `app2smile_qqnews_json` | Scripts/app2smile-qqnews-stable-plus.conf:5 | QQ 新闻 | http-response | 1 | app2smile | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https:\/\/(news\.ssp\.qq\.com\/app\|r\.inews\.qq\.com\/(get(QQNewsUnreadList\|TagFeedList)\|` | `https://raw.githubusercontent.com/app2smile/rules/master/js/qq-news.js` |
| `spotify-json` | Scripts/spotify.conf:2 | Spotify | http-request | 0 | app2smile | 必须独立保留 | request-body 类处理风险较高，不能并入 response JSON cleaner | `^https:\/\/(spclient\.wg\.spotify\.com\|.*-spclient\.spotify\.com(:443)?)\/(artistview\/v1\` | `https://raw.githubusercontent.com/app2smile/rules/master/js/spotify-json.js` |
| `spotify-proto` | Scripts/spotify.conf:3 | Spotify | http-response | 1 | app2smile | 必须独立保留 | 二进制 body / protobuf 类处理，不能简单合并 | `^https:\/\/(spclient\.wg\.spotify\.com\|.*-spclient\.spotify\.com(:443)?)\/(bootstrap\/v1\/` | `https://raw.githubusercontent.com/app2smile/rules/master/js/spotify-proto.js` |
| `youtube.response` | Scripts/youtube.conf:1 | YouTube | http-response | 1 | Maasea | 必须独立保留 | 二进制 body / protobuf 类处理，不能简单合并 | `^https:\/\/youtubei\.googleapis\.com\/(youtubei\/v1\/(browse\|next\|player\|search\|reel\/reel` | `https://raw.githubusercontent.com/Maasea/sgmodule/master/Script/Youtube/youtube.response.js` |
| `zhihu-enhance` | Scripts/zhihu-enhance.conf:4 | 知乎 | http-response | 1 | local | 需要人工复核 | 脚本逻辑较大或涉及深层结构，不能仅凭入口判断为低风险 | `^https?:\/\/api\.zhihu\.com\/(topstory\|moments\|feed\|notifications\|v\d+\/questions\/\d+\/(f` | `https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Scripts/zhihu-enhance.js` |
