/*
 * GrandpaNiu Zhihu enhanced ad cleaner
 * Scope: remove ad, promotion, commercial, sponsored and marketing cards/fields only.
 * Boundary: do not modify membership, payment, login, account identity or paid content fields.
 */

(() => {
  const input = typeof $response !== "undefined" ? $response.body : "";
  if (!input) {
    $done({});
    return;
  }

  let payload;
  try {
    payload = JSON.parse(input);
  } catch (_) {
    $done({});
    return;
  }

  const blockedExactKeys = new Set([
    "ad",
    "ads",
    "ad_info",
    "adInfo",
    "ad_extra",
    "adExtra",
    "ad_card",
    "adCard",
    "ad_slot",
    "adSlot",
    "ad_style",
    "adStyle",
    "ad_tracking",
    "adTracking",
    "advert",
    "advertise",
    "advertisement",
    "advertisements",
    "brand_ad",
    "brandAd",
    "commercial",
    "commercial_info",
    "commercialInfo",
    "promotion",
    "promotions",
    "promo",
    "marketing",
    "banner_ad",
    "bannerAd",
    "sponsor",
    "sponsored"
  ]);

  const protectedKeys = new Set([
    "vip",
    "svip",
    "member",
    "membership",
    "premium",
    "pay",
    "paid",
    "payment",
    "wallet",
    "balance",
    "account",
    "login",
    "auth",
    "token",
    "cookie",
    "salt",
    "yanxuan",
    "paid_content",
    "paidContent"
  ]);

  const metaKeys = new Set([
    "type",
    "card_type",
    "cardType",
    "item_type",
    "itemType",
    "content_type",
    "contentType",
    "business_type",
    "businessType",
    "template",
    "template_name",
    "templateName",
    "name",
    "label",
    "badge",
    "source",
    "reason",
    "recommend_reason",
    "recommendReason"
  ]);

  const adText = /(^|[^a-z])(ad|ads|advert|advertise|advertisement|commercial|promotion|promoted|sponsor|sponsored|brand_ad|banner_ad|feed_ad|native_ad)([^a-z]|$)|广告|推荐的广告|赞助|推广|商业推广|品牌推广/i;

  function hasProtectedKey(object) {
    return Object.keys(object).some((key) => protectedKeys.has(key));
  }

  function isAdCard(value) {
    if (!value || typeof value !== "object" || Array.isArray(value)) return false;

    if (hasProtectedKey(value)) return false;

    if (value.is_ad === true || value.isAd === true || value.has_ad === true || value.hasAd === true) return true;
    if (value.ad === true || value.ads === true) return true;

    for (const key of Object.keys(value)) {
      if (blockedExactKeys.has(key)) return true;
      if (/^(ad|ads|advert|commercial|promotion|sponsor)[A-Z_]/.test(key)) return true;
      if (/(^|_)(ad|ads|advert|commercial|promotion|sponsor)(_|$)/i.test(key)) return true;
    }

    for (const key of metaKeys) {
      const raw = value[key];
      if (typeof raw === "string" && adText.test(raw)) return true;
    }

    if (typeof value.creative_id === "string" || typeof value.creativeId === "string") return true;
    if (typeof value.ad_id === "string" || typeof value.adId === "string") return true;

    return false;
  }

  function clean(value, inArray = false) {
    if (Array.isArray(value)) {
      const result = [];
      for (const item of value) {
        if (isAdCard(item)) continue;
        result.push(clean(item, true));
      }
      return result;
    }

    if (!value || typeof value !== "object") return value;

    if (inArray && isAdCard(value)) return null;

    const output = {};
    for (const [key, child] of Object.entries(value)) {
      if (blockedExactKeys.has(key)) continue;
      if (!protectedKeys.has(key) && /^(ad|ads|advert|commercial|promotion|sponsor)[A-Z_]/.test(key)) continue;
      if (!protectedKeys.has(key) && /(^|_)(ad|ads|advert|commercial|promotion|sponsor)(_|$)/i.test(key)) continue;
      const cleaned = clean(child, false);
      if (cleaned !== null) output[key] = cleaned;
    }
    return output;
  }

  $done({ body: JSON.stringify(clean(payload)) });
})();
