<div align="center">

# GrandpaNiu

### ✨ Shadowrocket / Surge 自用融合净化模块

**一个入口 · 常用 App / 网页广告净化 · Spotify / YouTube 重点保护 · 自动维护 · 可回滚**

本仓库以 `Ronghemokuai.sgmodule` 作为主模块入口，目标是把广告净化、播放保护、脚本规则、远程规则源和日常维护集中到一个清晰可管理的模块里。

<br>

[![安装模块](https://img.shields.io/static/v1?label=安装模块&message=立即导入&color=0A84FF&labelColor=111827&logo=rocket&logoColor=white&style=for-the-badge)](https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2FGrandpaNiuu%2FGrandpaNiu%2Fmain%2FRonghemokuai.sgmodule)
[![备用页面](https://img.shields.io/static/v1?label=备用页面&message=复制导入&color=34C759&labelColor=111827&logo=safari&logoColor=white&style=for-the-badge)](https://grandpaniuu.github.io/GrandpaNiu/import.html)

<br>

![Shadowrocket](https://img.shields.io/badge/Shadowrocket-支持-0A84FF?style=flat-square)
![Surge](https://img.shields.io/badge/Surge-兼容-5856D6?style=flat-square)
![Spotify](https://img.shields.io/badge/Spotify-重点保护-1DB954?style=flat-square)
![YouTube](https://img.shields.io/badge/YouTube-增强保留-FF3B30?style=flat-square)
![Auto](https://img.shields.io/badge/自动维护-启用-F59E0B?style=flat-square)
![Safe](https://img.shields.io/badge/安全边界-不做破解-6B7280?style=flat-square)

</div>

---

## 🚀 快速导入

| 入口 | 说明 |
|---|---|
| [安装模块](https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2FGrandpaNiuu%2FGrandpaNiu%2Fmain%2FRonghemokuai.sgmodule) | 推荐入口，点击后自动跳转 Shadowrocket 导入 |
| [备用导入页面](https://grandpaniuu.github.io/GrandpaNiu/import.html) | 无法自动跳转时使用，复制模块地址手动导入 |
| [Raw 模块地址](https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Ronghemokuai.sgmodule) | GitHub Raw 原始文件地址 |
| [GitHub Pages 模块地址](https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule) | Pages 加速访问地址，也是模块 update-url 指向地址 |

导入后建议在 Shadowrocket 中执行一次：更新模块、更新脚本、更新全部。

---

## 📌 模块定位

GrandpaNiu 是一个面向 Shadowrocket / Surge 兼容使用的融合净化模块。它不是单一广告规则，也不是单一脚本模块，而是把多个层面的能力整合在一个入口里。

它主要做这些事：

- 拦截常见广告域名、广告 SDK、追踪统计请求。
- 清理部分 App 的开屏广告、弹窗、横幅、信息流、推荐位、活动卡片。
- 保留 Spotify 播放链路保护，降低跳歌、秒切、加载失败概率。
- 保留 YouTube Enhance 相关逻辑，维持 YouTube 增强能力。
- 使用远程规则、本地规则、Rewrite、Script、Map Local、MITM 共同处理。
- 用 GitHub Actions 做每日检查、失效源审计、历史记录和稳定备份辅助。

---

## ✨ 核心功能

### 1. 通用广告净化

用于处理网页和 App 中常见的广告请求、追踪统计、广告 SDK、活动位、推荐位和信息流广告。

包含能力：

```text
DOMAIN / DOMAIN-SUFFIX / DOMAIN-KEYWORD
IP-CIDR
URL-REGEX
RULE-SET / DOMAIN-SET
REJECT / REJECT-DROP / DIRECT
```

主要覆盖：

```text
网页广告
App 开屏广告
弹窗广告
横幅广告
信息流广告
推荐位
活动卡片
广告 SDK
统计追踪请求
```

### 2. Spotify 重点保护

Spotify 是模块里的重点保护对象。相关规则优先保证播放链路稳定，避免被综合广告规则误伤。

保留内容：

```text
Spotify DIRECT 白名单
spotify-json
spotify-proto
Header Rewrite
spclient.wg.spotify.com
*.spclient.spotify.com
Spotify 必要 MITM hostname
```

处理目标：

```text
降低跳歌
降低歌曲秒切
降低接口误杀
保留播放链路
避免重复脚本冲突
```

### 3. YouTube Enhance 保留

YouTube 相关功能以保留增强逻辑和稳定播放为主，不盲目删除核心脚本。

保留内容：

```text
youtube.response
YouTube Enhance 参数
YouTube 必要 MITM hostname
Shorts / 字幕 / 歌词 / 翻译相关能力
```

如果出现视频转圈，优先排查 YouTube 相关 Map Local、googlevideo 规则和网络环境，不直接删除整个 YouTube 逻辑。

### 4. 常用 App 净化

模块覆盖方向包括但不限于：

| 分类 | 覆盖方向 |
|---|---|
| 音乐类 | Spotify、QQ 音乐、网易云、喜马拉雅等 |
| 视频类 | YouTube、Bilibili、爱奇艺、优酷、芒果 TV 等 |
| 社交类 | 小红书、微博、知乎、Soul、LINE 等 |
| 电商类 | 淘宝 / 闲鱼、京东、拼多多、美团 / 饿了么等 |
| 工具类 | WPS、高德地图、网盘、天气类 App 等 |
| 网页类 | 通用网页广告、统计、追踪、广告 SDK |

更详细覆盖状态见：[功能覆盖清单](docs/COVERAGE.md)。

### 5. Rewrite / Script / MITM 组合处理

本模块不是只靠规则拦截，也会结合重写、脚本和 MITM 做更精细的净化。

| 区块 | 作用 |
|---|---|
| `[Rule]` | 域名、IP、URL、远程规则源、白名单和拦截规则 |
| `[URL Rewrite]` | URL 层广告接口重写和拦截 |
| `[Header Rewrite]` | Header 层处理，例如 Spotify 缓存头处理 |
| `[Body Rewrite]` | 响应体字段清理，处理广告位、弹窗、活动卡片 |
| `[Map Local]` | 本地空响应、本地替换响应 |
| `[Script]` | Spotify、YouTube、App 净化脚本 |
| `[MITM]` | 追加必要 hostname，支持 HTTPS 解密处理 |

MITM 使用 `%APPEND%` 追加方式，尽量保留你已有配置，减少覆盖风险。

---

## 🧪 维护入口

| 类型 | 入口 | 用途 |
|---|---|---|
| 每日检查 | [daily_update_report.md](reports/daily_update_report.md) | 查看每日基础检查结果 |
| 失效源审计 | [invalid_sources_report.md](reports/invalid_sources_report.md) | 查看失效链接、可疑链接、处理结果 |
| 失效历史 | [invalid_sources_history.json](reports/invalid_sources_history.json) | 记录连续失败次数和历史状态 |
| 基础工作流 | [daily-module-update.yml](.github/workflows/daily-module-update.yml) | 每日更新日期并生成基础检查报告 |
| 修复工作流 | [daily-invalid-source-repair.yml](.github/workflows/daily-invalid-source-repair.yml) | 连续 2 天确认失效后安全处理 |
| 安全整理报告 | [module_refine_report.md](reports/module_refine_report.md) | 查看模块整理、脚本融合、重复项验证 |
| 维护说明 | [MAINTENANCE.md](docs/MAINTENANCE.md) | 日常维护、每周维护、每月维护说明 |
| 问题排查 | [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | Spotify、YouTube、登录支付异常排查 |
| 覆盖清单 | [COVERAGE.md](docs/COVERAGE.md) | 查看功能覆盖方向和待补充项 |
| 项目范围 | [SCOPE.md](docs/SCOPE.md) | 查看允许和禁止加入的内容范围 |
| 变更记录 | [CHANGELOG.md](CHANGELOG.md) | 查看仓库主要变更历史 |
| 稳定备份 | [backup/README.md](backup/README.md) | 查看稳定备份和回滚说明 |

---

## 🔄 自动维护机制

### 每日基础检查

工作流：[daily-module-update.yml](.github/workflows/daily-module-update.yml)

它负责：

- 更新模块日期。
- 检查 `[Rule]`、`[Script]`、`[MITM]` 是否存在。
- 检查 `spotify-json`、`spotify-proto`、`youtube.response` 是否存在。
- 检查主要远程链接状态。
- 生成每日检查报告。

### 每日失效源审计

工作流：[daily-invalid-source-repair.yml](.github/workflows/daily-invalid-source-repair.yml)

它负责：

- 扫描 `script-path`、`RULE-SET`、`DOMAIN-SET`、`update-url`、GitHub raw 链接。
- 记录失效历史。
- 连续 2 天确认失败后才处理。
- 优先替换可靠新地址。
- 找不到可靠新地址时才注释。
- 只有低风险独立远程规则才允许删除。

保护项不会自动破坏：

```text
Spotify
YouTube
主模块 update-url
GitHub Pages 模块地址
安装页面
导入页面
核心远程规则源
```

---

## 🛡️ 安全边界

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
YouTube 增强保留
远程规则安全维护
```

本仓库不做：

```text
会员破解
Premium 解锁
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
```

---

## 🧯 常见问题定位

| 问题 | 优先检查 |
|---|---|
| Spotify 跳歌 | Spotify 白名单、`spotify-json`、`spotify-proto`、MITM hostname、是否启用其他 Spotify 模块 |
| YouTube 转圈 | `youtube.response`、YouTube Enhance、googlevideo / Map Local 相关规则 |
| 登录异常 | 临时关闭模块确认是否误伤，再检查最近新增规则 |
| 支付 / 验证码异常 | 优先检查 MITM 和最近新增的 Rewrite / Map Local |
| 远程链接失败 | 先看报告是否连续失败，不因单日 GitHub 网络错误直接删除 |

完整排查见：[问题排查说明](docs/TROUBLESHOOTING.md)。

---

## 📌 维护原则

- 一个模块入口，减少重复导入。
- 稳定优先，不盲目堆规则。
- 新增规则按功能小步提交。
- Spotify / YouTube 优先保护。
- 登录、支付、验证码相关接口优先避免误伤。
- 失效链接先记录，再确认，再处理。
- 所有自动操作必须可回滚。

---

<div align="center">

**GrandpaNiu · Clean Module Hub ⚡**

干净、稳定、清楚、可维护。

</div>
