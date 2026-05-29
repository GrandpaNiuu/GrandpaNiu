# Rewrite

本目录用于管理模块生成相关的重写框架。

目录设计：

```text
Rewrite/
├─ Generator/       生成器与构建说明
├─ Profiles/        模块配置模板
├─ Remotes/         远程规则源清单
├─ Sources/         本地模块片段
├─ Manifest.conf    构建清单
└─ Registry.md      模块片段登记表
```

当前状态：

- 根目录 `Ronghemokuai.sgmodule` 仍然是正式导入入口。
- `Rewrite/` 先作为结构化维护层使用。
- 后续可逐步把主模块内容拆分到 `Rewrite/Sources/`，再由生成器输出发布版本。
