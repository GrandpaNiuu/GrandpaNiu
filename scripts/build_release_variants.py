#!/usr/bin/env python3
"""Generate the single fusion release report.

The repository now publishes one entry only:

- Ronghemokuai.sgmodule
- Release/Ronghemokuai.sgmodule

Former stable / stable-plus / lite / full artifacts are no longer public entry
points. The maintained build profile is Rewrite/Profiles/fusion.conf.
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_module  # noqa: E402

REPORT = ROOT / "reports" / "multi_release_report.md"
RELEASE = ROOT / "Release" / "Ronghemokuai.sgmodule"
ROOT_MODULE = ROOT / "Ronghemokuai.sgmodule"
BASE_PAGES = "https://grandpaniuu.github.io/GrandpaNiu"
BASE_RAW = "https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main"
PROFILE = "fusion"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def count_mitm(text: str) -> int:
    start = text.find("[MITM]")
    if start < 0:
        return 0
    count = 0
    for line in text[start:].splitlines():
        if not line.strip().startswith("hostname ="):
            continue
        value = line.split("=", 1)[1].replace("%APPEND%", "")
        count += len([host.strip() for host in value.split(",") if host.strip()])
    return count


def count_scripts(text: str) -> int:
    start = text.find("[Script]")
    end = text.find("[MITM]")
    if start < 0 or end < 0 or end <= start:
        return 0
    return len([
        line for line in text[start:end].splitlines()
        if line.strip() and not line.lstrip().startswith("#") and not line.startswith("[")
    ])


def main() -> None:
    text = build_module.build_from_sources(PROFILE)
    build_module.validate(text)
    write(RELEASE, text)

    root_text = read(ROOT_MODULE)
    same_as_root = root_text.strip() == text.strip()
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    pages_url = f"{BASE_PAGES}/Ronghemokuai.sgmodule"
    raw_url = f"{BASE_RAW}/Ronghemokuai.sgmodule"
    release_pages_url = f"{BASE_PAGES}/Release/Ronghemokuai.sgmodule"
    release_raw_url = f"{BASE_RAW}/Release/Ronghemokuai.sgmodule"

    lines = [
        "# 单一融合版发布报告",
        "",
        f"生成时间：{now}",
        "",
        "本仓库现在只发布一个融合模块，不再拆分 Stable / Stable Plus / Lite / Full 给用户选择。",
        "",
        "| Profile | 文件 | 脚本数 | MITM 数量 | 默认发布 | 用途 | Pages 地址 | Raw 地址 |",
        "|---|---|---:|---:|---|---|---|---|",
        f"| fusion | `Ronghemokuai.sgmodule` | {count_scripts(text)} | {count_mitm(text)} | yes | 单一融合模块入口 | {pages_url} | {raw_url} |",
        f"| fusion | `Release/Ronghemokuai.sgmodule` | {count_scripts(text)} | {count_mitm(text)} | yes | Release 同步入口 | {release_pages_url} | {release_raw_url} |",
        "",
        "## 使用规则",
        "",
        "- Shadowrocket / Surge 只导入 `Ronghemokuai.sgmodule`。",
        "- 不再要求用户判断 Stable、Stable Plus、Lite、Full。",
        "- 规则、脚本、Rewrite、MITM 的维护仍然通过源头文件完成。",
        "- 若某个 App 误伤，直接在 fusion 源头层回滚对应规则或 hostname。",
        "",
        "## 构建状态",
        "",
        f"- 构建 profile：{PROFILE}",
        f"- Release 与 Root 当前是否一致：{'是' if same_as_root else '否，后续 factory_finalize.py 会同步 Root'}",
        "- 旧多版本文件不再作为公开入口。",
        "",
    ]
    write(REPORT, "\n".join(lines))
    print(f"Built single fusion release report and wrote {REPORT}")


if __name__ == "__main__":
    main()
