#!/usr/bin/env python3
"""Migrate QQ News and VGTime old entries to app-cleaner active.

This script removes only the old entries now covered by Scripts/app-cleaner.js:
- cmp_block_097_ad        QQ News upstream app2smile
- cmp_allad_046_txnews    QQ News upstream zirawell fork
- cmp_block_098_vgtime    VGTime upstream app2smile

It does not touch Spotify, YouTube, Zhihu, Tieba JSON/proto, login, payment,
captcha, or bank-related entries.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP_CLEAN = ROOT / "Scripts" / "app-clean.conf"
REPORT = ROOT / "reports" / "script_dedupe_report.md"
ROLLBACK = ROOT / "reports" / "script_consolidation_rollback_report.md"
ACTIVE_ENTRY = ROOT / "Scripts" / "app-cleaner-active.conf"
REMOVED_NAMES = {
    "cmp_block_097_ad": "QQ News app2smile entry",
    "cmp_allad_046_txnews": "QQ News zirawell entry",
    "cmp_block_098_vgtime": "VGTime app2smile entry",
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


def main() -> None:
    original = read(APP_CLEAN)
    active = read(ACTIVE_ENTRY)
    if "app-cleaner-active-qqnews-vgtime" not in active:
        raise SystemExit("Active app-cleaner entry missing: Scripts/app-cleaner-active.conf")
    if "app-cleaner.js" not in active:
        raise SystemExit("Active app-cleaner entry does not point to Scripts/app-cleaner.js")

    kept: list[str] = []
    removed: list[str] = []
    for line in original.splitlines():
        name = script_name(line)
        if name in REMOVED_NAMES:
            removed.append(line)
            continue
        kept.append(line)

    if removed:
        write(APP_CLEAN, "\n".join(kept).rstrip() + "\n")

    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
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
        f"- 移除旧入口数量：{len(removed)}",
        "- 新增 active 入口数量：1",
        f"- 净减少脚本入口：{max(len(removed) - 1, 0)}",
        "- 目标：Stable 脚本数从 104 降到 102。",
        "",
        "## 移除的旧入口",
        "",
    ]
    if removed:
        for line in removed:
            name = script_name(line)
            report += [f"### `{name}`", "", f"- 说明：{REMOVED_NAMES.get(name, '旧入口')}", "", "```text", line, "```", ""]
    else:
        report.append("- 无，旧入口已不存在。")
    report += [
        "",
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
        "3. 将下方旧入口恢复到 `Scripts/app-clean.conf`。",
        "4. 重新运行 build / finalize / build_release_variants / validate。",
        "",
        "## 需要恢复的旧入口",
        "",
    ]
    if removed:
        for line in removed:
            rollback += ["```text", line, "```", ""]
    else:
        rollback.append("- 当前脚本运行时没有新移除旧入口；如需回滚，请从 Git 历史恢复旧入口。")
    rollback += [
        "",
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
    print(f"QQ News/VGTime active migration complete. removed={len(removed)}")


if __name__ == "__main__":
    main()
