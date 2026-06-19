#!/usr/bin/env python3
"""Convert selected Quantumult X rule lists and normalize remote rule types.

The generated files are consumed through RULE-SET entries in Shadowrocket modules.
Do not put QuanX `host`, `host-suffix`, `host-keyword`, `ip-cidr`, or
`ip6-cidr` rules directly into Shadowrocket RULE-SET remotes.

This script also normalizes known pure-domain upstreams to DOMAIN-SET before
module builds, so stale compatibility sources cannot reintroduce Shadowrocket
remote-rule red-cross failures.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "Rules" / "converted"
REMOTES_JSON = ROOT / "Rewrite" / "Remotes" / "sources.json"
USER_AGENT = "GrandpaNiu-QuanX-Rule-Converter/1.1"

PURE_DOMAIN_SET_URLS = {
    "https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules_surge_domainset.txt",
    "https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge2.txt",
    "https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/reject.txt",
    "https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksurge.list",
}

NORMALIZE_TEXT_FILES = [
    ROOT / "Ronghemokuai.sgmodule",
    ROOT / "Release" / "Ronghemokuai.sgmodule",
    ROOT / "Rewrite" / "Sources" / "Rule.conf",
    ROOT / "Rules" / "original-remote-rule-sets.list",
]


@dataclass(frozen=True)
class Source:
    name: str
    url: str
    output: Path


SOURCES = [
    Source(
        name="zirawell App AdBlock",
        url="https://raw.githubusercontent.com/zirawell/R-Store/main/Rule/QuanX/Adblock/All/filter/appAdBlock.list",
        output=OUT_DIR / "zirawell-appAdBlock-shadowrocket.list",
    ),
    Source(
        name="zirawell All AdBlock",
        url="https://raw.githubusercontent.com/zirawell/R-Store/main/Rule/QuanX/Adblock/All/filter/allAdBlock.list",
        output=OUT_DIR / "zirawell-allAdBlock-shadowrocket.list",
    ),
]

RULE_TYPE_MAP = {
    "host": "DOMAIN",
    "host-suffix": "DOMAIN-SUFFIX",
    "host-keyword": "DOMAIN-KEYWORD",
    "ip-cidr": "IP-CIDR",
    "ip-cidr6": "IP-CIDR6",
    "ip6-cidr": "IP-CIDR6",
}

DOMAIN_VALUE_RE = re.compile(r"^[A-Za-z0-9*_.:-]+$")

PROTECTED_CONVERTED_RULE_TOKENS = (
    "api.iqiyi.com",
    "api.biliapi",
    "app.biliapi",
    "httpdns",
    "hdns.ksyun.com",
    "adgw.alipay.com",
    "amdc.alipay.com",
    "amdc-sibling.alipay.com.cn",
    "mobiledc.stable.alipay.net",
    "rtms.alipay.com",
    "api.verify.mob.com",
    "log-verify.mob.com",
    "mdap.wallet.pbcdci.cn",
    "mdc.wallet.pbcdci.cn",
    "baidustatic.com",
    "zijieapi.com",
    "zijieapi.net",
    "zijiecdn.com",
    "snssdk.com",
    "video-cn.snssdk.com",
)


def stop(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def normalize_pure_domain_set_remotes() -> list[str]:
    changed: list[str] = []

    for path in NORMALIZE_TEXT_FILES:
        if not path.exists():
            continue
        text = read_text(path)
        original = text
        for url in PURE_DOMAIN_SET_URLS:
            text = text.replace(f"RULE-SET,{url},", f"DOMAIN-SET,{url},")
        if text != original:
            write_text(path, text)
            changed.append(path.relative_to(ROOT).as_posix())

    if REMOTES_JSON.exists():
        try:
            data = json.loads(read_text(REMOTES_JSON))
        except json.JSONDecodeError as exc:
            stop(f"invalid JSON in {REMOTES_JSON.relative_to(ROOT)}: {exc}")
        json_changed = False
        for item in data.get("rule_sets", []):
            url = str(item.get("url", "")).strip()
            if url in PURE_DOMAIN_SET_URLS and item.get("type") != "DOMAIN-SET":
                item["type"] = "DOMAIN-SET"
                item["purpose"] = "domain-set advertising supplement"
                json_changed = True
        if json_changed:
            write_text(REMOTES_JSON, json.dumps(data, ensure_ascii=False, indent=2) + "\n")
            changed.append(REMOTES_JSON.relative_to(ROOT).as_posix())

    return changed


def fetch_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            return response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        stop(f"failed to fetch {url}: {exc}")
    except UnicodeDecodeError as exc:
        stop(f"upstream is not valid UTF-8: {url}: {exc}")


def clean_value(value: str, rule_type: str) -> str:
    value = value.strip()
    if rule_type in {"DOMAIN", "DOMAIN-SUFFIX"}:
        if value.startswith("*."):
            value = value[2:]
        value = value.lstrip(".")
    return value


def convert_line(raw: str) -> tuple[str | None, str | None]:
    line = raw.strip()
    if not line or line.startswith(("#", ";", "//")):
        return None, None

    parts = [part.strip() for part in line.split(",")]
    if len(parts) < 2:
        return None, raw

    source_type = parts[0].lower()
    target_type = RULE_TYPE_MAP.get(source_type)
    if target_type is None:
        return None, raw

    value = clean_value(parts[1], target_type)
    if not value:
        return None, raw

    if target_type.startswith("DOMAIN") and not DOMAIN_VALUE_RE.match(value):
        return None, raw

    if target_type in {"IP-CIDR", "IP-CIDR6"}:
        return f"{target_type},{value},no-resolve", None
    return f"{target_type},{value}", None


def is_protected_converted_rule(line: str) -> bool:
    lowered = line.lower()
    return any(token in lowered for token in PROTECTED_CONVERTED_RULE_TOKENS)


def source_meta(text: str) -> list[str]:
    keep_prefixes = ("#!name=", "#!desc=", "#!author=", "#!homepage=", "#!raw-url=", "#!date=")
    lines: list[str] = []
    for raw in text.splitlines():
        stripped = raw.strip()
        if stripped.startswith(keep_prefixes):
            lines.append("# upstream-" + stripped[2:])
    return lines


def convert_text(source: Source, text: str) -> str:
    rules: list[str] = []
    seen: set[str] = set()
    unsupported: list[str] = []
    filtered: list[str] = []

    for raw in text.splitlines():
        converted, bad = convert_line(raw)
        if converted:
            if is_protected_converted_rule(converted):
                filtered.append(converted)
                continue
            if converted not in seen:
                seen.add(converted)
                rules.append(converted)
            continue
        if bad:
            unsupported.append(bad.strip())

    if unsupported:
        preview = "\n".join(f"  - {line}" for line in unsupported[:20])
        stop(
            f"{source.name} has unsupported QuanX rules; refusing incomplete conversion.\n"
            f"Unsupported count: {len(unsupported)}\n{preview}"
        )

    if not rules:
        stop(f"{source.name} conversion produced no rules")

    header = [
        "# Converted for Shadowrocket/Surge RULE-SET usage.",
        "# Do not edit by hand; generated by scripts/convert_quanx_rules.py.",
        f"# source-name: {source.name}",
        f"# source-url: {source.url}",
        f"# rule-count: {len(rules)}",
        f"# protected-filtered-count: {len(filtered)}",
        *source_meta(text),
        "",
    ]
    return "\n".join(header + rules).rstrip() + "\n"


def main() -> None:
    normalized = normalize_pure_domain_set_remotes()
    if normalized:
        print("Normalized pure DOMAIN-SET remotes in: " + ", ".join(normalized))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for source in SOURCES:
        text = fetch_text(source.url)
        converted = convert_text(source, text)
        source.output.write_text(converted, encoding="utf-8", newline="\n")
        print(f"Converted {source.name}: {source.output.relative_to(ROOT)} ({len(converted.splitlines())} lines)")


if __name__ == "__main__":
    main()
