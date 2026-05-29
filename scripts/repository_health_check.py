#!/usr/bin/env python3
"""Generate a professional repository health report.

This script is intentionally read-only except for writing
reports/repository_health_report.md. It complements validate_repository.py:
- validate_repository.py is the blocking quality gate;
- repository_health_check.py is the maintenance dashboard and gap scanner.
"""

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
    "CHANGELOG.md",
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


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


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
        if not target or target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        path_part = target.split("#", 1)[0]
        if path_part and not (ROOT / path_part).exists():
            missing.append(target)
    return sorted(set(missing))


def run_validator() -> tuple[bool, str]:
    path = ROOT / "scripts" / "validate_repository.py"
    if not path.exists():
        return False, "scripts/validate_repository.py missing"
    proc = subprocess.run([sys.executable, str(path)], cwd=ROOT, text=True, capture_output=True)
    output = (proc.stdout + proc.stderr).strip()
    return proc.returncode == 0, output or "no output"


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


def main() -> None:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    root_text = read(MODULE)
    release_text = read(RELEASE)
    source_data = json_load(SOURCES_JSON)
    candidate_data = json_load(CANDIDATES_JSON)
    script_names, script_dupes = collect_script_names()
    mitm_hosts, mitm_dupes = collect_mitm_hosts()
    validator_ok, validator_output = run_validator()

    missing_files = [rel for rel in REQUIRED_FILES if not exists(rel)]
    missing_workflows = [rel for rel in REQUIRED_WORKFLOWS if not exists(rel)]
    missing_markers = [marker for marker in BLOCKING_MARKERS if marker not in root_text]
    missing_links = readme_missing_links()
    section_counts = module_section_counts(root_text)

    enabled_sources = [item for item in source_data.get("rule_sets", []) if item.get("enabled")]
    enabled_candidates = [item for item in candidate_data.get("candidates", []) if item.get("enabled") and item.get("activate", False)]
    pending_scripts = [item.get("name", "unnamed") for item in candidate_data.get("candidates", []) if item.get("kind") == "script" and item.get("status") == "pending"]

    critical_issues = []
    if root_text != release_text:
        critical_issues.append("Root 与 Release 不一致")
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

    warnings = []
    if missing_files:
        warnings.append("存在缺失资料文件")
    if missing_workflows:
        warnings.append("存在缺失工作流")
    if not pending_scripts:
        warnings.append("当前没有 pending 脚本候选，后续新增脚本时应保持 pending 审核模式")
    if len(enabled_sources) > 20:
        warnings.append("启用远程源较多，需观察误杀与性能")

    lines = [
        "# 仓库健康检查报告",
        "",
        f"生成时间：{now}",
        "",
        "## 总体状态",
        "",
        f"- 阻断问题：{len(critical_issues)}",
        f"- 提醒事项：{len(warnings)}",
        f"- 统一验证：{'通过' if validator_ok else '失败'}",
        f"- Root 与 Release 一致：{'yes' if root_text == release_text else 'no'}",
        f"- 启用远程源：{len(enabled_sources)}",
        f"- 启用候选源：{len(enabled_candidates)}",
        f"- pending 脚本候选：{len(pending_scripts)}",
        f"- 脚本总数：{len(script_names)}",
        f"- MITM hostname 数量：{len(mitm_hosts)}",
        "",
        "## 模块区块行数",
        "",
        *[f"- {name}: {count}" for name, count in section_counts.items()],
        "",
        "## 阻断问题",
        "",
        *(f"- {item}" for item in critical_issues) if critical_issues else ["- 无"],
        "",
        "## 提醒事项",
        "",
        *(f"- {item}" for item in warnings) if warnings else ["- 无"],
        "",
        "## 缺失资料文件",
        "",
        *(f"- `{item}`" for item in missing_files) if missing_files else ["- 无"],
        "",
        "## 缺失工作流",
        "",
        *(f"- `{item}`" for item in missing_workflows) if missing_workflows else ["- 无"],
        "",
        "## 主模块缺失关键标记",
        "",
        *(f"- `{item}`" for item in missing_markers) if missing_markers else ["- 无"],
        "",
        "## 重复脚本名",
        "",
        *(f"- `{item}`" for item in script_dupes) if script_dupes else ["- 无"],
        "",
        "## 重复 MITM hostname",
        "",
        *(f"- `{item}`" for item in mitm_dupes) if mitm_dupes else ["- 无"],
        "",
        "## README 失效本地链接",
        "",
        *(f"- `{item}`" for item in missing_links) if missing_links else ["- 无"],
        "",
        "## Pending 脚本候选",
        "",
        *(f"- {item}" for item in pending_scripts) if pending_scripts else ["- 无"],
        "",
        "## 统一验证输出",
        "",
        "```text",
        validator_output,
        "```",
        "",
        "## 后续维护建议",
        "",
        "1. 每次修改源头文件后运行 Module Factory Build。",
        "2. Root 与 Release 必须保持一致。",
        "3. 新脚本默认 pending，不直接进入 stable。",
        "4. 耗电异常时优先测试 lite profile。",
        "5. 远程源连续失败 2 天后再处理，避免 GitHub 临时网络波动误删。",
        "",
    ]

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Repository health report written to {REPORT}")

    if critical_issues:
        raise SystemExit("Repository health check found blocking issues: " + "; ".join(critical_issues))


if __name__ == "__main__":
    main()
