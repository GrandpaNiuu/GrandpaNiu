# Module Factory Diff Report

Root lines: 2840
Release lines: 2855
Diff lines: 31
Diff clipped: no

```diff
--- Ronghemokuai.sgmodule
+++ Release/Ronghemokuai.sgmodule
@@ -516,6 +516,18 @@
 RULE-SET,https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/reject.txt,REJECT
 # remote: 217heidai adblockfilters
 RULE-SET,https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksurge.list,REJECT
+# Direct rules
+# Spotify rules
+# YouTube rules
+# Reject rules
+# App rules
+# Web rules
+# remote: blackmatrix7 Advertising
+# remote: Cats-Team AdRules
+# remote: anti-AD Surge
+# remote: ACL4SSR BanAD
+# remote: Loyalsoldier reject
+# remote: 217heidai adblockfilters
 # Spotify playback protection rules
 # Keep these rules before remote advertising sources.
 # YouTube playback protection placeholder
@@ -2728,6 +2740,9 @@
 cmp_block_095_rrtv_json = type=http-response,pattern=^https?:\/\/api\.rr\.tv\/ad\/getAll,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/rrtv_json.js,requires-body=1,timeout=60,script-update-interval=86400
 cmp_block_096_ad = type=http-response,pattern=^https?:\/\/haojia\.m\.smzdm\.com\/detail_modul\/user_related_modul\?,script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/smzdm/smzdm_ads.js,requires-body=1,timeout=60,script-update-interval=86400
 cmp_block_099_ad = type=http-response,pattern=^https?:\/\/dict\.youdao\.com\/(homepage\/promotion|course\/tab\/home|homepage\/tile),script-path=https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/youdao/dict-youdao-ad.js,requires-body=1,timeout=60,script-update-interval=86400
+# Spotify scripts
+# YouTube scripts
+# App scripts
 # === 新框架 Layer 5：Script 层 ===
 # 原 YouTube/Spotify 脚本保持不覆盖；新增脚本统一 cmp_ 前缀，来源公开 raw，按去广告用途筛选。
 
```
