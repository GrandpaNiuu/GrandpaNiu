#!/usr/bin/env python3
"""Check whether governance reports are newer than their source inputs.

This script is report-only by default. It writes reports/report_freshness_report.md
and exits with success unless --strict is passed. Repository Health Check can use
this output to surface stale reports without blocking normal maintenance runs.
"""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "report_freshness_report.md"

CHECKS = [
    {
        "report": "reports/profile_validation_report.md",
        "inputs": ["Rewrite/Profiles", "Scripts", "scripts/build_module.py", "scripts/validate_profiles.py"],
        "reason": "Profile、脚本或构建逻辑变更后必须重新验证四版本构建。",
    },
    {
        "report": "reports/script_inventory_report.md",
        "inputs": ["Scripts", "scripts/generate_script_inventory_report.py"],
        "reason": "Scripts 入口或脚本清单生成逻辑变更后必须刷新脚本清单。",
    },
    {
        "report": "reports/repository_health_report.md",
        "inputs": ["README.md", "docs", "scripts", "Rewrite", "Rules", "Scripts", ".github/workflows"],
        "reason": "仓库治理、工作流或模块源头变更后必须刷新健康报告。",
    },
    {
        "report": "reports/app_cleaner_active_report.md",
        "inputs": ["Scripts/app-cleaner.js", "Scripts/app-cleaner-active.conf", "scripts/dedupe_qq_news_script_path.py"],
        "reason": "app-cleaner 主脚本、active 入口或迁移脚本变更后必须刷新融合说明。",
    },
    {
        "report": "reports/app_cleaner_refactor_report.md",
        "inputs": ["Scripts/app-cleaner.js"],
        "reason": "app-cleaner 架构变更后必须刷新重构报告。",
    },
    {
        "report": "reports/candidate_security_score_report.md",
        "inputs": ["Rewrite/Remotes/candidates.json", "scripts/score_candidates.py"],
        "reason": "候选源或评分脚本变更后必须刷新安全评分报告。",
    },
    {
        "report": "reports/manual_test_log.md",
        "inputs": ["Ronghemokuai.sgmodule", "Release", "Scripts", "Rewrite/Sources"],
        "reason": "模块大改后手动测试记录必须明确保持未测或更新真实测试结果。",
        "manual": True,
    },
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def latest_mtime(path: Path) -> float:
    if not path.exists():
        return 0.0
    if path.is_file():
        return path.stat().st_mtime
    latest = path.stat().st_mtime
    for item in path.rglob("*"):
        if item.is_file() and ".git" not in item.parts:
            latest = max(latest, item.stat().st_mtime)
    return latest


def fmt(timestamp: float) -> str:
    if timestamp <= 0:
        return "缺失"
    return dt.datetime.fromtimestamp(timestamp, dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")


def evaluate(check: dict) -> dict[str, str | bool]:
    report_path = ROOT / str(check["report"])
    input_paths = [ROOT / str(item) for item in check["inputs"]]
    report_time = latest_mtime(report_path)
    input_time = max((latest_mtime(path) for path in input_paths), default=0.0)
    exists = report_path.exists()
    stale = not exists or report_time < input_time
    manual = bool(check.get("manual", False))
    status = "fresh"
    if not exists:
        status = "missing"
    elif stale and manual:
        status = "manual-review"
    elif stale:
        status = "stale"
    return {
        "report": str(check["report"]),
        "exists": exists,
        "status": status,
        "report_time": fmt(report_time),
        "input_time": fmt(input_time),
        "reason": str(check["reason"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="exit non-zero if any report is missing or stale")
    args = parser.parse_args()

    rows = [evaluate(check) for check in CHECKS]
    stale_rows = [row for row in rows if row["status"] in {"missing", "stale"}]
    manual_rows = [row for row in rows if row["status"] == "manual-review"]
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")

    lines = [
        "# 报告新鲜度检查报告",
        "",
        f"生成时间：{now}",
        "",
        "本报告检查治理报告是否落后于对应源文件。`manual_test_log.md` 属于人工记录，变更后只提示复核，不自动写成通过。",
        "",
        "## 总体统计",
        "",
        f"- 检查项：{len(rows)}",
        f"- 新鲜：{len([row for row in rows if row['status'] == 'fresh'])}",
        f"- 过期：{len(stale_rows)}",
        f"- 需人工复核：{len(manual_rows)}",
        "",
        "## 明细",
        "",
        "| 报告 | 状态 | 报告时间 | 输入最新时间 | 原因 |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(f"| `{row['report']}` | {row['status']} | {row['report_time']} | {row['input_time']} | {row['reason']} |")
    lines += [
        "",
        "## 处理规则",
        "",
        "- `fresh`：报告不早于输入文件。",
        "- `stale`：报告落后于输入文件，应重新运行对应生成脚本。",
        "- `missing`：报告缺失，应补齐。",
        "- `manual-review`：人工测试记录落后于模块变更，应确认仍为未测试或更新真实测试结果。",
        "",
    ]
    write(REPORT, "\n".join(lines))
    print(f"Report freshness report written to {REPORT}")
    if args.strict and stale_rows:
        raise SystemExit("Stale governance reports: " + ", ".join(str(row["report"]) for row in stale_rows))


if __name__ == "__main__":
    main()
