# 本地维护环境

GrandpaNiu 是 source-first 的 Shadowrocket / Surge / Android / Windows 规则构建仓库。当前公开策略是 **Fusion 单一融合模块**。

`Rules/`、`Scripts/`、`Rewrite/Sources/`、`Rewrite/Remotes/` 是日常维护源头；`Release/`、`Web/`、`reports/`、根目录 `Ronghemokuai.sgmodule` 是构建结果或报告结果，不应长期手工维护。

## 必需工具

- Git：用于克隆、查看差异、提交和回滚。
- Python 3.10+：用于构建、验证和报告脚本。
- Node.js LTS：用于检查 JavaScript 脚本语法。
- Shadowrocket / Surge：用于真实设备导入和人工实测。

注意大小写：

- `Scripts/` 是模块脚本和脚本配置目录。
- `scripts/` 是维护脚本目录。

## 克隆仓库

```bash
git clone https://github.com/GrandpaNiuu/GrandpaNiu.git
cd GrandpaNiu
```

## 开始维护前

先读：

```text
AGENTS.md
PROJECT_STATE.md
AI_HANDOFF.md
docs/ai/TASKS.md
docs/ai/DECISIONS.md
docs/ai/RISK_LOG.md
docs/ai/WORKLOG.md
```

再运行：

```bash
git status
git branch --show-current
```

如果存在未提交修改，先确认来源，不要直接覆盖。

## 标准构建和验证

标准构建入口：

```bash
python3 Rewrite/Generator/Builder.py --profile fusion --release
```

推荐完整质量门：

```bash
python3 scripts/quality_gate.py
```

常用只读或轻量检查：

```bash
python3 -m py_compile scripts/*.py Rewrite/Generator/Builder.py
node --check Scripts/app-cleaner.js
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

## 输出关系

```text
Rules/
Scripts/
Rewrite/Sources/
Rewrite/Remotes/
Rewrite/Profiles/fusion.conf
        -> Rewrite/Generator/Builder.py --profile fusion --release
        -> Release/Ronghemokuai.sgmodule
        -> Release/Module.sgmodule
        -> Ronghemokuai.sgmodule
        -> Release/Rules.conf
        -> Release/RulesGroup.conf
        -> Release/Modules/
        -> Release/Android/
        -> Web/
        -> reports/
```

## Deprecated / Legacy Reference

以下旧四版本文件如果存在，只作为历史兼容、审计或回滚参考：

```text
Release/Ronghemokuai-stable.sgmodule
Release/Ronghemokuai-stable-plus.sgmodule
Release/Ronghemokuai-lite.sgmodule
Release/Ronghemokuai-full.sgmodule
Rewrite/Profiles/stable.conf
Rewrite/Profiles/stable-plus.conf
Rewrite/Profiles/lite.conf
Rewrite/Profiles/full.conf
```

不要把它们写回 README、导入页、默认 workflow、健康检查、发布报告或 Web catalog。

## 禁止直接手改生成结果

不要长期手工维护：

- `Ronghemokuai.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Module.sgmodule`
- `Release/Rules.conf`
- `Release/RulesGroup.conf`
- `Release/Modules/`
- `Release/Android/`
- `Web/catalog.md`
- `Web/release-links.json`
- `reports/`

需要改变模块行为时，优先改源头：

- `Rules/*.list`
- `Scripts/*.conf`
- `Scripts/*.js`
- `Rewrite/Sources/*.conf`
- `Rewrite/Sources/Apps/*.conf`
- `Rewrite/Sources/Misc/*.conf`
- `Rewrite/Remotes/*.json`

然后重新构建和验证。
