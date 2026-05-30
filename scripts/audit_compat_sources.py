#!/usr/bin/env python3
"""Audit compatibility source fragments before disabling compat layers."""

from __future__ import annotations

import configparser
import datetime as dt
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "Rewrite" / "Profiles" / "stable.conf"
RULE_COMPAT = ROOT / "Rewrite" / "Sources" / "Rule.conf"
SCRIPT_COMPAT = ROOT / "Rewrite" / "Sources" / "Script.conf"
REPORT = ROOT / "reports" / "compat_migration_report.md"
SCRIPT_NAME_RE = re.compile(r"^\s*([^#\s][^=]+?)\s*=")


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


def main() -> None:
    source_rule_compat, source_script_compat = profile_flags()
    rule_lines = active_lines(read(RULE_COMPAT))
    script_lines = active_lines(read(SCRIPT_COMPAT))

    rules_text = "\n".join(read(path) for path in (ROOT / "Rules").glob("*.list"))
    scripts_text = "\n".join(read(path) for path in (ROOT / "Scripts").glob("*.conf"))
    migrated_rules = [line for line in rule_lines if line in rules_text]
    pending_rules = [line for line in rule_lines if line not in rules_text]

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
        f"- 建议下一步是否可以关闭 compat：{'可以，但仍建议人工抽样测试' if can_close else '暂不建议'}",
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
        "- 本脚本只生成报告，不关闭 compat。",
        "- 关闭 compat 前必须确认 Root 与 Release 一致，并手动测试 Spotify、YouTube、知乎、登录、支付和验证码。",
        "- 如果仍存在未迁移项，应先迁移到 Rules/*.list 或 Scripts/*.conf，再考虑关闭 compat。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Compatibility migration report written to {REPORT}")


if __name__ == "__main__":
    main()
