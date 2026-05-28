<div align="center">

# GrandpaNiu

Shadowrocket 自用模块合集  
一键跳转 Shadowrocket 安装模块 🚀

[![安装模块 GrandpaNiu](https://img.shields.io/static/v1?label=安装模块&message=GrandpaNiu&color=grey&logo=educative&logoColor=white&labelColor=blue&messageColor=white)](https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2FGrandpaNiuu%2FGrandpaNiu%2Fmain%2FRonghemokuai.sgmodule "一键安装本模块")
[![备用页面](https://img.shields.io/static/v1?label=备用页面&message=复制导入&color=grey&logo=safari&logoColor=white&labelColor=%2325A162&messageColor=white)](https://grandpaniuu.github.io/GrandpaNiu/import.html "备用导入页面")

</div>

---

## 📦 模块导入

### 🚀 推荐方式：一键自动安装

点击下面按钮，会先打开 GitHub Pages 跳转页，再自动唤起 Shadowrocket 安装模块：

[![安装模块 GrandpaNiu](https://img.shields.io/static/v1?label=安装模块&message=GrandpaNiu&color=grey&logo=educative&logoColor=white&labelColor=blue&messageColor=white)](https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2FGrandpaNiuu%2FGrandpaNiu%2Fmain%2FRonghemokuai.sgmodule "一键安装本模块")

### 🧩 备用方式：打开导入页面

如果 GitHub App 内无法直接唤起 Shadowrocket，请使用 Safari 打开备用页面：

[🚀 打开备用导入页面](https://grandpaniuu.github.io/GrandpaNiu/import.html)

---

## 🔗 模块地址

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Ronghemokuai.sgmodule
```

GitHub Pages 地址：

```text
https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule
```

---

## 🧩 模块功能

本模块是面向 Shadowrocket / Surge 兼容使用的自用融合净化模块，目标是一个模块集中处理常用 App 和网页的广告、弹窗、横幅、信息流、推荐位和活动卡片。

### 核心能力

- 通用广告域名拦截：接入 blackmatrix7 Advertising.list、Cats-Team AdRules、Remote AdBlock Hub 等远程规则源。
- 本地补充规则：包含本地域名、IP、URL-REGEX、DIRECT 白名单和 REJECT 规则。
- App 广告净化：覆盖部分国内常用 App 的开屏广告、弹窗、横幅、信息流、推荐位和活动卡片。
- 网页广告净化：补充通用网页广告、追踪统计和常见广告 SDK 域名拦截。
- Spotify 处理：保留 Spotify 播放链路白名单、Header Rewrite、spotify-json、spotify-proto 和必要 MITM hostname，降低跳歌和误杀概率。
- YouTube Enhance：保留 YouTube 增强逻辑，支持上传按钮、选段按钮、Shorts、字幕翻译、歌词翻译等参数控制。
- Body Rewrite / Map Local：用于清理部分接口返回中的广告、弹窗、活动位、推荐位和空响应。
- MITM 支持：使用 `%APPEND%` 追加必要 hostname，尽量保留用户其他模块的 MITM 配置。
- 自动维护：每日基础检查、每日失效源审计、连续 2 天失效后的安全处理、失效历史记录和稳定备份。

### 覆盖方向

| 分类 | 覆盖状态 | 说明 |
|---|---|---|
| 音乐类 | 部分覆盖 | Spotify 已覆盖；QQ 音乐、网易云音乐、喜马拉雅为部分覆盖；酷狗音乐待补充。 |
| 视频类 | 部分覆盖 | YouTube 已覆盖；Bilibili、爱奇艺、优酷、芒果 TV、咪咕视频为部分覆盖。 |
| 社交类 | 部分覆盖 | 小红书、知乎、微博、Soul、LINE 为部分覆盖。 |
| 电商类 | 部分覆盖 | 淘宝 / 闲鱼、京东、拼多多、饿了么 / 美团、唯品会为部分覆盖。 |
| 工具类 | 部分覆盖 | WPS、高德地图、百度网盘 / 阿里云盘、墨迹天气为部分覆盖。 |
| 网页广告 | 已覆盖 / 部分覆盖 | 通用广告域名已覆盖；弹窗、横幅、信息流、追踪统计为部分覆盖。 |
| 远程规则 | 已覆盖 | blackmatrix7、Cats-Team、Remote AdBlock Hub 和本地补充规则。 |
| Spotify | 已覆盖 | 播放保护、脚本处理、核心链路白名单。 |
| YouTube | 已覆盖 | YouTube Enhance、字幕 / 歌词翻译参数、必要脚本。 |
| MITM | 已覆盖 | 必要 hostname 追加，使用 `%APPEND%` 保留其他配置。 |

### 安全边界

本模块只做广告净化和稳定增强，不做以下内容：

```text
会员破解
Premium 解锁
支付绕过
登录绕过
账户权益伪造
证书绕过
Cookie 签到任务
BoxJS 账号任务
成人内容
博彩内容
灰产内容
短链脚本
未知混淆脚本
```

---

## 🧪 维护状态

- [每日检查报告](reports/daily_update_report.md)
- [每日失效源审计报告](reports/invalid_sources_report.md)
- [失效源历史记录](reports/invalid_sources_history.json)
- [每日失效源修复工作流](.github/workflows/daily-invalid-source-repair.yml)
- [模块安全整理报告](reports/module_refine_report.md)
- [旧版精选迁移报告](reports/legacy_selected_migration_report.md)
- [维护说明](docs/MAINTENANCE.md)
- [问题排查](docs/TROUBLESHOOTING.md)
- [功能覆盖清单](docs/COVERAGE.md)
- [项目范围说明](docs/SCOPE.md)
- [变更记录](CHANGELOG.md)
- [稳定备份说明](backup/README.md)

每日自动更新工作流（基础检查，仅报告）：

```text
.github/workflows/daily-module-update.yml
```

说明：该基础工作流只更新日期、检查关键结构、检查主要远程链接并生成报告，不会自动删除规则、注释脚本或替换 Spotify / YouTube。

每日失效源修复工作流（连续 2 天确认失效后处理）：

```text
.github/workflows/daily-invalid-source-repair.yml
```

说明：失效源修复工作流不会因为单日网络失败修改规则；连续 2 天确认失效后，优先查找同源可靠新地址并替换，找不到可靠新地址时才注释，只有低风险独立远程规则才允许删除。Spotify、YouTube、主模块地址、安装/导入页面和核心远程规则源只写入报告，等待人工确认。

---

## 📱 使用说明

1. 确保 iPhone 已安装 Shadowrocket
2. 推荐在 Safari 或 GitHub App 中点击“安装模块”按钮
3. 跳转到 Shadowrocket 后确认添加模块
4. 在模块列表中启用即可
5. 如果没有自动跳转，请打开备用页面后复制模块地址手动导入

---

## 🛠️ 日常维护

1. 在 Shadowrocket 里更新模块和脚本
2. 查看每日检查报告是否有远程链接失败
3. 测试 Spotify、YouTube、登录、支付、验证码
4. 无异常时不要修改仓库
5. 新增规则时按 App 或功能类别小步提交

---

<div align="center">

Made for Shadowrocket ⚡

</div>
