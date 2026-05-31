#!/usr/bin/env python3
"""Generate a repository health report for the source-driven module factory."""

from __future__ import annotations

import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "repository_health_report.md"
MODULE = ROOT / "Ronghemokuai.sgmodule"
RELEASE = ROOT / "Release" / "Ronghemokuai.sgmodule"
SOURCES_JSON = ROOT / "Rewrite" / "Remotes" / "sources.json"
CANDIDATES_JSON = ROOT / "Rewrite" / "Remotes" / "candidates.json"
EXPECTED_UPDATE_URL = "#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule"

REQUIRED_FILES = [
    "README.md",
    "Ronghemokuai.sgmodule",
    "Release/Ronghemokuai.sgmodule",
    "Rewrite/Profiles/stable.conf",
    "Rewrite/Profiles/stable-plus.conf",
    "Rewrite/Profiles/lite.conf",
    "Rewrite/Profiles/full.conf",
    "Rewrite/Sources/MITM-core.conf",
    "Rewrite/Sources/MITM-app-clean.conf",
    "Rewrite/Sources/MITM-stable-plus.conf",
    "Rewrite/Sources/MITM-extended.conf",
    "Rewrite/Remotes/sources.json",
    "Rewrite/Remotes/candidates.json",
    "Scripts/spotify.conf",
    "Scripts/youtube.conf",
    "Scripts/app-clean.conf",
    "Scripts/app-cleaner.js",
    "Scripts/app-cleaner-active.conf",
    "Scripts/zhihu-enhance.conf",
    "Scripts/zhihu-enhance.js",
    "Rules/direct.list",
    "Rules/spotify-direct.list",
    "Rules/youtube-direct.list",
    "Rules/reject.list",
    "Rules/app-clean.list",
    "Rules/web-ads.list",
    "docs/FACTORY_FLOW.md",
    "docs/MAINTENANCE.md",
    "docs/TROUBLESHOOTING.md",
    "docs/COVERAGE.md",
    "docs/SCOPE.md",
    "docs/PERFORMANCE.md",
    "docs/QUALITY_GATE.md",
    "docs/RELEASE.md",
    "docs/SCRIPT_REVIEW.md",
    "docs/MITM_POLICY.md",
    "docs/VERSIONING.md",
    "docs/ROADMAP.md",
    "docs/PROFILE_POLICY.md",
    "docs/MODULE_FEATURES.md",
    "docs/AUTOMATION_POLICY.md",
    "SECURITY.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "backup/README.md",
    "backup/manifest.json",
    "requirements.txt",
    ".editorconfig",
    ".gitignore",
]

REQUIRED_WORKFLOWS = [
    ".github/workflows/module-factory-build.yml",
    ".github/workflows/daily-module-update.yml",
    ".github/workflows/daily-invalid-source-repair.yml",
    ".github/workflows/upstream-collect.yml",
    ".github/workflows/repository-health.yml",
]

OPTIONAL_REPORTS = [
    "reports/app_coverage_matrix.md",
    "reports/change_impact_report.md",
    "reports/workflow_health_report.md",
    "reports/profile_validation_report.md",
    "reports/manual_test_log.md",
    "reports/candidate_security_score_report.md",
    "reports/report_freshness_report.md",
    "reports/repository_maturity_review.md",
]

BLOCKING_MARKERS = [
    "[Rule]",
    "[URL Rewrite]",
    "[Header Rewrite]",
    "[Body Rewrite]",
    "[Map Local]",
    "[Script]",
    "[MITM]",
    "spotify-json",
    "spotify-proto",
    "youtube.response",
    "zhihu-enhance",
    EXPECTED_UPDATE_URL,
]

LOCAL_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SCRIPT_NAME_RE = re.compile(r"^\s*([^#\s][^=]+?)\s*=")
HOSTNAME_RE = re.compile(r"^\s*hostname\s*=\s*(.+)$")
PROFILE_USE = {
    "lite": "低耗电参考版，不默认发布",
    "stable": "默认正式版，可以发布",
    "stable-plus": "常用 App 增强测试版，不默认发布",
    "full": "全量排查测试版，不默认发布",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def json_load(path: Path) -> dict:
    try:
        return json.loads(read(path))
    except Exception:
        return {}


def active_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip() and not line.lstrip().startswith("#")]


def collect_script_names() -> tuple[list[str], list[str]]:
    names: list[str] = []
    for path in (ROOT / "Scripts").glob("*.conf"):
        for line in active_lines(read(path)):
            match = SCRIPT_NAME_RE.match(line)
            if match:
                names.append(match.group(1).strip())
    dupes = sorted({name for name in names if names.count(name) > 1})
    return names, dupes


def parse_hosts(text: str) -> list[str]:
    hosts: list[str] = []
    for line in text.splitlines():
        match = HOSTNAME_RE.match(line)
        if not match:
            continue
        value = match.group(1).replace("%APPEND%", "")
        for host in value.split(","):
            clean = host.strip()
            if clean:
                hosts.append(clean)
    return hosts


def collect_mitm_hosts() -> tuple[list[str], list[str]]:
    text = read(MODULE)
    start = text.find("[MITM]")
    if start < 0:
        return [], []
    hosts = parse_hosts(text[start:])
    dupes = sorted({host for host in hosts if hosts.count(host) > 1})
    return hosts, dupes


def readme_missing_links() -> list[str]:
    text = read(ROOT / "README.md")
    missing: list[str] = []
    for match in LOCAL_LINK_RE.finditer(text):
        target = match.group(1).strip()
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        path_part = target.split("#", 1)[0]
        if path_part and not (ROOT / path_part).exists():
            missing.append(target)
    return sorted(set(missing))


def run_validator() -> tuple[bool, str]:
    proc = subprocess.run(
        [sys.executable, "scripts/validate_repository.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    output = (proc.stdout + proc.stderr).strip() or "无输出"
    return proc.returncode == 0, output


def run_js_check() -> tuple[bool, str]:
    proc = subprocess.run(
        ["node", "--check", "Scripts/app-cleaner.js"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    output = (proc.stdout + proc.stderr).strip() or "无输出"
    return proc.returncode == 0, output


def module_section_counts(text: str) -> dict[str, int]:
    sections = ["Rule", "URL Rewrite", "Header Rewrite", "Body Rewrite", "Map Local", "Script", "MITM"]
    counts = {section: 0 for section in sections}
    current = ""
    for line in text.splitlines():
        if line.startswith("[") and line.endswith("]"):
            current = line.strip("[]")
            continue
        if current in counts and line.strip():
            counts[current] += 1
    return counts


def workflow_summary(path: Path) -> str:
    text = read(path)
    status = []
    status.append("contents:write" if "contents: write" in text else "missing-contents-write")
    status.append("concurrency" if "concurrency:" in text else "missing-concurrency")
    if "--profile full" in text:
        status.append("uses-full")
    elif "--profile stable-plus" in text:
        status.append("uses-stable-plus")
    elif "--profile stable" in text:
        status.append("uses-stable")
    if "node --check Scripts/app-cleaner.js" in text:
        status.append("node-check")
    return ", ".join(status)


def profile_summary_rows() -> list[str]:
    rows = []
    for profile, usage in PROFILE_USE.items():
        path = ROOT / "Rewrite" / "Profiles" / f"{profile}.conf"
        text = read(path)
        mitm_sources = []
        in_mitm = False
        for line in text.splitlines():
            stripped = line.strip()
            if stripped == "[mitm]":
                in_mitm = True
                continue
            if stripped.startswith("[") and stripped.endswith("]"):
                in_mitm = False
            if in_mitm and "=" in stripped and not stripped.startswith("#"):
                mitm_sources.append(stripped.split("=", 1)[1].strip())
        rows.append(f"| {profile} | {', '.join(mitm_sources) if mitm_sources else 'legacy MITM.conf'} | {usage} |")
    return rows


def mitm_layer_rows() -> list[str]:
    rows = []
    for rel in [
        "Rewrite/Sources/MITM-core.conf",
        "Rewrite/Sources/MITM-app-clean.conf",
        "Rewrite/Sources/MITM-stable-plus.conf",
        "Rewrite/Sources/MITM-extended.conf",
        "Rewrite/Sources/MITM.conf",
    ]:
        hosts = parse_hosts(read(ROOT / rel)) if (ROOT / rel).exists() else []
        rows.append(f"| `{rel}` | {len(hosts)} |")
    return rows


def list_block(title: str, items: list[str], code: bool = False) -> list[str]:
    lines = ["", f"## {title}", ""]
    if not items:
        lines.append("- 无")
        return lines
    for item in items:
        lines.append(f"- `{item}`" if code else f"- {item}")
    return lines


def main() -> None:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    root_text = read(MODULE)
    release_text = read(RELEASE)
    source_data = json_load(SOURCES_JSON)
    candidate_data = json_load(CANDIDATES_JSON)
    script_names, script_dupes = collect_script_names()
    mitm_hosts, mitm_dupes = collect_mitm_hosts()
    validator_ok, validator_output = run_validator()
    js_ok, js_output = run_js_check()

    missing_files = [rel for rel in REQUIRED_FILES if not (ROOT / rel).exists()]
    missing_workflows = [rel for rel in REQUIRED_WORKFLOWS if not (ROOT / rel).exists()]
    missing_reports = [rel for rel in OPTIONAL_REPORTS if not (ROOT / rel).exists()]
    missing_markers = [marker for marker in BLOCKING_MARKERS if marker not in root_text]
    missing_links = readme_missing_links()
    enabled_sources = [item for item in source_data.get("rule_sets", []) if item.get("enabled")]
    enabled_candidates = [item for item in candidate_data.get("candidates", []) if item.get("enabled") and item.get("activate", False)]
    pending_scripts = [item.get("name", "unnamed") for item in candidate_data.get("candidates", []) if item.get("kind") == "script" and item.get("status") == "pending"]

    history = json_load(ROOT / "reports" / "invalid_sources_history.json")
    failed_sources = [value.get("url", key) for key, value in history.items() if int(value.get("fail_count", 0)) >= 1]
    two_day_failed = [value.get("url", key) for key, value in history.items() if int(value.get("fail_count", 0)) >= 2]

    critical_issues: list[str] = []
    if root_text != release_text:
        critical_issues.append("Root 与 Release 不一致")
    if missing_files:
        critical_issues.append("缺少必要仓库文件")
    if missing_workflows:
        critical_issues.append("缺少必要工作流")
    if missing_markers:
        critical_issues.append("主模块缺少关键标记")
    if script_dupes:
        critical_issues.append("存在重复脚本名")
    if mitm_dupes:
        critical_issues.append("存在重复 MITM hostname")
    if missing_links:
        critical_issues.append("README 存在失效本地链接")
    if not validator_ok:
        critical_issues.append("统一验证脚本未通过")
    if not js_ok:
        critical_issues.append("app-cleaner JavaScript 语法检查未通过")

    warnings: list[str] = []
    if missing_reports:
        warnings.append("部分可选治理报告尚未生成，首次运行报告生成器后会补齐")
    if not pending_scripts:
        warnings.append("当前没有 pending 脚本候选，请确认脚本自动收集仍保持关闭")
    if len(enabled_sources) > 20:
        warnings.append("启用远程源较多，需要持续观察误杀与性能")
    if failed_sources:
        warnings.append(f"当前存在失效源历史记录：{len(failed_sources)} 条")
    if two_day_failed:
        warnings.append(f"存在连续失败 2 天及以上的源：{len(two_day_failed)} 条，应确认是否已禁用或替代")

    workflow_items = [f"{rel}: {workflow_summary(ROOT / rel)}" for rel in REQUIRED_WORKFLOWS if (ROOT / rel).exists()]

    lines: list[str] = [
        "# 仓库健康检查报告",
        "",
        f"生成时间：{now}",
        "",
        "## 总体状态",
        "",
        f"- 阻断问题：{len(critical_issues)}",
        f"- 提醒事项：{len(warnings)}",
        f"- 统一验证：{'通过' if validator_ok else '失败'}",
        f"- app-cleaner JS 语法：{'通过' if js_ok else '失败'}",
        f"- Root 与 Release 一致：{'是' if root_text == release_text else '否'}",
        f"- 启用远程规则源：{len(enabled_sources)}",
        f"- 启用候选源：{len(enabled_candidates)}",
        f"- pending 脚本候选：{len(pending_scripts)}",
        f"- 脚本总数：{len(script_names)}",
        f"- stable 当前 MITM hostname 数量：{len(mitm_hosts)}",
        "- 默认发布策略：stable only；stable-plus / full 不默认发布",
        "",
        "## 模块区块行数",
        "",
    ]
    lines += [f"- {name}: {count}" for name, count in module_section_counts(root_text).items()]
    lines += [
        "",
        "## Profile 策略摘要",
        "",
        "| Profile | MITM 输入 | 用途 |",
        "|---|---|---|",
        *profile_summary_rows(),
        "",
        "## MITM 分层数量",
        "",
        "| 文件 | hostname 数量 |",
        "|---|---:|",
        *mitm_layer_rows(),
    ]

    lines += list_block("阻断问题", critical_issues)
    lines += list_block("提醒事项", warnings)
    lines += list_block("缺少必要文件", missing_files, code=True)
    lines += list_block("缺少工作流", missing_workflows, code=True)
    lines += list_block("未生成的可选报告", missing_reports, code=True)
    lines += list_block("主模块缺少关键标记", missing_markers, code=True)
    lines += list_block("重复脚本名", script_dupes, code=True)
    lines += list_block("重复 MITM hostname", mitm_dupes, code=True)
    lines += list_block("README 失效本地链接", missing_links, code=True)
    lines += list_block("Workflow 摘要", workflow_items)
    lines += list_block("Pending 脚本候选", pending_scripts)
    lines += list_block("失效源历史记录", failed_sources, code=True)
    lines += [
        "",
        "## app-cleaner JS 语法输出",
        "",
        "```text",
        js_output,
        "```",
        "",
        "## 统一验证输出",
        "",
        "```text",
        validator_output,
        "```",
        "",
        "## 后续维护建议",
        "",
        "1. 日常修改应优先编辑 Rules、Scripts、Rewrite/Sources、Rewrite/Remotes 和 Rewrite/Profiles。",
        "2. Root 模块只作为生成结果，必须通过 build_module.py 与 factory_finalize.py 同步。",
        "3. 新脚本默认 pending，不直接进入 stable。",
        "4. MITM 从 extended 进入 stable 前，应先进入 stable-plus 并完成真实测试。",
        "5. 出现登录、支付、验证码异常时，优先回查 MITM、Body Rewrite 和 Map Local。",
        "6. 远程源连续失败 2 天后才进入处理流程，单日网络失败只报告观察。",
        "7. 候选源必须先经过 candidate_security_score_report.md 评分，再进入测试或晋级流程。",
        "8. 重要报告应通过 report_freshness_report.md 确认没有落后于源文件。",
        "",
    ]

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Repository health report written to {REPORT}")
    if critical_issues:
        raise SystemExit("Repository health check found blocking issues: " + "; ".join(critical_issues))


if __name__ == "__main__":
    main()
