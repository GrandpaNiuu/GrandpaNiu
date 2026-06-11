# GrandpaNiu 架构说明

本文档把仓库整理为“源材料 → 生成清单 → 生成器 → Release → Web 分发 → 报告校验”的模块工厂结构。目标是对齐图片里的成品框架，但不把目录机械复制，而是把现有半成品生产线收口。

## 1. 分层职责

| 层级 | 目录 / 文件 | 职责 | 是否允许日常手动修改 |
|---|---|---|---|
| 规则源 | `Rules/` | 保存 DIRECT、REJECT、App 净化、网页广告、Spotify、YouTube 等规则源 | 是 |
| 脚本源 | `Scripts/` | 保存本地 JS 与脚本配置片段 | 是 |
| Rewrite 源材料 | `Rewrite/Sources/` | 保存 Meta、Rule、URL Rewrite、Header Rewrite、Body Rewrite、Map Local、Script、MITM 等模块片段 | 是 |
| 远程源登记 | `Rewrite/Remotes/` | 保存上游源索引、候选源、安全策略和远程规则清单 | 是，必须登记来源 |
| Profile | `Rewrite/Profiles/` | 保存构建 Profile，目前主线为 `fusion.conf` | 是，但需校验 |
| 生成清单 | `Rewrite/Generate.conf` | 声明参与构建的源文件、输出文件和检查策略 | 是，结构变更时修改 |
| 生成器入口 | `Rewrite/Generator/Builder.py` | 统一调用现有构建、同步和校验脚本 | 是，维护构建流程时修改 |
| 现有脚本实现 | `scripts/` | 保存实际构建、同步、报告、校验脚本 | 是 |
| Release 产物 | `Release/` | 保存生成后的正式产物 | 否，原则上由生成器生成 |
| Web 分发 | `Web/` 与根目录 HTML | 用户导入入口、跳转入口和 Android 说明入口 | 是 |
| 报告 | `reports/` | 保存构建、差异、治理、误伤、测试等报告 | 自动生成优先 |

## 2. 当前主构建链路

```text
Rules/
Scripts/
Rewrite/Sources/
Rewrite/Remotes/
Rewrite/Profiles/fusion.conf
Rewrite/Generate.conf
        ↓
Rewrite/Generator/Builder.py
        ↓
scripts/build_module.py --build --profile fusion
        ↓
Release/Ronghemokuai.sgmodule
        ↓
scripts/factory_finalize.py --sync-root
        ↓
Ronghemokuai.sgmodule
        ↓
scripts/build_release_variants.py
        ↓
reports/multi_release_report.md
```

## 3. 对齐图片框架的映射关系

| 图片框架 | 本仓库对应项 | 当前策略 |
|---|---|---|
| `Rules/` | `Rules/` | 保留为规则源头 |
| `Scripts/` | `Scripts/` | 保留为脚本源头 |
| `Rewrite/Sources/` | `Rewrite/Sources/` | 继续作为模块片段层 |
| `Rewrite/Generate.conf` | `Rewrite/Generate.conf` | 新增为生成总清单 |
| `Rewrite/Manifest.conf` | `Rewrite/Manifest.conf` | 保存模块段落和源文件映射 |
| `Rewrite/Registry.md` | `Rewrite/Registry.md` | 扩展为来源、风险、测试、回滚登记表 |
| `Rewrite/Generator/Builder.py` | `Rewrite/Generator/Builder.py` | 新增为统一入口，内部调用 `scripts/` |
| `Release/Module.sgmodule` | `Release/Ronghemokuai.sgmodule` | 主融合模块输出 |
| `Release/Rules.conf` | `Release/Rules.conf` | 规划中的纯规则输出 |
| `Release/RulesGroup.conf` | `Release/RulesGroup.conf` | 规划中的规则组输出 |
| `Release/Modules/` | `Release/Modules/` | 规划中的按 App 拆分输出 |
| `Web/` | `Web/` + 根目录 `import.html` / `android.html` / `redirect.html` | 逐步迁移到统一 Web 层 |

## 4. 维护原则

1. `Release/` 不是源头，日常不要直接改最终产物。
2. 规则、脚本、Rewrite 片段必须优先改源材料层。
3. 新增上游源必须登记到 `Rewrite/Registry.md` 或 `Rewrite/Remotes/`。
4. 高风险改动必须能回滚，尤其是 MITM、Body Rewrite、Header Rewrite、登录、支付、视频播放相关规则。
5. Android 输出与 iOS / Surge / Shadowrocket 模块能力不同，不要混用同一套能力假设。

## 5. 推荐命令

```bash
python Rewrite/Generator/Builder.py --profile fusion --release --check
```

只查看将要执行的步骤：

```bash
python Rewrite/Generator/Builder.py --profile fusion --release --check --dry-run
```

## 6. 后续补齐目标

- 生成 `Release/Rules.conf`。
- 生成 `Release/RulesGroup.conf`。
- 生成 `Release/Modules/*.sgmodule`。
- 把根目录 HTML 入口逐步迁移或镜像到 `Web/`。
- 把 `Rewrite/Registry.md` 从基础登记表升级为完整溯源库。
- 将真实设备测试结果固定写入 `reports/manual_test_log.md`。
