# 候选源安全评分报告

生成时间：2026-06-01 01:45:38 +0800

本报告只评分候选源，不自动启用、不自动禁用、不自动晋级 Stable。

## 总体统计

- 候选总数：11
- candidate-ok：9
- manual-review：2
- block：0
- enabled-risk：0

## 判定规则

- `candidate-ok`：可信来源、低风险规则类候选，可以继续进入候选/测试流程。
- `manual-review`：需要人工复核，不能直接进入 Stable。
- `block`：包含高风险关键词、未知来源或风险过高，不能启用。
- `enabled-risk`：已启用但评分为阻断风险，必须人工处理。

## 候选评分明细

| 候选 | 类型 | 启用 | 激活 | 分数 | 结论 | 原因 | URL |
|---|---|---|---|---:|---|---|---|
| blackmatrix7 Advertising Lite | remote_rule | 是 | 是 | 100 | candidate-ok | trusted:blackmatrix7/ios_rule_script; remote-rule; warning-keywords:script; safe-keywords:ad,advert,advertising,lite,surge | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AdvertisingLite/AdvertisingLite.list` |
| blackmatrix7 Hijacking | remote_rule | 是 | 是 | 99 | candidate-ok | trusted:blackmatrix7/ios_rule_script; remote-rule; warning-keywords:script; safe-keywords:hijacking,surge | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Hijacking/Hijacking.list` |
| blackmatrix7 Privacy | remote_rule | 是 | 是 | 100 | candidate-ok | trusted:blackmatrix7/ios_rule_script; remote-rule; warning-keywords:script; safe-keywords:privacy,surge,tracker | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Privacy/Privacy.list` |
| blackmatrix7 Privacy Lite | remote_rule | 否 | 否 | 100 | candidate-ok | trusted:blackmatrix7/ios_rule_script; remote-rule; warning-keywords:script; safe-keywords:lite,privacy,surge,tracker | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/PrivacyLite/PrivacyLite.list` |
| blackmatrix7 Advertising MiTV | remote_rule | 是 | 是 | 100 | candidate-ok | trusted:blackmatrix7/ios_rule_script; remote-rule; warning-keywords:script; safe-keywords:ad,advert,advertising,surge | `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AdvertisingMiTV/AdvertisingMiTV.list` |
| ACL4SSR BanProgramAD | remote_rule | 是 | 是 | 100 | candidate-ok | trusted:ACL4SSR/ACL4SSR; remote-rule; safe-keywords:ad,advert,advertising | `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list` |
| ACL4SSR BanEasyListChina | remote_rule | 是 | 是 | 100 | candidate-ok | trusted:ACL4SSR/ACL4SSR; remote-rule; safe-keywords:ad,advert,advertising | `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyListChina.list` |
| Loyalsoldier reject domain set | remote_rule | 否 | 否 | 100 | candidate-ok | trusted:Loyalsoldier/surge-rules; remote-rule; safe-keywords:ad,reject,surge | `https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/reject.txt` |
| Cats-Team AdRules DNS list | remote_rule | 否 | 否 | 100 | candidate-ok | trusted:Cats-Team/AdRules; remote-rule; safe-keywords:ad,domain-set | `https://raw.githubusercontent.com/Cats-Team/AdRules/main/dns.txt` |
| app2smile Tieba script | script | 否 | 否 | 72 | manual-review | trusted:app2smile/rules; script-candidate; pending; warning-keywords:body,script; safe-keywords:ad | `https://raw.githubusercontent.com/app2smile/rules/master/js/tieba-json.js` |
| Maasea YouTube Enhance reference | reference_module | 否 | 否 | 85 | manual-review | trusted:Maasea/sgmodule; reference-only; protected-reference | `https://github.com/Maasea/sgmodule` |

## 处理原则

1. 规则源可以自动进入候选报告，但不能无审核直接进入 Stable。
2. 脚本候选默认 pending，必须人工复核和真机测试。
3. 出现 Cookie、Token、登录、支付、验证码、会员权益、混淆、代理镜像等关键词时，不得自动启用。
4. Stable Plus 或 pending 通过真实测试后，才允许单项晋级 Stable。
