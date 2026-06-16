# 发布与回滚

正式发布入口：

```text
Ronghemokuai.sgmodule
```

工厂生成副本：

```text
Release/Ronghemokuai.sgmodule
```

Root 与 Release 必须一致。

## Profile

- `stable.conf`：默认正式版。
- `lite.conf`：低耗电参考版，不默认发布。
- `full.conf`：全覆盖测试版，不默认发布。

默认 workflow 不使用 full。

## 正式发布流程

```text
python3 -m py_compile scripts/build_module.py scripts/factory_finalize.py scripts/audit_repair_invalid_sources.py scripts/collect_upstreams.py scripts/validate_repository.py scripts/repository_health_check.py
python3 scripts/build_module.py --build --profile fusion
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

## 发布前检查

- Root 与 Release diff lines = 0。
- `validate_repository.py` 通过。
- `repository_health_check.py` 通过。
- `spotify-json`、`spotify-proto`、`youtube.response`、`zhihu-enhance` 存在。
- README 本地链接有效。
- 无重复脚本名。
- 无重复 MITM hostname。

## Shadowrocket 测试

- 更新模块。
- 更新脚本。
- 更新全部资源。
- 测试 Spotify 连续播放。
- 测试 YouTube 首页、搜索、播放和 Shorts。
- 测试知乎首页、回答页、搜索页。
- 测试登录、支付、验证码、银行、微信、支付宝。

## 回滚

优先顺序：

1. 回滚最近提交。
2. 使用 `backup/Ronghemokuai.stable.sgmodule`。
3. 使用 `backup/Ronghemokuai.before-factory-refactor.sgmodule`。

回滚后仍需运行构建、同步、验证和健康检查。
