<div align="center">

# GrandpaNiu

**iOS / Android 广告净化规则与模块集合**

一句话：**按设备选一个入口导入，不要同时启用多个版本。**

[![Import](https://img.shields.io/static/v1?label=Import&message=Multi%20Version%20Page&color=0A84FF&labelColor=111827&style=for-the-badge)][import-page]
[![Stable](https://img.shields.io/static/v1?label=Stable&message=Default&color=34C759&labelColor=111827&style=for-the-badge)][stable-import]
[![Android](https://img.shields.io/static/v1?label=Android&message=Import&color=3DDC84&labelColor=111827&style=for-the-badge)][android-import]
[![Health](https://img.shields.io/static/v1?label=Health&message=Reports&color=5856D6&labelColor=111827&style=for-the-badge)][health-report]

</div>

---

## 👀 小白先看

| 你现在的情况 | 直接点这个 | 不要做什么 |
|---|---|---|
| 🍎 iPhone / iPad，用 Shadowrocket | [导入 Stable][stable-import] | 不要同时导入 Stable Plus、Lite、Full |
| 🍎 iPhone / iPad，想看全部版本 | [打开 iOS 多版本导入页][import-page] | 不懂就别选 Full |
| 🤖 Android，没有节点，只想拦广告 | [打开 Android 导入页][android-import] | 不要把 iOS `.sgmodule` 导入 Android |
| 🤖 Android，已经有节点订阅 | [打开 Android 导入页][android-import] | 不要用完整配置覆盖自己的节点 |
| 🧪 出现异常、图片不加载、登录不正常 | 换 Lite 或关闭增强包 | 不要继续叠加更多规则 |

> **最推荐：iOS 普通用户用 Stable；Android 用户先打开 Android 导入页。**

---

## 🚀 一分钟怎么用

### 🍎 iOS / Shadowrocket / Surge

1. 点：**[导入 Stable][stable-import]**。
2. 打开 Shadowrocket 后启用模块。
3. 在 Shadowrocket 里执行：**更新模块、更新脚本、更新全部资源**。
4. 出问题时先换 Lite，不要直接开 Full。

### 🤖 Android

1. 点：**[打开 Android 导入页][android-import]**。
2. 看自己有没有节点。
3. 没有节点：用完整配置版。
4. 已有节点：用 Mihomo 规则集版。
5. 想更强：再测试 iOS 可复用规则包，误伤时先关闭它。

---

## 🧭 版本怎么选

| 版本 | 一句话说明 | 适合谁 | 风险 | 导入 |
|---|---|---|---|---|
| ✅ Stable | 默认稳定版 | 大多数 iOS 用户 | 低 | [导入][stable-import] |
| 🧪 Stable Plus | 更多测试覆盖 | 想多拦一点、能接受测试风险 | 中 | [导入][stable-plus-import] |
| 🪶 Lite | 最小排查版 | 登录异常、发热、图片不加载时排查 | 低 | [导入][lite-import] |
| 🧰 Full | 全量排查版 | 查漏拦、定位 hostname | 高 | [导入][full-import] |

> **普通用户只选 Stable。不要多个版本一起开。**

---

## ✨ 这个仓库能做什么

### 🍎 iOS / Shadowrocket / Surge

- 🧹 拦截常见广告、开屏、弹窗、横幅、信息流推荐、活动卡片。
- 🔧 包含部分 App 的 Rule、Rewrite、Script、MITM hostname 覆盖。
- 🎵 已纳入 Spotify、YouTube、知乎等维护项。
- 🧩 低风险 JSON 清理类脚本由 `Scripts/app-cleaner.js` 统一承接，减少重复脚本入口。

### 🤖 Android

Android 版本是**可迁移规则导出**，不是 iOS `.sgmodule`。

支持：

- 📦 Mihomo / Clash Meta / FlClash 完整配置
- 🧩 Mihomo / Clash Meta / FlClash 规则集
- 📘 sing-box rule-set
- 🛡️ AdGuard DNS / AdGuard Home 自定义过滤规则
- 🧭 v2rayNG / V2Ray / Xray routing 片段
- 📱 App 可选增强规则：按 App 或组合包手动启用
- ⚡ iOS 可复用规则包：覆盖更强，也更容易误伤

Android 版主要通过域名、关键词和 IP 规则拦截常见广告域名、追踪域名和部分 App 广告请求。它不包含 Shadowrocket / Surge 的 Script、MITM、Rewrite、Header Rewrite、Body Rewrite 能力。

---

## 🤖 Android 怎么用

Android 用户请先进入专门导入页：

- 👉 [打开 Android 导入页][android-import]

| 场景 | 推荐版本 | 文件 | 适合客户端 | 导入方式 |
|---|---|---|---|---|
| 🟢 没有节点，只想拦广告 | 完整配置版 | [GrandpaNiu-Android-Full.yaml][android-full-raw] | FlClash / Mihomo / Clash Meta | 直接作为完整配置导入 |
| 🔵 已经有节点订阅 | Mihomo 规则集版 | [GrandpaNiu-Ads.yaml][android-mihomo-ads-raw] | FlClash / Mihomo / Clash Meta | 作为 rule-provider 合并进原配置 |
| ⚡ 想使用更强通用增强包 | iOS 可复用规则包 | [Mihomo][android-ios-compatible-mihomo-raw] / [sing-box][android-ios-compatible-singbox-raw] / [AdGuard][android-ios-compatible-adguard-raw] / [v2rayNG][android-ios-compatible-v2rayng-raw] | Mihomo / sing-box / AdGuard / v2rayNG | 作为增强包额外导入，误伤时先关闭它 |
| 📘 使用 sing-box | sing-box 规则集版 | [GrandpaNiu-Ads.json][android-singbox-raw] | sing-box / SFA | 在自己的配置中引用 rule-set |
| 🛡️ 使用 AdGuard | DNS 规则版 | [GrandpaNiu-DNS.txt][android-adguard-raw] | AdGuard Android / AdGuard DNS / AdGuard Home | 作为自定义 DNS / 过滤规则导入 |
| 🧭 使用 v2rayNG / V2Ray / Xray | routing 片段版 | [GrandpaNiu-v2rayng-routing.json][android-v2rayng-raw] | v2rayNG / V2Ray / Xray | 手动合并 routing 规则 |

> ⚠️ `iOS-Compatible-Reject` 是增强包。它比普通 App 单包覆盖更广，也更容易影响图片加载、播放、定位、部分 App 启动或登录前接口。出现异常时，先关闭这个增强包。

---

## 🧯 出问题先这样排查

| 现象 | 先做什么 |
|---|---|
| App 登录异常 | iOS 先切 Lite；Android 先关闭增强包 |
| 图片不加载 | 先关 iOS 可复用规则包 / App 增强包 |
| 视频无法播放 | 先关闭对应 App 增强规则 |
| 手机发热、耗电 | iOS 先切 Lite，Android 减少叠加规则 |
| 一键导入无反应 | 复制链接，在客户端里手动从 URL 导入 |

> 不要一出问题就继续加规则。先减法排查。

---

## 🚫 小白不要做这些

- 不要同时启用 Stable、Stable Plus、Lite、Full。
- 不要把 Android 文件导入 Shadowrocket。
- 不要把 iOS `.sgmodule` 当成 Android 配置。
- 不要把 Full 当日常版本长期使用。
- 不要把“覆盖存在”理解成“每个 App 都已经真机测试通过”。
- 不懂配置时，不要先碰 sing-box、v2rayNG 手动 routing。

---

## 使用限制与风险声明

> 本仓库所有资源仅供个人学习、研究与实验使用，严禁用于任何商业、盈利、收费、转售、引流、代运营、付费服务或其他变相商业目的。
>
> 未经维护者明确许可，禁止转载、搬运、镜像、二次发布或改名发布至任何境内平台。
>
> 本仓库内容仅供参考。使用者应自行判断是否适合使用，并自行承担由导入、运行、修改或依赖本仓库内容产生的风险。

详细安全策略见：[SECURITY.md](SECURITY.md)。

---

## 🔒 Android 使用边界

Android 版只迁移这些能力：

- 域名规则
- 关键词规则
- IP 规则
- 部分可迁移拦截逻辑

Android 版不包含这些 iOS 能力：

- Script
- MITM
- Rewrite
- Header Rewrite
- Body Rewrite

所以 Android 版不保证达到 iOS / Shadowrocket / Surge 完全相同的净化效果。

`iOS-Compatible-Reject` 只提取 Android 规则引擎能识别的规则，不包含 iOS / Surge / Shadowrocket 的 Script、MITM、Rewrite、Header Rewrite、Body Rewrite 能力。

---

<details>
<summary>维护方式</summary>

本仓库采用 **source-first** 维护方式：

```text
Rules + Scripts + Rewrite/Sources + Rewrite/Remotes + Rewrite/Profiles
        -> scripts/build_module.py --build --profile stable
        -> scripts/factory_finalize.py --sync-root
        -> scripts/build_release_variants.py
        -> Release/Ronghemokuai-*.sgmodule
```

根目录 `Ronghemokuai.sgmodule` 是默认 Stable 的生成结果。正常维护时应先改源头文件，再构建生成，不要只手动修改最终模块。

</details>

<details>
<summary>仓库结构</summary>

| 路径 | 作用 |
|---|---|
| `Rules/` | 规则源头：direct、reject、app-clean、web-ads 等 |
| `Scripts/` | 脚本源头与统一 cleaner |
| `Rewrite/Sources/` | 模块各 section 的源头文件 |
| `Rewrite/Profiles/` | Stable / Stable Plus / Lite / Full 构建配置 |
| `Rewrite/Remotes/` | 外部规则源、候选源和参考模块 |
| `Release/` | 自动生成的发布模块 |
| `Android/` | Android 可用规则、配置和 App 增强规则 |
| `docs/` | 使用、维护、测试、回滚文档 |
| `reports/` | 健康检查、覆盖、风险和候选报告 |
| `scripts/` | 构建、验证、审计、报告脚本 |

</details>

<details>
<summary>维护入口</summary>

| 类型 | 链接 | 用途 |
|---|---|---|
| 误杀预防标准 | [docs/FALSE_POSITIVE_PREVENTION.md](docs/FALSE_POSITIVE_PREVENTION.md) | 少误杀、Stable 准入、pending 边界和 Lite 对照排查 |
| 模块功能 | [docs/MODULE_FEATURES.md](docs/MODULE_FEATURES.md) | 四个版本功能、App 覆盖和使用边界 |
| 自动化策略 | [docs/AUTOMATION_POLICY.md](docs/AUTOMATION_POLICY.md) | 自动收集、自动筛选、人工晋级边界 |
| Profile 边界 | [docs/PROFILE_POLICY.md](docs/PROFILE_POLICY.md) | Stable / Stable Plus / Lite / Full 发布边界 |
| MITM 策略 | [docs/MITM_POLICY.md](docs/MITM_POLICY.md) | hostname 分级和增长控制 |
| 测试标准 | [docs/TESTING.md](docs/TESTING.md) | 手动测试流程和记录要求 |
| 发布回滚 | [docs/RELEASE.md](docs/RELEASE.md) | 发布、测试、回滚流程 |
| 质量门禁 | [docs/QUALITY_GATE.md](docs/QUALITY_GATE.md) | 阻断项和发布前检查 |
| 长期路线 | [docs/ROADMAP.md](docs/ROADMAP.md) | 后续优化方向和优先级 |
| Android App 规则索引 | [Android/apps.md](Android/apps.md) | Android 可选增强、组合包、单 App、风险层说明 |

</details>

<details>
<summary>报告入口</summary>

| 报告 | 用途 |
|---|---|
| [reports/repository_health_report.md][health-report] | 仓库健康总览 |
| [reports/profile_validation_report.md](reports/profile_validation_report.md) | 四个 profile 构建结果、脚本数、MITM 数 |
| [reports/app_coverage_matrix.md](reports/app_coverage_matrix.md) | App 覆盖矩阵 |
| [reports/app_status_matrix.md](reports/app_status_matrix.md) | App 状态矩阵，区分覆盖与真实测试 |
| [reports/reject_risk_report.md](reports/reject_risk_report.md) | REJECT 高风险误伤分类 |
| [reports/rule_traceability_matrix.md](reports/rule_traceability_matrix.md) | 高风险规则来源、风险等级、测试状态和回滚路径 |
| [reports/stable_plus_promotion_report.md](reports/stable_plus_promotion_report.md) | Stable Plus 晋级候选报告 |
| [reports/manual_test_log.md](reports/manual_test_log.md) | 人工测试记录 |
| [reports/candidate_security_score_report.md](reports/candidate_security_score_report.md) | 候选源安全评分 |
| [reports/report_freshness_report.md](reports/report_freshness_report.md) | 治理报告新鲜度检查 |
| [reports/domestic_app_connectivity_audit.md](reports/domestic_app_connectivity_audit.md) | 国内 App 联网和图片加载误伤排查 |
| [reports/workflow_health_report.md](reports/workflow_health_report.md) | workflow 最新状态 |

</details>

[import-page]: https://grandpaniuu.github.io/GrandpaNiu/import.html
[stable-import]: https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fgrandpaniuu.github.io%2FGrandpaNiu%2FRelease%2FRonghemokuai-stable.sgmodule
[stable-plus-import]: https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fgrandpaniuu.github.io%2FGrandpaNiu%2FRelease%2FRonghemokuai-stable-plus.sgmodule
[lite-import]: https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fgrandpaniuu.github.io%2FGrandpaNiu%2FRelease%2FRonghemokuai-lite.sgmodule
[full-import]: https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fgrandpaniuu.github.io%2FGrandpaNiu%2FRelease%2FRonghemokuai-full.sgmodule
[android-import]: https://grandpaniuu.github.io/GrandpaNiu/android.html
[stable-pages]: https://grandpaniuu.github.io/GrandpaNiu/Release/Ronghemokuai-stable.sgmodule
[stable-plus-pages]: https://grandpaniuu.github.io/GrandpaNiu/Release/Ronghemokuai-stable-plus.sgmodule
[lite-pages]: https://grandpaniuu.github.io/GrandpaNiu/Release/Ronghemokuai-lite.sgmodule
[full-pages]: https://grandpaniuu.github.io/GrandpaNiu/Release/Ronghemokuai-full.sgmodule
[root-pages]: https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule
[stable-raw]: https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Release/Ronghemokuai-stable.sgmodule
[stable-plus-raw]: https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Release/Ronghemokuai-stable-plus.sgmodule
[lite-raw]: https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Release/Ronghemokuai-lite.sgmodule
[full-raw]: https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Release/Ronghemokuai-full.sgmodule
[root-raw]: https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Ronghemokuai.sgmodule
[android-full-raw]: https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Android-Full.yaml
[android-mihomo-ads-raw]: https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Ads.yaml
[android-singbox-raw]: https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/sing-box/GrandpaNiu-Ads.json
[android-adguard-raw]: https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/adguard/GrandpaNiu-DNS.txt
[android-v2rayng-raw]: https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/v2rayng/GrandpaNiu-v2rayng-routing.json
[android-ios-compatible-mihomo-raw]: https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/apps/iOS-Compatible-Reject.yaml
[android-ios-compatible-singbox-raw]: https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/sing-box/apps/iOS-Compatible-Reject.json
[android-ios-compatible-adguard-raw]: https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/adguard/apps/iOS-Compatible-Reject.txt
[android-ios-compatible-v2rayng-raw]: https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/v2rayng/apps/iOS-Compatible-Reject-routing.json
[health-report]: reports/repository_health_report.md
