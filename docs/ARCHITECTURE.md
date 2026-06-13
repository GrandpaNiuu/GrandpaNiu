# GrandpaNiu 架构说明

本文档把仓库整理为“源材料 → 候选审查 → 生成清单 → 生成器 → 单一融合 Release → Web 分发 → 报告校验”的模块工厂结构。目标不是机械复制图片里的目录，而是把现有生产线收口成可维护、可自动生成、可校验的单一融合模块系统。

## 1. 分层职责

| 层级 | 目录 / 文件 | 职责 | 是否允许日常手动修改 |
|---|---|---|---|
| 规则源 | `Rules/` | 保存 DIRECT、REJECT、App 净化、网页广告、Spotify、YouTube 与保护规则源 | 是 |
| 保护规则 | `Rules/protect-*.list` | 保存登录、支付、视频播放、CDN 等稳定性优先的 DIRECT 规则 | 是，必须保守 |
| 脚本源 | `Scripts/` | 保存本地 JS 与脚本配置片段 | 是 |
| Rewrite 源材料 | `Rewrite/Sources/` | 保存 Meta、Rule、URL Rewrite、Header Rewrite、Body Rewrite、Map Local、Script、MITM 等模块片段 | 是 |
| 候选源 | `Rewrite/Sources/Candidates/` | 保存尚未进入融合模块的候选规则、脚本或 Rewrite 片段 | 是，不参与默认构建 |
| 拒绝源 | `Rewrite/Sources/Rejected/` | 保存已评估但暂不适合进入融合模块的材料 | 是，保留原因 |
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
Rules/protect-*.list
Scripts/
Rewrite/Sources/
Rewrite/Sources/Candidates/   # 候选池，不直接进入公开模块
Rewrite/Sources/Rejected/     # 拒绝池，不直接进入公开模块
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
Release/Module.sgmodule       # 兼容别名
        ↓
Release/Rules.conf
Release/RulesGroup.conf
Release/Modules/*.sgmodule    # 诊断/便利用，不是公开多版本路线
Release/Android/
Web/modules.html
Web/release-links.json
reports/build_summary.*
```

## 3. 单一融合模块策略

GrandpaNiu 公开策略是一个模块：

```text
Ronghemokuai.sgmodule
```

维护原则是“集百家之长，但只输出一个稳定融合入口”：

1. 上游材料先进入候选池。
2. 通过来源、重复、风险和范围检查后再合入源材料层。
3. 保护规则优先加载，避免核心功能被误伤。
4. App 独立模块只作为诊断和便利用途，不作为公开多版本体系。
5. `Release/Module.sgmodule` 只作为兼容别名。

详细准入标准见 `docs/FUSION_POLICY.md`。

## 4. 对齐图片框架的映射关系

| 图片框架 | 本仓库对应项 | 当前策略 |
|---|---|---|
| `Rules/` | `Rules/` + `Rules/protect-*.list` | 保留为规则源头，并增加稳定性保护规则 |
| `Scripts/` | `Scripts/` | 保留为脚本源头 |
| `Rewrite/Sources/` | `Rewrite/Sources/` + `Rewrite/Sources/Candidates/` + `Rewrite/Sources/Rejected/` | 源材料、候选材料和拒绝材料分层 |
| `Rewrite/Generate.conf` | `Rewrite/Generator/Generate.conf` + `Rewrite/Generate.conf` | 首选清单在 `Generator/`，旧路径保留为兼容镜像 |
| `Rewrite/Manifest.conf` | `Rewrite/Manifest.conf` | 保存模块段落和源文件映射 |
| `Rewrite/Registry.md` | `Rewrite/Registry.md` | 扩展为来源、风险、测试、回滚登记表 |
| `Rewrite/Generator/Builder.py` | `Rewrite/Generator/Builder.py` | 统一入口，内部调用 `scripts/` |
| `Release/Module.sgmodule` | `Release/Module.sgmodule` / `Release/Ronghemokuai.sgmodule` | 主融合模块输出与别名输出 |
| `Release/Rules.conf` | `Release/Rules.conf` | 已接入生成链路 |
| `Release/RulesGroup.conf` | `Release/RulesGroup.conf` | 已接入生成链路 |
| `Release/Modules/` | `Release/Modules/` | 已接入按 App 拆分输出，但不是公开多版本路线 |
| `Web/` | `Web/` + 根目录 `import.html` / `android.html` / `redirect.html` | Web 目录和根入口并行维护 |

## 5. 维护原则

1. `Release/` 不是源头，日常不要直接改最终产物。
2. 规则、脚本、Rewrite 片段必须优先改源材料层。
3. 新增上游源先进入 `Rewrite/Sources/Candidates/`，通过审查后再合入正式源材料。
4. 不适合合入的材料放入 `Rewrite/Sources/Rejected/`，保留原因，避免重复引入。
5. 新增上游源必须登记到 `Rewrite/Registry.md` 或 `Rewrite/Remotes/`。
6. 高风险改动必须能回滚，尤其是 MITM、Body Rewrite、Header Rewrite、登录、支付、视频播放相关规则。
7. Android 输出与 iOS / Surge / Shadowrocket 模块能力不同，不要混用同一套能力假设。
8. 新增 Release 产物时，必须同时接入 `Rewrite/Generator/Generate.conf`、`Rewrite/Generator/Builder.py` 和相应校验。
9. 不新增公开多版本模块；所有维护优先服务 `Ronghemokuai.sgmodule`。

## 6. 推荐命令

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

## 7. 仍然需要人工维护的部分

- 新规则是否误伤登录、支付、视频播放，仍需要真实设备测试。
- `reports/automated_quality_evidence.md` 需要记录自动化验证结果。
- 新接入上游源时，必须补充来源、风险、回滚说明。
