#!/usr/bin/env python3
"""Build Ronghemokuai.sgmodule from source-driven factory inputs."""

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

SECTION_ORDER = ["Rule", "URL Rewrite", "Header Rewrite", "Body Rewrite", "Map Local", "Script", "MITM"]
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
REWRITE_PROFILE_SECTIONS = {
    "URL Rewrite": "url_rewrite",
    "Header Rewrite": "header_rewrite",
    "Body Rewrite": "body_rewrite",
    "Map Local": "map_local",
}
REQUIRED_SECTIONS = set(SECTION_ORDER)
CORE_TOKENS = ("spotify-json", "spotify-proto", "youtube.response", "zhihu-enhance")
EXPECTED_UPDATE_URL = "#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule"
SECTION_RE = re.compile(r"^\[([^\]]+)\]\s*$")
SCRIPT_NAME_RE = re.compile(r"^\s*([^#\s][^=]+?)\s*=")
HOSTNAME_RE = re.compile(r"^\s*hostname\s*=\s*(.+)$")
REMOTE_REQUIRED_FIELDS = {"name", "type", "url", "policy", "enabled", "protected", "purpose"}
DISALLOWED_REMOTE_TOKENS = ("ghproxy", "mirror", "tinyurl", "bit.ly", "t.co/", "shorturl")


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
    meta: list[str] = []
    sections: dict[str, list[str]] = {name: [] for name in SECTION_ORDER}
    current: str | None = None
    for line in text.splitlines():
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
    meta, sections = split_module(read_text(MODULE))
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
    return line.strip()


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


def is_preserved_metadata(line: str) -> bool:
    stripped = line.lstrip()
    return stripped.startswith("#!") or stripped.startswith("# update-date:")


def minify_module_text(text: str) -> str:
    """Remove blank lines and ordinary comments from generated module output."""
    lines: list[str] = []
    for raw in text.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#") and not is_preserved_metadata(stripped):
            continue
        lines.append(line)
    return "\n".join(lines).rstrip() + "\n"


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
        missing = sorted(REMOTE_REQUIRED_FIELDS - set(item))
        if missing:
            stop(f"remote source missing fields {missing}: {item}")
        if not item.get("enabled", False):
            continue
        rule_type = str(item.get("type", "")).strip()
        url = str(item.get("url", "")).strip()
        policy = str(item.get("policy", "REJECT")).strip()
        if rule_type not in {"RULE-SET", "DOMAIN-SET"}:
            stop(f"unsupported remote source type: {item}")
        if not url.startswith("https://"):
            stop(f"enabled remote source must use https: {url}")
        if any(token in url.lower() for token in DISALLOWED_REMOTE_TOKENS):
            stop(f"disallowed remote source URL: {url}")
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


def build_rewrite_section(profile: configparser.ConfigParser, section: str) -> str:
    blocks: list[str] = [read_text(source_file(section), required=False)]
    profile_section = REWRITE_PROFILE_SECTIONS.get(section)
    if profile_section:
        blocks.extend(load_optional_files(iter_profile_paths(profile, profile_section)))
    return merge_lines(blocks)


def parse_mitm_hosts(block: str) -> list[str]:
    hosts: list[str] = []
    for line in block.splitlines():
        match = HOSTNAME_RE.match(line)
        if not match:
            continue
        value = match.group(1).replace("%APPEND%", "")
        for host in value.split(","):
            clean = host.strip()
            if clean:
                hosts.append(clean)
    return hosts


def build_mitm(profile: configparser.ConfigParser) -> str:
    """Build the MITM section from profile-selected layers."""
    if not profile.has_section("mitm"):
        return read_text(source_file("MITM"), required=False).rstrip() + "\n"

    hosts: list[str] = []
    seen: set[str] = set()
    comments: list[str] = ["# MITM profile layers generated by scripts/build_module.py"]
    for path in iter_profile_paths(profile, "mitm"):
        if not path.exists():
            stop(f"profile MITM source missing: {path.relative_to(ROOT)}")
        comments.append(f"# source: {path.relative_to(ROOT).as_posix()}")
        for host in parse_mitm_hosts(read_text(path)):
            if host not in seen:
                seen.add(host)
                hosts.append(host)
    if not hosts:
        stop("profile MITM sources produced an empty hostname list")
    return "\n".join(comments + ["hostname = %APPEND% " + ",".join(hosts)]) + "\n"


def build_from_sources(profile_name: str) -> str:
    profile = load_profile(profile_name)
    parts: list[str] = [read_text(source_file("META")).rstrip()]
    for section in SECTION_ORDER:
        parts.append(f"[{section}]")
        if section == "Rule":
            body = build_rules(profile)
        elif section == "Script":
            body = build_scripts(profile)
        elif section == "MITM":
            body = build_mitm(profile)
        elif section in REWRITE_PROFILE_SECTIONS:
            body = build_rewrite_section(profile, section)
        else:
            body = read_text(source_file(section), required=False).rstrip() + "\n"
        if body.strip():
            parts.append(body.rstrip())
    return minify_module_text("\n".join(parts).rstrip() + "\n")


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
    return parse_mitm_hosts(text[index:])


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
        script_dupes = duplicates(script_names(text))
        if script_dupes:
            stop("duplicate script names: " + ", ".join(script_dupes))
    mitm_index = text.find("[MITM]")
    if mitm_index >= 0:
        hosts = mitm_hostnames(text)
        if not hosts:
            stop("[MITM] hostname is missing")
        mitm_dupes = duplicates(hosts)
        if mitm_dupes:
            stop("duplicate MITM hostnames: " + ", ".join(mitm_dupes[:20]))


def make_report(release_text: str, extracted: bool, profile: str) -> str:
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
    root_text = read_text(MODULE)
    build_stage_same_as_root = release_text.strip() == root_text.strip()
    section_counts = []
    for section in SECTION_ORDER:
        path = source_file(section)
        count = len(read_text(path, required=False).splitlines()) if path.exists() else 0
        section_counts.append(f"- {section}: {count} 行")
    script_dupes = duplicates(script_names(release_text))
    mitm_dupes = duplicates(mitm_hostnames(release_text))
    mitm_count = len(mitm_hostnames(release_text))
    return "\n".join([
        "# 模块工厂报告",
        "",
        f"- 日期：{today}",
        f"- 构建 profile：{profile}",
        f"- 是否从 root 反拆：{'是' if extracted else '否'}",
        f"- 构建阶段 Root/Release 是否一致：{'是' if build_stage_same_as_root else '否'}",
        f"- Release 行数：{len(release_text.splitlines())}",
        f"- Release MITM hostname 数量：{mitm_count}",
        "",
        "## 源文件统计",
        *section_counts,
        "",
        "## 构建输入",
        f"- Rewrite/Profiles/{profile}.conf",
        "- Rewrite/Remotes/sources.json",
        "- Rules/: DIRECT、Spotify、YouTube、本地 App、网页、Reject 和 legacy stable import 规则片段",
        "- Scripts/: Spotify、YouTube、知乎、App-clean 和 legacy reviewed 脚本片段",
        "- Rewrite/Sources/: Meta、Rewrite、Body Rewrite、Map Local、MITM、legacy reviewed 和兼容片段",
        "- [mitm] profile 可选择 MITM-core / MITM-app-clean / MITM-extended / MITM-legacy-reviewed 分层输入；stable 默认只吃 reviewed legacy 层。",
        "",
        "## 重复检查",
        f"- 重复脚本名：{', '.join(script_dupes) if script_dupes else '无'}",
        f"- 重复 MITM hostname：{', '.join(mitm_dupes) if mitm_dupes else '无'}",
        "",
        "## 模块输出清理",
        "- 生成模块会自动删除空行和普通 # 注释说明。",
        "- 保留 #!update-url、#!name、#!desc 和 # update-date: 等必要元数据。",
        "",
        "## 说明",
        "- 日常维护应优先修改 Rules、Scripts、Rewrite/Sources、Rewrite/Remotes 和 Rewrite/Profiles。",
        "- Release/Ronghemokuai.sgmodule 由工厂源头生成。",
        "- 根目录 Ronghemokuai.sgmodule 由 factory_finalize.py 同步生成。",
        "- legacy Script / MITM / Rewrite 必须进入 reviewed 源头后才会被 stable profile 读取。",
        "- --extract-from-root 只用于初始化或恢复源头，不是日常构建路径。",
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
        "# 模块工厂差异报告",
        "",
        f"- Root 行数：{len(root_text.splitlines())}",
        f"- Release 行数：{len(release_text.splitlines())}",
        f"- Diff lines：{len(diff)}",
        f"- Diff 是否截断：{'是' if len(diff) > max_lines else '否'}",
        "",
        "```diff",
        *clipped,
        "```",
        "",
    ])


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the source-driven module factory output.")
    parser.add_argument("--extract-from-root", action="store_true", help="rebuild Rewrite/Sources from root module; use only for initialization or recovery")
    parser.add_argument("--build", action="store_true", help="build Release/Ronghemokuai.sgmodule from factory sources")
    parser.add_argument("--profile", default="stable", help="profile name under Rewrite/Profiles, default: stable")
    args = parser.parse_args()
    if not args.extract_from_root and not args.build:
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
