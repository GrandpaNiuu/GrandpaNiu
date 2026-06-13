# GrandpaNiu 长期维护路线图

本仓库的目标不是无限堆规则，而是做一个可长期运行、可回滚、可测试、可解释的 Surge 模块工厂。

## 总体方向

1. 默认发布只追求稳定，不追求最大覆盖。
2. 增强覆盖必须先进 `stable-plus`，通过自动化验证后才允许进入 `stable`。
3. 全量覆盖只留在 `full`，用于排查和临时测试，不作为默认发布。
4. 所有规则、脚本和 MITM 变更必须能追踪来源、能回滚、能解释风险。
5. 不做会员、付费、支付、登录、证书、安全绕过类能力。

## Profile 分层路线

| Profile | 定位 | 发布策略 |
|---|---|---|
| `lite` | 低耗电、低 MITM 参考版 | 不默认发布 |
| `stable` | 默认正式版，优先稳定 | 默认发布 |
| `stable-plus` | 常用 App 增强测试版 | 自动化验证后按需使用 |
| `full` | 全量测试版 | 只用于排查，不发布 |

## P0：稳定性优先

必须长期保持：

- Root 与 Release 一致。
- `validate_repository.py` 通过。
- `Module Factory Build` 成功。
- `Daily invalid source audit and repair` 成功。
- `Repository Health Check` 成功。
- stable 不默认使用 `MITM-extended.conf`。
- 新脚本默认 pending，不直接进 stable。

## P1：覆盖增强

增强覆盖只允许按以下路径推进：

```text
MITM-extended.conf
-> MITM-stable-plus.conf
-> 自动化验证
-> MITM-app-clean.conf 或 stable 保留
```

不得直接从 extended 大批量合并到 stable。

优先测试和增强这些常用类别：

- 视频：爱奇艺、芒果 TV、咪咕视频、AcFun、虎牙、快手。
- 电商：得物、唯品会、当当、转转、什么值得买。
- 出行：携程、去哪儿、途家、途牛、航旅纵横、飞常准。
- 内容：豆瓣、LOFTER、虎嗅、澎湃、华尔街见闻。
- 职场：猎聘、BOSS、51job。
- 工具：WPS、有道、阿里云盘、天翼云盘、迅雷。

## P2：安全边界

以下内容不能进入 stable：

- 银行、证券交易、支付、借贷、保险核心交易域名。
- 登录、验证码、passport、token、cookie、security 相关域名。
- 会员、Premium、VIP、unlock、crack、paywall 相关脚本。
- 第三方 ZIP、图片注入、证书绕过、安全策略绕过。

发现疑似敏感 hostname 时，优先保留在 `MITM-extended.conf` 或删除，不进入 `stable`。

## P3：测试治理

每次大改至少测试：

- Spotify：播放、切歌、搜索、歌单。
- YouTube：首页、搜索、播放、Shorts、评论。
- 知乎：首页、回答页、搜索、评论、点赞、收藏。
- Bilibili：首页、搜索、播放、评论。
- 淘宝 / 京东 / 拼多多：首页、搜索、详情页、购物车、订单。
- 微信 / 支付宝 / 银行 App：登录、验证码、支付前置流程、消息推送。

没有真实测试，不允许在 `automated_quality_evidence.md` 中写“通过”。

## P4：自动化治理

长期应继续增强：

- Workflow 报告应优先显示最新 completed 状态，避免把 running 当最终结论。
- 失效源连续失败 2 天后才处理，避免误判单日网络问题。
- 每次 Release 应记录 commit、日期、MITM 数量、脚本数量和 Root/Release diff。
- 重要变更要有回滚说明。

## 不做的方向

- 不追求全网自动搜索规则。
- 不追求每天自动替换核心脚本。
- 不追求最大 MITM 覆盖。
- 不把 full 作为默认发布。
- 不牺牲登录、支付、验证码稳定性换广告覆盖。
