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
    "Rewrite/Profiles/lite.conf",
    "Rewrite/Profiles/full.conf",
    "Rewrite/Remotes/sources.json",
    "Rewrite/Remotes/candidates.json",
    "Scripts/spotify.conf",
    "Scripts/youtube.conf",
    "Scripts/app-clean.conf",
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


def collect_mitm_hosts() -> tuple[list[str], list[str]]:
    text = read(MODULE)
    start = text.find("[MITM]")
    if start < 0:
        return [], []
    hosts: list[str] = []
    for line in text[start:].splitlines():
        match = HOSTNAME_RE.match(line)
        if not match:
            continue
        for host in match.group(1).split(","):
            clean = host.strip()
            if clean and clean != "%APPEND%":
                hosts.append(clean)
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
    elif "--profile stable" in text:
        status.append("uses-stable")
    return ", ".join(status)


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

    missing_files = [rel for rel in REQUIRED_FILES if not (ROOT / rel).exists()]
    missing_workflows = [rel for rel in REQUIRED_WORKFLOWS if not (ROOT / rel).exists()]
    missing_reports = [rel for rel in OPTIONAL_REPORTS if not (ROOT / rel).exists()]
    missing_markers = [marker for marker in BLOCKING_MARKERS if marker not in root_text]
    missing_links = readme_missing_links()
    enabled_sources = [item for item in source_data.get("rule_sets", []) if item.get("enabled")]
    enabled_candidates = [
        item for item in candidate_data.get("candidates", []) if item.get("enabled") and item.get("activate", False)
    ]
    pending_scripts = [
        item.get("name", "unnamed")
        for item in candidate_data.get("candidates", [])
        if item.get("kind") == "script" and item.get("status") == "pending"
    ]

    history = json_load(ROOT / "reports" / "invalid_sources_history.json")
    privacy_lite_url = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/PrivacyLite/PrivacyLite.list"
    privacy_lite = {}
    for key, value in history.items():
        if key == privacy_lite_url or privacy_lite_url in key or value.get("url") == privacy_lite_url:
            privacy_lite = value
            break

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

    warnings: list[str] = []
    if missing_reports:
        warnings.append("部分可选治理报告尚未生成，首次运行报告生成器后会补齐")
    if not pending_scripts:
        warnings.append("当前没有 pending 脚本候选，请确认脚本自动收集仍保持关闭")
    if len(enabled_sources) > 20:
        warnings.append("启用远程源较多，需要持续观察误杀与性能")
    if privacy_lite and int(privacy_lite.get("fail_count", 0)) == 1:
        warnings.append("PrivacyLite 当前为单日 404，按策略仅观察，不禁用")
    if privacy_lite and int(privacy_lite.get("fail_count", 0)) >= 2:
        warnings.append("PrivacyLite 已连续失败 2 天及以上，应保守禁用候选或验证同源替代")

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
        f"- Root 与 Release 一致：{'是' if root_text == release_text else '否'}",
        f"- 启用远程规则源：{len(enabled_sources)}",
        f"- 启用候选源：{len(enabled_candidates)}",
        f"- pending 脚本候选：{len(pending_scripts)}",
        f"- 脚本总数：{len(script_names)}",
        f"- MITM hostname 数量：{len(mitm_hosts)}",
        "",
        "## 模块区块行数",
        "",
    ]
    lines += [f"- {name}: {count}" for name, count in module_section_counts(root_text).items()]

    workflow_items = [f"{rel}: {workflow_summary(ROOT / rel)}" for rel in REQUIRED_WORKFLOWS if (ROOT / rel).exists()]

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
    lines += [
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
        "4. 出现登录、支付、验证码异常时，优先回查 MITM、Body Rewrite 和 Map Local。",
        "5. 远程源连续失败 2 天后才进入处理流程，单日网络失败只报告观察。",
        "",
    ]

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Repository health report written to {REPORT}")
    if critical_issues:
        raise SystemExit("Repository health check found blocking issues: " + "; ".join(critical_issues))


if __name__ == "__main__":
    main()
