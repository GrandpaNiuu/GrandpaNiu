# 稳定备份说明

更新时间：2026-05-29

## 用途

- `Ronghemokuai.stable.sgmodule` 是当前主模块 `Ronghemokuai.sgmodule` 的稳定备份，用于在主模块误改、自动维护异常或规则大范围失效时进行人工回滚。
- `Ronghemokuai.before-factory-refactor.sgmodule` 是切换到源头驱动工厂前的主模块备份，用于对照或回滚本次工厂重构。

## 如何恢复

1. 人工确认主模块确实需要回滚。
2. 将 `backup/Ronghemokuai.stable.sgmodule` 或 `backup/Ronghemokuai.before-factory-refactor.sgmodule` 的内容复制覆盖到仓库根目录的 `Ronghemokuai.sgmodule`。
3. 检查 `[Rule]`、`[Script]`、`[MITM]`、Spotify、YouTube 和 `update-url` 是否仍然完整。
4. 提交回滚变更，并在提交说明中写清楚回滚原因。

## 注意事项

- 不要让每日自动维护脚本自动覆盖 `backup/` 目录。
- 不要把临时测试模块写入稳定备份。
- 更新稳定备份必须人工确认，并保留可追溯提交记录。
