# GitHub 同类模块仓库借鉴报告

- 生成时间：2026-07-03 08:00 +0800
- 检索范围：GitHub 上公开的 Surge / Shadowrocket / Quantumult X / Loon / Clash / sing-box 规则、模块、脚本转换与广告净化仓库
- 使用边界：本报告只总结维护方法和可借鉴工程能力，不直接引入规则，不导入 VIP、会员解锁、支付绕过、登录绕过、凭证/Token 改写类内容。

## 结论

GrandpaNiu 当前已经具备同类仓库里比较少见的完整工厂化能力：Fusion 单入口、App 源拆分、自动上游同步、脚本聚合、Android/Windows 投影、质量门禁、自动化报告和 AI 维护记录。

还值得继续学习的是：

- 更清晰的上游信任分层和来源许可证台账。
- 更清晰的 App / 客户端兼容矩阵。
- 更强的误伤反馈闭环和白名单治理。
- 更强的跨格式转换测试夹具。
- 更清晰的高风险 MITM / REJECT 风险展示。

其中“报告编码巡检”和“MITM/REJECT 风险台账”已在本次实现。

## 可借鉴仓库

| 仓库 / 作者 | 类型 | 值得学习 | GrandpaNiu 当前状态 | 建议加入方式 |
|---|---|---|---|---|
| [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | 规则生成器 / 多客户端规则 | 生成器产物带统计、来源说明、误拦截提示；Advertising README 明确说明规则由生成器自动生成并建议用放行规则修正误拦截。 | 已引用其广告类远程源；本仓库也已有 Builder 和报告体系。 | 增强每个远程源的 provenance：来源、类型、最近成功拉取时间、命中数量、风险等级。 |
| [app2smile/rules](https://github.com/app2smile/rules) | App scoped 去广告模块 | App 粒度清晰，并在 README 里写明不同客户端 MITM 能力差异和失效处理方式。 | 已有 398 个 App 源和独立 Release Modules。 | 给高风险 App 模块补“客户端兼容/需要 MITM 能力/失效处理”说明，不直接扩大 MITM。 |
| [Cats-Team/AdRules](https://github.com/Cats-Team/AdRules) | DNS / 域名广告过滤 | 专注中文区广告、跟踪、恶意、HTTPDNS、PCDN，并提供 issue / discussions 反馈入口。 | 已引用 AdRules 域名源。 | 加强 false-positive 台账：被保护、被拒绝、待观察，形成误伤闭环。 |
| [privacy-protection-tools/anti-AD](https://github.com/privacy-protection-tools/anti-AD) | 多格式广告过滤列表 | 聚合 hosts / ad filter lists / adblock lists，强调去重、失效域名剔除、黑白名单机制和多平台输出。 | 已引用 anti-AD；本仓库已有去重/失效源报告。 | 把“白名单/保护链路”报告化，不要只看 REJECT 数量。 |
| [Script-Hub-Org/Script-Hub](https://github.com/Script-Hub-Org/Script-Hub) | 重写 / 规则集转换器 | 支持 QX、Loon、Surge、Stash、Egern、LanceX、Shadowrocket，支持参数修改和跨客户端解析。 | 本仓库已有自有转换和 Builder。 | 给转换器补 fixtures：参数、Header Rewrite、Body Rewrite、Map Local、binary body、Shadowrocket 兼容语法。 |
| [Maasea/sgmodule](https://github.com/Maasea/sgmodule) | 专精 Surge 模块 | YouTube / Bilibili 等核心 App 模块写清功能、适用范围和兼容限制；YouTube/Bili 模块较专精。 | 本仓库已有 YouTube、Bilibili 加强和上游同步保护。 | 对 YouTube/Bilibili 继续采用“保护上游 + 备份 + 参数校验”，不做低质量大批量替换。 |
| [BiliUniverse/Universe](https://github.com/BiliUniverse/Universe) | Bilibili 专项生态 | 有讨论反馈入口，依赖 BoxJs 参数生态，明确多客户端支持程度。 | 本仓库 Bilibili 已是重点模块。 | 借鉴“专项模块反馈入口”和参数说明；不要自动引入解锁/灰色功能。 |
| [Repcz/Tool](https://github.com/Repcz/Tool) | 多平台规则分发 | README 展示 Surge、mihomo/Stash、Egern、sing-box 等不同引用方式，并说明 CI 自动提交变更记录。 | GrandpaNiu 已输出 iOS、Android、Windows 多平台。 | 继续强化 Web catalog：每个平台一键入口、更新时间、生成来源、注意事项。 |
| [ddgksf2013/Cuttlefish](https://github.com/ddgksf2013/ddgksf2013) | 用户入口 / 教程型配置 | README 对小白导入、配置更新时间、功能范围和 GitHub raw 加速提示比较友好。 | GrandpaNiu 有 Web/index、README、import/android 页面。 | 简化用户入口文案，减少高级术语；把“今天更新了吗/怎么导入”放在首屏。 |
| [VirgilClyne / NSRingo / BiliUniverse / DualSubs](https://github.com/VirgilClyne) | 模块生态 / 客户端兼容矩阵 | 公开说明 Loon、Surge、Stash、Egern、Quantumult X、Shadowrocket 的推荐/兼容/部分兼容状态。 | GrandpaNiu 有多端输出，但兼容说明还可以更结构化。 | 增加平台兼容矩阵：iOS Fusion、Shadowrocket、Surge、Android Mihomo/sing-box/AdGuard/v2rayNG、Windows v2rayN。 |
| [NobyDa/Script](https://github.com/NobyDa/Script) | 成熟脚本仓库 | 明确项目基于 Surge / Quantumult X 等脚本能力，并保留 GPLv3 license 信息。 | GrandpaNiu 目前引用和转换多来源脚本。 | 建立 license/provenance 台账，避免来源不清或许可证冲突。 |

## 值得加入的工程能力

### 1. 上游信任分层

建议给 `Rewrite/Remotes/app-modules.json` 和远程源报告增加稳定字段：

- `trusted`：长期使用、风险门禁通过、少误伤。
- `observe`：可同步但需保留备份、失败不阻断。
- `blocked`：包含解锁、支付绕过、登录绕过、授权/Token/Cookie 改写、系统核心服务误伤。

收益：大规模扩展时不靠记忆判断上游，自动化能解释为什么同步或跳过。

### 2. 来源许可证与作者台账

建议新增或扩展报告：

- source URL
- upstream project
- license
- direct_commit 状态
- backup 状态
- risk
- last successful sync
- last failure reason

收益：方便后续公开使用和排查来源争议。

### 3. App / 客户端兼容矩阵

建议在 Web 和 Release 报告里显示：

- Shadowrocket：是否支持脚本、二进制 body、MITM。
- Surge：是否原生适配。
- Android：是否只能规则层生效。
- Windows v2rayN：是否只支持路由层。

收益：用户不会误以为 Android/Windows 也能执行 iOS rewrite/script。

### 4. 转换器 fixtures

参考 Script-Hub 的方向，GrandpaNiu 可以给自有转换器增加固定样例：

- QX rewrite 到 Shadowrocket。
- Surge module 到 Source fragment。
- Loon plugin 到 Surge/Shadowrocket 可接受片段。
- `#!arguments`、`argument=`、`binary-body-mode=1`、`Map Local data=`、`http-response-jq`。

收益：以后新增上游时能先跑转换测试，不用靠人工盯语法。

### 5. 误伤反馈闭环

建议维护三个报告：

- `protected_traffic_ledger`：登录/支付/银行/验证码/视频/CDN 保护链路。
- `false_positive_review`：用户反馈误伤后，具体规则、来源、处理结论。
- `mitm_reject_risk_ledger`：当前已实现，只标风险不改规则。

收益：解决“广告清不掉”和“App 无网络”之间的长期拉扯。

## 不建议直接学习的部分

- 不建议导入 VIP / 会员解锁 / 付费绕过 / 登录绕过 / 票据伪造模块。
- 不建议直接照搬大而全的自用配置；很多配置混合了代理分流、解锁、签到、节点策略，不适合放进公开 Fusion 净化模块。
- 不建议把第三方转换服务当作唯一构建依赖；可以借鉴语法和测试思路，但 GrandpaNiu 应保持本地可复现 Builder。
- 不建议为了覆盖率扩大 `*.qq.com`、`*.bilibili.com`、`*.taobao.com` 这类高风险 MITM。

## 对 GrandpaNiu 的下一步建议

1. 保持当前 Fusion 单入口，不回到 Stable / Lite / Full 多版本公开路线。
2. 把 `mitm_reject_risk_ledger.md` 作为日常复核入口，先看来源和风险，再决定是否需要真实 App 日志。
3. 给上游同步记录补 license / trust tier / last sync summary。
4. 给转换器补一批固定 fixtures，尤其是参数、JQ、二进制 body、Map Local。
5. Web 首屏继续简化：用户只需要知道 iOS Fusion 一个入口，Android/Windows 是规则投影，不等于 iOS 脚本能力。
