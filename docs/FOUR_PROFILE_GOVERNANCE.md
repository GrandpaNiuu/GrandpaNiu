# 四版本治理统一说明

本文件统一说明 GrandpaNiu 的四版本边界，供 README、维护文档、报告和后续任务引用。旧文档如存在三版本表述，应以本文件为准后续逐步修正。

## 版本定义

| Profile | 发布文件 | 定位 | 默认发布 |
|---|---|---|---|
| `stable` | `Ronghemokuai.sgmodule` / `Release/Ronghemokuai-stable.sgmodule` | 默认正式版，长期日常使用 | 是 |
| `stable-plus` | `Release/Ronghemokuai-stable-plus.sgmodule` | 增强测试版，测试更多常用 App 覆盖 | 否 |
| `lite` | `Release/Ronghemokuai-lite.sgmodule` | 低耗电、低风险、异常排查 | 否 |
| `full` | `Release/Ronghemokuai-full.sgmodule` | 全量排查、查漏拦 | 否 |

## 统一边界

- `GrandpaNiu` / `Ronghemokuai.sgmodule` = 默认 Stable。
- `Release/Ronghemokuai-stable.sgmodule` 是默认 Stable 的独立发布文件。
- Stable Plus 只做增强测试，不默认发布，不整体合并进 Stable。
- Lite 用于省电和异常排查，不追求覆盖广度。
- Full 只用于全量排查，不长期启用。

## 构建链路

```text
Rules + Scripts + Rewrite/Sources + Rewrite/Remotes + Rewrite/Profiles
        -> scripts/build_module.py --build --profile fusion
        -> scripts/factory_finalize.py --sync-root
        -> scripts/build_release_variants.py
        -> Release/Ronghemokuai-*.sgmodule
```

Root 与 Release 必须保持一致。四个 Release 版本必须都能构建。

## 晋级规则

```text
Stable Plus 单项测试
-> 人工确认常用流程正常
-> 记录到 reports/automated_quality_evidence.md
-> 刷新 reports/app_status_matrix.md
-> 生成晋级审查材料
-> 单项进入 Stable
```

禁止把 Stable Plus 或 Full 整体合并进 Stable。

## 后续修正文档时的标准

凡是旧文档只写 `stable / lite / full`，都应改为 `stable / stable-plus / lite / full`。

凡是旧文档把 Full 写成可长期使用，都应修正为“只用于排查”。

凡是旧文档暗示 Stable Plus 可以整体进入 Stable，都应修正为“只允许单项晋级”。
