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
        "report": "reports/profile_validation_report.md",
        "inputs": ["Rewrite/Profiles", "Rules", "Scripts", "scripts/build_module.py", "scripts/validate_profiles.py"],
        "blocking": True,
        "reason": "Profile、规则、脚本或构建逻辑变更后必须重新验证四版本构建。",
    },
    {
        "report": "reports/repository_health_report.md",
        "inputs": ["README.md", "SECURITY.md", "docs", "scripts", "Rewrite", "Rules", "Scripts", ".github/workflows"],
        "blocking": True,
        "self_refresh": True,
        "reason": "仓库治理、工作流或模块源头变更后必须刷新健康报告。",
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
        "inputs": ["Rules", "Scripts", "Rewrite/Sources", "Rewrite/Profiles", "reports/manual_test_log.md", "scripts/generate_app_status_matrix.py"],
        "blocking": True,
        "reason": "覆盖源头或人工测试记录变更后必须刷新 App 状态矩阵。",
    },
    {
        "report": "reports/manual_test_log.md",
        "inputs": ["Ronghemokuai.sgmodule", "Release", "Scripts", "Rewrite/Sources"],
        "blocking": False,
        "manual": True,
        "reason": "人工测试记录落后时只进入 manual-review，不自动写成通过。",
    },
    {
        "report": "reports/app_cleaner_active_report.md",
        "inputs": ["Scripts/app-cleaner.js", "Scripts/app-cleaner-active.conf", "scripts/dedupe_qq_news_script_path.py"],
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
    if not exists:
        status = "missing"
    elif stale and check.get("manual"):
        status = "manual-review"
    elif stale:
        status = "stale"
    else:
        status = "fresh"
    return {
        "report": str(check["report"]),
        "status": status,
        "blocking": bool(check.get("blocking", False)),
        "manual": bool(check.get("manual", False)),
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
    manual_rows = [row for row in rows if row["status"] == "manual-review"]
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")

    lines = [
        "# 报告新鲜度检查报告",
        "",
        f"生成时间：{now}",
        "",
        "本报告检查治理报告是否落后于对应源文件。关键报告 stale 时应视为阻断项；`manual_test_log.md` 只作为 manual-review，不自动失败。",
        "",
        "## 总览",
        "",
        f"- 检查项：{len(rows)}",
        f"- fresh：{len([row for row in rows if row['status'] == 'fresh'])}",
        f"- stale / missing：{len([row for row in rows if row['status'] in {'stale', 'missing'}])}",
        f"- blocking stale / missing：{len(blocking_stale)}",
        f"- manual-review：{len(manual_rows)}",
        "",
        "## 明细",
        "",
        "| 报告 | 状态 | 是否阻断 | 报告时间 | 输入最新时间 | 原因 |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        block_label = "是" if row["blocking"] else "否"
        if row["self_refresh"] and row["status"] == "stale":
            block_label = "自刷新报告，Repository Health 运行后复查"
        lines.append(f"| `{row['report']}` | {row['status']} | {block_label} | {row['report_time']} | {row['input_time']} | {row['reason']} |")
    lines += [
        "",
        "## 处理规则",
        "",
        "- `fresh`：报告不早于输入文件。",
        "- `stale`：报告落后于输入文件，应重新运行对应生成脚本。",
        "- `missing`：报告缺失，应补齐。",
        "- `manual-review`：人工测试记录落后于模块变更，应确认仍为未测或更新真实测试结果。",
        "- `repository_health_report.md` 属于自刷新报告，健康检查运行后应再次刷新本报告。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Report freshness report written to {REPORT}")
    if args.strict and blocking_stale:
        raise SystemExit("Blocking stale governance reports: " + ", ".join(str(row["report"]) for row in blocking_stale))


if __name__ == "__main__":
    main()
