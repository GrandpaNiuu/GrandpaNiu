# 变更记录

## 2026-05-29

- 完善长期维护系统，补齐 README 维护入口对应的真实文件。
- 新增每日失效源修复系统：连续 2 天确认失效后，优先同源替换，其次注释，最后才允许低风险独立远程规则删除。
- 新增稳定备份 `backup/Ronghemokuai.stable.sgmodule` 和备份说明，便于人工回滚。
- 新增功能覆盖清单 `docs/COVERAGE.md`。
- 新增项目范围说明 `docs/SCOPE.md`。

## 2026-05-28

- 新增每日失效审计与安全修复工作流。
- 新增失效历史记录和审计报告。
- 在 README 维护状态区域加入报告、历史和工作流入口。
- 明确基础检查工作流与失效源修复工作流的行为差异。

## 2026-05-25

- 增加一键安装按钮。
- 增加 `redirect.html` 跳转页和 `import.html` 备用导入页面。
- 增加每日自动更新工作流。
- 增加维护文档和问题排查文档。
- 增加 Spotify 白名单与 Spotify / YouTube 关键项检查。
- 引入 Remote AdBlock Hub、blackmatrix7、Cats-Team、zirawell/R-Store、fmz200/wool_scripts、app2smile 等远程规则或脚本来源。
- 增加旧版精选规则迁移流程和迁移报告。
- 增加安全整理脚本，用于重复统计、脚本融合和关键项验证。
