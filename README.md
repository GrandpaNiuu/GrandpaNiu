<div align="center">

# GrandpaNiu

### Shadowrocket / Surge 自用融合净化模块工厂

一个入口，集中维护 App 去广告、网页广告过滤、Spotify 播放保护、YouTube Enhance、知乎增强净化、远程规则源、自动构建、失效源审计、性能说明和回滚报告。

<br>

[![安装模块](https://img.shields.io/static/v1?label=安装模块&message=Shadowrocket&color=0A84FF&labelColor=111827&logo=rocket&logoColor=white&style=for-the-badge)](https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2FGrandpaNiuu%2FGrandpaNiu%2Fmain%2FRonghemokuai.sgmodule)
[![备用页面](https://img.shields.io/static/v1?label=备用页面&message=复制导入&color=34C759&labelColor=111827&logo=safari&logoColor=white&style=for-the-badge)](https://grandpaniuu.github.io/GrandpaNiu/import.html)

<br>

![Shadowrocket](https://img.shields.io/badge/Shadowrocket-支持-0A84FF?style=flat-square)
![Surge](https://img.shields.io/badge/Surge-兼容-5856D6?style=flat-square)
![Spotify](https://img.shields.io/badge/Spotify-重点保护-1DB954?style=flat-square)
![YouTube](https://img.shields.io/badge/YouTube%20Enhance-保留-FF3B30?style=flat-square)
![Factory](https://img.shields.io/badge/源头驱动-模块工厂-F59E0B?style=flat-square)
![Safe](https://img.shields.io/badge/安全边界-不做破解-6B7280?style=flat-square)

</div>

---

## 快速导入

| 入口 | 用途 |
|---|---|
| [安装模块](https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2FGrandpaNiuu%2FGrandpaNiu%2Fmain%2FRonghemokuai.sgmodule) | 推荐入口，点击后跳转 Shadowrocket 导入 |
| [备用导入页面](https://grandpaniuu.github.io/GrandpaNiu/import.html) | 自动跳转失败时使用，复制模块地址手动导入 |
| [Raw 模块地址](https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Ronghemokuai.sgmodule) | GitHub 原始模块地址 |
| [Pages 模块地址](https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule) | 稳定访问地址，也是模块 `update-url` |

导入后建议在 Shadowrocket 中执行一次：更新模块、更新脚本、更新全部资源。

---

## 项目定位

GrandpaNiu 是一个面向 Shadowrocket / Surge 的自用融合净化模块。它不是单一规则，也不是单一脚本，而是通过规则、脚本、重写、本地映射、MITM、远程规则源和自动化报告组合维护的模块工厂。

根目录 `Ronghemokuai.sgmodule` 是最终导入结果，不是长期手工维护源头。日常维护优先修改 `Rules/`、`Scripts/`、`Rewrite/Sources/`、`Rewrite/Remotes/` 和 `Rewrite/Profiles/`，再由工厂流程生成并同步主模块。

---

## 模块工厂流程

```text
Profiles + Remotes + Rules + Scripts + Rewrite/Sources
        -> scripts/build_module.py --build --profile stable
        -> Release/Ronghemokuai.sgmodule
        -> scripts/factory_finalize.py --sync-root
        -> Ronghemokuai.sgmodule
```

| 层级 | 说明 |
|---|---|
| `Rewrite/Profiles/stable.conf` | 当前默认稳定构建配置 |
| `Rewrite/Profiles/lite.conf` | 低耗电参考配置，不默认发布 |
| `Rewrite/Remotes/sources.json` | 可信远程 `RULE-SET` / `DOMAIN-SET` 清单 |
| `Rewrite/Remotes/candidates.json` | 可信候选源池，不做全网乱搜 |
| `Rules/*.list` | 本地规则源，参与 `[Rule]` 构建 |
| `Scripts/*.conf` | 脚本源，参与 `[Script]` 构建 |
| `Rewrite/Sources/*.conf` | Meta、URL Rewrite、Header Rewrite、Body Rewrite、Map Local、MITM 片段 |
| `Release/Ronghemokuai.sgmodule` | 工厂生成副本 |
| `Ronghemokuai.sgmodule` | 正式导入入口，由 Release 同步得到 |

完整流程见：[模块工厂说明](docs/FACTORY_FLOW.md)。

---

## 核心能力

| 能力 | 说明 |
|---|---|
| 通用广告过滤 | 处理广告域名、广告 SDK、追踪统计、劫持域名、网页广告 |
| App 净化 | 处理开屏、弹窗、横幅、信息流、推荐位、活动卡片 |
| Spotify 保护 | DIRECT 白名单、Header Rewrite、`spotify-json`、`spotify-proto`、必要 MITM |
| YouTube Enhance | 保留 `youtube.response`，处理 YouTube 增强相关逻辑 |
| 知乎增强净化 | 处理知乎信息流、回答页、推荐广告、商业卡片，不碰会员/登录/付费 |
| Bilibili 局部净化 | 通过规则和 Map Local 处理活动、搜索、广告素材、PGC 活动物料等接口 |
| 远程规则源 | blackmatrix7、Cats-Team、anti-AD、ACL4SSR、Loyalsoldier、217heidai 等 |
| 自动维护 | 自动构建、自动同步、失效源审计、候选源收集、报告生成 |
| 性能维护 | 提供 `docs/PERFORMANCE.md` 和 `lite.conf` 低耗电参考配置 |

---

## 重点生效对象

说明：以下是当前模块中有明确规则、脚本、Body Rewrite、Map Local 或专项保护的重点对象。远程规则源还会额外覆盖大量广告域名和网页广告，不逐一列出。

| 分类 | App / 服务 |
|---|---|
| 专项保护 | Spotify、YouTube、知乎、Bilibili |
| 社区内容 | 微博、百度贴吧、小红书、酷安、小黑盒、脉脉、Reddit、飞客茶馆、盖得排行、Soul、皮皮虾 |
| 新闻资讯 | QQ 新闻 / 腾讯新闻、网易新闻、财新、IT之家、什么值得买、51CTO |
| 视频音乐 | 芒果 TV、人人视频、网易云音乐、咪咕视频、斗鱼、喜马拉雅、小宇宙 FM、快看漫画 |
| 电商生活 | 淘宝、闲鱼、京东、拼多多、盒马、菜鸟、美团、美团外卖、大众点评、饿了么、瑞幸、Cotti、Manner、朴朴、Lawson、途虎养车 |
| 出行地图 | 滴滴、12306、航旅纵横、高德地图、百度地图、飞猪、国航、吉祥航空、深圳通类 App |
| 阅读教育 | 起点、网易有道词典、问卷星、宝宝树、薄荷、Gaoding、51CTO |
| 工具其他 | 迅雷、转转、海尔、配音秀、360 摄像机、萤石云、搜狗输入法、韵达、Usmile、QBB6 |

覆盖强度大致分为三类：Spotify / YouTube / 知乎属于重点专项；微博、贴吧、小红书、淘宝、闲鱼、京东、美团、滴滴、高德等属于脚本或重写明确覆盖；Bilibili 当前属于局部净化，不是完整独立脚本模块。

---

## 维护入口

| 类型 | 入口 | 用途 |
|---|---|---|
| 工厂流程 | [docs/FACTORY_FLOW.md](docs/FACTORY_FLOW.md) | 查看源头驱动构建逻辑 |
| 工厂工作流 | [.github/workflows/module-factory-build.yml](.github/workflows/module-factory-build.yml) | 生成 Release 并同步主模块 |
| 工厂报告 | [reports/module_factory_report.md](reports/module_factory_report.md) | 查看构建 profile、来源、行数和重复检查 |
| 差异报告 | [reports/module_factory_diff_report.md](reports/module_factory_diff_report.md) | 查看 Root 与 Release 是否一致 |
| 同步报告 | [reports/factory_finalize_report.md](reports/factory_finalize_report.md) | 查看 Release 同步主模块结果 |
| 每日报告 | [reports/daily_update_report.md](reports/daily_update_report.md) | 查看每日结构和链接检查 |
| 失效源报告 | [reports/invalid_sources_report.md](reports/invalid_sources_report.md) | 查看失效链接审计和修复结果 |
| 失效源历史 | [reports/invalid_sources_history.json](reports/invalid_sources_history.json) | 记录连续失败次数 |
| 候选源池 | [Rewrite/Remotes/candidates.json](Rewrite/Remotes/candidates.json) | 可信候选规则源，禁止全网乱搜 |
| 候选源工作流 | [.github/workflows/upstream-collect.yml](.github/workflows/upstream-collect.yml) | 每周保守收集可信候选源 |
| 候选源报告 | [reports/upstream_collect_report.md](reports/upstream_collect_report.md) | 查看新增、跳过和待人工测试项 |
| 质量门禁 | [docs/QUALITY_GATE.md](docs/QUALITY_GATE.md) | 查看阻断项、提醒项和发布前必须通过的检查 |
| 发布回滚 | [docs/RELEASE.md](docs/RELEASE.md) | 查看正式发布、Shadowrocket 测试和回滚流程 |
| 健康工作流 | [.github/workflows/repository-health.yml](.github/workflows/repository-health.yml) | 每周或手动运行仓库健康检查 |
| 健康报告 | [reports/repository_health_report.md](reports/repository_health_report.md) | 查看阻断问题、提醒事项、缺失文件、重复脚本和验证输出 |
| 维护标准 | [docs/MAINTENANCE.md](docs/MAINTENANCE.md) | 日常维护规则和测试标准 |
| 性能说明 | [docs/PERFORMANCE.md](docs/PERFORMANCE.md) | 查看耗电来源、低耗电策略和 lite profile 用法 |
| 低耗电配置 | [Rewrite/Profiles/lite.conf](Rewrite/Profiles/lite.conf) | 低耗电参考 profile，不默认发布 |
| 问题排查 | [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | Spotify、YouTube、登录、支付、验证码排查 |
| 覆盖清单 | [docs/COVERAGE.md](docs/COVERAGE.md) | 查看功能覆盖状态 |
| 范围说明 | [docs/SCOPE.md](docs/SCOPE.md) | 查看允许和禁止加入的内容 |
| 变更记录 | [CHANGELOG.md](CHANGELOG.md) | 查看主要变更 |
| 稳定备份 | [backup/README.md](backup/README.md) | 查看备份和回滚说明 |

---

## 自动维护机制

### 模块工厂构建

工作流：[module-factory-build.yml](.github/workflows/module-factory-build.yml)

执行内容：编译脚本、从源头文件构建 Release、同步到根目录主模块、运行统一验证、必要时提交构建结果。`--extract-from-root` 只用于初始化或灾难恢复，不是日常构建路径。

### 每日基础检查

工作流：[daily-module-update.yml](.github/workflows/daily-module-update.yml)

执行内容：更新日期、检查关键区块、检查 Spotify / YouTube / update-url、检查主要远程链接并生成日报。

### 每日失效源审计

工作流：[daily-invalid-source-repair.yml](.github/workflows/daily-invalid-source-repair.yml)

执行内容：优先扫描并修复 `Rewrite/Remotes/`、`Rules/`、`Scripts/`、`Rewrite/Sources/` 中的外部链接。连续 2 天确认失败后才处理，Spotify、YouTube、安装页、导入页和 update-url 只报告，不自动破坏。

### 每周候选源收集

工作流：[upstream-collect.yml](.github/workflows/upstream-collect.yml)

执行内容：只读取 `Rewrite/Remotes/candidates.json`，不全网搜索。候选源必须来自可信仓库、格式明确、无风险关键词、无短链/镜像/代理，脚本默认保持 pending。

### 每周仓库健康检查

工作流：[repository-health.yml](.github/workflows/repository-health.yml)

执行内容：构建 stable、同步 Root、运行统一验证、生成仓库健康报告。用于确认当前仓库是否具备发布条件。

### 低耗电参考构建

默认正式构建仍使用：

```text
python3 scripts/build_module.py --build --profile stable
```

低耗电测试可使用：

```text
python3 scripts/build_module.py --build --profile lite
```

`lite.conf` 只作为测试和排查用，不建议未经 24 小时测试直接替代 stable。

---

## 安全边界

本仓库只做：

```text
广告拦截
开屏广告清理
弹窗清理
横幅清理
信息流净化
推荐位清理
活动卡片清理
网页广告净化
Spotify 播放保护
YouTube Enhance 保留
知乎广告卡片净化
远程规则安全维护
源头驱动模块构建
```

本仓库不做：

```text
会员解锁
Premium 破解
支付绕过
登录绕过
账户权益伪造
证书绕过
Cookie / BoxJS 账号任务
成人内容
博彩内容
灰产内容
短链脚本
未知混淆脚本
ghproxy / 镜像站正式源
来源不可验证脚本
```

---

## 常见问题

| 问题 | 优先检查 |
|---|---|
| Spotify 跳歌 | Spotify DIRECT、`spotify-json`、`spotify-proto`、Header Rewrite、`spclient.wg.spotify.com`、其他 Spotify 模块是否叠加 |
| YouTube 转圈 | `youtube.response`、YouTube MITM、Map Local 中的 googlevideo initplayback 规则、最近新增重写 |
| 知乎广告仍出现 | HTTPS 解密和证书、`zhihu-enhance` 是否已构建进模块、知乎是否杀后台重开 |
| Bilibili 仍有广告 | 当前只做局部净化，不是完整脚本模块；优先检查 Map Local 和相关 REJECT 规则 |
| 耗电偏高 | 查看 [docs/PERFORMANCE.md](docs/PERFORMANCE.md)，优先检查 MITM、Body Rewrite、知乎/YouTube 等高频脚本 |
| 登录异常 | 临时停用模块确认，再检查最近新增 Rules、Scripts、MITM、Rewrite |
| 支付 / 验证码异常 | 优先检查 MITM、URL Rewrite、Body Rewrite、Map Local |
| 远程源失败 | 查看报告是否连续失败，不因单日 GitHub 网络波动直接删除 |

更多说明见：[问题排查](docs/TROUBLESHOOTING.md)。

---

## 维护原则

```text
优先改源头文件，不直接长期手写主模块。
由工厂生成 Release，再同步到 Ronghemokuai.sgmodule。
Root 与 Release 必须保持一致。
Spotify、YouTube、知乎核心脚本优先保护。
脚本新增必须人工确认，不自动加入未知脚本。
远程规则优先替换，其次注释，最后才删除低风险独立规则。
所有自动化结果必须有报告，所有异常都要能回滚。
```

---

<div align="center">

**GrandpaNiu · Ronghemokuai.sgmodule**

干净、稳定、清楚、可维护。

</div>
