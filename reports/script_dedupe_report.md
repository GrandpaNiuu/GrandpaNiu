# 脚本去重与 app-cleaner active 迁移报告

生成时间：2026-05-31 07:38:03 +0800

## 本次迁移

- 迁移范围：Batch 1-4 专项清理 + Batch 5 通用低风险 JSON 广告字段清理
- 新承接入口：`Scripts/app-cleaner-active.conf` / `app-cleaner-active-json-clean`
- 新承接脚本：`Scripts/app-cleaner.js`
- 计划替换旧入口数量：67
- Scripts/app-clean.conf 本次移除旧入口数量：50
- 所有源文件合计本次移除旧入口数量：100
- 新增 active 入口数量：1
- 说明：这是大批量融合，但保留高风险和复杂脚本独立运行。

## 移除的旧入口

### `Scripts/app-clean.conf`

#### `cmp_allad_018_coolapk`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_018_coolapk = type=http-response,pattern=^https?:\/\/api\.coolapk\.com\/v\d\/main\/(?:dataList|indexV|init),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/coolapk.js,script-update-interval=86400
```

#### `cmp_allad_023_dianping`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_023_dianping = type=http-response,pattern=^https?:\/\/ddplus\.meituan\.net\/v\d\/mss_\w+\/picassovc,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/dianping.js,script-update-interval=86400
```

#### `cmp_allad_029_amap`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_029_amap = type=http-response,pattern=^https?:\/\/m\d\.amap\.com\/ws\/shield\/search_business\/process\/marketingOperationStructured\?,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/amap.js,script-update-interval=86400
```

#### `cmp_allad_030_babytree`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_030_babytree = type=http-response,pattern=^https?:\/\/go\.babytree\.com\/go_pregnancy\/api\/(?:app_index|cms_column),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/babytree.js,script-update-interval=86400
```

#### `cmp_allad_032_mafengwo`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_032_mafengwo = type=http-response,pattern=^https?:\/\/mapi\.mafengwo\.cn\/user\/profile\/get_(?:list|profile),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/mafengwo.js,script-update-interval=86400
```

#### `cmp_allad_033_gaoding`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_033_gaoding = type=http-response,pattern=^https?:\/\/www\.gaoding\.com\/api\/v\d\/oc\/exhibitions\/template\/resources$,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/gaoding.js,script-update-interval=86400
```

#### `cmp_allad_034_pdd`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_034_pdd = type=http-response,pattern=^https?:\/\/api\.pinduoduo\.com\/api\/oak\/integration\/render,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/pdd.js,script-update-interval=86400
```

#### `cmp_allad_035_qidian`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_035_qidian = type=http-response,pattern=^https?:\/\/mage(v\d)?\.if\.qidian\.com\/argus\/api\/v\d\/(deeplink\/geturl|client\/getconf|bookshelf\/getHoverAdv|dailyrecommend\/getdailyrecommend|assembly\/toolbar|user\/getaccountpage),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/qidian.js,script-update-interval=86400
```

#### `cmp_allad_036_kuaishou`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_036_kuaishou = type=http-response,pattern=^https?:\/\/open\.e\.kuaishou\.com\/rest\/e\/v\d\/open\/univ$,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/adsense.js,script-update-interval=86400
```

#### `cmp_allad_037_freshippo`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_037_freshippo = type=http-response,pattern=^https?:\/\/acs\.m\.shyhhema\.com\/h5\/mtop\.wdk\.render\.query(?:index|my)page,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/freshippo.js,script-update-interval=86400
```

#### `cmp_allad_038_xunlei`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_038_xunlei = type=http-response,pattern=^https?:\/\/conf-m-ssl\.xunlei\.com\/external\/,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xunlei.js,script-update-interval=86400
```

#### `cmp_allad_039_cainiao`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_039_cainiao = type=http-response,pattern=^https?:\/\/cn-acs\.m\.cainiao\.com\/gw\/mtop\.cainiao\.nbpresentation\.(pickup\.empty\.page|protocol\.homepage)\.get,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/cainiao.js,script-update-interval=86400
```

#### `cmp_allad_040_zhuanzhuan`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_040_zhuanzhuan = type=http-response,pattern=^https?:\/\/app\.zhuanzhuan\.com\/zz\/v\d\/zzlogic\/mywxcontinenthomepage,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/zhuanzhuan.js,script-update-interval=86400
```

#### `cmp_allad_041_baidumap`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_041_baidumap = type=http-response,pattern=^https?:\/\/newclient\.map\.baidu\.com\/client\/phpui2\/\?qt=ads,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/baiduMap.js,script-update-interval=86400
```

#### `cmp_allad_042_ehaier`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_042_ehaier = type=http-response,pattern=^https?:\/\/zj\.haier\.net\/omsappapi\/resource\/v\d\/get\/resourceBag$,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/haier.js,script-update-interval=86400
```

#### `cmp_allad_045_xiaoyuzhoufm`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_045_xiaoyuzhoufm = type=http-response,pattern=^https?:\/\/api\.xiaoyuzhoufm\.com\/v\d\/discovery-feed\/list,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xiaoyuzhoufm.js,script-update-interval=86400
```

#### `cmp_allad_047_peiyinxiu`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_047_peiyinxiu = type=http-response,pattern=^https?:\/\/iosapi\.peiyinxiu\.com\/Api\/Film\/GetConfigValue,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/peiyinxiu.js,script-update-interval=86400
```

#### `cmp_allad_048_jd`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_048_jd = type=http-response,pattern=^https?:\/\/api\.m\.jd\.com\/client\.action\?functionId=(?:deliverLayer|getTabHomeInfo|myOrderInfo|orderTrackBusiness|personinfoBusiness|start|welcomeHome|readCustomSurfaceList),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/jd.js,script-update-interval=86400
```

#### `cmp_allad_049_meituan`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_049_meituan = type=http-response,pattern=^https?:\/\/p\d\.meituan\.net\/linglong\/,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/meituan.js,script-update-interval=86400
```

#### `cmp_allad_050_reddit`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_050_reddit = type=http-response,pattern=^https?:\/\/gql(-fed)?\.reddit\.com,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/reddit.js,script-update-interval=86400
```

#### `cmp_allad_051_boohee`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_051_boohee = type=http-response,pattern=^https?:\/\/api\.boohee\.com\/open-interface\/v\d\/string\/market_page\?title=metabolism_config$,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/boohee.js,script-update-interval=86400
```

#### `cmp_allad_052_360cam`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_052_360cam = type=http-response,pattern=^https?:\/\/jia\.360\.cn\/conf\/v\d\.json,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/360cam.js,script-update-interval=86400
```

#### `cmp_allad_053_fliggy`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_053_fliggy = type=http-response,pattern=^https?:\/\/acs\.m\.taobao\.com\/gw\/mtop\.fliggy\.ssif\.pattern\.home,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/fliggy.js,script-update-interval=86400
```

#### `cmp_allad_054_1314zhilv`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_054_1314zhilv = type=http-response,pattern=^https?:\/\/www\.1314zhilv\.com\/ltsstnew\/(common\/getJGQIconNew|city\/getAllBannelByCity),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/ltsst.js,script-update-interval=86400
```

#### `cmp_allad_055_adunion`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_055_adunion = type=http-response,pattern=^https?:\/\/g\.alicdn\.com\/.*o2o-ad,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/alicdn.js,script-update-interval=86400
```

#### `cmp_allad_056_ppx`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_056_ppx = type=http-response,pattern=^https?:\/\/.+\.pipix\.com\/bds\/feed\/channel_list\/,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/ppx.js,script-update-interval=86400
```

#### `cmp_allad_059_quda`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_059_quda = type=http-response,pattern=^https?:\/\/iqushangwang\.8quan\.com\/index\.php\/i\/index\/index,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/quda.js,script-update-interval=86400
```

#### `cmp_allad_060_maimai`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_060_maimai = type=http-response,pattern=^https?:\/\/(h3\.)?open\.taou\.com\/maimai\/(feed|gossip)\/v\d\/(?:focus_feed|gossip_detail_comment|feed_detail_comment),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/maimai.js,script-update-interval=86400
```

#### `cmp_allad_061_foliday`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_061_foliday = type=http-response,pattern=^https?:\/\/apis\.folidaymall\.com\/online\/capi\/component\/getPageComponents,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/foliday.js,script-update-interval=86400
```

#### `cmp_allad_062_tuhu`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_062_tuhu = type=http-response,pattern=^https?:\/\/(cl-)?gateway\.tuhu\.cn(\/cl)?\/cl-common-api\/api\/personalCenter\/getCmsModuleList,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/tuhu.js,script-update-interval=86400
```

#### `cmp_allad_063_163youdao`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_063_163youdao = type=http-response,pattern=^https?:\/\/dict\.youdao\.com\/(homepage\/promotion|course\/tab\/home|homepage\/tile),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/163youdao.js,script-update-interval=86400
```

#### `cmp_allad_064_ys7`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_064_ys7 = type=http-response,pattern=^https?:\/\/\w+\.ys7\.com\/v\d\/valueadded\/operation\/config\/master\/station,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/ys7.js,script-update-interval=86400
```

#### `cmp_allad_065_flyert`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_065_flyert = type=http-response,pattern=^https?:\/\/www\.flyert(rip)?\.com(\.cn)?\/.*plugin,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/flyert.js,script-update-interval=86400
```

#### `cmp_allad_067_guiderank`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_067_guiderank = type=http-response,pattern=^https?:\/\/zone\.guiderank-app\.com\/guiderank-web\/app\/home\/getHomePageV,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/guiderank.js,script-update-interval=86400
```

#### `cmp_allad_068_mishop`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_068_mishop = type=http-response,pattern=^https?:\/\/api\.m\.mi\.com\/v\d\/order\/expressView,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/mishop.js,script-update-interval=86400
```

#### `cmp_allad_069_qbb`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_069_qbb = type=http-response,pattern=^https?:\/\/webapi\.qbb6\.com\/h5\/api\/lib\/internal\/append\/get,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/qbb.js,script-update-interval=86400
```

#### `cmp_allad_071_51cto`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_071_51cto = type=http-response,pattern=^https?:\/\/edu\.51cto\.com\/app\.php\?$,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/51cto.js,script-update-interval=86400
```

#### `cmp_allad_073_meituanwm`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_073_meituanwm = type=http-response,pattern=^https?:\/\/web\.meituan\.com\/api\/miniprogram\/tabbar\/all\/query,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/meituanwm.js,script-update-interval=86400
```

#### `cmp_allad_076_ithome`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_076_ithome = type=http-response,pattern=^https?:\/\/napi\.ithome\.com\/api\/(news\/index|topmenu\/getfeeds),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/ithome.js,script-update-interval=86400
```

#### `cmp_allad_077_eleme`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_077_eleme = type=http-response,pattern=^https?:\/\/waimai-guide\.ele\.me\/(gw|h5)\/mtop\.alsc\.eleme\.miniapp\.homepage,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/eleme.js,script-update-interval=86400
```

#### `cmp_allad_078_duitang`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_078_duitang = type=http-response,pattern=^https?:\/\/(www|api)\.duitang\.com\/napi\/settings\/,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/duitang.js,script-update-interval=86400
```

#### `cmp_allad_079_51job`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_079_51job = type=http-response,pattern=^https?:\/\/cupid\.51job(app)?\.com\/open\/my-page\/,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/51job.js,script-update-interval=86400
```

#### `cmp_allad_081_usmile`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_081_usmile = type=http-response,pattern=^https?:\/\/www\.myusmile\.online\/user\/plaqueTopic\/selectByType,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/usmile.js,script-update-interval=86400
```

#### `cmp_block_086_ad`

- 说明：Generic JSON ad-field cleaner

```text
cmp_block_086_ad = type=http-response,pattern=^https?:\/\/gg\.caixin\.com\/s\?z=caixin&op=1&c=3362,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/caixin/caixinAd.js,requires-body=1,timeout=60,script-update-interval=86400
```

#### `cmp_block_089_ad`

- 说明：Generic JSON ad-field cleaner

```text
cmp_block_089_ad = type=http-response,pattern=^https:\/\/lawsonapi\.yorentown\.com\/portal\/app\/globalLaunch\/listAdvert,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/lawson.js,requires-body=1,timeout=60,script-update-interval=86400
```

#### `cmp_block_091_app`

- 说明：Generic JSON ad-field cleaner

```text
cmp_block_091_app = type=http-response,pattern=^https:\/\/config-service\.seeyouyima\.com\/api\/configs\/batch\?,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/meiyou/meiyou_ads.js,requires-body=1,timeout=60,script-update-interval=86400
```

#### `cmp_block_092_ad`

- 说明：Generic JSON ad-field cleaner

```text
cmp_block_092_ad = type=http-response,pattern=^https?:\/\/display-sc\.miguvideo\.com\/display\/v3\/static\/PERSONAL_CENTER$,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/refs/heads/main/Scripts/miguvideo/miguvideo_ads.js,requires-body=1,timeout=60,script-update-interval=86400
```

#### `cmp_block_093_ad`

- 说明：Generic JSON ad-field cleaner

```text
cmp_block_093_ad = type=http-response,pattern=^https:\/\/j1\.pupuapi\.com\/client\/search\/hot_keywords\/v3,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/PupuSplashAds.js,requires-body=1,timeout=60,script-update-interval=86400
```

#### `cmp_block_094_ad`

- 说明：Generic JSON ad-field cleaner

```text
cmp_block_094_ad = type=http-response,pattern=^https?:\/\/(?:webapi|miniapp)\.qmai\.cn\/web\/catering([0-9]-apiserver)?\/advertising\/ad\/advertiseInfo,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/qmai.js,requires-body=1,timeout=60,script-update-interval=86400
```

#### `cmp_block_096_ad`

- 说明：Generic JSON ad-field cleaner

```text
cmp_block_096_ad = type=http-response,pattern=^https?:\/\/haojia\.m\.smzdm\.com\/detail_modul\/user_related_modul\?,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/smzdm/smzdm_ads.js,requires-body=1,timeout=60,script-update-interval=86400
```

### `Rewrite/Sources/Script.conf`

#### `cmp_allad_018_coolapk`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_018_coolapk = type=http-response,pattern=^https?:\/\/api\.coolapk\.com\/v\d\/main\/(?:dataList|indexV|init),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/coolapk.js,script-update-interval=86400
```

#### `cmp_allad_023_dianping`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_023_dianping = type=http-response,pattern=^https?:\/\/ddplus\.meituan\.net\/v\d\/mss_\w+\/picassovc,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/dianping.js,script-update-interval=86400
```

#### `cmp_allad_029_amap`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_029_amap = type=http-response,pattern=^https?:\/\/m\d\.amap\.com\/ws\/shield\/search_business\/process\/marketingOperationStructured\?,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/amap.js,script-update-interval=86400
```

#### `cmp_allad_030_babytree`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_030_babytree = type=http-response,pattern=^https?:\/\/go\.babytree\.com\/go_pregnancy\/api\/(?:app_index|cms_column),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/babytree.js,script-update-interval=86400
```

#### `cmp_allad_032_mafengwo`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_032_mafengwo = type=http-response,pattern=^https?:\/\/mapi\.mafengwo\.cn\/user\/profile\/get_(?:list|profile),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/mafengwo.js,script-update-interval=86400
```

#### `cmp_allad_033_gaoding`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_033_gaoding = type=http-response,pattern=^https?:\/\/www\.gaoding\.com\/api\/v\d\/oc\/exhibitions\/template\/resources$,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/gaoding.js,script-update-interval=86400
```

#### `cmp_allad_034_pdd`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_034_pdd = type=http-response,pattern=^https?:\/\/api\.pinduoduo\.com\/api\/oak\/integration\/render,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/pdd.js,script-update-interval=86400
```

#### `cmp_allad_035_qidian`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_035_qidian = type=http-response,pattern=^https?:\/\/mage(v\d)?\.if\.qidian\.com\/argus\/api\/v\d\/(deeplink\/geturl|client\/getconf|bookshelf\/getHoverAdv|dailyrecommend\/getdailyrecommend|assembly\/toolbar|user\/getaccountpage),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/qidian.js,script-update-interval=86400
```

#### `cmp_allad_036_kuaishou`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_036_kuaishou = type=http-response,pattern=^https?:\/\/open\.e\.kuaishou\.com\/rest\/e\/v\d\/open\/univ$,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/adsense.js,script-update-interval=86400
```

#### `cmp_allad_037_freshippo`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_037_freshippo = type=http-response,pattern=^https?:\/\/acs\.m\.shyhhema\.com\/h5\/mtop\.wdk\.render\.query(?:index|my)page,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/freshippo.js,script-update-interval=86400
```

#### `cmp_allad_038_xunlei`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_038_xunlei = type=http-response,pattern=^https?:\/\/conf-m-ssl\.xunlei\.com\/external\/,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xunlei.js,script-update-interval=86400
```

#### `cmp_allad_039_cainiao`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_039_cainiao = type=http-response,pattern=^https?:\/\/cn-acs\.m\.cainiao\.com\/gw\/mtop\.cainiao\.nbpresentation\.(pickup\.empty\.page|protocol\.homepage)\.get,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/cainiao.js,script-update-interval=86400
```

#### `cmp_allad_040_zhuanzhuan`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_040_zhuanzhuan = type=http-response,pattern=^https?:\/\/app\.zhuanzhuan\.com\/zz\/v\d\/zzlogic\/mywxcontinenthomepage,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/zhuanzhuan.js,script-update-interval=86400
```

#### `cmp_allad_041_baidumap`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_041_baidumap = type=http-response,pattern=^https?:\/\/newclient\.map\.baidu\.com\/client\/phpui2\/\?qt=ads,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/baiduMap.js,script-update-interval=86400
```

#### `cmp_allad_042_ehaier`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_042_ehaier = type=http-response,pattern=^https?:\/\/zj\.haier\.net\/omsappapi\/resource\/v\d\/get\/resourceBag$,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/haier.js,script-update-interval=86400
```

#### `cmp_allad_045_xiaoyuzhoufm`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_045_xiaoyuzhoufm = type=http-response,pattern=^https?:\/\/api\.xiaoyuzhoufm\.com\/v\d\/discovery-feed\/list,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/xiaoyuzhoufm.js,script-update-interval=86400
```

#### `cmp_allad_047_peiyinxiu`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_047_peiyinxiu = type=http-response,pattern=^https?:\/\/iosapi\.peiyinxiu\.com\/Api\/Film\/GetConfigValue,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/peiyinxiu.js,script-update-interval=86400
```

#### `cmp_allad_048_jd`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_048_jd = type=http-response,pattern=^https?:\/\/api\.m\.jd\.com\/client\.action\?functionId=(?:deliverLayer|getTabHomeInfo|myOrderInfo|orderTrackBusiness|personinfoBusiness|start|welcomeHome|readCustomSurfaceList),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/jd.js,script-update-interval=86400
```

#### `cmp_allad_049_meituan`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_049_meituan = type=http-response,pattern=^https?:\/\/p\d\.meituan\.net\/linglong\/,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/meituan.js,script-update-interval=86400
```

#### `cmp_allad_050_reddit`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_050_reddit = type=http-response,pattern=^https?:\/\/gql(-fed)?\.reddit\.com,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/reddit.js,script-update-interval=86400
```

#### `cmp_allad_051_boohee`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_051_boohee = type=http-response,pattern=^https?:\/\/api\.boohee\.com\/open-interface\/v\d\/string\/market_page\?title=metabolism_config$,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/boohee.js,script-update-interval=86400
```

#### `cmp_allad_052_360cam`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_052_360cam = type=http-response,pattern=^https?:\/\/jia\.360\.cn\/conf\/v\d\.json,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/360cam.js,script-update-interval=86400
```

#### `cmp_allad_053_fliggy`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_053_fliggy = type=http-response,pattern=^https?:\/\/acs\.m\.taobao\.com\/gw\/mtop\.fliggy\.ssif\.pattern\.home,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/fliggy.js,script-update-interval=86400
```

#### `cmp_allad_054_1314zhilv`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_054_1314zhilv = type=http-response,pattern=^https?:\/\/www\.1314zhilv\.com\/ltsstnew\/(common\/getJGQIconNew|city\/getAllBannelByCity),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/ltsst.js,script-update-interval=86400
```

#### `cmp_allad_055_adunion`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_055_adunion = type=http-response,pattern=^https?:\/\/g\.alicdn\.com\/.*o2o-ad,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/alicdn.js,script-update-interval=86400
```

#### `cmp_allad_056_ppx`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_056_ppx = type=http-response,pattern=^https?:\/\/.+\.pipix\.com\/bds\/feed\/channel_list\/,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/ppx.js,script-update-interval=86400
```

#### `cmp_allad_059_quda`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_059_quda = type=http-response,pattern=^https?:\/\/iqushangwang\.8quan\.com\/index\.php\/i\/index\/index,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/quda.js,script-update-interval=86400
```

#### `cmp_allad_060_maimai`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_060_maimai = type=http-response,pattern=^https?:\/\/(h3\.)?open\.taou\.com\/maimai\/(feed|gossip)\/v\d\/(?:focus_feed|gossip_detail_comment|feed_detail_comment),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/maimai.js,script-update-interval=86400
```

#### `cmp_allad_061_foliday`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_061_foliday = type=http-response,pattern=^https?:\/\/apis\.folidaymall\.com\/online\/capi\/component\/getPageComponents,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/foliday.js,script-update-interval=86400
```

#### `cmp_allad_062_tuhu`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_062_tuhu = type=http-response,pattern=^https?:\/\/(cl-)?gateway\.tuhu\.cn(\/cl)?\/cl-common-api\/api\/personalCenter\/getCmsModuleList,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/tuhu.js,script-update-interval=86400
```

#### `cmp_allad_063_163youdao`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_063_163youdao = type=http-response,pattern=^https?:\/\/dict\.youdao\.com\/(homepage\/promotion|course\/tab\/home|homepage\/tile),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/163youdao.js,script-update-interval=86400
```

#### `cmp_allad_064_ys7`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_064_ys7 = type=http-response,pattern=^https?:\/\/\w+\.ys7\.com\/v\d\/valueadded\/operation\/config\/master\/station,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/ys7.js,script-update-interval=86400
```

#### `cmp_allad_065_flyert`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_065_flyert = type=http-response,pattern=^https?:\/\/www\.flyert(rip)?\.com(\.cn)?\/.*plugin,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/flyert.js,script-update-interval=86400
```

#### `cmp_allad_067_guiderank`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_067_guiderank = type=http-response,pattern=^https?:\/\/zone\.guiderank-app\.com\/guiderank-web\/app\/home\/getHomePageV,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/guiderank.js,script-update-interval=86400
```

#### `cmp_allad_068_mishop`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_068_mishop = type=http-response,pattern=^https?:\/\/api\.m\.mi\.com\/v\d\/order\/expressView,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/mishop.js,script-update-interval=86400
```

#### `cmp_allad_069_qbb`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_069_qbb = type=http-response,pattern=^https?:\/\/webapi\.qbb6\.com\/h5\/api\/lib\/internal\/append\/get,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/qbb.js,script-update-interval=86400
```

#### `cmp_allad_071_51cto`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_071_51cto = type=http-response,pattern=^https?:\/\/edu\.51cto\.com\/app\.php\?$,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/51cto.js,script-update-interval=86400
```

#### `cmp_allad_073_meituanwm`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_073_meituanwm = type=http-response,pattern=^https?:\/\/web\.meituan\.com\/api\/miniprogram\/tabbar\/all\/query,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/meituanwm.js,script-update-interval=86400
```

#### `cmp_allad_076_ithome`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_076_ithome = type=http-response,pattern=^https?:\/\/napi\.ithome\.com\/api\/(news\/index|topmenu\/getfeeds),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/ithome.js,script-update-interval=86400
```

#### `cmp_allad_077_eleme`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_077_eleme = type=http-response,pattern=^https?:\/\/waimai-guide\.ele\.me\/(gw|h5)\/mtop\.alsc\.eleme\.miniapp\.homepage,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/eleme.js,script-update-interval=86400
```

#### `cmp_allad_078_duitang`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_078_duitang = type=http-response,pattern=^https?:\/\/(www|api)\.duitang\.com\/napi\/settings\/,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/duitang.js,script-update-interval=86400
```

#### `cmp_allad_079_51job`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_079_51job = type=http-response,pattern=^https?:\/\/cupid\.51job(app)?\.com\/open\/my-page\/,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/51job.js,script-update-interval=86400
```

#### `cmp_allad_081_usmile`

- 说明：Generic JSON ad-field cleaner

```text
cmp_allad_081_usmile = type=http-response,pattern=^https?:\/\/www\.myusmile\.online\/user\/plaqueTopic\/selectByType,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/usmile.js,script-update-interval=86400
```

#### `cmp_block_086_ad`

- 说明：Generic JSON ad-field cleaner

```text
cmp_block_086_ad = type=http-response,pattern=^https?:\/\/gg\.caixin\.com\/s\?z=caixin&op=1&c=3362,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/caixin/caixinAd.js,requires-body=1,timeout=60,script-update-interval=86400
```

#### `cmp_block_089_ad`

- 说明：Generic JSON ad-field cleaner

```text
cmp_block_089_ad = type=http-response,pattern=^https:\/\/lawsonapi\.yorentown\.com\/portal\/app\/globalLaunch\/listAdvert,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/lawson.js,requires-body=1,timeout=60,script-update-interval=86400
```

#### `cmp_block_091_app`

- 说明：Generic JSON ad-field cleaner

```text
cmp_block_091_app = type=http-response,pattern=^https:\/\/config-service\.seeyouyima\.com\/api\/configs\/batch\?,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/meiyou/meiyou_ads.js,requires-body=1,timeout=60,script-update-interval=86400
```

#### `cmp_block_092_ad`

- 说明：Generic JSON ad-field cleaner

```text
cmp_block_092_ad = type=http-response,pattern=^https?:\/\/display-sc\.miguvideo\.com\/display\/v3\/static\/PERSONAL_CENTER$,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/refs/heads/main/Scripts/miguvideo/miguvideo_ads.js,requires-body=1,timeout=60,script-update-interval=86400
```

#### `cmp_block_093_ad`

- 说明：Generic JSON ad-field cleaner

```text
cmp_block_093_ad = type=http-response,pattern=^https:\/\/j1\.pupuapi\.com\/client\/search\/hot_keywords\/v3,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/PupuSplashAds.js,requires-body=1,timeout=60,script-update-interval=86400
```

#### `cmp_block_094_ad`

- 说明：Generic JSON ad-field cleaner

```text
cmp_block_094_ad = type=http-response,pattern=^https?:\/\/(?:webapi|miniapp)\.qmai\.cn\/web\/catering([0-9]-apiserver)?\/advertising\/ad\/advertiseInfo,script-path=https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/qmai.js,requires-body=1,timeout=60,script-update-interval=86400
```

#### `cmp_block_096_ad`

- 说明：Generic JSON ad-field cleaner

```text
cmp_block_096_ad = type=http-response,pattern=^https?:\/\/haojia\.m\.smzdm\.com\/detail_modul\/user_related_modul\?,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/smzdm/smzdm_ads.js,requires-body=1,timeout=60,script-update-interval=86400
```

## 不变范围

- 不动 Spotify。
- 不动 YouTube。
- 不动知乎增强与知乎 R-Store 条目。
- 不动 Tieba JSON / proto。
- 不动小红书、Cotti、RRTV、网易云音乐、12306、航旅纵横、搜狗输入法、韵达等复杂或高风险条目。
- 不动登录、支付、验证码、银行相关条目。
- 不合并复杂加密、持久化配置、会员权益、binary-body 脚本。
