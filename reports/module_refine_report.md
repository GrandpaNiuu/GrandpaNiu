# 模块安全整理报告

生成时间：2026-05-29 00:39:31 +0800

## 本次原则

- 不删除现有有效规则。
- 不改写 Spotify、YouTube 核心脚本。
- 不自动删除 script-path、RULE-SET、DOMAIN-SET。
- 只融合同一 script-path 且执行参数一致的脚本条目。
- 过长 pattern 或复杂 argument 脚本不融合。

## 结果

- 整理前脚本条目数：102
- 整理后脚本条目数：102
- 减少显示脚本数：0

## 融合记录

- 没有发现可安全融合的脚本组，因此未强行合并。

## 重复统计

- 重复脚本名称组：0
- 重复规则行组：0
- 重复 MITM hostname 组：0

## 关键项验证

- [Rule]: 存在
- [Script]: 存在
- [MITM]: 存在
- spotify-json: 存在
- spotify-proto: 存在
- youtube.response: 存在

## 手动测试建议

1. Shadowrocket 更新模块。
2. 更新脚本。
3. 测试 Spotify 播放、专辑页、歌手页。
4. 测试 YouTube 首页、搜索、播放、Shorts。
5. 测试淘宝、京东、微信、支付宝、银行类 App 登录和支付页。
