<div align="center">

# GrandpaNiu

### ✨ Shadowrocket / Surge 自用融合净化模块

**一个入口 · 全局净化 · 重点保护 Spotify / YouTube · 自动维护 · 可回滚**

本仓库以 `Ronghemokuai.sgmodule` 作为唯一主模块入口，集中处理常用 App 与网页中的广告、弹窗、横幅、信息流、推荐位、活动卡片，并保留 Spotify / YouTube 等重点功能的稳定增强逻辑。

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

## 🧭 一眼看懂

```text
GrandpaNiu
├─ 一个主模块：Ronghemokuai.sgmodule
├─ 一个导入入口：Shadowrocket / Surge 兼容
├─ 一套广告净化：远程规则 + 本地规则 + Rewrite + Script + MITM
├─ 两个重点保护：Spotify / YouTube
├─ 一个维护系统：每日检查 + 失效源审计 + 稳定备份
└─ 一个安全边界：只做广告净化，不做破解、支付绕过、登录绕过
```

这个仓库的目标不是单纯堆规则，而是把常用的去广告、净化、增强、维护能力整理成一个更稳定、更清楚、更容易回滚的融合模块。

---

## 🚀 快速导入

推荐直接点击顶部 **安装模块** 按钮。无法自动跳转时，使用备用页面复制导入。

```text
Raw 模块地址：
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Ronghemokuai.sgmodule

GitHub Pages 地址：
https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule
```

使用顺序：

```text
1. iPhone 安装 Shadowrocket
2. 点击“安装模块”
3. 确认导入 Ronghemokuai.sgmodule
4. 在 Shadowrocket 内更新模块和脚本
5. 只启用本模块测试 Spotify / YouTube / 常用 App
```

---

## ✨ 模块核心能力

### 1. 通用广告净化

用于处理常见广告域名、广告 SDK、网页广告、追踪统计和部分 App 广告请求。

主要包含：

- 远程广告规则源
- 本地域名拦截规则
- URL-REGEX 规则
- REJECT / REJECT-DROP / DIRECT 规则
- 常见广告、统计、追踪域名补充

适用场景：

```text
网页广告
App 开屏广告
弹窗广告
横幅广告
信息流广告
推荐位
活动卡片
部分广告 SDK 请求
```

### 2. Spotify 重点保护

Spotify 是本模块重点保护对象，目标是尽量避免跳歌、秒切、播放失败、页面加载异常。

保留内容包括：

- Spotify 播放链路白名单
- `spotify-json`
- `spotify-proto`
- Header Rewrite
- `spclient.wg.spotify.com`
- `*.spclient.spotify.com`
- Spotify 相关 MITM hostname

设计原则：

```text
Spotify 播放链路优先 DIRECT
避免远程广告规则误杀播放请求
不随意删除 spotify-json / spotify-proto
如果出现跳歌，优先排查冲突规则
```

### 3. YouTube Enhance 保留

YouTube 相关逻辑保留增强能力，同时尽量降低转圈、加载慢、接口误杀风险。

主要包含：

- YouTube Enhance 脚本
- `youtube.response`
- Shorts / 字幕 / 歌词 / 翻译等参数支持
- YouTube 必要 MITM hostname
- YouTube 相关接口净化规则

注意：如果出现视频转圈，应优先检查 YouTube 相关 Map Local / googlevideo 规则，不要直接删除整个 YouTube Enhance。

### 4. 常用 App 净化

模块包含部分国内外常用 App 的净化规则，主要面向广告、弹窗、活动位和推荐位，不处理账号权益和支付逻辑。

覆盖方向：

```text
音乐类：Spotify、QQ 音乐、网易云、喜马拉雅等
视频类：YouTube、Bilibili、爱奇艺、优酷、芒果 TV 等
社交类：小红书、微博、知乎、Soul、LINE 等
电商类：淘宝 / 闲鱼、京东、拼多多、美团 / 饿了么等
工具类：WPS、高德地图、网盘、天气类 App 等
网页类：通用网页广告、统计、追踪、广告 SDK
```

更详细覆盖状态见：[功能覆盖清单](docs/COVERAGE.md)。

### 5. Rewrite / Script / MITM 组合处理

模块不是只有规则，也包含必要的重写和脚本处理能力。

```text
[URL Rewrite]     URL 层广告接口拦截
[Header Rewrite]  Header 层缓存 / 请求头处理
[Body Rewrite]    响应体字段清理
[Map Local]       本地空响应 / 替换响应
[Script]          远程脚本与 App 净化脚本
[MITM]            追加必要 hostname 解密支持
```

MITM 使用 `%APPEND%` 追加方式，尽量保留你本机其他模块或配置里的 hostname。

---

## 🧱 模块结构

```text
Ronghemokuai.sgmodule
├─ [Rule]
│  ├─ Spotify / YouTube 白名单保护
│  ├─ 远程广告规则集
│  ├─ 本地域名与 URL 规则
│  └─ 低风险补充拦截规则
│
├─ [URL Rewrite]
│  └─ 广告接口、开屏接口、弹窗接口处理
│
├─ [Header Rewrite]
│  └─ Spotify 等重点接口 Header 处理
│
├─ [Body Rewrite]
│  └─ 响应体广告字段、活动位、推荐位清理
│
├─ [Map Local]
│  └─ 空响应、占位响应、本地替换
│
├─ [Script]
│  ├─ Spotify
│  ├─ YouTube
│  └─ 常用 App 净化脚本
│
└─ [MITM]
   └─ 使用 %APPEND% 追加必要 hostname
```

---

## 🔄 自动维护机制

仓库内置维护体系，目标是让模块长期可用、可查、可回滚。

### 每日基础检查

```text
.github/workflows/daily-module-update.yml
```

作用：

- 更新模块日期
- 检查 `[Rule]`、`[Script]`、`[MITM]`
- 检查 Spotify / YouTube 核心项是否存在
- 检查主要远程链接
- 生成每日检查报告

### 每日失效源审计

```text
.github/workflows/daily-invalid-source-repair.yml
```

作用：

- 扫描 `script-path`、`RULE-SET`、`DOMAIN-SET`、`update-url`、GitHub raw 链接
- 记录失效历史
- 连续 2 天确认失败后才处理
- 优先替换可靠新地址
- 找不到可靠新地址时才注释
- 只有低风险独立远程规则才允许删除

保护项：

```text
Spotify
YouTube
主模块 update-url
GitHub Pages 模块地址
安装页面
导入页面
核心远程规则源
```

这些内容即使检查失败，也优先写入报告，不自动破坏模块。

---

## 🧪 维护入口

```text
reports/daily_update_report.md              每日基础检查报告
reports/invalid_sources_report.md           每日失效源审计报告
reports/invalid_sources_history.json        失效源历史记录
reports/module_refine_report.md             模块安全整理报告
docs/MAINTENANCE.md                         日常维护说明
docs/TROUBLESHOOTING.md                     问题排查说明
docs/COVERAGE.md                            功能覆盖清单
docs/SCOPE.md                               项目范围说明
CHANGELOG.md                                变更记录
backup/README.md                            稳定备份说明
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

```text
Spotify 跳歌：
优先检查 Spotify 白名单、spotify-json、spotify-proto、MITM hostname、其他模块冲突。

YouTube 转圈：
优先检查 YouTube Enhance、youtube.response、googlevideo / Map Local 相关规则。

登录 / 支付 / 验证码异常：
优先临时关闭模块确认是否误伤，再定位最近新增规则，不要直接大面积删除。

远程链接失败：
先看报告，确认是否连续失败。不要因单日 GitHub 网络问题直接删除规则。
```

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
