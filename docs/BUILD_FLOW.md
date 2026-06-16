# 模块构建流程

`Ronghemokuai.sgmodule` 是正式导入入口，但它是构建产物，不是长期手工维护源头。

## 源头

日常维护优先修改：

- `Rules/*.list`
- `Scripts/*.conf`
- `Rewrite/Sources/*.conf`
- `Rewrite/Remotes/sources.json`
- `Rewrite/Remotes/candidates.json`
- `Rewrite/Profiles/*.conf`

## 构建链路

```text
Rules + Scripts + Rewrite/Sources + Rewrite/Remotes + Rewrite/Profiles
        -> scripts/build_module.py --build --profile fusion
        -> Release/Ronghemokuai.sgmodule
        -> scripts/factory_finalize.py --sync-root
        -> Ronghemokuai.sgmodule
```

`--extract-from-root` 只用于初始化或灾难恢复，不是日常构建入口。

## Profile 定位

| Profile | 用途 | 是否默认发布 |
|---|---|---|
| `stable.conf` | 默认正式版 | 是 |
| `lite.conf` | 低耗电参考版 | 否 |
| `full.conf` | 全覆盖测试版 | 否 |

构建脚本先生成 `Release/Ronghemokuai.sgmodule`，再由 `factory_finalize.py --sync-root` 同步到根目录 `Ronghemokuai.sgmodule`。profile 中不再使用容易误导的 `write_release_only` 字段。

## 关键保护项

构建结果必须保留：

- `[Rule]`
- `[URL Rewrite]`
- `[Header Rewrite]`
- `[Body Rewrite]`
- `[Map Local]`
- `[Script]`
- `[MITM]`
- `spotify-json`
- `spotify-proto`
- `youtube.response`
- `zhihu-enhance`
- `#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule`

Root 与 Release 最终必须完全一致。

## 兼容层

`source_rule_compat` 和 `source_script_compat` 是过渡兼容层。不要直接关闭。先运行：

```text
python3 scripts/audit_compat_sources.py
```

查看 `reports/compat_migration_report.md`，确认兼容层内容是否已迁移到 `Rules/*.list` 和 `Scripts/*.conf`。

## 自动维护边界

- `daily-module-update.yml` 只做日期、结构、链接和验证报告。
- `daily-invalid-source-repair.yml` 连续失效后才安全处理。
- `upstream-collect.yml` 只读取可信候选池，不全网搜索。
- `repository-health.yml` 用于治理状态检查。

脚本默认 pending，不直接进入 stable。Spotify、YouTube、知乎、登录、支付、验证码、银行、微信、支付宝优先保护。
