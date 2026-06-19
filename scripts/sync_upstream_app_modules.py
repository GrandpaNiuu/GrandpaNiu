#!/usr/bin/env python3
"""Discover and sync upstream app-scoped module sources.

This script owns Rewrite/Remotes/app-modules.json and rewrites only
Rewrite/Sources/Apps/*.conf targets. Release artifacts are intentionally left to
Rewrite/Generator/Builder.py so generated files stay source-first.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "Rewrite" / "Remotes" / "app-modules.json"
DEFAULT_APPS_DIR = ROOT / "Rewrite" / "Sources" / "Apps"
DEFAULT_REPORT = ROOT / "reports" / "upstream_app_module_sync_report.md"
BACKUP_ROOT = ROOT / "backup" / "upstream-app-modules"
KELEE_CATALOG_URL = "https://hub.kelee.one/list.json"
KELEE_UPSTREAM_PROJECT = "Kelee PluginHub"
KELEE_USER_AGENT = "Loon/889 CFNetwork/1496.0.7 Darwin/23.5.0"
SPOTIFY_STABLE_UPSTREAM_URL = "https://raw.githubusercontent.com/app2smile/rules/master/module/spotify.module"

ALLOWED_SECTIONS = [
    "General",
    "Rule",
    "URL Rewrite",
    "Header Rewrite",
    "Body Rewrite",
    "Map Local",
    "Script",
    "MITM",
]
SOURCE_SECTIONS = ALLOWED_SECTIONS + ["Rewrite"]
SECTION_ALIASES = {
    "mitm": "MITM",
    "rewrite": "Rewrite",
    "rewrite_local": "Rewrite",
    "rewrite_remote": "Rewrite",
    "filter_local": "Rule",
    "filter_remote": "Rule",
    "url rewrite": "URL Rewrite",
    "header rewrite": "Header Rewrite",
    "body rewrite": "Body Rewrite",
    "map local": "Map Local",
}
DROP_META_KEYS = {"icon", "category", "openurl", "homepage", "author", "loon_version", "tag"}
REQUIRED_RECORD_KEYS = [
    "id",
    "name",
    "source_url",
    "target",
    "enabled",
    "direct_commit",
    "risk",
    "backup",
    "upstream_project",
    "last_sync_mode",
]
CORE_BACKUP_IDS = {"spotify", "youtube", "zhihu", "wechat", "weibo", "bilibili"}
HIGH_RISK_IDS = CORE_BACKUP_IDS | {"terabox"}
TRUSTED_REPOSITORIES = ["QingRex/LoonKissSurge", "app2smile/rules", "Maasea/sgmodule", "fmz200/wool_scripts"]
KELEE_PINNED_REMOTE_SCRIPT_IDS = {"spotify", "youtube"}
AD_TAG = "\u53bb\u5e7f\u544a"
KELEE_EXCLUDED_BASES = {
    "Block_HTTPDNS.lpx",
    "BlockAdvertisers.lpx",
    "Google.lpx",
    "QQ_Redirect.lpx",
    "QuickSearch.lpx",
    "Remove_ads_by_keli.lpx",
}
KELEE_ID_OVERRIDES = {
    "Amap_remove_ads.lpx": "amap",
    "BaiduSearchWebpage_remove_ads.lpx": "baidu",
    "Bilibili_remove_ads.lpx": "bilibili",
    "BiliComic_remove_ads.lpx": "bilibili-comic",
    "ColorfulClouds_remove_ads.lpx": "caiyun-weather",
    "CosmosPodcast_remove_ads.lpx": "xiaoyuzhou",
    "Himalaya_remove_ads.lpx": "ximalaya",
    "IThome_remove_ads.lpx": "ithome",
    "JD_remove_ads.lpx": "jd",
    "Keep_remove_ads.lpx": "keep",
    "MangoTV_remove_ads.lpx": "mgtv",
    "NeteaseCloudMusic_remove_ads.lpx": "netease-music",
    "PinDuoDuo_remove_ads.lpx": "pinduoduo",
    "QQMusic_remove_ads.lpx": "qqmusic",
    "QuarkBrowser_remove_ads.lpx": "quark",
    "QuarkScanking_remove_ads.lpx": "quark-scan",
    "RedPaper_remove_ads.lpx": "rednote",
    "Reddit_remove_ads.lpx": "reddit",
    "Soul_remove_ads.lpx": "soul",
    "Spotify_remove_ads.lpx": "spotify",
    "Taobao_remove_ads.lpx": "taobao",
    "TeraBox_remove_ads.lpx": "terabox",
    "Tieba_remove_ads.lpx": "tieba",
    "Umetrip_remove_ads.lpx": "umetrip",
    "Weibo_intl_remove_ads.lpx": "weibo-intl",
    "Weibo_remove_ads.lpx": "weibo",
    "Weixin_Official_Accounts_remove_ads.lpx": "wechat-official-accounts",
    "WexinMiniPrograms_Remove_ads.lpx": "wechat-mini-programs",
    "WPS_Documents_remove_ads.lpx": "wps",
    "YouKu_Video_remove_ads.lpx": "youku",
    "YouTube_remove_ads.lpx": "youtube",
    "Zhihu_remove_ads.lpx": "zhihu",
    "smzdm_remove_ads.lpx": "zdm",
}
HIGH_RISK_NAME_TOKENS = (
    "12306",
    "bank",
    "pay",
    "wallet",
    "\u4fdd\u9669",
    "\u51fa\u884c",
    "\u5730\u56fe",
    "\u9152\u5e97",
    "\u65c5\u884c",
    "\u673a\u7968",
    "\u7968",
    "\u652f\u4ed8",
    "\u6536\u94f6",
    "\u94f6\u884c",
    "\u90ae\u7bb1",
    "\u4e91\u76d8",
    "\u7f51\u76d8",
    "\u8d2d\u7269",
)

URL_RE = re.compile(r"https?://[^\s,\"'<>]+")
SECTION_RE = re.compile(r"^\s*\[([^\]]+)\]\s*$")
META_RE = re.compile(r"^\s*#!([^=\s]+)\s*=\s*(.*)$")
COMMENT_FIELD_RE = re.compile(r"^\s*#\s*([A-Za-z0-9_-]+)\s*:\s*(.+?)\s*$")
SCRIPT_PATH_RE = re.compile(r"script-path=(https?://[^,\s]+)", re.IGNORECASE)
RULE_SET_RE = re.compile(r"RULE-SET,(https?://[^,\s]+)", re.IGNORECASE)
RAW_MODULE_HINT_RE = re.compile(r"\.(?:sgmodule|module|conf|lpx|snippet)(?:$|[?#])", re.IGNORECASE)
QX_RULE_TYPES = {
    "host-suffix": "DOMAIN-SUFFIX",
    "host": "DOMAIN",
    "host-keyword": "DOMAIN-KEYWORD",
    "ip-cidr": "IP-CIDR",
    "ip-cidr6": "IP-CIDR6",
    "geoip": "GEOIP",
    "user-agent": "USER-AGENT",
}
QX_REJECT_ACTIONS = {
    "reject",
    "reject-200",
    "reject-dict",
    "reject-img",
    "reject-array",
    "reject-drop",
    "reject-ttl",
    "reject-tinygif",
}
QX_SCRIPT_ACTIONS = {
    "script-response-body": ("http-response", True),
    "script-request-body": ("http-request", True),
    "script-response-header": ("http-response", False),
    "script-request-header": ("http-request", False),
}
EXAMPLE_TOKENS = ("this-is-an-example.com", "example.com")
SUSPICIOUS_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        r"(vip|premium|member(?:ship)?).{0,12}(unlock|crack|free|true)",
        r"(unlock|crack|bypass|remove).{0,12}(vip|premium|member(?:ship)?)",
        r"(receipt|entitlement|in[_-]?app[_-]?purchase|purchase[_-]?receipt)",
        r"(payment|pay|bank|alipay|wechatpay).{0,12}(bypass|crack|unlock)",
        r"(login|passport|auth).{0,12}(bypass|crack|unlock)",
        r"(account|账号).{0,12}(share|共享)",
        r"(会员|付费|订阅).{0,12}(解锁|破解|绕过|免费)",
        r"(支付|登录|验证码|银行).{0,12}(绕过|破解|解锁)",
    )
]
PROTECTED_REJECT_TOKENS = (
    "api.biliapi",
    "app.biliapi",
    "api.iqiyi.com",
    "httpdns",
    "hdns.ksyun.com",
    "adgw.alipay.com",
    "amdc.alipay.com",
    "amdc-sibling.alipay.com.cn",
    "mobiledc.stable.alipay.net",
    "rtms.alipay.com",
    "api.verify.mob.com",
    "log-verify.mob.com",
    "mdap.wallet.pbcdci.cn",
    "mdc.wallet.pbcdci.cn",
    "baidustatic.com",
    "zijieapi.com",
    "zijieapi.net",
    "zijiecdn.com",
    "snssdk.com",
)
PROTECTED_MITM_HOST_TOKENS = ("httpdns", "hdns.ksyun.com")
BILIBILI_SPARKLE_SOURCE_URL = "https://raw.githubusercontent.com/kokoryh/Sparkle/master/release/surge/module/bilibili.sgmodule"
BILIBILI_ARGUMENT_LINES = [
    "#!arguments=动态最常访问:auto,创作中心:0,过滤置顶评论广告:1,优化评论区加载:bilibili.request,空降助手:bilibili.airborne,空降助手策略:DIRECT,日志等级:4",
    "#!arguments-desc=动态最常访问\\n- auto: 仅当列表中存在直播状态时显示\\n- show: 始终显示\\n- hide: 始终隐藏\\n\\n创作中心\\n- 0: 隐藏\\n- 1: 显示\\n\\n过滤置顶评论广告\\n- 0: 关闭\\n- 1: 开启\\n\\n优化评论区加载: 默认开启，配置为 # 时关闭\\n\\n空降助手: 默认开启，配置为 # 时关闭\\n\\n空降助手策略: 默认直连，可改为你的代理策略\\n\\n日志等级\\n- 1: DEBUG\\n- 2: INFO\\n- 3: WARN\\n- 4: ERROR\\n- 5: OFF",
]
BILIBILI_UNSAFE_RULE_PREFIXES = (
    "DOMAIN,api.biliapi.com,REJECT",
    "DOMAIN,app.biliapi.com,REJECT",
    "DOMAIN,api.biliapi.net,REJECT",
    "DOMAIN,app.biliapi.net,REJECT",
    "DOMAIN-KEYWORD,api.biliapi,REJECT",
    "DOMAIN-KEYWORD,app.biliapi,REJECT",
)
BILIBILI_SCRIPT_LINES = {
    "airborne": r'{{{空降助手}}} = type=http-request,pattern=^https:\/\/(?:grpc\.biliapi\.net|app\.bilibili\.com)\/bilibili\.community\.service\.dm\.v1\.DM\/DmSegMobile$,argument="{"logLevel":"{{{日志等级}}}"}",requires-body=1,binary-body-mode=1,max-size=-1,engine=webview,timeout=10,script-path=https://raw.githubusercontent.com/kokoryh/Sparkle/refs/heads/master/dist/bilibili.protobuf.request.js',
    "request": r'{{{优化评论区加载}}} = type=http-request,pattern=^https:\/\/(?:grpc\.biliapi\.net|app\.bilibili\.com)\/bilibili\.(?:app\.viewunite\.v1\.View\/View|main\.community\.reply\.v1\.Reply\/MainList)$,argument="{"purifyComment":{{{过滤置顶评论广告}}},"logLevel":"{{{日志等级}}}"}",requires-body=1,binary-body-mode=1,max-size=-1,engine=webview,timeout=10,script-path=https://raw.githubusercontent.com/kokoryh/Sparkle/refs/heads/master/dist/bilibili.protobuf.request.js',
    "skin": r'bilibili.skin = type=http-response,pattern=^https:\/\/app\.bilibili\.com\/x\/resource\/show\/skin\?,requires-body=1,max-size=-1,engine=webview,script-path=https://raw.githubusercontent.com/kokoryh/Script/master/js/bili-suit-diy.js',
    "json": r'bilibili.json = type=http-response,pattern=^https:\/\/app\.bilibili\.com\/x\/(?:resource\/show\/tab\/v2|v2\/(?:splash\/(?:list|show|event\/list2)|feed\/index(?:\/story)?|account\/(?:mine(?:\/ipad)?|myinfo)))\?,argument="{"showCreatorHub":{{{创作中心}}}}",requires-body=1,max-size=-1,engine=webview,script-path=https://raw.githubusercontent.com/kokoryh/Sparkle/refs/heads/master/dist/bilibili.json.js',
    "protobuf": r'bilibili.protobuf = type=http-response,pattern=^https:\/\/(?:grpc\.biliapi\.net|app\.bilibili\.com)\/bilibili\.(?:app\.(?:show\.v1\.Popular\/Index|dynamic\.v2\.Dynamic\/DynAll|view(?:unite)?\.v1\.View\/(?:View|ViewProgress|RelatesFeed)|playurl\.v1\.PlayURL\/PlayView|playerunite\.v1\.Player\/PlayViewUnite)|polymer\.app\.search\.v1\.Search\/SearchAll|community\.service\.dm\.v1\.DM\/DmView|main\.community\.reply\.v1\.Reply\/MainList|pgc\.gateway\.player\.v2\.PlayURL\/PlayView)$,argument="{"displayUpList":"{{{动态最常访问}}}","purifyComment":{{{过滤置顶评论广告}}},"sponsorBlock":"{{{空降助手}}}","logLevel":"{{{日志等级}}}"}",requires-body=1,binary-body-mode=1,max-size=-1,engine=webview,script-path=https://raw.githubusercontent.com/kokoryh/Sparkle/refs/heads/master/dist/bilibili.protobuf.response.js',
}
BILIBILI_EXTRA_RULE_LINES = [
    "DOMAIN,bsbsb.top,{{{空降助手策略}}},pre-matching",
    "DOMAIN,t-dsp.pinduoduo.com,REJECT,pre-matching",
    "DOMAIN,video-dsp.pddpic.com,REJECT,pre-matching",
    "DOMAIN,promotion.pddpic.com,REJECT,pre-matching",
    "DOMAIN,promotion-1.pddpic.com,REJECT,pre-matching",
    "DOMAIN,promotion-2.pddpic.com,REJECT,pre-matching",
    "DOMAIN,promotion-3.pddpic.com,REJECT,pre-matching",
    "DOMAIN-KEYWORD,pdd-ad,REJECT,pre-matching",
    "DOMAIN,ads.union.jd.com,REJECT,pre-matching",
    "DOMAIN,dsp-x.jd.com,REJECT,pre-matching",
    "DOMAIN,img-x.jd.com,REJECT,pre-matching",
    "DOMAIN,jzt.jd.com,REJECT,pre-matching",
    "DOMAIN,kepler.jd.com,REJECT,pre-matching",
    "DOMAIN,keplerapi.jd.com,REJECT,pre-matching",
    "DOMAIN-KEYWORD,jd-ad,REJECT,pre-matching",
    "DOMAIN-KEYWORD,jingdong-ad,REJECT,pre-matching",
    'AND,((DOMAIN-SUFFIX,pddpic.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching',
    'AND,((DOMAIN-SUFFIX,pddcdn.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching',
    'AND,((DOMAIN-SUFFIX,jdimg.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching',
    'AND,((DOMAIN-SUFFIX,360buyimg.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching',
    r'URL-REGEX,"^http:\/\/upos-sz-static\.bilivideo\.com\/ssaxcode\/\w{2}\/\w{2}\/\w{32}-1-SPLASH",REJECT-TINYGIF,extended-matching',
    r'URL-REGEX,"^http:\/\/[\d\.]+:8000\/v1\/resource\/\w{32}-1-SPLASH",REJECT-TINYGIF,extended-matching',
    r'URL-REGEX,"^https?:\/\/m\.360buyimg\.com\/(?:mobilecms|babel)\/.*",REJECT-IMG,extended-matching',
    "DOMAIN,cm.bilibili.com,REJECT,pre-matching",
    "DOMAIN,cm.bilibili.net,REJECT,pre-matching",
    "DOMAIN,ad.bilibili.com,REJECT,pre-matching",
    "DOMAIN,ad-game.bilibili.com,REJECT,pre-matching",
    "DOMAIN,impression.biligame.com,REJECT,pre-matching",
    "DOMAIN-SUFFIX,ad.bilibili.com,REJECT,pre-matching",
    "DOMAIN-KEYWORD,bili-ad,REJECT,pre-matching",
    "DOMAIN-KEYWORD,biliad,REJECT,pre-matching",
    "DOMAIN-KEYWORD,biligame-ad,REJECT,pre-matching",
    "AND,((DOMAIN-SUFFIX,chat.bilibili.com),(OR,((DOMAIN-KEYWORD,stun),(DOMAIN-KEYWORD,tracker)))),REJECT,pre-matching",
]
BILIBILI_EXTRA_MAP_LOCAL_LINES = [
    r'^https?:\/\/(?:app|api)\.bilibili\.com\/x\/v2\/splash\/ data-type=base64 data="eyJjb2RlIjowLCJtZXNzYWdlIjoiMCIsInR0bCI6MSwiZGF0YSI6eyJsaXN0IjpbXSwic2hvdyI6W10sImV2ZW50X2xpc3QiOltdLCJicmFuZF9saXN0IjpbXSwiYnJhbmRfc2hvdyI6W10sImJyYW5kX2V2ZW50X2xpc3QiOltdLCJtYXhfdGltZSI6MCwibWluX2ludGVydmFsIjozMTUzNjAwMH19" header="content-type: application/json; charset=utf-8|bili-status-code: 0"',
    r'^https?:\/\/(?:app|api)\.bilibili\.com\/x\/(?:resource\/(?:top\/activity|patch\/tab(?:\/v2)?)|v2\/search\/square|vip\/ads\/materials|v2\/ad\/index)\? data-type=base64 data="eyJjb2RlIjotNDA0LCJtZXNzYWdlIjoiLTQwNCIsInR0bCI6MSwiZGF0YSI6bnVsbH0=" header="content-type: application/json; charset=utf-8|bili-status-code: -404"',
    r'^https?:\/\/api\.bilibili\.com\/pgc\/activity\/deliver\/material\/receive\? data-type=base64 data="eyJjb2RlIjowLCJkYXRhIjp7ImNsb3NlVHlwZSI6ImNsb3NlX3dpbiIsImNvbnRhaW5lciI6W10sInNob3dUaW1lIjoiIn0sIm1lc3NhZ2UiOiJzdWNjZXNzIn0=" header="content-type: application/json|bili-status-code: 0"',
    r'^https?:\/\/api\.live\.bilibili\.com\/xlive\/e-commerce-interface\/v1\/ecommerce-user\/get_shopping_info\? data-type=base64 data="e30=" header="content-type: application/json"',
    r'^https?:\/\/line3-h5-mobile-api\.biligame\.com\/game\/live\/large_card_material\? data-type=base64 data="eyJjb2RlIjowLCJtZXNzYWdlIjoic3VjY2VzcyJ9" header="content-type: application/json"',
    r'^https?:\/\/grpc\.biliapi\.net\/bilibili\.app\.interface\.v\d+\.Teenagers\/ModeStatus$ data-type=base64 data="AAAAABMKEQgCEgl0ZWVuYWdlcnMgAioA" header="content-type: application/grpc|grpc-status: 0"',
    r'^https?:\/\/grpc\.biliapi\.net\/bilibili\.app\.interface\.v\d+\.Search\/DefaultWords$ data-type=base64 data="AAAAACEaHeaQnOe0ouinhumikeOAgeeVquWJp+aIlnVw5Li7KAE=" header="content-type: application/grpc|grpc-status: 0"',
    r'^https?:\/\/grpc\.biliapi\.net\/bilibili\.app\.(?:view\.v\d+\.View\/TFInfo|viewunite\.v\d+\.View\/(?:PlayPause|ViewEndPage))$ data-type=base64 data="AAAAAAA=" header="content-type: application/grpc|grpc-status: 0"',
]
BILIBILI_EXTRA_BODY_REWRITE_LINES = [
    r"""http-response-jq ^https://app.bilibili.com/x/v2/splash/(?:list|show|event/list2|brand/(?:list|show|event/list2))\? '.data |= (if type == "object" then . + {"list":[],"show":[],"event_list":[],"brand_list":[],"brand_show":[],"brand_event_list":[],"max_time":0,"min_interval":31536000} else . end)'""",
    r"""http-response-jq ^https://app.bilibili.com/x/resource/show/skin\? 'del(.data.common_equip)'""",
    r"""http-response-jq ^https://app.bilibili.com/x/resource/show/tab/v2\? '.data.tab=[{"pos":1,"id":731,"name":"直播","tab_id":"直播tab","uri":"bilibili://live/home"},{"pos":2,"id":477,"name":"推荐","tab_id":"推荐tab","uri":"bilibili://pegasus/promo","default_selected":1},{"pos":3,"id":478,"name":"热门","tab_id":"热门tab","uri":"bilibili://pegasus/hottopic"},{"pos":4,"id":3502,"name":"动画","tab_id":"bangumi","uri":"bilibili://pgc/bangumi_v2"},{"pos":5,"id":3503,"name":"影视","tab_id":"film","uri":"bilibili://pgc/cinema_v2"}] | .data.top=[{"pos":1,"id":176,"name":"消息","tab_id":"消息Top","uri":"bilibili://link/im_home","icon":"http://i0.hdslb.com/bfs/archive/d43047538e72c9ed8fd8e4e34415fbe3a4f632cb.png"}] | .data.bottom=[{"pos":1,"id":177,"name":"首页","tab_id":"home","uri":"bilibili://main/home/","icon":"http://i0.hdslb.com/bfs/archive/63d7ee88d471786c1af45af86e8cb7f607edf91b.png","icon_selected":"http://i0.hdslb.com/bfs/archive/e5106aa688dc729e7f0eafcbb80317feb54a43bd.png"},{"pos":2,"id":179,"name":"动态","tab_id":"dynamic","uri":"bilibili://following/home/","icon":"http://i0.hdslb.com/bfs/archive/86dfbe5fa32f11a8588b9ae0fccb77d3c27cedf6.png","icon_selected":"http://i0.hdslb.com/bfs/archive/25b658e1f6b6da57eecba328556101dbdcb4b53f.png"},{"pos":5,"id":181,"name":"我的","tab_id":"我的Bottom","uri":"bilibili://user_center/","icon":"http://i0.hdslb.com/bfs/archive/4b0b2c49ffeb4f0c2e6a4cceebeef0aab1c53fe1.png","icon_selected":"http://i0.hdslb.com/bfs/archive/a54a8009116cb896e64ef14dcf50e5cade401e00.png"}]'""",
    r"""http-response-jq ^https://api.bilibili.com/x/pd-proxy/tracker\? '.data[][]?="stun.chat.bilibili.com:3478"'""",
    r"""http-response-jq ^https://api.bilibili.com/pgc/page/channel\? '.data.modules |= map(select(.type != "TIP") | if .type == "BANNER" then .module_data.items |= map(select(.url | startswith("https://www.bilibili.com/blackboard/era/") | not)) else . end)'""",
    r"""http-response-jq ^https://api.bilibili.com/pgc/page/(?:bangumi|cinema/tab)\? '.result.modules |= if . then map(if (.style | startswith("tip")) or (.module_id | IN(241, 1283, 1441, 1284)) then .items = [] elif .style | startswith("banner") then .items |= if . then map(select(.link | contains("play"))) else [] end elif .style | startswith("function") then .items |= if . then map(select(.blink | startswith("bilibili"))) else [] end end) end'""",
    r"""http-response-jq ^https://api.live.bilibili.com/xlive/(?:app-interface/v2/index/feed|app-room/v1/index/getInfoBy(?:Room|User))\? '.data |= (del(.play_together_info, .play_together_info_v2, .activity_banner_info) | if .function_card then .function_card[] = null end | if .new_tab_info.outer_list then .new_tab_info.outer_list |= map(select(.biz_id != 33)) end | if .card_list then .card_list |= map(select(.card_type | IN("banner_v2", "activity_card_v1") | not)) end | reduce ([["show_reserve_status"], false], [["reserve_info", "show_reserve_status"], false], [["shopping_info", "is_show"], 0]) as [$path, $value] (.; if getpath($path) then setpath($path; $value) end))'""",
    r"""http-response-jq ^https://(?:app|api).bilibili.com/x/v2/view(?:/unite)?\? '.data |= (del(.cm,.cms,.ad_info,.ad_dislike,.special_cell,.activity_url,.banner,.banners,.cm_config,.relate_cm,.ad_reply,.ad_resource,.ad_tag,.ad_args,.commercial_info,.commerce,.ecommerce,.shopping_info,.shopping_card,.goods_info,.goods_card,.recommend_ad,.operation_card,.activity_banner_info,.middle_ad,.bottom_ad,.pop_ad) | if .relates then .relates |= map(select(((.card_goto? // "") | test("ad|cm|banner|mall|shop|goods") | not) and ((.goto? // "") | test("ad|cm|banner|mall|shop|goods") | not) and (.ad_cb? == null) and (.cm_mark? == null) and (((.uri? // "") | test("cm\.bilibili|ad\.bilibili|mall\.bilibili|bilicm|ad_|shopping|ecommerce|taobao|tmall|pinduoduo|pdd")) | not))) else . end | if .cms then .cms = [] else . end)'""",
    r"""http-response-jq ^https://app.bilibili.com/x/v2/feed/index/story\? 'if .data.items then .data.items |= map(select((.ad_info == null) and (.card_goto | IN("vertical_ad_av", "vertical_ad_live", "vertical_ad_picture") | not)) | del(.story_cart_icon, .free_flow_toast, .image_infos, .course_info, .game_info)) end'""",
    r"""http-response-jq ^https://app.bilibili.com/x/v2/feed/index\? 'if .data.items then .data.items |= map(select((.banner_item == null) and (.ad_info == null) and (.card_goto == "av") and (.card_type | IN("small_cover_v2", "large_cover_single_v9", "large_cover_v1")))) end'""",
    r"""http-response-jq ^https://(?:app|api).bilibili.com/x/v2/feed/index(?:/story)?\? '.data.items |= if . then map(select(((.card_goto? // "") | test("ad|cm|banner|mall|shop|goods|vertical_ad") | not) and ((.goto? // "") | test("ad|cm|banner|mall|shop|goods") | not) and (.banner_item? == null) and (.ad_info? == null) and (.ad_cb? == null) and (.cm_mark? == null))) else [] end'""",
    r"""http-response-jq ^https://(?:app|api).bilibili.com/x/v2/feed/index(?:/story)?\? 'if .data.items then .data.items |= map(select((tostring | test("pinduoduo|yangkeduo|pddpic|pddcdn|t-dsp"; "i") | not))) else . end'""",
    r"""http-response-jq ^https://(?:app|api).bilibili.com/x/v2/view(?:/unite)?\? 'if .data.relates then .data.relates |= map(select((tostring | test("pinduoduo|yangkeduo|pddpic|pddcdn|t-dsp"; "i") | not))) else . end'""",
    r"""http-response-jq ^https://api.bilibili.com/x/v2/reply/(?:main|reply)\? 'del(.data.cm,.data.cms,.data.ad,.data.ads,.data.upper.ad) | if .data.replies then .data.replies |= map(select((tostring | test("pinduoduo|yangkeduo|pddpic|pddcdn|t-dsp"; "i") | not))) else . end'""",
    r"""http-response-jq ^https://(?:app|api).bilibili.com/x/v2/feed/index(?:/story)?\? 'if .data.items then .data.items |= map(select((tostring | test("jd|jingdong|360buyimg|jdimg|jdpay|union\\.jd|m\\.jd\\.com|kepler"; "i") | not))) else . end'""",
    r"""http-response-jq ^https://(?:app|api).bilibili.com/x/v2/view(?:/unite)?\? 'if .data.relates then .data.relates |= map(select((tostring | test("jd|jingdong|360buyimg|jdimg|jdpay|union\\.jd|m\\.jd\\.com|kepler"; "i") | not))) else . end'""",
    r"""http-response-jq ^https://api.bilibili.com/x/v2/reply/(?:main|reply)\? 'del(.data.cm,.data.cms,.data.ad,.data.ads,.data.upper.ad) | if .data.replies then .data.replies |= map(select((tostring | test("jd|jingdong|360buyimg|jdimg|jdpay|union\\.jd|m\\.jd\\.com|kepler"; "i") | not))) else . end'""",
]
BILIBILI_COMIC_EXTRA_BODY_REWRITE_LINES = [
    r"""http-response-jq ^https?:\/\/manga\.bilibili\.com\/twirp\/comic\.v\d\.Comic\/GetClassPageAllTabs 'if .data then (.data.home_type? |= map(select(.name | in({"新人":1, "新作":1}) | not))) | (.data.home_feed? |= map(select(.name == "商城" | not))) else . end'""",
    r"""http-response-jq ^https?:\/\/manga\.bilibili\.com\/twirp\/user\.v\d\.User\/UCenterConf 'if .data.confs then .data.confs |= map(select(.title | in({"漫画商城":1, "超漫俱乐部":1, "看漫免流量":1}) | not)) else . end'""",
]


class SyncError(RuntimeError):
    """Fatal sync configuration error."""


def repo_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"trusted_repositories": TRUSTED_REPOSITORIES, "modules": []}
    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        raise SyncError(f"invalid json: {rel(path)}: {exc}") from exc
    if not isinstance(data, dict):
        raise SyncError(f"invalid json root: {rel(path)} must be an object")
    data.setdefault("trusted_repositories", TRUSTED_REPOSITORIES)
    data.setdefault("modules", [])
    if not isinstance(data["modules"], list):
        raise SyncError(f"invalid modules list: {rel(path)}")
    return data


def clean_app_name(raw: str, slug: str) -> str:
    name = raw.strip()
    if name.startswith("GrandpaNiu "):
        name = name[len("GrandpaNiu ") :]
    if name.endswith(" Source"):
        name = name[: -len(" Source")]
    if not name:
        name = title_from_slug(slug)
    return name.strip()


def title_from_slug(slug: str) -> str:
    special = {"jd": "JD", "wps": "WPS", "qqmusic": "QQ Music", "qqnews": "QQ News"}
    if slug in special:
        return special[slug]
    return " ".join(part.upper() if part in {"jd", "qq", "wps"} else part.capitalize() for part in slug.split("-"))


def name_from_source(path: Path, slug: str) -> str:
    for line in read_text(path).splitlines():
        match = META_RE.match(line)
        if match and match.group(1).lower() == "name":
            return clean_app_name(match.group(2), slug)
    return title_from_slug(slug)


def github_project_from_url(url: str) -> str:
    match = re.search(r"raw\.githubusercontent\.com/([^/]+/[^/]+)/", url, re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.search(r"github\.com/([^/]+/[^/]+)", url, re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.search(r"https?://([^/]+)/", url, re.IGNORECASE)
    return match.group(1) if match else ""


def raw_module_url(url: str) -> bool:
    return bool(url and RAW_MODULE_HINT_RE.search(url))


def slug_from_lpx(filename: str) -> str:
    stem = filename
    if stem.lower().endswith(".lpx"):
        stem = stem[:-4]
    stem = re.sub(r"_?remove_ads$", "", stem, flags=re.IGNORECASE)
    stem = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", stem)
    stem = stem.replace("_", "-").replace(" ", "-")
    stem = re.sub(r"[^A-Za-z0-9-]+", "-", stem)
    stem = re.sub(r"-+", "-", stem).strip("-").lower()
    return stem or "kelee-app"


def display_name_from_plugin(name: str, slug: str) -> str:
    clean = name.replace(AD_TAG, "").strip()
    return clean or title_from_slug(slug)


def risk_from_kelee(name: str, filename: str, slug: str) -> str:
    haystack = f"{name} {filename} {slug}".lower()
    if slug in HIGH_RISK_IDS:
        return "high"
    if any(token.lower() in haystack for token in HIGH_RISK_NAME_TOKENS):
        return "high"
    return "medium"


def fetch_kelee_catalog() -> list[dict[str, str]]:
    request = urllib.request.Request(
        KELEE_CATALOG_URL,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json,text/plain,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(request, timeout=35) as response:
        data = json.loads(response.read().decode("utf-8-sig", errors="replace"))
    items: list[dict[str, str]] = []
    for item in data.get("lists", []):
        name = str(item.get("name") or "").strip()
        tags = [str(tag) for tag in item.get("tag", [])]
        if AD_TAG not in name and not any(AD_TAG in tag for tag in tags):
            continue
        url = str(item.get("url") or "").strip()
        if "plugin=" in url:
            url = urllib.parse.unquote(url.split("plugin=", 1)[1])
        filename = Path(urllib.parse.urlparse(url).path).name
        if not filename.endswith(".lpx") or filename in KELEE_EXCLUDED_BASES:
            continue
        slug = KELEE_ID_OVERRIDES.get(filename, slug_from_lpx(filename))
        items.append(
            {
                "id": slug,
                "name": display_name_from_plugin(name, slug),
                "source_url": url,
                "filename": filename,
                "risk": risk_from_kelee(name, filename, slug),
            }
        )
    return items


def merge_kelee_catalog(records: list[dict[str, Any]], include_kelee: bool) -> list[dict[str, Any]]:
    if not include_kelee:
        return records
    by_id = {str(record["id"]): record for record in records}
    try:
        items = fetch_kelee_catalog()
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        print(f"WARNING: Kelee catalog fetch failed: {exc}", file=sys.stderr)
        return records

    for item in items:
        module_id = item["id"]
        if module_id in KELEE_PINNED_REMOTE_SCRIPT_IDS:
            continue
        existing = by_id.get(module_id)
        if existing is None:
            risk = item["risk"]
            by_id[module_id] = {
                "id": module_id,
                "name": item["name"],
                "source_url": item["source_url"],
                "target": f"Rewrite/Sources/Apps/{module_id}.conf",
                "enabled": True,
                "direct_commit": True,
                "risk": risk,
                "backup": risk == "high" or module_id in CORE_BACKUP_IDS,
                "upstream_project": KELEE_UPSTREAM_PROJECT,
                "last_sync_mode": "configured",
            }
            continue

        mode = str(existing.get("last_sync_mode") or "")
        source_url = str(existing.get("source_url") or "")
        should_fill = (
            not source_url
            or mode in {"missing-upstream-source", "remote-script-only", "clue-only", "discovered-disabled"}
        )
        if should_fill:
            existing["name"] = existing.get("name") or item["name"]
            existing["source_url"] = item["source_url"]
            existing["enabled"] = True
            existing["direct_commit"] = True
            existing["risk"] = "high" if existing.get("risk") == "high" or item["risk"] == "high" else item["risk"]
            existing["backup"] = bool(existing.get("backup") or existing["risk"] == "high" or module_id in CORE_BACKUP_IDS)
            existing["upstream_project"] = KELEE_UPSTREAM_PROJECT
            existing["last_sync_mode"] = "configured"

    return sorted(by_id.values(), key=lambda record: str(record["id"]))


def clue_urls(text: str) -> list[str]:
    urls: list[str] = []
    seen: set[str] = set()
    for line in text.splitlines():
        for pattern in (SCRIPT_PATH_RE, RULE_SET_RE):
            for match in pattern.finditer(line):
                url = match.group(1)
                clean = url.rstrip(").]")
                if clean not in seen:
                    seen.add(clean)
                    urls.append(clean)
    return urls


def extract_source_clues(path: Path) -> dict[str, str]:
    text = read_text(path)
    explicit_url = ""
    converted_from = ""
    upstream_project = ""
    for line in text.splitlines():
        field = COMMENT_FIELD_RE.match(line)
        if not field:
            continue
        key = field.group(1).lower().replace("_", "-")
        value = field.group(2).strip()
        if key in {"source-url", "source", "upstream-url"}:
            urls = URL_RE.findall(value)
            if urls:
                explicit_url = urls[0]
        elif key == "converted-from":
            converted_from = value
            project = value.split()[0].strip()
            if "/" in project:
                upstream_project = project
        elif key in {"upstream-base", "upstream-name"} and not upstream_project:
            upstream_project = value
    if explicit_url and not upstream_project:
        upstream_project = github_project_from_url(explicit_url)
    if not upstream_project:
        for url in clue_urls(text):
            project = github_project_from_url(url)
            if project:
                upstream_project = project
                break
    return {
        "source_url": explicit_url,
        "converted_from": converted_from,
        "upstream_project": upstream_project,
    }


def inferred_risk(slug: str, path: Path, existing: dict[str, Any] | None) -> str:
    if existing and existing.get("risk"):
        return str(existing["risk"])
    if slug in HIGH_RISK_IDS:
        return "high"
    for line in read_text(path).splitlines():
        field = COMMENT_FIELD_RE.match(line)
        if field and field.group(1).lower() == "risk":
            return field.group(2).strip().lower() or "medium"
    return "medium"


def complete_record(slug: str, path: Path, existing: dict[str, Any] | None = None) -> dict[str, Any]:
    existing = dict(existing or {})
    clues = extract_source_clues(path)
    source_url = str(existing.get("source_url") or clues["source_url"] or "").strip()
    source_is_module = raw_module_url(source_url)
    source_name = name_from_source(path, slug)
    existing_name = clean_app_name(str(existing.get("name") or ""), slug) if existing.get("name") else ""
    fallback_name = title_from_slug(slug)
    if not existing_name or (existing_name == fallback_name and source_name != fallback_name):
        name = source_name
    else:
        name = existing_name
    risk = inferred_risk(slug, path, existing)
    backup = bool(existing.get("backup", slug in CORE_BACKUP_IDS or risk == "high"))
    enabled = bool(existing.get("enabled", bool(source_url and source_is_module and existing)))
    direct_commit = bool(existing.get("direct_commit", enabled and bool(source_url)))
    existing_project = str(existing.get("upstream_project") or "").strip()
    if not source_url and existing_project.startswith(("api.", "app.", "manga.", "m.", "www.")):
        existing_project = ""
    upstream_project = existing_project or clues["upstream_project"] or github_project_from_url(source_url)
    mode = str(existing.get("last_sync_mode") or ("configured" if enabled else "discovered-disabled"))
    if source_url and not source_is_module and not existing.get("enabled"):
        mode = "clue-only"
        enabled = False
        direct_commit = False
    record = {
        "id": slug,
        "name": name,
        "source_url": source_url,
        "target": rel(path),
        "enabled": enabled,
        "direct_commit": direct_commit,
        "risk": risk,
        "backup": backup,
        "upstream_project": upstream_project,
        "last_sync_mode": mode,
    }
    for key in REQUIRED_RECORD_KEYS:
        record.setdefault(key, "")
    return record


def discover_modules(config: dict[str, Any], apps_dir: Path) -> list[dict[str, Any]]:
    existing_by_id = {
        str(item.get("id")): item
        for item in config.get("modules", [])
        if isinstance(item, dict) and item.get("id")
    }
    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    for path in sorted(apps_dir.glob("*.conf")):
        slug = path.stem
        if slug.startswith("_"):
            continue
        records.append(complete_record(slug, path, existing_by_id.get(slug)))
        seen.add(slug)
    for slug, item in sorted(existing_by_id.items()):
        if slug in seen:
            continue
        target = repo_path(item.get("target") or f"Rewrite/Sources/Apps/{slug}.conf")
        records.append(complete_record(slug, target, item))
    records.sort(key=lambda item: item["id"])
    return records


def fetch_text(url: str) -> str:
    user_agent = KELEE_USER_AGENT if "kelee.one/" in url else "GrandpaNiu-Upstream-App-Sync/1.0"
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": user_agent,
            "Accept": "text/plain,*/*;q=0.8",
            "Referer": "https://hub.kelee.one/",
        },
    )
    with urllib.request.urlopen(request, timeout=35) as response:
        data = response.read()
    return data.decode("utf-8-sig", errors="replace")


def suspicious_reason(text: str) -> str:
    for pattern in SUSPICIOUS_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(0).strip()
    return ""


def allow_known_spotify_upstream(module_id: str, source_url: str, reason: str) -> bool:
    """Allow the pinned app2smile Spotify source despite upstream wording."""
    return module_id == "spotify" and source_url == SPOTIFY_STABLE_UPSTREAM_URL and bool(reason)


def split_module(text: str) -> tuple[list[str], dict[str, list[str]]]:
    meta: list[str] = []
    sections: dict[str, list[str]] = {name: [] for name in SOURCE_SECTIONS}
    current: str | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        match = SECTION_RE.match(line)
        if match:
            raw_name = match.group(1).strip()
            name = SECTION_ALIASES.get(raw_name.lower(), raw_name)
            current = name if name in sections else None
            continue
        if current is None:
            meta.append(line)
        else:
            sections[current].append(line)
    return meta, sections


def normalize_pattern(value: str) -> str:
    return value.strip().replace("\\/", "/")


def comparable_line(value: str) -> str:
    return normalize_pattern(value).replace("\\.", ".").lower()


def is_example_line(value: str) -> bool:
    comparable = comparable_line(value)
    return any(token in comparable for token in EXAMPLE_TOKENS)


def jq_path(path: str) -> str:
    path = path.strip().strip(",")
    if not path:
        return "."
    if path.startswith("."):
        return path
    return "." + path


def convert_json_del(args: str) -> str:
    paths = [jq_path(item) for item in args.split() if item.strip()]
    if not paths:
        return "del(.)"
    return "del(" + ",".join(paths) + ")"


def convert_json_replace(args: str) -> str:
    parts = args.split(None, 1)
    if len(parts) != 2:
        return ""
    path, value = parts
    return f"{jq_path(path)} = {value.strip()}"


def split_pattern_action(line: str) -> tuple[str, str]:
    normalized = normalize_pattern(line)
    parts = normalized.split(None, 1)
    if len(parts) == 1:
        return parts[0], ""
    return parts[0], parts[1].strip()


def convert_loon_rewrite_line(line: str) -> tuple[str, str]:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return "", ""
    if stripped.startswith(("http-request ", "http-response ")) and "script-path=" not in stripped:
        parts = stripped.split(None, 1)
        stripped = parts[1] if len(parts) == 2 else stripped
    pattern, action = split_pattern_action(stripped)
    if not action:
        return "URL Rewrite", f"# unsupported-loon-rewrite: {normalize_pattern(stripped)}"

    simple = action.split()[0]
    if simple == "url":
        action = action[len("url") :].strip()
        if not action:
            return "", ""
        simple = action.split()[0]
    if simple == "header":
        replacement = action[len("header") :].strip()
        if replacement:
            return "URL Rewrite", f"{pattern} {replacement} header"
    if simple in {"header-replace", "header-replace-regex", "header-del"}:
        return "Header Rewrite", f"http-request {pattern} {action}"
    if simple in QX_REJECT_ACTIONS:
        return "URL Rewrite", f"{pattern} - {simple}"
    if simple in {"mock-response-body", "mock-response-body-replace"}:
        body = action[len(simple) :].strip()
        status = "200"
        header = ""
        if "data-type=json" in body and "header=" not in body:
            header = ' header="content-type: application/json"'
        return "Map Local", f"{pattern} {body} status-code={status}{header}".strip()
    if simple == "response-body-json-jq":
        jq = action[len("response-body-json-jq") :].strip()
        return "Body Rewrite", f"http-response-jq {pattern} {jq}"
    if simple == "response-body-json-del":
        jq = convert_json_del(action[len("response-body-json-del") :].strip())
        return "Body Rewrite", f"http-response-jq {pattern} '{jq}'"
    if simple == "response-body-json-replace":
        jq = convert_json_replace(action[len("response-body-json-replace") :].strip())
        if jq:
            return "Body Rewrite", f"http-response-jq {pattern} '{jq}'"
    return "URL Rewrite", f"# unsupported-loon-rewrite: {normalize_pattern(stripped)}"


def convert_qx_script_line(pattern: str, action: str, module_id: str, index: int) -> str:
    parts = action.split()
    if not parts:
        return ""
    script_type, requires_body = QX_SCRIPT_ACTIONS.get(parts[0], ("", False))
    if not script_type:
        return ""
    script_path = ""
    if len(parts) > 1 and parts[1].startswith("http"):
        script_path = parts[1]
    if not script_path:
        match = URL_RE.search(action)
        script_path = match.group(0) if match else ""
    if not script_path:
        return ""
    suffix = "response" if script_type == "http-response" else "request"
    name = safe_script_name("", f"{module_id}.{suffix}.{index}")
    fields = [f"{name} = type={script_type}", f"pattern={normalize_pattern(pattern)}"]
    if requires_body:
        fields.extend(["requires-body=1", "max-size=0"])
    fields.append(f"script-path={script_path}")
    return ",".join(fields)


def convert_rewrite_line(line: str, module_id: str, index: int) -> tuple[str, str]:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return "", ""
    if is_example_line(stripped):
        return "", ""
    pattern, action = split_pattern_action(stripped)
    if action.startswith("url "):
        action = action[len("url") :].strip()
    action_name = action.split()[0] if action else ""
    if action_name in QX_SCRIPT_ACTIONS:
        converted = convert_qx_script_line(pattern, action, module_id, index)
        return ("Script", converted) if converted else ("", "")
    section, converted = convert_loon_rewrite_line(stripped)
    if converted.startswith("# unsupported-loon-rewrite:"):
        return "", ""
    return section, converted


def convert_qx_rule_line(line: str) -> str:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return stripped
    if is_example_line(stripped):
        return ""
    parts = [part.strip() for part in stripped.split(",")]
    if len(parts) < 3:
        return ""
    rule_type = QX_RULE_TYPES.get(parts[0].lower())
    if not rule_type:
        return ""
    value = parts[1]
    policy_raw = parts[2]
    policy_low = policy_raw.lower()
    if policy_low.startswith("reject"):
        policy = "REJECT"
    elif policy_low == "direct":
        policy = "DIRECT"
    else:
        policy = policy_raw.upper()
    return f"{rule_type},{value},{policy}"


def convert_loose_qx_lines(lines: list[str], module_id: str) -> dict[str, list[str]]:
    converted_sections: dict[str, list[str]] = {name: [] for name in ALLOWED_SECTIONS}
    mitm_lines: list[str] = []
    for index, raw in enumerate(lines, 1):
        stripped = raw.strip()
        if not stripped or stripped.startswith("#!") or stripped.startswith("#"):
            continue
        if stripped.lower().startswith("hostname"):
            mitm_lines.append(stripped)
            continue
        rule = convert_qx_rule_line(stripped)
        if rule:
            converted_sections["Rule"].append(rule)
            continue
        target_section, converted = convert_rewrite_line(stripped, module_id, index)
        if target_section and converted:
            converted_sections[target_section].append(converted)
    converted_sections["MITM"].extend(convert_mitm_lines(mitm_lines))
    return converted_sections


def option_value(options: str, key: str) -> str:
    match = re.search(rf"(?:^|,\s*){re.escape(key)}\s*=\s*([^,]+)", options)
    return match.group(1).strip().strip('"') if match else ""


def truthy(value: str) -> bool:
    return value.lower() in {"1", "true", "yes"}


def safe_script_name(raw: str, fallback: str) -> str:
    name = raw.strip() or fallback
    name = re.sub(r"\s+", "-", name)
    name = re.sub(r"[^A-Za-z0-9_.-]+", "-", name)
    name = re.sub(r"-+", "-", name).strip("-")
    if not re.search(r"[A-Za-z0-9]", name):
        name = fallback
    return name[:80] or fallback


def convert_loon_script_line(line: str, module_id: str, index: int) -> str:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return stripped
    match = re.match(r"^(http-request|http-response)\s+(\S+)\s+(.+)$", stripped)
    if not match:
        return stripped
    script_type, pattern, options = match.groups()
    script_path = option_value(options, "script-path")
    if not script_path:
        return f"# unsupported-loon-script: {normalize_pattern(stripped)}"
    tag = option_value(options, "tag")
    name = safe_script_name(tag, f"{module_id}.{script_type.split('-')[-1]}.{index}")
    parts = [f"{name} = type={script_type}", f"pattern={normalize_pattern(pattern)}"]
    if truthy(option_value(options, "requires-body")):
        parts.append("requires-body=1")
    if truthy(option_value(options, "binary-body-mode")):
        parts.append("binary-body-mode=1")
    max_size = option_value(options, "max-size")
    if max_size:
        parts.append(f"max-size={max_size}")
    parts.append(f"script-path={script_path}")
    timeout = option_value(options, "timeout")
    if timeout:
        parts.append(f"timeout={timeout}")
    return ",".join(parts)


def is_protected_reject_line(line: str) -> bool:
    lowered = line.lower()
    if "reject" not in lowered:
        return False
    return any(token in lowered for token in PROTECTED_REJECT_TOKENS)


def convert_mitm_lines(lines: list[str]) -> list[str]:
    hosts: list[str] = []
    seen: set[str] = set()
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            _, value = line.split("=", 1)
        else:
            value = line
        value = value.replace("%APPEND%", "")
        for host in value.split(","):
            clean = host.strip()
            if is_example_line(clean):
                continue
            if any(token in clean.lower() for token in PROTECTED_MITM_HOST_TOKENS):
                continue
            if clean and clean not in seen:
                seen.add(clean)
                hosts.append(clean)
    return ["hostname = %APPEND% " + ",".join(hosts)] if hosts else []


def convert_rule_lines(lines: list[str]) -> list[str]:
    out: list[str] = []
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            out.append(raw.rstrip())
            continue
        if is_protected_reject_line(line):
            out.append(f"# skipped protected core reject: {line}")
            continue
        parts = [part.strip() for part in line.split(",")]
        out.append(",".join(parts))
    return out


def upstream_name(meta: list[str], fallback: str) -> str:
    for line in meta:
        match = META_RE.match(line)
        if match and match.group(1).lower() == "name":
            return match.group(2).strip() or fallback
    return fallback


def preserved_arguments(meta: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for line in meta:
        match = META_RE.match(line)
        if not match:
            continue
        key = match.group(1)
        low = key.lower()
        if low in DROP_META_KEYS:
            continue
        if low in {"arguments", "arguments-desc"}:
            clean = f"#!{key}={match.group(2).strip()}"
            if clean not in seen:
                seen.add(clean)
                out.append(clean)
    return out


def clean_section_lines(lines: list[str]) -> list[str]:
    out: list[str] = []
    seen_active: set[str] = set()
    last_blank = False
    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            if out and not last_blank:
                out.append("")
            last_blank = True
            continue
        if is_protected_reject_line(stripped):
            continue
        if not stripped.startswith("#"):
            if stripped in seen_active:
                continue
            seen_active.add(stripped)
        out.append(line)
        last_blank = False
    while out and not out[-1].strip():
        out.pop()
    return out


def converted_source(record: dict[str, Any], upstream_text: str) -> tuple[str, str]:
    meta, sections = split_module(upstream_text)
    converted_sections: dict[str, list[str]] = {name: [] for name in ALLOWED_SECTIONS}
    module_id = str(record["id"])
    for section, lines in sections.items():
        if section == "Rewrite":
            for index, line in enumerate(lines, 1):
                target_section, converted = convert_rewrite_line(line, module_id, index)
                if target_section and converted:
                    converted_sections[target_section].append(converted)
        elif section == "Rule":
            qx_rules = [convert_qx_rule_line(line) for line in lines]
            if any(qx_rules):
                converted_sections[section].extend(rule for rule in qx_rules if rule)
            else:
                converted_sections[section].extend(convert_rule_lines(lines))
        elif section == "MITM":
            converted_sections[section].extend(convert_mitm_lines(lines))
        elif section == "Script":
            for index, line in enumerate(lines, 1):
                converted_sections[section].append(convert_loon_script_line(line, module_id, index))
        elif section in converted_sections:
            converted_sections[section].extend(lines)

    if not any(lines for lines in converted_sections.values()):
        loose_sections = convert_loose_qx_lines(meta, module_id)
        for section, lines in loose_sections.items():
            converted_sections[section].extend(lines)

    body_sections = {name: clean_section_lines(lines) for name, lines in converted_sections.items()}
    body_sections = {
        name: lines
        for name, lines in body_sections.items()
        if any(line.strip() and not line.strip().startswith("#") for line in lines)
    }
    if not body_sections:
        raise ValueError("no supported module sections found")

    app_name = clean_app_name(str(record["name"]), str(record["id"]))
    source_url = str(record["source_url"])
    upstream = upstream_name(meta, app_name)
    lines = [
        f"#!name=GrandpaNiu {app_name} Source",
        "#!desc=Auto-synced app-scoped source fragment",
        "# auto-sync: true",
        f"# source-url: {source_url}",
        f"# upstream-name: {upstream}",
        f"# risk: {record['risk']}",
    ]
    lines.extend(preserved_arguments(meta))
    for section in ALLOWED_SECTIONS:
        section_lines = body_sections.get(section)
        if not section_lines:
            continue
        lines.append("")
        lines.append(f"[{section}]")
        lines.extend(section_lines)
    return "\n".join(lines).rstrip() + "\n", upstream


def postprocess_bilibili_source(text: str) -> str:
    """Keep the latest Sparkle Bilibili cleanup active without risky account rewrites."""
    lines: list[str] = []
    inserted_arguments = False
    for raw in text.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if stripped.startswith("# source-url:"):
            line = f"# source-url: {BILIBILI_SPARKLE_SOURCE_URL}"
            stripped = line.strip()
        elif stripped.startswith("# upstream-name:"):
            line = "# upstream-name: Bilibili enhanced (kokoryh/Sparkle)"
            stripped = line.strip()
        elif stripped.startswith("#!arguments"):
            continue
        elif any(stripped.startswith(prefix) for prefix in BILIBILI_UNSAFE_RULE_PREFIXES):
            continue
        elif (
            ("pgc\\/view\\/v2\\/app\\/season" in stripped or "pgc/view/v2/app/season" in stripped)
            and ("payment" in stripped or ("pay" in stripped and "ment" in stripped))
        ):
            continue
        elif " data-type=text data=\"{" in stripped:
            continue
        elif "grpc\\.biliapi\\.net" in stripped and " data-type=base64 " in stripped:
            continue
        elif "bilibili.protobuf.request.js" in stripped and r"DM\/DmSegMobile" in stripped:
            line = BILIBILI_SCRIPT_LINES["airborne"]
            stripped = line.strip()
        elif "bilibili.protobuf.request.js" in stripped and r"Reply\/MainList" in stripped:
            line = BILIBILI_SCRIPT_LINES["request"]
            stripped = line.strip()
        elif stripped.startswith("bilibili.skin ="):
            line = BILIBILI_SCRIPT_LINES["skin"]
            stripped = line.strip()
        elif stripped.startswith("bilibili.json ="):
            line = BILIBILI_SCRIPT_LINES["json"]
            stripped = line.strip()
        elif stripped.startswith("bilibili.protobuf ="):
            line = BILIBILI_SCRIPT_LINES["protobuf"]
            stripped = line.strip()
        elif "bilibili.protobuf.js" in stripped:
            line = line.replace("bilibili.protobuf.js", "bilibili.protobuf.response.js")
            stripped = line.strip()

        lines.append(line)
        if stripped.startswith("# risk:") and not inserted_arguments:
            lines.extend(BILIBILI_ARGUMENT_LINES)
            inserted_arguments = True
    return apply_bilibili_overlay("\n".join(lines).rstrip() + "\n")


def bilibili_line_key(line: str) -> str:
    key = line.strip().replace("\\/", "/").replace("\\.", ".")
    key = re.sub(r"\s+", " ", key)
    return key


def merge_bilibili_section(additions: list[str], existing: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for raw in [*additions, *existing]:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        key = bilibili_line_key(stripped)
        if key in seen:
            continue
        seen.add(key)
        out.append(line)
    return out


def apply_bilibili_overlay(text: str) -> str:
    meta, sections = split_module(text)
    sections["Rule"] = merge_bilibili_section(BILIBILI_EXTRA_RULE_LINES, sections.get("Rule", []))
    sections["Map Local"] = merge_bilibili_section(BILIBILI_EXTRA_MAP_LOCAL_LINES, sections.get("Map Local", []))
    sections["Body Rewrite"] = merge_bilibili_section(
        BILIBILI_EXTRA_BODY_REWRITE_LINES,
        sections.get("Body Rewrite", []),
    )
    lines = [line.rstrip() for line in meta if line.strip()]
    for section in ALLOWED_SECTIONS:
        section_lines = clean_section_lines(sections.get(section, []))
        if not section_lines:
            continue
        lines.append("")
        lines.append(f"[{section}]")
        lines.extend(section_lines)
    return "\n".join(lines).rstrip() + "\n"


def apply_bilibili_comic_overlay(text: str) -> str:
    meta, sections = split_module(text)
    sections["Body Rewrite"] = merge_bilibili_section(
        BILIBILI_COMIC_EXTRA_BODY_REWRITE_LINES,
        sections.get("Body Rewrite", []),
    )
    lines = [line.rstrip() for line in meta if line.strip()]
    for section in ALLOWED_SECTIONS:
        section_lines = clean_section_lines(sections.get(section, []))
        if not section_lines:
            continue
        lines.append("")
        lines.append(f"[{section}]")
        lines.extend(section_lines)
    return "\n".join(lines).rstrip() + "\n"


def postprocess_converted_source(record: dict[str, Any], text: str) -> str:
    if str(record.get("id")) == "bilibili":
        return postprocess_bilibili_source(text)
    if str(record.get("id")) == "bilibili-comic":
        return apply_bilibili_comic_overlay(text)
    return text


def backup_target(target: Path, module_id: str, timestamp: str) -> str:
    if not target.exists():
        return ""
    backup = BACKUP_ROOT / module_id / f"{timestamp}.conf"
    backup.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(target, backup)
    return rel(backup)


def sync_records(records: list[dict[str, Any]], config_only: bool) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    updated: list[dict[str, str]] = []
    skipped: list[dict[str, str]] = []
    blocked: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")

    for record in records:
        module_id = str(record["id"])
        target = repo_path(record["target"])
        source_url = str(record["source_url"])
        if config_only:
            record["last_sync_mode"] = "config-only"
            skipped.append({"id": module_id, "reason": "config-only"})
            continue
        if not record.get("enabled"):
            skipped.append({"id": module_id, "reason": "disabled"})
            continue
        if not record.get("direct_commit"):
            skipped.append({"id": module_id, "reason": "direct_commit=false"})
            continue
        if not source_url:
            record["last_sync_mode"] = "missing-source"
            skipped.append({"id": module_id, "reason": "missing source_url"})
            continue
        if not raw_module_url(source_url):
            record["last_sync_mode"] = "not-module-url"
            skipped.append({"id": module_id, "reason": "source_url is not a raw module"})
            continue
        try:
            upstream_text = fetch_text(source_url)
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            record["last_sync_mode"] = "fetch-failed"
            errors.append({"id": module_id, "reason": f"fetch failed: {exc}"})
            continue
        reason = suspicious_reason(upstream_text + "\n" + source_url + "\n" + str(record.get("name", "")))
        if reason and not allow_known_spotify_upstream(module_id, source_url, reason):
            record["last_sync_mode"] = "blocked-risk"
            blocked.append({"id": module_id, "reason": reason})
            continue
        try:
            converted, upstream = converted_source(record, upstream_text)
            converted = postprocess_converted_source(record, converted)
        except ValueError as exc:
            record["last_sync_mode"] = "convert-failed"
            errors.append({"id": module_id, "reason": str(exc)})
            continue
        previous = read_text(target)
        if previous == converted:
            record["last_sync_mode"] = "unchanged"
            skipped.append({"id": module_id, "reason": "unchanged"})
            continue
        backup_path = backup_target(target, module_id, timestamp) if record.get("backup") else ""
        write_text(target, converted)
        record["upstream_project"] = str(record.get("upstream_project") or github_project_from_url(source_url))
        record["last_sync_mode"] = "updated"
        updated.append({"id": module_id, "source": source_url, "backup": backup_path, "upstream": upstream})
    return updated, skipped, blocked, errors


def write_config(path: Path, config: dict[str, Any], records: list[dict[str, Any]]) -> None:
    config["trusted_repositories"] = config.get("trusted_repositories") or TRUSTED_REPOSITORIES
    config["modules"] = [{key: record.get(key, "") for key in REQUIRED_RECORD_KEYS} for record in records]
    write_text(path, json.dumps(config, ensure_ascii=False, indent=2))


def table(rows: list[dict[str, str]], columns: list[str]) -> list[str]:
    if not rows:
        return ["_None._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(column, "")).replace("|", "\\|") for column in columns) + " |")
    return lines


def write_report(
    path: Path,
    records: list[dict[str, Any]],
    updated: list[dict[str, str]],
    skipped: list[dict[str, str]],
    blocked: list[dict[str, str]],
    errors: list[dict[str, str]],
) -> None:
    enabled = sum(1 for record in records if record.get("enabled"))
    direct = sum(1 for record in records if record.get("direct_commit"))
    lines = [
        "# Upstream App Module Sync Report",
        "",
        f"- generated: {dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace('+00:00', 'Z')}",
        f"- modules: {len(records)}",
        f"- enabled: {enabled}",
        f"- direct_commit: {direct}",
        f"- updated: {len(updated)}",
        f"- skipped: {len(skipped)}",
        f"- blocked: {len(blocked)}",
        f"- errors: {len(errors)}",
        "",
        "## Updated",
        *table(updated, ["id", "upstream", "backup", "source"]),
        "",
        "## Skipped",
        *table(skipped, ["id", "reason"]),
        "",
        "## Blocked",
        *table(blocked, ["id", "reason"]),
        "",
        "## Errors",
        *table(errors, ["id", "reason"]),
    ]
    write_text(path, "\n".join(lines))


def selected_records(
    records: list[dict[str, Any]],
    projects: list[str],
    module_ids: list[str],
) -> list[dict[str, Any]]:
    project_needles = [item.lower() for item in projects if item.strip()]
    id_needles = {item.strip() for item in module_ids if item.strip()}
    if not project_needles and not id_needles:
        return records
    out: list[dict[str, Any]] = []
    for record in records:
        module_id = str(record.get("id", ""))
        source_url = str(record.get("source_url", "")).lower()
        upstream_project = str(record.get("upstream_project", "")).lower()
        if id_needles and module_id in id_needles:
            out.append(record)
            continue
        if project_needles and any(needle in upstream_project or needle in source_url for needle in project_needles):
            out.append(record)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync upstream raw app modules into Rewrite/Sources/Apps.")
    parser.add_argument("--config", default=rel(DEFAULT_CONFIG), help="Path to Rewrite/Remotes/app-modules.json")
    parser.add_argument("--apps-dir", default=rel(DEFAULT_APPS_DIR), help="App source directory")
    parser.add_argument("--report", default=rel(DEFAULT_REPORT), help="Markdown report path")
    parser.add_argument("--config-only", action="store_true", help="Only discover and write app-modules.json/report")
    parser.add_argument("--no-kelee", action="store_true", help="Do not import Kelee PluginHub app ad modules")
    parser.add_argument("--project", action="append", default=[], help="Only sync records matching this upstream project or URL")
    parser.add_argument("--id", action="append", default=[], help="Only sync a specific module id")
    args = parser.parse_args()

    config_path = repo_path(args.config)
    apps_dir = repo_path(args.apps_dir)
    report_path = repo_path(args.report)

    try:
        config = read_json(config_path)
        records = discover_modules(config, apps_dir)
        records = merge_kelee_catalog(records, include_kelee=not args.no_kelee)
        targets = selected_records(records, args.project, args.id)
        updated, skipped, blocked, errors = sync_records(targets, args.config_only)
        write_config(config_path, config, records)
        write_report(report_path, targets, updated, skipped, blocked, errors)
    except SyncError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(
        "Upstream app module sync complete: "
        f"{len(records)} module(s), {len(updated)} updated, "
        f"{len(blocked)} blocked, {len(errors)} error(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
