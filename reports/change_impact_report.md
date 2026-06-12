# 变更影响报告

- 生成时间：2026-06-13 00:09:39 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `README.md`
- `Release/README.md`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Rewrite/Registry.md`
- `Web/catalog.md`
- `Web/release-links.json`
- `reports/release_modules_report.md`
- `scripts/build_release_modules.py`
- `scripts/build_web_catalog.py`

## 新增文件

- 无

## 删除文件

- 无

## 修改文件

- `README.md`
- `Release/README.md`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Rewrite/Registry.md`
- `Web/catalog.md`
- `Web/release-links.json`
- `reports/release_modules_report.md`
- `scripts/build_release_modules.py`
- `scripts/build_web_catalog.py`

## 影响的模块层

- Other
- README/docs
- Scripts/maintenance

## 可能影响的 App

- Spotify

## 风险判断

- 是否涉及脚本：是
- 是否涉及 MITM：是
- 是否涉及 Body Rewrite：否
- 是否涉及远程规则源：否
- 是否需要测试 Spotify：是
- 是否需要测试 YouTube：按需
- 是否需要测试知乎：按需
- 是否需要测试登录/支付/验证码：按需

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，优先回滚最近一次 Fusion 输出提交。
- 回滚后运行 `build_module.py --build --profile fusion`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
