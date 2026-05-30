#!/usr/bin/env python3
"""Generate workflow health report.

The script tries GitHub API first when GITHUB_TOKEN is available. If runtime has
no API access, it falls back to a static workflow checklist and states that in
the report.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "workflow_health_report.md"
REPO = os.environ.get("GITHUB_REPOSITORY", "GrandpaNiuu/GrandpaNiu")
TOKEN = os.environ.get("GITHUB_TOKEN")

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


def api_json(url: str) -> dict:
    if not TOKEN:
        raise RuntimeError("GITHUB_TOKEN not available")
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {TOKEN}",
            "User-Agent": "GrandpaNiu-Workflow-Health/1.0",
        },
    )
    with urllib.request.urlopen(req, timeout=25) as response:
        return json.loads(response.read().decode("utf-8"))


def latest_run(workflow_path: str) -> dict | None:
    workflow_name = Path(workflow_path).name
    url = f"https://api.github.com/repos/{REPO}/actions/workflows/{workflow_name}/runs?per_page=1&branch=main"
    data = api_json(url)
    runs = data.get("workflow_runs", [])
    return runs[0] if runs else None


def failed_job_summary(run_id: int) -> tuple[str, str]:
    try:
        data = api_json(f"https://api.github.com/repos/{REPO}/actions/runs/{run_id}/jobs?per_page=100")
    except Exception:
        return "待确认", "待确认"
    for job in data.get("jobs", []):
        if job.get("conclusion") not in {None, "success", "skipped"}:
            failed_step = "待确认"
            for step in job.get("steps", []):
                if step.get("conclusion") not in {None, "success", "skipped"}:
                    failed_step = step.get("name", "待确认")
                    break
            return job.get("name", "待确认"), failed_step
    return "无", "无"


def main() -> None:
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    mode = "GitHub API 真实状态模式"
    rows: list[str] = []
    try:
        for name, rel, purpose in WORKFLOWS:
            text = read(ROOT / rel)
            run = latest_run(rel)
            if run:
                status = f"{run.get('status')} / {run.get('conclusion') or 'running'}"
                conclusion = run.get("conclusion") or run.get("status") or "待确认"
                result = "正常" if conclusion == "success" else "需要检查"
                failed_job, failed_step = failed_job_summary(int(run.get("id"))) if conclusion not in {"success", "completed"} else ("无", "无")
                commit = str(run.get("head_sha", ""))[:12] or "待确认"
                time = run.get("updated_at") or run.get("created_at") or "待确认"
                advice = priority(rel)
                rows.append(f"| {name} | {purpose} | {triggers(text)} | {time} | {status} | {result} | {failed_job} | {failed_step} | {commit} | {advice} |")
            else:
                rows.append(f"| {name} | {purpose} | {triggers(text)} | 无运行记录 | 待确认 | 需要检查 | 待确认 | 待确认 | 待确认 | {priority(rel)} |")
    except (RuntimeError, urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        mode = f"静态清单模式：无法自动获取最近状态（{exc}）"
        rows = []
        for name, rel, purpose in WORKFLOWS:
            text = read(ROOT / rel)
            exists = "存在" if text else "缺失"
            rows.append(f"| {name} | {purpose} | {triggers(text)} | 需要在 GitHub Actions 页面确认 | {exists} | 待人工确认 | 待确认 | 待确认 | 待确认 | {priority(rel)} |")

    lines = [
        "# Workflow 健康报告",
        "",
        f"- 生成时间：{today}",
        f"- 状态模式：{mode}",
        "",
        "| Workflow | 用途 | 触发方式 | 最近运行时间 | 最近状态 | 结论 | 失败 Job | 失败 Step | 对应 commit | 失败时优先排查 |",
        "|---|---|---|---|---|---|---|---|---|---|",
        *rows,
        "",
        "## 说明",
        "",
        "- 有 `GITHUB_TOKEN` 时，本报告尝试读取 GitHub Actions 最近运行状态。",
        "- 无法读取 API 时，报告会退回静态清单模式，并要求人工到 Actions 页面确认。",
        "- 所有会写仓库的 workflow 应使用 `permissions: contents: write` 和共享并发组 `module-maintenance`。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Workflow health report written to {REPORT}")


if __name__ == "__main__":
    main()
