// GrandpaNiu app-cleaner shadow runner
// Current mode: shadow/no-op. This script must not mutate response bodies until
// a specific App group is manually tested and explicitly promoted.

(function () {
  const DEFAULT_CONFIG = {
    version: "embedded-shadow-v1",
    mode: "shadow",
    safety: {
      defaultAction: "passThrough",
      failClosed: false,
      blockUnknown: false,
      forbiddenKeywords: [
        "login", "passport", "token", "cookie", "captcha", "payment", "pay",
        "bank", "security", "membership", "vip", "premium", "paywall"
      ]
    },
    groups: [
      {
        key: "qq-news-shadow",
        app: "QQ News",
        status: "shadow-only",
        replaceExisting: false,
        urlPatterns: [
          "news.ssp.qq.com/app",
          "r.inews.qq.com/getQQNewsUnreadList",
          "r.inews.qq.com/getTagFeedList",
          "r.inews.qq.com/gw/page/event_detail",
          "r.inews.qq.com/news_feed/hot_module_list"
        ],
        actions: []
      }
    ]
  };

  function getRequestUrl() {
    try {
      return ($request && $request.url) || "";
    } catch (_) {
      return "";
    }
  }

  function getBody() {
    try {
      return ($response && typeof $response.body === "string") ? $response.body : "";
    } catch (_) {
      return "";
    }
  }

  function isForbidden(url, config) {
    const lowered = String(url || "").toLowerCase();
    const tokens = (((config || {}).safety || {}).forbiddenKeywords) || [];
    return tokens.some(token => lowered.includes(String(token).toLowerCase()));
  }

  function matchGroup(url, config) {
    const groups = Array.isArray(config.groups) ? config.groups : [];
    return groups.find(group => {
      const patterns = Array.isArray(group.urlPatterns) ? group.urlPatterns : [];
      return patterns.some(pattern => String(url || "").includes(pattern));
    }) || null;
  }

  function doneUnchanged(body) {
    if (typeof $response !== "undefined" && typeof body === "string") {
      $done({ body });
    } else {
      $done({});
    }
  }

  function main() {
    const config = DEFAULT_CONFIG;
    const url = getRequestUrl();
    const body = getBody();

    if (!url || isForbidden(url, config)) {
      doneUnchanged(body);
      return;
    }

    const group = matchGroup(url, config);

    // Shadow mode intentionally does not mutate the body. It only verifies that
    // the unified runner can load and safely pass through matched traffic.
    if (!group || config.mode !== "active" || group.status !== "active") {
      doneUnchanged(body);
      return;
    }

    // Active mode is deliberately not implemented yet. Future cleaners must be
    // white-list based, App-specific, and covered by manual_test_log.md before
    // replacing old entries.
    doneUnchanged(body);
  }

  try {
    main();
  } catch (_) {
    try {
      doneUnchanged(getBody());
    } catch (e) {
      $done({});
    }
  }
})();
