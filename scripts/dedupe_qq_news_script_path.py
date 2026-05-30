#!/usr/bin/env python3
"""Migrate QQ News and VGTime old entries to app-cleaner active.

This script removes only the old entries now covered by Scripts/app-cleaner.js:
- cmp_block_097_ad        QQ News upstream app2smile
- cmp_allad_046_txnews    QQ News upstream zirawell fork
- cmp_block_098_vgtime    VGTime upstream app2smile

It applies the same cleanup to Scripts/app-clean.conf and Rewrite/Sources/Script.conf
so source_script_compat does not reintroduce old entries during builds.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    ROOT / "Scripts" / "app-clean.conf",
    ROOT / "Rewrite" / "Sources" / "Script.conf",
]
REPORT = ROOT / "reports" / "script_dedupe_report.md"
ROLLBACK = ROOT / "reports" / "script_consolidation_rollback_report.md"
ACTIVE_ENTRY = ROOT / "Scripts" / "app-cleaner-active.conf"
REMOVED_NAMES = {
    "cmp_block_097_ad": "QQ News app2smile entry",
    "cmp_allad_046_txnews": "QQ News zirawell entry",
    "cmp_block_098_vgtime": "VGTime app2smile entry",
    "legacy_safe_qqnews": "Legacy QQ News duplicate entry",
}
PROTECTED_NAMES = {
    "spotify-json",
    "spotify-proto",
    "youtube.response",
    "zhihu-enhance",
    "cmp_block_084_json",
    "cmp_block_085_proto",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def script_name(line: str) -> str:
    if "=" not in line:
        return ""
    return line.split("=", 1)[0].strip()


def clean_file(path: Path) -> list[str]:
    original = read(path)
    kept: list[str] = []
    removed: list[str] = []
    for line in original.splitlines():
        name = script_name(line)
        if name in PROTECTED_NAMES:
            kept.append(line)
            continue
        if name in REMOVED_NAMES:
            removed.append(line)
            continue
        kept.append(line)
    if removed:
        write(path, "\n".join(kept).rstrip() + "\n")
    return removed


def main() -> None:
    active = read(ACTIVE_ENTRY)
    if "app-cleaner-active-qqnews-vgtime" not in active:
        raise SystemExit("Active app-cleaner entry missing: Scripts/app-cleaner-active.conf")
    if "app-cleaner.js" not in active:
        raise SystemExit("Active app-cleaner entry does not point to Scripts/app-cleaner.js")

    removed_by_file: dict[str, list[str]] = {}
    for target in TARGETS:
        removed_by_file[target.relative_to(ROOT).as_posix()] = clean_file(target)

    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    total_removed = sum(len(items) for items in removed_by_file.values())
    app_clean_removed = len(removed_by_file.get("Scripts/app-clean.conf", []))

    report = [
        "# 脚本去重与 app-cleaner active 迁移报告",
        "",
        f"生成时间：{now}",
        "",
        "## 本次迁移",
        "",
        "- 迁移范围：QQ News + VGTime",
        "- 新承接入口：`Scripts/app-cleaner-active.conf` / `app-cleaner-active-qqnews-vgtime`",
        "- 新承接脚本：`Scripts/app-cleaner.js`",
        f"- Scripts/app-clean.conf 移除旧入口数量：{app_clean_removed}",
        f"- 所有源文件合计移除旧入口数量：{total_removed}",
        "- 新增 active 入口数量：1",
        "- 目标：Stable 脚本数从 104 降到 102。",
        "",
        "## 移除的旧入口",
        "",
    ]
    for file_name, removed in removed_by_file.items():
        report += [f"### `{file_name}`", ""]
        if removed:
            for line in removed:
                name = script_name(line)
                report += [f"#### `{name}`", "", f"- 说明：{REMOVED_NAMES.get(name, '旧入口')}", "", "```text", line, "```", ""]
        else:
            report.append("- 无，目标旧入口已不存在。")
            report.append("")
    report += [
        "## 不变范围",
        "",
        "- 不动 Spotify。",
        "- 不动 YouTube。",
        "- 不动知乎增强。",
        "- 不动 Tieba JSON / proto。",
        "- 不动登录、支付、验证码、银行相关条目。",
        "",
    ]
    write(REPORT, "\n".join(report).rstrip() + "\n")

    rollback = [
        "# 脚本瘦身回滚报告",
        "",
        f"生成时间：{now}",
        "",
        "## 回滚条件",
        "",
        "如果 QQ News 或 VGTime 在 Stable 中出现页面异常、广告残留加重、JSON 解析异常、加载失败，应回滚本次迁移。",
        "",
        "## 回滚步骤",
        "",
        "1. 从 `Rewrite/Profiles/stable.conf` 移除 `app_cleaner_active = Scripts/app-cleaner-active.conf`。",
        "2. 从 `Rewrite/Profiles/stable-plus.conf` 移除 `app_cleaner_active = Scripts/app-cleaner-active.conf`。",
        "3. 将下方旧入口恢复到对应文件。",
        "4. 重新运行 build / finalize / build_release_variants / validate。",
        "",
        "## 需要恢复的旧入口",
        "",
    ]
    for file_name, removed in removed_by_file.items():
        rollback += [f"### `{file_name}`", ""]
        if removed:
            for line in removed:
                rollback += ["```text", line, "```", ""]
        else:
            rollback.append("- 当前脚本运行时没有新移除旧入口；如需回滚，请从 Git 历史恢复旧入口。")
            rollback.append("")
    rollback += [
        "## 验证命令",
        "",
        "```bash",
        "python3 scripts/build_module.py --build --profile stable",
        "python3 scripts/factory_finalize.py --sync-root",
        "python3 scripts/build_release_variants.py",
        "python3 scripts/validate_repository.py",
        "python3 scripts/validate_profiles.py",
        "python3 scripts/repository_health_check.py",
        "```",
        "",
    ]
    write(ROLLBACK, "\n".join(rollback).rstrip() + "\n")
    print(f"QQ News/VGTime active migration complete. removed={total_removed}, app_clean_removed={app_clean_removed}")


if __name__ == "__main__":
    main()
