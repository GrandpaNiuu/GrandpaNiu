#!/usr/bin/env python3
"""Generate a health report for the single Fusion module."""

from __future__ import annotations

import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "repository_health_report.md"
MODULE = ROOT / "Ronghemokuai.sgmodule"
RELEASE = ROOT / "Release" / "Ronghemokuai.sgmodule"
EXPECTED_UPDATE_URL = "#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule"

REQUIRED_FILES = [
    "README.md",
    "Ronghemokuai.sgmodule",
    "Release/Ronghemokuai.sgmodule",
    "Rewrite/Profiles/fusion.conf",
    "Rewrite/Remotes/sources.json",
    "Rewrite/Remotes/candidates.json",
    "Rewrite/Sources/MITM-core.conf",
    "Rewrite/Sources/MITM-app-clean.conf",
    "Rewrite/Sources/MITM-stable-plus.conf",
    "Rewrite/Sources/MITM-extended.conf",
    "Rules/direct.list",
    "Rules/reject.list",
    "Rules/wechat-ad.list",
    "Scripts/app-cleaner.js",
    "Scripts/app-cleaner-active.conf",
    "Scripts/spotify.conf",
    "Scripts/youtube.conf",
    "Scripts/zhihu-enhance.conf",
    "Scripts/zhihu-enhance.js",
    "scripts/build_module.py",
    "scripts/build_release_variants.py",
    "scripts/factory_finalize.py",
    "scripts/validate_repository.py",
    "scripts/validate_profiles.py",
]

REQUIRED_WORKFLOWS = [
    ".github/workflows/module-factory-build.yml",
    ".github/workflows/daily-module-update.yml",
    ".github/workflows/daily-audit-and-repair.yml",
    ".github/workflows/daily-invalid-source-repair.yml",
    ".github/workflows/upstream-collect.yml",
    ".github/workflows/repository-health.yml",
]

REQUIRED_MARKERS = [
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

SCRIPT_NAME_RE = re.compile(r"^\s*([^#\s][^=]+?)\s*=")
HOSTNAME_RE = re.compile(r"^\s*hostname\s*=\s*(.+)$")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def run_command(args: list[str]) -> tuple[bool, str]:
    proc = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    output = (proc.stdout + proc.stderr).strip() or "无输出"
    return proc.returncode == 0, output


def active_script_names() -> list[str]:
    names: list[str] = []
    for path in (ROOT / "Scripts").glob("*.conf"):
        for line in read(path).splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            match = SCRIPT_NAME_RE.match(line)
            if match:
                names.append(match.group(1).strip())
    return names


def mitm_hosts(text: str) -> list[str]:
    start = text.find("[MITM]")
    if start < 0:
        return []
    hosts: list[str] = []
    for line in text[start:].splitlines():
        match = HOSTNAME_RE.match(line)
        if not match:
            continue
        value = match.group(1).replace("%APPEND%", "")
        hosts.extend(host.strip() for host in value.split(",") if host.strip())
    return hosts


def section_counts(text: str) -> dict[str, int]:
    sections = ["Rule", "URL Rewrite", "Header Rewrite", "Body Rewrite", "Map Local", "Script", "MITM"]
    counts = {section: 0 for section in sections}
    current = ""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("[") and stripped.endswith("]"):
            current = stripped.strip("[]")
            continue
        if current in counts and stripped:
            counts[current] += 1
    return counts


def workflow_summary(path: Path) -> str:
    text = read(path)
    items = []
    items.append("contents: write" if "contents: write" in text else "缺少 contents: write")
    items.append("concurrency" if "concurrency:" in text else "缺少 concurrency")
    items.append("fusion" if "--profile fusion" in text else "缺少 fusion 构建")
    items.append("rebase retry" if "git rebase origin/main" in text else "缺少 rebase retry")
    return "；".join(items)


def list_block(title: str, items: list[str]) -> list[str]:
    lines = ["", f"## {title}", ""]
    if not items:
        lines.append("- 无")
    else:
        lines.extend(f"- {item}" for item in items)
    return lines


def main() -> None:
    root_text = read(MODULE)
    release_text = read(RELEASE)
    fusion_text = read(ROOT / "Rewrite" / "Profiles" / "fusion.conf")
    validator_ok, validator_output = run_command([sys.executable, "scripts/validate_repository.py"])
    js_ok, js_output = run_command(["node", "--check", "Scripts/app-cleaner.js"])

    names = active_script_names()
    duplicate_scripts = sorted({name for name in names if names.count(name) > 1})
    hosts = mitm_hosts(root_text)
    duplicate_hosts = sorted({host for host in hosts if hosts.count(host) > 1})
    missing_files = [item for item in REQUIRED_FILES if not (ROOT / item).exists()]
    missing_workflows = [item for item in REQUIRED_WORKFLOWS if not (ROOT / item).exists()]
    missing_markers = [marker for marker in REQUIRED_MARKERS if marker not in root_text]

    workflow_items = [f"`{item}`：{workflow_summary(ROOT / item)}" for item in REQUIRED_WORKFLOWS if (ROOT / item).exists()]

    blockers: list[str] = []
    if root_text != release_text:
        blockers.append("Root 与 Release 不一致")
    if missing_files:
        blockers.append("缺少必要文件")
    if missing_workflows:
        blockers.append("缺少必要 workflow")
    if missing_markers:
        blockers.append("主模块缺少必要标记")
    if duplicate_scripts:
        blockers.append("存在重复脚本名")
    if duplicate_hosts:
        blockers.append("存在重复 MITM hostname")
    if "name = fusion" not in fusion_text or "single_public_entry = true" not in fusion_text:
        blockers.append("fusion profile 未就绪")
    if not validator_ok:
        blockers.append("validate_repository.py 未通过")
    if not js_ok:
        blockers.append("node --check Scripts/app-cleaner.js 未通过")

    counts = section_counts(root_text)
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# 仓库健康检查报告",
        "",
        f"生成时间：{now}",
        "",
        "## 总体状态",
        "",
        f"- 阻断问题：{len(blockers)}",
        f"- Root 与 Release 一致：{'是' if root_text == release_text else '否'}",
        "- GrandpaNiu = 默认 Fusion：是",
        f"- fusion profile：{'就绪' if 'name = fusion' in fusion_text else '异常'}",
        f"- validate_repository.py：{'通过' if validator_ok else '失败'}",
        f"- node --check Scripts/app-cleaner.js：{'通过' if js_ok else '失败'}",
        f"- 脚本总数：{len(names)}",
        f"- MITM hostname 数量：{len(hosts)}",
        "",
        "## 区块检查",
        "",
    ]
    lines.extend(f"- [{section}]：{count} 行" for section, count in counts.items())
    lines += list_block("阻断问题", blockers)
    lines += list_block("缺少文件", missing_files)
    lines += list_block("缺少 workflow", missing_workflows)
    lines += list_block("主模块缺少标记", missing_markers)
    lines += list_block("重复脚本名", duplicate_scripts)
    lines += list_block("重复 MITM hostname", duplicate_hosts)
    lines += list_block("Workflow 配置摘要", workflow_items)
    lines += [
        "",
        "## validate_repository.py 输出",
        "",
        "```text",
        validator_output,
        "```",
        "",
        "## node --check 输出",
        "",
        "```text",
        js_output,
        "```",
        "",
        "## 维护边界",
        "",
        "- 所有修改应 source-first，先改 Rules / Scripts / Rewrite/Sources / Rewrite/Remotes / Rewrite/Profiles/fusion.conf，再构建 Release 和 Root。",
        "- Fusion 是唯一用户入口，不再拆分 Stable / Stable Plus / Lite / Full。",
        "- 旧多版本文件如果存在，只作为历史兼容文件，不作为健康检查阻断项。",
        "",
    ]
    write(REPORT, "\n".join(lines))
    print(f"Repository health report written to {REPORT}")
    if blockers:
        raise SystemExit("Repository health check found blocking issues: " + "; ".join(blockers))


if __name__ == "__main__":
    main()
