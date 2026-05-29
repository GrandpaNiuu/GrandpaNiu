# 发布与回滚标准

本文件说明 GrandpaNiu 模块工厂的发布、测试和回滚方式。

## 发布产物

正式导入入口：

```text
Ronghemokuai.sgmodule
```

工厂生成副本：

```text
Release/Ronghemokuai.sgmodule
```

规则：

```text
Root 与 Release 必须一致。
Root 是给 Shadowrocket / Surge 导入的最终结果。
Release 是构建过程中的发布副本。
```

## 正式发布流程

默认发布使用 stable profile：

```text
python3 -m py_compile scripts/build_module.py scripts/factory_finalize.py scripts/audit_repair_invalid_sources.py scripts/collect_upstreams.py scripts/validate_repository.py scripts/repository_health_check.py
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

GitHub Actions 对应：

```text
Actions -> Module Factory Build -> Run workflow
```

## 低耗电测试流程

低耗电参考 profile：

```text
Rewrite/Profiles/lite.conf
```

测试构建命令：

```text
python3 scripts/build_module.py --build --profile lite
```

注意：lite 不是默认正式发布版本。除非经过 24 小时实测，否则不要直接替换 stable 发布结果。

## 发布前检查

发布前必须确认：

```text
Root 与 Release diff lines = 0
validate_repository.py 通过
repository_health_check.py 通过
Spotify 不跳歌
YouTube 不转圈
知乎不空白
登录 / 支付 / 验证码正常
README 链接没有失效
```

## Shadowrocket 测试流程

1. 更新模块。
2. 更新脚本。
3. 更新全部资源。
4. 杀后台重开重点 App。
5. 测试 Spotify 连续播放。
6. 测试 YouTube 播放。
7. 测试知乎信息流与回答页。
8. 测试淘宝、京东、拼多多、美团等常用页面。
9. 测试微信、支付宝、银行 App 登录、支付、验证码。

## 回滚方式

优先级从高到低：

1. 使用 Git 提交历史回滚最近一次改动。
2. 使用 `backup/Ronghemokuai.stable.sgmodule`。
3. 使用 `backup/Ronghemokuai.before-factory-refactor.sgmodule`。
4. 临时关闭问题 profile 或问题脚本入口。

回滚后必须运行：

```text
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

## 不能直接发布的情况

出现以下情况不要发布：

```text
Root 与 Release 不一致
缺少 Spotify / YouTube / 知乎核心脚本
出现重复脚本名
出现重复 MITM hostname
新增脚本未经人工审核
新增规则可能影响登录、支付、验证码
远程源大面积网络失败
Shadowrocket 电池异常升高且原因未确认
```
