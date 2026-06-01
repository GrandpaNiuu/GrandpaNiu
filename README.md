<div align="center">

# GrandpaNiu

一个面向 Shadowrocket 的去广告与 App 净化模块工厂

[![Release](https://img.shields.io/github/v/release/GrandpaNiuu/GrandpaNiu?style=for-the-badge&labelColor=111827)](https://github.com/GrandpaNiuu/GrandpaNiu/releases)
[![License](https://img.shields.io/github/license/GrandpaNiuu/GrandpaNiu?style=for-the-badge&labelColor=111827)](LICENSE)
[![Module](https://img.shields.io/static/v1?label=Module&message=Stable&color=34C759&labelColor=111827&style=for-the-badge)](https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule)
[![Stars](https://img.shields.io/github/stars/GrandpaNiuu/GrandpaNiu?style=for-the-badge&labelColor=111827)](https://github.com/GrandpaNiuu/GrandpaNiu/stargazers)

GrandpaNiu 是一个面向 Shadowrocket 的模块工厂，目标是用更少配置获得更强的广告净化体验。

[安装与订阅](#安装与订阅) · [核心特性](#核心特性) · [版本说明](#版本说明) · [使用方法](#使用方法) · [维护与报告](#维护与报告)

</div>

---

## 项目简介

GrandpaNiu 采用 source-first 结构维护规则、脚本、MITM 与 Profile，并自动生成可直接导入的多版本模块。

- Shadowrocket / Surge 风格模块工厂
- 自动构建 `Ronghemokuai.sgmodule`
- 支持 Stable / Stable Plus / Lite / Full 多版本
- 默认 Stable 已启用激进广告源
- 用于国内外 App、网页广告、信息流、启动页、统计域名等净化

---

## 安装与订阅

| 版本 | 适合谁 | 说明 | 链接 |
|---|---|---|---|
| Stable | 日常使用 | 默认正式版，已启用激进去广告 | [导入](https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule) |
| Stable 独立版 | 固定 Release 路径 | 与默认 Stable 同类用途 | [导入](https://grandpaniuu.github.io/GrandpaNiu/Release/Ronghemokuai-stable.sgmodule) |
| Stable Plus | 增强覆盖测试 | 常用 App 增强测试 | [导入](https://grandpaniuu.github.io/GrandpaNiu/Release/Ronghemokuai-stable-plus.sgmodule) |
| Lite | 低耗电 / 低干扰 | 低风险、低覆盖、便于排查 | [导入](https://grandpaniuu.github.io/GrandpaNiu/Release/Ronghemokuai-lite.sgmodule) |
| Full | 全量排查 | 不建议长期启用 | [导入](https://grandpaniuu.github.io/GrandpaNiu/Release/Ronghemokuai-full.sgmodule) |

> 日常使用 Stable。不要同时启用多个版本。

---

## 核心特性

- 自动构建模块
- 自动同步根目录模块
- 多版本输出
- 国内外广告规则
- App 专项净化
- YouTube / Spotify / Zhihu 核心入口保留
- 激进广告源已接入默认 Stable
- 支持回滚与报告审计

---

## 版本说明

| Profile | 用途 | 默认发布 | 风险 |
|---|---|---|---|
| Stable | 日常正式版，已启用激进去广告 | 是 | 中 |
| Stable Plus | 常用 App 增强测试 | 否 | 中高 |
| Lite | 低耗电 / 低干扰 | 否 | 低 |
| Full | 全量排查 | 否 | 高 |

---

## 使用方法

1. 打开 Shadowrocket。
2. 进入「模块」。
3. 新建模块。
4. 粘贴订阅链接。
5. 更新模块、更新脚本、更新资源。
6. 只启用一个版本，不要多个版本同时启用。

---

## 注意事项

- 默认 Stable 现在是强力去广告模式。
- 可能误伤图片、视频、验证码、活动页、支付前置。
- 遇到问题优先反馈 App、页面、可疑域名。
- 不建议同时启用多个模块版本。
- Full 不建议长期启用。

---

## 维护与报告

维护细节放在 `docs/` 和 `reports/`，首页不展开。

- [docs/](docs/)
- [仓库健康报告](reports/repository_health_report.md)
- [多版本发布报告](reports/multi_release_report.md)
- [REJECT 风险审计](reports/reject_risk_report.md)
- [激进 Stable 广告源报告](reports/aggressive_stable_ad_sources_report.md)

---

## 许可证

本项目使用 [GPL-3.0](LICENSE) 许可证。
