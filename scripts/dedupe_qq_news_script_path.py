#!/usr/bin/env python3
"""Remove the redundant QQ News legacy script entry.

The retained entry `cmp_block_097_ad` uses the same script-path and has broader
coverage than `legacy_safe_qqnews`, so removing the legacy line reduces one
script entry without reducing URL coverage.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP_CLEAN = ROOT / "Scripts" / "app-clean.conf"
REPORT = ROOT / "reports" / "script_dedupe_report.md"
LEGACY_NAME = "legacy_safe_qqnews"
RETAINED_NAME = "cmp_block_097_ad"
SCRIPT_PATH = "https://raw.githubusercontent.com/app2smile/rules/master/js/qq-news.js"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    original = read(APP_CLEAN)
    lines = original.splitlines()
    removed: list[str] = []
    kept: list[str] = []
    retained_present = any(line.startswith(f"{RETAINED_NAME} =") and SCRIPT_PATH in line for line in lines)

    if not retained_present:
        raise SystemExit(f"Retained QQ News entry missing or wrong script-path: {RETAINED_NAME}")

    for line in lines:
        if line.startswith(f"{LEGACY_NAME} =") and SCRIPT_PATH in line:
            removed.append(line)
            continue
        kept.append(line)

    if removed:
        write(APP_CLEAN, "\n".join(kept).rstrip() + "\n")

    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    report = [
        "# 脚本去重报告",
        "",
        f"生成时间：{now}",
        "",
        "## QQ News script-path 去重",
        "",
        f"- 保留入口：`{RETAINED_NAME}`",
        f"- 移除入口：`{LEGACY_NAME}`" if removed else f"- 移除入口：无，`{LEGACY_NAME}` 已不存在",
        f"- script-path：`{SCRIPT_PATH}`",
        "- 功能判断：保留入口覆盖 `legacy_safe_qqnews` 的 URL 范围，并额外覆盖 `gw/page/event_detail`。",
        "- 操作类型：去重，不是功能删除。",
        "- 后续要求：重新构建四个 Release 版本，并运行 validate_repository.py / validate_profiles.py。",
        "",
        "## 被移除的原始行",
        "",
    ]
    report += [f"```text\n{line}\n```" for line in removed] if removed else ["- 无"]
    write(REPORT, "\n".join(report) + "\n")
    print(f"QQ News dedupe complete. removed={len(removed)}")


if __name__ == "__main__":
    main()
