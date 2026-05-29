# 模块工厂流程

本文件说明 GrandpaNiu 仓库的源头驱动构建方式。

## 核心原则

`Ronghemokuai.sgmodule` 是正式导入结果，不是长期手工维护源头。

日常维护优先修改：

```text
Rules/*.list
Scripts/*.conf
Rewrite/Sources/*.conf
Rewrite/Remotes/sources.json
Rewrite/Remotes/candidates.json
Rewrite/Profiles/stable.conf
Rewrite/Profiles/lite.conf
```

## 完整流程

```text
Rules + Scripts + Rewrite/Sources + Rewrite/Remotes + Rewrite/Profiles
        -> scripts/build_module.py --build --profile stable
        -> Release/Ronghemokuai.sgmodule
        -> scripts/factory_finalize.py --sync-root
        -> Ronghemokuai.sgmodule
```

`--extract-from-root` 只用于初始化或恢复源头文件，不作为日常构建路径。

## 目录职责

| 路径 | 职责 |
|---|---|
| `Rewrite/Profiles/stable.conf` | 默认正式构建 profile |
| `Rewrite/Profiles/lite.conf` | 低耗电参考 profile，不默认发布 |
| `Rewrite/Remotes/sources.json` | 已启用可信远程规则源 |
| `Rewrite/Remotes/candidates.json` | 可信候选源池，只收集来源可信、改动可回滚、报告可验证的来源 |
| `Rules/*.list` | 本地规则源 |
| `Scripts/spotify.conf` | Spotify 脚本入口，只放 Spotify 相关脚本 |
| `Scripts/youtube.conf` | YouTube 脚本入口，只放 YouTube 相关脚本 |
| `Scripts/zhihu-enhance.conf` | 知乎增强净化脚本入口 |
| `Scripts/app-clean.conf` | 普通 App 净化脚本入口 |
| `Rewrite/Sources/*.conf` | Meta、Rewrite、Body Rewrite、Map Local、MITM 片段 |
| `Release/Ronghemokuai.sgmodule` | 工厂生成副本 |
| `Ronghemokuai.sgmodule` | 正式导入入口 |

## 构建命令

正式构建：

```text
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
```

低耗电测试构建：

```text
python3 scripts/build_module.py --build --profile lite
```

## 关键保护项

构建结果必须保留：

```text
[Rule]
[URL Rewrite]
[Header Rewrite]
[Body Rewrite]
[Map Local]
[Script]
[MITM]
spotify-json
spotify-proto
youtube.response
zhihu-enhance
#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule
```

Root 与 Release 最终必须一致。

## 自动维护边界

| 工作流 | 作用 |
|---|---|
| `module-factory-build.yml` | 从源头构建 Release 并同步 Root |
| `daily-module-update.yml` | 每日结构和链接检查 |
| `daily-invalid-source-repair.yml` | 连续确认失败后保守处理失效源 |
| `upstream-collect.yml` | 只读取候选池，保守收集可信来源 |
| `repository-health.yml` | 生成仓库健康报告 |

候选源收集不追求数量，只接受来源可信、改动可回滚、报告可验证的内容。脚本默认 pending，不直接进入 stable。

## 报告文件

| 报告 | 用途 |
|---|---|
| `reports/module_factory_report.md` | 构建来源、profile、区块行数、重复检查 |
| `reports/module_factory_diff_report.md` | Root 与 Release 差异 |
| `reports/factory_finalize_report.md` | 同步结果 |
| `reports/repository_health_report.md` | 仓库健康状态 |
| `reports/upstream_collect_report.md` | 候选源收集结果 |
| `reports/invalid_sources_report.md` | 失效源审计结果 |

## 维护方法

1. 先改源头文件。
2. 再运行构建和同步。
3. 再运行统一验证。
4. 最后在 Shadowrocket 中测试 Spotify、YouTube、知乎、Bilibili、登录、支付、验证码和常用 App。
