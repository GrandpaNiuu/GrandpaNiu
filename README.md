<div align="center">

# GrandpaNiu

Shadowrocket / Surge / Android 净化规则与模块集合。

[![Import](https://img.shields.io/static/v1?label=Import&message=Multi%20Version%20Page&color=0A84FF&labelColor=111827&style=for-the-badge)][import-page]
[![Stable](https://img.shields.io/static/v1?label=Stable&message=Default&color=34C759&labelColor=111827&style=for-the-badge)][stable-import]
[![Android](https://img.shields.io/static/v1?label=Android&message=Import&color=3DDC84&labelColor=111827&style=for-the-badge)][android-import]
[![Health](https://img.shields.io/static/v1?label=Health&message=Reports&color=5856D6&labelColor=111827&style=for-the-badge)][health-report]

</div>

## 快速说明

`GrandpaNiu` 是一个面向 Shadowrocket / Surge / Android 用户的规则与模块项目，用于拦截常见广告、开屏、弹窗、横幅、信息流推荐、活动卡片、追踪域名和部分 App 广告请求。

普通用户只需要做一件事：**按自己的设备和使用场景选择一个版本导入，不要同时启用多个版本。**

日常使用推荐：**Stable**。

## 使用限制与风险声明

> 本仓库所有资源仅供个人学习、研究与实验使用，严禁用于任何商业、盈利、收费、转售、引流、代运营、付费服务或其他变相商业目的。
>
> 未经维护者明确许可，禁止转载、搬运、镜像、二次发布或改名发布至任何境内平台。
>
> 本仓库内容仅供参考。使用者应自行判断是否适合使用，并自行承担由导入、运行、修改或依赖本仓库内容产生的风险。

详细安全策略见：[SECURITY.md](SECURITY.md)。

## 版本怎么选

| 版本 | 适合谁 | 覆盖范围 | 风险边界 | 推荐程度 | 导入 |
|---|---|---|---|---|---|
| Stable | 大多数用户 | 稳定覆盖 + 常用净化 | 优先低误伤、可长期使用 | 默认推荐 | [导入][stable-import] |
| Stable Plus | 想测试更多 App 覆盖的用户 | Stable + 更多测试覆盖 | 不自动晋级 Stable | 测试使用 | [导入][stable-plus-import] |
| Lite | 手机发热、耗电、登录异常时排查 | 最小必要覆盖 | 覆盖少、风险低 | 排查使用 | [导入][lite-import] |
| Full | 查漏拦、临时定位 hostname | 全量排查覆盖 | 不适合长期启用 | 高级排查 | [导入][full-import] |

> 普通用户默认导入 Stable。不要同时启用多个版本。覆盖存在不等于所有 App 都已人工测试通过。导入后建议在 Shadowrocket 中执行：更新模块、更新脚本、更新全部资源。

## 功能作用

### iOS / Shadowrocket / Surge

主要包含：

- 常见广告、开屏、弹窗、横幅、信息流、推荐位、活动卡片净化。
- 部分 App 的规则、Rewrite、Script、MITM hostname 覆盖。
- Spotify、YouTube、知乎等已纳入 App 的统一维护项。
- 低风险 JSON 清理类脚本由 `Scripts/app-cleaner.js` 统一承接，减少重复脚本入口。

### Android

Android 版本是可迁移规则导出，不是 iOS `.sgmodule`。

目前支持：

- Mihomo / Clash Meta / FlClash 完整配置
- Mihomo / Clash Meta / FlClash 规则集
- sing-box rule-set
- AdGuard DNS / AdGuard Home 自定义过滤规则
- v2rayNG / V2Ray / Xray routing 片段

Android 版主要通过域名、关键词和 IP 规则拦截常见广告域名、追踪域名和部分 App 广告请求。它不包含 Shadowrocket / Surge 的 Script、MITM、Rewrite、Header Rewrite、Body Rewrite 能力。

## Android 怎么用

Android 不放在 iOS 模块导入表里。Android 用户请从这里进入专门的导入页：

- [打开 Android 导入页][android-import]

如果你不确定选哪个版本，先看下面这个表。

| 场景 | 推荐版本 | 文件 | 适合客户端 | 导入方式 |
|---|---|---|---|---|
| 没有节点，只想拦广告 | 完整配置版 | [GrandpaNiu-Android-Full.yaml][android-full-raw] | FlClash / Mihomo / Clash Meta | 直接作为完整配置导入 |
| 已经有节点订阅 | Mihomo 规则集版 | [GrandpaNiu-Ads.yaml][android-mihomo-ads-raw] | FlClash / Mihomo / Clash Meta | 作为 rule-provider 合并进原配置 |
| 使用 sing-box | sing-box 规则集版 | [GrandpaNiu-Ads.json][android-singbox-raw] | sing-box / SFA | 在自己的配置中引用 rule-set |
| 使用 AdGuard | DNS 规则版 | [GrandpaNiu-DNS.txt][android-adguard-raw] | AdGuard Android / AdGuard DNS / AdGuard Home | 作为自定义 DNS / 过滤规则导入 |
| 使用 v2rayNG / V2Ray / Xray | routing 片段版 | [GrandpaNiu-v2rayng-routing.json][android-v2rayng-raw] | v2rayNG / V2Ray / Xray | 手动合并 routing 规则 |

> 如果一键导入无反应，通常不是链接失效，而是客户端不支持跳转协议。请复制链接后，在客户端中手动导入。

### 1）完整配置版：GrandpaNiu-Android-Full.yaml

适合：

- 没有机场节点。
- 没有现成配置。
- 只想做广告拦截。
- 想直接导入就用。

文件：

- [GrandpaNiu-Android-Full.yaml][android-full-raw]

导入方式：

#### FlClash / Mihomo / Clash Meta

1. 打开客户端。
2. 进入 **配置 / Profiles**。
3. 选择 **从 URL 导入**。
4. 粘贴下面链接：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Android-Full.yaml
```

5. 保存并启用该配置。

注意事项：

- 这是**完整配置**。
- **已有节点订阅用户不要导入这个版本**。
- 否则可能覆盖你原来的节点、策略组和规则。

---

### 2）Mihomo 规则集版：GrandpaNiu-Ads.yaml

适合：

- 已经有机场节点订阅。
- 已经有自己的 Mihomo / Clash Meta / FlClash 配置。
- 只想把 GrandpaNiu 广告规则加进去，不想覆盖原配置。

文件：

- [GrandpaNiu-Ads.yaml][android-mihomo-ads-raw]

导入方式：

#### 方法一：手动合并到原配置（推荐）

把下面内容加入你的原配置：

```yaml
rule-providers:
  grandpaniu_ads:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Ads.yaml"
    path: ./ruleset/GrandpaNiu-Ads.yaml
    interval: 86400

rules:
  - RULE-SET,grandpaniu_ads,REJECT
  - MATCH,🚀 节点选择
```

#### 方法二：如果客户端支持远程规则集

1. 打开原配置。
2. 找到 `rule-providers`。
3. 添加 GrandpaNiu 的远程规则源。
4. 在 `rules` 最前面加入：

```yaml
- RULE-SET,grandpaniu_ads,REJECT
```

注意事项：

- **不要把它当完整配置导入**。
- 它只是**规则集**。
- `RULE-SET,grandpaniu_ads,REJECT` 必须放在 `MATCH`、`GEOIP`、代理分流规则之前。
- 否则广告请求可能先被原规则命中，导致不生效。

最终效果：

- 保留你原来的节点。
- 保留你原来的策略组。
- 广告请求被 GrandpaNiu 规则拦截。
- 其他流量继续走你原来的配置。

---

### 3）sing-box 规则集版：GrandpaNiu-Ads.json

适合：

- 已经会维护 sing-box 配置。
- 使用 sing-box / SFA。
- 想把 GrandpaNiu 作为远程 rule-set 引入。

文件：

- [GrandpaNiu-Ads.json][android-singbox-raw]

导入方式：

#### sing-box / SFA

1. 打开自己的 sing-box 配置。
2. 在 `route.rule_set` 或等效 rule-set 区域添加远程规则集地址。
3. 在 `route.rules` 中引用 GrandpaNiu 规则集。
4. 命中后走拦截动作。
5. 保存配置并重载客户端。

注意事项：

- 这不是完整 sing-box 配置。
- 不是一键导入版。
- 需要你自己会改 sing-box JSON。
- 如果你不会改，优先使用 Mihomo / FlClash 方案。

---

### 4）AdGuard DNS 规则版：GrandpaNiu-DNS.txt

适合：

- 使用 AdGuard Android。
- 使用 AdGuard DNS。
- 使用 AdGuard Home。
- 只想做轻量的域名过滤。

文件：

- [GrandpaNiu-DNS.txt][android-adguard-raw]

导入方式：

#### AdGuard Android

1. 打开 AdGuard。
2. 进入 **过滤器 / 用户规则** 或 **DNS 过滤**。
3. 添加自定义规则或订阅。
4. 粘贴下面链接：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/adguard/GrandpaNiu-DNS.txt
```

5. 保存并刷新规则。

#### AdGuard DNS / AdGuard Home

1. 进入后台。
2. 找到自定义过滤规则 / DNS 拦截列表。
3. 添加 GrandpaNiu 规则地址。
4. 保存并刷新规则。

注意事项：

- 这是**域名级**过滤。
- 不包含脚本、MITM、Rewrite。
- 效果会弱于 iOS 模块。
- 但更轻量，适合长期运行。

---

### 5）v2rayNG / V2Ray / Xray routing 片段版

适合：

- 高级用户。
- 已经会手动改 V2Ray / Xray 配置。
- 想把 GrandpaNiu 广告规则并入自己现有 routing。

文件：

- [GrandpaNiu-v2rayng-routing.json][android-v2rayng-raw]

导入方式：

#### v2rayNG / V2Ray / Xray

1. 打开你现有的配置文件。
2. 找到 `routing.rules`。
3. 把 GrandpaNiu 的广告 routing 片段手动合并进去。
4. 确保广告拦截规则排在普通代理 / 直连规则之前。
5. 保存并重新加载配置。

注意事项：

- **这不是节点订阅**。
- **这不是完整配置**。
- **不能直接一键导入就用**。
- 必须手动合并。
- 如果你不会手动改 routing，优先使用 Mihomo / FlClash 方案。

---

### 新手推荐顺序

如果你是普通用户，按这个顺序选：

1. **没有节点** → 用 `GrandpaNiu-Android-Full.yaml`。
2. **已有节点** → 用 `GrandpaNiu-Ads.yaml`。
3. **完全不懂配置** → 优先用 FlClash / Mihomo，不要先碰 sing-box 和 v2rayNG。
4. **只想轻量过滤** → 用 `GrandpaNiu-DNS.txt`。

### Android 使用边界

Android 版只迁移这些能力：

- 域名规则。
- 关键词规则。
- IP 规则。
- 部分可迁移拦截逻辑。

Android 版不包含这些 iOS 能力：

- Script。
- MITM。
- Rewrite。
- Header Rewrite。
- Body Rewrite。

所以 Android 版不保证达到 iOS / Shadowrocket / Surge 完全相同的净化效果。

### Android 使用教程

- [GrandpaNiu Android 使用教程](docs/android-user-guide.md)
- [已有节点用户教程](Android/mihomo/README-With-Proxy.md)
- [v2rayNG 手动合并教程](Android/v2rayng/README.md)

## 使用提醒

### 日常使用

- iOS / Shadowrocket / Surge 普通用户默认使用 Stable。
- 不要同时启用多个版本；Stable Plus、Lite、Full 主要用于测试或排查。
- 导入或更新模块后，建议在 Shadowrocket 中执行：更新模块、更新脚本、更新全部资源。

### 异常排查

- 出现登录异常、页面空白、图片不加载、App 发热或耗电时，先切 Lite。
- 如果切 Lite 后恢复正常，再逐步判断是 MITM、脚本还是规则导致。
- Full 只用于查漏拦和临时定位 hostname，不建议长期启用。

### Android 提醒

- Android 版只迁移域名、关键词、IP 规则和部分可迁移拦截逻辑。
- Android 版不包含 Script、MITM、Rewrite、Header Rewrite、Body Rewrite。
- YouTube、TikTok、Instagram、Facebook 等平台内嵌广告可能与正常内容共用域名，Android 规则不保证完全去除。

### 高风险场景

- 登录、支付、验证码、银行、微信、支付宝、Cookie、Token、会员权益相关链路默认应保持谨慎。
- 未经真机测试，不要把“规则覆盖存在”理解成“已经验证通过”。

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
| `Android/` | Android 可用规则和配置 |
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
[health-report]: reports/repository_health_report.md
