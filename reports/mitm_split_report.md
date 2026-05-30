# MITM 分层报告

生成时间：2026-05-31 04:55:22 +0800

- 原 MITM hostname 总数：1009
- core 数量：11
- app-clean 数量：109
- extended 数量：889
- 未分类数量：0（未命中 core/app-clean 的 hostname 已进入 extended）
- 是否存在重复 hostname：否
- 疑似包含支付 / 登录 / 验证码 / 银行相关 hostname：是
- stable 使用哪些 MITM 文件：建议 MITM-core.conf + MITM-app-clean.conf，切换前必须人工确认
- lite 使用哪些 MITM 文件：建议 MITM-core.conf，切换前必须人工确认
- full 使用哪些 MITM 文件：建议 MITM-core.conf + MITM-app-clean.conf + MITM-extended.conf

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
- 切换 profile 使用分层 MITM 前，必须测试 Spotify、YouTube、知乎、登录、支付和验证码。
- 如果发现敏感 hostname，应优先移出 stable，必要时进入 extended 或删除。
