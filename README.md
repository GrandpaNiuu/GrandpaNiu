<div align="center">

# GrandpaNiu

Shadowrocket / Surge 自用融合净化模块  
一个入口，集中维护广告净化、Spotify、YouTube 和常用 App 规则。

[![安装模块](https://img.shields.io/static/v1?label=安装模块&message=GrandpaNiu&color=grey&logo=educative&logoColor=white&labelColor=blue&messageColor=white)](https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2FGrandpaNiuu%2FGrandpaNiu%2Fmain%2FRonghemokuai.sgmodule "一键安装本模块")
[![备用页面](https://img.shields.io/static/v1?label=备用页面&message=复制导入&color=grey&logo=safari&logoColor=white&labelColor=%2325A162&messageColor=white)](https://grandpaniuu.github.io/GrandpaNiu/import.html "备用导入页面")

</div>

---

## 快速入口

| 类型 | 地址 |
|---|---|
| 一键安装 | [打开 Shadowrocket 安装](https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2FGrandpaNiuu%2FGrandpaNiu%2Fmain%2FRonghemokuai.sgmodule) |
| 备用导入页 | [打开备用页面](https://grandpaniuu.github.io/GrandpaNiu/import.html) |
| Raw 模块地址 | `https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Ronghemokuai.sgmodule` |
| GitHub Pages 地址 | `https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule` |

---

## 模块功能

| 模块层 | 说明 |
|---|---|
| 远程规则 | blackmatrix7、Cats-Team、Remote AdBlock Hub 等可信规则源 |
| 本地规则 | 域名、IP、URL-REGEX、DIRECT 白名单和 REJECT 补充规则 |
| Spotify | 播放链路白名单、Header Rewrite、spotify-json、spotify-proto |
| YouTube | YouTube Enhance、Shorts / 字幕 / 歌词等参数控制 |
| App 净化 | 常用 App 的开屏广告、弹窗、横幅、信息流和活动位清理 |
| Body / Map Local | 清理接口返回、空响应、活动位和推荐位 |
| MITM | 使用 `%APPEND%` 追加必要 hostname，尽量保留其他配置 |
| 自动维护 | 每日检查、失效源审计、历史记录、稳定备份和回滚辅助 |

更多覆盖细节见：[功能覆盖清单](docs/COVERAGE.md)。

---

## 维护入口

| 分类 | 文件 |
|---|---|
| 每日检查 | [daily_update_report.md](reports/daily_update_report.md) |
| 失效源审计 | [invalid_sources_report.md](reports/invalid_sources_report.md) |
| 失效源历史 | [invalid_sources_history.json](reports/invalid_sources_history.json) |
| 失效源修复工作流 | [daily-invalid-source-repair.yml](.github/workflows/daily-invalid-source-repair.yml) |
| 基础更新工作流 | `.github/workflows/daily-module-update.yml` |
| 安全整理报告 | [module_refine_report.md](reports/module_refine_report.md) |
| 维护说明 | [MAINTENANCE.md](docs/MAINTENANCE.md) |
| 问题排查 | [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) |
| 项目范围 | [SCOPE.md](docs/SCOPE.md) |
| 变更记录 | [CHANGELOG.md](CHANGELOG.md) |
| 稳定备份 | [backup/README.md](backup/README.md) |

---

## 维护原则

- 正常使用时只更新模块和脚本，不频繁修改仓库。
- 新增规则按 App 或功能类别小步提交，观察稳定后再继续。
- 失效源不会因单日网络失败直接删除；连续 2 天确认失败后，优先替换，其次注释，最后才低风险删除。
- Spotify、YouTube、主模块地址、安装页和核心远程规则源只写入报告，等待人工确认。

---

## 安全边界

本仓库只做广告净化和稳定增强，不做会员破解、Premium 解锁、支付绕过、登录绕过、证书绕过、账户权益伪造、Cookie 任务、成人内容、博彩内容、灰产内容、短链脚本和未知混淆脚本。

---

## 使用建议

1. iPhone 安装 Shadowrocket。
2. 点击顶部“安装模块”按钮。
3. 跳转后确认添加模块。
4. 在 Shadowrocket 内更新模块和脚本。
5. 若无法自动跳转，使用备用导入页复制模块地址手动导入。

---

<div align="center">

Made for Shadowrocket ⚡

</div>
