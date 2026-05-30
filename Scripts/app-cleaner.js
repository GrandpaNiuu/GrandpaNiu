// GrandpaNiu app-cleaner active runner
// First active batch: QQ News + VGTime only.
// Unknown URLs, invalid JSON, or unexpected bodies pass through unchanged.

(function () {
  const VERSION = "2026-05-31-active-v1";

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

  function cleanQQNews(bodyObject, url) {
    if (url.includes("r.inews.qq.com/gw/page/event_detail") || url.includes("r.inews.qq.com/gw/page/channel_feed")) {
      const widgets = bodyObject && bodyObject.data && bodyObject.data.widget_list;
      if (Array.isArray(widgets)) {
        bodyObject.data.widget_list = widgets.filter(item => !(item && item.widget_type === "ad_list"));
      }
      return bodyObject;
    }

    if (Object.prototype.hasOwnProperty.call(bodyObject || {}, "adList")) {
      bodyObject.adList = null;
    }
    return bodyObject;
  }

  function cleanVGTime(bodyObject) {
    if (bodyObject && bodyObject.data && Object.prototype.hasOwnProperty.call(bodyObject.data, "ad")) {
      bodyObject.data.ad = null;
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

    doneUnchanged(body);
  }

  try {
    main();
  } catch (_) {
    try { doneUnchanged(responseBody()); } catch (e) { $done({}); }
  }
})();
