#!/usr/bin/env python3
"""Generate a static workflow health checklist report."""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "workflow_health_report.md"

WORKFLOWS = [
    ("Module Factory Build", ".github/workflows/module-factory-build.yml", "构建 Release 并同步 Root"),
    ("Daily Module Update", ".github/workflows/daily-module-update.yml", "每日日期、结构、链接和验证检查"),
    ("Daily invalid source audit and repair", ".github/workflows/daily-invalid-source-repair.yml", "连续失效源审计和安全处理"),
    ("Upstream candidate collect", ".github/workflows/upstream-collect.yml", "每周可信候选源收集"),
    ("Repository Health Check", ".github/workflows/repository-health.yml", "仓库治理健康检查"),
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def triggers(text: str) -> str:
    items = []
    if "workflow_dispatch" in text:
        items.append("手动")
    if "schedule:" in text:
        items.append("定时")
    if re.search(r"(?m)^\s*push:", text):
        items.append("push")
    return " / ".join(items) if items else "待确认"


def priority(path: str) -> str:
    if "module-factory" in path:
        return "build_module.py、factory_finalize.py、profile、sources、Root/Release diff"
    if "daily-module" in path:
        return "核心标记、远程链接、validate_repository.py 输出"
    if "invalid-source" in path:
        return "GitHub 网络、history 计数、保护项、误判 404"
    if "upstream" in path:
        return "candidates.json、风险词、重复源、trusted_repositories"
    if "repository-health" in path:
        return "缺失治理文件、README 链接、重复脚本、重复 MITM"
    return "待确认"


def main() -> None:
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# Workflow 健康报告",
        "",
        f"- 生成时间：{today}",
        "- 最近状态：需要在 GitHub Actions 页面确认",
        "",
        "| Workflow | 用途 | 触发方式 | 最近状态 | 失败时优先排查 |",
        "|---|---|---|---|---|",
    ]
    for name, rel, purpose in WORKFLOWS:
        text = read(ROOT / rel)
        exists = "存在" if text else "缺失"
        lines.append(f"| {name} | {purpose} | {triggers(text)} | {exists}，最近状态需在 GitHub Actions 页面确认 | {priority(rel)} |")
    lines += [
        "",
        "## 说明",
        "",
        "- 本报告不调用 GitHub API；如果需要最近运行状态，请打开仓库 Actions 页面确认。",
        "- 所有会写仓库的 workflow 应使用 `permissions: contents: write` 和共享并发组 `module-maintenance`。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Workflow health report written to {REPORT}")


if __name__ == "__main__":
    main()
