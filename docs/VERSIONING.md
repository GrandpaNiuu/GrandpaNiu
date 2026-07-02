# 版本策略

GrandpaNiu 使用“日期元信息 + 语义版本”的双轨版本管理。

- 模块元信息 `#!desc` 使用日期，便于客户端判断更新时间。
- 仓库治理、发布记录和结构性变更使用语义版本，并记录在 `CHANGELOG.md`。

## 版本原则

| 类型 | 触发条件 |
|---|---|
| patch | 文档、报告、验证脚本或非功能性修复 |
| minor | 新增可信规则源、轻量脚本或治理能力 |
| major | 主模块结构、MITM 范围、脚本体系或公开发布策略的大改 |

## 发布对象

版本只对应 Fusion 主模块。仓库不再维护 Stable、Stable Plus、Lite 或 Full 的独立版本号、构建结果或发布流程。

## 发布前检查

1. 更新 `CHANGELOG.md`。
2. 构建 Fusion。
3. 确认 Root 与 Release 一致。
4. 运行 `validate_profiles.py`、`validate_repository.py` 和 `repository_health_check.py`。
5. 对涉及的功能执行相应的真实使用验证。
