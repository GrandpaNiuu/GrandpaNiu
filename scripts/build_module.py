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
MISC_SOURCES = SOURCES / "Misc"
APP_SOURCES = SOURCES / "Apps"
PROFILES = ROOT / "Rewrite" / "Profiles"
REMOTES_JSON = ROOT / "Rewrite" / "Remotes" / "sources.json"

DEFAULT_PROFILE = "fusion"
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
RULE_PREFIXES = {
    "AND",
    "DOMAIN",
    "DOMAIN-KEYWORD",
    "DOMAIN-SET",
    "DOMAIN-SUFFIX",
    "IP-CIDR",
    "IP-CIDR6",
    "RULE-SET",
    "URL-REGEX",
}
REWRITE_ACTIONS = (
    "reject",
    "reject-200",
    "reject-array",
    "reject-dict",
    "reject-img",
    "reject-ttl",
    "echo-response",
    "script-path=",
    "header-del ",
    "header-replace ",
    "302 ",
    " 302",
    "307 ",
    " 307",
    "308 ",
    " 308",
    " header",
)
REQUIRED_SECTIONS = set(SECTION_ORDER)
CORE_TOKENS = ("spotify-json", "spotify-proto", "youtube.response", "zhihu-enhance")
EXPECTED_UPDATE_URL = "#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule"
SECTION_RE = re.compile(r"^\[([^\]]+)\]\s*$")
SCRIPT_NAME_RE = re.compile(r"^\s*([^#\s][^=]+?)\s*=")
HOSTNAME_RE = re.compile(r"^\s*hostname\s*=\s*(.+)$")
SCRIPT_FIELD_SPLIT_RE = re.compile(
    r",\s*(?=(?:type|pattern|argument|requires-body|max-size|binary-body-mode|script-path|timeout|engine|script-update-interval)\s*=)"
)
REMOTE_REQUIRED_FIELDS = {"name", "type", "url", "policy", "enabled", "protected", "purpose"}
DISALLOWED_REMOTE_TOKENS = ("ghproxy", "mirror", "tinyurl", "bit.ly", "t.co/", "shorturl")
KNOWN_DOMAIN_SET_URLS = {
    "https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksurge.list",
    "https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules_surge_domainset.txt",
}
MISC_PROTECT_RULE_FILES = ("cdn-direct.conf", "finance-protect.conf", "video-protect.conf")
UNRESOLVED_ARGUMENT_RE = re.compile(r"\{\{\{[^}]+\}\}\}")
PROTECTED_REJECT_TOKENS = (
    "api.biliapi.com",
    "api.biliapi.net",
    "app.biliapi.com",
    "app.biliapi.net",
    "ipv4.music.163.com",
    "ipv6.music.163.com",
    "httpdns.music.163.com",
    "wechatpay",
    "alipay",
    "abchina.com.cn",
    "boc.cn",
    "icbc",
    "ccb.com",
    "cmbchina",
    "bankcomm",
    "psbc",
    "cd-1.pddpic.com",
    "cdl-1.pddpic.com",
    "cdl-p2.pddpic.com",
    "ossgw.alicdn.com",
    "hudong.alicdn.com",
    "baichuan-sdk.alicdn.com",
    "nbsdk-baichuan.alicdn.com",
)
SCRIPT_MERGE_MAX_ITEMS = 24
SCRIPT_MERGE_MAX_PATTERN_LEN = 6000
SCRIPT_MERGE_ESSENTIAL_PREFIXES = CORE_TOKENS + ("bilibili.", "zhihu-enhance")


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


def split_source_fragment(text: str) -> dict[str, str]:
    """Split a partial source fragment without requiring every module section."""
    sections: dict[str, list[str]] = {name: [] for name in SECTION_ORDER}
    current: str | None = None
    for line in text.splitlines():
        match = SECTION_RE.match(line.strip())
        if match:
            section = match.group(1)
            current = section if section in sections else None
            continue
        if current is not None:
            sections[current].append(line)
    return {section: "\n".join(lines).rstrip() + ("\n" if lines else "") for section, lines in sections.items()}


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


def misc_paths(preferred: Iterable[str] = (), exclude: Iterable[str] = ()) -> list[Path]:
    if not MISC_SOURCES.exists():
        return []
    by_name = {path.name: path for path in MISC_SOURCES.glob("*.conf")}
    excluded = set(exclude)
    ordered: list[Path] = []
    for name in preferred:
        path = by_name.pop(name, None)
        if path is not None and path.name not in excluded:
            ordered.append(path)
    ordered.extend(path for name, path in sorted(by_name.items()) if name not in excluded)
    return ordered


def misc_section_blocks(section: str, preferred: Iterable[str] = (), exclude: Iterable[str] = ()) -> list[str]:
    blocks: list[str] = []
    for path in misc_paths(preferred=preferred, exclude=exclude):
        body = split_source_fragment(read_text(path, required=False)).get(section, "")
        if body.strip():
            blocks.append(body)
    return blocks


def misc_mitm_blocks() -> list[tuple[Path, str]]:
    blocks: list[tuple[Path, str]] = []
    for path in misc_paths():
        body = split_source_fragment(read_text(path, required=False)).get("MITM", "")
        if body.strip():
            blocks.append((path, body))
    return blocks


def app_paths() -> list[Path]:
    if not APP_SOURCES.exists():
        return []
    return sorted(path for path in APP_SOURCES.glob("*.conf") if not path.name.startswith("_"))


def iter_profile_paths(profile: configparser.ConfigParser, section: str) -> Iterable[Path]:
    if not profile.has_section(section):
        return []
    paths: list[Path] = []
    for _, value in profile.items(section):
        value = value.strip()
        if value:
            paths.append(ROOT / value)
    return paths


def normalize_known_remote_line(line: str) -> str:
    stripped = line.strip()
    for url in KNOWN_DOMAIN_SET_URLS:
        if stripped.startswith(f"RULE-SET,{url},"):
            return line.replace(f"RULE-SET,{url},", f"DOMAIN-SET,{url},", 1)
    return line


def is_unsafe_protected_reject(line: str) -> bool:
    stripped = line.strip()
    upper = stripped.upper()
    if "REJECT" not in upper:
        return False
    if stripped.startswith("AND,") and "PROTOCOL,UDP" in upper and (
        "googlevideo.com" in stripped.lower() or "youtubei.googleapis.com" in stripped.lower()
    ):
        return False
    lowered = stripped.lower()
    return any(token in lowered for token in PROTECTED_REJECT_TOKENS)


def should_skip_generated_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return False
    if UNRESOLVED_ARGUMENT_RE.search(stripped):
        return True
    return is_unsafe_protected_reject(stripped)


def slug_script_block(path: Path, body: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "-", path.stem).strip("-").lower() or "app"
    lines: list[str] = []
    index = 0
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or should_skip_generated_line(line):
            continue
        if "=" not in line:
            continue
        index += 1
        _, rhs = line.split("=", 1)
        lines.append(f"app.{slug}.{index} = {rhs.strip()}")
    return "\n".join(lines).strip() + ("\n" if lines else "")


def valid_rule_block(body: str) -> str:
    lines: list[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            lines.append(raw)
            continue
        prefix = line.split(",", 1)[0]
        if prefix not in RULE_PREFIXES:
            continue
        lines.append(raw)
    return "\n".join(lines).strip() + ("\n" if lines else "")


def valid_rewrite_block(section: str, body: str) -> str:
    lines: list[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            lines.append(raw)
            continue
        if section == "Header Rewrite":
            if " header-del " not in line and " header-replace " not in line:
                continue
        elif section == "Body Rewrite":
            if not line.startswith(("http-request ", "http-response ", "http-response-jq ")):
                continue
            if len(line.split()) < 3:
                continue
        elif section == "Map Local":
            if " data-type=" not in line:
                continue
            if " data=" not in line and "data-type=tiny-gif" not in line:
                continue
        elif section == "URL Rewrite":
            if not any(action in line for action in REWRITE_ACTIONS):
                continue
        lines.append(raw)
    return "\n".join(lines).strip() + ("\n" if lines else "")


def app_section_blocks(section: str) -> list[str]:
    blocks: list[str] = []
    for path in app_paths():
        body = split_source_fragment(read_text(path, required=False)).get(section, "")
        if not body.strip():
            continue
        if section == "Script":
            body = slug_script_block(path, body)
        elif section == "Rule":
            body = valid_rule_block(body)
        elif section in REWRITE_PROFILE_SECTIONS:
            body = valid_rewrite_block(section, body)
        if body.strip():
            blocks.append(body)
    return blocks


def app_mitm_blocks() -> list[tuple[Path, str]]:
    blocks: list[tuple[Path, str]] = []
    for path in app_paths():
        body = split_source_fragment(read_text(path, required=False)).get("MITM", "")
        if body.strip():
            blocks.append((path, body))
    return blocks


def active_key(line: str) -> str:
    return normalize_known_remote_line(line).strip()


def merge_lines(blocks: Iterable[str]) -> str:
    merged: list[str] = []
    seen: set[str] = set()
    last_blank = False
    for block in blocks:
        for line in block.splitlines():
            line = normalize_known_remote_line(line.rstrip())
            if should_skip_generated_line(line):
                continue
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


def split_script_fields(value: str) -> list[str]:
    return [part.strip() for part in SCRIPT_FIELD_SPLIT_RE.split(value.strip()) if part.strip()]


def parse_script_entry(line: str) -> dict[str, str] | None:
    if "script-path=" not in line or "pattern=" not in line:
        return None
    match = SCRIPT_NAME_RE.match(line.strip())
    if not match:
        return None
    name = match.group(1).strip()
    if name.startswith(SCRIPT_MERGE_ESSENTIAL_PREFIXES):
        return None
    _, value = line.split("=", 1)
    fields: dict[str, str] = {"__name__": name}
    for field in split_script_fields(value):
        if "=" not in field:
            return None
        key, field_value = field.split("=", 1)
        fields[key.strip()] = field_value.strip()
    if "argument" in fields or "pattern" not in fields or "script-path" not in fields or "type" not in fields:
        return None
    return fields


def script_entry_signature(entry: dict[str, str]) -> tuple[tuple[str, str], ...]:
    return tuple(sorted((key, value) for key, value in entry.items() if key not in {"__name__", "pattern"}))


def merged_script_line(name: str, template: dict[str, str], patterns: list[str]) -> str:
    values = dict(template)
    values["pattern"] = "(?:" + "|".join(patterns) + ")"
    ordered = [
        "type",
        "pattern",
        "requires-body",
        "max-size",
        "binary-body-mode",
        "engine",
        "timeout",
        "script-path",
        "script-update-interval",
    ]
    for key in template:
        if key.startswith("__") or key in ordered or key == "pattern":
            continue
        ordered.append(key)
    fields = [f"{key}={values[key]}" for key in ordered if key in values]
    return f"{name} = " + ",".join(fields)


def consolidate_script_entries(body: str) -> str:
    """Fuse repeated Script entries that only differ by pattern.

    This reduces Shadowrocket's visible script list without changing the
    underlying script URL or execution parameters. Entries with arguments or
    binary bodies are intentionally left alone because they are usually app-core
    protobuf handlers.
    """
    lines: list[str] = []
    seen_rhs: set[str] = set()
    for raw in body.splitlines():
        stripped = raw.strip()
        if "script-path=" in stripped and "=" in stripped:
            _, rhs = stripped.split("=", 1)
            rhs_key = re.sub(r"\s+", "", rhs)
            if rhs_key in seen_rhs:
                continue
            seen_rhs.add(rhs_key)
        lines.append(raw)
    parsed: dict[int, dict[str, str]] = {}
    groups: dict[tuple[tuple[str, str], ...], list[int]] = {}
    for index, line in enumerate(lines):
        entry = parse_script_entry(line.strip())
        if entry is None:
            continue
        parsed[index] = entry
        groups.setdefault(script_entry_signature(entry), []).append(index)

    merge_heads: dict[int, list[int]] = {}
    for indices in groups.values():
        if len(indices) < 2 or len(indices) > SCRIPT_MERGE_MAX_ITEMS:
            continue
        patterns = [parsed[index]["pattern"] for index in indices]
        if len("(?:" + "|".join(patterns) + ")") > SCRIPT_MERGE_MAX_PATTERN_LEN:
            continue
        merge_heads[indices[0]] = indices

    consumed: set[int] = set()
    out: list[str] = []
    existing_names = {entry["__name__"] for entry in parsed.values()}
    for index, line in enumerate(lines):
        if index in consumed:
            continue
        if index in merge_heads:
            indices = merge_heads[index]
            first = parsed[index]
            base_name = f"{first['__name__']}_merged"
            name = base_name
            suffix = 2
            while name in existing_names:
                name = f"{base_name}{suffix}"
                suffix += 1
            existing_names.add(name)
            patterns = [parsed[item]["pattern"] for item in indices]
            out.append(merged_script_line(name, first, patterns))
            consumed.update(indices)
            continue
        out.append(line)
    return "\n".join(line.rstrip() for line in out if line.strip()).strip() + "\n"


def is_preserved_metadata(line: str) -> bool:
    stripped = line.lstrip()
    return stripped.startswith("#!") or stripped.startswith("# update-date:")


def minify_module_text(text: str) -> str:
    """Remove blank lines and ordinary comments from generated module output."""
    lines: list[str] = []
    for raw in text.splitlines():
        line = normalize_known_remote_line(raw.rstrip())
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
        if url in KNOWN_DOMAIN_SET_URLS:
            rule_type = "DOMAIN-SET"
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
    blocks.extend(misc_section_blocks("Rule", preferred=MISC_PROTECT_RULE_FILES))
    if as_bool(profile, "include", "rules", True):
        blocks.extend(load_optional_files(iter_profile_paths(profile, "rules")))
    blocks.extend(app_section_blocks("Rule"))
    blocks.extend(misc_section_blocks("Rule", exclude=MISC_PROTECT_RULE_FILES))
    if as_bool(profile, "include", "remotes", True):
        blocks.append(remote_rule_lines())
    if as_bool(profile, "include", "source_rule_compat", True):
        blocks.append(read_text(source_file("Rule"), required=False))
    return merge_lines(blocks)


def build_scripts(profile: configparser.ConfigParser) -> str:
    blocks: list[str] = []
    if as_bool(profile, "include", "scripts", True):
        blocks.extend(load_optional_files(iter_profile_paths(profile, "scripts")))
    blocks.extend(app_section_blocks("Script"))
    blocks.extend(misc_section_blocks("Script"))
    if as_bool(profile, "include", "source_script_compat", True):
        blocks.append(read_text(source_file("Script"), required=False))
    return consolidate_script_entries(merge_lines(blocks))


def build_rewrite_section(profile: configparser.ConfigParser, section: str) -> str:
    blocks: list[str] = [read_text(source_file(section), required=False)]
    profile_section = REWRITE_PROFILE_SECTIONS.get(section)
    if profile_section:
        blocks.extend(load_optional_files(iter_profile_paths(profile, profile_section)))
    blocks.extend(misc_section_blocks(section))
    blocks.extend(app_section_blocks(section))
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
    for path, block in misc_mitm_blocks():
        comments.append(f"# source: {path.relative_to(ROOT).as_posix()}")
        for host in parse_mitm_hosts(block):
            if host not in seen:
                seen.add(host)
                hosts.append(host)
    for path, block in app_mitm_blocks():
        comments.append(f"# source: {path.relative_to(ROOT).as_posix()}")
        for host in parse_mitm_hosts(block):
            if host not in seen:
                seen.add(host)
                hosts.append(host)
    if not hosts:
        stop("profile MITM sources produced an empty hostname list")
    return "\n".join(comments + ["hostname = %APPEND% " + ",".join(hosts)]) + "\n"


def build_from_sources(profile_name: str = DEFAULT_PROFILE) -> str:
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
    if UNRESOLVED_ARGUMENT_RE.search(text):
        stop("generated module contains unresolved argument placeholders")
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
    stale = f"RULE-SET,https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksurge.list,REJECT"
    if stale in text:
        stop("217heidai adblocksurge is a pure domain set; it must be DOMAIN-SET, not RULE-SET")


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
        f"- 默认公开入口：单一融合版",
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
        "- Rules/: DIRECT、Spotify、YouTube、本地 App、网页、Reject、legacy、Stable Plus 与 Full 规则片段",
        "- Scripts/: Spotify、YouTube、知乎、App-clean、legacy reviewed、QingRex 与 Stable Plus 脚本片段",
        "- Rewrite/Sources/: Meta、Rewrite、Body Rewrite、Map Local、MITM、legacy reviewed、stable-plus、extended 和兼容片段",
        "- [mitm] fusion profile 同时读取 core / app-clean / legacy-reviewed / qingrex / stable-plus / extended 层。",
        "",
        "## 重复检查",
        f"- 重复脚本名：{', '.join(script_dupes) if script_dupes else '无'}",
        f"- 重复 MITM hostname：{', '.join(mitm_dupes) if mitm_dupes else '无'}",
        "",
        "## 模块输出清理",
        "- 生成模块会自动删除空行和普通 # 注释说明。",
        "- 保留 #!update-url、#!name、#!desc 和 # update-date: 等必要元数据。",
        "- 已知纯域名远程源会自动规范为 DOMAIN-SET，避免 Shadowrocket 红叉。",
        "",
        "## 说明",
        "- 日常维护应优先修改 Rules、Scripts、Rewrite/Sources、Rewrite/Remotes 和 Rewrite/Profiles/fusion.conf。",
        "- Release/Ronghemokuai.sgmodule 由工厂源头生成。",
        "- 根目录 Ronghemokuai.sgmodule 由 factory_finalize.py 同步生成。",
        "- 本仓库默认不再拆分 Stable / Stable Plus / Lite / Full 作为用户入口。",
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
    parser.add_argument("--profile", default=DEFAULT_PROFILE, help=f"profile name under Rewrite/Profiles, default: {DEFAULT_PROFILE}")
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
