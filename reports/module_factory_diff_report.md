# Module Factory Diff Report

Root lines: 2815
Release lines: 2825
Diff lines: 63
Diff clipped: no

```diff
--- Ronghemokuai.sgmodule
+++ Release/Ronghemokuai.sgmodule
@@ -12,25 +12,37 @@
 # changelog: 修复 IPv6 CIDR 与拼多多 IPv6 正则；移除 Dreame ZIP 注入、粉笔第三方图片注入、Bilibili 伪会员改写；新增 cmp_ 脚本层。
 # arguments: YouTube Enhance 参数沿用上游，字幕/歌词翻译默认关闭以降低兼容风险。
 [Rule]
-# Spotify 白名单：放在远程广告规则前，避免广告规则误杀播放链路导致跳歌
+# Spotify playback protection rules
+# Keep these rules before remote advertising sources.
 DOMAIN-SUFFIX,spotify.com,DIRECT
 DOMAIN-SUFFIX,scdn.co,DIRECT
 DOMAIN-SUFFIX,spotifycdn.com,DIRECT
 DOMAIN-SUFFIX,pscdn.co,DIRECT
 DOMAIN,spclient.wg.spotify.com,DIRECT
 DOMAIN-SUFFIX,spclient.spotify.com,DIRECT
+# YouTube playback protection placeholder
+# Keep this file available for future precise DIRECT rules.
+# Do not add broad googlevideo or google domains unless a specific conflict is confirmed.
+# Reject rules
+# remote: blackmatrix7 Advertising
+RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Advertising/Advertising.list,REJECT
+# remote: Cats-Team AdRules
+DOMAIN-SET,https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules_surge_domainset.txt,REJECT
+# remote: anti-AD Surge
+RULE-SET,https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge2.txt,REJECT
+# remote: ACL4SSR BanAD
+RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list,REJECT
+# remote: Loyalsoldier reject
+RULE-SET,https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/reject.txt,REJECT
+# remote: 217heidai adblockfilters
+RULE-SET,https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksurge.list,REJECT
+# Spotify 白名单：放在远程广告规则前，避免广告规则误杀播放链路导致跳歌
 # === 新框架 Layer 1：基础拦截层 ===
 # 顺序原则：必要 DIRECT 白名单优先，其后远程广告规则、本地域名/IP、URL-REGEX/AND 逻辑。
 # 安全边界：不主动拦截支付、登录、验证码、银行证券、微信/支付宝安全、证书校验接口。
 # GitHub 去广告规则补充（Surge 端按远程资源自动更新）
-RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Advertising/Advertising.list,REJECT
-DOMAIN-SET,https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules_surge_domainset.txt,REJECT
 # === Remote AdBlock Hub：远程广告规则增强层 ===
 # 只添加可信远程规则，不覆盖本地规则；用于补充国内外网页、App 通用广告域名。
-RULE-SET,https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge2.txt,REJECT
-RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list,REJECT
-RULE-SET,https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/reject.txt,REJECT
-RULE-SET,https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksurge.list,REJECT
 DOMAIN,dorangesource.alicdn.com,DIRECT
 DOMAIN,push.m.youku.com,DIRECT
 DOMAIN,un-acs.youku.com,DIRECT
@@ -2123,7 +2135,6 @@
 # Spotify（app2smile 必要配置，2026-05-25 上游检查）
 # 删除 if-none-match，避免 304 缓存导致 spotify-proto 无法取得可修改响应体。
 http-request ^https:\/\/(spclient\.wg\.spotify\.com|.*-spclient\.spotify\.com(:443)?)\/user-customization-service\/v1\/customize$ header-del if-none-match
-
 [Body Rewrite]
 # === 新框架 Layer 3：Body Rewrite / JQ 层 ===
 # 仅清理复杂 JSON 中广告节点；禁止改写会员权益、支付状态、账号等级与用户身份。
@@ -2599,7 +2610,6 @@
 # YouTube Enhance：仅拦截带 oad 参数的 googlevideo initplayback 广告初始化请求；若视频转圈，可临时注释本行。
 ^https?:\/\/[\w-]+\.googlevideo\.com\/initplayback.+&oad data-type=text data="" status-code=200
 [Script]
-
 # === 新框架 Layer 5：Script 层 ===
 # 原 YouTube/Spotify 脚本保持不覆盖；新增脚本统一 cmp_ 前缀，来源公开 raw，按去广告用途筛选。
 
```
