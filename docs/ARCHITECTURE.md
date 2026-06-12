# GrandpaNiu 架构说明

本文档把仓库整理为“源材料 → 生成清单 → 生成器 → Release → Web 分发 → 报告校验”的模块工厂结构。目标不是机械复制图片里的目录，而是把现有生产线收口成可维护、可自动生成、可校验的结构。

## 1. 分层职责

| 层级 | 目录 / 文件 | 职责 | 是否允许日常手动修改 |
|---|---|---|---|
| 规则源 | `Rules/` | 保存 DIRECT、REJECT、App 净化、网页广告、Spotify、YouTube 等规则源 | 是 |
| 脚本源 | `Scripts/` | 保存本地 JS 与脚本配置片段 | 是 |
| Rewrite 源材料 | `Rewrite/Sources/` | 保存 Meta、Rule、URL Rewrite、Header Rewrite、Body Rewrite、Map Local、Script、MITM 等模块片段 | 是 |
| 远程源登记 | `Rewrite/Remotes/` | 保存上游源索引、候选源、安全策略和远程规则清单 | 是，必须登记来源 |
| Profile | `Rewrite/Profiles/` | 保存构建 Profile，目前主线为 `fusion.conf` | 是，但需校验 |
| 首选生成清单 | `Rewrite/Generator/Generate.conf` | 声明参与构建的源文件、输出文件、发布脚本和检查策略 | 是，结构变更时修改 |
| 兼容生成清单 | `Rewrite/Generate.conf` | 旧命令兼容镜像，不作为第一入口 | 尽量只随首选清单同步 |
| 生成器入口 | `Rewrite/Generator/Builder.py` | 统一调用构建、同步、Release、Web、Android 和校验脚本 | 是，维护构建流程时修改 |
| 现有脚本实现 | `scripts/` | 保存实际构建、同步、报告、校验脚本 | 是 |
| Release 产物 | `Release/` | 保存生成后的正式产物，包括主模块、规则、分组、独立模块、Android 镜像 | 否，原则上由生成器生成 |
| Web 分发 | `Web/` 与根目录 HTML | 用户导入入口、跳转入口、模块目录和 Android 说明入口 | 自动生成优先，入口页可手动维护 |
| 报告 | `reports/` | 保存构建、差异、治理、误伤、测试等报告 | 自动生成优先 |

## 2. 当前主构建链路

```text
Rules/
Scripts/
Rewrite/Sources/
Rewrite/Remotes/
Rewrite/Profiles/fusion.conf
Rewrite/Generator/Generate.conf
        ↓
Rewrite/Generator/Builder.py
        ↓
scripts/build_module.py --build --profile fusion
        ↓
Ronghemokuai.sgmodule
        ↓
scripts/factory_finalize.py --sync-root
        ↓
Release/Ronghemokuai.sgmodule
        ↓
Release/Rules.conf
Release/RulesGroup.conf
Release/Modules/*.sgmodule
Release/Stable/
Release/Beta/
Release/Canary/
Release/Android/
Web/modules.html
Web/release-links.json
reports/build_summary.*
```

## 3. 对齐图片框架的映射关系

| 图片框架 | 本仓库对应项 | 当前策略 |
|---|---|---|
| `Rules/` | `Rules/` | 保留为规则源头 |
| `Scripts/` | `Scripts/` | 保留为脚本源头 |
| `Rewrite/Sources/` | `Rewrite/Sources/` | 继续作为模块片段层 |
| `Rewrite/Generate.conf` | `Rewrite/Generator/Generate.conf` + `Rewrite/Generate.conf` | 首选清单在 `Generator/`，旧路径保留为兼容镜像 |
| `Rewrite/Manifest.conf` | `Rewrite/Manifest.conf` | 保存模块段落和源文件映射 |
| `Rewrite/Registry.md` | `Rewrite/Registry.md` | 扩展为来源、风险、测试、回滚登记表 |
| `Rewrite/Generator/Builder.py` | `Rewrite/Generator/Builder.py` | 统一入口，内部调用 `scripts/` |
| `Release/Module.sgmodule` | `Release/Module.sgmodule` / `Release/Ronghemokuai.sgmodule` | 主融合模块输出与别名输出 |
| `Release/Rules.conf` | `Release/Rules.conf` | 已接入生成链路 |
| `Release/RulesGroup.conf` | `Release/RulesGroup.conf` | 已接入生成链路 |
| `Release/Modules/` | `Release/Modules/` | 已接入按 App 拆分输出 |
| `Web/` | `Web/` + 根目录 `import.html` / `android.html` / `redirect.html` | Web 目录和根入口并行维护 |

## 4. 维护原则

1. `Release/` 不是源头，日常不要直接改最终产物。
2. 规则、脚本、Rewrite 片段必须优先改源材料层。
3. 新增上游源必须登记到 `Rewrite/Registry.md` 或 `Rewrite/Remotes/`。
4. 高风险改动必须能回滚，尤其是 MITM、Body Rewrite、Header Rewrite、登录、支付、视频播放相关规则。
5. Android 输出与 iOS / Surge / Shadowrocket 模块能力不同，不要混用同一套能力假设。
6. 新增 Release 产物时，必须同时接入 `Rewrite/Generator/Generate.conf`、`Rewrite/Generator/Builder.py` 和相应校验。

## 5. 推荐命令

```bash
python Rewrite/Generator/Builder.py --profile fusion --release --check
```

只查看将要执行的步骤：

```bash
python Rewrite/Generator/Builder.py --profile fusion --release --check --dry-run
```

单独检查生成清单是否漂移：

```bash
python scripts/validate_generator_config.py
```

## 6. 仍然需要人工维护的部分

- 新规则是否误伤登录、支付、视频播放，仍需要真实设备测试。
- `reports/manual_test_log.md` 需要记录人工测试结果。
- 新接入上游源时，必须补充来源、风险、回滚说明。
