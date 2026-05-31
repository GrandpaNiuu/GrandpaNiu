# 误杀预防标准

本文件定义 GrandpaNiu 仓库的少误杀策略。目标是让 Stable 保守、可追责、可回滚，而不是追求最大拦截覆盖。

## 基本原则

1. Stable 只接收低误杀、可长期使用、可回滚的规则。
2. Stable Plus 用于增强测试，不整体合并进 Stable。
3. Lite 是故障对照组，用于判断异常是否由规则、脚本或 MITM 引起。
4. Full 只用于全量排查，不长期启用。
5. 不确定项先 pending 或 manual-review，不靠关键词硬判。

## 默认不能 REJECT 的域名类型

以下类型默认不能进入 Stable REJECT：

| 类型 | 示例范围 | 原因 | 默认动作 |
|---|---|---|---|
| 登录 / 账号 | passport、account、login、auth、security | 可能导致登录失败或账号状态异常 | DIRECT / manual-review |
| 支付 | pay、payment、wechatpay、alipay、cashier、wallet | 可能导致支付前置页失败 | DIRECT / manual-review |
| 验证码 | captcha、verify、sms、risk、sec | 可能导致短信、滑块、图形验证码异常 | DIRECT / manual-review |
| 银行 | bank、icbc、ccb、cmb、boc、psbc 等 | 高敏感链路 | DIRECT / manual-review |
| 微信媒体 / 小程序 | qpic、gtimg、qlogo、servicewechat、wxapp | 可能影响发图、收图、头像、小程序资源 | DIRECT / manual-review |
| 图片 / CDN | img、image、pic、cdn、alicdn、pddpic、jdimg、biliimg | 广告和核心图片经常共用域名 | DIRECT / manual-review |
| HTTPDNS | httpdns、dns、resolver | 可能影响 App 首屏加载和网络降级 | manual-review |
| 国内核心 API | biliapi、meituan、dianping、amap 等 | 可能影响首页、搜索、订单前置、地图等核心功能 | manual-review |
| Cookie / Token | cookie、token、session、credential | 可能影响账号安全或状态 | 禁止改写 / manual-review |
| 会员权益 | vip、premium、membership、paywall | 可能触碰权益绕过 | 禁止 |

## 可以进入 Stable 的规则

规则进入 Stable 必须满足以下条件：

1. 来源明确。
2. 风险分类明确。
3. 不涉及登录、支付、验证码、银行、Cookie、Token、会员权益。
4. 不影响图片 CDN、核心 API、HTTPDNS。
5. 已在 Stable Plus 或本地真实测试确认。
6. 有 rollback_path。
7. `validate_repository.py` 通过。
8. `repository_health_check.py` 阻断问题为 0。

典型可进入 Stable 的类型：

| 类型 | 条件 |
|---|---|
| 明确广告域 | 域名语义明确，且不承载核心资源 |
| 明确统计 / 埋点 | 不影响核心页面、登录、支付、验证码 |
| 单 App 明确开屏广告接口 | 已测试首页、详情页、登录状态正常 |
| 已验证低风险 JSON cleaner | 不改 request body、不碰 Cookie/Token、不碰会员权益 |

## 只能进入 Stable Plus 的规则

以下内容不得直接进 Stable，只能先进入 Stable Plus 或 pending：

- 新 App 的广告规则。
- 未经过真实测试的广告接口。
- 可能影响首页、图片、评论、搜索、订单前置的规则。
- 涉及小程序、媒体资源、地图、云盘、设备联动的规则。
- 需要扩大 MITM 的规则。
- 任何需要观察广告减少效果的规则。

Stable Plus 晋级 Stable 只能单项进行，不允许整体合并。

## 必须 pending 的内容

以下内容必须 pending，不得进入 Stable 或 Stable Plus：

- 未知作者脚本。
- 混淆脚本。
- 会改 request body 的脚本。
- 访问或写入 Cookie / Token / 账号状态的脚本。
- 会员权益、破解、绕过、支付、登录、验证码相关脚本。
- 无法解释用途的远程模块。
- 依赖短链、镜像、ghproxy、未知代理源的内容。

## 使用 Lite 做对照排查

Lite 是故障排查对照组，不是主力去广告版本。

排查流程：

```text
Stable 出现异常
-> 切换 Lite
-> Lite 正常：问题大概率来自 Stable 的规则 / 脚本 / MITM
-> Lite 也异常：问题可能不是模块导致，继续检查网络、App、系统或上游服务
```

常见判断：

| 现象 | Lite 正常时的判断 | 优先排查 |
|---|---|---|
| 图片不显示 | Stable 可能误杀 CDN | `Rules/reject.list`、`Rules/direct.list` |
| 登录失败 | Stable 可能影响账号链路 | MITM、REJECT、脚本入口 |
| 支付前置页失败 | Stable 可能影响支付资源 | DIRECT 保护、支付域名、MITM |
| 验证码失败 | Stable 可能影响风险控制接口 | 验证码 / risk / security 域名 |
| 首页白屏 | 核心 API 或 HTTPDNS 可能被影响 | HTTPDNS、API、Body Rewrite |

## 回滚要求

每个高风险变更必须写明：

```text
修改文件：
影响版本：
影响 App / 服务：
风险分类：
测试状态：
回滚文件：
重建命令：
复测范围：
```

最小回滚动作：

```bash
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

## PR 粒度

一个 PR 只能处理一个风险单元：

- 一个 App；或
- 一类 CDN；或
- 一组 HTTPDNS；或
- 一个低风险脚本融合项；或
- 一批同源、同风险等级的广告域。

禁止在一个 PR 里同时修改规则、MITM、脚本、文档和发布产物，除非这些产物是同一风险单元的必要重建结果。
