# 项目结构说明

本仓库正在从“单一成品模块仓库”升级为“模块工厂仓库”。

## 当前正式入口

```text
Ronghemokuai.sgmodule
```

这个文件仍然是 Shadowrocket / Surge 的正式导入入口。

## 工厂化目录

```text
Release/
Rewrite/
  ├─ Generator/
  ├─ Profiles/
  ├─ Remotes/
  ├─ Sources/
  ├─ Manifest.conf
  └─ Registry.md
Rules/
Scripts/
Web/
scripts/
reports/
docs/
backup/
.github/workflows/
```

## 目录职责

| 目录 | 职责 |
|---|---|
| `Release/` | 保存生成后的发布副本 |
| `Rewrite/` | 管理模块生成框架、清单、来源、登记表 |
| `Rewrite/Generator/` | 生成器说明和后续构建逻辑 |
| `Rewrite/Profiles/` | 不同构建模板，例如 stable / full / test |
| `Rewrite/Remotes/` | 远程规则源和脚本源登记 |
| `Rewrite/Sources/` | 从主模块拆分出来的模块片段 |
| `Rules/` | 后续存放纯规则文件 |
| `Scripts/` | 后续存放脚本来源说明或本地脚本 |
| `Web/` | 后续管理导入页和跳转页 |
| `scripts/` | 维护脚本、构建脚本、审计脚本 |
| `reports/` | 自动生成的检查报告和维护报告 |
| `docs/` | 使用、维护、排查、结构说明 |
| `backup/` | 稳定备份和回滚说明 |
| `.github/workflows/` | GitHub Actions 自动化流程 |

## 生成流程

```text
Ronghemokuai.sgmodule
        ↓
scripts/build_module.py --extract-from-root --build
        ↓
Rewrite/Sources/
        ↓
Release/Ronghemokuai.sgmodule
        ↓
reports/module_factory_report.md
```

## 当前阶段

当前阶段采取保守策略：

1. 根目录 `Ronghemokuai.sgmodule` 继续作为正式导入入口。
2. `Rewrite/Sources/` 作为结构化拆分区。
3. `Release/Ronghemokuai.sgmodule` 作为生成副本。
4. 暂不让 Release 自动覆盖根目录主模块。
5. 只有确认 Release 与根目录主模块完全一致后，才考虑进入下一阶段。

## 后续阶段

后续可以逐步推进：

```text
第一阶段：搭建框架和环境
第二阶段：从主模块拆分 Sources
第三阶段：生成 Release 副本
第四阶段：对比 Release 与主模块一致性
第五阶段：逐步改为 Sources 驱动主模块
```

安全原则：

- 不破坏当前可导入的主模块。
- 不自动删除 Spotify / YouTube 核心内容。
- 不让生成器主动改变规则语义。
- 所有生成结果先写入 Release，确认后再考虑同步到根目录。
