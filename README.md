<div align="center">

# GrandpaNiu

### ✨ Shadowrocket / Surge 自用融合净化模块

一个入口，集中维护广告净化、Spotify、YouTube 与常用 App 规则。  
目标是 **干净、稳定、好用、可长期维护**。

<br>

[![安装模块](https://img.shields.io/static/v1?label=安装模块&message=立即导入&color=0A84FF&labelColor=111827&logo=rocket&logoColor=white&style=for-the-badge)](https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2FGrandpaNiuu%2FGrandpaNiu%2Fmain%2FRonghemokuai.sgmodule)
[![备用页面](https://img.shields.io/static/v1?label=备用页面&message=复制导入&color=34C759&labelColor=111827&logo=safari&logoColor=white&style=for-the-badge)](https://grandpaniuu.github.io/GrandpaNiu/import.html)

<br>

![Shadowrocket](https://img.shields.io/badge/Shadowrocket-支持-0A84FF?style=flat-square)
![Surge](https://img.shields.io/badge/Surge-兼容-5856D6?style=flat-square)
![Spotify](https://img.shields.io/badge/Spotify-已集成-1DB954?style=flat-square)
![YouTube](https://img.shields.io/badge/YouTube-增强-FF3B30?style=flat-square)
![Auto](https://img.shields.io/badge/自动维护-启用-F59E0B?style=flat-square)

</div>

---

## 🚀 立即使用

**推荐：** 点击顶部 `安装模块`，自动跳转 Shadowrocket 导入。  
**备用：** 如果 GitHub App 无法唤起 Shadowrocket，打开 `备用页面` 复制导入。

<details>
<summary>展开模块地址</summary>

```text
Raw 地址：
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Ronghemokuai.sgmodule

GitHub Pages 地址：
https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule
```

</details>

---

## ✨ 这个模块解决什么

> **一个模块集中生效**  
> 尽量减少多个模块叠加造成的重复、冲突、误杀和维护负担。

> **Spotify / YouTube 优先保护**  
> 保留 Spotify 播放链路、`spotify-json`、`spotify-proto`、YouTube Enhance 和必要 MITM。

> **广告净化覆盖常用场景**  
> 覆盖开屏广告、弹窗、横幅、信息流、推荐位、活动卡片、网页广告和部分广告 SDK。

> **自动维护更省心**  
> 每日基础检查、失效源审计、失效历史记录、连续 2 天失效后的安全处理、稳定备份。

---

## 🧩 模块能力

**规则层**  
远程规则、本地补充规则、DIRECT 白名单、REJECT 规则、URL-REGEX。

**重写层**  
URL Rewrite、Header Rewrite、Body Rewrite、Map Local。

**脚本层**  
Spotify、YouTube、常用 App 净化脚本和远程脚本检查。

**维护层**  
每日检查、失效源报告、历史记录、稳定备份、问题排查文档。

更多细节见：[功能覆盖清单](docs/COVERAGE.md)。

---

## 🧪 维护中心

- [每日检查报告](reports/daily_update_report.md)
- [每日失效源审计报告](reports/invalid_sources_report.md)
- [失效源历史记录](reports/invalid_sources_history.json)
- [每日失效源修复工作流](.github/workflows/daily-invalid-source-repair.yml)
- [模块安全整理报告](reports/module_refine_report.md)
- [维护说明](docs/MAINTENANCE.md)
- [问题排查](docs/TROUBLESHOOTING.md)
- [功能覆盖清单](docs/COVERAGE.md)
- [项目范围说明](docs/SCOPE.md)
- [变更记录](CHANGELOG.md)
- [稳定备份说明](backup/README.md)

<details>
<summary>展开自动维护说明</summary>

```text
基础自动更新工作流：
.github/workflows/daily-module-update.yml

失效源修复工作流：
.github/workflows/daily-invalid-source-repair.yml
```

失效源不会因为单日网络错误直接删除。连续 2 天确认失败后，优先替换，其次注释，最后才低风险删除。Spotify、YouTube、主模块地址、安装页和核心远程规则源优先人工确认。

</details>

---

## 🛡️ 安全边界

本仓库只做 **广告净化 / 稳定增强 / 规则维护**。

不做：会员破解、Premium 解锁、支付绕过、登录绕过、账户权益伪造、证书绕过、Cookie / BoxJS 任务、成人内容、博彩内容、灰产内容、短链脚本、未知混淆脚本。

---

## 📱 使用建议

1. 先确认 iPhone 已安装 Shadowrocket。
2. 点击顶部 **安装模块**。
3. 跳转到 Shadowrocket 后确认导入。
4. 在 Shadowrocket 内更新模块和脚本。
5. 如果无法自动跳转，使用备用页面复制导入。

---

<div align="center">

**GrandpaNiu · Clean Module Hub ⚡**

</div>
