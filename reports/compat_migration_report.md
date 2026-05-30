# 兼容层迁移审计报告

- 日期：2026-05-30
- source_rule_compat 当前是否开启：是
- source_script_compat 当前是否开启：是
- Rule.conf 行数：523
- Script.conf 行数：213
- 已迁移规则数量：486
- 未迁移规则数量：6
- 已迁移脚本数量：103
- 未迁移脚本数量：0
- 建议下一步是否可以关闭 compat：暂不建议

## 未迁移规则

- `RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Advertising/Advertising.list,REJECT`
- `DOMAIN-SET,https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules_surge_domainset.txt,REJECT`
- `RULE-SET,https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge2.txt,REJECT`
- `RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list,REJECT`
- `RULE-SET,https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/reject.txt,REJECT`
- `RULE-SET,https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksurge.list,REJECT`

## 未迁移脚本

- 无

## 风险说明

- 本脚本只生成报告，不关闭 compat。
- 关闭 compat 前必须确认 Root 与 Release 一致，并手动测试 Spotify、YouTube、知乎、登录、支付和验证码。
- 如果仍存在未迁移项，应先迁移到 Rules/*.list 或 Scripts/*.conf，再考虑关闭 compat。
