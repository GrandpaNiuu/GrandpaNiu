# Module Factory Report

日期：2026-05-29
是否从根目录主模块拆分：yes
Release 是否与根目录主模块一致：no
Release 行数：2814

## Sources 统计
- Rule: 506 lines
- URL Rewrite: 1598 lines
- Header Rewrite: 5 lines
- Body Rewrite: 456 lines
- Map Local: 16 lines
- Script: 211 lines
- MITM: 2 lines

## 说明
- 根目录 Ronghemokuai.sgmodule 仍是正式导入入口。
- Rewrite/Sources/ 保存从主模块拆分出来的结构化片段。
- Release/Ronghemokuai.sgmodule 是由 Sources 重新拼接得到的发布副本。
- 启用根目录自动生成前，必须先确认 Release 与根目录主模块一致。
