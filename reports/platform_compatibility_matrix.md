# 平台兼容矩阵

- 生成时间：2026-09-04 03:25:21 +0800

## 核心结论

- iOS Fusion 是主公开入口，具备最完整的 Rewrite / Script / MITM 能力。
- Android 与 Windows 输出是规则投影，主要解决路由和域名层广告拦截，不能承诺 iOS 脚本效果。
- App 独立模块用于排查和精细导入，不是新的多版本路线。

| 平台 / 客户端 | 推荐入口 | 支持能力 | 不支持 / 限制 | 状态 |
|---|---|---|---|---|
| iOS Shadowrocket | `https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule` | Rule、URL/Header/Body Rewrite、Map Local、Script、MITM、二进制 body 参数 | 依赖 Shadowrocket 模块解析能力；需要用户本机证书和可用策略组 | 存在 |
| Surge | `Release/Ronghemokuai.sgmodule` 或 App 独立模块 | Surge 风格 section 大体兼容；适合做规则和模块参考 | Shadowrocket 特有参数或客户端行为不能保证完全等价 | 存在 |
| Android Mihomo / Clash Meta / Clash Mi | `Android/mihomo/GrandpaNiu-Ads.yaml`；完整配置参考 `Android/mihomo/GrandpaNiu-Android-Full.yaml` | 域名、关键词、IP、REJECT / DIRECT / PROXY 路由投影 | 不能执行 iOS Script、MITM、Body Rewrite、Map Local；Clash Meta / Clash Mi 建议关闭分应用代理 | 存在 |
| Android sing-box | `Android/sing-box/GrandpaNiu-Ads.json` | 规则集 JSON 投影，适合路由 / 域名层拦截 | 不能执行 iOS Script、MITM、Rewrite；只代表可迁移规则层 | 存在 |
| Android AdGuard / DNS | `Android/adguard/GrandpaNiu-DNS.txt` | DNS / 域名过滤层 | 不能处理路径级、body 级、脚本级净化；可能弱于 iOS 模块 | 存在 |
| Android v2rayNG / V2Ray / Xray | `Android/v2rayng/GrandpaNiu-v2rayng-routing.json` | routing.rules 层拦截和直连 / 代理尾部规则 | 不能执行 iOS Rewrite / Script；不是完整 App 净化模块 | 存在 |
| Windows v2rayN | `Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json` | v2rayN 自定义路由 JSON 数组 | 仅路由层；导入到 v2rayN 自定义规则，不是 iOS 模块 | 存在 |
| Release App Modules | `Release/Modules/*.sgmodule` | 按 App 拆分的独立模块，共 398 个 | 用于单 App 调试和引用；公开主入口仍是 Fusion 单模块 | 存在 |

## Android 分支

- `mihomo`：`Android/mihomo/GrandpaNiu-Ads.yaml` / `Release/Android/mihomo/GrandpaNiu-Ads.yaml`，规则数 `952`
- `sing-box`：`Android/sing-box/GrandpaNiu-Ads.json` / `Release/Android/sing-box/GrandpaNiu-Ads.json`，规则数 `952`
- `adguard`：`Android/adguard/GrandpaNiu-DNS.txt` / `Release/Android/adguard/GrandpaNiu-DNS.txt`，规则数 `891`
- `v2rayng`：`Android/v2rayng/GrandpaNiu-v2rayng-routing.json` / `Release/Android/v2rayng/GrandpaNiu-v2rayng-routing.json`，规则数 `952`

## 使用边界

- 不要把 Android / Windows 输出当作完整 iOS 模块使用。
- 不要为了兼容 Android / Windows 而把 iOS 高风险 MITM 或脚本逻辑硬转过去。
- 当某 App 发生无网络、无法登录、无法播放、图片空白时，优先定位具体平台输出和源文件，再做单点调整。
