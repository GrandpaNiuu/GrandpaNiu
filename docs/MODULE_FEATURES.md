# Fusion 模块功能与覆盖说明

本文件说明当前唯一公开 iOS 入口 `Ronghemokuai.sgmodule` 的能力边界。仓库已经切换为单一 Fusion 融合模块，不再让用户选择 Stable / Stable Plus / Lite / Full。

## 入口

| 项目 | 当前状态 |
|---|---|
| 公开模块 | `Ronghemokuai.sgmodule` |
| Release 模块 | `Release/Ronghemokuai.sgmodule` |
| 构建 profile | `Rewrite/Profiles/fusion.conf` |
| 导入地址 | `https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule` |
| 旧四版本文件 | 只作为历史兼容，不作为正式入口 |

## 功能层

| 层级 | 来源 | 作用 |
|---|---|---|
| `[Rule]` | `Rules/`、`Rewrite/Remotes/sources.json` | DIRECT 白名单、REJECT 本地规则、远程广告规则源 |
| `[URL Rewrite]` | `Rewrite/Sources/*URL-Rewrite*.conf` | 拦截广告接口、活动接口、弹窗接口和部分跟踪请求 |
| `[Header Rewrite]` | `Rewrite/Sources/Header-Rewrite.conf` | 处理少量明确需要 header 调整的接口，例如 Spotify 相关缓存头 |
| `[Body Rewrite]` | `Rewrite/Sources/*Body-Rewrite*.conf` | 清理 JSON 响应里的广告、推荐、活动卡片字段 |
| `[Map Local]` | `Rewrite/Sources/*Map-Local*.conf` | 对局部广告接口返回空响应或本地响应 |
| `[Script]` | `Scripts/*.conf`、`Scripts/app-cleaner.js` | Spotify、YouTube、知乎和通用 App JSON 清理 |
| `[MITM]` | `Rewrite/Sources/MITM-*.conf` | 给 Rewrite / Script 提供必要 hostname 覆盖 |

## 重点覆盖

| App / 服务 | 覆盖方式 | 当前定位 |
|---|---|---|
| Spotify | DIRECT、Header Rewrite、`spotify-json`、`spotify-proto`、MITM | 重点专项，保留播放和账号安全边界 |
| YouTube | DIRECT、`youtube.response`、Map Local、MITM | 重点专项，偏向广告与响应清理 |
| 知乎 | `zhihu-enhance`、Body Rewrite、URL Rewrite、MITM | 重点专项，清理信息流、回答页和商业字段 |
| Bilibili | Rule、URL Rewrite、Body Rewrite、Map Local、MITM | 局部净化，不做会员、登录、支付绕过 |
| QQ 新闻 / 腾讯新闻 | app2smile 单项脚本与规则 | Fusion 内保守启用，需继续人工复测 |
| 微信广告相关 | 窄范围广告域规则 | 仅保留广告域，禁止覆盖图片、小程序、支付、登录核心域 |
| 美团 / 点评 / 电商 / 地图 | Rule、Rewrite、Map Local、部分 MITM | 只处理明确广告、弹窗、活动入口；核心交易链路保持保守 |

## Android 关系

Android 输出不是 `.sgmodule`，而是从规则源迁移出的多格式规则：

| 格式 | 路径 | 作用 |
|---|---|---|
| Mihomo / Clash Meta | `Android/mihomo/` | 配置或 rule-provider 规则 |
| sing-box | `Android/sing-box/` | rule-set JSON |
| AdGuard | `Android/adguard/` | DNS / AdGuard Home 过滤规则 |
| v2rayNG / V2Ray / Xray | `Android/v2rayng/` | routing 片段 |

Android 只能承接域名、IP、关键字和部分 routing 逻辑，不包含 iOS 的 Script、MITM、Header Rewrite、Body Rewrite 能力。

## 风险边界

以下内容不得自动引入 Fusion：

- 会员破解、付费内容绕过、登录绕过。
- Cookie / Token / Authorization 改写。
- 银行、支付、验证码、证书校验、账号安全接口。
- 未知 request-body、protobuf、binary-body 或加密 body 脚本。
- 无来源、短链、代理镜像、混淆脚本。

以下内容只能保守处理并保留回滚路径：

- 微信媒体、小程序、支付和登录周边。
- Bilibili、美团、点评、淘宝、拼多多等核心 API。
- 图片/CDN、地图定位、订单前置页。
- HTTPDNS 相关域名。

## 维护方式

Fusion 采用 source-first 维护：

```text
Rules/
Scripts/
Rewrite/Sources/
Rewrite/Remotes/
Rewrite/Profiles/fusion.conf
        -> scripts/build_module.py --build --profile fusion
        -> scripts/factory_finalize.py --sync-root
        -> scripts/build_release_variants.py
        -> Ronghemokuai.sgmodule + Release/Ronghemokuai.sgmodule
```

正常维护时先修改源头文件，再重新构建最终模块。不要只手工改 `Ronghemokuai.sgmodule`。

## 验证标准

每次修改后至少运行：

```bash
python3 scripts/build_module.py --build --profile fusion
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_module_integrity.py
python3 scripts/validate_remote_rule_syntax.py
python3 scripts/validate_repository.py
```

其中 `validate_module_integrity.py` 会检查：

- Root / Release 是否一致。
- 是否存在重复 section。
- 是否存在重复 active rule / rewrite / script / MITM line。
- 是否存在重复 script name。
- 是否存在重复 MITM hostname。
- 同一规则文件内部是否存在重复 active entry。
- 远程规则源 URL 是否重复。

## 说明

覆盖存在不等于真机完整通过。没有 `reports/automated_quality_evidence.md` 或 Issue 反馈记录时，只能写“已纳入覆盖”或“待复测”，不能写“已验证通过”。
