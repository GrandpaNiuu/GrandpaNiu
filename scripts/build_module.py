#!/usr/bin/env python3
"""Build Ronghemokuai.sgmodule from source-driven factory inputs."""

from __future__ import annotations

import argparse
import configparser
import datetime as dt
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from refresh_module_date import refresh_module_date, today_beijing

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "Ronghemokuai.sgmodule"
RELEASE = ROOT / "Release" / "Ronghemokuai.sgmodule"
REPORT = ROOT / "reports" / "module_factory_report.md"
DIFF_REPORT = ROOT / "reports" / "module_factory_diff_report.md"
SCRIPT_AGGREGATION_REPORT = ROOT / "reports" / "script_aggregation_report.md"
MITM_OPTIMIZATION_REPORT_JSON = ROOT / "reports" / "mitm_optimization_report.json"
MITM_OPTIMIZATION_REPORT_MD = ROOT / "reports" / "mitm_optimization_report.md"
SOURCES = ROOT / "Rewrite" / "Sources"
MISC_SOURCES = SOURCES / "Misc"
APP_SOURCES = SOURCES / "Apps"
GENERATED_SCRIPTS = ROOT / "Scripts" / "generated"
SCRIPT_BUNDLE = GENERATED_SCRIPTS / "fusion-script-bundle.js"
SCRIPT_BUNDLE_MANIFEST = GENERATED_SCRIPTS / "fusion-script-bundle.manifest.json"
SCRIPT_BUNDLE_CACHE = GENERATED_SCRIPTS / "fusion-script-bundle.cache.json"
SCRIPT_BUNDLE_URL = "https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Scripts/generated/fusion-script-bundle.js"
SCRIPT_BUNDLE_VERSION = "grandpaniu-fusion-script-bundle-v1"
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
    "GEOIP",
    "IP-CIDR",
    "IP-CIDR6",
    "FINAL",
    "RULE-SET",
    "URL-REGEX",
}
RULE_POLICIES_TO_STRIP = {"DIRECT", "PROXY"}
RULE_POLICY_TOKENS = {"DIRECT", "PROXY", "REJECT", "REJECT-DROP", "REJECT-TINYGIF", "REJECT-IMG"}
COMPACT_NETWORK_SPLIT_RULES = (
    "# GrandpaNiu compact network split: China direct, overseas proxy",
    "GEOIP,CN,DIRECT",
    "FINAL,PROXY",
)
COMPACT_REGEX_LINE_LIMIT = 6000
COMPACT_URL_REWRITE_ACTIONS = {"reject", "reject-200", "reject-array", "reject-dict", "reject-img", "reject-ttl"}
URL_REWRITE_REJECT_RE = re.compile(
    r"^(?P<pattern>.+?)\s+(?P<replacement>-)\s+(?P<action>reject(?:-[a-z0-9]+)?)$"
)
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
MITM_EXACT_HOST_RE = re.compile(
    r"(?=.{1,253}\Z)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+"
    r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\Z",
    re.IGNORECASE,
)
URL_HOST_RE = re.compile(r"https\??:(?:\\\/\\\/|//)([^\s\)\(\|]+)", re.IGNORECASE)
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
PROTECTED_PROFILE_RULE_KEYS = ("protect_login", "protect_payment", "protect_video", "protect_cdn", "direct")
UNRESOLVED_ARGUMENT_RE = re.compile(r"\{\{\{[^}]+\}\}\}")
FUSION_ARGUMENT_NAMES = {
    "动态最常访问",
    "创作中心",
    "过滤置顶评论广告",
    "优化评论区加载",
    "空降助手",
    "空降助手策略",
    "日志等级",
    "屏蔽上传按钮",
    "屏蔽选段按钮",
    "屏蔽Shorts按钮",
    "字幕翻译语言",
    "歌词翻译语言",
    "启用调试模式",
}
PRESERVE_APP_SCRIPT_NAMES = {"bilibili", "youtube"}
MITM_DEEP_FEATURE_SECTIONS = ("URL Rewrite", "Header Rewrite", "Body Rewrite", "Map Local", "Script")
MITM_FORCE_KEEP_TOKENS = (
    "grpc.biliapi.net",
    "api.bilibili.com",
    "app.bilibili.com",
    "spclient.wg.spotify.com",
    "*.spclient.spotify.com",
    "youtubei.googleapis.com",
)
PROTECTED_REJECT_TOKENS = (
    "api.biliapi",
    "app.biliapi",
    "api.biliapi.com",
    "api.biliapi.net",
    "app.biliapi.com",
    "app.biliapi.net",
    "api.iqiyi.com",
    "ipv4.music.163.com",
    "ipv6.music.163.com",
    "httpdns",
    "httpdns.",
    "httpdns-",
    "httpdns.music.163.com",
    "httpdns.baidubce.com",
    "httpdnsmultiapi.meituan.com",
    "httpdnsmultiapivip.meituan.com",
    "hdns.ksyun.com",
    "lofter.httpdns.c.163.com",
    "wechatpay",
    "alipay",
    "adgw.alipay.com",
    "amdc.alipay.com",
    "amdc-sibling.alipay.com.cn",
    "mobiledc.stable.alipay.net",
    "rtms.alipay.com",
    "api.verify.mob.com",
    "log-verify.mob.com",
    "mdap.wallet.pbcdci.cn",
    "mdc.wallet.pbcdci.cn",
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
    "baidustatic.com",
    "zijieapi.com",
    "zijieapi.net",
    "zijiecdn.com",
    "snssdk.com",
)
SCRIPT_MERGE_MAX_ITEMS = 24
SCRIPT_MERGE_MAX_PATTERN_LEN = 6000
SCRIPT_MERGE_ESSENTIAL_PREFIXES = CORE_TOKENS + ("bilibili.", "zhihu-enhance")
SCRIPT_AGGREGATOR_MAX_PATTERN_LEN = 5600
SCRIPT_AGGREGATOR_FETCH_TIMEOUT = 20
SCRIPT_AGGREGATOR_ALLOWED_PREFIXES = (
    "https://kelee.one/Resource/JavaScript/",
    "https://raw.githubusercontent.com/zirawell/R-Store/main/Res/Scripts/AntiAd/",
    "https://raw.githubusercontent.com/fmz200/wool_scripts/main/Scripts/",
    "https://raw.githubusercontent.com/app2smile/rules/master/js/qq-news.js",
    "https://raw.githubusercontent.com/app2smile/rules/master/js/tieba-json.js",
)
SCRIPT_AGGREGATOR_PRESERVE_TOKENS = (
    "spotify",
    "youtube",
    "bilibili",
    "biliapi",
    "protobuf",
    "proto",
    "zhihu",
    "wechat",
    "weixin",
    "wechatpay",
    "alipay",
    "bank",
    "insurance",
    "finance",
    "securities",
    "fund",
    "loan",
    "credit",
    "wallet",
    "payment",
    "picc",
    "passport",
    "login",
    "auth",
    "12306",
    "umetrip",
    "airchina",
    "flight",
)


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


def unresolved_argument_names(text: str) -> set[str]:
    return {match.group(0)[3:-3].strip() for match in UNRESOLVED_ARGUMENT_RE.finditer(text)}


def declared_argument_names(text: str) -> set[str]:
    names: set[str] = set()
    for raw in text.splitlines():
        stripped = raw.strip()
        if not stripped.startswith("#!arguments="):
            continue
        raw_args = stripped.split("=", 1)[1]
        for item in raw_args.split(","):
            if ":" not in item:
                continue
            name = item.split(":", 1)[0].strip()
            if name:
                names.add(name)
    return names


def should_skip_generated_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return False
    placeholders = unresolved_argument_names(stripped)
    if placeholders and not placeholders <= FUSION_ARGUMENT_NAMES:
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
        if slug in PRESERVE_APP_SCRIPT_NAMES:
            lines.append(line)
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


def rule_policy(line: str) -> str | None:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None
    prefix = stripped.split(",", 1)[0]
    if prefix not in RULE_PREFIXES:
        return None
    parts = stripped.split(",")
    policy_parts = parts[1:] if parts[0] == "FINAL" else parts[2:]
    for part in policy_parts:
        token = part.strip().upper()
        if token in RULE_POLICY_TOKENS:
            return token
    return None


def strip_rule_policies(body: str, policies: set[str]) -> str:
    lines: list[str] = []
    for raw in body.splitlines():
        if rule_policy(raw) in policies:
            continue
        lines.append(raw)
    return "\n".join(lines).strip() + ("\n" if lines else "")


def append_compact_network_split(body: str) -> str:
    base = body.strip()
    suffix = "\n".join(COMPACT_NETWORK_SPLIT_RULES)
    return f"{base}\n\n{suffix}\n" if base else f"{suffix}\n"


@dataclass(frozen=True)
class ProtectedRoutePattern:
    kind: str
    host: str
    source: str = ""


def normalize_rule_host(value: str) -> str:
    host = value.strip().lower().rstrip(".")
    if host.startswith("*."):
        host = host[2:]
    return host


def parse_protected_route_patterns(body: str, source: str = "") -> tuple[ProtectedRoutePattern, ...]:
    patterns: list[ProtectedRoutePattern] = []
    seen: set[tuple[str, str]] = set()
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or rule_policy(line) not in {"DIRECT", "PROXY"}:
            continue
        parts = [part.strip() for part in line.split(",")]
        if len(parts) < 3 or parts[0] not in {"DOMAIN", "DOMAIN-SUFFIX"}:
            continue
        host = normalize_rule_host(parts[1])
        if not MITM_EXACT_HOST_RE.fullmatch(host):
            continue
        key = (parts[0], host)
        if key in seen:
            continue
        seen.add(key)
        patterns.append(ProtectedRoutePattern(kind=parts[0], host=host, source=source))
    return tuple(patterns)


def build_protected_route_patterns(profile: configparser.ConfigParser) -> tuple[ProtectedRoutePattern, ...]:
    paths: list[Path] = [MISC_SOURCES / name for name in MISC_PROTECT_RULE_FILES]
    if profile.has_section("rules"):
        for key in PROTECTED_PROFILE_RULE_KEYS:
            value = profile.get("rules", key, fallback="").strip()
            if value:
                paths.append(ROOT / value)

    patterns: list[ProtectedRoutePattern] = []
    seen: set[tuple[str, str]] = set()
    for path in paths:
        if not path.exists():
            continue
        body = split_source_fragment(read_text(path, required=False)).get("Rule", "")
        if not body.strip():
            body = read_text(path, required=False)
        try:
            source = path.relative_to(ROOT).as_posix()
        except ValueError:
            source = path.as_posix()
        for pattern in parse_protected_route_patterns(body, source):
            key = (pattern.kind, pattern.host)
            if key in seen:
                continue
            seen.add(key)
            patterns.append(pattern)
    return tuple(patterns)


def host_is_within_suffix(host: str, suffix: str) -> bool:
    return host == suffix or host.endswith(f".{suffix}")


def protected_pattern_overlaps_reject(
    reject_kind: str,
    reject_host: str,
    protected: ProtectedRoutePattern,
) -> bool:
    if reject_kind == "DOMAIN":
        if protected.kind == "DOMAIN":
            return reject_host == protected.host
        # A broad protection suffix does not prove that every exact ad endpoint
        # below it is core traffic. Only an exact suffix target is equivalent.
        return reject_host == protected.host
    if protected.kind == "DOMAIN":
        return host_is_within_suffix(protected.host, reject_host)
    # Rejecting the same or a broader suffix would cover the protected suffix.
    # A narrower reject may still be an app-scoped ad endpoint, so retain it.
    return host_is_within_suffix(protected.host, reject_host)


def reject_rule_target(line: str) -> tuple[str, str] | None:
    stripped = line.strip()
    if not stripped or stripped.startswith("#") or rule_policy(stripped) not in {
        "REJECT",
        "REJECT-DROP",
        "REJECT-TINYGIF",
        "REJECT-IMG",
    }:
        return None
    parts = [part.strip() for part in stripped.split(",")]
    if len(parts) < 3 or parts[0] not in {"DOMAIN", "DOMAIN-SUFFIX"}:
        return None
    host = normalize_rule_host(parts[1])
    if not MITM_EXACT_HOST_RE.fullmatch(host):
        return None
    return parts[0], host


def find_protected_reject_conflicts(
    body: str,
    protected_patterns: Iterable[ProtectedRoutePattern],
) -> list[str]:
    patterns = tuple(protected_patterns)
    conflicts: list[str] = []
    for raw in body.splitlines():
        target = reject_rule_target(raw)
        if target is None:
            continue
        kind, host = target
        if any(protected_pattern_overlaps_reject(kind, host, protected) for protected in patterns):
            conflicts.append(raw.strip())
    return conflicts


def strip_protected_reject_conflicts(
    body: str,
    protected_patterns: Iterable[ProtectedRoutePattern],
) -> str:
    conflicts = set(find_protected_reject_conflicts(body, protected_patterns))
    if not conflicts:
        return body
    lines = [raw for raw in body.splitlines() if raw.strip() not in conflicts]
    return "\n".join(lines).strip() + ("\n" if lines else "")


def joined_regex(patterns: list[str]) -> str:
    return "|".join(f"(?:{pattern})" for pattern in patterns)


def chunk_regex_patterns(patterns: list[str], prefix: str = "", suffix: str = "") -> list[list[str]]:
    chunks: list[list[str]] = []
    current: list[str] = []
    for pattern in patterns:
        candidate = [*current, pattern]
        if current and len(prefix + joined_regex(candidate) + suffix) > COMPACT_REGEX_LINE_LIMIT:
            chunks.append(current)
            current = [pattern]
        else:
            current = candidate
    if current:
        chunks.append(current)
    return chunks


def compact_regex_group(patterns: list[str], prefix: str = "", suffix: str = "") -> list[str]:
    return [prefix + joined_regex(chunk) + suffix for chunk in chunk_regex_patterns(patterns, prefix, suffix)]


def compact_url_rewrite(body: str) -> str:
    groups: dict[str, list[str]] = {}
    passthrough: list[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            passthrough.append(raw.rstrip())
            continue
        match = URL_REWRITE_REJECT_RE.match(line)
        if not match or match.group("action") not in COMPACT_URL_REWRITE_ACTIONS:
            passthrough.append(raw.rstrip())
            continue
        suffix = f" {match.group('replacement')} {match.group('action')}"
        groups.setdefault(suffix, []).append(match.group("pattern"))
    lines = [line for line in passthrough if line.strip()]
    for suffix, patterns in sorted(groups.items()):
        lines.extend(compact_regex_group(patterns, suffix=suffix))
    return "\n".join(lines).strip() + ("\n" if lines else "")


def compact_body_rewrite(body: str) -> str:
    groups: dict[tuple[str, str], list[str]] = {}
    passthrough: list[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            passthrough.append(raw.rstrip())
            continue
        parts = line.split(" ", 2)
        if len(parts) != 3 or parts[0] not in {"http-request", "http-response", "http-response-jq"}:
            passthrough.append(raw.rstrip())
            continue
        verb, pattern, operation = parts
        groups.setdefault((verb, operation), []).append(pattern)
    lines = [line for line in passthrough if line.strip()]
    for (verb, operation), patterns in sorted(groups.items()):
        lines.extend(compact_regex_group(patterns, prefix=f"{verb} ", suffix=f" {operation}"))
    return "\n".join(lines).strip() + ("\n" if lines else "")


def compact_map_local(body: str) -> str:
    groups: dict[str, list[str]] = {}
    passthrough: list[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            passthrough.append(raw.rstrip())
            continue
        parts = line.split(" ", 1)
        if len(parts) != 2:
            passthrough.append(raw.rstrip())
            continue
        pattern, operation = parts
        groups.setdefault(operation, []).append(pattern)
    lines = [line for line in passthrough if line.strip()]
    for operation, patterns in sorted(groups.items()):
        lines.extend(compact_regex_group(patterns, suffix=f" {operation}"))
    return "\n".join(lines).strip() + ("\n" if lines else "")


def compact_rewrite_section(section: str, body: str) -> str:
    if section == "URL Rewrite":
        return compact_url_rewrite(body)
    if section == "Body Rewrite":
        return compact_body_rewrite(body)
    if section == "Map Local":
        return compact_map_local(body)
    return body


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


def field_truthy(value: str | None) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes"}


def allowed_aggregate_script_path(path: str) -> bool:
    return any(path.startswith(prefix) for prefix in SCRIPT_AGGREGATOR_ALLOWED_PREFIXES)


def aggregate_candidate_reason(entry: dict[str, str]) -> str:
    script_type = entry.get("type", "").strip()
    script_path = entry.get("script-path", "").strip()
    lowered = " ".join([
        entry.get("__name__", ""),
        entry.get("pattern", ""),
        script_path,
    ]).lower()
    if script_type != "http-response":
        return "preserved: not http-response"
    if not field_truthy(entry.get("requires-body")):
        return "preserved: no response body"
    if field_truthy(entry.get("binary-body-mode")):
        return "preserved: binary body"
    if "argument" in entry:
        return "preserved: has argument"
    if not script_path.endswith(".js"):
        return "preserved: not javascript"
    if not allowed_aggregate_script_path(script_path):
        return "preserved: upstream not in aggregator allowlist"
    if any(token in lowered for token in SCRIPT_AGGREGATOR_PRESERVE_TOKENS):
        return "preserved: protected app or account/payment token"
    return ""


def fetch_script_source(url: str) -> tuple[str, str]:
    headers = {
        "User-Agent": "GrandpaNiu-Script-Aggregator/1.0",
        "Accept": "text/javascript,text/plain,*/*;q=0.8",
    }
    if "kelee.one/" in url:
        headers.update({
            "User-Agent": "Loon/889 CFNetwork/1496.0.7 Darwin/23.5.0",
            "Referer": "https://hub.kelee.one/",
        })
    request = urllib.request.Request(
        url,
        headers=headers,
    )
    try:
        with urllib.request.urlopen(request, timeout=SCRIPT_AGGREGATOR_FETCH_TIMEOUT) as response:
            data = response.read()
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return "", str(exc)
    text = data.decode("utf-8-sig", errors="replace").strip()
    if not text:
        return "", "empty script source"
    return text + "\n", ""


def parse_bundle_source_rows(bundle_text: str, manifest_text: str) -> dict[str, str]:
    try:
        manifest = json.loads(manifest_text)
    except json.JSONDecodeError:
        return {}
    key_to_url = {
        str(item.get("key", "")): str(item.get("url", ""))
        for item in manifest.get("sources", [])
        if isinstance(item, dict)
    }
    match = re.search(r"\n  const SOURCES = \{\n(?P<body>.*?)\n  \};", bundle_text, re.S)
    if not match:
        return {}
    rows: dict[str, str] = {}
    for raw in match.group("body").split(",\n"):
        line = raw.strip()
        if not line or ": " not in line:
            continue
        raw_key, raw_source = line.split(": ", 1)
        try:
            key = json.loads(raw_key)
            source = json.loads(raw_source)
        except json.JSONDecodeError:
            continue
        url = key_to_url.get(str(key), "")
        if url and isinstance(source, str) and source.strip() and allowed_aggregate_script_path(url):
            rows[url] = source if source.endswith("\n") else source + "\n"
    return rows


def read_git_head_text(relative: str) -> str:
    try:
        proc = subprocess.run(
            ["git", "show", f"HEAD:{relative}"],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            check=True,
            timeout=15,
        )
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return ""
    return proc.stdout


def load_committed_bundle_source_cache() -> dict[str, str]:
    cache: dict[str, str] = {}
    current_bundle = read_text(SCRIPT_BUNDLE, required=False)
    current_manifest = read_text(SCRIPT_BUNDLE_MANIFEST, required=False)
    if current_bundle and current_manifest:
        cache.update(parse_bundle_source_rows(current_bundle, current_manifest))
    head_bundle = read_git_head_text(SCRIPT_BUNDLE.relative_to(ROOT).as_posix())
    head_manifest = read_git_head_text(SCRIPT_BUNDLE_MANIFEST.relative_to(ROOT).as_posix())
    if head_bundle and head_manifest:
        cache.update(parse_bundle_source_rows(head_bundle, head_manifest))
    return cache


def load_script_source_cache() -> dict[str, str]:
    cache = load_committed_bundle_source_cache()
    if not SCRIPT_BUNDLE_CACHE.exists():
        return cache
    try:
        data = json.loads(read_text(SCRIPT_BUNDLE_CACHE))
    except (json.JSONDecodeError, OSError):
        return cache
    sources = data.get("sources", {}) if isinstance(data, dict) else {}
    if not isinstance(sources, dict):
        return cache
    for url, item in sources.items():
        if not isinstance(url, str) or not allowed_aggregate_script_path(url):
            continue
        source = item.get("source", "") if isinstance(item, dict) else item
        if isinstance(source, str) and source.strip():
            cache[url] = source if source.endswith("\n") else source + "\n"
    return cache


def write_script_source_cache(cache: dict[str, str]) -> None:
    rows = {}
    for url, source in sorted(cache.items()):
        rows[url] = {
            "sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
            "bytes": len(source.encode("utf-8")),
            "lines": len(source.splitlines()),
            "source": source,
        }
    payload = {
        "schema_version": 1,
        "generated": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "purpose": "Cache validated low-risk script sources so transient upstream fetch failures do not change the public module.",
        "sources": rows,
    }
    write_text(SCRIPT_BUNDLE_CACHE, json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def script_source_key(url: str) -> str:
    return "src_" + hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def js_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def build_script_bundle(routes: list[dict[str, str]], sources: dict[str, str]) -> str:
    route_rows = [
        "    {name: %s, pattern: %s, source: %s}" % (
            js_string(route["name"]),
            js_string(route["pattern"]),
            js_string(route["source_key"]),
        )
        for route in routes
    ]
    source_rows = [
        "    %s: %s" % (js_string(key), js_string(source))
        for key, source in sorted(sources.items())
    ]
    generated = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return "\n".join([
        "// Generated by scripts/build_module.py. Do not edit by hand.",
        f"// generated: {generated}",
        "// purpose: dispatch low-risk app cleanup scripts from one stable GrandpaNiu URL.",
        "(function () {",
        f"  const VERSION = {js_string(SCRIPT_BUNDLE_VERSION)};",
        "  const ROUTES = [",
        ",\n".join(route_rows),
        "  ];",
        "  const SOURCES = {",
        ",\n".join(source_rows),
        "  };",
        "",
        "  function requestUrl() {",
        "    try { return ($request && $request.url) || \"\"; } catch (_) { return \"\"; }",
        "  }",
        "  function finishUnchanged() {",
        "    try { $done({}); } catch (_) {}",
        "  }",
        "  function log(message) {",
        "    try { console.log(\"[GrandpaNiu script bundle] \" + message); } catch (_) {}",
        "  }",
        "  function runSource(name, source) {",
        "    const root = (typeof globalThis !== \"undefined\") ? globalThis : this;",
        "    const originalDone = root.$done;",
        "    let doneCalled = false;",
        "    if (typeof originalDone === \"function\") {",
        "      root.$done = function (payload) {",
        "        doneCalled = true;",
        "        return originalDone(payload);",
        "      };",
        "    }",
        "    try {",
        "      const result = (0, eval)(source);",
        "      if (!doneCalled) {",
        "        root.$done = originalDone;",
        "        log(name + \" did not call $done; passing through unchanged\");",
        "        return finishUnchanged();",
        "      }",
        "      return result;",
        "    } finally {",
        "      if (typeof originalDone === \"function\") root.$done = originalDone;",
        "    }",
        "  }",
        "",
        "  const url = requestUrl();",
        "  for (const route of ROUTES) {",
        "    try {",
        "      if (!new RegExp(route.pattern).test(url)) continue;",
        "      const source = SOURCES[route.source];",
        "      if (!source) { log(\"missing source for \" + route.name); return finishUnchanged(); }",
        "      return runSource(route.name, source);",
        "    } catch (error) {",
        "      log(route.name + \" failed: \" + (error && error.message ? error.message : error));",
        "      return finishUnchanged();",
        "    }",
        "  }",
        "  finishUnchanged();",
        "})();",
        "",
    ])


def chunk_patterns(routes: list[dict[str, str]]) -> list[list[dict[str, str]]]:
    chunks: list[list[dict[str, str]]] = []
    current: list[dict[str, str]] = []
    current_len = len("(?:)")
    for route in routes:
        pattern_len = len(route["pattern"])
        next_len = current_len + pattern_len + (1 if current else 0)
        if current and next_len > SCRIPT_AGGREGATOR_MAX_PATTERN_LEN:
            chunks.append(current)
            current = []
            current_len = len("(?:)")
        current.append(route)
        current_len += pattern_len + (1 if len(current) > 1 else 0)
    if current:
        chunks.append(current)
    return chunks


def build_script_bundle_manifest(
    stats: dict[str, object],
    routes: list[dict[str, str]],
    chunks: list[list[dict[str, str]]],
    sources_by_key: dict[str, str],
    source_urls_by_key: dict[str, str],
    bundle_text: str,
) -> dict[str, object]:
    chunk_by_name: dict[str, int] = {}
    for chunk_index, chunk in enumerate(chunks, 1):
        for route in chunk:
            chunk_by_name[route["name"]] = chunk_index

    source_rows = []
    for source_key, source in sorted(sources_by_key.items()):
        source_rows.append({
            "key": source_key,
            "url": source_urls_by_key.get(source_key, ""),
            "sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
            "bytes": len(source.encode("utf-8")),
            "lines": len(source.splitlines()),
        })

    route_rows = []
    for route in routes:
        route_rows.append({
            "name": route["name"],
            "pattern": route["pattern"],
            "pattern_sha256": hashlib.sha256(route["pattern"].encode("utf-8")).hexdigest(),
            "source_key": route["source_key"],
            "source_url": route["source_url"],
            "chunk": chunk_by_name.get(route["name"], 0),
        })

    return {
        "schema_version": 1,
        "generated": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "bundle": {
            "version": SCRIPT_BUNDLE_VERSION,
            "path": SCRIPT_BUNDLE.relative_to(ROOT).as_posix(),
            "url": SCRIPT_BUNDLE_URL,
            "sha256": hashlib.sha256(bundle_text.encode("utf-8")).hexdigest(),
            "chunks": len(chunks),
            "routes": len(routes),
            "sources": len(sources_by_key),
        },
        "policy": {
            "allowed_prefixes": list(SCRIPT_AGGREGATOR_ALLOWED_PREFIXES),
            "preserve_tokens": list(SCRIPT_AGGREGATOR_PRESERVE_TOKENS),
            "max_pattern_length": SCRIPT_AGGREGATOR_MAX_PATTERN_LEN,
            "fetch_timeout_seconds": SCRIPT_AGGREGATOR_FETCH_TIMEOUT,
        },
        "summary": {
            "input_entries": stats.get("input_entries", 0),
            "output_entries": stats.get("output_entries", 0),
            "unique_paths_before": stats.get("unique_paths_before", 0),
            "unique_paths_after": stats.get("unique_paths_after", 0),
            "bundled_entries": stats.get("bundled_entries", 0),
            "bundled_sources": stats.get("bundled_sources", 0),
            "fetch_failures": len(stats.get("fetch_failed", [])),
        },
        "routes": route_rows,
        "sources": source_rows,
        "fetch_failed": stats.get("fetch_failed", []),
        "fetch_cached": stats.get("fetch_cached", []),
        "preserved_reasons": stats.get("preserved_reasons", {}),
    }


def bundled_script_line(index: int, routes: list[dict[str, str]]) -> str:
    pattern = "(?:" + "|".join(route["pattern"] for route in routes) + ")"
    return (
        f"grandpaniu-script-bundle-{index} = "
        f"type=http-response,pattern={pattern},requires-body=1,max-size=0,"
        f"script-path={SCRIPT_BUNDLE_URL},script-update-interval=86400"
    )


def script_path_count(lines: list[str]) -> int:
    paths: set[str] = set()
    for line in lines:
        match = re.search(r"script-path=([^,\s]+)", line)
        if match:
            paths.add(match.group(1))
    return len(paths)


def write_script_aggregation_report(stats: dict[str, object]) -> None:
    bundled_names = stats.get("bundled_names", [])
    failed = stats.get("fetch_failed", [])
    cached = stats.get("fetch_cached", [])
    preserved = stats.get("preserved_reasons", {})
    lines = [
        "# Script Aggregation Report",
        "",
        f"- generated: {dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')}",
        f"- enabled: {stats.get('enabled', False)}",
        f"- input script entries: {stats.get('input_entries', 0)}",
        f"- output script entries: {stats.get('output_entries', 0)}",
        f"- unique script-path before: {stats.get('unique_paths_before', 0)}",
        f"- unique script-path after: {stats.get('unique_paths_after', 0)}",
        f"- bundled entries: {stats.get('bundled_entries', 0)}",
        f"- bundled upstream sources: {stats.get('bundled_sources', 0)}",
        f"- bundle chunks: {stats.get('bundle_chunks', 0)}",
        f"- output: `{SCRIPT_BUNDLE.relative_to(ROOT).as_posix()}`",
        f"- manifest: `{SCRIPT_BUNDLE_MANIFEST.relative_to(ROOT).as_posix()}`",
        "",
        "## Bundled Entries",
    ]
    if bundled_names:
        lines.extend(f"- `{name}`" for name in bundled_names)
    else:
        lines.append("- None")
    lines.extend(["", "## Fetch Failures"])
    if failed:
        for item in failed:
            lines.append(f"- `{item['url']}`: {item['reason']}")
    else:
        lines.append("- None")
    lines.extend(["", "## Cache Fallbacks"])
    if cached:
        for item in cached:
            lines.append(f"- `{item['url']}`: {item['reason']}")
    else:
        lines.append("- None")
    lines.extend(["", "## Preserved Reasons"])
    if preserved:
        for reason, count in sorted(preserved.items()):
            lines.append(f"- {reason}: {count}")
    else:
        lines.append("- None")
    write_text(SCRIPT_AGGREGATION_REPORT, "\n".join(lines) + "\n")


def aggregate_script_entries(body: str) -> str:
    lines = [line.rstrip() for line in body.splitlines() if line.strip()]
    stats: dict[str, object] = {
        "enabled": True,
        "input_entries": len(lines),
        "unique_paths_before": script_path_count(lines),
    }
    parsed: dict[int, dict[str, str]] = {}
    candidates: dict[int, dict[str, str]] = {}
    preserved_reasons: dict[str, int] = {}
    for index, line in enumerate(lines):
        entry = parse_script_entry(line.strip())
        if entry is None:
            preserved_reasons["preserved: unparsable or protected"] = preserved_reasons.get("preserved: unparsable or protected", 0) + 1
            continue
        parsed[index] = entry
        reason = aggregate_candidate_reason(entry)
        if reason:
            preserved_reasons[reason] = preserved_reasons.get(reason, 0) + 1
            continue
        candidates[index] = entry

    source_urls = sorted({entry["script-path"] for entry in candidates.values()})
    source_cache = load_script_source_cache()
    cache_dirty = not SCRIPT_BUNDLE_CACHE.exists()
    fetched_sources: dict[str, str] = {}
    fetch_failed: list[dict[str, str]] = []
    fetch_cached: list[dict[str, str]] = []
    for url in source_urls:
        source, reason = fetch_script_source(url)
        if reason:
            cached_source = source_cache.get(url, "")
            if cached_source:
                fetched_sources[url] = cached_source
                fetch_cached.append({"url": url, "reason": reason})
                continue
            fetch_failed.append({"url": url, "reason": reason})
            continue
        fetched_sources[url] = source
        if source_cache.get(url) != source:
            source_cache[url] = source
            cache_dirty = True

    if cache_dirty:
        write_script_source_cache(source_cache)

    routes: list[dict[str, str]] = []
    bundled_indices: set[int] = set()
    bundle_sources: dict[str, str] = {}
    bundle_source_urls: dict[str, str] = {}
    for index, entry in candidates.items():
        source_url = entry["script-path"]
        source = fetched_sources.get(source_url)
        if not source:
            continue
        source_key = script_source_key(source_url)
        bundle_sources[source_key] = source
        bundle_source_urls[source_key] = source_url
        routes.append({
            "name": entry["__name__"],
            "pattern": entry["pattern"],
            "source_key": source_key,
            "source_url": source_url,
        })
        bundled_indices.add(index)

    chunks = chunk_patterns(routes)
    bundle_text = build_script_bundle(routes, bundle_sources)
    write_text(SCRIPT_BUNDLE, bundle_text)
    manifest = build_script_bundle_manifest(
        stats | {
            "bundled_entries": len(routes),
            "bundled_sources": len(bundle_sources),
            "fetch_failed": fetch_failed,
            "fetch_cached": fetch_cached,
            "preserved_reasons": preserved_reasons,
        },
        routes,
        chunks,
        bundle_sources,
        bundle_source_urls,
        bundle_text,
    )
    write_text(SCRIPT_BUNDLE_MANIFEST, json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    bundled_lines = [bundled_script_line(index, chunk) for index, chunk in enumerate(chunks, 1)]
    inserted_bundle = False
    out: list[str] = []
    for index, line in enumerate(lines):
        if index in bundled_indices:
            if not inserted_bundle:
                out.extend(bundled_lines)
                inserted_bundle = True
            continue
        out.append(line)

    stats.update({
        "output_entries": len(out),
        "unique_paths_after": script_path_count(out),
        "bundled_entries": len(routes),
        "bundled_sources": len(bundle_sources),
        "bundle_chunks": len(chunks),
        "bundled_names": [route["name"] for route in routes],
        "fetch_failed": fetch_failed,
        "fetch_cached": fetch_cached,
        "preserved_reasons": preserved_reasons,
    })
    write_script_aggregation_report(stats)
    return "\n".join(out).strip() + "\n"


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
    rules = merge_lines(blocks)
    rules = strip_protected_reject_conflicts(rules, build_protected_route_patterns(profile))
    if as_bool(profile, "safety", "strip_direct_proxy_rules", False):
        rules = strip_rule_policies(rules, RULE_POLICIES_TO_STRIP)
    if as_bool(profile, "safety", "compact_network_split", False):
        rules = append_compact_network_split(rules)
    return rules


def build_scripts(profile: configparser.ConfigParser) -> str:
    blocks: list[str] = []
    if as_bool(profile, "include", "scripts", True):
        blocks.extend(load_optional_files(iter_profile_paths(profile, "scripts")))
    blocks.extend(app_section_blocks("Script"))
    blocks.extend(misc_section_blocks("Script"))
    if as_bool(profile, "include", "source_script_compat", True):
        blocks.append(read_text(source_file("Script"), required=False))
    return aggregate_script_entries(consolidate_script_entries(merge_lines(blocks)))


def build_rewrite_section(profile: configparser.ConfigParser, section: str) -> str:
    blocks: list[str] = [read_text(source_file(section), required=False)]
    profile_section = REWRITE_PROFILE_SECTIONS.get(section)
    if profile_section:
        blocks.extend(load_optional_files(iter_profile_paths(profile, profile_section)))
    blocks.extend(misc_section_blocks(section))
    blocks.extend(app_section_blocks(section))
    body = merge_lines(blocks)
    if as_bool(profile, "safety", "compact_rewrite_sections", False):
        body = compact_rewrite_section(section, body)
    return body


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


@dataclass(frozen=True)
class MITMHostEntry:
    order: int
    token: str
    normalized: str
    source: str
    raw_line: str


@dataclass(frozen=True)
class DeepFeature:
    order: int
    section: str
    expression: str
    action: str
    name: str
    source: str
    host_constraints: tuple[str, ...]
    opaque: bool
    requires_mitm: bool = True
    source_hosts: tuple[str, ...] = ()


class ShadowrocketMITMMatcher:
    """Conservative local model for target MITM hostname token matching."""

    CONTRACT_NAME = "shadowrocket-mitm-suffix-wildcard-v1"

    def __init__(
        self,
        wildcard_semantics_verified: bool = False,
        allow_reduction: bool = False,
        allow_equivalent_compaction: bool = False,
    ) -> None:
        self.wildcard_semantics_verified = wildcard_semantics_verified
        self.allow_reduction = allow_reduction
        self.allow_equivalent_compaction = allow_equivalent_compaction

    def normalize(self, value: str) -> str:
        return normalize_mitm_host_token(value)

    def covers(self, token: str, hostname: str) -> bool:
        token = self.normalize(token)
        hostname = self.normalize(hostname)
        if not token or token.startswith("-"):
            return False
        if token == hostname:
            return True
        if token.startswith("*."):
            suffix = token[2:]
            return hostname != suffix and hostname.endswith("." + suffix)
        return False

    def covered_by_any(self, hostname: str, tokens: Iterable[str]) -> bool:
        return any(self.covers(token, hostname) for token in tokens)

    def contract_evidence(self) -> dict[str, object]:
        return {
            "name": self.CONTRACT_NAME,
            "wildcard_semantics_verified": self.wildcard_semantics_verified,
            "allow_equivalent_compaction": self.allow_equivalent_compaction,
            "allow_range_reduction": self.allow_reduction,
            "exact_hostname_case_insensitive": True,
            "canonical_suffix_wildcard_matches_subdomains": True,
            "canonical_suffix_wildcard_matches_root": False,
            "canonical_suffix_wildcard_matches_multiple_levels": True,
            "negative_tokens_are_not_positive_coverage": True,
            "verification": "tests/test_mitm_optimizer.py and owner-approved repository compatibility contract",
        }


def normalize_mitm_host_token(token: str) -> str:
    return token.replace("%APPEND%", "").strip().lower()


def parse_mitm_host_entries(block: str, source: str, start_order: int = 0) -> list[MITMHostEntry]:
    entries: list[MITMHostEntry] = []
    order = start_order
    for line in block.splitlines():
        match = HOSTNAME_RE.match(line)
        if not match:
            continue
        value = match.group(1).replace("%APPEND%", "")
        for raw_host in value.split(","):
            clean = raw_host.strip()
            normalized = normalize_mitm_host_token(clean)
            if not normalized:
                continue
            entries.append(MITMHostEntry(order=order, token=clean, normalized=normalized, source=source, raw_line=line.strip()))
            order += 1
    return entries


def mitm_entry_dict(entry: MITMHostEntry) -> dict[str, object]:
    return {
        "order": entry.order,
        "token": entry.token,
        "normalized": entry.normalized,
        "source": entry.source,
        "raw_line": entry.raw_line,
    }


def deep_feature_dict(feature: DeepFeature) -> dict[str, object]:
    return {
        "order": feature.order,
        "section": feature.section,
        "expression": feature.expression,
        "action": feature.action,
        "name": feature.name,
        "source": feature.source,
        "host_constraints": list(feature.host_constraints),
        "opaque": feature.opaque,
        "requires_mitm": feature.requires_mitm,
        "source_hosts": list(feature.source_hosts),
    }


def ordered_unique_host_entries(entries: Iterable[MITMHostEntry]) -> list[MITMHostEntry]:
    unique: list[MITMHostEntry] = []
    seen: set[str] = set()
    for entry in entries:
        if entry.normalized in seen:
            continue
        seen.add(entry.normalized)
        unique.append(entry)
    return unique


def parse_script_fields(line: str) -> dict[str, str]:
    if "=" not in line:
        return {}
    _, body = line.split("=", 1)
    fields: dict[str, str] = {}
    for part in SCRIPT_FIELD_SPLIT_RE.split(body):
        if "=" not in part:
            continue
        key, value = part.strip().split("=", 1)
        fields[key.strip()] = value.strip()
    return fields


def unescape_host_fragment(value: str) -> tuple[str, bool]:
    host = value.strip()
    host = host.replace(r"\.", ".").replace(r"\-", "-").replace(r"\:", ":")
    if "\\" in host:
        return "", True
    if any(char in host for char in "()[]{}|+$^"):
        return "", True
    if "*" in host or "?" in host:
        return "", True
    if not host or host.startswith(".") or host.endswith("."):
        return "", True
    return host.lower(), False


def extract_static_hosts(expression: str) -> tuple[tuple[str, ...], bool]:
    if "{{{" in expression or "}}}" in expression:
        return (), True
    matches = list(URL_HOST_RE.finditer(expression))
    if not matches:
        return (), "http" in expression.lower()
    hosts: list[str] = []
    opaque = False
    for match in matches:
        raw_host = re.split(r"(?:\\\/|/)", match.group(1), maxsplit=1)[0]
        host, is_opaque = unescape_host_fragment(raw_host)
        if is_opaque:
            opaque = True
            continue
        hosts.append(host)
    return tuple(dict.fromkeys(hosts)), opaque or not hosts


def active_compiled_lines(body: str) -> list[str]:
    return [line.strip() for line in body.splitlines() if line.strip() and not line.lstrip().startswith("#")]


def feature_from_line(section: str, line: str, order: int) -> DeepFeature:
    name = ""
    expression = ""
    action = ""
    opaque = False
    if section == "Script":
        name = line.split("=", 1)[0].strip() if "=" in line else ""
        fields = parse_script_fields(line)
        expression = fields.get("pattern", "")
        action = fields.get("script-path", "")
        opaque = action.startswith(("http://", "https://")) or not expression
    elif section == "Body Rewrite":
        parts = line.split(" ", 2)
        expression = parts[1] if len(parts) > 1 else ""
        action = (parts[0] + (" " + parts[2] if len(parts) > 2 else "")).strip()
    else:
        parts = line.split(" ", 1)
        expression = parts[0] if parts else ""
        action = parts[1] if len(parts) > 1 else ""

    hosts, host_opaque = extract_static_hosts(expression)
    opaque = opaque or host_opaque
    return DeepFeature(
        order=order,
        section=section,
        expression=expression or line,
        action=action,
        name=name,
        source=f"compiled:{section}",
        host_constraints=hosts,
        opaque=opaque,
        source_hosts=hosts,
    )


def build_effective_deep_features(section_bodies: dict[str, str]) -> list[DeepFeature]:
    features: list[DeepFeature] = []
    order = 0
    for section in MITM_DEEP_FEATURE_SECTIONS:
        for line in active_compiled_lines(section_bodies.get(section, "")):
            features.append(feature_from_line(section, line, order))
            order += 1
    return features


def fingerprint_non_mitm_sections(section_bodies: dict[str, str]) -> list[dict[str, object]]:
    fingerprints: list[dict[str, object]] = []
    order = 0
    for section in SECTION_ORDER:
        if section == "MITM":
            continue
        for line in active_compiled_lines(section_bodies.get(section, "")):
            item: dict[str, object] = {"order": order, "section": section, "line": line}
            if section == "Script" and "=" in line:
                item["name"] = line.split("=", 1)[0].strip()
            fingerprints.append(item)
            order += 1
    return fingerprints


def non_mitm_fingerprint_summary(section_bodies: dict[str, str]) -> dict[str, object]:
    fingerprints = fingerprint_non_mitm_sections(section_bodies)
    payload = json.dumps(fingerprints, ensure_ascii=False, separators=(",", ":"))
    return {
        "sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
        "line_count": len(fingerprints),
    }


def feature_has_coverage(feature: DeepFeature, hosts: Iterable[str], matcher: ShadowrocketMITMMatcher) -> bool:
    if not feature.requires_mitm or feature.opaque or not feature.host_constraints:
        return True
    return all(matcher.covered_by_any(host, hosts) for host in feature.host_constraints)


def validate_compiled_mitm_contract(
    optimized_hosts: list[str],
    baseline_hosts: list[str],
    effective_deep_features: list[DeepFeature],
    matcher: ShadowrocketMITMMatcher,
    force_keep_hosts: Iterable[str],
    mode: str,
) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    optimized_set = set(optimized_hosts)
    baseline_set = set(baseline_hosts)
    force_keep = {normalize_mitm_host_token(host) for host in force_keep_hosts if normalize_mitm_host_token(host)}
    missing_force_keep = sorted(force_keep - optimized_set)
    if missing_force_keep:
        reasons.append("force_keep_hosts_missing:" + ",".join(missing_force_keep[:20]))
    if mode == "normalize" and optimized_set != baseline_set:
        reasons.append("normalized_set_differs_from_baseline")
    if mode == "reduce" and not optimized_set.issubset(baseline_set):
        reasons.append("reduced_set_is_not_baseline_subset")
    if mode == "reduce" and len(optimized_set) >= len(baseline_set):
        reasons.append("reduced_set_is_not_strictly_smaller")
    if mode == "equivalent":
        if not matcher.wildcard_semantics_verified:
            reasons.append("equivalent_matcher_contract_not_verified")
        if not optimized_set.issubset(baseline_set):
            reasons.append("equivalent_set_is_not_baseline_subset")
        baseline_patterns = {host for host in baseline_set if "*" in host or "?" in host}
        optimized_patterns = {host for host in optimized_set if "*" in host or "?" in host}
        if optimized_patterns != baseline_patterns:
            reasons.append("equivalent_pattern_token_set_changed")
        removed_hosts = baseline_set - optimized_set
        uncovered_removed = sorted(
            host
            for host in removed_hosts
            if host.startswith("-")
            or "*" in host
            or "?" in host
            or not matcher.covered_by_any(host, optimized_hosts)
        )
        if uncovered_removed:
            reasons.append("equivalent_removed_host_not_covered:" + ",".join(uncovered_removed[:20]))
    missing_coverage: list[str] = []
    for feature in effective_deep_features:
        if not feature.requires_mitm or feature.opaque or not feature.host_constraints:
            continue
        baseline_covered = feature_has_coverage(feature, baseline_hosts, matcher)
        optimized_covered = feature_has_coverage(feature, optimized_hosts, matcher)
        if baseline_covered and not optimized_covered:
            missing_coverage.append(f"{feature.section}:{feature.order}:{','.join(feature.host_constraints)}")
    if missing_coverage:
        reasons.append("deep_feature_mitm_coverage_missing:" + "|".join(missing_coverage[:20]))
    return not reasons, reasons


def reduction_candidates(
    baseline_hosts: list[str],
    effective_deep_features: list[DeepFeature],
    matcher: ShadowrocketMITMMatcher,
    force_keep_hosts: set[str],
) -> tuple[list[str], list[dict[str, object]], int]:
    optimized = list(baseline_hosts)
    items: list[dict[str, object]] = []
    baseline_set = set(baseline_hosts)
    opaque_retained = 0
    for wildcard in [host for host in baseline_hosts if host.startswith("*.")]:
        if wildcard in force_keep_hosts:
            items.append({"token": wildcard, "decision": "kept", "reason": "force_keep"})
            continue
        related = [feature for feature in effective_deep_features if any(matcher.covers(wildcard, host) for host in feature.host_constraints)]
        if not related:
            items.append({"token": wildcard, "decision": "kept", "reason": "no_static_consumers_is_not_deletion_proof"})
            continue
        if any(feature.opaque for feature in related):
            opaque_retained += 1
            items.append({"token": wildcard, "decision": "kept", "reason": "opaque_related_feature"})
            continue
        exact_hosts = sorted({host for feature in related for host in feature.host_constraints if matcher.covers(wildcard, host)})
        if not exact_hosts or any(host not in baseline_set for host in exact_hosts):
            items.append({"token": wildcard, "decision": "kept", "reason": "finite_exact_hosts_not_already_declared"})
            continue
        trial = [host for host in optimized if host != wildcard]
        if all(feature_has_coverage(feature, trial, matcher) for feature in related):
            optimized = trial
            items.append({"token": wildcard, "decision": "reduced", "replacement_hosts": exact_hosts})
        else:
            items.append({"token": wildcard, "decision": "kept", "reason": "coverage_would_change"})
    return optimized, items, opaque_retained


def equivalent_compaction_candidates(
    baseline_hosts: list[str],
    matcher: ShadowrocketMITMMatcher,
    force_keep_hosts: set[str],
) -> tuple[list[str], list[dict[str, object]]]:
    """Remove exact tokens already covered by an existing canonical wildcard."""

    wildcards = [
        host
        for host in baseline_hosts
        if host.startswith("*.") and MITM_EXACT_HOST_RE.fullmatch(host[2:])
    ]
    negative_patterns = [host[1:] for host in baseline_hosts if host.startswith("-") and len(host) > 1]
    optimized: list[str] = []
    items: list[dict[str, object]] = []
    for host in baseline_hosts:
        if host in force_keep_hosts:
            optimized.append(host)
            continue
        if not MITM_EXACT_HOST_RE.fullmatch(host):
            optimized.append(host)
            continue
        if any(matcher.covers(pattern, host) for pattern in negative_patterns):
            optimized.append(host)
            continue
        covering_wildcard = next(
            (wildcard for wildcard in wildcards if matcher.covers(wildcard, host)),
            "",
        )
        if not covering_wildcard:
            optimized.append(host)
            continue
        items.append(
            {
                "token": host,
                "decision": "removed_as_semantically_redundant",
                "covering_wildcard": covering_wildcard,
                "reason": "existing_wildcard_preserves_exact_host_coverage",
            }
        )
    return optimized, items


def as_mitm_entries(declared_hosts: Iterable[Any]) -> list[MITMHostEntry]:
    entries: list[MITMHostEntry] = []
    for order, value in enumerate(declared_hosts):
        if isinstance(value, MITMHostEntry):
            entries.append(value)
            continue
        token = str(value).strip()
        normalized = normalize_mitm_host_token(token)
        if normalized:
            entries.append(MITMHostEntry(order=order, token=token, normalized=normalized, source="<declared>", raw_line=token))
    return entries


def compile_mitm_hosts(
    declared_hosts: Iterable[Any],
    effective_deep_features: Iterable[DeepFeature],
    client_matcher: ShadowrocketMITMMatcher | None = None,
    force_keep_hosts: Iterable[str] = (),
) -> tuple[list[str], dict[str, object]]:
    """Normalize final MITM host output, with reduction allowed only under proof."""

    matcher = client_matcher or ShadowrocketMITMMatcher()
    features = list(effective_deep_features)
    entries = as_mitm_entries(declared_hosts)
    unique_entries = ordered_unique_host_entries(entries)
    baseline_hosts = [entry.normalized for entry in entries]
    unique_hosts = [entry.normalized for entry in unique_entries]
    baseline_set = set(baseline_hosts)
    wildcard_before = sum(1 for host in unique_hosts if host.startswith("*."))
    force_keep = {normalize_mitm_host_token(host) for host in force_keep_hosts if normalize_mitm_host_token(host)}
    optimization_items: list[dict[str, object]] = [
        {
            "token": entry.normalized,
            "decision": "kept",
            "reason": "first_occurrence",
            "source": entry.source,
            "order": entry.order,
        }
        for entry in unique_entries
    ]
    duplicate_entries: list[MITMHostEntry] = []
    duplicate_seen: set[str] = set()
    for entry in entries:
        if entry.normalized in duplicate_seen:
            duplicate_entries.append(entry)
            continue
        duplicate_seen.add(entry.normalized)

    mode = "normalize"
    optimized_hosts = list(unique_hosts)
    proof_reduce_disabled = 0
    range_reduction_disabled_count = 0
    proved_reduction_count = 0
    semantic_equivalent_removed_count = 0
    opaque_retained_count = 0
    reduction_items: list[dict[str, object]] = []
    if matcher.allow_reduction and matcher.wildcard_semantics_verified:
        mode = "reduce"
        optimized_hosts, reduction_items, opaque_retained_count = reduction_candidates(unique_hosts, features, matcher, force_keep)
        proved_reduction_count = sum(1 for item in reduction_items if item.get("decision") == "reduced")
        optimization_items.extend(reduction_items)
        if proved_reduction_count == 0:
            mode = "normalize"
            optimized_hosts = list(unique_hosts)
            proof_reduce_disabled = wildcard_before
    elif matcher.allow_equivalent_compaction and matcher.wildcard_semantics_verified:
        optimized_hosts, reduction_items = equivalent_compaction_candidates(unique_hosts, matcher, force_keep)
        first_entries = {entry.normalized: entry for entry in unique_entries}
        for item in reduction_items:
            exact_entry = first_entries.get(str(item.get("token", "")))
            wildcard_entry = first_entries.get(str(item.get("covering_wildcard", "")))
            if exact_entry is not None:
                item["source"] = exact_entry.source
                item["order"] = exact_entry.order
            if wildcard_entry is not None:
                item["covering_wildcard_source"] = wildcard_entry.source
                item["covering_wildcard_order"] = wildcard_entry.order
        semantic_equivalent_removed_count = len(reduction_items)
        optimization_items.extend(reduction_items)
        if semantic_equivalent_removed_count:
            mode = "equivalent"
        range_reduction_disabled_count = wildcard_before
    else:
        proof_reduce_disabled = wildcard_before
        range_reduction_disabled_count = wildcard_before
        optimization_items.extend(
            {"token": host, "decision": "kept", "reason": "proof_reduce_disabled_due_to_missing_matcher_evidence"}
            for host in unique_hosts
            if host.startswith("*.")
        )

    attempted_proved_reduction_count = proved_reduction_count
    attempted_semantic_equivalent_removed_count = semantic_equivalent_removed_count
    valid, reasons = validate_compiled_mitm_contract(optimized_hosts, unique_hosts, features, matcher, force_keep, mode)
    fallback = False
    fallback_reason = ""
    if not valid:
        fallback = True
        fallback_reason = ";".join(reasons)
        mode = "fallback"
        optimized_hosts = [entry.token for entry in unique_entries]
        proved_reduction_count = 0
        semantic_equivalent_removed_count = 0
    baseline_uncovered_count = sum(
        1
        for feature in features
        if feature.requires_mitm
        and not feature.opaque
        and feature.host_constraints
        and not feature_has_coverage(feature, unique_hosts, matcher)
    )

    evidence: dict[str, object] = {
        "version": 2,
        "generated_at": dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).isoformat(),
        "mode": mode,
        "baseline_hostname_token_count": len(baseline_hosts),
        "baseline_unique_hostname_token_count": len(unique_hosts),
        "normalized_hostname_token_count": len(optimized_hosts),
        "optimized_hostname_token_count": len(optimized_hosts),
        "same_hostname_token_set": {
            normalize_mitm_host_token(host) for host in optimized_hosts
        } == set(unique_hosts),
        "wildcard_count_before": wildcard_before,
        "wildcard_count_after": sum(1 for host in optimized_hosts if normalize_mitm_host_token(host).startswith("*.")),
        "deduplicated_exact_duplicate_count": len(baseline_hosts) - len(unique_hosts),
        "proved_reduction_count": proved_reduction_count,
        "attempted_proved_reduction_count": attempted_proved_reduction_count,
        "semantic_equivalent_removed_count": semantic_equivalent_removed_count,
        "attempted_semantic_equivalent_removed_count": attempted_semantic_equivalent_removed_count,
        "semantic_equivalent_removals": reduction_items if mode == "equivalent" else [],
        "opaque_retained_count": opaque_retained_count + sum(1 for feature in features if feature.opaque),
        "proof_reduce_disabled_due_to_missing_matcher_evidence": proof_reduce_disabled,
        "range_reduction_disabled_count": range_reduction_disabled_count,
        "same_mitm_coverage_under_matcher_contract": not fallback and mode in {"normalize", "equivalent"},
        "matcher_contract": matcher.contract_evidence(),
        "fallback": fallback,
        "fallback_reason": fallback_reason,
        "coverage_validation": {
            "passed": not fallback,
            "reasons": reasons,
            "deep_feature_count": len(features),
            "opaque_feature_count": sum(1 for feature in features if feature.opaque),
            "resolvable_feature_count": sum(1 for feature in features if not feature.opaque and feature.host_constraints),
            "baseline_uncovered_feature_count": baseline_uncovered_count,
        },
        "force_keep_hosts": sorted(force_keep),
        "baseline_unique_hosts": unique_hosts,
        "optimized_hosts": [normalize_mitm_host_token(host) for host in optimized_hosts],
        "host_entries": [mitm_entry_dict(entry) for entry in unique_entries],
        "duplicate_entries": [mitm_entry_dict(entry) for entry in duplicate_entries],
        "deep_features": [deep_feature_dict(feature) for feature in features],
        "optimization_items": optimization_items,
    }
    return optimized_hosts, evidence


def write_mitm_optimization_reports(evidence: dict[str, object]) -> None:
    MITM_OPTIMIZATION_REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    MITM_OPTIMIZATION_REPORT_JSON.write_text(json.dumps(evidence, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    coverage = evidence.get("coverage_validation", {})
    non_mitm = evidence.get("non_mitm_fingerprint", {})
    lines = [
        "# MITM Optimization Report",
        "",
        "- Scope: final Fusion `[MITM]` compile output only.",
        "- Guarantee: exact duplicates are removed, and exact tokens may be compacted only when an existing canonical wildcard preserves the same matcher coverage.",
        "- Boundary: Script, URL Rewrite, Header Rewrite, Body Rewrite, Map Local and Rule sections are not rewritten by this stage.",
        "- Reduction policy: no wildcard is created or removed; wildcard range reduction remains disabled.",
        "",
        "## Summary",
        "",
        f"- generated_at: `{evidence.get('generated_at')}`",
        f"- mode: `{evidence.get('mode')}`",
        f"- baseline hostname tokens: `{evidence.get('baseline_hostname_token_count')}`",
        f"- baseline unique hostname tokens: `{evidence.get('baseline_unique_hostname_token_count')}`",
        f"- normalized hostname tokens: `{evidence.get('normalized_hostname_token_count')}`",
        f"- same normalized hostname set: `{evidence.get('same_hostname_token_set')}`",
        f"- same MITM coverage under matcher contract: `{evidence.get('same_mitm_coverage_under_matcher_contract')}`",
        f"- matcher contract: `{(evidence.get('matcher_contract') or {}).get('name')}`",
        f"- non-MITM semantic fingerprint: `{non_mitm.get('sha256') if isinstance(non_mitm, dict) else None}`",
        f"- non-MITM fingerprint lines: `{non_mitm.get('line_count') if isinstance(non_mitm, dict) else None}`",
        f"- wildcard count before: `{evidence.get('wildcard_count_before')}`",
        f"- wildcard count after: `{evidence.get('wildcard_count_after')}`",
        f"- strict duplicate tokens removed: `{evidence.get('deduplicated_exact_duplicate_count')}`",
        f"- proved wildcard reductions: `{evidence.get('proved_reduction_count')}`",
        f"- attempted wildcard reductions: `{evidence.get('attempted_proved_reduction_count')}`",
        f"- semantically redundant exact tokens removed: `{evidence.get('semantic_equivalent_removed_count')}`",
        f"- attempted semantically redundant removals: `{evidence.get('attempted_semantic_equivalent_removed_count')}`",
        f"- opaque retained count: `{evidence.get('opaque_retained_count')}`",
        f"- reductions disabled by missing matcher proof: `{evidence.get('proof_reduce_disabled_due_to_missing_matcher_evidence')}`",
        f"- wildcard range reductions kept disabled: `{evidence.get('range_reduction_disabled_count')}`",
        f"- fallback: `{evidence.get('fallback')}`",
        f"- fallback reason: `{evidence.get('fallback_reason') or 'none'}`",
        "",
        "## Coverage Validation",
        "",
        f"- passed: `{coverage.get('passed')}`",
        f"- deep features: `{coverage.get('deep_feature_count')}`",
        f"- resolvable features: `{coverage.get('resolvable_feature_count')}`",
        f"- opaque features: `{coverage.get('opaque_feature_count')}`",
        f"- baseline uncovered features: `{coverage.get('baseline_uncovered_feature_count')}`",
        f"- reasons: `{'; '.join(coverage.get('reasons', [])) if isinstance(coverage.get('reasons'), list) and coverage.get('reasons') else 'none'}`",
        "",
        "## Source Trace",
        "",
        "- Full per-host source trace and compiled-section feature fingerprints are written to `reports/mitm_optimization_report.json`.",
        "- Equivalent compaction evidence records both the exact-token source and the covering-wildcard source in the JSON report.",
        "- This report does not claim every client behavior is globally proven; it states equivalence under the named repository matcher contract.",
        "- Any hostname or dependency that cannot be proven safe is kept in the output.",
        "",
    ]
    MITM_OPTIMIZATION_REPORT_MD.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def touch_mitm_optimization_reports() -> None:
    """Keep report mtimes newer than the final module written from the same build."""
    reference_time = max(
        (path.stat().st_mtime for path in (RELEASE, MITM_OPTIMIZATION_REPORT_JSON, MITM_OPTIMIZATION_REPORT_MD) if path.exists()),
        default=0.0,
    )
    validated_time = reference_time + 1.0
    for path in (MITM_OPTIMIZATION_REPORT_JSON, MITM_OPTIMIZATION_REPORT_MD):
        if path.exists():
            os.utime(path, (validated_time, validated_time))


def force_keep_mitm_hosts(entries: Iterable[MITMHostEntry]) -> set[str]:
    keep = {normalize_mitm_host_token(host) for host in MITM_FORCE_KEEP_TOKENS}
    for entry in entries:
        token = entry.normalized
        if token.startswith("-"):
            keep.add(token)
    return {host for host in keep if host}


def collect_mitm_entries(profile: configparser.ConfigParser) -> tuple[list[MITMHostEntry], list[str]]:
    """Collect final Fusion MITM declarations without running other build stages."""

    entries: list[MITMHostEntry] = []
    sources: list[str] = []
    for path in iter_profile_paths(profile, "mitm"):
        if not path.exists():
            stop(f"profile MITM source missing: {path.relative_to(ROOT)}")
        source = path.relative_to(ROOT).as_posix()
        sources.append(source)
        entries.extend(parse_mitm_host_entries(read_text(path), source, len(entries)))
    for path, block in misc_mitm_blocks():
        source = path.relative_to(ROOT).as_posix()
        sources.append(source)
        entries.extend(parse_mitm_host_entries(block, source, len(entries)))
    for path, block in app_mitm_blocks():
        source = path.relative_to(ROOT).as_posix()
        sources.append(source)
        entries.extend(parse_mitm_host_entries(block, source, len(entries)))
    return entries, sources


def build_mitm(profile: configparser.ConfigParser, section_bodies: dict[str, str] | None = None) -> str:
    """Build the MITM section from profile-selected layers."""
    if not profile.has_section("mitm"):
        return read_text(source_file("MITM"), required=False).rstrip() + "\n"

    entries, sources = collect_mitm_entries(profile)
    comments: list[str] = ["# MITM profile layers generated by scripts/build_module.py"]
    comments.extend(f"# source: {source}" for source in sources)
    if not entries:
        stop("profile MITM sources produced an empty hostname list")

    deep_features = build_effective_deep_features(section_bodies or {})
    matcher = ShadowrocketMITMMatcher(
        wildcard_semantics_verified=True,
        allow_reduction=False,
        allow_equivalent_compaction=True,
    )
    hosts, evidence = compile_mitm_hosts(entries, deep_features, matcher, force_keep_mitm_hosts(entries))
    evidence["non_mitm_fingerprint"] = non_mitm_fingerprint_summary(section_bodies or {})
    if not hosts:
        evidence["fallback"] = True
        evidence["fallback_reason"] = "optimizer_returned_empty_host_list"
        hosts = [entry.token for entry in ordered_unique_host_entries(entries)]
    write_mitm_optimization_reports(evidence)
    return "\n".join(comments + ["hostname = %APPEND% " + ",".join(hosts)]) + "\n"


def build_from_sources(profile_name: str = DEFAULT_PROFILE) -> str:
    profile = load_profile(profile_name)
    parts: list[str] = [read_text(source_file("META")).rstrip()]
    section_bodies: dict[str, str] = {}
    for section in SECTION_ORDER:
        parts.append(f"[{section}]")
        if section == "Rule":
            body = build_rules(profile)
        elif section == "Script":
            body = build_scripts(profile)
        elif section == "MITM":
            body = build_mitm(profile, section_bodies)
        elif section in REWRITE_PROFILE_SECTIONS:
            body = build_rewrite_section(profile, section)
        else:
            body = read_text(source_file(section), required=False).rstrip() + "\n"
        section_bodies[section] = body
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
    unresolved = unresolved_argument_names(text)
    if unresolved:
        declared = declared_argument_names(text)
        missing = sorted(unresolved - declared)
        if missing:
            stop("generated module contains undeclared argument placeholders: " + ", ".join(missing))
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
        if "-grpc.biliapi.net" in hosts:
            stop("MITM must not exclude grpc.biliapi.net; Bilibili protobuf cleanup requires it")
        if "grpc.biliapi.net" not in hosts:
            stop("MITM must include grpc.biliapi.net for Bilibili protobuf cleanup")
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
        refresh_module_date(today_beijing())
        release_text = build_from_sources(args.profile)
        validate(release_text)
        write_text(RELEASE, release_text)
        write_text(REPORT, make_report(release_text, extracted, args.profile))
        write_text(DIFF_REPORT, make_diff_report(release_text))
        touch_mitm_optimization_reports()
        print(f"Built {RELEASE} ({len(release_text.splitlines())} lines) using profile={args.profile}")


if __name__ == "__main__":
    main()
