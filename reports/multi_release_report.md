# 多版本发布报告

生成时间：2026-06-08 05:22:42 +0800

默认根目录 `Ronghemokuai.sgmodule` 仍由 stable 构建并同步；以下文件是 Shadowrocket 独立导入版本。

| Profile | 文件 | 脚本数 | MITM 数量 | 默认发布 | 用途 | Pages 地址 | Raw 地址 |
|---|---|---:|---:|---|---|---|---|
| stable | `Release/Ronghemokuai-stable.sgmodule` | 45 | 264 | yes | 默认正式版，优先长期稳定 | https://grandpaniuu.github.io/GrandpaNiu/Release/Ronghemokuai-stable.sgmodule | https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Release/Ronghemokuai-stable.sgmodule |
| stable-plus | `Release/Ronghemokuai-stable-plus.sgmodule` | 34 | 217 | no | 常用 App 增强测试版，不默认发布 | https://grandpaniuu.github.io/GrandpaNiu/Release/Ronghemokuai-stable-plus.sgmodule | https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Release/Ronghemokuai-stable-plus.sgmodule |
| lite | `Release/Ronghemokuai-lite.sgmodule` | 4 | 11 | no | 低耗电参考版，不默认发布 | https://grandpaniuu.github.io/GrandpaNiu/Release/Ronghemokuai-lite.sgmodule | https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Release/Ronghemokuai-lite.sgmodule |
| full | `Release/Ronghemokuai-full.sgmodule` | 32 | 1009 | no | 全量排查测试版，不默认发布 | https://grandpaniuu.github.io/GrandpaNiu/Release/Ronghemokuai-full.sgmodule | https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Release/Ronghemokuai-full.sgmodule |

## 使用规则

- Shadowrocket 中不要同时启用多个版本。
- 日常使用 stable。
- 想测试更多 App 覆盖时使用 stable-plus。
- 手机发热、耗电或异常时使用 lite。
- full 只用于排查，不建议长期启用。
