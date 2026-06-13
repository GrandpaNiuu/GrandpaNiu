#!/usr/bin/env python3
"""Audit compatibility source fragments before disabling compat layers."""

from __future__ import annotations

import configparser
import datetime as dt
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "Rewrite" / "Profiles" / "stable.conf"
RULE_COMPAT = ROOT / "Rewrite" / "Sources" / "Rule.conf"
SCRIPT_COMPAT = ROOT / "Rewrite" / "Sources" / "Script.conf"
SOURCES_JSON = ROOT / "Rewrite" / "Remotes" / "sources.json"
REPORT = ROOT / "reports" / "compat_migration_report.md"
SCRIPT_NAME_RE = re.compile(r"^\s*([^#\s][^=]+?)\s*=")
REMOTE_RE = re.compile(r"^(RULE-SET|DOMAIN-SET),([^,]+),([^,]+)$")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def active_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip() and not line.lstrip().startswith("#")]


def script_names(text: str) -> list[str]:
    names: list[str] = []
    for line in active_lines(text):
        match = SCRIPT_NAME_RE.match(line)
        if match:
            names.append(match.group(1).strip())
    return names


def profile_flags() -> tuple[bool, bool]:
    parser = configparser.ConfigParser()
    parser.read(PROFILE, encoding="utf-8")
    return (
        parser.getboolean("include", "source_rule_compat", fallback=False),
        parser.getboolean("include", "source_script_compat", fallback=False),
    )


def remote_source_lines() -> set[str]:
    try:
        data = json.loads(read(SOURCES_JSON) or "{}")
    except json.JSONDecodeError:
        return set()
    lines: set[str] = set()
    for item in data.get("rule_sets", []):
        if not item.get("enabled", False):
            continue
        rule_type = str(item.get("type", "")).strip()
        url = str(item.get("url", "")).strip()
        policy = str(item.get("policy", "REJECT")).strip()
        if rule_type and url and policy:
            lines.add(f"{rule_type},{url},{policy}")
    return lines


def is_rule_migrated(line: str, rules_text: str, remote_lines: set[str]) -> bool:
    if line in rules_text:
        return True
    if line in remote_lines:
        return True
    match = REMOTE_RE.match(line)
    if match:
        _, url, _ = match.groups()
        return any(url in remote_line for remote_line in remote_lines)
    return False


def main() -> None:
    source_rule_compat, source_script_compat = profile_flags()
    rule_lines = active_lines(read(RULE_COMPAT))
    script_lines = active_lines(read(SCRIPT_COMPAT))

    rules_text = "\n".join(read(path) for path in (ROOT / "Rules").glob("*.list"))
    scripts_text = "\n".join(read(path) for path in (ROOT / "Scripts").glob("*.conf"))
    remotes = remote_source_lines()

    migrated_rules = [line for line in rule_lines if is_rule_migrated(line, rules_text, remotes)]
    pending_rules = [line for line in rule_lines if not is_rule_migrated(line, rules_text, remotes)]

    compat_script_names = script_names("\n".join(script_lines))
    migrated_script_names = set(script_names(scripts_text))
    migrated_scripts = [name for name in compat_script_names if name in migrated_script_names]
    pending_scripts = [name for name in compat_script_names if name not in migrated_script_names]

    can_close = not pending_rules and not pending_scripts
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
    lines = [
        "# 兼容层迁移审计报告",
        "",
        f"- 日期：{today}",
        f"- source_rule_compat 当前是否开启：{'是' if source_rule_compat else '否'}",
        f"- source_script_compat 当前是否开启：{'是' if source_script_compat else '否'}",
        f"- Rule.conf 行数：{len(read(RULE_COMPAT).splitlines())}",
        f"- Script.conf 行数：{len(read(SCRIPT_COMPAT).splitlines())}",
        f"- 已迁移规则数量：{len(migrated_rules)}",
        f"- 未迁移规则数量：{len(pending_rules)}",
        f"- 已迁移脚本数量：{len(migrated_scripts)}",
        f"- 未迁移脚本数量：{len(pending_scripts)}",
        f"- 建议下一步是否可以关闭 compat：{'可以，但必须构建验证并自动化验证' if can_close else '暂不建议'}",
        "- 关闭 compat 后 Root / Release 是否一致：需运行 Module Factory Build 后确认",
        "",
        "## 未迁移规则",
        "",
    ]
    lines += [f"- `{line}`" for line in pending_rules[:200]] or ["- 无"]
    if len(pending_rules) > 200:
        lines.append(f"- 其余 {len(pending_rules) - 200} 条省略")
    lines += ["", "## 未迁移脚本", ""]
    lines += [f"- `{name}`" for name in pending_scripts] or ["- 无"]
    lines += [
        "",
        "## 风险说明",
        "",
        "- 本脚本只生成报告，不直接修改 profile。",
        "- 关闭 compat 前必须确认 Root 与 Release 一致，并自动化验证 Spotify、YouTube、知乎、登录、支付和验证码。",
        "- 远程 RULE-SET / DOMAIN-SET 如果已存在于 Rewrite/Remotes/sources.json，会被视为已迁移。",
        "- 如果仍存在未迁移项，应先迁移到 Rules/*.list、Scripts/*.conf 或 Rewrite/Remotes/sources.json，再考虑关闭 compat。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Compatibility migration report written to {REPORT}")


if __name__ == "__main__":
    main()
