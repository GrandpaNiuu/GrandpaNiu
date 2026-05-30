#!/usr/bin/env python3
"""Build independent Release/*.sgmodule variants for Shadowrocket import.

The root Ronghemokuai.sgmodule remains the stable default. This script only
writes additional versioned release files under Release/ and a report.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_module  # noqa: E402

REPORT = ROOT / "reports" / "multi_release_report.md"
BASE_PAGES = "https://grandpaniuu.github.io/GrandpaNiu"
BASE_RAW = "https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main"

VARIANTS = {
    "stable": {
        "file": "Release/Ronghemokuai-stable.sgmodule",
        "name": "GrandpaNiu Stable",
        "role": "默认正式版，优先长期稳定",
        "publish": "yes",
    },
    "stable-plus": {
        "file": "Release/Ronghemokuai-stable-plus.sgmodule",
        "name": "GrandpaNiu Stable Plus",
        "role": "常用 App 增强测试版，不默认发布",
        "publish": "no",
    },
    "lite": {
        "file": "Release/Ronghemokuai-lite.sgmodule",
        "name": "GrandpaNiu Lite",
        "role": "低耗电参考版，不默认发布",
        "publish": "no",
    },
    "full": {
        "file": "Release/Ronghemokuai-full.sgmodule",
        "name": "GrandpaNiu Full",
        "role": "全量排查测试版，不默认发布",
        "publish": "no",
    },
}


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


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


def update_header(text: str, profile: str, meta: dict[str, str]) -> str:
    pages_url = f"{BASE_PAGES}/{meta['file']}"
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
    text = re.sub(r"^#!update-url=.*$", f"#!update-url={pages_url}", text, flags=re.M)
    text = re.sub(r"^#!name=.*$", f"#!name={meta['name']}", text, flags=re.M)
    text = re.sub(r"^#!desc=.*$", f"#!desc={today} / {profile}", text, flags=re.M)
    text = re.sub(r"^# update-date:.*$", f"# update-date: {today}", text, flags=re.M)
    banner = f"# profile: {profile}\n# profile-role: {meta['role']}\n# profile-update-url: {pages_url}"
    if "# profile:" not in text:
        text = text.replace("[Rule]", banner + "\n[Rule]", 1)
    return text


def build_variant(profile: str, meta: dict[str, str]) -> dict[str, str]:
    text = build_module.build_from_sources(profile)
    build_module.validate(text)
    text = update_header(text, profile, meta)
    path = ROOT / meta["file"]
    write(path, text)
    return {
        "profile": profile,
        "file": meta["file"],
        "name": meta["name"],
        "role": meta["role"],
        "publish": meta["publish"],
        "lines": str(len(text.splitlines())),
        "scripts": str(count_scripts(text)),
        "mitm": str(count_mitm(text)),
        "pages_url": f"{BASE_PAGES}/{meta['file']}",
        "raw_url": f"{BASE_RAW}/{meta['file']}",
    }


def main() -> None:
    rows = [build_variant(profile, meta) for profile, meta in VARIANTS.items()]
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# 多版本发布报告",
        "",
        f"生成时间：{now}",
        "",
        "默认根目录 `Ronghemokuai.sgmodule` 仍由 stable 构建并同步；以下文件是 Shadowrocket 独立导入版本。",
        "",
        "| Profile | 文件 | 脚本数 | MITM 数量 | 默认发布 | 用途 | Pages 地址 | Raw 地址 |",
        "|---|---|---:|---:|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['profile']} | `{row['file']}` | {row['scripts']} | {row['mitm']} | {row['publish']} | {row['role']} | {row['pages_url']} | {row['raw_url']} |"
        )
    lines += [
        "",
        "## 使用规则",
        "",
        "- Shadowrocket 中不要同时启用多个版本。",
        "- 日常使用 stable。",
        "- 想测试更多 App 覆盖时使用 stable-plus。",
        "- 手机发热、耗电或异常时使用 lite。",
        "- full 只用于排查，不建议长期启用。",
        "",
    ]
    write(REPORT, "\n".join(lines))
    print(f"Built {len(rows)} release variants and wrote {REPORT}")


if __name__ == "__main__":
    main()
