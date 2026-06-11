<<<<<<< Updated upstream
<div align="center">

# GrandpaNiu

**Shadowrocket / Surge / Android 净化规则与模块集合**

[![Module Factory Build](https://github.com/GrandpaNiuu/GrandpaNiu/actions/workflows/module-factory-build.yml/badge.svg)](https://github.com/GrandpaNiuu/GrandpaNiu/actions/workflows/module-factory-build.yml)
[![Repository Health Check](https://github.com/GrandpaNiuu/GrandpaNiu/actions/workflows/repository-health.yml/badge.svg)](https://github.com/GrandpaNiuu/GrandpaNiu/actions/workflows/repository-health.yml)
[![Scheduled Module Update](https://github.com/GrandpaNiuu/GrandpaNiu/actions/workflows/scheduled-module-update.yml/badge.svg)](https://github.com/GrandpaNiuu/GrandpaNiu/actions/workflows/scheduled-module-update.yml)

拦截常见广告、开屏、弹窗、横幅、信息流推荐、活动卡片和追踪请求。  

## 使用限制与风险声明

> 本仓库所有资源仅供个人学习、研究与实验使用，严禁用于任何商业、盈利、收费、转售、引流、代运营、付费服务或其他变相商业目的。
>
> 未经维护者明确许可，禁止转载、搬运、镜像、二次发布或改名发布至任何境内平台。
>
> 本仓库内容仅供参考。使用者应自行判断是否适合使用，并自行承担由导入、运行、修改或依赖本仓库内容产生的风险。

详细安全策略见：[SECURITY.md](SECURITY.md)。

</div>

---

## 公开入口

- GitHub Pages 首页：<https://grandpaniuu.github.io/GrandpaNiu/>
- iOS Fusion 模块：<https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule>
- Shadowrocket 导入页：<https://grandpaniuu.github.io/GrandpaNiu/import.html>
- Android 导入页：<https://grandpaniuu.github.io/GrandpaNiu/android.html>
- Release 目录：<https://grandpaniuu.github.io/GrandpaNiu/Web/catalog.md>
- 机器可读索引：<https://grandpaniuu.github.io/GrandpaNiu/Web/release-links.json>

---

## 入口选择

| 图标 | 你现在的情况 | 点这里 | 说明 |
|---|---|---|---|
|  | iPhone / iPad，使用 Shadowrocket | [导入融合模块][fusion-import] | 唯一推荐入口 |
| 📱 | Android 用户 | [打开 Android 导入页][android-import] | 进去后按“有无节点”选择版本 |
| 📊 | 想看仓库健康和报告 | [查看报告][health-report] | 给维护者和高级用户查看 |

**最简单选择：**

- iOS 普通用户：只导入 **融合模块**。
- Android 用户：进 **Android 导入页**。
- 出问题：先关闭模块或对应 App 增强规则，不再切换多版本。

---

## 新手怎么用

### iOS / Shadowrocket

1. 从上面的入口选择 **融合模块**。
2. 打开 Shadowrocket，启用模块。
3. 执行：**更新模块、更新脚本、更新全部资源**。
4. 如果出现登录异常、页面空白、图片不加载，先关闭模块或定位对应 App 规则。

### Android

1. 从上面的入口进入 **Android 导入页**。
2. 没有节点：选完整配置版。
3. 已有节点订阅：选 Mihomo 规则集版，不要覆盖原节点。
4. 想增强覆盖：再测试 iOS 可复用规则包。
5. 出现误伤：先关闭增强包，不要继续叠加规则。

---

## 版本策略

本仓库现在采用 **单一融合版**：

| 版本 | 适合谁 | 一句话说明 | 风险 |
|---|---|---|---|
| **Fusion** | 所有 iOS 用户 | 合并原 Stable、Stable Plus、Lite、Full 的覆盖入口 | 高于旧 Stable，低于手动多版本叠加 |

> 不再提供 Stable / Stable Plus / Lite / Full 给用户选择。后续维护只围绕 `Rewrite/Profiles/fusion.conf`。

---

## 功能范围

### iOS / Shadowrocket / Surge

- 🧹 净化常见广告、开屏、弹窗、横幅、信息流推荐、活动卡片。
- 🔧 支持部分 App 的 Rule、Rewrite、Script、MITM hostname 覆盖。
- 🎵 已纳入 Spotify、YouTube、知乎等常用维护项。
- 🧩 低风险 JSON 清理脚本由 `Scripts/app-cleaner.js` 统一承接，减少重复脚本入口。

### Android

Android 版是从规则中迁移出的可用格式，**不是 iOS `.sgmodule`**。

支持：

- 📦 Mihomo / Clash Meta / FlClash 完整配置
- 🧩 Mihomo / Clash Meta / FlClash 规则集
- 📘 sing-box rule-set
- 🛡️ AdGuard DNS / AdGuard Home 过滤规则
- 🧭 v2rayNG / V2Ray / Xray routing 片段
- 📱 App 可选增强规则
- ⚡ iOS 可复用规则包

Android 主要依靠域名、关键词和 IP 规则拦截。它不包含 iOS 的 Script、MITM、Rewrite、Header Rewrite、Body Rewrite 能力。

---

## Android 怎么选

| 场景 | 推荐选择 | 提醒 |
|---|---|---|
| 没有节点，只想拦广告 | 完整配置版 | 适合 FlClash / Mihomo / Clash Meta |
| 已有节点订阅 | Mihomo 规则集版 | 不覆盖原节点，作为 rule-provider 合并 |
| 使用 sing-box | sing-box rule-set | 需要会引用 rule-set |
| 使用 AdGuard | DNS 过滤规则 | 只能做域名级过滤 |
| 使用 v2rayNG / V2Ray / Xray | routing 片段 | 需要手动合并 routing |
| 想增强通用覆盖 | iOS 可复用规则包 | 覆盖更广，也更容易误伤 |

> Android 用户统一从上方 **Android 导入页** 进入，不在 README 里重复放每个文件入口，避免选错。

---

## 出问题先看这里

| 现象 | 先做什么 |
|---|---|
| 登录异常 | 关闭模块，再定位对应 App 规则 |
| 图片不加载 | 关闭 iOS 可复用规则包或对应 App 增强规则 |
| 视频无法播放 | 关闭对应 App 增强规则 |
| 手机发热、耗电 | 减少规则叠加，回滚 fusion 中对应源头 |
| 一键导入无反应 | 复制入口链接，在客户端里从 URL 手动导入 |

排查原则：**先减少规则，再逐步加回。**

---

## 不建议这样做

- 不要把 Android 文件导入 Shadowrocket。
- 不要把 iOS `.sgmodule` 当成 Android 配置。
- 不要把“规则覆盖存在”理解成“已经完整真机测试”。
- 不懂配置时，不要先改 sing-box 或 v2rayNG routing。

<details>
<summary>Android 使用边界</summary>

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

</details>

<details>
<summary>维护方式</summary>

本仓库采用 **source-first** 维护方式：

```text
Rules + Scripts + Rewrite/Sources + Rewrite/Remotes + Rewrite/Profiles/fusion.conf
        -> scripts/build_module.py --build --profile fusion
        -> scripts/factory_finalize.py --sync-root
        -> scripts/build_release_variants.py
        -> Ronghemokuai.sgmodule + Release/Ronghemokuai.sgmodule
```

根目录 `Ronghemokuai.sgmodule` 是融合版生成结果。正常维护时应先改源头文件，再构建生成，不要只手动修改最终模块。

</details>

<details>
<summary>仓库结构</summary>

| 路径 | 作用 |
|---|---|
| `Rules/` | 规则源头：direct、reject、app-clean、web-ads 等 |
| `Scripts/` | 脚本源头与统一 cleaner |
| `Rewrite/Sources/` | 模块各 section 的源头文件 |
| `Rewrite/Profiles/fusion.conf` | 单一融合构建配置 |
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
| 误杀预防标准 | [docs/FALSE_POSITIVE_PREVENTION.md](docs/FALSE_POSITIVE_PREVENTION.md) | 少误杀、准入、pending 边界和对照排查 |
| 模块功能 | [docs/MODULE_FEATURES.md](docs/MODULE_FEATURES.md) | App 覆盖和使用边界 |
| 自动化策略 | [docs/AUTOMATION_POLICY.md](docs/AUTOMATION_POLICY.md) | 自动收集、自动筛选、人工复核边界 |
| Profile 边界 | [docs/PROFILE_POLICY.md](docs/PROFILE_POLICY.md) | Fusion 发布边界 |
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
| [reports/profile_validation_report.md](reports/profile_validation_report.md) | fusion profile 构建结果、脚本数、MITM 数 |
| [reports/module_integrity_report.md](reports/module_integrity_report.md) | Fusion 模块语法、重复项、脚本入口和 MITM 完整性 |
| [reports/app_coverage_matrix.md](reports/app_coverage_matrix.md) | App 覆盖矩阵 |
| [reports/app_status_matrix.md](reports/app_status_matrix.md) | App 状态矩阵，区分覆盖与真实测试 |
| [reports/reject_risk_report.md](reports/reject_risk_report.md) | REJECT 高风险误伤分类 |
| [reports/rule_traceability_matrix.md](reports/rule_traceability_matrix.md) | 高风险规则来源、风险等级、测试状态和回滚路径 |
| [reports/manual_test_log.md](reports/manual_test_log.md) | 人工测试记录 |
| [reports/candidate_security_score_report.md](reports/candidate_security_score_report.md) | 候选源安全评分 |
| [reports/report_freshness_report.md](reports/report_freshness_report.md) | 治理报告新鲜度检查 |
| [reports/domestic_app_connectivity_audit.md](reports/domestic_app_connectivity_audit.md) | 国内 App 联网和图片加载误伤排查 |
| [reports/workflow_health_report.md](reports/workflow_health_report.md) | workflow 最新状态 |

</details>

<details>
<summary>发布文件直链</summary>

| 版本 | Pages 地址 |
|---|---|
| Fusion | https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule |
| Fusion Release | https://grandpaniuu.github.io/GrandpaNiu/Release/Ronghemokuai.sgmodule |

</details>

[fusion-import]: https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fgrandpaniuu.github.io%2FGrandpaNiu%2FRonghemokuai.sgmodule
[android-import]: https://grandpaniuu.github.io/GrandpaNiu/android.html
[health-report]: reports/repository_health_report.md
=======
﻿Get-Clipboard | Set-Content -Path README.md -Encoding UTF8
>>>>>>> Stashed changes
