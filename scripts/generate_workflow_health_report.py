#!/usr/bin/env python3
"""Generate workflow health report with optional GitHub Actions run status."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "workflow_health_report.md"
DEFAULT_REPOSITORY = "GrandpaNiuu/GrandpaNiu"
API_ROOT = "https://api.github.com"

WORKFLOWS = [
    ("Module Factory Build", ".github/workflows/module-factory-build.yml", "构建 Release 并同步 Root"),
    ("Daily Module Update", ".github/workflows/daily-module-update.yml", "每日日期、结构、链接和验证检查"),
    ("Daily invalid source audit and repair", ".github/workflows/daily-invalid-source-repair.yml", "连续失效源审计和安全处理"),
    ("Upstream candidate collect", ".github/workflows/upstream-collect.yml", "每周可信候选源收集"),
    ("Repository Health Check", ".github/workflows/repository-health.yml", "仓库治理健康检查"),
    ("Stable Plus Promotion PR", ".github/workflows/stable-plus-promotion-pr.yml", "单项 App 晋级审查 PR 入口"),
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def triggers(text: str) -> str:
    items: list[str] = []
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
        return "必要标记、远程链接、validate_repository.py 输出"
    if "invalid-source" in path:
        return "GitHub 网络、history 计数、误判 404"
    if "upstream" in path:
        return "candidates.json、风险词、重复源、trusted_repositories"
    if "repository-health" in path:
        return "治理文件、README 链接、重复脚本、重复 MITM、报告新鲜度"
    if "promotion" in path:
        return "manual_test_log.md、单项 App 范围、PR 是否为 draft"
    return "待确认"


def github_json(path: str) -> tuple[dict[str, Any] | None, str]:
    request = urllib.request.Request(
        f"{API_ROOT}{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "GrandpaNiu-workflow-health",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return json.loads(response.read().decode("utf-8")), ""
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:200]
        return None, f"HTTP {exc.code}: {detail}"
    except OSError as exc:
        return None, f"{type(exc).__name__}: {exc}"


def latest_run(workflow_path: str, repository: str) -> tuple[dict[str, str], str]:
    workflow_file = workflow_path.rsplit("/", 1)[-1]
    data, error = github_json(f"/repos/{repository}/actions/workflows/{workflow_file}/runs?per_page=1")
    if error:
        return {}, error
    runs = data.get("workflow_runs", []) if isinstance(data, dict) else []
    if not runs:
        return {}, "未找到运行记录"
    run = runs[0]
    return {
        "created_at": str(run.get("created_at") or ""),
        "status": str(run.get("status") or "unknown"),
        "conclusion": str(run.get("conclusion") or "pending"),
        "url": str(run.get("html_url") or ""),
    }, ""


def conclusion_advice(status: str, conclusion: str, fallback: str) -> str:
    if fallback:
        return f"无法确认：{fallback}"
    if status != "completed":
        return "运行中或未完成，等待完成后复查"
    if conclusion == "success":
        return "通过"
    if conclusion in {"failure", "cancelled", "timed_out", "action_required"}:
        return "打开 run 日志，优先排查失败步骤"
    return "状态未知，人工复核"


def main() -> None:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    repository = os.environ.get("GITHUB_REPOSITORY", DEFAULT_REPOSITORY).strip() or DEFAULT_REPOSITORY

    lines = [
        "# Workflow 健康报告",
        "",
        f"生成时间：{now}",
        "",
        "本报告用于确认 workflow 文件是否存在，并尽量读取 GitHub Actions 最近运行状态。若 API 不可用，则只报告配置存在性，不伪造成功状态。",
        "",
        f"- Repository：`{repository}`",
        "",
        "| Workflow | 文件 | 用途 | 触发方式 | 最近运行时间 | Status | Conclusion | Run URL | 处理建议 |",
        "|---|---|---|---|---|---|---|---|---|",
    ]

    for name, rel, purpose in WORKFLOWS:
        text = read(ROOT / rel)
        if not text:
            lines.append(f"| {name} | `{rel}` | {purpose} | 缺失 | 缺失 | missing | missing | - | 补齐 workflow 文件 |")
            continue
        run_info, error = latest_run(rel, repository)
        status = run_info.get("status", "unconfirmed")
        conclusion = run_info.get("conclusion", "unconfirmed")
        created_at = run_info.get("created_at", "无法确认")
        url = run_info.get("url", "-")
        url_cell = f"[open]({url})" if url.startswith("https://") else "-"
        advice = conclusion_advice(status, conclusion, error) if run_info else f"配置存在；{priority(rel)}；需要 Actions 页面确认"
        lines.append(f"| {name} | `{rel}` | {purpose} | {triggers(text)} | {created_at} | {status} | {conclusion} | {url_cell} | {advice} |")

    lines += [
        "",
        "## 说明",
        "",
        "- `success` 才能视为 workflow 最近一次运行通过。",
        "- `failure`、`cancelled`、`timed_out`、`action_required` 必须打开对应 run 日志排查。",
        "- API 不可用时，本报告只确认配置存在，不确认真实运行状态。",
        "- Promotion PR 只允许单项 App 审查，不自动合并，不整体合并 Stable Plus。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Workflow health report written to {REPORT}")


if __name__ == "__main__":
    main()
