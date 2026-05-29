#!/usr/bin/env python3
"""Build and split Ronghemokuai.sgmodule with the repository factory layout.

The builder is intentionally conservative:
- root Ronghemokuai.sgmodule stays the formal import entry;
- generated output is written to Release/Ronghemokuai.sgmodule;
- source files in Rules, Scripts, Remotes and Rewrite/Sources can participate in the Release build;
- exact duplicate active lines are removed during assembly.
"""

from __future__ import annotations

import argparse
import configparser
import datetime as dt
import difflib
import json
import re
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "Ronghemokuai.sgmodule"
RELEASE = ROOT / "Release" / "Ronghemokuai.sgmodule"
REPORT = ROOT / "reports" / "module_factory_report.md"
DIFF_REPORT = ROOT / "reports" / "module_factory_diff_report.md"
SOURCES = ROOT / "Rewrite" / "Sources"
PROFILES = ROOT / "Rewrite" / "Profiles"
REMOTES_JSON = ROOT / "Rewrite" / "Remotes" / "sources.json"

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
SCRIPT_NAME_RE = re.compile(r"^\s*([^#\s][^=]+?)\s*=")


def stop(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path, required: bool = True) -> str:
    if not path.exists():
        if required:
            stop(f"missing file: {path}")
        return ""
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
            sections.setdefault(current, [])
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


def profile_path(name: str) -> Path:
    return PROFILES / f"{name}.conf"


def load_profile(name: str) -> configparser.ConfigParser:
    parser = configparser.ConfigParser()
    path = profile_path(name)
    if not path.exists():
        stop(f"profile not found: {path}")
    parser.read(path, encoding="utf-8")
    return parser


def as_bool(profile: configparser.ConfigParser, section: str, key: str, default: bool) -> bool:
    if not profile.has_option(section, key):
        return default
    return profile.getboolean(section, key)


def source_file(section: str) -> Path:
    return SOURCES / SECTION_FILES[section]


def iter_profile_paths(profile: configparser.ConfigParser, section: str) -> Iterable[Path]:
    if not profile.has_section(section):
        return []
    paths: list[Path] = []
    for _, value in profile.items(section):
        value = value.strip()
        if value:
            paths.append(ROOT / value)
    return paths


def active_key(line: str) -> str:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return ""
    return stripped


def merge_lines(blocks: Iterable[str]) -> str:
    merged: list[str] = []
    seen: set[str] = set()
    last_blank = False
    for block in blocks:
        for line in block.splitlines():
            key = active_key(line)
            if key and key in seen:
                continue
            if key:
                seen.add(key)
            if not line.strip():
                if not last_blank and merged:
                    merged.append("")
                last_blank = True
                continue
            merged.append(line.rstrip())
            last_blank = False
    return "\n".join(merged).strip() + "\n"


def load_optional_files(paths: Iterable[Path]) -> list[str]:
    return [read_text(path, required=False) for path in paths if path.exists()]


def remote_rule_lines() -> str:
    if not REMOTES_JSON.exists():
        return ""
    try:
        data = json.loads(read_text(REMOTES_JSON))
    except json.JSONDecodeError as exc:
        stop(f"invalid remote sources json: {exc}")
    lines: list[str] = []
    for item in data.get("rule_sets", []):
        if not item.get("enabled", False):
            continue
        rule_type = str(item.get("type", "")).strip()
        url = str(item.get("url", "")).strip()
        policy = str(item.get("policy", "REJECT")).strip()
        if rule_type not in {"RULE-SET", "DOMAIN-SET"} or not url.startswith("http"):
            continue
        name = str(item.get("name", "remote source")).strip()
        lines.append(f"# remote: {name}")
        lines.append(f"{rule_type},{url},{policy}")
    return "\n".join(lines).strip() + ("\n" if lines else "")


def build_rules(profile: configparser.ConfigParser) -> str:
    blocks: list[str] = []
    if as_bool(profile, "include", "rules", True):
        blocks.extend(load_optional_files(iter_profile_paths(profile, "rules")))
    if as_bool(profile, "include", "remotes", True):
        blocks.append(remote_rule_lines())
    if as_bool(profile, "include", "source_rule_compat", True):
        blocks.append(read_text(source_file("Rule"), required=False))
    return merge_lines(blocks)


def build_scripts(profile: configparser.ConfigParser) -> str:
    blocks: list[str] = []
    if as_bool(profile, "include", "scripts", True):
        blocks.extend(load_optional_files(iter_profile_paths(profile, "scripts")))
    if as_bool(profile, "include", "source_script_compat", True):
        blocks.append(read_text(source_file("Script"), required=False))
    return merge_lines(blocks)


def build_from_sources(profile_name: str) -> str:
    profile = load_profile(profile_name)
    meta = read_text(source_file("META")).rstrip()
    parts: list[str] = [meta]

    for section in SECTION_ORDER:
        parts.append(f"[{section}]")
        if section == "Rule":
            body = build_rules(profile)
        elif section == "Script":
            body = build_scripts(profile)
        else:
            body = read_text(source_file(section), required=False).rstrip() + "\n"
        if body.strip():
            parts.append(body.rstrip())
    return "\n".join(parts).rstrip() + "\n"


def script_names(text: str) -> list[str]:
    in_script = False
    names: list[str] = []
    for line in text.splitlines():
        match = SECTION_RE.match(line.strip())
        if match:
            in_script = match.group(1) == "Script"
            continue
        if not in_script or not line.strip() or line.lstrip().startswith("#"):
            continue
        name_match = SCRIPT_NAME_RE.match(line)
        if name_match:
            names.append(name_match.group(1).strip())
    return names


def mitm_hostnames(text: str) -> list[str]:
    index = text.find("[MITM]")
    if index < 0:
        return []
    tail = text[index:]
    hosts: list[str] = []
    for line in tail.splitlines():
        if not line.strip().startswith("hostname ="):
            continue
        _, value = line.split("=", 1)
        for host in value.split(","):
            clean = host.strip()
            if clean and clean != "%APPEND%":
                hosts.append(clean)
    return hosts


def duplicates(values: list[str]) -> list[str]:
    seen: set[str] = set()
    dupes: list[str] = []
    for value in values:
        if value in seen and value not in dupes:
            dupes.append(value)
        seen.add(value)
    return dupes


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


def make_report(release_text: str, extracted: bool, profile: str) -> str:
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
    root_text = read_text(MODULE)
    same_as_root = release_text.strip() == root_text.strip()
    section_counts = []
    for section in SECTION_ORDER:
        path = source_file(section)
        count = len(read_text(path, required=False).splitlines()) if path.exists() else 0
        section_counts.append(f"- {section}: {count} lines")

    script_dupes = duplicates(script_names(release_text))
    mitm_dupes = duplicates(mitm_hostnames(release_text))
    return "\n".join([
        "# Module Factory Report",
        "",
        f"日期：{today}",
        f"构建 profile：{profile}",
        f"是否从根目录主模块拆分：{'yes' if extracted else 'no'}",
        f"Release 是否与根目录主模块一致：{'yes' if same_as_root else 'no'}",
        f"Release 行数：{len(release_text.splitlines())}",
        "",
        "## Sources 统计",
        *section_counts,
        "",
        "## 参与构建的源头",
        "- Rewrite/Sources/: rewrite、body、map local、MITM 与过渡兼容片段",
        "- Rules/: DIRECT、Spotify、YouTube、本地规则片段",
        "- Scripts/: Spotify、YouTube、App 脚本片段",
        "- Rewrite/Remotes/sources.json: 远程 RULE-SET / DOMAIN-SET 清单",
        "- Rewrite/Profiles/: 构建 profile",
        "",
        "## 重复检查",
        f"- 重复脚本名：{', '.join(script_dupes) if script_dupes else '无'}",
        f"- 重复 MITM hostname：{', '.join(mitm_dupes) if mitm_dupes else '无'}",
        "",
        "## 说明",
        "- 根目录 Ronghemokuai.sgmodule 仍是正式导入入口。",
        "- Release/Ronghemokuai.sgmodule 是工厂源文件生成的发布副本。",
        "- 当前构建不会自动覆盖根目录主模块。",
        "",
    ])


def make_diff_report(release_text: str) -> str:
    root_text = read_text(MODULE)
    diff = list(difflib.unified_diff(
        root_text.splitlines(),
        release_text.splitlines(),
        fromfile="Ronghemokuai.sgmodule",
        tofile="Release/Ronghemokuai.sgmodule",
        lineterm="",
    ))
    max_lines = 400
    clipped = diff[:max_lines]
    return "\n".join([
        "# Module Factory Diff Report",
        "",
        f"Root lines: {len(root_text.splitlines())}",
        f"Release lines: {len(release_text.splitlines())}",
        f"Diff lines: {len(diff)}",
        f"Diff clipped: {'yes' if len(diff) > max_lines else 'no'}",
        "",
        "```diff",
        *clipped,
        "```",
        "",
    ])


def main() -> None:
    parser = argparse.ArgumentParser(description="Split and build the module factory output.")
    parser.add_argument("--extract-from-root", action="store_true", help="split root Ronghemokuai.sgmodule into Rewrite/Sources")
    parser.add_argument("--build", action="store_true", help="build Release/Ronghemokuai.sgmodule from factory sources")
    parser.add_argument("--profile", default="stable", help="profile name under Rewrite/Profiles, default: stable")
    args = parser.parse_args()

    if not args.extract_from_root and not args.build:
        args.extract_from_root = True
        args.build = True

    extracted = False
    if args.extract_from_root:
        extract_sources()
        extracted = True

    if args.build:
        release_text = build_from_sources(args.profile)
        validate(release_text)
        write_text(RELEASE, release_text)
        write_text(REPORT, make_report(release_text, extracted, args.profile))
        write_text(DIFF_REPORT, make_diff_report(release_text))
        print(f"Built {RELEASE} ({len(release_text.splitlines())} lines) using profile={args.profile}")


if __name__ == "__main__":
    main()
