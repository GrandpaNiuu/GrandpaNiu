# 远程规则语法校验报告

生成时间：2026-06-14 05:49:06 +0800

本报告用于阻断 Shadowrocket / Surge 远程规则集红叉问题。校验目标包括：

- `RULE-SET` 远程内容必须是 Shadowrocket/Surge 可识别的规则类型。
- `DOMAIN-SET` 远程内容必须是纯域名集合，不允许混入带逗号的规则行。
- 不允许把 Quantumult X 的 `host`、`host-suffix`、`host-keyword`、`ip6-cidr` 直接作为 Shadowrocket `RULE-SET`。
- 已知纯域名上游会在验证前自动规范成 `DOMAIN-SET`，防止旧生成文件反复导致红叉。
- 仓库自有 Pages / raw 链接严格阻断；外部源下载失败记录为 warn，避免网络抖动阻断仓库构建。

## 汇总

- 检查远程规则数：17
- 通过：17
- 警告：0
- 失败：0
- 自动规范化文件数：0

## 自动规范化文件

- 无

## 明细

| 状态 | 类型 | 规则数 | 检查来源 | 引用位置 | URL | 错误 / 警告 |
|---|---|---:|---|---|---|---|
| pass | DOMAIN-SET | 179779 | http:200 | Release/Ronghemokuai.sgmodule:695<br>Rewrite/Remotes/sources.json:217heidai adblockfilters<br>Ronghemokuai.sgmodule:695 | `https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksurge.list` | - |
| pass | DOMAIN-SET | 177791 | http:200 | Release/Ronghemokuai.sgmodule:691<br>Rewrite/Remotes/sources.json:Cats-Team AdRules<br>Ronghemokuai.sgmodule:691 | `https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules_surge_domainset.txt` | - |
| pass | DOMAIN-SET | 167120 | http:200 | Release/Ronghemokuai.sgmodule:694<br>Rewrite/Remotes/sources.json:Loyalsoldier reject<br>Ronghemokuai.sgmodule:694 | `https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/reject.txt` | - |
| pass | DOMAIN-SET | 104136 | http:200 | Release/Ronghemokuai.sgmodule:692<br>Rewrite/Remotes/sources.json:anti-AD Surge<br>Ronghemokuai.sgmodule:692 | `https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge2.txt` | - |
| pass | RULE-SET | 1423 | local:Rules/converted/zirawell-allAdBlock-shadowrocket.list | Release/Ronghemokuai.sgmodule:805<br>Ronghemokuai.sgmodule:805<br>Rules/aggressive-ad-sources.list:2 | `https://grandpaniuu.github.io/GrandpaNiu/Rules/converted/zirawell-allAdBlock-shadowrocket.list` | - |
| pass | RULE-SET | 1399 | local:Rules/converted/zirawell-appAdBlock-shadowrocket.list | Release/Ronghemokuai.sgmodule:804<br>Ronghemokuai.sgmodule:804<br>Rules/aggressive-ad-sources.list:1 | `https://grandpaniuu.github.io/GrandpaNiu/Rules/converted/zirawell-appAdBlock-shadowrocket.list` | - |
| pass | RULE-SET | 588 | http:200 | Release/Ronghemokuai.sgmodule:693<br>Rewrite/Remotes/sources.json:ACL4SSR BanAD<br>Ronghemokuai.sgmodule:693 | `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list` | - |
| pass | RULE-SET | 40977 | http:200 | Release/Ronghemokuai.sgmodule:1104<br>Rewrite/Remotes/sources.json:ACL4SSR BanEasyList<br>Ronghemokuai.sgmodule:1104 | `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyList.list` | - |
| pass | RULE-SET | 5050 | http:200 | Release/Ronghemokuai.sgmodule:700<br>Rewrite/Remotes/sources.json:ACL4SSR BanEasyListChina<br>Ronghemokuai.sgmodule:700 | `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyListChina.list` | - |
| pass | RULE-SET | 39852 | http:200 | Release/Ronghemokuai.sgmodule:1105<br>Rewrite/Remotes/sources.json:ACL4SSR BanEasyPrivacy<br>Ronghemokuai.sgmodule:1105 | `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyPrivacy.list` | - |
| pass | RULE-SET | 1016 | http:200 | Release/Ronghemokuai.sgmodule:699<br>Rewrite/Remotes/sources.json:ACL4SSR BanProgramAD<br>Ronghemokuai.sgmodule:699 | `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list` | - |
| pass | RULE-SET | 2 | http:200 | Release/Ronghemokuai.sgmodule:1035<br>Ronghemokuai.sgmodule:1035 | `https://raw.githubusercontent.com/app2smile/rules/master/rule/tieba-ad.list` | - |
| pass | RULE-SET | 782 | http:200 | Release/Ronghemokuai.sgmodule:690<br>Rewrite/Remotes/sources.json:blackmatrix7 Advertising<br>Ronghemokuai.sgmodule:690 | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Advertising/Advertising.list` | - |
| pass | RULE-SET | 377 | http:200 | Release/Ronghemokuai.sgmodule:696<br>Rewrite/Remotes/sources.json:blackmatrix7 Advertising Lite<br>Ronghemokuai.sgmodule:696 | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AdvertisingLite/AdvertisingLite.list` | - |
| pass | RULE-SET | 165 | http:200 | Release/Ronghemokuai.sgmodule:701<br>Rewrite/Remotes/sources.json:blackmatrix7 Advertising MiTV<br>Ronghemokuai.sgmodule:701 | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AdvertisingMiTV/AdvertisingMiTV.list` | - |
| pass | RULE-SET | 228 | http:200 | Release/Ronghemokuai.sgmodule:697<br>Rewrite/Remotes/sources.json:blackmatrix7 Hijacking<br>Ronghemokuai.sgmodule:697 | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Hijacking/Hijacking.list` | - |
| pass | RULE-SET | 20 | http:200 | Release/Ronghemokuai.sgmodule:698<br>Rewrite/Remotes/sources.json:blackmatrix7 Privacy<br>Ronghemokuai.sgmodule:698 | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Privacy/Privacy.list` | - |

## 发布规则

- 本报告出现 `fail` 时，不允许发布模块。
- `warn` 表示外部源下载失败或临时不可读，需要人工观察，但不阻断仓库自有构建。
- 新增远程源前，必须先确认源格式属于 `RULE-SET` 或 `DOMAIN-SET` 的真实兼容格式。
- 如果上游是 Quantumult X 格式，必须先转换到 `Rules/converted/` 后再引用。
- 如果上游是纯域名列表，必须用 `DOMAIN-SET`，不能用 `RULE-SET`。
