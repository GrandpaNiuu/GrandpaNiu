# 脚本清单与瘦身分析报告

生成时间：2026-05-31 07:38:04 +0800

本报告只做静态分析，不删除、不合并、不禁用任何脚本。减少脚本前必须先完成真机测试和回滚准备。

## 总体统计

- 脚本入口总数：37
- 识别到的 App / 服务方向数量：15
- 重复脚本名：0
- 多入口共用同一 script-path：0

## 分类统计

- 必须独立保留：6
- 可合并候选：24
- 可改规则候选：5
- 需要人工复核：2

## 来源统计

- zirawell R-Store：23
- fmz200 wool_scripts：6
- app2smile：4
- local：2
- raw.githubusercontent.com：1
- Maasea：1

## 文件分布

- `Scripts/app-clean.conf`：32
- `Scripts/spotify.conf`：2
- `Scripts/app-cleaner-active.conf`：1
- `Scripts/youtube.conf`：1
- `Scripts/zhihu-enhance.conf`：1

## 重复脚本名

- 无

## 多入口共用同一 script-path

- 无

## 可合并候选摘要

- zirawell R-Store：17 个，可考虑进入统一 `app-cleaner.js` 的配置化处理
- fmz200 wool_scripts：6 个，可考虑进入统一 `app-cleaner.js` 的配置化处理
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
| `cmp_allad_019_zhihu` | Scripts/app-clean.conf:12 | 知乎 | http-response | 1 | zirawell R-Store | 必须独立保留 | 核心专项脚本，合并风险高 | `^https?:\/\/api\.zhihu\.com\/(v\d\/)?questions\/\d+\/(feeds\|answers)\?` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/zhihu.js` |
| `cmp_allad_024_12306` | Scripts/app-clean.conf:13 | 未识别 / 通用 | http-response | 0 | zirawell R-Store | 可改规则候选 | 不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite | `^https?:\/\/mobile\.12306\.cn\/otsmobile\/app\/mgs\/mgw\.htm$` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/mgw.js` |
| `cmp_allad_025_rrtv` | Scripts/app-clean.conf:14 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/api\.rr\.tv\/drama\/app\/get_combined_drama_detail` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/rrtv.js` |
| `cmp_allad_026_163music` | Scripts/app-clean.conf:15 | 网易云音乐 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/interface\d?\.music\.163\.com\/w?e?api\/song\/play\/more\/list\/v\d` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/163music.js` |
| `cmp_allad_027_airchina` | Scripts/app-clean.conf:16 | 未识别 / 通用 | http-response | 0 | zirawell R-Store | 可改规则候选 | 不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite | `^https?:\/\/m\.airchina\.com\.cn\/airchina\/gateway\/v\d(\.\d)*\/api\/services` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/airchina.js` |
| `cmp_allad_028_xmgtv` | Scripts/app-clean.conf:17 | 芒果 TV | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/mgesq\.api\.mgtv\.com\/dsl\/index\.+` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xmgtv.js` |
| `cmp_allad_031_baidutieba` | Scripts/app-clean.conf:18 | 贴吧 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/c\.tieba\.baidu\.com\/c\/s\/sync$` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/tiebaJson.js` |
| `cmp_allad_057_douyu` | Scripts/app-clean.conf:19 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/apiv2\.douyucdn\.cn\/japi\/entrance\/roomRes\/nc\/m\/list` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/douyu.js` |
| `cmp_allad_058_sptcc` | Scripts/app-clean.conf:20 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/online\.sptcc\.com:\d+\/handapp_update\/AppInfo` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/sptcc.js` |
| `cmp_allad_066_wjx` | Scripts/app-clean.conf:21 | 未识别 / 通用 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/kaoshi\.wjx\.top\/wjx\/join\/completemobile` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/wjx.js` |
| `cmp_allad_070_sogou` | Scripts/app-clean.conf:22 | 未识别 / 通用 | http-response | 0 | zirawell R-Store | 可改规则候选 | 不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite | `^https?:\/\/sec\.sginput\.qq\.com\/q` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/sougou.js` |
| `cmp_allad_072_baidutieba` | Scripts/app-clean.conf:23 | 贴吧 | http-response | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/c\.tieba\.baidu\.com\/c\/f\/(excellent\/personalized\|frs\/(?:generalTabList\|pa` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/tiebaProto.js` |
| `cmp_allad_074_adunion` | Scripts/app-clean.conf:24 | 淘宝 | http-response | 0 | zirawell R-Store | 可改规则候选 | 不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite | `^https?:\/\/amdc\.m\.taobao\.com\/amdc\/mobileDispatch$` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/amdc.js` |
| `cmp_allad_075_umetrip` | Scripts/app-clean.conf:25 | 未识别 / 通用 | http-response | 0 | zirawell R-Store | 可改规则候选 | 不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite | `^https?:\/\/(bkclient\|umerp\|home)\.umetrip\.com(\.cn){0` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/umetrip.js` |
| `cmp_allad_080_yunda` | Scripts/app-clean.conf:26 | 未识别 / 通用 | http-request | 1 | zirawell R-Store | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/mbpxapi\.yundasys\.com(:\d+)?\/gateway\/interface` | `https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/yunda.js` |
| `cmp_block_082_12306` | Scripts/app-clean.conf:27 | 未识别 / 通用 | http-request | 1 | raw.githubusercontent.com | 需要人工复核 | 无法静态判断，需结合脚本内容和真机测试 | `^https?:\/\/ad\.12306\.cn\/ad\/ser\/getAdList` | `https://raw.githubusercontent.com/kokoryh/Script/master/js/12306.js` |
| `cmp_block_083_ad` | Scripts/app-clean.conf:28 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/[\d\.]+\/3f1\/cards\.iqiyi\.com\/(views_home\/3\.0\/qy_home\|waterfall\/3\.0\/f` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/cnftp.js` |
| `cmp_block_087_ad` | Scripts/app-clean.conf:29 | 滴滴 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/ct\.xiaojukeji\.com\/agent\/v3\/feeds` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/didi/didiAds.js` |
| `cmp_block_088_ad` | Scripts/app-clean.conf:30 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^http?:\/\/(114\.115\.217\.129)\|(home\.umetrip\.com)\/gateway\/api\/umetrip\/native$` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/umetrip/umetrip_ads.js` |
| `cmp_block_090_ad` | Scripts/app-clean.conf:31 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https:\/\/(h3\.)?open\.taou\.com\/maimai\/feed\/v6\/detail_recommend_feeds\?` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/maimai/maimai_ads.js` |
| `cmp_block_095_rrtv_json` | Scripts/app-clean.conf:32 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/api\.rr\.tv\/ad\/getAll` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/rrtv_json.js` |
| `cmp_block_099_ad` | Scripts/app-clean.conf:33 | 未识别 / 通用 | http-response | 1 | fmz200 wool_scripts | 可合并候选 | 普通 App JSON 清理脚本，可评估合并到统一 app-cleaner | `^https?:\/\/dict\.youdao\.com\/(homepage\/promotion\|course\/tab\/home\|homepage\/tile)` | `https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/youdao/dict-youdao-ad.js` |
| `app-cleaner-active-json-clean` | Scripts/app-cleaner-active.conf:8 | VGTime / 快看漫画 / 闲鱼 | http-response | 1 | local | 需要人工复核 | 无法静态判断，需结合脚本内容和真机测试 | `^https?:\/\/.*(qq\.com\|vgtime\.com\|17gwx\.com\|163\.com\|xiaoheihe\.cn\|wearemanner\.com\|chao` | `https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Scripts/app-cleaner.js` |
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
