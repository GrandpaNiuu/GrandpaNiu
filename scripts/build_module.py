#!/usr/bin/env python3
"""Build and split Ronghemokuai.sgmodule with the repository factory layout."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "Ronghemokuai.sgmodule"
RELEASE = ROOT / "Release" / "Ronghemokuai.sgmodule"
REPORT = ROOT / "reports" / "module_factory_report.md"
SOURCES = ROOT / "Rewrite" / "Sources"

SECTION_ORDER = [
    "Rule",
    "URL Rewrite",
    "Header Rewrite",
    "Body Rewrite",
    "Map Local",
    "Script",
    "MITM",
]

SECTION_FILES = {
    "META": "Meta.conf",
    "Rule": "Rule.conf",
    "URL Rewrite": "URL-Rewrite.conf",
    "Header Rewrite": "Header-Rewrite.conf",
    "Body Rewrite": "Body-Rewrite.conf",
    "Map Local": "Map-Local.conf",
    "Script": "Script.conf",
    "MITM": "MITM.conf",
}

REQUIRED_SECTIONS = {"Rule", "Script", "MITM"}
CORE_TOKENS = ("spotify-json", "spotify-proto", "youtube.response")
EXPECTED_UPDATE_URL = "#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule"
SECTION_RE = re.compile(r"^\[([^\]]+)\]\s*$")


def stop(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeError as exc:
        stop(f"UTF-8 read failed: {path}: {exc}")
    except OSError as exc:
        stop(f"cannot read {path}: {exc}")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def split_module(text: str) -> tuple[str, dict[str, str]]:
    lines = text.splitlines()
    meta: list[str] = []
    sections: dict[str, list[str]] = {name: [] for name in SECTION_ORDER}
    current: str | None = None

    for line in lines:
        match = SECTION_RE.match(line.strip())
        if match:
            current = match.group(1)
            if current not in sections:
                sections[current] = []
            continue
        if current is None:
            meta.append(line)
        else:
            sections.setdefault(current, []).append(line)

    missing = sorted(section for section in REQUIRED_SECTIONS if section not in sections or not sections[section])
    if missing:
        stop("required sections are missing or empty: " + ", ".join(missing))

    return "\n".join(meta).rstrip() + "\n", {
        section: "\n".join(sections.get(section, [])).rstrip() + "\n" for section in SECTION_ORDER
    }


def extract_sources() -> None:
    text = read_text(MODULE)
    meta, sections = split_module(text)
    write_text(SOURCES / SECTION_FILES["META"], meta)
    for section in SECTION_ORDER:
        write_text(SOURCES / SECTION_FILES[section], sections[section])


def source_file(section: str) -> Path:
    return SOURCES / SECTION_FILES[section]


def build_from_sources() -> str:
    meta_path = source_file("META")
    if not meta_path.exists():
        stop("source meta file is missing; run with --extract-from-root first")

    parts: list[str] = [read_text(meta_path).rstrip()]
    for section in SECTION_ORDER:
        path = source_file(section)
        if not path.exists():
            stop(f"source section file is missing: {path}")
        body = read_text(path).rstrip()
        parts.append(f"[{section}]")
        if body:
            parts.append(body)
    return "\n".join(parts).rstrip() + "\n"


def validate(text: str) -> None:
    if EXPECTED_UPDATE_URL not in text:
        stop("update-url is missing or incorrect")
    for section in REQUIRED_SECTIONS:
        if f"[{section}]" not in text:
            stop(f"required section missing: [{section}]")
    for token in CORE_TOKENS:
        if token not in text:
            stop(f"required core token missing: {token}")

    section_positions = {match.group(1): match.start() for match in SECTION_RE.finditer(text)}
    if "Script" in section_positions and "MITM" in section_positions:
        script_block = text[section_positions["Script"]:section_positions["MITM"]]
        active_script_lines = [line for line in script_block.splitlines() if line.strip() and not line.lstrip().startswith("#") and not line.startswith("[")]
        if not active_script_lines:
            stop("[Script] section would be empty")
    mitm_index = text.find("[MITM]")
    if mitm_index >= 0 and "hostname =" not in text[mitm_index:]:
        stop("[MITM] hostname is missing")


def make_report(release_text: str, extracted: bool) -> str:
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
    root_text = read_text(MODULE)
    same_as_root = release_text.strip() == root_text.strip()
    section_counts = []
    for section in SECTION_ORDER:
        path = source_file(section)
        if path.exists():
            count = len(read_text(path).splitlines())
        else:
            count = 0
        section_counts.append(f"- {section}: {count} lines")

    return "\n".join([
        "# Module Factory Report",
        "",
        f"日期：{today}",
        f"是否从根目录主模块拆分：{'yes' if extracted else 'no'}",
        f"Release 是否与根目录主模块一致：{'yes' if same_as_root else 'no'}",
        f"Release 行数：{len(release_text.splitlines())}",
        "",
        "## Sources 统计",
        *section_counts,
        "",
        "## 说明",
        "- 根目录 Ronghemokuai.sgmodule 仍是正式导入入口。",
        "- Rewrite/Sources/ 保存从主模块拆分出来的结构化片段。",
        "- Release/Ronghemokuai.sgmodule 是由 Sources 重新拼接得到的发布副本。",
        "- 启用根目录自动生成前，必须先确认 Release 与根目录主模块一致。",
        "",
    ])


def main() -> None:
    parser = argparse.ArgumentParser(description="Split and build the module factory output.")
    parser.add_argument("--extract-from-root", action="store_true", help="split root Ronghemokuai.sgmodule into Rewrite/Sources")
    parser.add_argument("--build", action="store_true", help="build Release/Ronghemokuai.sgmodule from Rewrite/Sources")
    args = parser.parse_args()

    if not args.extract_from_root and not args.build:
        args.extract_from_root = True
        args.build = True

    extracted = False
    if args.extract_from_root:
        extract_sources()
        extracted = True

    if args.build:
        release_text = build_from_sources()
        validate(release_text)
        write_text(RELEASE, release_text)
        write_text(REPORT, make_report(release_text, extracted))
        print(f"Built {RELEASE} ({len(release_text.splitlines())} lines)")


if __name__ == "__main__":
    main()
