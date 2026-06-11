# 仓库健康检查报告

生成时间：2026-06-11 23:58:31 +0800

## 总体状态

- 阻断问题：0
- Root 与 Release 一致：是
- GrandpaNiu = 默认 Fusion：是
- fusion profile：就绪
- validate_repository.py：通过
- node --check Scripts/app-cleaner.js：通过
- 脚本总数：46
- MITM hostname 数量：1072

## 区块检查

- [Rule]：642 行
- [URL Rewrite]：1644 行
- [Header Rewrite]：1 行
- [Body Rewrite]：455 行
- [Map Local]：149 行
- [Script]：46 行
- [MITM]：1 行

## 阻断问题

- 无

## 缺少文件

- 无

## 缺少 workflow

- 无

## 主模块缺少标记

- 无

## 重复脚本名

- 无

## 重复 MITM hostname

- 无

## Workflow 配置摘要

- `.github/workflows/module-factory-build.yml`：contents: write；concurrency；fusion；regenerate retry
- `.github/workflows/daily-module-update.yml`：contents: write；concurrency；fusion；regenerate retry
- `.github/workflows/daily-audit-and-repair.yml`：contents: write；concurrency；fusion；regenerate retry
- `.github/workflows/daily-invalid-source-repair.yml`：contents: write；concurrency；fusion；regenerate retry
- `.github/workflows/upstream-collect.yml`：contents: write；concurrency；fusion；regenerate retry
- `.github/workflows/repository-health.yml`：contents: write；concurrency；fusion；regenerate retry

## validate_repository.py 输出

```text
Repository validation passed.
```

## node --check 输出

```text
无输出
```

## 维护边界

- 所有修改应 source-first，先改 Rules / Scripts / Rewrite/Sources / Rewrite/Remotes / Rewrite/Profiles/fusion.conf，再构建 Release 和 Root。
- Fusion 是唯一用户入口，不再拆分 Stable / Stable Plus / Lite / Full。
- 旧多版本文件如果存在，只作为历史兼容文件，不作为健康检查阻断项。
