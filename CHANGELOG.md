# 变更记录

## 2026-05-30

- 中文化 `README.md`，补充快速导入、模块工厂流程、重点生效对象、维护入口、安全边界和常见问题。
- 新增知乎增强净化层：`Scripts/zhihu-enhance.js` 与 `Scripts/zhihu-enhance.conf`，只处理广告卡片、推荐广告、商业字段，不处理会员、登录、支付、账号或付费内容。
- 将 `Rewrite/Profiles/stable.conf` 接入 `zhihu-enhance`。
- 新增 `Rewrite/Profiles/lite.conf` 低耗电参考 profile。
- 新增 `docs/PERFORMANCE.md`，说明耗电来源、判断标准和 lite profile 用法。
- 新增 `scripts/validate_repository.py`，作为阻断型质量门禁。
- 新增 `scripts/repository_health_check.py`，生成 `reports/repository_health_report.md`。
- 新增 `.github/workflows/repository-health.yml`，用于每周仓库健康检查。
- 新增 `docs/QUALITY_GATE.md`，定义质量门禁、阻断项、提醒项和上线前检查。
- 新增 `docs/RELEASE.md`，定义发布、测试和回滚标准。
- 将 `scripts/audit_repair_invalid_sources.py` 改为 source-first 失效源审计和保守修复。
- 更新 `daily-invalid-source-repair.yml`，失效源修复后重新构建 Release、同步 Root 并运行验证。
- 更新 `module-factory-build.yml` 与 `upstream-collect.yml`，加入统一验证流程。
- 扩展 `Rewrite/Remotes/candidates.json` 的低风险候选源池，仍保持脚本 pending。
- 更新 `docs/COVERAGE.md`，同步 README 的重点生效对象，明确 Spotify、YouTube、知乎、Bilibili 的覆盖状态。
- 更新 `docs/TROUBLESHOOTING.md`，新增知乎、Bilibili、耗电异常排查。
- 更新 `docs/SCOPE.md`，补充知乎广告卡片净化、Bilibili 局部净化、源头驱动模块构建和低耗电维护边界。
- 中文化 `docs/FACTORY_FLOW.md`，明确源头驱动流程、报告文件、自动维护边界和保守候选源收集原则。
- 候选源收集策略保持保守：不开启全网大规模自动收集，只收集来源可信、改动可回滚、报告可验证的内容。

## 2026-05-29

- Added a conservative upstream candidate collection system with `Rewrite/Remotes/candidates.json`, `scripts/collect_upstreams.py`, `.github/workflows/upstream-collect.yml`, and `reports/upstream_collect_report.md`.
- The upstream collector is candidate-list driven, weekly by default, duplicate-aware, risk-keyword aware, and keeps scripts pending unless explicitly approved.
- Refactored the module factory into a source-driven build: `Rules/`, `Scripts/`, `Rewrite/Sources/`, `Rewrite/Remotes/sources.json`, and `Rewrite/Profiles/stable.conf` are now the maintained inputs.
- Updated `scripts/build_module.py` so the default daily path builds from source inputs instead of extracting from the root module.
- Updated `scripts/factory_finalize.py` so the default path validates `Release/Ronghemokuai.sgmodule` and syncs it to the root module without rewriting source files.
- Updated `.github/workflows/module-factory-build.yml` to compile scripts, build from sources, finalize with `--sync-root`, and verify Root/Release equality.
- Preserved Spotify playback protection, Spotify header rewrite, YouTube Enhance, and the GitHub Pages update URL.
- Moved misplaced app ad reject rules out of `Rules/spotify-direct.list` and into `Rules/app-clean.list`.
- Added `backup/Ronghemokuai.before-factory-refactor.sgmodule` as a pre-refactor rollback point.
- Added `reports/factory_refactor_report.md`.

## 2026-05-28

- Completed the long-term maintenance file set and verified README maintenance links point to existing files.
- Added the daily invalid-source repair system with a 2-day confirmed failure threshold.
- Added stable backup files under `backup/`.
- Added `docs/COVERAGE.md` and `docs/SCOPE.md`.

## 2026-05-25

- Added one-click import buttons, `redirect.html`, and `import.html`.
- Added the daily module update workflow.
- Added maintenance and troubleshooting documentation.
- Added Spotify whitelist handling and Spotify / YouTube core checks.
- Registered trusted remote sources such as Remote AdBlock Hub, blackmatrix7, Cats-Team, zirawell/R-Store, fmz200/wool_scripts, and app2smile references.
- Added legacy selected-rule migration and reports.
- Added safe module refinement scripts for duplicate checks, script grouping, and core marker validation.
