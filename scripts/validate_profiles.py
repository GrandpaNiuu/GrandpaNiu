#!/usr/bin/env python3
"""Validate stable, stable-plus, lite and full profiles without syncing Root."""

from __future__ import annotations

import datetime as dt
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "Release" / "Ronghemokuai.sgmodule"
REPORT = ROOT / "reports" / "profile_validation_report.md"
FACTORY_REPORT = ROOT / "reports" / "module_factory_report.md"
FACTORY_DIFF = ROOT / "reports" / "module_factory_diff_report.md"
PROFILES = {
    "stable": ("默认正式版", "是"),
    "stable-plus": ("常用 App 增强测试版", "否"),
    "lite": ("低耗电参考版", "否"),
    "full": ("全覆盖测试版", "否"),
}
REQUIRED_MARKERS = (
    "[Rule]",
    "[URL Rewrite]",
    "[Header Rewrite]",
    "[Body Rewrite]",
    "[Map Local]",
    "[Script]",
    "[MITM]",
    "spotify-json",
    "spotify-proto",
    "youtube.response",
    "zhihu-enhance",
    "#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def count_scripts(text: str) -> int:
    start = text.find("[Script]")
    end = text.find("[MITM]")
    if start < 0 or end < 0 or end <= start:
        return 0
    return len([line for line in text[start:end].splitlines() if line.strip() and not line.lstrip().startswith("#") and not line.startswith("[")])


def count_mitm(text: str) -> int:
    start = text.find("[MITM]")
    if start < 0:
        return 0
    total = 0
    for line in text[start:].splitlines():
        if line.strip().startswith("hostname ="):
            total += len([h.strip() for h in line.split("=", 1)[1].split(",") if h.strip() and h.strip() != "%APPEND%"])
    return total


def validate_profile(profile: str) -> dict[str, str]:
    proc = subprocess.run(
        [sys.executable, "scripts/build_module.py", "--build", "--profile", profile],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    text = read(RELEASE)
    missing = [marker for marker in REQUIRED_MARKERS if marker not in text]
    return {
        "profile": profile,
        "ok": "是" if proc.returncode == 0 and not missing else "否",
        "markers": "通过" if not missing else "缺少：" + ", ".join(missing),
        "scripts": str(count_scripts(text)),
        "mitm": str(count_mitm(text)),
        "stdout": (proc.stdout + proc.stderr).strip() or "无输出",
    }


def main() -> None:
    release_backup = read(RELEASE)
    report_backup = read(FACTORY_REPORT)
    diff_backup = read(FACTORY_DIFF)
    rows = []
    try:
        for profile in PROFILES:
            rows.append(validate_profile(profile))
    finally:
        if release_backup:
            write(RELEASE, release_backup)
        if report_backup:
            write(FACTORY_REPORT, report_backup)
        if diff_backup:
            write(FACTORY_DIFF, diff_backup)

    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# Profile 全量验证报告",
        "",
        f"生成时间：{now}",
        "",
        "说明：本脚本只验证 stable / stable-plus / lite / full 是否可以构建，不会把 lite、stable-plus 或 full 同步到根目录主模块。验证结束后会恢复原 Release 和工厂报告。",
        "",
        "| Profile | 构建结果 | 必要标记 | 脚本数 | MITM 数量 | 适用场景 | 是否可发布 |",
        "|---|---|---|---:|---:|---|---|",
    ]
    for row in rows:
        usage, publishable = PROFILES[row["profile"]]
        lines.append(f"| {row['profile']} | {row['ok']} | {row['markers']} | {row['scripts']} | {row['mitm']} | {usage} | {publishable} |")
    lines += [
        "",
        "## 规则",
        "",
        "- stable 是默认正式版，可以发布。",
        "- stable-plus 是常用 App 增强测试版，不默认发布。",
        "- lite 是低耗电参考版，不默认发布。",
        "- full 是全覆盖测试版，不默认发布。",
        "- 默认 workflow 仍应使用 stable，不允许默认使用 stable-plus 或 full。",
        "- 必要标记用于确认模块结构和已纳入脚本入口存在，不代表某几个 App 被单独设为例外。",
        "",
    ]
    write(REPORT, "\n".join(lines))
    failed = [row["profile"] for row in rows if row["ok"] != "是"]
    if failed:
        raise SystemExit("Profile validation failed: " + ", ".join(failed))
    print(f"Profile validation report written to {REPORT}")


if __name__ == "__main__":
    main()
