# 🐮 GrandpaNiu

<p align="center">
  <img src="https://img.shields.io/badge/Shadowrocket-Module-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Surge-sgmodule-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Android-Rules-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Auto%20Build-GitHub%20Actions-black?style=for-the-badge" />
</p>

<p align="center">
  <a href="https://github.com/GrandpaNiuu/GrandpaNiu/actions/workflows/daily-module-update.yml">
    <img src="https://github.com/GrandpaNiuu/GrandpaNiu/actions/workflows/daily-module-update.yml/badge.svg" />
  </a>
  <a href="https://github.com/GrandpaNiuu/GrandpaNiu/actions/workflows/module-factory-build.yml">
    <img src="https://github.com/GrandpaNiuu/GrandpaNiu/actions/workflows/module-factory-build.yml/badge.svg" />
  </a>
  <a href="https://github.com/GrandpaNiuu/GrandpaNiu/actions/workflows/repository-health.yml">
    <img src="https://github.com/GrandpaNiuu/GrandpaNiu/actions/workflows/repository-health.yml/badge.svg" />
  </a>
</p>

---

# ⚠️ 使用限制与风险声明

本仓库内容仅供 **个人学习、研究和实验使用**。

禁止将本仓库内容用于以下行为：

* 商业服务
* 收费转售
* 改名搬运
* 镜像分发
* 代运营
* 引流项目
* 其他变相商业用途

规则净化存在误杀风险。使用本仓库模块后，可能出现：

* App 打不开
* 视频无法播放
* 图片加载异常
* 登录异常
* 页面空白
* 某些按钮失效
* 某些广告未完全去除

遇到问题时，请先关闭模块，或者关闭对应 App 的增强规则进行排查。使用者需要自行承担导入、运行、修改和依赖本仓库内容所产生的风险。

---

## 📌 这是什么？

GrandpaNiu 是一个用于 **Shadowrocket、Surge 和 Android 规则客户端** 的广告净化与规则构建仓库。

简单理解：

> 这是一个把常见 App 广告规则、脚本规则、重写规则和 Android 规则整理到一起的自动化融合模块仓库。

主要用于处理：

* 开屏广告
* 弹窗广告
* 横幅广告
* 活动卡片
* 信息流推荐
* 追踪请求
* 部分 App 冗余接口请求

---

## 🧭 当前策略：只维护一个融合模块

GrandpaNiu 的公开入口只保留一个主模块：

```text
Ronghemokuai.sgmodule
```

设计原则是：

```text
多来源规则与脚本 → 候选池 → 审查与去重 → 保护规则优先 → 单一融合模块
```

也就是说，本仓库不是 Stable / Lite / Full / Aggressive 多版本路线。`Release/Modules/` 下的 App 独立模块只是诊断和便利用途，不作为新的公开版本体系。

融合策略详见：`docs/FUSION_POLICY.md`。

---

## ✅ 小白怎么用？

普通用户只需要用下面这个主模块入口。

### 🍎 iPhone / Shadowrocket / Surge

推荐使用主融合模块：

```text
https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule
```

[![安装模块 GrandpaNiu Fusion](https://img.shields.io/static/v1?label=安装模块&message=GrandpaNiu%20Fusion&color=grey&logo=educative&logoColor=white&labelColor=blue&messageColor=white)](https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fgrandpaniuu.github.io%2FGrandpaNiu%2FRonghemokuai.sgmodule "一键安装 Fusion 模块")
[![模块文件 Fusion](https://img.shields.io/static/v1?label=模块文件&message=Fusion&color=grey&logo=todoist&logoColor=white&labelColor=%2325A162&messageColor=white)](https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule "点击访问模块文件")

使用步骤：

1. 点击上面的“安装模块”按钮，或复制模块链接。
2. 打开 Shadowrocket 或 Surge。
3. 找到“模块”或“Module”。
4. 选择“从 URL 导入”。
5. 粘贴链接。
6. 启用模块。
7. 更新模块、脚本和资源。
8. 重启需要净化的 App。

### 🤖 Android

Android 用户可以查看 Android 规则入口：

[![Android 导入页](https://img.shields.io/static/v1?label=Android&message=导入页&color=grey&logo=android&logoColor=white&labelColor=%2325A162&messageColor=white)](https://grandpaniuu.github.io/GrandpaNiu/android.html "打开 Android 导入页")
[![Release 目录](https://img.shields.io/static/v1?label=Release&message=目录&color=grey&logo=github&logoColor=white&labelColor=blue&messageColor=white)](https://grandpaniuu.github.io/GrandpaNiu/Web/catalog.md "查看 Release 目录")

Android 规则主要适合：

* Mihomo
* Clash Meta
* FlClash
* sing-box
* AdGuard DNS
* AdGuard Home
* v2rayNG / V2Ray / Xray 分流片段

注意：Android 规则不能完全等同于 iOS 模块，因为 Android 通常不支持 Shadowrocket / Surge 那种 Script、MITM、Rewrite 能力。

---

## 🚀 核心功能

### 🍎 iOS 模块

* Shadowrocket / Surge 融合模块
* 常见广告域名拦截
* App 开屏广告净化
* 弹窗、横幅、活动卡片清理
* 部分 App 脚本增强
* YouTube、Spotify、知乎、Bilibili、微博、淘宝、京东、拼多多等常见规则维护
* 单一公开入口，避免用户选择多个版本

### 🤖 Android 规则

* 域名规则
* 关键词规则
* IP 规则
* DNS 拦截规则
* sing-box / Mihomo / Clash Meta / AdGuard 等格式输出

### ⚙️ 自动化构建

仓库已配置 GitHub Actions，用于：

* 每日自动更新
* 每日自动重建融合模块
* 自动同步 Release 产物
* 自动生成健康检查报告
* 源文件变化后自动构建最终模块

---

## 🧩 当前版本策略

本仓库当前采用 **Fusion 单一融合版**。

不再主要维护多个旧版本入口，例如：

* Stable
* Stable Plus
* Lite
* Full

维护方向不是增加公开版本数量，而是提高唯一融合模块的稳定性：

* 候选规则先进入 `Rewrite/Sources/Candidates/`
* 不适合的规则归档到 `Rewrite/Sources/Rejected/`
* 登录、支付、视频播放、CDN 等稳定性保护规则优先加载
* 最终公开输出仍然是 `Ronghemokuai.sgmodule`
