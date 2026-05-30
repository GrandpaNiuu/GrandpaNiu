// GrandpaNiu app-cleaner active runner
// Active consolidation batches:
// - Batch 1: QQ News + VGTime
// - Batch 2: SQKB + 163News + XiaoHeiHe + Manner + Chaoge
// - Batch 3: SMZDM + Taobao + JuneYaoAir + DDXQ + ZSGJ
// - Batch 4: KKMH + Goofish + XMly + Didi
// - Batch 5: generic low-risk JSON ad-field cleaner for selected app endpoints
// Unknown URLs, invalid JSON, or unexpected bodies pass through unchanged.

(function () {
  const VERSION = "2026-05-31-active-v5";

  const GENERIC_HOST_TOKENS = [
    "api.coolapk.com", "ddplus.meituan.net", "m.amap.com", "go.babytree.com", "mapi.mafengwo.cn",
    "www.gaoding.com", "api.pinduoduo.com", "qidian.com", "kuaishou.com", "shyhhema.com",
    "xunlei.com", "cainiao.com", "zhuanzhuan.com", "map.baidu.com", "haier.net",
    "xiaoyuzhoufm.com", "peiyinxiu.com", "api.m.jd.com", "p.meituan.net", "reddit.com",
    "boohee.com", "jia.360.cn", "acs.m.taobao.com", "1314zhilv.com", "alicdn.com",
    "pipix.com", "8quan.com", "open.taou.com", "folidaymall.com", "tuhu.cn",
    "youdao.com", "ys7.com", "flyert", "guiderank-app.com", "mi.com",
    "qbb6.com", "51cto.com", "web.meituan.com", "ele.me", "duitang.com",
    "51job", "myusmile", "caixin.com", "lawsonapi.yorentown.com", "seeyouyima.com",
    "miguvideo.com", "pupuapi.com", "qmai.cn"
  ];

  const GENERIC_DROP_KEYS = new Set([
    "ad", "ads", "adList", "ad_list", "adInfo", "ad_info", "adInfos", "advert", "adverts", "advertise",
    "advertisement", "advertisements", "banner", "banners", "bannerList", "banner_list", "splash", "splashAd",
    "splash_ad", "popup", "popups", "popUp", "popupsList", "popUpList", "floatAd", "floatingAd", "floatingInfo",
    "promotion", "promotions", "marketing", "marketingInfo", "marketing_info", "operation", "operationAd",
    "operation_ad", "activityAd", "activity_ad", "recommendAd", "recommend_ad", "feedAd", "feed_ad", "cardAd",
    "card_ad", "topBanner", "top_banner", "bottomAd", "bottom_ad", "interstitial", "commercial", "commercials"
  ]);

  const GENERIC_FILTER_KEYS = [
    "isAd", "is_ad", "adInfo", "ad_info", "adType", "ad_type", "adid", "adId", "ad_mark", "adMark",
    "bizType", "moduleType", "contentType", "content_type", "templateType", "template_type", "displayClass"
  ];

  function requestUrl() {
    try { return ($request && $request.url) || ""; } catch (_) { return ""; }
  }

  function responseBody() {
    try { return ($response && typeof $response.body === "string") ? $response.body : ""; } catch (_) { return ""; }
  }

  function doneUnchanged(body) {
    if (typeof $response !== "undefined" && typeof body === "string") {
      $done({ body });
    } else {
      $done({});
    }
  }

  function doneBody(body) {
    $done({ body });
  }

  function doneJson(object) {
    $done({ body: JSON.stringify(object) });
  }

  function parseJsonOrNull(body) {
    try { return JSON.parse(body); } catch (_) { return null; }
  }

  function hasOwn(object, key) {
    return Object.prototype.hasOwnProperty.call(object || {}, key);
  }

  function setArrayEmpty(object, key) {
    if (object && Array.isArray(object[key])) {
      object[key] = [];
    }
  }

  function removeKey(object, key) {
    if (object && hasOwn(object, key)) {
      delete object[key];
    }
  }

  function removeObjectsWith(object, key, targets) {
    if (Array.isArray(object)) {
      return object.filter(item => !item || !item[key] || !targets.includes(item[key]));
    }
    if (object && typeof object === "object") {
      Object.keys(object).forEach(k => {
        if (object[k] && typeof object[k] === "object") {
          if (object[k][key] && targets.includes(object[k][key])) {
            delete object[k];
          } else {
            object[k] = removeObjectsWith(object[k], key, targets);
          }
        }
      });
    }
    return object;
  }

  function looksLikeAdValue(value) {
    if (value === true) return true;
    const text = String(value || "").toLowerCase();
    if (!text) return false;
    return text === "ad" || text === "ads" || text === "advert" || text === "advertise" ||
      text === "advertisement" || text === "splash" || text === "popup" || text === "mix_ad" ||
      text === "feed_ad" || text === "commercial" || text === "promotion" || text.includes("_ad") ||
      text.includes("-ad") || text.includes("advert") || text.includes("广告") || text.includes("推广");
  }

  function shouldDropArrayItem(item) {
    if (!item || typeof item !== "object") return false;
    for (const key of GENERIC_FILTER_KEYS) {
      if (hasOwn(item, key) && looksLikeAdValue(item[key])) return true;
    }
    if (typeof item.title === "string" && /广告|推广|福利|优惠商城/.test(item.title)) return true;
    if (typeof item.name === "string" && /广告|推广/.test(item.name)) return true;
    return false;
  }

  function genericAdFieldClean(value, depth) {
    if (depth > 8 || value == null) return value;
    if (Array.isArray(value)) {
      return value.filter(item => !shouldDropArrayItem(item)).map(item => genericAdFieldClean(item, depth + 1));
    }
    if (typeof value !== "object") return value;

    Object.keys(value).forEach(key => {
      if (GENERIC_DROP_KEYS.has(key) || /^ad[A-Z_]/.test(key) || /^ads[A-Z_]/.test(key) || /(^|_)(ad|ads|advert|splash|popup|banner)($|_)/i.test(key)) {
        delete value[key];
        return;
      }
      value[key] = genericAdFieldClean(value[key], depth + 1);
    });
    return value;
  }

  function isGenericJsonBatch(url) {
    return GENERIC_HOST_TOKENS.some(token => url.includes(token));
  }

  function isQQNews(url) {
    return url.includes("news.ssp.qq.com/app") ||
      url.includes("r.inews.qq.com/getQQNewsUnreadList") ||
      url.includes("r.inews.qq.com/getTagFeedList") ||
      url.includes("r.inews.qq.com/gw/page/event_detail") ||
      url.includes("r.inews.qq.com/gw/page/channel_feed") ||
      url.includes("r.inews.qq.com/news_feed/hot_module_list");
  }

  function isVGTime(url) { return url.includes("app02.vgtime.com:8080/vgtime-app/api/v2/init/ad.json"); }
  function isSQKB(url) { return url.includes("api.17gwx.com") && url.includes("/history/remind/list"); }
  function is163News(url) { return url.includes("gw.m.163.com") && url.includes("/search/hot-word"); }
  function isXiaoHeiHe(url) { return url.includes("api.xiaoheihe.cn/bbs/app/feeds/news"); }
  function isManner(url) { return url.includes("triangle.wearemanner.com") && url.includes("/mp-api/") && url.includes("/ads"); }
  function isChaoge(url) { return url.includes("mapi.chaogejiaoyu.com/api/outline/getAppBanner"); }
  function isSMZDM(url) { return url.includes("haojia.m.smzdm.com/detail_modul/user_related_modul"); }
  function isTaobao(url) { return url.includes("poplayer.template.alibaba.com"); }
  function isJuneYaoAir(url) { return url.includes("hoapp.juneyaoair.com/data/index/getPictureList"); }
  function isDDXQ(url) { return url.includes("user.api.ddxq.mobi/userportal-service/api/") && url.includes("/user/queryMyPage"); }
  function isZSGJ(url) { return url.includes("wx.mygolbs.com/WxBusServer/ApiData.do"); }
  function isKKMH(url) { return url.includes("api.kkmh.com") || url.includes("cdn-api.kkmh.com"); }
  function isGoofish(url) { return url.includes("acs.m.goofish.com") || url.includes("g-acs.m.goofish.com"); }
  function isXMly(url) { return url.includes(".xima") && url.includes(".com/"); }
  function isDidi(url) { return url.includes("diditaxi.com.cn") || url.includes("common.diditaxi.com.cn"); }

  function cleanQQNews(bodyObject, url) {
    if (url.includes("r.inews.qq.com/gw/page/event_detail") || url.includes("r.inews.qq.com/gw/page/channel_feed")) {
      const widgets = bodyObject && bodyObject.data && bodyObject.data.widget_list;
      if (Array.isArray(widgets)) bodyObject.data.widget_list = widgets.filter(item => !(item && item.widget_type === "ad_list"));
      return bodyObject;
    }
    if (hasOwn(bodyObject, "adList")) bodyObject.adList = null;
    return bodyObject;
  }

  function cleanVGTime(bodyObject) {
    if (bodyObject && bodyObject.data && hasOwn(bodyObject.data, "ad")) bodyObject.data.ad = null;
    return bodyObject;
  }

  function cleanSQKB(bodyObject) {
    if (bodyObject && bodyObject.data) bodyObject.data.recommend_coupon_list = [];
    return bodyObject;
  }

  function clean163News(bodyObject) {
    if (bodyObject && bodyObject.data) {
      if (Array.isArray(bodyObject.data.special)) bodyObject.data.special = [];
      if (Array.isArray(bodyObject.data.RollhotWordList)) bodyObject.data.RollhotWordList = [];
    }
    return bodyObject;
  }

  function cleanXiaoHeiHe(bodyObject) {
    const links = bodyObject && bodyObject.result && bodyObject.result.links;
    if (Array.isArray(links)) {
      const fields = ["title", "ad_pm", "img_gif", "idea_id", "ad_report", "label", "source", "intranet_only", "ad_cm", "content_type", "protocol", "img", "ad_ratio"];
      links.forEach(link => { if (link && link.content_type === 27) fields.forEach(field => { delete link[field]; }); });
    }
    return bodyObject;
  }

  function cleanManner(bodyObject) {
    const data = bodyObject && bodyObject.data;
    if (data) ["myAnims", "homeAds", "orderPopups", "homePopups", "broadcasts", "menuPopups", "giftCardAds", "myPopups", "menuAnims", "orderAnims", "pmPopups", "goodsCategoryAds", "shopAds", "ooAds", "homeAnims", "startAds"].forEach(key => setArrayEmpty(data, key));
    return bodyObject;
  }

  function cleanChaoge(bodyObject, url) {
    if (!url.includes("adv_flag=1")) return bodyObject;
    if (Array.isArray(bodyObject && bodyObject.data)) bodyObject.data = bodyObject.data.filter(item => !(item && item.adv_flag === "1"));
    return bodyObject;
  }

  function cleanSMZDM(bodyObject) { if (bodyObject && bodyObject.data) removeKey(bodyObject.data, "super_coupon"); return bodyObject; }

  function cleanTaobao(bodyObject) {
    if (bodyObject && bodyObject.res) { setArrayEmpty(bodyObject.res, "images"); setArrayEmpty(bodyObject.res, "videos"); }
    if (bodyObject && hasOwn(bodyObject, "enable")) bodyObject.enable = false;
    if (bodyObject && bodyObject.mainRes) setArrayEmpty(bodyObject.mainRes, "images");
    return bodyObject;
  }

  function cleanJuneYaoAir(bodyObject) {
    if (bodyObject && Array.isArray(bodyObject.objData)) bodyObject.objData = bodyObject.objData.filter(item => !(item && String(item.picLocation || "").includes("POSITION_POP")) && !(item && String(item.picLocation || "").includes("FLOATING")));
    return bodyObject;
  }

  function cleanDDXQ(bodyObject) {
    const data = bodyObject && bodyObject.data;
    if (data && Array.isArray(data.advertList)) data.advertList = data.advertList.filter(item => item && /福利中心|叮咚榜单|查添加剂|好货百科/.test(String(item.title || "")));
    if (data && Array.isArray(data.links)) data.links.splice(10);
    return bodyObject;
  }

  function cleanZSGJRaw(body) { return String(body || "").replace(/Ad":1/g, 'Ad":0').replace(/Ad_ab":1/g, 'Ad_ab":0'); }

  function cleanKKMH(bodyObject, url) {
    if (url.includes("/ironman/discovery") && url.includes("/tab_list")) return removeObjectsWith(bodyObject, "title", ["KK评委", "2024新漫报到", "VIP"]);
    if (url.includes("/graph/homepage/comicVideo") && url.includes("/configs")) return removeObjectsWith(bodyObject, "desc", ["超级漫画节", "在kk当评委", "屈臣氏·KKCOS大赏", "KK朋友圈", "KK运势"]);
    if (url.includes("/ironman/comic/recommend") && bodyObject && bodyObject.data) ["operation_float_ball", "topic_goods", "total_coupon", "share_comics_page_lottery"].forEach(key => removeKey(bodyObject.data, key));
    if (url.includes("/graph/unified_feed") && bodyObject && bodyObject.data && Array.isArray(bodyObject.data.universalModels)) {
      bodyObject.data.universalModels.forEach(model => { removeKey(model, "loopBanner"); if (model && model.post && Array.isArray(model.post.promotions) && model.post.promotions[0] && model.post.promotions[0].type === 4) delete model.post.promotions; });
    }
    return bodyObject;
  }

  function cleanGoofish(bodyObject, url) {
    if (!bodyObject || !bodyObject.data) return bodyObject;
    if (url.includes("/mtop.taobao.idlehome.home.nextfresh")) {
      removeKey(bodyObject.data, "widgetReturnDO"); removeKey(bodyObject.data, "bannerReturnDO");
      if (Array.isArray(bodyObject.data.sections)) {
        const excludeNames = ["fish_home_yunying_card_d3", "idlefish_seafood_market", "fish_home_chat_room"];
        bodyObject.data.sections = bodyObject.data.sections.filter(section => { const bizType = section && section.data && section.data.bizType; const name = section && section.template && section.template.name; return !(bizType === "AD" || bizType === "homepage" || excludeNames.includes(name)); });
      }
    } else if (url.includes("/mtop.taobao.idle.local.home")) {
      if (Array.isArray(bodyObject.data.sections)) bodyObject.data.sections = bodyObject.data.sections.filter(section => !(section && section.data && section.data.bizType === "AD"));
    } else if (url.includes("/mtop.taobao.idle.home.whale.modulet") && bodyObject.data.container) removeKey(bodyObject.data.container, "sections");
    return bodyObject;
  }

  function cleanXMly(bodyObject, url) {
    if (url.includes("discovery-category/customCategories")) {
      const keep = item => item && ["recommend", "template_category", "single_category"].includes(item.itemType) && item.categoryId !== 1005;
      if (Array.isArray(bodyObject.customCategoryList)) bodyObject.customCategoryList = bodyObject.customCategoryList.filter(keep);
      if (Array.isArray(bodyObject.defaultTabList)) bodyObject.defaultTabList = bodyObject.defaultTabList.filter(keep);
    } else if (url.includes("discovery-category") && url.includes("/category")) {
      if (bodyObject.focusImages && bodyObject.focusImages.data) bodyObject.focusImages.data = bodyObject.focusImages.data.filter(item => item && String(item.realLink || "").includes("open") && !item.isAd);
    } else if (url.includes("focus-mobile/focusPic")) {
      const data = bodyObject.header && bodyObject.header[0] && bodyObject.header[0].item && bodyObject.header[0].item.list && bodyObject.header[0].item.list[0] && bodyObject.header[0].item.list[0].data;
      if (Array.isArray(data)) bodyObject.header[0].item.list[0].data = data.filter(item => item && String(item.realLink || "").includes("open") && !item.isAd);
    } else if (url.includes("discovery-feed") && url.includes("/mix")) {
      if (Array.isArray(bodyObject.header) && bodyObject.header.length === 2) delete bodyObject.header[0];
      if (Array.isArray(bodyObject.body)) bodyObject.body = bodyObject.body.filter(item => !(item && item.item && item.item.adInfo) && !(item && item.item && item.item.moduleType === "mix_ad") && !(item && item.displayClass === "bigCard"));
    } else if (url.includes("mobile-user") && url.includes("/homePage")) {
      const entrances = bodyObject.data && bodyObject.data.serviceModule && bodyObject.data.serviceModule.entrances;
      if (Array.isArray(entrances)) bodyObject.data.serviceModule.entrances = entrances.filter(item => item && [210, 213, 215].includes(item.id));
    }
    return bodyObject;
  }

  function cleanDidi(bodyObject, url) {
    const data = bodyObject && bodyObject.data;
    if (!data) return bodyObject;
    if (url.includes("/other/pGetSceneList")) {
      if (Array.isArray(data.scene_list)) data.scene_list = data.scene_list.filter(item => item && item.text !== "优惠商城");
      if (Array.isArray(data.show_data)) data.show_data.forEach(block => { if (Array.isArray(block.scene_ids)) block.scene_ids = block.scene_ids.filter(id => id !== "scene_coupon_mall"); });
    } else if (url.includes("/homepage/v") && url.includes("/core")) {
      const nav = data.order_cards && data.order_cards.nav_list_card && data.order_cards.nav_list_card.data;
      if (Array.isArray(nav)) data.order_cards.nav_list_card.data = nav.filter(item => item && ["dache_anycar", "driverservice", "bike"].includes(item.nav_id));
      const bottom = data.disorder_cards && data.disorder_cards.bottom_nav_list && data.disorder_cards.bottom_nav_list.data;
      if (Array.isArray(bottom)) data.disorder_cards.bottom_nav_list.data = bottom.filter(item => item && ["v6x_home", "user_center"].includes(item.id));
    } else if (url.includes("/ota/na/yuantu/infoList")) {
      const banner = data.disorder_cards && data.disorder_cards.top_banner_card && data.disorder_cards.top_banner_card.data;
      if (Array.isArray(banner) && banner[0] && banner[0].T === "yuentu_top_banner") banner.splice(0, 1);
    } else if (url.includes("/usercenter/me") && Array.isArray(data.cards)) {
      const excludedTitles = ["天天领福利", "金融服务", "更多服务", "企业服务", "安全中心"];
      data.cards = data.cards.filter(card => card && !excludedTitles.includes(card.title));
      data.cards.forEach(card => { if (card && card.tag === "wallet") { if (Array.isArray(card.items)) card.items = card.items.filter(item => item && item.title === "优惠券"); if (card.card_type === 4 && Array.isArray(card.bottom_items)) card.bottom_items = card.bottom_items.filter(item => item && ["省钱套餐", "天天神券"].includes(item.title)); } });
    }
    return bodyObject;
  }

  function main() {
    void VERSION;
    const url = requestUrl();
    const body = responseBody();
    if (!url || !body) { doneUnchanged(body); return; }

    if (isZSGJ(url)) { doneBody(cleanZSGJRaw(body)); return; }

    const object = parseJsonOrNull(body);
    if (!object) { doneUnchanged(body); return; }

    if (isQQNews(url)) { doneJson(cleanQQNews(object, url)); return; }
    if (isVGTime(url)) { doneJson(cleanVGTime(object)); return; }
    if (isSQKB(url)) { doneJson(cleanSQKB(object)); return; }
    if (is163News(url)) { doneJson(clean163News(object)); return; }
    if (isXiaoHeiHe(url)) { doneJson(cleanXiaoHeiHe(object)); return; }
    if (isManner(url)) { doneJson(cleanManner(object)); return; }
    if (isChaoge(url)) { doneJson(cleanChaoge(object, url)); return; }
    if (isSMZDM(url)) { doneJson(cleanSMZDM(object)); return; }
    if (isTaobao(url)) { doneJson(cleanTaobao(object)); return; }
    if (isJuneYaoAir(url)) { doneJson(cleanJuneYaoAir(object)); return; }
    if (isDDXQ(url)) { doneJson(cleanDDXQ(object)); return; }
    if (isKKMH(url)) { doneJson(cleanKKMH(object, url)); return; }
    if (isGoofish(url)) { doneJson(cleanGoofish(object, url)); return; }
    if (isXMly(url)) { doneJson(cleanXMly(object, url)); return; }
    if (isDidi(url)) { doneJson(cleanDidi(object, url)); return; }
    if (isGenericJsonBatch(url)) { doneJson(genericAdFieldClean(object, 0)); return; }

    doneUnchanged(body);
  }

  try {
    main();
  } catch (_) {
    try { doneUnchanged(responseBody()); } catch (e) { $done({}); }
  }
})();
