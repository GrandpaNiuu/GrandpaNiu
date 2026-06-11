# 脚本去重与 app-cleaner active 迁移报告

生成时间：2026-06-12 07:58:45 +0800

## 本次迁移

- 迁移范围：Batch 1-6 低风险 JSON / 字段清理融合
- 新承接入口：`Scripts/app-cleaner-active.conf` / `app-cleaner-active-json-clean`
- 新承接脚本：`Scripts/app-cleaner.js`
- 计划替换旧入口数量：71
- Scripts/app-clean.conf 本次移除旧入口数量：0
- 所有源文件合计本次移除旧入口数量：0
- 新增 active 入口数量：1
- 说明：这是大批量融合，但保留高风险和复杂脚本独立运行。

## 移除的旧入口

### `Scripts/app-clean.conf`

- 无，目标旧入口已不存在。

### `Rewrite/Sources/Script.conf`

- 无，目标旧入口已不存在。

## 不变范围

- 不动 Spotify。
- 不动 YouTube。
- 不动知乎增强与知乎 R-Store 条目。
- 不动 Tieba JSON / proto。
- 不动微博、Keep、Soul、Cotti、RRTV、网易云音乐、12306、航旅纵横、搜狗输入法、韵达等复杂或高风险条目。
- 不动登录、支付、验证码、银行相关条目。
- 不合并复杂加密、持久化配置、会员权益、binary-body 脚本。
