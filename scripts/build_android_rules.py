#!/usr/bin/env python3
"""Build Android app rule formats from Android/sources/apps.yaml.

The source file intentionally uses JSON-compatible YAML so the builder can run
with the Python standard library only.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Android" / "sources" / "apps.yaml"
MIHOMO_DIR = ROOT / "Android" / "mihomo" / "apps"
SING_BOX_DIR = ROOT / "Android" / "sing-box" / "apps"
ADGUARD_DIR = ROOT / "Android" / "adguard" / "apps"
V2RAYNG_DIR = ROOT / "Android" / "v2rayng" / "apps"
REPORT = ROOT / "reports" / "android_rules_report.md"

SUPPORTED_TYPES = {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD"}


def read_source() -> dict[str, Any]:
    if not SOURCE.exists():
        raise SystemExit(f"missing source: {SOURCE.relative_to(ROOT)}")
    try:
        data = json.loads(SOURCE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON-compatible YAML in {SOURCE.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("apps"), dict):
        raise SystemExit("Android/sources/apps.yaml must contain an apps object")
    return data


def clean_app_name(name: str) -> str:
    allowed = []
    for char in name.strip():
        if char.isalnum() or char in {"-", "_"}:
            allowed.append(char)
        elif char in {" ", "/"}:
            allowed.append("-")
    cleaned = "".join(allowed).strip("-")
    if not cleaned:
        raise SystemExit(f"invalid app name: {name!r}")
    return cleaned


def normalize_rules(app_name: str, rules: list[dict[str, Any]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    normalized: list[dict[str, str]] = []
    for index, rule in enumerate(rules, 1):
        if not isinstance(rule, dict):
            raise SystemExit(f"{app_name} rule[{index}] must be an object")
        rule_type = str(rule.get("type", "")).strip().upper()
        value = str(rule.get("value", "")).strip()
        if rule_type not in SUPPORTED_TYPES:
            raise SystemExit(f"{app_name} rule[{index}] has unsupported type: {rule_type}")
        if not value:
            raise SystemExit(f"{app_name} rule[{index}] has empty value")
        key = (rule_type, value.lower())
        if key in seen:
            continue
        seen.add(key)
        normalized.append({
            "type": rule_type,
            "value": value,
            "risk": str(rule.get("risk", "medium")).strip().lower(),
            "purpose": str(rule.get("purpose", "unspecified")).strip(),
        })
    normalized.sort(key=lambda item: (item["type"], item["value"].lower()))
    return normalized


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
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False) + "\n"


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
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False) + "\n"


def write_if_changed(path: Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def generate_report(app_stats: list[dict[str, Any]]) -> None:
    now = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# Android 规则生成报告",
        "",
        f"- 最后更新时间：{now}",
        f"- App 总数：{len(app_stats)}",
        "- 源头：Android/sources/apps.yaml",
        "- 输出：Mihomo / sing-box / AdGuard / v2rayNG",
        "",
        "| App | 规则数 | 风险 | 测试状态 | 国内组合包 | 四格式输出 |",
        "|---|---:|---|---|---|---|",
    ]
    for item in sorted(app_stats, key=lambda row: row["name"].lower()):
        lines.append(
            f"| {item['name']} | {item['count']} | {item['risk']} | {item['test_status']} | "
            f"{'是' if item['domestic_bundle'] else '否'} | 是 |"
        )
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    data = read_source()
    app_stats: list[dict[str, Any]] = []
    domestic_rules: list[dict[str, str]] = []

    for app_name, meta in sorted(data["apps"].items(), key=lambda item: item[0].lower()):
        if not isinstance(meta, dict):
            raise SystemExit(f"{app_name} metadata must be an object")
        rules = normalize_rules(app_name, meta.get("rules", []))
        safe_name = clean_app_name(app_name)
        write_if_changed(MIHOMO_DIR / f"{safe_name}.yaml", render_mihomo(rules))
        write_if_changed(SING_BOX_DIR / f"{safe_name}.json", render_sing_box(rules))
        write_if_changed(ADGUARD_DIR / f"{safe_name}.txt", render_adguard(rules))
        write_if_changed(V2RAYNG_DIR / f"{safe_name}-routing.json", render_v2rayng(rules))

        domestic = bool(meta.get("domestic_bundle", False))
        if domestic:
            domestic_rules.extend(rules)
        app_stats.append({
            "name": safe_name,
            "count": len(rules),
            "risk": meta.get("risk", "medium"),
            "test_status": meta.get("test_status", "untested"),
            "domestic_bundle": domestic,
        })

    if domestic_rules:
        domestic_rules = normalize_rules("Domestic-Apps", domestic_rules)
        write_if_changed(MIHOMO_DIR / "Domestic-Apps.yaml", render_mihomo(domestic_rules))
        write_if_changed(SING_BOX_DIR / "Domestic-Apps.json", render_sing_box(domestic_rules))
        write_if_changed(ADGUARD_DIR / "Domestic-Apps.txt", render_adguard(domestic_rules))
        write_if_changed(V2RAYNG_DIR / "Domestic-Apps-routing.json", render_v2rayng(domestic_rules))

    generate_report(app_stats)
    print("Android rule formats generated.")


if __name__ == "__main__":
    main()
