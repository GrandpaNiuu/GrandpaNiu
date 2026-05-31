# 规则可追责矩阵

本矩阵用于把高风险 REJECT 项转成可追责、可复核、可回滚的资产。本文件只记录治理信息，不新增规则、不删除规则、不扩大 MITM、不启用脚本。

## 字段说明

| 字段 | 含义 |
|---|---|
| rule | 规则或风险范围。无法定位到单条规则时使用域名 / 关键词范围。 |
| app/service | 可能受影响的 App 或服务。 |
| category | 风险分类：图片/CDN、HTTPDNS、微信/支付/银行、国内核心 API、不确定 REJECT。 |
| source | 依据来源：审计报告、用户反馈、Shadowrocket 日志、上游规则、人工确认。 |
| risk_level | low / medium / high / critical。 |
| current_profile | 当前所在范围或影响范围。 |
| recommendation | 建议动作。 |
| test_status | 测试状态。没有真实测试不得写通过。 |
| rollback_path | 出问题时的回滚路径。 |

## 高风险优先矩阵

| rule | app/service | category | source | risk_level | current_profile | recommendation | test_status | rollback_path |
|---|---|---|---|---|---|---|---|---|
| `alicdn.com` related REJECT hits | 淘宝 / 天猫 / 阿里系图片与活动资源 | 图片/CDN | `reports/reject_risk_report.md` / `reports/domestic_app_connectivity_audit.md` | high | Stable risk surface | 等待日志；确认核心图片资源后单条 DIRECT 或移出 Stable | 未测；不得写通过 | 回滚 `Rules/reject.list` 中对应 REJECT；必要时补 `Rules/direct.list`；重建 stable / Release / Root |
| `pddpic.com` related REJECT hits | 拼多多商品图 / 活动图 / 店铺图 | 图片/CDN | `reports/reject_risk_report.md` / 用户历史反馈 | high | Stable risk surface | 优先复核；商品图异常时保护图片 CDN，不做批量 REJECT | Stable 第一轮用户确认正常；后续大改需复测 | 回滚对应 REJECT；重建 stable；复测拼多多首页、搜索、商品图、订单前置 |
| `meituan.net` / `d.meituan.net` / `lx.meituan.net` | 美团 / 大众点评页面资源、埋点、活动卡片 | 图片/CDN / 国内核心 API | `reports/reject_risk_report.md` | high | Stable risk surface | 区分广告、埋点、核心资源；不确定项保持 manual-review | Stable 第一轮用户确认正常；单条仍未测 | 回滚对应 REJECT；复测美团首页、商详、下单前置、图片加载 |
| `httpdns*` / `*httpdns*` | 多数国内 App 网络解析链路 | HTTPDNS | `reports/reject_risk_report.md` | critical | Stable risk surface | 不建议 pre-matching REJECT；优先 manual-review 或保护 | 未测；必须依赖日志确认 | 回滚 HTTPDNS 相关 REJECT；必要时加 DIRECT；复测首页加载、登录、图片、支付前置 |
| `qpic.cn` / `gtimg.cn` / `qlogo.cn` | 微信头像、聊天图片、公众号、小程序资源 | 微信媒体资源 | `reports/reject_risk_report.md` | critical | Protected / DIRECT expected | 保持默认保护；不得 REJECT | Stable 第一轮用户确认微信图片正常；后续改动需复测 | 若误伤，回滚相关 REJECT 并恢复 DIRECT；复测发图、收图、朋友圈、公众号、小程序 |
| `wxs.qq.com` / `wx.qq.com` / `weixin.qq.com` | 微信登录、网页、服务资源 | 微信核心服务 | `reports/reject_risk_report.md` | critical | Protected / DIRECT expected | 默认保护；不得直接 REJECT | Stable 第一轮用户确认正常；Stable Plus 微信广告仍未测 | 回滚相关 REJECT/MITM；复测登录、发图、收图、小程序、支付前置 |
| `wechatpay.cn` | 微信支付前置链路 | 支付 | `reports/reject_risk_report.md` | critical | Protected / DIRECT expected | 默认保护；不得 REJECT | Stable 第一轮用户确认支付相关正常；单项仍需复测 | 回滚任何支付相关拦截；复测支付前置页，不测试真实扣款 |
| 银行 / 验证码相关命中 | 银行 App、短信/滑块/图形验证码 | 银行 / 验证码 | `reports/reject_risk_report.md` / `manual_test_log.md` | critical | Stable risk surface | 不进入 REJECT；只允许保护确认 | Stable 第一轮用户确认正常；后续大改需复测 | 回滚相关 REJECT/MITM；切 Lite 对照；复测验证码和登录 |
| `biliapi` related risk | Bilibili 首页、播放、评论、账号接口 | 国内核心 API | `reports/reject_risk_report.md` | high | Stable risk surface | 区分广告接口和核心 API；不确定项移到 Stable Plus 或 pending | Stable 第一轮用户确认正常；具体规则未逐条测 | 回滚对应 REJECT；复测首页、播放页、评论、登录状态 |
| `amap` related risk | 高德地图搜索、地图瓦片、定位、路线 | 国内核心 API | `reports/reject_risk_report.md` | high | Stable risk surface | 地图核心链路默认保护；广告接口需日志确认 | 未测；需真实 App 使用确认 | 回滚对应 REJECT；切 Lite 对照；复测搜索、定位、路线规划 |
| `dianping` related risk | 大众点评首页、商详、图片、下单前置 | 国内核心 API | `reports/reject_risk_report.md` | high | Stable risk surface | 不确定项 manual-review；不批量 REJECT | Stable 第一轮用户确认正常；具体规则未逐条测 | 回滚对应 REJECT；复测首页、商详、图片、优惠/订单前置 |
| `meituan` core API risk | 美团首页、商详、图片、下单前置 | 国内核心 API | `reports/reject_risk_report.md` | high | Stable risk surface | 只保留明确广告域；核心 API 保护 | Stable 第一轮用户确认正常；具体规则未逐条测 | 回滚对应 REJECT；复测首页、商详、下单前置 |
| `alicdn.com` exact image hosts | 淘宝 / 天猫 / 闲鱼图片资源 | 图片/CDN | `reports/reject_manual_review_plan.md` | high | Stable risk surface | 第一批优先复核；日志确认后再动 | 未测 | 回滚对应 REJECT；复测商品图、搜索图、店铺图 |
| `pddpic.com` exact image hosts | 拼多多商品图片 | 图片/CDN | `reports/reject_manual_review_plan.md` | high | Stable risk surface | 第一批优先复核；异常优先保护 | Stable 第一轮正常；需单条确认 | 回滚对应 REJECT；复测商品图和活动页 |
| `meituan.net` exact hosts | 美团 / 大众点评资源 | 图片/CDN / API | `reports/reject_manual_review_plan.md` | high | Stable risk surface | 第一批优先复核；不要批量改 | Stable 第一轮正常；需单条确认 | 回滚对应 REJECT；复测图片、首页、商详 |
| `httpdns` wildcard-like entries | 国内 App 网络解析 | HTTPDNS | `reports/reject_manual_review_plan.md` | critical | Stable risk surface | 第一批优先复核；不建议 REJECT | 未测 | 回滚 HTTPDNS REJECT；复测多 App 首屏加载 |
| 微信广告规则 | 微信广告减少测试 | 微信 / Stable Plus | `reports/stable_plus_manual_test_plan.md` | critical | Stable Plus only | 保持 Stable Plus；单项测试通过前不得晋级 Stable | 未测试；不得写通过 | 从 Stable Plus 移除对应规则；复测发图、收图、朋友圈、公众号、小程序、支付前置 |
| unknown REJECT group A | 不确定 REJECT | 不确定 REJECT | `reports/reject_risk_report.md` | medium | Stable risk surface | 先分类，不直接删除；无法确认则 pending | 未测 | 单条回滚对应 REJECT；重建 stable；观察命中日志 |
| unknown REJECT group B | 不确定 REJECT | 不确定 REJECT | `reports/reject_risk_report.md` | medium | Stable risk surface | 按 App 和域名语义分组；优先保守 | 未测 | 单条回滚对应 REJECT；切 Lite 对照 |
| unknown REJECT group C | 不确定 REJECT | 不确定 REJECT | `reports/reject_risk_report.md` | medium | Stable risk surface | 不进入新增 Stable；后续分批复核 | 未测 | 单条回滚对应 REJECT；记录到 manual_test_log 或复核计划 |

## 使用规则

1. 新增或调整高风险规则前，必须先更新本矩阵。
2. `test_status` 没有真实证据时只能写“未测”或“manual-review”。
3. `rollback_path` 必须能指出具体文件和重建动作。
4. 单个 PR 只能处理一个风险单元，例如一个 App、一类 CDN 或一组 HTTPDNS。
5. 任何涉及支付、登录、验证码、银行、微信媒体、小程序的项默认 critical。
