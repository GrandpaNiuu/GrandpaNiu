# 脚本瘦身回滚报告

生成时间：2026-06-12 03:06:29 +0800

## 回滚条件

如果本批 App 在 Stable 中出现页面异常、广告残留加重、JSON 解析异常、加载失败，应回滚本次迁移。

## 回滚步骤

1. 从 `Rewrite/Profiles/stable.conf` 移除 `app_cleaner_active = Scripts/app-cleaner-active.conf`。
2. 从 `Rewrite/Profiles/stable-plus.conf` 移除 `app_cleaner_active = Scripts/app-cleaner-active.conf`。
3. 将下方旧入口恢复到对应文件。
4. 重新运行 build / finalize / build_release_variants / validate。

## 需要恢复的旧入口

### `Scripts/app-clean.conf`

- 当前脚本运行时没有新移除旧入口；如需回滚，请从 Git 历史恢复旧入口。

### `Rewrite/Sources/Script.conf`

- 当前脚本运行时没有新移除旧入口；如需回滚，请从 Git 历史恢复旧入口。

## 验证命令

```bash
python3 scripts/build_module.py --build --profile fusion
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_repository.py
python3 scripts/validate_profiles.py
python3 scripts/repository_health_check.py
```
