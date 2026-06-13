# 自动化验证标准

本文件定义模块发布前后的自动化验证流程。仓库不再维护人工设备记录作为发布门禁；发布判断只看可重复执行的构建、校验和报告证据。

## 一键质量门禁

发布、自动更新或大改后统一运行：

```bash
python scripts/quality_gate.py
```

该命令会执行：

- Python 维护脚本语法检查。
- `Scripts/app-cleaner.js` JavaScript 语法检查。
- 标准库单元测试。
- Android 规则生成与格式检查。
- Fusion 模块构建、Root / Release 同步和 Release 别名生成。
- 远程规则语法校验、治理扩展校验、Profile 校验和模块完整性校验。
- App 覆盖矩阵、状态矩阵、脚本清单、安全评分、误伤风险和仓库健康报告生成。
- `reports/automated_quality_evidence.md` 自动化证据报告生成。

## 证据文件

```text
reports/automated_quality_evidence.md
```

该报告是发布判断入口。它记录质量门禁命令、关键报告状态、Root / Release 一致性和 BOM 扫描结果。

## 用户反馈处理

用户反馈可以触发 Issue、回滚或修复，但不作为发布阻断门禁。报告生成脚本不得把反馈自动改写为“通过”。

## 失败处理

1. 查看失败命令输出。
2. 优先修源头文件，不直接改 Release 成品。
3. 重新运行 `python scripts/quality_gate.py`。
4. 确认 `reports/automated_quality_evidence.md` 已刷新。
5. 提交前检查 `git diff`，确保只有预期变更。

## 回滚后验证

回滚后仍必须运行：

```bash
python scripts/quality_gate.py
```
