#!/usr/bin/env python3
"""Generate a repository health report for the module factory."""

from __future__ import annotations

import datetime as dt
import os
import re
import shutil
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
    "SECURITY.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "Ronghemokuai.sgmodule",
    "Release/Ronghemokuai.sgmodule",
    "Release/Ronghemokuai-stable.sgmodule",
    "Release/Ronghemokuai-stable-plus.sgmodule",
    "Release/Ronghemokuai-lite.sgmodule",
    "Release/Ronghemokuai-full.sgmodule",
    "Rewrite/Profiles/stable.conf",
    "Rewrite/Profiles/stable-plus.conf",
    "Rewrite/Profiles/lite.conf",
    "Rewrite/Profiles/full.conf",
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
    "scripts/audit_reject_risk.py",
    "scripts/generate_app_status_matrix.py",
    "scripts/create_promotion_pr.py",
    "scripts/score_candidates.py",
    "scripts/check_report_freshness.py",
    "scripts/audit_domestic_app_connectivity.py",
    "scripts/validate_repository.py",
    "scripts/validate_profiles.py",
    "docs/MODULE_FEATURES.md",
    "docs/AUTOMATION_POLICY.md",
    "docs/PROFILE_POLICY.md",
    "docs/TESTING.md",
    "docs/QUALITY_GATE.md",
    "docs/RELEASE.md",
    "backup/manifest.json",
]

REQUIRED_WORKFLOWS = [
    ".github/workflows/module-factory-build.yml",
    ".github/workflows/daily-module-update.yml",
    ".github/workflows/daily-invalid-source-repair.yml",
    ".github/workflows/upstream-collect.yml",
    ".github/workflows/repository-health.yml",
    ".github/workflows/stable-plus-promotion-pr.yml",
]

REQUIRED_REPORTS = [
    "reports/profile_validation_report.md",
    "reports/repository_health_report.md",
    "reports/workflow_health_report.md",
    "reports/domestic_app_connectivity_audit.md",
    "reports/candidate_security_score_report.md",
    "reports/report_freshness_report.md",
    "reports/media_wechat_false_positive_report.md",
    "reports/wechat_ad_test_report.md",
    "reports/repository_maturity_review.md",
    "reports/reject_risk_report.md",
    "reports/app_status_matrix.md",
    "reports/promotion_pr_report.md",
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
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def active_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip() and not line.lstrip().startswith("#")]


def run_command(args: list[str], env: dict[str, str] | None = None) -> tuple[bool, str]:
    try:
        proc = subprocess.run(args, cwd=ROOT, text=True, capture_output=True, env=env)
    except OSError as exc:
        return False, f"{type(exc).__name__}: {exc}"
    output = (proc.stdout + proc.stderr).strip() or "无输出"
    return proc.returncode == 0, output


def node_binary() -> str:
    env_node = os.environ.get("NODE_BINARY")
    if env_node and Path(env_node).exists():
        return env_node
    bundled = Path.home() / ".cache" / "codex-runtimes" / "codex-primary-runtime" / "dependencies" / "node" / "bin" / "node.exe"
    if os.name == "nt" and bundled.exists():
        return str(bundled)
    found = shutil.which("node")
    if found:
        return found
    if bundled.exists():
        return str(bundled)
    return "node"


def run_generators() -> list[str]:
    generators = [
        ["scripts/audit_reject_risk.py"],
        ["scripts/generate_app_status_matrix.py"],
        ["scripts/create_promotion_pr.py"],
        ["scripts/score_candidates.py"],
        ["scripts/audit_domestic_app_connectivity.py"],
        ["scripts/generate_workflow_health_report.py"],
        ["scripts/check_report_freshness.py"],
    ]
    notes: list[str] = []
    for script in generators:
        ok, output = run_command([sys.executable, *script])
        notes.append(f"`{' '.join(script)}`：{'通过' if ok else '失败'}")
        if not ok:
            notes.append(f"  - {output}")
    return notes


def collect_script_dupes() -> tuple[int, list[str]]:
    names: list[str] = []
    for path in (ROOT / "Scripts").glob("*.conf"):
        for line in active_lines(read(path)):
            match = SCRIPT_NAME_RE.match(line)
            if match:
                names.append(match.group(1).strip())
    dupes = sorted({name for name in names if names.count(name) > 1})
    return len(names), dupes


def parse_hosts(text: str) -> list[str]:
    hosts: list[str] = []
    for line in text.splitlines():
        match = HOSTNAME_RE.match(line)
        if not match:
            continue
        value = match.group(1).replace("%APPEND%", "")
        hosts.extend(host.strip() for host in value.split(",") if host.strip())
    return hosts


def collect_mitm_dupes() -> tuple[int, list[str]]:
    text = read(MODULE)
    start = text.find("[MITM]")
    hosts = parse_hosts(text[start:]) if start >= 0 else []
    dupes = sorted({host for host in hosts if hosts.count(host) > 1})
    return len(hosts), dupes


def readme_missing_links() -> list[str]:
    missing: list[str] = []
    for match in MD_LINK_RE.finditer(read(ROOT / "README.md")):
        target = match.group(1).strip()
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        path_part = target.split("#", 1)[0]
        if path_part and not (ROOT / path_part).exists():
            missing.append(target)
    return sorted(set(missing))


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
    if "node --check Scripts/app-cleaner.js" in text:
        items.append("node --check")
    if "--profile stable" in text:
        items.append("默认 stable")
    if "--profile full" in text or "--profile stable-plus" in text:
        items.append("存在非默认 profile 调用，需确认是否仅测试步骤")
    return "；".join(items)


def freshness_blockers() -> list[str]:
    text = read(ROOT / "reports" / "report_freshness_report.md")
    blockers: list[str] = []
    for line in text.splitlines():
        if not line.startswith("| `reports/"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 3 and cells[1] in {"stale", "missing"} and cells[2] == "是":
            blockers.append(cells[0].strip("`"))
    return blockers


def list_block(title: str, items: list[str], code: bool = False) -> list[str]:
    lines = ["", f"## {title}", ""]
    if not items:
        lines.append("- 无")
    else:
        for item in items:
            lines.append(f"- `{item}`" if code else f"- {item}")
    return lines


def main() -> None:
    generator_notes = run_generators()
    root_text = read(MODULE)
    release_text = read(RELEASE)
    script_count, script_dupes = collect_script_dupes()
    mitm_count, mitm_dupes = collect_mitm_dupes()
    validator_ok, validator_output = run_command([sys.executable, "scripts/validate_repository.py"])
    js_ok, js_output = run_command([node_binary(), "--check", "Scripts/app-cleaner.js"])

    missing_files = [rel for rel in REQUIRED_FILES if not (ROOT / rel).exists()]
    missing_workflows = [rel for rel in REQUIRED_WORKFLOWS if not (ROOT / rel).exists()]
    missing_reports = [rel for rel in REQUIRED_REPORTS if not (ROOT / rel).exists()]
    missing_markers = [marker for marker in REQUIRED_MARKERS if marker not in root_text]
    missing_links = readme_missing_links()
    freshness = freshness_blockers()

    stable = read(ROOT / "Rewrite" / "Profiles" / "stable.conf")
    stable_plus = read(ROOT / "Rewrite" / "Profiles" / "stable-plus.conf")
    lite = read(ROOT / "Rewrite" / "Profiles" / "lite.conf")
    wechat_plus_only = "wechat_ad_test = Rules/wechat-ad.list" in stable_plus and "wechat_ad_test" not in stable and "wechat_ad_test" not in lite

    critical: list[str] = []
    if root_text != release_text:
        critical.append("Root 与 Release 不一致")
    if missing_files:
        critical.append("缺少必要文件")
    if missing_workflows:
        critical.append("缺少必要 workflow")
    if missing_reports:
        critical.append("缺少必要报告")
    if missing_markers:
        critical.append("主模块缺少必要标记")
    if script_dupes:
        critical.append("存在重复脚本名")
    if mitm_dupes:
        critical.append("存在重复 MITM hostname")
    if missing_links:
        critical.append("README 存在失效本地链接")
    if not validator_ok:
        critical.append("validate_repository.py 未通过")
    if not js_ok:
        critical.append("node --check Scripts/app-cleaner.js 未通过")
    if freshness:
        critical.append("存在 blocking stale report")
    if not wechat_plus_only:
        critical.append("微信广告规则没有保持 Stable Plus only")

    workflow_items = [f"`{rel}`：{workflow_summary(ROOT / rel)}" for rel in REQUIRED_WORKFLOWS if (ROOT / rel).exists()]
    counts = section_counts(root_text)
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")

    lines = [
        "# 仓库健康检查报告",
        "",
        f"生成时间：{now}",
        "",
        "## 总体状态",
        "",
        f"- 阻断问题：{len(critical)}",
        f"- Root 与 Release 一致：{'是' if root_text == release_text else '否'}",
        "- GrandpaNiu = 默认 Stable：是",
        f"- validate_repository.py：{'通过' if validator_ok else '失败'}",
        f"- node --check Scripts/app-cleaner.js：{'通过' if js_ok else '失败'}",
        f"- workflow 最新状态：无法确认，需要在 GitHub Actions 页面确认 completed / success",
        f"- 微信广告仅 Stable Plus：{'是' if wechat_plus_only else '否'}",
        f"- 脚本总数：{script_count}",
        f"- MITM hostname 数量：{mitm_count}",
        "",
        "## 区块检查",
        "",
    ]
    lines += [f"- [{section}]：{count} 行" for section, count in counts.items()]
    lines += list_block("报告生成器运行结果", generator_notes)
    lines += list_block("阻断问题", critical)
    lines += list_block("缺少文件", missing_files, code=True)
    lines += list_block("缺少 workflow", missing_workflows, code=True)
    lines += list_block("缺少报告", missing_reports, code=True)
    lines += list_block("主模块缺少标记", missing_markers, code=True)
    lines += list_block("重复脚本名", script_dupes, code=True)
    lines += list_block("重复 MITM hostname", mitm_dupes, code=True)
    lines += list_block("README 失效本地链接", missing_links, code=True)
    lines += list_block("Blocking stale reports", freshness, code=True)
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
        "- 所有修改应 source-first，先改 Rules / Scripts / Rewrite/Sources / Rewrite/Remotes / Rewrite/Profiles，再构建 Release 和 Root。",
        "- Stable 目标是稳定、低误伤、可长期使用，不追求最大覆盖。",
        "- Stable Plus 只做增强测试，不整体合并进 Stable。",
        "- 没有真实手测记录时，报告必须写未测或 manual-review。",
        "- 本报告无法确认远端 workflow 最新运行状态，需在 GitHub Actions 页面查看。",
        "",
    ]
    write(REPORT, "\n".join(lines))
    print(f"Repository health report written to {REPORT}")
    if critical:
        raise SystemExit("Repository health check found blocking issues: " + "; ".join(critical))


if __name__ == "__main__":
    main()
