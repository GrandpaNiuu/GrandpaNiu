# 变更影响报告

- 生成时间：2026-05-31 07:36:17 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `Scripts/app-cleaner-active.conf`

## 新增文件

- 无

## 删除文件

- 无

## 修改文件

- `Scripts/app-cleaner-active.conf`

## 影响的模块层

- Scripts

## 可能影响的 App

- 酷安
- 淘宝
- 闲鱼
- 京东
- 拼多多
- 美团
- 滴滴
- 高德地图
- 喜马拉雅
- 小宇宙
- Reddit

## 风险判断

- 是否涉及脚本：是
- 是否涉及 MITM：否
- 是否涉及 Body Rewrite：否
- 是否涉及远程规则源：否
- 是否需要测试 Spotify：是
- 是否需要测试 YouTube：是
- 是否需要测试知乎：是
- 是否需要测试登录/支付/验证码：是

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，可用 `backup/Ronghemokuai.stable.sgmodule` 人工恢复。
- 回滚后运行 `build_module.py --build --profile stable`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
