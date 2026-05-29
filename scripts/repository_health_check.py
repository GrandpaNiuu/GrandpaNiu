#!/usr/bin/env python3
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
    "README.md", "Ronghemokuai.sgmodule", "Release/Ronghemokuai.sgmodule",
    "Rewrite/Profiles/stable.conf", "Rewrite/Profiles/lite.conf",
    "Rewrite/Remotes/sources.json", "Rewrite/Remotes/candidates.json",
    "Scripts/spotify.conf", "Scripts/youtube.conf", "Scripts/app-clean.conf",
    "Scripts/zhihu-enhance.conf", "Scripts/zhihu-enhance.js",
    "Rules/direct.list", "Rules/spotify-direct.list", "Rules/youtube-direct.list",
    "Rules/reject.list", "Rules/app-clean.list", "Rules/web-ads.list",
    "docs/FACTORY_FLOW.md", "docs/MAINTENANCE.md", "docs/TROUBLESHOOTING.md",
    "docs/COVERAGE.md", "docs/SCOPE.md", "docs/PERFORMANCE.md",
    "docs/QUALITY_GATE.md", "docs/RELEASE.md", "CHANGELOG.md",
    "requirements.txt", ".editorconfig", ".gitignore",
]
REQUIRED_WORKFLOWS = [
    ".github/workflows/module-factory-build.yml",
    ".github/workflows/daily-module-update.yml",
    ".github/workflows/daily-invalid-source-repair.yml",
    ".github/workflows/upstream-collect.yml",
    ".github/workflows/repository-health.yml",
]
BLOCKING_MARKERS = [
    "[Rule]", "[URL Rewrite]", "[Header Rewrite]", "[Body Rewrite]", "[Map Local]",
    "[Script]", "[MITM]", "spotify-json", "spotify-proto", "youtube.response",
    "zhihu-enhance", EXPECTED_UPDATE_URL,
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
    return names, sorted({name for name in names if names.count(name) > 1})


def collect_mitm_hosts() -> tuple[list[str], list[str]]:
    text = read(MODULE)
    start = text.find("[MITM]")
    if start < 0:
        return [], []
    hosts: list[str] = []
    for line in text[start:].splitlines():
        match = HOSTNAME_RE.match(line)
        if match:
            hosts.extend([h.strip() for h in match.group(1).split(",") if h.strip() and h.strip() != "%APPEND%"])
    return hosts, sorted({host for host in hosts if hosts.count(host) > 1})


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
    proc = subprocess.run([sys.executable, "scripts/validate_repository.py"], cwd=ROOT, text=True, capture_output=True)
    return proc.returncode == 0, (proc.stdout + proc.stderr).strip() or "no output"


def module_section_counts(text: str) -> dict[str, int]:
    sections = ["Rule", "URL Rewrite", "Header Rewrite", "Body Rewrite", "Map Local", "Script", "MITM"]
    counts = {section: 0 for section in sections}
    current = ""
    for line in text.splitlines():
        if line.startswith("[") and line.endswith("]"):
            current = line.strip("[]")
        elif current in counts and line.strip():
            counts[current] += 1
    return counts


def bullet(items: list[str], code: bool = False) -> list[str]:
    if not items:
        return ["- 无"]
    return [f"- `{item}`" if code else f"- {item}" for item in items]


def add_section(lines: list[str], title: str, items: list[str], code: bool = False) -> None:
    lines += ["", f"## {title}", ""]
    lines += bullet(items, code)


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
    missing_markers = [marker for marker in BLOCKING_MARKERS if marker not in root_text]
    missing_links = readme_missing_links()
    enabled_sources = [item for item in source_data.get("rule_sets", []) if item.get("enabled")]
    enabled_candidates = [item for item in candidate_data.get("candidates", []) if item.get("enabled") and item.get("activate", False)]
    pending_scripts = [item.get("name", "unnamed") for item in candidate_data.get("candidates", []) if item.get("kind") == "script" and item.get("status") == "pending"]

    critical_issues: list[str] = []
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

    warnings: list[str] = []
    if missing_files:
        warnings.append("存在缺失资料文件")
    if missing_workflows:
        warnings.append("存在缺失工作流")
    if not pending_scripts:
        warnings.append("当前没有 pending 脚本候选")
    if len(enabled_sources) > 20:
        warnings.append("启用远程源较多，需观察误杀与性能")

    lines: list[str] = [
        "# 仓库健康检查报告", "", f"生成时间：{now}", "",
        "## 总体状态", "",
        f"- 阻断问题：{len(critical_issues)}",
        f"- 提醒事项：{len(warnings)}",
        f"- 统一验证：{'通过' if validator_ok else '失败'}",
        f"- Root 与 Release 一致：{'yes' if root_text == release_text else 'no'}",
        f"- 启用远程源：{len(enabled_sources)}",
        f"- 启用候选源：{len(enabled_candidates)}",
        f"- pending 脚本候选：{len(pending_scripts)}",
        f"- 脚本总数：{len(script_names)}",
        f"- MITM hostname 数量：{len(mitm_hosts)}",
        "", "## 模块区块行数", "",
    ]
    lines += [f"- {name}: {count}" for name, count in module_section_counts(root_text).items()]

    add_section(lines, "阻断问题", critical_issues)
    add_section(lines, "提醒事项", warnings)
    add_section(lines, "缺失资料文件", missing_files, code=True)
    add_section(lines, "缺失工作流", missing_workflows, code=True)
    add_section(lines, "主模块缺失关键标记", missing_markers, code=True)
    add_section(lines, "重复脚本名", script_dupes, code=True)
    add_section(lines, "重复 MITM hostname", mitm_dupes, code=True)
    add_section(lines, "README 失效本地链接", missing_links, code=True)
    add_section(lines, "Pending 脚本候选", pending_scripts)
    lines += ["", "## 统一验证输出", "", "```text", validator_output, "```", "", "## 后续维护建议", "", "1. 每次修改源头文件后运行 Module Factory Build。", "2. Root 与 Release 必须保持一致。", "3. 新脚本默认 pending，不直接进入 stable。", "4. 耗电异常时优先测试 lite profile。", "5. 远程源连续失败 2 天后再处理，避免临时网络波动误删。", ""]

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Repository health report written to {REPORT}")
    if critical_issues:
        raise SystemExit("Repository health check found blocking issues: " + "; ".join(critical_issues))


if __name__ == "__main__":
    main()
