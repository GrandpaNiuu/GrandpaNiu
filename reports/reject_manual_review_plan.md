# REJECT 人工复核计划

生成目的：把 `reports/reject_risk_report.md` 与 `reports/domestic_app_connectivity_audit.md` 中的高风险 REJECT 项转成可执行复核清单。本报告只做计划，不自动删除、不批量注释、不批量加 DIRECT。

## 处理原则

- 不直接大面积删除 REJECT。
- 涉及图片、登录、支付、验证码、银行、微信、支付宝、HTTPDNS、核心 API 的规则默认 manual-review。
- 修复必须 source-first，优先改 `Rules/` 源头，再构建 Release 和 Root。
- 必须结合 Shadowrocket 命中日志和真实 App 行为，不用关键词猜测。

## 分类复核清单

| 分类 | 规则 / 范围 | 当前风险 | 建议动作 | 是否需要日志确认 | 是否允许自动修复 |
|---|---|---|---|---|---|
| 图片/CDN | `pddpic.com` 相关 REJECT | 可能影响拼多多图片、商品图、活动图加载 | 等待日志；必要时单条 DIRECT 或移出 Stable | 是 | 否 |
| 图片/CDN | `alicdn.com` 相关 REJECT | 可能影响淘宝、天猫、阿里系图片和活动资源 | 等待日志；只允许单条验证 | 是 | 否 |
| 图片/CDN | `meituan.net` / `d.meituan.net` / `lx.meituan.net` | 可能影响美团、大众点评页面资源 | 等待日志；优先确认是否广告或核心资源 | 是 | 否 |
| HTTPDNS | `httpdns*`、`*httpdns*` | 可能影响国内 App 解析、加载、降级策略 | 默认 manual-review，不建议 pre-matching REJECT | 是 | 否 |
| 微信 / 支付 / 银行 | 银行、支付、微信媒体相关命中 | 可能影响支付前置页、登录、验证码、发图收图 | 默认保护；需要真实测试和日志 | 是 | 否 |
| 国内核心 API | `biliapi`、`meituan`、`amap`、`dianping` 等核心 API | 可能影响首页、搜索、订单前置、地图加载 | 单条复核；必要时移到 Stable Plus 或 Full | 是 | 否 |
| 不确定规则 | `reports/reject_risk_report.md` 中 pending / manual-review 项 | 无法静态判断是否误杀 | 保持 manual-review；按 App 逐项测试 | 是 | 否 |
| 明确广告域 | `ad*`、`ads*`、`adx*`、统计广告域 | 误杀风险较低 | 可保留 REJECT，但仍保留回滚路径 | 否 | 是，限单条 |

## 执行动作定义

| 动作 | 使用条件 |
|---|---|
| 保留 | 明确广告域，且无真实误杀反馈。 |
| 加 DIRECT | 明确影响图片、支付、登录、验证码、核心 API。 |
| 移到 Stable Plus | 需要测试，但不适合直接进入 Stable。 |
| 移到 Full | 只用于排查或覆盖风险过大。 |
| manual-review | 无法确认真实影响。 |
| 等待日志 | 必须依赖 Shadowrocket 命中日志确认。 |

## 复核顺序

1. 先复核用户已反馈异常相关域名。
2. 再复核图片/CDN 和微信媒体链路。
3. 再复核支付、银行、验证码相关命中。
4. 再复核 HTTPDNS。
5. 最后处理不确定规则。

## 禁止事项

- 不要一次性删除大量 REJECT。
- 不要因为域名里有 `ad` 就直接保留或删除。
- 不要把国内核心 API 直接 REJECT 后发布 Stable。
- 不要把未验证项写成已通过。

## 回滚要求

任何 REJECT 调整后必须说明：

- 改了哪条源头规则。
- 是否影响 Stable。
- 是否需要同步 Release 和 Root。
- 需要用户复测哪些 App 和流程。
