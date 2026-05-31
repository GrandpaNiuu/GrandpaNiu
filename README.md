<div align="center">

# GrandpaNiu

Shadowrocket / Surge 自用融合净化模块工厂。

[![Import](https://img.shields.io/static/v1?label=Import&message=Multi%20Version%20Page&color=0A84FF&labelColor=111827&style=for-the-badge)][import-page]
[![Stable](https://img.shields.io/static/v1?label=Stable&message=Default&color=34C759&labelColor=111827&style=for-the-badge)][stable-import]
[![Health](https://img.shields.io/static/v1?label=Health&message=Reports&color=5856D6&labelColor=111827&style=for-the-badge)][health-report]

</div>

## 使用限制与风险声明

> 本仓库所有资源仅供个人学习、研究与实验使用，严禁用于任何商业、盈利、收费、转售、引流、代运营、付费服务或其他变相商业目的。
>
> 未经维护者明确许可，禁止以任何形式将本仓库资源转载、分享、搬运、镜像、二次发布或改名发布至任何境内平台，包括但不限于社交媒体、博客、论坛、网盘、代码托管平台、公众号、即时通讯群组、付费社群、资源站或聚合站。
>
> 本仓库所有资源仅供参考，使用者应自行判断是否适合使用，并自行承担全部风险。维护者不对因使用、复制、修改、分发、转载、导入、运行、参考或依赖本仓库内容造成的任何直接或间接损失承担责任，包括但不限于数据丢失、网络故障、账号异常、服务不可用、配置损坏、隐私泄露、第三方追责或法律纠纷。

详细安全策略见：[SECURITY.md](SECURITY.md)。

## 一句话说明

`GrandpaNiu` 是一个源头驱动的 Shadowrocket 模块工厂。仓库不会长期手工维护根目录模块，而是从 `Rules`、`Scripts`、`Rewrite/Sources`、`Rewrite/Profiles` 和维护脚本自动生成四个独立模块。

维护原则：**所有已纳入覆盖的 App 一视同仁维护，不设置单独例外。**

日常使用只推荐启用一个版本：**默认用 Stable**。根目录 `Ronghemokuai.sgmodule` 就是默认 Stable，Release 目录中的 Stable 是同一默认版本的独立发布文件。

## 版本选择

优先从多版本导入页选择版本：

[打开多版本导入页][import-page]

| 版本 | 定位 | 默认使用 | 覆盖重点 | 风险边界 | 导入 |
|---|---|---|---|---|---|
| Stable | 默认正式版 | 是 | 已纳入 App 的稳定覆盖 + 常用净化 | 优先稳定、低误杀 | [导入][stable-import] |
| Stable Plus | 增强测试版 | 否 | Stable + 更多常用 App MITM 覆盖 | 只做测试，不自动晋级 Stable | [导入][stable-plus-import] |
| Lite | 低耗电版 | 否 | 最小必要覆盖集合 | 覆盖少，适合排查异常 | [导入][lite-import] |
| Full | 全量排查版 | 否 | 完整 extended MITM 层 | 不建议长期启用 | [导入][full-import] |

> 不要同时启用多个版本。覆盖说明来自规则、脚本、Rewrite、MITM 和静态扫描，不等于所有 App 都已人工测试通过。

## 四个版本分别包含什么

### Stable：默认正式版

适合长期日常使用。目标不是最大覆盖，而是稳定、低误杀、可长期维护。

主要包含：

- 已纳入 App 的广告、开屏、弹窗、横幅、信息流、推荐位、活动卡片净化。
- Spotify、YouTube、知乎等已纳入 App 按统一标准维护，不设置特殊优先级。
- 常用方向：电商购物、本地生活、内容社区、音频内容、地图工具、资讯与工具类 App。
- 脚本融合：低风险 JSON 清理类脚本由 `Scripts/app-cleaner.js` 统一承接，减少重复脚本入口。

### Stable Plus：增强测试版

适合测试更多常用 App 覆盖。它不是默认发布版本，也不会自动把内容合并进 Stable。

晋级规则：

```text
Stable Plus 中测试
-> 登录 / 验证码 / 支付前置 / 常用流程无异常
-> 单项 App 进入晋级候选
-> 人工确认后再进入 Stable
```

### Lite：低耗电版

适合手机发热、耗电明显、App 登录异常、页面异常时排查。Lite 不追求覆盖广度，它的价值是低风险、低 MITM、便于定位异常来源。

### Full：全量排查版

只适合查漏拦和临时定位缺失 hostname，不建议长期启用。Full 不适合：登录、支付、验证码、银行 App、对耗电敏感的设备、长期日常使用。

## 自动拉取规则和脚本的边界

仓库可以做“自动化收集和筛选”，但不能无审核地把外部脚本直接塞进默认 Stable。专业的自动化路径应该是：

```text
可信来源收集
-> 静态安全扫描
-> 生成候选报告
-> 进入 Stable Plus 或 pending 区
-> 构建验证 / 语法验证 / 重复检查
-> 人工测试
-> 单项晋级 Stable
```

可以自动进入的内容：

- 明确安全的规则源。
- 已知可信源的低风险广告域名规则。
- 不涉及登录、支付、验证码、会员权益、Cookie、Token、加密 body 的普通净化逻辑。
- 通过语法检查、结构检查、重复检查的候选项。

不能自动直接进入 Stable 的内容：

- 未知作者脚本。
- 混淆脚本。
- 会员权益、破解、绕过、登录、支付、验证码相关脚本。
- 会改写 request body、Cookie、Token、账户状态的脚本。
- 无法解释用途的远程模块。

## 导入地址

| 版本 | Pages 地址 | Raw 地址 |
|---|---|---|
| Stable | [Ronghemokuai-stable.sgmodule][stable-pages] | [Raw][stable-raw] |
| Stable Plus | [Ronghemokuai-stable-plus.sgmodule][stable-plus-pages] | [Raw][stable-plus-raw] |
| Lite | [Ronghemokuai-lite.sgmodule][lite-pages] | [Raw][lite-raw] |
| Full | [Ronghemokuai-full.sgmodule][full-pages] | [Raw][full-raw] |
| 默认 Root | [Ronghemokuai.sgmodule][root-pages] | [Raw][root-raw] |

导入后建议在 Shadowrocket 中执行：更新模块、更新脚本、更新全部资源。

## 构建流程

```text
Rules + Scripts + Rewrite/Sources + Rewrite/Remotes + Rewrite/Profiles
        -> scripts/build_module.py --build --profile stable
        -> scripts/factory_finalize.py --sync-root
        -> scripts/build_release_variants.py
        -> Release/Ronghemokuai-*.sgmodule
```

根目录 `Ronghemokuai.sgmodule` 仍保持 Stable。四个独立版本由 `scripts/build_release_variants.py` 自动生成。

## 自动化能力

仓库可以自动做：

- 构建 Stable / Stable Plus / Lite / Full 四个独立模块。
- 检查 Root 与 Release 是否一致。
- 检查 profile 是否能构建。
- 检查 JS 语法：`node --check Scripts/app-cleaner.js`。
- 生成覆盖矩阵、脚本清单、健康报告、回滚报告。
- 收集可信候选规则源并生成候选报告。
- 对 workflow 失败自动创建 Issue。

仓库不会也不应该无条件自动做：

- 自动真机测试 App。
- 自动确认任何 App 的实际可用性。
- 自动确认电商订单页、支付前置、验证码、登录流程无异常。
- 自动把 Stable Plus、Full 或未知远程脚本直接晋级到 Stable。

## 安全边界

本仓库不加入：

- 会员解锁、Premium 破解、支付绕过、登录绕过、账户权益伪造。
- Cookie / Token / BoxJS 依赖。
- 成人、博彩、短链、镜像源、`ghproxy`、未知混淆脚本。

安全策略对所有 App 一视同仁：只要涉及登录、支付、验证码、银行、账户权益、Cookie、Token，都必须按高风险处理；不因为某个 App 被长期使用就给它特殊例外，也不因为某个 App 新加入就降低安全门槛。

## 维护入口

| 类型 | 链接 | 用途 |
|---|---|---|
| Codex 执行标准 | [docs/CODEX_EXECUTION_STANDARD.md](docs/CODEX_EXECUTION_STANDARD.md) | Codex 修改边界、任务分级、必跑命令和回滚要求 |
| 模块功能 | [docs/MODULE_FEATURES.md](docs/MODULE_FEATURES.md) | 四个版本功能、App 覆盖和使用边界 |
| 自动化策略 | [docs/AUTOMATION_POLICY.md](docs/AUTOMATION_POLICY.md) | 自动收集、自动筛选、人工晋级边界 |
| Profile 边界 | [docs/PROFILE_POLICY.md](docs/PROFILE_POLICY.md) | Stable / Stable Plus / Lite / Full 发布边界 |
| 脚本融合计划 | [docs/SCRIPT_CONSOLIDATION_PLAN.md](docs/SCRIPT_CONSOLIDATION_PLAN.md) | 脚本减少、融合、回滚策略 |
| MITM 策略 | [docs/MITM_POLICY.md](docs/MITM_POLICY.md) | hostname 分级和增长控制 |
| 测试标准 | [docs/TESTING.md](docs/TESTING.md) | 手动测试流程和记录要求 |
| 发布回滚 | [docs/RELEASE.md](docs/RELEASE.md) | 发布、测试、回滚流程 |
| 质量门禁 | [docs/QUALITY_GATE.md](docs/QUALITY_GATE.md) | 阻断项和发布前检查 |
| 长期路线 | [docs/ROADMAP.md](docs/ROADMAP.md) | 后续优化方向和优先级 |

## 报告入口

| 报告 | 用途 |
|---|---|
| [reports/repository_health_report.md][health-report] | 仓库健康总览 |
| [reports/profile_validation_report.md](reports/profile_validation_report.md) | 四个 profile 构建结果、脚本数、MITM 数 |
| [reports/script_inventory_report.md](reports/script_inventory_report.md) | 脚本清单与可融合分析 |
| [reports/script_dedupe_report.md](reports/script_dedupe_report.md) | 脚本融合和旧入口移除报告 |
| [reports/script_consolidation_rollback_report.md](reports/script_consolidation_rollback_report.md) | 脚本融合回滚路径 |
| [reports/app_cleaner_active_report.md](reports/app_cleaner_active_report.md) | app-cleaner active 批量融合说明 |
| [reports/app_coverage_matrix.md](reports/app_coverage_matrix.md) | App 覆盖矩阵 |
| [reports/app_status_matrix.md](reports/app_status_matrix.md) | App 状态矩阵，区分覆盖与真实测试 |
| [reports/reject_risk_report.md](reports/reject_risk_report.md) | REJECT 高风险误伤分类 |
| [reports/reject_manual_review_plan.md](reports/reject_manual_review_plan.md) | REJECT 人工复核计划 |
| [reports/stable_plus_promotion_report.md](reports/stable_plus_promotion_report.md) | Stable Plus 晋级候选报告 |
| [reports/stable_plus_manual_test_plan.md](reports/stable_plus_manual_test_plan.md) | Stable Plus 单项测试计划 |
| [reports/promotion_pr_report.md](reports/promotion_pr_report.md) | Stable Plus 单项晋级 PR 审查材料 |
| [reports/manual_test_log.md](reports/manual_test_log.md) | 人工测试记录 |
| [reports/candidate_security_score_report.md](reports/candidate_security_score_report.md) | 候选源安全评分 |
| [reports/candidate_followup_plan.md](reports/candidate_followup_plan.md) | 候选源后续处理计划 |
| [reports/report_freshness_report.md](reports/report_freshness_report.md) | 治理报告新鲜度检查 |
| [reports/domestic_app_connectivity_audit.md](reports/domestic_app_connectivity_audit.md) | 国内 App 联网和图片加载误伤排查 |
| [reports/workflow_health_report.md](reports/workflow_health_report.md) | workflow 最新状态 |

## 使用提醒

- 默认使用 Stable。
- 不要同时启用多个版本。
- Full 只用于排查，不适合长期启用。
- 未经真机测试，不要把“规则覆盖存在”理解为“已经验证通过”。
- 出现异常时先切 Lite，再逐步定位是 MITM、脚本还是规则导致。

[import-page]: https://grandpaniuu.github.io/GrandpaNiu/import.html
[stable-import]: https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fgrandpaniuu.github.io%2FGrandpaNiu%2FRelease%2FRonghemokuai-stable.sgmodule
[stable-plus-import]: https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fgrandpaniuu.github.io%2FGrandpaNiu%2FRelease%2FRonghemokuai-stable-plus.sgmodule
[lite-import]: https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fgrandpaniuu.github.io%2FGrandpaNiu%2FRelease%2FRonghemokuai-lite.sgmodule
[full-import]: https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fgrandpaniuu.github.io%2FGrandpaNiu%2FRelease%2FRonghemokuai-full.sgmodule
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
[health-report]: reports/repository_health_report.md
