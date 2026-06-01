# MITM 分层报告

生成时间：2026-06-02 06:09:34 +0800

- 原 MITM hostname 总数：1009
- core 数量：11
- app-clean 数量：109
- extended 数量：889
- 未分类数量：0（未命中 core/app-clean 的 hostname 已进入 extended）
- 是否存在重复 hostname：否
- 疑似包含支付 / 登录 / 验证码 / 银行相关 hostname：是
- stable 使用哪些 MITM 文件：MITM-core.conf + MITM-app-clean.conf
- lite 使用哪些 MITM 文件：MITM-core.conf
- full 使用哪些 MITM 文件：MITM-core.conf + MITM-app-clean.conf + MITM-extended.conf
- 回滚路径：保留 Rewrite/Sources/MITM.conf 原始完整列表；如 stable 出现漏拦截，可临时移除 profile 的 [mitm] 分层配置回到 legacy MITM.conf。

## 分层文件

- `Rewrite/Sources/MITM-core.conf`
- `Rewrite/Sources/MITM-app-clean.conf`
- `Rewrite/Sources/MITM-extended.conf`

## 疑似敏感 hostname（前 100 条）

- `abcapi.lenovoimage.com`
- `wechat.tf.cn`

## 风险说明

- 本脚本只做分层，不删除 hostname。
- 分层结果是关键词分类，不等于人工安全确认。
- 切换 profile 使用分层 MITM 后，必须测试 Spotify、YouTube、知乎、登录、支付和验证码。
- 疑似敏感 hostname 不应默认进入 stable；必要时保留在 extended 或删除。
