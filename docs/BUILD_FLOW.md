# 模块构建流程

`Ronghemokuai.sgmodule` 是构建产物，不是长期手工维护源头。

日常维护只修改：

- `Rules/`
- `Scripts/`
- `Rewrite/Sources/`
- `Rewrite/Remotes/`
- `Rewrite/Profiles/fusion.conf`

统一构建入口：

`python3 Rewrite/Generator/Builder.py --profile fusion --release`

统一验证入口：

`python3 scripts/quality_gate.py`

仓库仅使用 Fusion 构建路径；旧版多配置路线不再存在。`--extract-from-root` 只用于初始化或灾难恢复。
