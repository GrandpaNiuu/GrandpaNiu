#!/usr/bin/env python3
"""Generate a health report for the single Fusion module repository."""

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
RELEASE_ALIAS = ROOT / "Release" / "Module.sgmodule"
EXPECTED_UPDATE_URL = "#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule"

REQUIRED_FILES = [
    "README.md",
    "Ronghemokuai.sgmodule",
    "Release/Ronghemokuai.sgmodule",
    "Release/Module.sgmodule",
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
    "scripts/commit_generated_changes.sh",
    "tools/acquire_automation_lock.sh",
    "tools/release_automation_lock.sh",
    "scripts/validate_repository.py",
    "scripts/validate_profiles.py",
    "scripts/validate_app_sources.py",
    "tools/generate_automated_quality_evidence.py",
    "tools/validate_script_aggregation.py",
    "tools/test_script_bundle_sandbox.py",
    "tools/validate_upstream_risk_gate.py",
    "tools/generate_mitm_scope_report.py",
    "tools/generate_rule_overlap_report.py",
    "tools/generate_app_cleaner_active_report.py",
    "reports/automated_quality_evidence.md",
    "reports/script_aggregation_validation_report.md",
    "reports/script_bundle_sandbox_report.md",
    "reports/upstream_risk_gate_report.md",
    "reports/mitm_scope_report.md",
    "reports/rule_overlap_report.md",
    "reports/app_cleaner_active_report.md",
    "reports/app_source_validation_report.md",
]

REQUIRED_WORKFLOWS = [
    ".github/workflows/module-factory-build.yml",
    ".github/workflows/daily-module-update.yml",
    ".github/workflows/daily-audit-and-repair.yml",
    ".github/workflows/daily-invalid-source-repair.yml",
    ".github/workflows/scheduled-module-update.yml",
    ".github/workflows/upstream-app-module-sync.yml",
    ".github/workflows/upstream-collect.yml",
    ".github/workflows/daily-schedule-watchdog.yml",
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
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def normalize_output(text: str) -> str:
    root = str(ROOT)
    normalized_root = root.replace("\\", "/")
    return text.replace(root, ".").replace(normalized_root, ".").replace("\\", "/")


def run_command(args: list[str]) -> tuple[bool, str]:
    try:
        proc = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    except OSError as exc:
        return False, f"{type(exc).__name__}: {exc}"
    output = (proc.stdout + proc.stderr).strip() or "no output"
    return proc.returncode == 0, normalize_output(output)


def node_executable() -> str | None:
    configured = os.environ.get("NODE_BINARY")
    if configured and Path(configured).exists():
        return configured
    found = shutil.which("node")
    if found:
        return found
    return None


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


def workflow_has_fusion_build(text: str) -> bool:
    compact = re.sub(r"\s+", " ", text)
    return any(
        token in text or token in compact
        for token in (
            "fusion-build-marker: scripts/build_module.py --build --profile fusion",
            "scripts/build_module.py --build --profile fusion",
            "--profile fusion",
            "--profile=fusion",
            '"--profile", "fusion"',
            "'--profile', 'fusion'",
            "profile=fusion",
        )
    )


def workflow_summary(path: Path) -> str:
    text = read(path)
    helper = read(ROOT / "scripts" / "commit_generated_changes.sh")
    uses_helper = "scripts/commit_generated_changes.sh" in text
    items = [
        "contents: write" if "contents: write" in text else "missing contents: write",
        "isolated concurrency"
        if "group: module-maintenance-${{ github.workflow }}-${{ github.ref }}" in text
        else "missing isolated concurrency",
        "fusion" if workflow_has_fusion_build(text) else "missing fusion build",
        "safe commit helper" if uses_helper else "missing safe commit helper",
        "cross-workflow lock"
        if "tools/acquire_automation_lock.sh" in text
        and "tools/release_automation_lock.sh" in text
        and "if: always()" in text
        else "missing cross-workflow lock",
        "rebase retry" if uses_helper and "git rebase origin/main" in helper else "missing rebase retry",
    ]
    return "; ".join(items)


def list_block(title: str, items: list[str]) -> list[str]:
    lines = ["", f"## {title}", ""]
    if not items:
        lines.append("- none")
    else:
        lines.extend(f"- {item}" for item in items)
    return lines


def main() -> None:
    root_text = read(MODULE)
    release_text = read(RELEASE)
    alias_text = read(RELEASE_ALIAS)
    fusion_text = read(ROOT / "Rewrite" / "Profiles" / "fusion.conf")

    validator_ok, validator_output = run_command([sys.executable, "scripts/validate_repository.py"])
    evidence_ok, evidence_output = run_command([sys.executable, "tools/generate_automated_quality_evidence.py"])
    node_bin = node_executable()
    if node_bin:
        js_ok, js_output = run_command([node_bin, "--check", "Scripts/app-cleaner.js"])
    else:
        js_ok, js_output = False, "node executable not found"

    names = active_script_names()
    duplicate_scripts = sorted({name for name in names if names.count(name) > 1})
    hosts = mitm_hosts(root_text)
    duplicate_hosts = sorted({host for host in hosts if hosts.count(host) > 1})
    missing_files = [item for item in REQUIRED_FILES if not (ROOT / item).exists()]
    missing_workflows = [item for item in REQUIRED_WORKFLOWS if not (ROOT / item).exists()]
    missing_markers = [marker for marker in REQUIRED_MARKERS if marker not in root_text]
    workflow_items = [f"`{item}`: {workflow_summary(ROOT / item)}" for item in REQUIRED_WORKFLOWS if (ROOT / item).exists()]

    blockers: list[str] = []
    if root_text != release_text:
        blockers.append("Root module and Release module differ")
    if alias_text != release_text:
        blockers.append("Release module alias and Release module differ")
    if missing_files:
        blockers.append("Required files are missing")
    if missing_workflows:
        blockers.append("Required workflows are missing")
    if missing_markers:
        blockers.append("Fusion module is missing required markers")
    if duplicate_scripts:
        blockers.append("Duplicate script names exist")
    if duplicate_hosts:
        blockers.append("Duplicate MITM hostnames exist")
    if "name = fusion" not in fusion_text or "single_public_entry = true" not in fusion_text:
        blockers.append("Fusion profile is not finalized")
    if not validator_ok:
        blockers.append("validate_repository.py failed")
    if not evidence_ok:
        blockers.append("automated quality evidence generation failed")
    if not js_ok:
        blockers.append("node --check Scripts/app-cleaner.js failed")

    counts = section_counts(root_text)
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# Repository Health Report",
        "",
        f"- Generated at: {now}",
        f"- Blocking issues: {len(blockers)}",
        f"- Root and Release identical: {'yes' if root_text == release_text else 'no'}",
        f"- Release alias identical: {'yes' if alias_text == release_text else 'no'}",
        f"- Fusion profile finalized: {'yes' if 'name = fusion' in fusion_text and 'single_public_entry = true' in fusion_text else 'no'}",
        f"- validate_repository.py: {'passed' if validator_ok else 'failed'}",
        f"- automated quality evidence: {'passed' if evidence_ok else 'failed'}",
        f"- node --check Scripts/app-cleaner.js: {'passed' if js_ok else 'failed'}",
        f"- Script entries: {len(names)}",
        f"- MITM hostnames: {len(hosts)}",
        "",
        "## Section Counts",
        "",
    ]
    lines.extend(f"- [{section}]: {count}" for section, count in counts.items())
    lines += list_block("Blocking Issues", blockers)
    lines += list_block("Missing Files", missing_files)
    lines += list_block("Missing Workflows", missing_workflows)
    lines += list_block("Missing Fusion Markers", missing_markers)
    lines += list_block("Duplicate Script Names", duplicate_scripts)
    lines += list_block("Duplicate MITM Hostnames", duplicate_hosts)
    lines += list_block("Workflow Summary", workflow_items)
    lines += [
        "",
        "## validate_repository.py Output",
        "",
        "```text",
        validator_output,
        "```",
        "",
        "## automated quality evidence Output",
        "",
        "```text",
        evidence_output,
        "```",
        "",
        "## node --check Output",
        "",
        "```text",
        js_output,
        "```",
    ]
    write(REPORT, "\n".join(lines))


if __name__ == "__main__":
    main()
