# GrandpaNiu 长期维护路线图

本仓库目标不是无限堆规则，而是做一个可长期运行、可回滚、可测试、可解释的 Fusion 模块工厂。

## 总体方向

1. 公开 iOS 入口只维护 Fusion 单一融合模块。
2. 不再以 Stable / Stable Plus / Lite / Full 作为公开版本路线。
3. 所有规则、脚本、MITM 和上游同步都必须能追踪来源、能回滚、能解释风险。
4. 不加入会员、付费、支付、登录、证书、安全绕过类能力。
5. 登录、支付、银行、验证码、视频播放、图片/CDN 链路优先保护。

## 当前发布模型

| 层级 | 定位 | 发布策略 |
|---|---|---|
| Fusion | 唯一公开 iOS 主模块 | 默认公开 |
| App Modules | App 独立诊断和便利用模块 | catalog 辅助入口，不是新版本线 |
| Android | Mihomo / sing-box / AdGuard / v2rayNG 输出 | 从安全可迁移规则生成 |
| Windows v2rayN | v2rayN routing JSON | 从 Android v2rayNG 路由生成 |
| Legacy variants | 旧四版本占位/参考 | deprecated / legacy reference |

## P0：稳定性优先

必须长期保持：

- 根目录 `Ronghemokuai.sgmodule` 与 `Release/Ronghemokuai.sgmodule` 内容一致。
- `Release/Module.sgmodule` 是 `Release/Ronghemokuai.sgmodule` 的兼容别名。
- `validate_repository.py` 通过。
- `Module Factory Build` 成功。
- `Repository Health Check` 成功。
- `Upstream app module sync` 受风险门禁约束。
- 新脚本和聚合脚本通过 sandbox / syntax 检查。

## P1：覆盖增强

增强覆盖只能按 source-first 小步推进：

```text
Rewrite/Sources/Apps/
Rewrite/Sources/Misc/
Rules/
Scripts/
Rewrite/Remotes/
        -> risk gate / sandbox / validation
        -> Fusion
```

不要通过恢复多公开版本路线来承载不稳定规则。

优先关注：

- 视频：爱奇艺、芒果 TV、哔哩哔哩、AcFun、虎牙、快手。
- 电商：淘宝、京东、拼多多、得物、唯品会、转转、什么值得买。
- 出行：高德、百度地图、携程、去哪儿、途牛、航旅纵横、飞常准。
- 内容：小红书、微博、知乎、豆瓣、LOFTER、虎扑。
- 工具：WPS、有道、阿里云盘、百度网盘、迅雷。

## P2：安全边界

以下内容不应进入自动直提或默认净化：

- 银行、证券交易、支付、借贷、保险核心交易域名。
- 登录、验证码、passport、token、cookie、security 相关域名。
- 会员、Premium、VIP、unlock、crack、paywall 相关脚本。
- 第三方 ZIP、证书绕过、安全策略绕过。

发现敏感 hostname 时，优先标记 manual-review，不做批量 REJECT。

## P3：测试治理

每次大改至少人工验证：

- Spotify：播放、切歌、搜索、歌单。
- YouTube：首页、搜索、播放、Shorts、评论。
- 知乎：首页、回答页、搜索、评论、点赞、收藏。
- Bilibili：首页、搜索、播放、评论。
- 淘宝 / 京东 / 拼多多：首页、搜索、详情页、购物车、订单。
- 微信 / 支付宝 / 银行 App：登录、验证码、支付前置流程、消息推送。

没有真实测试记录时，不允许在自动化证据中写“通过”。

## P4：自动化治理

长期增强方向：

- Workflow 报告优先显示最新 completed 状态，避免把 running 当最终结论。
- 失效源连续失败后再处理，避免误判单日网络问题。
- 每次 Release 记录 commit、日期、MITM 数量、脚本数量和 Root/Release diff。
- 重要变更保留回滚说明。
- `git add` 使用明确路径，不使用宽泛 `git add -A`。
- workflow 构建入口逐步统一到 `Rewrite/Generator/Builder.py --profile fusion --release`。

## 不做的方向

- 不追求全网自动替换核心脚本。
- 不追求最大 MITM 覆盖。
- 不把 legacy full/lite/stable/stable-plus 当公开路线。
- 不牺牲登录、支付、验证码、视频播放、图片/CDN 稳定性换广告覆盖。
