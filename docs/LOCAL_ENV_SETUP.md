# 本地维护环境

本仓库是 source-first 的 Shadowrocket / Surge 多版本模块工厂。`Rules/`、`Scripts/`、`Rewrite/Sources/`、`Rewrite/Profiles/`、`Rewrite/Remotes/` 是日常维护源头；`Release/` 和根目录 `Ronghemokuai.sgmodule` 是构建结果，不是长期手工维护源头。

## 必需工具

- Git：用于克隆仓库、查看差异、提交和回滚。
- Python 3.10+：用于构建、验证和报告脚本。
- Node.js LTS：用于检查 `Scripts/app-cleaner.js` 语法。
- Shadowrocket：用于在真实设备上导入模块并做人工测试。

建议在区分大小写的文件系统中维护仓库，或至少严格使用路径大小写：`Scripts/` 是脚本配置源头，`scripts/` 是维护脚本目录。

## 克隆仓库

```bash
git clone https://github.com/GrandpaNiuu/GrandpaNiu.git
cd GrandpaNiu
```

## 本地语法检查

```bash
python3 -m py_compile \
  scripts/build_module.py \
  scripts/build_release_variants.py \
  scripts/factory_finalize.py \
  scripts/validate_repository.py \
  scripts/repository_health_check.py \
  scripts/validate_profiles.py \
  scripts/check_report_freshness.py

node --check Scripts/app-cleaner.js
```

## 标准构建和验证

Stable 是默认正式版；根目录 `Ronghemokuai.sgmodule` 必须等于 Stable 构建结果。

```bash
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_repository.py
python3 scripts/check_report_freshness.py
python3 scripts/repository_health_check.py
```

构建链路：

```text
Rules + Scripts + Rewrite/Sources + Rewrite/Remotes + Rewrite/Profiles
        -> scripts/build_module.py --build --profile stable
        -> Release/Ronghemokuai.sgmodule
        -> scripts/factory_finalize.py --sync-root
        -> Ronghemokuai.sgmodule
        -> scripts/build_release_variants.py
        -> Release/Ronghemokuai-stable.sgmodule
        -> Release/Ronghemokuai-stable-plus.sgmodule
        -> Release/Ronghemokuai-lite.sgmodule
        -> Release/Ronghemokuai-full.sgmodule
```

## 四个版本

- `GrandpaNiu / Ronghemokuai.sgmodule`：默认 Stable，适合日常长期使用。
- `Release/Ronghemokuai-stable.sgmodule`：Stable 独立发布文件。
- `Release/Ronghemokuai-stable-plus.sgmodule`：增强测试版，不默认发布，不整体合并进 Stable。
- `Release/Ronghemokuai-lite.sgmodule`：低耗电和异常定位版。
- `Release/Ronghemokuai-full.sgmodule`：全量排查版，只用于查漏和定位，不建议长期启用。

不要同时启用多个版本。

## 禁止直接手改生成结果

不要直接长期维护或手工修改：

- `Ronghemokuai.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Ronghemokuai-*.sgmodule`

如果确实需要改变模块内容，先修改源头文件：

- `Rules/*.list`
- `Scripts/*.conf`
- `Rewrite/Sources/*.conf`
- `Rewrite/Profiles/*.conf`
- `Rewrite/Remotes/*.json`

然后重新运行构建和验证命令。

## Source-First 原则

所有修改必须 source-first：

- 规则变更先进入 `Rules/` 或 `Rewrite/Remotes/`。
- 脚本变更先进入 `Scripts/`，未知脚本保持 pending。
- Rewrite、Header、Body、Map Local、MITM 变更先进入 `Rewrite/Sources/`。
- 版本差异先进入 `Rewrite/Profiles/`。
- 报告只记录状态，不作为规则或脚本源头。

没有真实人工测试记录时，不得把覆盖写成“通过”。
