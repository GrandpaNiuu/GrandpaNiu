# 维护标准

GrandpaNiu 是源头驱动的 Shadowrocket / Surge 模块工厂。维护时不要把根目录 `Ronghemokuai.sgmodule` 当作唯一源头。

## 日常维护入口

- 规则：`Rules/*.list`
- 脚本：`Scripts/*.conf`
- Rewrite / Body / Map Local / MITM：`Rewrite/Sources/*.conf`
- 远程源：`Rewrite/Remotes/sources.json`
- 候选池：`Rewrite/Remotes/candidates.json`
- Profile：`Rewrite/Profiles/*.conf`

## Profile

- `stable.conf`：默认正式版。
- `lite.conf`：低耗电参考版，不默认发布。
- `full.conf`：全覆盖测试版，不默认发布，可用于未来 extended MITM 或更广覆盖测试。

GitHub Actions 默认仍使用 `stable`。

## 必跑命令

```text
python3 scripts/build_module.py --build --profile fusion
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

## 候选源

- 不开启全网搜索。
- 只使用 `trusted_repositories` 中的候选。
- 低风险 `remote_rule` 可以自动登记。
- 脚本保持 pending，必须人工审核。
- 不使用短链、镜像、`ghproxy`。

## 安全优先级

优先保护：

- Spotify
- YouTube
- 知乎增强
- 登录
- 支付
- 验证码
- 银行
- 微信
- 支付宝

出现异常时，优先检查最近修改的 `Scripts/`、`Rewrite/Sources/MITM.conf`、`Body-Rewrite.conf`、`URL-Rewrite.conf`、`Map-Local.conf` 和 `Rewrite/Remotes/sources.json`。

## 报告

常用报告：

- `reports/module_factory_report.md`
- `reports/module_factory_diff_report.md`
- `reports/factory_finalize_report.md`
- `reports/repository_health_report.md`
- `reports/compat_migration_report.md`
- `reports/app_coverage_matrix.md`
- `reports/change_impact_report.md`
- `reports/workflow_health_report.md`

报告应可读、可追溯、可用于回滚判断。
