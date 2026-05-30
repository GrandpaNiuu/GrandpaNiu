// GrandpaNiu app-cleaner active runner
// Active consolidation batches:
// - Batch 1: QQ News + VGTime
// - Batch 2: SQKB + 163News + XiaoHeiHe + Manner + Chaoge
// Unknown URLs, invalid JSON, or unexpected bodies pass through unchanged.

(function () {
  const VERSION = "2026-05-31-active-v2";

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

  function isQQNews(url) {
    return url.includes("news.ssp.qq.com/app") ||
      url.includes("r.inews.qq.com/getQQNewsUnreadList") ||
      url.includes("r.inews.qq.com/getTagFeedList") ||
      url.includes("r.inews.qq.com/gw/page/event_detail") ||
      url.includes("r.inews.qq.com/gw/page/channel_feed") ||
      url.includes("r.inews.qq.com/news_feed/hot_module_list");
  }

  function isVGTime(url) {
    return url.includes("app02.vgtime.com:8080/vgtime-app/api/v2/init/ad.json");
  }

  function isSQKB(url) {
    return url.includes("api.17gwx.com") && url.includes("/history/remind/list");
  }

  function is163News(url) {
    return url.includes("gw.m.163.com") && url.includes("/search/hot-word");
  }

  function isXiaoHeiHe(url) {
    return url.includes("api.xiaoheihe.cn/bbs/app/feeds/news");
  }

  function isManner(url) {
    return url.includes("triangle.wearemanner.com") && url.includes("/mp-api/") && url.includes("/ads");
  }

  function isChaoge(url) {
    return url.includes("mapi.chaogejiaoyu.com/api/outline/getAppBanner");
  }

  function cleanQQNews(bodyObject, url) {
    if (url.includes("r.inews.qq.com/gw/page/event_detail") || url.includes("r.inews.qq.com/gw/page/channel_feed")) {
      const widgets = bodyObject && bodyObject.data && bodyObject.data.widget_list;
      if (Array.isArray(widgets)) {
        bodyObject.data.widget_list = widgets.filter(item => !(item && item.widget_type === "ad_list"));
      }
      return bodyObject;
    }

    if (hasOwn(bodyObject, "adList")) {
      bodyObject.adList = null;
    }
    return bodyObject;
  }

  function cleanVGTime(bodyObject) {
    if (bodyObject && bodyObject.data && hasOwn(bodyObject.data, "ad")) {
      bodyObject.data.ad = null;
    }
    return bodyObject;
  }

  function cleanSQKB(bodyObject) {
    if (bodyObject && bodyObject.data) {
      bodyObject.data.recommend_coupon_list = [];
    }
    return bodyObject;
  }

  function clean163News(bodyObject) {
    if (bodyObject && bodyObject.data) {
      if (Array.isArray(bodyObject.data.special)) {
        bodyObject.data.special = [];
      }
      if (Array.isArray(bodyObject.data.RollhotWordList)) {
        bodyObject.data.RollhotWordList = [];
      }
    }
    return bodyObject;
  }

  function cleanXiaoHeiHe(bodyObject) {
    const links = bodyObject && bodyObject.result && bodyObject.result.links;
    if (Array.isArray(links)) {
      const fields = ["title", "ad_pm", "img_gif", "idea_id", "ad_report", "label", "source", "intranet_only", "ad_cm", "content_type", "protocol", "img", "ad_ratio"];
      links.forEach(link => {
        if (link && link.content_type === 27) {
          fields.forEach(field => { delete link[field]; });
        }
      });
    }
    return bodyObject;
  }

  function cleanManner(bodyObject) {
    const data = bodyObject && bodyObject.data;
    if (data) {
      [
        "myAnims", "homeAds", "orderPopups", "homePopups", "broadcasts", "menuPopups", "giftCardAds", "myPopups",
        "menuAnims", "orderAnims", "pmPopups", "goodsCategoryAds", "shopAds", "ooAds", "homeAnims", "startAds"
      ].forEach(key => setArrayEmpty(data, key));
    }
    return bodyObject;
  }

  function cleanChaoge(bodyObject, url) {
    if (!url.includes("adv_flag=1")) {
      return bodyObject;
    }
    if (Array.isArray(bodyObject && bodyObject.data)) {
      bodyObject.data = bodyObject.data.filter(item => !(item && item.adv_flag === "1"));
    }
    return bodyObject;
  }

  function main() {
    void VERSION;
    const url = requestUrl();
    const body = responseBody();
    if (!url || !body) {
      doneUnchanged(body);
      return;
    }

    const object = parseJsonOrNull(body);
    if (!object) {
      doneUnchanged(body);
      return;
    }

    if (isQQNews(url)) {
      doneJson(cleanQQNews(object, url));
      return;
    }

    if (isVGTime(url)) {
      doneJson(cleanVGTime(object));
      return;
    }

    if (isSQKB(url)) {
      doneJson(cleanSQKB(object));
      return;
    }

    if (is163News(url)) {
      doneJson(clean163News(object));
      return;
    }

    if (isXiaoHeiHe(url)) {
      doneJson(cleanXiaoHeiHe(object));
      return;
    }

    if (isManner(url)) {
      doneJson(cleanManner(object));
      return;
    }

    if (isChaoge(url)) {
      doneJson(cleanChaoge(object, url));
      return;
    }

    doneUnchanged(body);
  }

  try {
    main();
  } catch (_) {
    try { doneUnchanged(responseBody()); } catch (e) { $done({}); }
  }
})();
