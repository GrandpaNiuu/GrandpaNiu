# 版本策略

GrandpaNiu 使用“日期元信息 + 语义版本”的双轨版本管理。

## 双轨规则

- 模块元信息 `#!desc` 可以继续使用日期，便于 Shadowrocket 中快速判断更新时间。
- 仓库治理、发布记录和大版本变更使用语义版本，并记录在 `CHANGELOG.md`。

## 版本里程碑

| 版本 | 含义 |
|---|---|
| `v1.0 stable factory` | 源头驱动模块工厂稳定成型 |
| `v1.1 zhihu enhance` | 知乎增强净化加入并通过校验 |
| `v1.2 governance` | 安全、贡献、脚本审核、MITM 策略加入 |
| `v1.3 health reports` | 仓库健康、覆盖矩阵、变更影响和 workflow 报告加入 |
| `v1.4 mitm policy` | MITM 增长控制和分层治理开始推进 |
| `v1.5 profile validation` | stable / lite / full profile 全量构建验证 |

## 升级规则

| 类型 | 触发条件 |
|---|---|
| `patch` | 文档、报告、验证脚本、非功能性修复 |
| `minor` | 新增可信规则源、轻量脚本、profile、报告生成器或治理文件 |
| `major` | 主模块结构大改、MITM 大规模调整、脚本体系重构或默认发布策略改变 |

## Profile 与版本关系

| Profile | 版本角色 |
|---|---|
| `stable` | 默认正式发布版本 |
| `lite` | 低耗电参考版本，不默认发布 |
| `full` | 全覆盖测试版本，不默认发布 |

发布版本默认只指向 `stable`。`lite` 和 `full` 只能作为测试、排查和对照，不应自动覆盖根目录主模块。

## 发布前检查

发布前必须：

1. 更新 `CHANGELOG.md`。
2. 使用 `stable` 构建。
3. 从 Release 同步 Root。
4. 运行 `validate_repository.py`。
5. 运行 `repository_health_check.py`。
6. 运行 `validate_profiles.py`，确认 stable / lite / full 都能构建。
7. 确认 Root 与 Release diff lines 为 `0`。
8. 相关改动涉及时，测试 Spotify、YouTube、知乎、登录、支付和验证码流程。
