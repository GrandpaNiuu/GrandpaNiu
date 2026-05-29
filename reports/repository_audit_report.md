# Repository Audit Report

日期：2026-05-29

## 审计范围

本次只检查和整理仓库结构、维护脚本、工作流和文档，不修改 `Ronghemokuai.sgmodule` 主模块内容。

## 当前仓库状态

仓库当前处于“主模块发布入口 + 模块工厂框架”并行状态。

```text
Ronghemokuai.sgmodule              正式导入入口，当前未改动
Release/                           生成后的发布副本目录
Rewrite/                           模块工厂框架目录
Rewrite/Generator/                 生成器说明
Rewrite/Profiles/                  构建模板说明
Rewrite/Remotes/                   远程源索引
Rewrite/Sources/                   拆分后的模块片段目录
Rewrite/Manifest.conf              构建清单
Rewrite/Registry.md                片段登记表
Rules/                             纯规则目录
Scripts/                           脚本来源目录
Web/                               网页入口目录
scripts/                           维护脚本和构建脚本
reports/                           报告目录
docs/                              文档目录
backup/                            稳定备份目录
.github/workflows/                 自动化工作流
```

## 已检查的核心文件

```text
.github/workflows/daily-module-update.yml
.github/workflows/daily-invalid-source-repair.yml
.github/workflows/module-factory-build.yml
scripts/build_module.py
scripts/audit_repair_invalid_sources.py
Rewrite/Manifest.conf
Rewrite/Registry.md
docs/PROJECT_STRUCTURE.md
```

## 当前工作流关系

| 工作流 | 作用 | 是否会修改主模块 | 风险 |
|---|---|---|---|
| Daily Module Update | 更新日期、生成每日检查报告 | 会，仅更新日期 | 低 |
| Daily invalid source audit and repair | 检查失效源，连续 2 天后安全处理 | 可能会，受安全条件限制 | 中 |
| Module Factory Build | 从主模块拆分 Sources 并生成 Release 副本 | 不覆盖主模块 | 低 |

## 已优化内容

本次已为 3 个会写入仓库的工作流添加统一并发控制：

```yaml
concurrency:
  group: module-maintenance
  cancel-in-progress: false
```

作用：

- 避免每日更新、失效源修复、工厂构建同时写仓库。
- 降低 GitHub Actions 之间互相覆盖、提交冲突、push 失败的概率。
- 保持多个维护任务按顺序执行。

已调整文件：

```text
.github/workflows/daily-module-update.yml
.github/workflows/daily-invalid-source-repair.yml
.github/workflows/module-factory-build.yml
```

## 潜在冲突点

### 1. 每日更新与工厂构建

`daily-module-update.yml` 会更新 `Ronghemokuai.sgmodule` 日期。`module-factory-build.yml` 监听主模块变化后会拆分并生成 Release 副本。

当前状态：可接受。

原因：

- 工厂构建不会覆盖根目录主模块。
- Release 只是生成副本。
- 已添加并发控制，避免同时写入。

### 2. 失效源修复与每日更新

`daily-invalid-source-repair.yml` 可能在连续 2 天确认失效后修改主模块。`daily-module-update.yml` 也会修改主模块日期。

当前状态：需要观察，但风险已降低。

原因：

- 已添加并发控制。
- 失效源修复有保护项和自动停止条件。
- 核心 Spotify / YouTube / update-url 不会自动破坏。

### 3. 工厂构建与 Sources 状态

当前 `Rewrite/Sources/` 是通过 `scripts/build_module.py` 从根目录主模块拆分生成。生成结果是 Release 副本。

当前状态：安全。

原因：

- 根目录主模块仍是正式导入入口。
- 生成器不会主动改变规则语义。
- 只有确认 Release 与主模块一致后，才建议进入下一阶段。

## 结构评价

当前仓库已经不是单纯的成品模块仓库，而是：

```text
正式主模块
+
模块工厂框架
+
自动检查系统
+
失效源审计系统
+
稳定备份与文档体系
```

这个结构适合后续长期维护，但当前仍处于过渡阶段。

## 当前不建议做的事

```text
1. 不建议立刻让 Release/Ronghemokuai.sgmodule 替代根目录主模块。
2. 不建议一次性把所有规则手工迁移到 Rules/ 和 Scripts/。
3. 不建议开启自动删除大量规则。
4. 不建议删除主模块里的现有有效规则。
5. 不建议加入 .claude / CLAUDE.md。
```

## 后续建议

### 第一优先

手动运行一次：

```text
Actions → Module Factory Build → Run workflow
```

确认是否生成：

```text
Rewrite/Sources/Meta.conf
Rewrite/Sources/Rule.conf
Rewrite/Sources/URL-Rewrite.conf
Rewrite/Sources/Header-Rewrite.conf
Rewrite/Sources/Body-Rewrite.conf
Rewrite/Sources/Map-Local.conf
Rewrite/Sources/Script.conf
Rewrite/Sources/MITM.conf
Release/Ronghemokuai.sgmodule
reports/module_factory_report.md
```

### 第二优先

查看 `reports/module_factory_report.md`，确认：

```text
Release 是否与根目录主模块一致：yes
```

如果为 `yes`，说明工厂拆分和重新生成流程可靠。

### 第三优先

再考虑把部分纯规则逐步从 `Rewrite/Sources/Rule.conf` 拆到：

```text
Rules/direct.list
Rules/reject.list
Rules/spotify-direct.list
Rules/youtube-direct.list
```

不要一次性大拆。

## 本次结论

当前仓库整体结构合理，没有发现必须立即回滚的结构性冲突。

需要重点观察的是：

```text
1. 三个写仓库的 Actions 是否能按顺序运行。
2. Module Factory Build 是否能成功生成 Release 副本。
3. Release 副本是否与根目录主模块一致。
4. Daily invalid source audit and repair 是否只在连续 2 天失败后处理。
```

本次未修改 `Ronghemokuai.sgmodule` 主模块内容。
