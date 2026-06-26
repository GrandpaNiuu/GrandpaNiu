#!/usr/bin/env python3
"""Generate the automated quality evidence report.

GrandpaNiu releases are governed by reproducible automation rather than
operator-entered device-test logs. This report is the durable summary of the
commands and generated reports that make a release auditable.
"""

from __future__ import annotations

import datetime as dt
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "automated_quality_evidence.md"
MODULE = ROOT / "Ronghemokuai.sgmodule"
RELEASE = ROOT / "Release" / "Ronghemokuai.sgmodule"

EVIDENCE_FILES = [
    "reports/android_rules_report.md",
    "reports/module_integrity_report.md",
    "reports/app_source_validation_report.md",
    "reports/multi_release_report.md",
    "reports/profile_validation_report.md",
    "reports/remote_rule_syntax_report.md",
    "reports/repository_health_report.md",
    "reports/report_freshness_report.md",
    "reports/app_coverage_matrix.md",
    "reports/app_status_matrix.md",
    "reports/script_inventory_report.md",
    "reports/script_aggregation_report.md",
    "reports/script_aggregation_validation_report.md",
    "reports/script_bundle_sandbox_report.md",
    "reports/upstream_risk_gate_report.md",
    "reports/mitm_scope_report.md",
    "reports/rule_overlap_report.md",
    "reports/app_cleaner_active_report.md",
    "reports/candidate_security_score_report.md",
    "reports/reject_risk_report.md",
    "reports/domestic_app_connectivity_audit.md",
    "reports/automation_status_report.md",
]

QUALITY_COMMANDS = [
    "python -m py_compile scripts/*.py Rewrite/Generator/Builder.py tools/*.py",
    "node --check Scripts/app-cleaner.js",
    "python -m unittest discover -s tests",
    "python scripts/convert_quanx_rules.py",
    "python Rewrite/Generator/Builder.py --profile fusion --release",
    "python scripts/validate_app_sources.py",
    "python scripts/android_format_check.py",
    "node --check Scripts/generated/fusion-script-bundle.js",
    "python tools/validate_script_aggregation.py",
    "python tools/test_script_bundle_sandbox.py",
    "python tools/validate_upstream_risk_gate.py",
    "python scripts/validate_generator_config.py",
    "python scripts/validate_manifest.py",
    "python scripts/validate_remote_rule_syntax.py",
    "python scripts/validate_governance_extensions.py",
    "python scripts/validate_profiles.py",
    "python scripts/validate_module_integrity.py",
    "python tools/generate_mitm_scope_report.py",
    "python tools/generate_rule_overlap_report.py",
    "python tools/generate_app_cleaner_active_report.py",
    "python scripts/repository_health_check.py",
    "python scripts/check_automation_status.py",
    "python tools/generate_automated_quality_evidence.py",
    "python scripts/validate_repository.py",
]

TEXT_SUFFIXES = {
    ".conf",
    ".sgmodule",
    ".module",
    ".list",
    ".py",
    ".js",
    ".json",
    ".md",
    ".yml",
    ".yaml",
    ".html",
    ".txt",
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def git_value(*args: str) -> str:
    try:
        proc = subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True, check=True)
        return proc.stdout.strip() or "unavailable"
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def tracked_text_files() -> list[Path]:
    try:
        proc = subprocess.run(["git", "ls-files"], cwd=ROOT, text=True, capture_output=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return []
    result: list[Path] = []
    for raw in proc.stdout.splitlines():
        path = ROOT / raw
        if path.exists() and (path.suffix.lower() in TEXT_SUFFIXES or path.name in {"LICENSE", "README.md", "CONTRIBUTING.md"}):
            result.append(path)
    return result


def bom_hits() -> list[str]:
    hits: list[str] = []
    for path in tracked_text_files():
        if b"\xef\xbb\xbf" in path.read_bytes():
            hits.append(rel(path))
    return sorted(hits)


def report_status(path: Path) -> str:
    return "present" if path.exists() and read(path).strip() else "missing"


def main() -> None:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    root_release_identical = MODULE.exists() and RELEASE.exists() and MODULE.read_bytes() == RELEASE.read_bytes()
    boms = bom_hits()
    sha = git_value("rev-parse", "--short", "HEAD")
    branch = git_value("branch", "--show-current")

    lines = [
        "# 自动化质量证据报告",
        "",
        f"生成时间：{now}",
        f"Git 分支：`{branch}`",
        f"Git 提交：`{sha}`",
        "",
        "本仓库发布门禁以可重复执行的自动化证据为准：构建、语法检查、远程规则校验、模块完整性、报告新鲜度和仓库健康检查。",
        "",
        "## 核心结论",
        "",
        f"- Root / Release 一致：{'是' if root_release_identical else '否'}",
        f"- UTF-8 BOM 命中：{len(boms)}",
        f"- 证据报告数量：{len(EVIDENCE_FILES)}",
        "",
        "## 必跑自动化命令",
        "",
    ]
    lines.extend(f"- `{command}`" for command in QUALITY_COMMANDS)
    lines += [
        "",
        "## 证据文件状态",
        "",
        "| 文件 | 状态 |",
        "|---|---|",
    ]
    for item in EVIDENCE_FILES:
        lines.append(f"| `{item}` | {report_status(ROOT / item)} |")
    lines += ["", "## BOM 扫描", ""]
    if boms:
        lines.extend(f"- `{item}`" for item in boms)
    else:
        lines.append("- 未发现 UTF-8 BOM。")
    lines += [
        "",
        "## 发布策略",
        "",
        "- 自动化门禁失败时不得发布主模块。",
        "- 静态覆盖不写成已验证通过；它只表示规则、脚本或 MITM 层存在命中。",
        "- 用户反馈可以作为 Issue 输入，但不是发布阻断门禁。",
        "- 高风险改动必须保留来源、风险、回滚路径，并通过自动化质量门禁。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Automated quality evidence written to {REPORT}")


if __name__ == "__main__":
    main()
