#!/usr/bin/env python3
"""Validate governance additions that protect releases from red-cross and false-positive regressions.

The check verifies that required governance files and core policy concepts exist.
It intentionally avoids depending on one exact Chinese sentence when several
semantically equivalent policy phrases are acceptable.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "scripts/validate_remote_rule_syntax.py",
    "scripts/convert_quanx_rules.py",
    "reports/manual_test_log.md",
    ".github/ISSUE_TEMPLATE/rule_false_positive.yml",
    ".github/ISSUE_TEMPLATE/import_red_cross.yml",
    "docs/QUALITY_GATE.md",
    "docs/PROFILE_POLICY.md",
]

MANUAL_TEST_REQUIRED_TOKENS = [
    "标准测试记录模板",
    "是否与 Lite 对照",
    "是否关闭模块对照",
    "Shadowrocket 日志关键命中",
    "Full 排查记录",
    "失败 / 误伤记录",
    "不允许 Full 整体合并进 Stable",
]

QUALITY_GATE_REQUIRED_TOKENS = [
    "validate_remote_rule_syntax.py",
    "convert_quanx_rules.py",
    "远程规则语法门禁",
    "Full 冻结边界",
    "Quantumult X",
    "host-suffix",
]

QUALITY_GATE_REQUIRED_ANY = [
    ["不允许发布模块", "不应发布主模块", "不允许发布主模块", "阻断发布"],
]

PROFILE_POLICY_REQUIRED_TOKENS = [
    "Full 冻结规则",
    "不允许从 full 批量直接进入 stable",
    "不允许把 `host`、`host-suffix`、`host-keyword`、`ip6-cidr` 直接作为 Shadowrocket `RULE-SET`",
    "reports/manual_test_log.md",
    "Lite 对照结果",
]

FALSE_POSITIVE_TEMPLATE_REQUIRED_TOKENS = [
    "使用的模块版本",
    "切换 Lite 后是否正常",
    "关闭模块后是否正常",
    "是否已更新模块、脚本、全部资源",
    "Shadowrocket / Surge 日志关键命中",
]

IMPORT_TEMPLATE_REQUIRED_TOKENS = [
    "导入失败 / 红叉",
    "模块链接",
    "浏览器能否打开模块链接",
    "客户端错误提示",
    "哪些远程规则显示红叉",
]

WORKFLOW_REQUIRED_TOKENS = [
    "scripts/validate_remote_rule_syntax.py",
    "scripts/validate_governance_extensions.py",
    "python3 scripts/convert_quanx_rules.py",
    "python3 scripts/validate_remote_rule_syntax.py",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.exists():
        fail(f"missing required governance file: {relative}")
    return path.read_text(encoding="utf-8", errors="replace")


def require_tokens(relative: str, tokens: list[str]) -> None:
    text = read(relative)
    missing = [token for token in tokens if token not in text]
    if missing:
        fail(f"{relative} missing required governance tokens: " + ", ".join(missing))


def require_any(relative: str, groups: list[list[str]]) -> None:
    text = read(relative)
    missing_groups: list[str] = []
    for group in groups:
        if not any(token in text for token in group):
            missing_groups.append(" / ".join(group))
    if missing_groups:
        fail(f"{relative} missing required governance concept(s): " + ", ".join(missing_groups))


def main() -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            fail(f"missing required governance file: {relative}")

    require_tokens("reports/manual_test_log.md", MANUAL_TEST_REQUIRED_TOKENS)
    require_tokens("docs/QUALITY_GATE.md", QUALITY_GATE_REQUIRED_TOKENS)
    require_any("docs/QUALITY_GATE.md", QUALITY_GATE_REQUIRED_ANY)
    require_tokens("docs/PROFILE_POLICY.md", PROFILE_POLICY_REQUIRED_TOKENS)
    require_tokens(".github/ISSUE_TEMPLATE/rule_false_positive.yml", FALSE_POSITIVE_TEMPLATE_REQUIRED_TOKENS)
    require_tokens(".github/ISSUE_TEMPLATE/import_red_cross.yml", IMPORT_TEMPLATE_REQUIRED_TOKENS)
    require_tokens(".github/workflows/module-factory-build.yml", WORKFLOW_REQUIRED_TOKENS)

    daily = read(".github/workflows/daily-module-update.yml")
    for token in ("validate_remote_rule_syntax.py", "convert_quanx_rules.py"):
        if token not in daily:
            fail(f"daily-module-update.yml missing governance token: {token}")

    print("Governance extension validation passed.")


if __name__ == "__main__":
    main()
