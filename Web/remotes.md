# Remote Source Catalog

Target: Web distribution

## Summary

- Rule sets: 16
- Enabled rule sets: 14
- Protected rule sets: 2
- Reference modules: 24
- Enabled reference modules: 0
- Protected reference modules: 12

## Active rule sets

| Name | Type | Policy | Protected | Purpose | URL |
|---|---|---|---|---|---|
| blackmatrix7 Advertising | RULE-SET | REJECT | True | general advertising rules | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Advertising/Advertising.list |
| Cats-Team AdRules | DOMAIN-SET | REJECT | True | domain advertising rules | https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules_surge_domainset.txt |
| anti-AD Surge | DOMAIN-SET | REJECT | False | domain-set advertising supplement | https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge2.txt |
| ACL4SSR BanAD | RULE-SET | REJECT | False | advertising supplement | https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list |
| Loyalsoldier reject | DOMAIN-SET | REJECT | False | domain-set advertising supplement | https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/reject.txt |
| 217heidai adblockfilters | DOMAIN-SET | REJECT | False | domain-set advertising supplement | https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksurge.list |
| blackmatrix7 Advertising Lite | RULE-SET | REJECT | False | trusted same-upstream advertising candidate enabled for conservative collection | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AdvertisingLite/AdvertisingLite.list |
| blackmatrix7 Hijacking | RULE-SET | REJECT | False | trusted anti-hijacking rule candidate enabled for conservative collection | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Hijacking/Hijacking.list |
| blackmatrix7 Privacy | RULE-SET | REJECT | False | trusted privacy and tracker rule candidate enabled for conservative collection | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Privacy/Privacy.list |
| ACL4SSR BanProgramAD | RULE-SET | REJECT | False | trusted program advertising rule candidate enabled for conservative collection | https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list |
| ACL4SSR BanEasyListChina | RULE-SET | REJECT | False | trusted China advertising supplement enabled for conservative collection | https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyListChina.list |
| blackmatrix7 Advertising MiTV | RULE-SET | REJECT | False | trusted TV advertising rule enabled for conservative collection | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AdvertisingMiTV/AdvertisingMiTV.list |
| ACL4SSR BanEasyList | RULE-SET | REJECT | False | trusted EasyList advertising supplement enabled for conservative collection | https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyList.list |
| ACL4SSR BanEasyPrivacy | RULE-SET | REJECT | False | trusted EasyPrivacy tracker supplement enabled for conservative collection | https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyPrivacy.list |

## Reference modules

| Name | Enabled | Protected | Purpose | URL |
|---|---:|---:|---|---|
| Kelee Spotify module | False | True | reference/source for Spotify app module; synced through Rewrite/Remotes/app-modules.json | https://kelee.one/Tool/Loon/Lpx/Spotify_remove_ads.lpx |
| app2smile Qidian module | False | True | reference only; extract source-first into Stable Plus after manual review | https://raw.githubusercontent.com/app2smile/rules/master/module/qidian.sgmodule |
| app2smile Bilibili module | False | True | reference only; extract source-first into Stable Plus after manual review | https://raw.githubusercontent.com/app2smile/rules/master/module/bilibili.sgmodule |
| app2smile Tieba module | False | True | reference only; extract source-first into Stable Plus after manual review | https://raw.githubusercontent.com/app2smile/rules/master/module/tieba.sgmodule |
| app2smile QQ News module | False | True | reference only; extract source-first into Stable Plus after manual review | https://raw.githubusercontent.com/app2smile/rules/master/module/qqnews.sgmodule |
| app2smile VGTime module | False | True | reference only; extract source-first into Stable Plus after manual review | https://raw.githubusercontent.com/app2smile/rules/master/module/vgtime.sgmodule |
| app2smile YouTube module | False | True | reference only; never replace existing YouTube core entries without manual testing | https://raw.githubusercontent.com/app2smile/rules/master/module/youtube.sgmodule |
| app2smile Zhihu module | False | True | reference only; never replace existing Zhihu entries without manual testing | https://raw.githubusercontent.com/app2smile/rules/master/module/zhihu.sgmodule |
| app2smile Baidu Map module | False | True | reference only; extract source-first into Stable Plus after manual review | https://raw.githubusercontent.com/app2smile/rules/master/module/baidumap.sgmodule |
| app2smile Adsense module | False | True | reference only; extract source-first into Stable Plus after manual review | https://raw.githubusercontent.com/app2smile/rules/master/module/adsense.sgmodule |
| app2smile Baidu no redirect module | False | True | reference only; redirect behavior must be manually reviewed before activation | https://raw.githubusercontent.com/app2smile/rules/master/module/baidu-no-redirect.sgmodule |
| Maasea sgmodule | False | True | YouTube Enhance reference source | https://github.com/Maasea/sgmodule |
| zirawell Taobao module | False | False | reference for Taobao aggressive source-first extraction | https://raw.githubusercontent.com/zirawell/R-Store/main/Rule/Surge/Adblock/App/T/%E6%B7%98%E5%AE%9D/taobao.sgmodule |
| zirawell JD module | False | False | reference for JD aggressive source-first extraction | https://raw.githubusercontent.com/zirawell/R-Store/main/Rule/Surge/Adblock/App/J/%E4%BA%AC%E4%B8%9C/jd.sgmodule |
| zirawell Pinduoduo module | False | False | reference for Pinduoduo aggressive source-first extraction | https://raw.githubusercontent.com/zirawell/R-Store/main/Rule/Surge/Adblock/App/P/%E6%8B%BC%E5%A4%9A%E5%A4%9A/pdd.sgmodule |
| zirawell Xiaohongshu module | False | False | reference for Xiaohongshu aggressive source-first extraction | https://raw.githubusercontent.com/zirawell/R-Store/main/Rule/Surge/Adblock/App/X/%E5%B0%8F%E7%BA%A2%E4%B9%A6/xiaohongshu.sgmodule |
| zirawell Zhihu module | False | False | reference for Zhihu aggressive source-first extraction | https://raw.githubusercontent.com/zirawell/R-Store/main/Rule/Surge/Adblock/App/Z/%E7%9F%A5%E4%B9%8E/zhihu.sgmodule |
| fmz200 Taobao module | False | False | secondary Taobao reference for comparison | https://raw.githubusercontent.com/fmz200/wool_scripts/main/Surge/module/split/partT/Taobao.sgmodule |
| fmz200 JD module | False | False | secondary JD reference for comparison | https://raw.githubusercontent.com/fmz200/wool_scripts/main/Surge/module/split/partJ/JD.com.sgmodule |
| fmz200 Pinduoduo module | False | False | secondary Pinduoduo reference for comparison | https://raw.githubusercontent.com/fmz200/wool_scripts/main/Surge/module/split/partP/Pinduoduo.sgmodule |
| fmz200 Bilibili module | False | False | secondary Bilibili reference for comparison | https://raw.githubusercontent.com/fmz200/wool_scripts/main/Surge/module/split/partB/bilibili.sgmodule |
| fmz200 Xiaohongshu module | False | False | secondary Xiaohongshu reference for comparison | https://raw.githubusercontent.com/fmz200/wool_scripts/main/Surge/module/split/partX/Xiaohongshu.sgmodule |
| fmz200 Zhihu module | False | False | secondary Zhihu reference for comparison | https://raw.githubusercontent.com/fmz200/wool_scripts/main/Surge/module/split/partZ/Zhihu.sgmodule |
| zirawell App AdBlock module | False | False | broad aggressive app ad block module reference for domestic app residual ads | https://raw.githubusercontent.com/zirawell/R-Store/main/Rule/Surge/Adblock/All/appAdBlock.sgmodule |
