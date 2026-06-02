#!/usr/bin/env python3
"""Build Android app rule formats.

Current source of truth: Android/mihomo/apps/*.yaml

This absorbs the useful idea from the old builder.py: use one app-level source
and generate the other distributable formats from it. A structured JSON/YAML
source can be added later, but this keeps the repository runnable immediately.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MIHOMO_DIR = ROOT / "Android" / "mihomo" / "apps"
SING_BOX_DIR = ROOT / "Android" / "sing-box" / "apps"
ADGUARD_DIR = ROOT / "Android" / "adguard" / "apps"
V2RAYNG_DIR = ROOT / "Android" / "v2rayng" / "apps"
REPORT = ROOT / "reports" / "android_rules_report.md"
SUPPORTED_TYPES = {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD"}


def parse_mihomo_file(path: Path) -> list[dict[str, str]]:
    rules: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line == "payload:" or line.startswith("#"):
            continue
        if line.startswith("-"):
            line = line[1:].strip()
        if "," not in line:
            continue
        rule_type, value = [part.strip() for part in line.split(",", 1)]
        rule_type = rule_type.upper()
        if rule_type not in SUPPORTED_TYPES or not value:
            continue
        key = (rule_type, value.lower())
        if key in seen:
            continue
        seen.add(key)
        rules.append({"type": rule_type, "value": value})
    rules.sort(key=lambda item: (item["type"], item["value"].lower()))
    return rules


def render_mihomo(rules: list[dict[str, str]]) -> str:
    lines = ["payload:"]
    lines.extend(f"  - {rule['type']},{rule['value']}" for rule in rules)
    return "\n".join(lines) + "\n"


def render_sing_box(rules: list[dict[str, str]]) -> str:
    bucket = {"domain": [], "domain_suffix": [], "domain_keyword": []}
    for rule in rules:
        if rule["type"] == "DOMAIN":
            bucket["domain"].append(rule["value"])
        elif rule["type"] == "DOMAIN-SUFFIX":
            bucket["domain_suffix"].append(rule["value"])
        elif rule["type"] == "DOMAIN-KEYWORD":
            bucket["domain_keyword"].append(rule["value"])
    payload = {"version": 1, "rules": [{key: values for key, values in bucket.items() if values}]}
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def render_adguard(rules: list[dict[str, str]]) -> str:
    lines: list[str] = []
    for rule in rules:
        value = rule["value"]
        if rule["type"] in {"DOMAIN", "DOMAIN-SUFFIX"}:
            lines.append(f"||{value}^")
        elif rule["type"] == "DOMAIN-KEYWORD":
            lines.append(f"/{value}/")
    return "\n".join(lines) + "\n"


def render_v2rayng(rules: list[dict[str, str]]) -> str:
    domains: list[str] = []
    for rule in rules:
        value = rule["value"]
        if rule["type"] == "DOMAIN":
            domains.append(f"full:{value}")
        elif rule["type"] == "DOMAIN-SUFFIX":
            domains.append(f"domain:{value}")
        elif rule["type"] == "DOMAIN-KEYWORD":
            domains.append(f"keyword:{value}")
    payload = {"routing": {"rules": [{"type": "field", "domain": domains, "outboundTag": "block"}]}}
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def write_if_changed(path: Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def generate_report(stats: list[dict[str, str | int]]) -> None:
    now = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# Android 规则生成报告",
        "",
        f"- 最后更新时间：{now}",
        f"- App 总数：{len(stats)}",
        "- 当前源头：Android/mihomo/apps/*.yaml",
        "- 输出：Mihomo / sing-box / AdGuard / v2rayNG",
        "",
        "| App | 规则数 | 四格式输出 |",
        "|---|---:|---|",
    ]
    for item in sorted(stats, key=lambda row: str(row["name"]).lower()):
        lines.append(f"| {item['name']} | {item['count']} | 是 |")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    if not MIHOMO_DIR.exists():
        raise SystemExit("missing Android/mihomo/apps source directory")
    stats: list[dict[str, str | int]] = []
    for source in sorted(MIHOMO_DIR.glob("*.yaml"), key=lambda path: path.name.lower()):
        app_name = source.stem
        rules = parse_mihomo_file(source)
        if not rules:
            continue
        normalized = render_mihomo(rules)
        write_if_changed(source, normalized)
        write_if_changed(SING_BOX_DIR / f"{app_name}.json", render_sing_box(rules))
        write_if_changed(ADGUARD_DIR / f"{app_name}.txt", render_adguard(rules))
        write_if_changed(V2RAYNG_DIR / f"{app_name}-routing.json", render_v2rayng(rules))
        stats.append({"name": app_name, "count": len(rules)})
    generate_report(stats)
    print("Android rule formats generated.")


if __name__ == "__main__":
    main()
