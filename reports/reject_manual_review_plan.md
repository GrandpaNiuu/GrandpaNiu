# REJECT 人工复核计划

生成目的：把 `reports/reject_risk_report.md` 与 `reports/domestic_app_connectivity_audit.md` 中的高风险 REJECT 项转成可执行复核清单。本报告只做计划，不自动删除、不批量注释、不批量加 DIRECT。

## 处理原则

- 不直接大面积删除 REJECT。
- 涉及图片、登录、支付、验证码、银行、微信、支付宝、HTTPDNS、核心 API 的规则默认 manual-review。
- 修复必须 source-first，优先改 `Rules/` 源头，再构建 Release 和 Root。
- 必须结合 Shadowrocket 命中日志和真实 App 行为，不用关键词猜测。
- 每个 PR 只能处理一个风险单元，不能把多类高风险项混在一个提交里。

## 238 项人工复核分批

| 批次 | 范围 | 优先级 | 目标 | 处理方式 |
|---|---|---:|---|---|
| Batch 1 | 图片/CDN、HTTPDNS、微信/支付/银行、国内核心 API | P0 | 先排除核心功能误杀 | 日志确认、Lite 对照、单条回滚路径 |
| Batch 2 | 国内核心 API 剩余项 | P1 | 区分广告接口和核心接口 | 单 App 逐项复核 |
| Batch 3 | 不确定 REJECT 中高命中项 | P1 | 降低未知风险 | 按 App / 服务归类 |
| Batch 4 | 不确定 REJECT 中语义偏广告项 | P2 | 确认可保留项 | 明确广告域保留，其他 pending |
| Batch 5 | 低命中、低置信、不明来源项 | P3 | 收敛历史债务 | 无证据不进 Stable 新增范围 |

## 第一批 20 个优先复核目标

| # | 分类 | 目标 | 可能影响 | 建议动作 | 日志确认 | rollback_path |
|---:|---|---|---|---|---|---|
| 1 | 图片/CDN | `alicdn.com` 命中项 | 淘宝 / 天猫 / 闲鱼图片与活动资源 | 确认是否核心图片资源；不确定则保护或移出 Stable | 是 | 回滚 `Rules/reject.list` 对应项；必要时补 `Rules/direct.list`；重建 stable / Release / Root |
| 2 | 图片/CDN | `pddpic.com` 命中项 | 拼多多商品图、活动图、店铺图 | 优先确认商品图；异常时保护 CDN | 是 | 回滚对应 REJECT；复测拼多多首页、搜索、商品图、订单前置 |
| 3 | 图片/CDN | `meituan.net` 命中项 | 美团 / 大众点评图片与活动资源 | 区分广告和核心资源 | 是 | 回滚对应 REJECT；复测首页、商详、下单前置 |
| 4 | 图片/CDN | `d.meituan.net` 命中项 | 美团资源加载 | manual-review，不批量修改 | 是 | 回滚对应 REJECT；切 Lite 对照 |
| 5 | 图片/CDN | `lx.meituan.net` 命中项 | 美团埋点 / 资源混合风险 | 判断是否纯埋点；不确定则 pending | 是 | 回滚对应 REJECT；复测美团核心页面 |
| 6 | HTTPDNS | `httpdns*` 命中项 | 多 App 首屏加载、网络降级 | 不建议 pre-matching REJECT | 是 | 回滚 HTTPDNS REJECT；复测多 App 首页加载 |
| 7 | HTTPDNS | `*httpdns*` 命中项 | 国内 App DNS 解析 | 保持 manual-review | 是 | 回滚对应 REJECT；观察日志 |
| 8 | HTTPDNS | App-specific HTTPDNS hit group | 单 App 网络解析 | 按 App 单独测试 | 是 | 单条回滚；复测目标 App 首页、登录、图片 |
| 9 | 微信媒体 | `qpic.cn` / related protected range | 微信图片、头像、聊天图 | 保持保护，不进入 REJECT | 是 | 恢复 DIRECT；复测发图、收图、朋友圈 |
| 10 | 微信媒体 | `gtimg.cn` / related protected range | 微信 / 腾讯媒体资源 | 保持保护 | 是 | 恢复 DIRECT；复测图片、小程序、公众号 |
| 11 | 微信媒体 | `qlogo.cn` / related protected range | 头像资源 | 保持保护 | 是 | 恢复 DIRECT；复测头像、聊天列表 |
| 12 | 微信核心 | `servicewechat.com` | 小程序资源 | 不直接 REJECT | 是 | 恢复 DIRECT；复测小程序打开、图片、登录态 |
| 13 | 微信核心 | `wxapp.tc.qq.com` | 小程序和媒体资源 | manual-review | 是 | 回滚对应 REJECT；复测小程序资源 |
| 14 | 支付链路 | `wechatpay.cn` | 支付前置页 | 默认保护，不 REJECT | 是 | 恢复 DIRECT；只复测支付前置页 |
| 15 | 账号 / 支付链路 | Alipay related protected range | 登录、支付前置 | 默认保护 | 是 | 回滚对应 REJECT/MITM；复测登录、支付前置、验证码 |
| 16 | 验证链路 | bank / captcha / verify related hits | 银行、短信/滑块/图形验证码 | 不进入 REJECT | 是 | 回滚对应 REJECT/MITM；切 Lite 对照；复测验证码 |
| 17 | 国内核心 API | `biliapi` related risk | Bilibili 首页、播放、评论 | 区分广告接口和核心 API | 是 | 回滚对应 REJECT；复测首页、播放、评论、登录 |
| 18 | 国内核心 API | `amap` related risk | 地图搜索、定位、路线 | 地图核心链路默认保护 | 是 | 回滚对应 REJECT；复测搜索、定位、路线规划 |
| 19 | 国内核心 API | `dianping` related risk | 大众点评首页、商详、图片 | 不确定项 manual-review | 是 | 回滚对应 REJECT；复测首页、商详、图片、订单前置 |
| 20 | 国内核心 API | `meituan` core API risk | 美团首页、商详、下单前置 | 只保留明确广告域 | 是 | 回滚对应 REJECT；复测首页、商详、下单前置 |

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
5. 再复核国内核心 API。
6. 最后处理不确定规则。

## 禁止事项

- 不要一次性删除大量 REJECT。
- 不要因为域名里有 `ad` 就直接保留或删除。
- 不要把国内核心 API 直接 REJECT 后发布 Stable。
- 不要把未验证项写成已通过。
- 不要在同一个 PR 里同时处理多类风险单元。

## 回滚要求

任何 REJECT 调整后必须说明：

- 改了哪条源头规则。
- 是否影响 Stable。
- 是否需要同步 Release 和 Root。
- 需要用户复测哪些 App 和流程。
- 对应 `reports/rule_traceability_matrix.md` 中的 rollback_path。
