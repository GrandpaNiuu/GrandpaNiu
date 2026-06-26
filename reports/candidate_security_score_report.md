# 候选源安全评分报告

生成时间：2026-06-26 22:24:16 +0800

本报告只评分候选源，不自动启用、禁用、下载、替换或晋级 Stable。未知脚本默认 `manual-review`，高风险内容一律 `blocked`。

## 统计

- 候选总数：12
- safe-rule-candidate：8
- stable-plus-only：0
- manual-review：4
- blocked：0

## 结论定义

- `safe-rule-candidate`：可信、低风险、规则类候选，可继续进入候选收集和测试流程。
- `stable-plus-only`：只适合测试版，不进入默认 Stable。
- `manual-review`：需要人工复核，不能自动进入默认模块。
- `blocked`：不得进入任何默认模块。

## 评分明细

| 候选 | 类型 | 启用 | 激活 | source_trust_score | obfuscation_risk | request_body_risk | cookie_token_risk | payment_login_risk | membership_unlock_risk | license_status | rollback_available | final_verdict | 原因 | URL |
|---|---|---|---|---:|---|---|---|---|---|---|---|---|---|---|
| blackmatrix7 Advertising Lite | remote_rule | 是 | 是 | 95 | 低 | 低 | 低 | 低 | 低 | upstream-public-rule | 是 | safe-rule-candidate | trust=blackmatrix7/ios_rule_script; rule-hints=advert | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AdvertisingLite/AdvertisingLite.list` |
| blackmatrix7 Hijacking | remote_rule | 是 | 是 | 95 | 低 | 低 | 低 | 低 | 低 | upstream-public-rule | 是 | safe-rule-candidate | trust=blackmatrix7/ios_rule_script; rule-hints=hijacking | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Hijacking/Hijacking.list` |
| blackmatrix7 Privacy | remote_rule | 是 | 是 | 95 | 低 | 低 | 低 | 低 | 低 | upstream-public-rule | 是 | safe-rule-candidate | trust=blackmatrix7/ios_rule_script; rule-hints=privacy,tracker | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Privacy/Privacy.list` |
| blackmatrix7 Advertising MiTV | remote_rule | 是 | 是 | 95 | 低 | 低 | 低 | 低 | 低 | upstream-public-rule | 是 | safe-rule-candidate | trust=blackmatrix7/ios_rule_script; rule-hints=advert | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AdvertisingMiTV/AdvertisingMiTV.list` |
| ACL4SSR BanProgramAD | remote_rule | 是 | 是 | 95 | 低 | 低 | 低 | 低 | 低 | upstream-public-rule | 是 | safe-rule-candidate | trust=ACL4SSR/ACL4SSR; rule-hints=advert | `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list` |
| ACL4SSR BanEasyListChina | remote_rule | 是 | 是 | 95 | 低 | 低 | 低 | 低 | 低 | upstream-public-rule | 是 | safe-rule-candidate | trust=ACL4SSR/ACL4SSR; rule-hints=advert | `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyListChina.list` |
| ACL4SSR BanEasyList | remote_rule | 是 | 是 | 95 | 低 | 低 | 低 | 低 | 低 | upstream-public-rule | 是 | safe-rule-candidate | trust=ACL4SSR/ACL4SSR; rule-hints=advert | `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyList.list` |
| ACL4SSR BanEasyPrivacy | remote_rule | 是 | 是 | 95 | 低 | 低 | 低 | 低 | 低 | upstream-public-rule | 是 | safe-rule-candidate | trust=ACL4SSR/ACL4SSR; rule-hints=privacy,tracker | `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyPrivacy.list` |
| Loyalsoldier reject domain set | remote_rule | 否 | 否 | 95 | 低 | 低 | 低 | 低 | 低 | upstream-public-rule | 是 | manual-review | trust=Loyalsoldier/surge-rules; rule-hints=domain,reject | `https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/reject.txt` |
| Cats-Team AdRules DNS list | remote_rule | 否 | 否 | 95 | 低 | 低 | 低 | 低 | 低 | upstream-public-rule | 是 | manual-review | trust=Cats-Team/AdRules; rule-hints=domain,domain-set | `https://raw.githubusercontent.com/Cats-Team/AdRules/main/dns.txt` |
| app2smile Tieba script | script | 否 | 否 | 95 | 低 | 中 | 低 | 低 | 低 | unknown | 是 | manual-review | trust=app2smile/rules; script默认 pending，不能自动进入 stable | `https://raw.githubusercontent.com/app2smile/rules/master/js/tieba-json.js` |
| Maasea YouTube Enhance reference | reference_module | 否 | 否 | 95 | 低 | 低 | 低 | 低 | 低 | reference-only | 是 | manual-review | trust=Maasea/sgmodule; reference only | `https://github.com/Maasea/sgmodule` |

## 安全边界

- `blocked` 不得进入任何默认模块。
- 未知脚本默认 `manual-review`。
- 混淆脚本必须 `blocked`。
- Cookie / Token / BoxJS 必须 `blocked`。
- 会员破解 / 权益伪造必须 `blocked`。
- request-body 脚本默认不能进 Stable。
- 普通规则源可以进入 pending 或候选收集，但不能无审核进 Stable。
