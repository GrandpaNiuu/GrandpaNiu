# 每日模块更新报告

- 日期：2026-06-11
- 日期源头：Rewrite/Sources/Meta.conf
- 构建流程：Meta.conf -> convert_quanx_rules.py -> build_android_rules.py -> build_module.py --build --profile stable -> factory_finalize.py --sync-root -> build_release_variants.py -> validate_remote_rule_syntax.py -> validate_governance_extensions.py -> validate_repository.py -> repository_health_check.py

## QuanX 转换结果

```text
Normalized pure DOMAIN-SET remotes in: backup/Ronghemokuai.before-factory-refactor.sgmodule, backup/Ronghemokuai.stable.sgmodule
Converted zirawell App AdBlock: Rules/converted/zirawell-appAdBlock-shadowrocket.list (1411 lines)
Converted zirawell All AdBlock: Rules/converted/zirawell-allAdBlock-shadowrocket.list (1435 lines)
```

## Android 生成检查结果

```text
Android rule formats generated.

Android format check passed.
```

## Stable 构建输出

```text
Built /home/runner/work/GrandpaNiu/GrandpaNiu/Release/Ronghemokuai.sgmodule (2923 lines) using profile=stable

no output

Built 4 release variants and wrote /home/runner/work/GrandpaNiu/GrandpaNiu/reports/multi_release_report.md
```

## Android 规则报告

# Android 规则生成报告

- 最后更新时间：2026-06-11 06:27:17
- App 总数：18
- 当前 Android App 源头：Android/mihomo/apps/*.yaml
- iOS 可复用源头：Rules/reject.list -> iOS-Compatible-Reject
- 输出：Mihomo / sing-box / AdGuard / v2rayNG

| App | 规则数 | 四格式输出 |
|---|---:|---|
| Bilibili | 5 | 是 |
| Domestic-Apps | 160 | 是 |
| Douyin | 12 | 是 |
| iOS-Compatible-Reject | 266 | 是 |
| iQiyi | 4 | 是 |
| Kugou | 4 | 是 |
| MangoTV | 12 | 是 |
| Meituan-Dianping | 11 | 是 |
| NeteaseMusic | 5 | 是 |
| Pinduoduo | 12 | 是 |
| Spotify | 14 | 是 |
| Taobao | 13 | 是 |
| TencentMusic | 5 | 是 |
| Weibo | 6 | 是 |
| Xiaohongshu | 7 | 是 |
| Ximalaya | 6 | 是 |
| Youku | 8 | 是 |
| YouTube | 15 | 是 |


## 远程规则语法报告

# 远程规则语法校验报告

生成时间：2026-06-11 06:27:20 +0800

本报告用于阻断 Shadowrocket / Surge 远程规则集红叉问题。校验目标包括：

- `RULE-SET` 远程内容必须是 Shadowrocket/Surge 可识别的规则类型。
- `DOMAIN-SET` 远程内容必须是纯域名集合，不允许混入带逗号的规则行。
- 不允许把 Quantumult X 的 `host`、`host-suffix`、`host-keyword`、`ip6-cidr` 直接作为 Shadowrocket `RULE-SET`。
- 已知纯域名上游会在验证前自动规范成 `DOMAIN-SET`，防止旧生成文件反复导致红叉。
- 仓库自有 Pages / raw 链接严格阻断；外部源下载失败记录为 warn，避免网络抖动阻断仓库构建。

## 汇总

- 检查远程规则数：14
- 通过：14
- 警告：0
- 失败：0
- 自动规范化文件数：0

## 自动规范化文件

- 无

## 明细

| 状态 | 类型 | 规则数 | 检查来源 | 引用位置 | URL | 错误 / 警告 |
|---|---|---:|---|---|---|---|
| pass | DOMAIN-SET | 189074 | http:200 | Release/Ronghemokuai-full.sgmodule:543<br>Release/Ronghemokuai-lite.sgmodule:475<br>Release/Ronghemokuai-stable-plus.sgmodule:568<br>Release/Ronghemokuai-stable.sgmodule:541<br>Release/Ronghemokuai.sgmodule:538<br>Rewrite/Remotes/sources.json:217heidai adblockfilters<br>Ronghemokuai.sgmodule:538 | `https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksurge.list` | - |
| pass | DOMAIN-SET | 176703 | http:200 | Release/Ronghemokuai-full.sgmodule:539<br>Release/Ronghemokuai-lite.sgmodule:471<br>Release/Ronghemokuai-stable-plus.sgmodule:564<br>Release/Ronghemokuai-stable.sgmodule:537<br>Release/Ronghemokuai.sgmodule:534<br>Rewrite/Remotes/sources.json:Cats-Team AdRules<br>Ronghemokuai.sgmodule:534 | `https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules_surge_domainset.txt` | - |
| pass | DOMAIN-SET | 166028 | http:200 | Release/Ronghemokuai-full.sgmodule:542<br>Release/Ronghemokuai-lite.sgmodule:474<br>Release/Ronghemokuai-stable-plus.sgmodule:567<br>Release/Ronghemokuai-stable.sgmodule:540<br>Release/Ronghemokuai.sgmodule:537<br>Rewrite/Remotes/sources.json:Loyalsoldier reject<br>Ronghemokuai.sgmodule:537 | `https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/reject.txt` | - |
| pass | DOMAIN-SET | 103435 | http:200 | Release/Ronghemokuai-full.sgmodule:540<br>Release/Ronghemokuai-lite.sgmodule:472<br>Release/Ronghemokuai-stable-plus.sgmodule:565<br>Release/Ronghemokuai-stable.sgmodule:538<br>Release/Ronghemokuai.sgmodule:535<br>Rewrite/Remotes/sources.json:anti-AD Surge<br>Ronghemokuai.sgmodule:535 | `https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge2.txt` | - |
| pass | RULE-SET | 1423 | local:Rules/converted/zirawell-allAdBlock-shadowrocket.list | Release/Ronghemokuai-full.sgmodule:537<br>Release/Ronghemokuai-stable-plus.sgmodule:562<br>Rules/aggressive-ad-sources.list:2 | `https://grandpaniuu.github.io/GrandpaNiu/Rules/converted/zirawell-allAdBlock-shadowrocket.list` | - |
| pass | RULE-SET | 1399 | local:Rules/converted/zirawell-appAdBlock-shadowrocket.list | Release/Ronghemokuai-full.sgmodule:536<br>Release/Ronghemokuai-stable-plus.sgmodule:561<br>Rules/aggressive-ad-sources.list:1 | `https://grandpaniuu.github.io/GrandpaNiu/Rules/converted/zirawell-appAdBlock-shadowrocket.list` | - |
| pass | RULE-SET | 588 | http:200 | Release/Ronghemokuai-full.sgmodule:541<br>Release/Ronghemokuai-lite.sgmodule:473<br>Release/Ronghemokuai-stable-plus.sgmodule:566<br>Release/Ronghemokuai-stable.sgmodule:539<br>Release/Ronghemokuai.sgmodule:536<br>Rewrite/Remotes/sources.json:ACL4SSR BanAD<br>Ronghemokuai.sgmodule:536 | `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list` | - |
| pass | RULE-SET | 5050 | http:200 | Release/Ronghemokuai-full.sgmodule:548<br>Release/Ronghemokuai-lite.sgmodule:480<br>Release/Ronghemokuai-stable-plus.sgmodule:573<br>Release/Ronghemokuai-stable.sgmodule:546<br>Release/Ronghemokuai.sgmodule:543<br>Rewrite/Remotes/sources.json:ACL4SSR BanEasyListChina<br>Ronghemokuai.sgmodule:543 | `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyListChina.list` | - |
| pass | RULE-SET | 1016 | http:200 | Release/Ronghemokuai-full.sgmodule:547<br>Release/Ronghemokuai-lite.sgmodule:479<br>Release/Ronghemokuai-stable-plus.sgmodule:572<br>Release/Ronghemokuai-stable.sgmodule:545<br>Release/Ronghemokuai.sgmodule:542<br>Rewrite/Remotes/sources.json:ACL4SSR BanProgramAD<br>Ronghemokuai.sgmodule:542 | `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list` | - |
| pass | RULE-SET | 782 | http:200 | Release/Ronghemokuai-full.sgmodule:538<br>Release/Ronghemokuai-lite.sgmodule:470<br>Release/Ronghemokuai-stable-plus.sgmodule:563<br>Release/Ronghemokuai-stable.sgmodule:536<br>Release/Ronghemokuai.sgmodule:533<br>Rewrite/Remotes/sources.json:blackmatrix7 Advertising<br>Ronghemokuai.sgmodule:533 | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Advertising/Advertising.list` | - |
| pass | RULE-SET | 377 | http:200 | Release/Ronghemokuai-full.sgmodule:544<br>Release/Ronghemokuai-lite.sgmodule:476<br>Release/Ronghemokuai-stable-plus.sgmodule:569<br>Release/Ronghemokuai-stable.sgmodule:542<br>Release/Ronghemokuai.sgmodule:539<br>Rewrite/Remotes/sources.json:blackmatrix7 Advertising Lite<br>Ronghemokuai.sgmodule:539 | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AdvertisingLite/AdvertisingLite.list` | - |
| pass | RULE-SET | 165 | http:200 | Release/Ronghemokuai-full.sgmodule:549<br>Release/Ronghemokuai-lite.sgmodule:481<br>Release/Ronghemokuai-stable-plus.sgmodule:574<br>Release/Ronghemokuai-stable.sgmodule:547<br>Release/Ronghemokuai.sgmodule:544<br>Rewrite/Remotes/sources.json:blackmatrix7 Advertising MiTV<br>Ronghemokuai.sgmodule:544 | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AdvertisingMiTV/AdvertisingMiTV.list` | - |
| pass | RULE-SET | 228 | http:200 | Release/Ronghemokuai-full.sgmodule:545<br>Release/Ronghemokuai-lite.sgmodule:477<br>Release/Ronghemokuai-stable-plus.sgmodule:570<br>Release/Ronghemokuai-stable.sgmodule:543<br>Release/Ronghemokuai.sgmodule:540<br>Rewrite/Remotes/sources.json:blackmatrix7 Hijacking<br>Ronghemokuai.sgmodule:540 | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Hijacking/Hijacking.list` | - |
| pass | RULE-SET | 20 | http:200 | Release/Ronghemokuai-full.sgmodule:546<br>Release/Ronghemokuai-lite.sgmodule:478<br>Release/Ronghemokuai-stable-plus.sgmodule:571<br>Release/Ronghemokuai-stable.sgmodule:544<br>Release/Ronghemokuai.sgmodule:541<br>Rewrite/Remotes/sources.json:blackmatrix7 Privacy<br>Ronghemokuai.sgmodule:541 | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Privacy/Privacy.list` | - |

## 发布规则

- 本报告出现 `fail` 时，不允许发布模块。
- `warn` 表示外部源下载失败或临时不可读，需要人工观察，但不阻断仓库自有构建。
- 新增远程源前，必须先确认源格式属于 `RULE-SET` 或 `DOMAIN-SET` 的真实兼容格式。
- 如果上游是 Quantumult X 格式，必须先转换到 `Rules/converted/` 后再引用。
- 如果上游是纯域名列表，必须用 `DOMAIN-SET`，不能用 `RULE-SET`。


## 完整区块检查结果

- `[Rule]`：通过
- `[URL Rewrite]`：通过
- `[Header Rewrite]`：通过
- `[Body Rewrite]`：通过
- `[Map Local]`：通过
- `[Script]`：通过
- `[MITM]`：通过

## 核心检查结果

- `spotify-json`：通过
- `spotify-proto`：通过
- `youtube.response`：通过
- `zhihu-enhance`：通过
- `zhihu-enhance.js`：通过
- `update-url`：通过
- `meta-date`：通过

## 多版本文件检查

- `Release/Ronghemokuai-stable.sgmodule`：通过
- `Release/Ronghemokuai-stable-plus.sgmodule`：通过
- `Release/Ronghemokuai-lite.sgmodule`：通过
- `Release/Ronghemokuai-full.sgmodule`：通过

## 远程链接检查结果

- `https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule`：OK HTTP 200
- `https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Scripts/zhihu-enhance.js`：OK HTTP 200
- `https://grandpaniuu.github.io/GrandpaNiu/Rules/converted/zirawell-appAdBlock-shadowrocket.list`：OK HTTP 200
- `https://grandpaniuu.github.io/GrandpaNiu/Rules/converted/zirawell-allAdBlock-shadowrocket.list`：OK HTTP 200
- `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Advertising/Advertising.list`：OK HTTP 200
- `https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules_surge_domainset.txt`：OK HTTP 200
- `https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge2.txt`：OK HTTP 200
- `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list`：OK HTTP 200
- `https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/reject.txt`：OK HTTP 200
- `https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksurge.list`：OK HTTP 200
- `https://raw.githubusercontent.com/app2smile/rules/master/js/spotify-json.js`：OK HTTP 200
- `https://raw.githubusercontent.com/app2smile/rules/master/js/spotify-proto.js`：OK HTTP 200
- `https://raw.githubusercontent.com/Maasea/sgmodule/master/Script/Youtube/youtube.response.js`：OK HTTP 200

## validate_remote_rule_syntax.py 输出

```text
Remote rule syntax validation completed: 14 source(s), 0 warning(s), 0 normalization file(s); report=reports/remote_rule_syntax_report.md
```

## validate_governance_extensions.py 输出

```text
Governance extension validation passed.
```

## validate_repository.py 输出

```text
Repository validation passed.
```

## 治理报告刷新输出

```text
$ validate_profiles.py
Profile validation report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/profile_validation_report.md

$ audit_reject_risk.py
Reject risk report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/reject_risk_report.md

$ generate_app_status_matrix.py
App status matrix written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/app_status_matrix.md

$ create_promotion_pr.py
Promotion PR report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/promotion_pr_report.md

$ score_candidates.py
Candidate security score report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/candidate_security_score_report.md

$ audit_domestic_app_connectivity.py
Domestic App connectivity audit written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/domestic_app_connectivity_audit.md

$ generate_workflow_health_report.py
Workflow health report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/workflow_health_report.md

$ check_report_freshness.py
Report freshness report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/report_freshness_report.md
```

## repository_health_check.py 输出

```text
Repository health report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/repository_health_report.md
```

## check_report_freshness.py 输出

```text
Report freshness report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/report_freshness_report.md
```

## 自动更新边界说明

- 本 workflow 会更新源头日期、转换 QuanX 远程规则、重新构建 stable、同步 Release 与 Root，并生成四个独立 Release 版本。
- 本 workflow 会校验远程 RULE-SET / DOMAIN-SET 语法，失败时阻断发布。
- 本 workflow 会从 Android/mihomo/apps/*.yaml 生成 Android 多格式 App 规则。
- 默认根目录 Ronghemokuai.sgmodule 仍保持 stable。
- Full 只用于排查，不自动合并进 Stable。
- 不自动删除规则。
