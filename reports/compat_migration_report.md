# 兼容层迁移审计报告

- 日期：2026-06-08
- source_rule_compat 当前是否开启：是
- source_script_compat 当前是否开启：是
- Rule.conf 行数：525
- Script.conf 行数：141
- 已迁移规则数量：490
- 未迁移规则数量：0
- 已迁移脚本数量：31
- 未迁移脚本数量：0
- 建议下一步是否可以关闭 compat：可以，但必须构建验证并手动测试
- 关闭 compat 后 Root / Release 是否一致：需运行 Module Factory Build 后确认

## 未迁移规则

- 无

## 未迁移脚本

- 无

## 风险说明

- 本脚本只生成报告，不直接修改 profile。
- 关闭 compat 前必须确认 Root 与 Release 一致，并手动测试 Spotify、YouTube、知乎、登录、支付和验证码。
- 远程 RULE-SET / DOMAIN-SET 如果已存在于 Rewrite/Remotes/sources.json，会被视为已迁移。
- 如果仍存在未迁移项，应先迁移到 Rules/*.list、Scripts/*.conf 或 Rewrite/Remotes/sources.json，再考虑关闭 compat。
