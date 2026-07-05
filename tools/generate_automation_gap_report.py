#!/usr/bin/env python3
"""Generate a blocking report for remaining automation coverage gaps.

This check is intentionally about maintainability, not ad-rule effectiveness.
It verifies that generated outputs, workflow writers, platform projections, and
release reports are wired into automation. It does not score replacement
upstreams and it does not treat real device testing as a CI gate.
"""

from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "automation_gap_report.md"

ROOT_MODULE = ROOT / "Ronghemokuai.sgmodule"
RELEASE_MODULE = ROOT / "Release" / "Ronghemokuai.sgmodule"
RELEASE_ALIAS = ROOT / "Release" / "Module.sgmodule"
APP_SOURCES_DIR = ROOT / "Rewrite" / "Sources" / "Apps"
RELEASE_MODULES_DIR = ROOT / "Release" / "Modules"
ANDROID_BRANCHES = ROOT / "Android" / "branches.json"
RELEASE_ANDROID_BRANCHES = ROOT / "Release" / "Android" / "branches.json"
V2RAYN_OUTPUT = ROOT / "Windows" / "v2rayN" / "GrandpaNiu-v2rayN-custom-routing.json"
QUALITY_GATE = ROOT / "scripts" / "quality_gate.py"
COMMIT_HELPER = ROOT / "scripts" / "commit_generated_changes.sh"
PAGES_DEPLOY_WORKFLOW = ROOT / ".github" / "workflows" / "pages-deploy.yml"
SCRIPT_BUNDLE = ROOT / "Scripts" / "generated" / "fusion-script-bundle.js"
SCRIPT_MANIFEST = ROOT / "Scripts" / "generated" / "fusion-script-bundle.manifest.json"
SCRIPT_CACHE = ROOT / "Scripts" / "generated" / "fusion-script-bundle.cache.json"

REQUIRED_REPORTS = (
    "reports/android_rules_report.md",
    "reports/app_source_validation_report.md",
    "reports/automation_status_report.md",
    "reports/automated_quality_evidence.md",
    "reports/mitm_scope_report.md",
    "reports/mitm_reject_risk_ledger.md",
    "reports/upstream_provenance_report.md",
    "reports/platform_compatibility_matrix.md",
    "reports/protected_traffic_ledger.md",
    "reports/false_positive_review_report.md",
    "reports/module_integrity_report.md",
    "reports/release_android_report.md",
    "reports/release_modules_report.md",
    "reports/report_freshness_report.md",
    "reports/rule_overlap_report.md",
    "reports/report_encoding_report.md",
    "reports/script_aggregation_validation_report.md",
    "reports/script_bundle_sandbox_report.md",
    "reports/upstream_risk_gate_report.md",
)

REQUIRED_QUALITY_COMMANDS = (
    "Rewrite/Generator/Builder.py",
    "scripts/validate_app_sources.py",
    "scripts/android_format_check.py",
    "tools/validate_script_aggregation.py",
    "tools/test_script_bundle_sandbox.py",
    "tools/validate_upstream_risk_gate.py",
    "scripts/check_automation_status.py",
    "tools/generate_upstream_provenance_report.py",
    "tools/generate_platform_compatibility_matrix.py",
    "tools/generate_protected_traffic_ledger.py",
    "tools/generate_false_positive_review_report.py",
    "tools/generate_automation_gap_report.py",
    "tools/check_report_encoding.py",
    "scripts/validate_repository.py",
)

REQUIRED_DAILY_WORKFLOWS = {
    ".github/workflows/daily-module-update.yml": "37 16 * * *",
    ".github/workflows/daily-audit-and-repair.yml": "43 16 * * *",
    ".github/workflows/daily-invalid-source-repair.yml": "49 16 * * *",
    ".github/workflows/upstream-collect.yml": "55 16 * * *",
    ".github/workflows/scheduled-module-update.yml": "7 17 * * *",
    ".github/workflows/upstream-app-module-sync.yml": "19 17 * * *",
    ".github/workflows/daily-schedule-watchdog.yml": "30 20 * * *",
}

BUILDER_WRITER_WORKFLOWS = (
    ".github/workflows/module-factory-build.yml",
    ".github/workflows/daily-module-update.yml",
    ".github/workflows/daily-audit-and-repair.yml",
    ".github/workflows/daily-invalid-source-repair.yml",
    ".github/workflows/scheduled-module-update.yml",
    ".github/workflows/upstream-app-module-sync.yml",
    ".github/workflows/upstream-collect.yml",
    ".github/workflows/daily-schedule-watchdog.yml",
    ".github/workflows/repository-health.yml",
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def active_app_sources() -> list[Path]:
    if not APP_SOURCES_DIR.exists():
        return []
    return sorted(path for path in APP_SOURCES_DIR.glob("*.conf") if not path.stem.startswith("_"))


def release_modules() -> list[Path]:
    if not RELEASE_MODULES_DIR.exists():
        return []
    return sorted(RELEASE_MODULES_DIR.glob("*.sgmodule"))


def add_gap(gaps: list[str], message: str) -> None:
    gaps.append(message)


def check_release_outputs(gaps: list[str], notes: list[str]) -> None:
    if not ROOT_MODULE.exists() or not RELEASE_MODULE.exists() or not RELEASE_ALIAS.exists():
        add_gap(gaps, "Fusion public module, Release module, or Release alias is missing.")
        return
    root_bytes = ROOT_MODULE.read_bytes()
    release_bytes = RELEASE_MODULE.read_bytes()
    alias_bytes = RELEASE_ALIAS.read_bytes()
    if root_bytes != release_bytes:
        add_gap(gaps, "Root module and Release/Ronghemokuai.sgmodule differ.")
    if alias_bytes != release_bytes:
        add_gap(gaps, "Release/Module.sgmodule and Release/Ronghemokuai.sgmodule differ.")
    notes.append("Fusion public entries are byte-identical." if root_bytes == release_bytes == alias_bytes else "Fusion public entries need repair.")


def check_app_module_coverage(gaps: list[str], notes: list[str]) -> None:
    sources = active_app_sources()
    modules = release_modules()
    if not sources:
        add_gap(gaps, "No app source files were found under Rewrite/Sources/Apps.")
    if not modules:
        add_gap(gaps, "No generated app modules were found under Release/Modules.")
    if sources and modules and len(sources) != len(modules):
        add_gap(gaps, f"App source and Release module counts differ: sources={len(sources)}, modules={len(modules)}.")
    missing = sorted({path.stem for path in sources} - {path.stem for path in modules})
    if missing:
        add_gap(gaps, "Missing Release app modules: " + ", ".join(missing[:20]))
    notes.append(f"App source files: {len(sources)}; Release app modules: {len(modules)}.")


def count_mihomo(path: Path) -> int:
    pattern = re.compile(r"^\s*-\s*(DOMAIN|DOMAIN-SUFFIX|DOMAIN-KEYWORD|IP-CIDR|IP-CIDR6),")
    return sum(1 for line in read(path).splitlines() if pattern.match(line))


def count_sing_box(path: Path) -> int:
    data = read_json(path)
    total = 0
    for rule in data.get("rules", []):
        if isinstance(rule, dict):
            for key in ("domain", "domain_suffix", "domain_keyword", "ip_cidr"):
                value = rule.get(key, [])
                if isinstance(value, list):
                    total += len(value)
    return total


def count_adguard(path: Path) -> int:
    return sum(1 for line in read(path).splitlines() if line.strip() and not line.lstrip().startswith("!"))


def count_v2rayng(path: Path) -> int:
    data = read_json(path)
    total = 0
    for rule in data.get("routing", {}).get("rules", []):
        if not isinstance(rule, dict) or rule.get("outboundTag") != "block":
            continue
        for key in ("domain", "ip"):
            value = rule.get(key, [])
            if isinstance(value, list):
                total += len(value)
    return total


def branch_rule_count(branch_id: str, path: Path) -> int:
    if branch_id == "mihomo":
        return count_mihomo(path)
    if branch_id == "sing-box":
        return count_sing_box(path)
    if branch_id == "adguard":
        return count_adguard(path)
    if branch_id == "v2rayng":
        return count_v2rayng(path)
    return -1


def check_android_windows_parity(gaps: list[str], notes: list[str]) -> None:
    if not ANDROID_BRANCHES.exists() or not RELEASE_ANDROID_BRANCHES.exists():
        add_gap(gaps, "Android branch manifest is missing from source or Release output.")
        return
    source_manifest = read_json(ANDROID_BRANCHES)
    release_manifest = read_json(RELEASE_ANDROID_BRANCHES)
    if source_manifest != release_manifest:
        add_gap(gaps, "Android/branches.json and Release/Android/branches.json differ.")
    branches = source_manifest.get("branches", [])
    if not isinstance(branches, list) or not branches:
        add_gap(gaps, "Android branch manifest has no branches.")
        return
    for branch in branches:
        if not isinstance(branch, dict):
            add_gap(gaps, "Android branch manifest contains a non-object branch entry.")
            continue
        branch_id = str(branch.get("id", ""))
        for key in ("target", "release_target"):
            value = branch.get(key)
            if not isinstance(value, str) or not (ROOT / value).exists():
                add_gap(gaps, f"Android branch {branch_id} missing output: {key}={value}")
        target = branch.get("target")
        expected = branch.get("rule_count")
        if isinstance(target, str) and isinstance(expected, int) and (ROOT / target).exists():
            actual = branch_rule_count(branch_id, ROOT / target)
            if actual != expected:
                add_gap(gaps, f"Android branch {branch_id} rule count differs: manifest={expected}, actual={actual}.")
    if V2RAYN_OUTPUT.exists():
        rules = read_json(V2RAYN_OUTPUT)
        if not isinstance(rules, list) or len(rules) < 6:
            add_gap(gaps, "Windows v2rayN custom routing is empty or missing tail rules.")
        else:
            tail = rules[-5:]
            expected_tail = [
                ("domain", ["geosite:private"], "direct"),
                ("domain", ["geosite:cn"], "direct"),
                ("ip", ["geoip:private"], "direct"),
                ("ip", ["geoip:cn"], "direct"),
                ("port", "0-65535", "proxy"),
            ]
            for rule, (key, value, outbound) in zip(tail, expected_tail):
                if not isinstance(rule, dict) or rule.get(key) != value or rule.get("outboundTag") != outbound or rule.get("enabled") is not True:
                    add_gap(gaps, "Windows v2rayN custom routing tail rules are not in the expected direct/proxy order.")
                    break
    else:
        add_gap(gaps, "Windows v2rayN custom routing output is missing.")
    notes.append(f"Android branches checked: {len(branches)}; Windows v2rayN output checked.")


def workflow_contains_cron(text: str, cron: str) -> bool:
    return f'cron: "{cron}"' in text or f"cron: '{cron}'" in text


def check_workflows(gaps: list[str], notes: list[str]) -> None:
    helper_text = read(COMMIT_HELPER)
    if 'git add -- "$@"' not in helper_text:
        add_gap(gaps, "Generated commit helper does not stage explicit paths.")
    if "git rebase origin/main" not in helper_text or "for attempt in 1 2 3" not in helper_text:
        add_gap(gaps, "Generated commit helper is missing fetch/rebase/retry push behavior.")
    if "git add -A" in helper_text or "git reset --hard" in helper_text or "git clean -fd" in helper_text:
        add_gap(gaps, "Generated commit helper contains broad or destructive git behavior.")

    for relative, cron in REQUIRED_DAILY_WORKFLOWS.items():
        path = ROOT / relative
        text = read(path)
        if not text:
            add_gap(gaps, f"Required scheduled workflow is missing: {relative}.")
            continue
        if not workflow_contains_cron(text, cron):
            add_gap(gaps, f"Scheduled workflow {relative} does not use the expected Beijing cron {cron}.")

    for relative in BUILDER_WRITER_WORKFLOWS:
        path = ROOT / relative
        text = read(path)
        if not text:
            add_gap(gaps, f"Required writer workflow is missing: {relative}.")
            continue
        for token in (
            "group: module-maintenance-${{ github.workflow }}-${{ github.ref }}",
            "tools/acquire_automation_lock.sh",
            "tools/release_automation_lock.sh",
            "scripts/commit_generated_changes.sh",
        ):
            if token not in text:
                add_gap(gaps, f"Writer workflow {relative} is missing automation token: {token}.")
        if "git add -A" in text or "git reset --hard" in text or "git clean -fd" in text:
            add_gap(gaps, f"Writer workflow {relative} contains broad or destructive git behavior.")
        if "Rewrite/Generator/Builder.py --profile fusion --release" in text:
            for output in ("Android", "Windows", "Release", "Web", "reports"):
                if f"\n            {output} \\" not in text and f"\n            {output}\n" not in text:
                    add_gap(gaps, f"Workflow {relative} runs the full Builder but does not stage {output}.")
    notes.append(f"Scheduled workflows checked: {len(REQUIRED_DAILY_WORKFLOWS)}; writer workflows checked: {len(BUILDER_WRITER_WORKFLOWS)}.")

    pages_text = read(PAGES_DEPLOY_WORKFLOW)
    if not pages_text:
        add_gap(gaps, "Pages deploy workflow is missing.")
    else:
        for token in (
            "pages: write",
            "id-token: write",
            "group: pages-deploy-main",
            "cancel-in-progress: false",
            "actions/upload-pages-artifact@",
            "actions/deploy-pages@",
            "path: _site",
            "timeout: 600000",
            "name: github-pages-${{ github.run_attempt }}",
            "artifact_name: github-pages-${{ github.run_attempt }}",
            "name: github-pages-${{ github.run_attempt }}-retry-2",
            "artifact_name: github-pages-${{ github.run_attempt }}-retry-2",
            "name: github-pages-${{ github.run_attempt }}-retry-3",
            "artifact_name: github-pages-${{ github.run_attempt }}-retry-3",
            "continue-on-error: true",
            "Wait before Pages retry 2",
            "Wait before Pages retry 3",
            "All Pages deployment attempts failed.",
        ):
            if token not in pages_text:
                add_gap(gaps, f"Pages deploy workflow missing token: {token}.")
        if "\n  push:" in pages_text:
            add_gap(gaps, "Pages deploy workflow still deploys directly on push; it should publish after final workflow_run only.")
        for token in (
            "Daily Module Update",
            "Daily invalid rule audit and safe repair",
            "Daily invalid source audit and repair",
            "Scheduled Module Factory Update",
            "Upstream app module sync",
            "Upstream candidate collect",
            "Repository Health Check",
        ):
            if token in pages_text:
                add_gap(gaps, f"Pages deploy workflow still listens to high-frequency workflow_run trigger: {token}.")
        for token in ("git add -A", "git reset --hard", "git clean -fd", "git push --force"):
            if token in pages_text:
                add_gap(gaps, f"Pages deploy workflow contains unsafe git command: {token}.")
    notes.append("Pages deployment workflow checked for self-managed artifact deploy, maximum supported deployment timeout, serialized final deployment, reduced trigger noise, and deployment retry guard.")


def check_quality_gate(gaps: list[str], notes: list[str]) -> None:
    text = read(QUALITY_GATE)
    for token in REQUIRED_QUALITY_COMMANDS:
        if token not in text:
            add_gap(gaps, f"quality_gate.py is missing automation command token: {token}.")
    notes.append(f"Quality gate command tokens checked: {len(REQUIRED_QUALITY_COMMANDS)}.")


def check_reports_and_script_cache(gaps: list[str], notes: list[str]) -> None:
    missing = [item for item in REQUIRED_REPORTS if not (ROOT / item).exists()]
    if missing:
        add_gap(gaps, "Required automation reports are missing: " + ", ".join(missing[:20]))
    for path in (SCRIPT_MANIFEST, SCRIPT_CACHE):
        if not path.exists():
            add_gap(gaps, f"Script aggregation file is missing: {rel(path)}.")
            continue
        try:
            read_json(path)
        except json.JSONDecodeError as exc:
            add_gap(gaps, f"Script aggregation JSON is invalid in {rel(path)}: {exc}.")
    if not SCRIPT_BUNDLE.exists() or not read(SCRIPT_BUNDLE).strip():
        add_gap(gaps, "Generated fusion script bundle is missing or empty.")
    notes.append(f"Required reports checked: {len(REQUIRED_REPORTS)}; script aggregation cache checked.")


def write_report(gaps: list[str], notes: list[str]) -> None:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# Automation Gap Report",
        "",
        f"- Generated at: {now}",
        f"- Blocking gaps: {len(gaps)}",
        "",
        "## Blocking Gaps",
        "",
    ]
    if gaps:
        lines.extend(f"- {gap}" for gap in gaps)
    else:
        lines.append("- none")
    lines += [
        "",
        "## Covered Automation Areas",
        "",
    ]
    lines.extend(f"- {note}" for note in notes)
    lines += [
        "",
        "## Intentional Non-CI Boundaries",
        "",
        "- Real App end-to-end behavior is not a CI gate; it remains owner/device verified.",
        "- Ad impression disappearance is not a CI gate; static checks prove syntax, wiring, and source traceability only.",
        "- Upstream replacement scoring is intentionally not implemented in this pass.",
        "- App feedback ingestion is intentionally not implemented in this pass.",
        "- Android and Windows outputs are routing projections; iOS Script, MITM, Body Rewrite, and Map Local behavior cannot be fully projected.",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> int:
    gaps: list[str] = []
    notes: list[str] = []
    check_release_outputs(gaps, notes)
    check_app_module_coverage(gaps, notes)
    check_android_windows_parity(gaps, notes)
    check_workflows(gaps, notes)
    check_quality_gate(gaps, notes)
    check_reports_and_script_cache(gaps, notes)
    write_report(gaps, notes)
    if gaps:
        for gap in gaps:
            print(f"ERROR: {gap}")
        print(f"Automation gap check failed: {len(gaps)} blocking gap(s).")
        return 1
    print("Automation gap check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
