#!/usr/bin/env python3
"""Check whether governance reports are newer than their source inputs."""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "report_freshness_report.md"

CHECKS = [
    {
        "report": "reports/app_source_validation_report.md",
        "inputs": ["Rewrite/Sources/Apps", "scripts/validate_app_sources.py", "scripts/sync_upstream_app_modules.py"],
        "blocking": True,
        "reason": "App 源或上游转换逻辑变更后必须重新验证每个独立模块的语法。",
    },
    {
        "report": "reports/profile_validation_report.md",
        "inputs": ["Rewrite/Profiles", "Rules", "Scripts", "scripts/build_module.py", "scripts/validate_profiles.py"],
        "blocking": True,
        "reason": "Profile、规则、脚本或构建逻辑变更后必须重新验证 Fusion 构建。",
    },
    {
        "report": "reports/repository_health_report.md",
        "inputs": ["README.md", "SECURITY.md", "docs", "scripts", "tools", "tests", "Rewrite", "Rules", "Scripts", ".github/workflows"],
        "blocking": True,
        "self_refresh": True,
        "reason": "仓库治理、工作流或模块源头变更后必须刷新健康报告。",
    },
    {
        "report": "reports/automated_quality_evidence.md",
        "inputs": ["scripts", "tools", "tests", "Rewrite", "Rules", "Scripts", ".github/workflows"],
        "blocking": True,
        "self_refresh": True,
        "reason": "自动化证据报告必须反映当前构建、校验和质量门禁。",
    },
    {
        "report": "reports/automation_status_report.md",
        "inputs": ["scripts/check_automation_status.py", ".github/workflows"],
        "blocking": True,
        "reason": "Automation status report must reflect the current workflow set and watchdog policy.",
    },
    {
        "report": "reports/automation_gap_report.md",
        "inputs": [
            "tools/generate_automation_gap_report.py",
            "scripts/quality_gate.py",
            "Rewrite/Generator/Generate.conf",
            "Rewrite/Generate.conf",
            ".github/workflows",
            "Android/branches.json",
            "Release/Android/branches.json",
            "Rewrite/Sources/Apps",
            "Release/Modules",
            "Windows/v2rayN",
            "Scripts/generated/fusion-script-bundle.manifest.json",
            "Scripts/generated/fusion-script-bundle.cache.json",
        ],
        "blocking": True,
        "reason": "Automation gap report must reflect current workflow wiring, platform parity, app module coverage, and script aggregation cache state.",
    },
    {
        "report": "reports/candidate_security_score_report.md",
        "inputs": ["Rewrite/Remotes/candidates.json", "scripts/score_candidates.py"],
        "blocking": True,
        "reason": "候选源或评分脚本变更后必须刷新安全评分。",
    },
    {
        "report": "reports/domestic_app_connectivity_audit.md",
        "inputs": ["Rules/reject.list", "Rules/direct.list", "Scripts/app-cleaner-active.conf", "Scripts/app-cleaner.js", "scripts/audit_domestic_app_connectivity.py"],
        "blocking": True,
        "reason": "国内 App 联网风险相关源头变更后必须刷新审计报告。",
    },
    {
        "report": "reports/reject_risk_report.md",
        "inputs": ["Rules/reject.list", "Rules/direct.list", "scripts/audit_reject_risk.py"],
        "blocking": True,
        "reason": "REJECT 或 DIRECT 变更后必须刷新误伤风险分类。",
    },
    {
        "report": "reports/app_status_matrix.md",
        "inputs": ["Rules", "Scripts", "Rewrite/Sources", "Rewrite/Profiles", "scripts/generate_app_status_matrix.py"],
        "blocking": True,
        "reason": "覆盖源头或状态矩阵生成逻辑变更后必须刷新 App 状态矩阵。",
    },
    {
        "report": "reports/script_aggregation_validation_report.md",
        "inputs": ["Scripts/generated/fusion-script-bundle.js", "Scripts/generated/fusion-script-bundle.manifest.json", "Scripts/generated/fusion-script-bundle.cache.json", "tools/validate_script_aggregation.py"],
        "blocking": True,
        "reason": "Script aggregation manifest and bundle changes must be validated.",
    },
    {
        "report": "reports/script_bundle_sandbox_report.md",
        "inputs": ["Scripts/generated/fusion-script-bundle.js", "Scripts/generated/fusion-script-bundle.manifest.json", "Scripts/generated/fusion-script-bundle.cache.json", "tools/test_script_bundle_sandbox.py"],
        "blocking": True,
        "reason": "Script bundle runtime sandbox coverage must match the generated bundle.",
    },
    {
        "report": "reports/upstream_risk_gate_report.md",
        "inputs": ["Rewrite/Remotes/app-modules.json", "Rewrite/Sources/Apps", "tools/validate_upstream_risk_gate.py"],
        "blocking": True,
        "reason": "Enabled direct-commit upstream app modules must pass the risk gate.",
    },
    {
        "report": "reports/mitm_scope_report.md",
        "inputs": ["Release/Ronghemokuai.sgmodule", "tools/generate_mitm_scope_report.py"],
        "blocking": True,
        "reason": "MITM scope report must reflect the current generated module.",
    },
    {
        "report": "reports/mitm_optimization_report.md",
        "inputs": [
            "Release/Ronghemokuai.sgmodule",
            "reports/mitm_optimization_report.json",
            "scripts/build_module.py",
            "tools/build_mitm_baseline.py",
            "tools/validate_mitm_coverage.py",
        ],
        "blocking": True,
        "reason": "MITM optimization report must reflect the current generated Fusion MITM output and compiler contract.",
    },
    {
        "report": "reports/mitm_reject_risk_ledger.md",
        "inputs": [
            "Rules",
            "Rewrite/Sources",
            "Scripts",
            "Rewrite/Profiles",
            "tools/generate_mitm_reject_risk_ledger.py",
        ],
        "blocking": True,
        "reason": "MITM / REJECT 风险台账必须反映当前源文件范围，并且只能标记风险、不直接改规则。",
    },
    {
        "report": "reports/upstream_provenance_report.md",
        "inputs": [
            "Rewrite/Remotes/app-modules.json",
            "Rewrite/Remotes/sources.json",
            "Rewrite/Sources/Apps",
            "tools/generate_upstream_provenance_report.py",
        ],
        "blocking": True,
        "reason": "上游来源、可信分层和许可台账必须反映当前直接同步配置。",
    },
    {
        "report": "reports/platform_compatibility_matrix.md",
        "inputs": [
            "Ronghemokuai.sgmodule",
            "Release",
            "Android",
            "Windows",
            "tools/generate_platform_compatibility_matrix.py",
        ],
        "blocking": True,
        "reason": "平台兼容矩阵必须反映当前 iOS、Android、Windows 输出边界。",
    },
    {
        "report": "reports/protected_traffic_ledger.md",
        "inputs": [
            "Rules/direct.list",
            "Rules/protect-login.list",
            "Rules/protect-payment.list",
            "Rules/protect-video.list",
            "Rules/protect-cdn.list",
            "Rewrite/Sources/Misc",
            "tools/generate_protected_traffic_ledger.py",
        ],
        "blocking": True,
        "reason": "登录、支付、银行、视频、CDN 和 HTTPDNS 保护链路台账必须保持新鲜。",
    },
    {
        "report": "reports/false_positive_review_report.md",
        "inputs": [
            "reports/mitm_reject_risk_ledger.md",
            "reports/reject_risk_report.md",
            "reports/protected_traffic_ledger.md",
            "tools/generate_false_positive_review_report.py",
        ],
        "blocking": True,
        "reason": "误伤复核队列必须基于最新风险台账和保护链路台账。",
    },
    {
        "report": "reports/rule_overlap_report.md",
        "inputs": ["Rules", "tools/generate_rule_overlap_report.py"],
        "blocking": False,
        "reason": "Source-level rule overlap report should reflect current rule files.",
    },
    {
        "report": "reports/app_cleaner_active_report.md",
        "inputs": ["Scripts/app-cleaner.js", "Scripts/app-cleaner-active.conf", "Scripts/app-cleaner.config.json", "tools/generate_app_cleaner_active_report.py"],
        "blocking": False,
        "reason": "app-cleaner active 入口或融合逻辑变更后建议刷新说明。",
    },
]


def latest_mtime(path: Path) -> float:
    if not path.exists():
        return 0.0
    if path.is_file():
        return path.stat().st_mtime
    latest = path.stat().st_mtime
    for item in path.rglob("*"):
        if item.is_file() and "__pycache__" not in item.parts and ".git" not in item.parts:
            latest = max(latest, item.stat().st_mtime)
    return latest


def fmt(value: float) -> str:
    if value <= 0:
        return "缺失"
    return dt.datetime.fromtimestamp(value, dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")


def evaluate(check: dict) -> dict[str, object]:
    report = ROOT / str(check["report"])
    report_time = latest_mtime(report)
    input_time = max((latest_mtime(ROOT / str(item)) for item in check["inputs"]), default=0.0)
    exists = report.exists()
    stale = not exists or report_time < input_time
    status = "missing" if not exists else "stale" if stale else "fresh"
    return {
        "report": str(check["report"]),
        "status": status,
        "blocking": bool(check.get("blocking", False)),
        "self_refresh": bool(check.get("self_refresh", False)),
        "report_time": fmt(report_time),
        "input_time": fmt(input_time),
        "reason": str(check["reason"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="exit non-zero if a blocking report is stale or missing")
    args = parser.parse_args()

    rows = [evaluate(check) for check in CHECKS]
    blocking_stale = [row for row in rows if row["blocking"] and row["status"] in {"missing", "stale"} and not row["self_refresh"]]
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")

    lines = [
        "# 报告新鲜度检查报告",
        "",
        f"生成时间：{now}",
        "",
        "本报告检查治理报告是否落后于对应源文件。关键报告 stale 时应视为阻断项；自刷新报告会在质量门禁末尾再生成一次。",
        "",
        "## 总览",
        "",
        f"- 检查项：{len(rows)}",
        f"- fresh：{len([row for row in rows if row['status'] == 'fresh'])}",
        f"- stale / missing：{len([row for row in rows if row['status'] in {'stale', 'missing'}])}",
        f"- blocking stale / missing：{len(blocking_stale)}",
        "",
        "## 明细",
        "",
        "| 报告 | 状态 | 是否阻断 | 报告时间 | 输入最新时间 | 原因 |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        block_label = "是" if row["blocking"] else "否"
        if row["self_refresh"] and row["status"] == "stale":
            block_label = "自刷新报告，质量门禁末尾复查"
        lines.append(f"| `{row['report']}` | {row['status']} | {block_label} | {row['report_time']} | {row['input_time']} | {row['reason']} |")
    lines += [
        "",
        "## 处理规则",
        "",
        "- `fresh`：报告不早于输入文件。",
        "- `stale`：报告落后于输入文件，应重新运行对应生成脚本。",
        "- `missing`：报告缺失，应补齐。",
        "- `repository_health_report.md` 与 `automated_quality_evidence.md` 属于自刷新报告，质量门禁运行后应再次刷新。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Report freshness report written to {REPORT}")
    if args.strict and blocking_stale:
        raise SystemExit("Blocking stale governance reports: " + ", ".join(str(row["report"]) for row in blocking_stale))


if __name__ == "__main__":
    main()
