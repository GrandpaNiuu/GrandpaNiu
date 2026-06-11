#!/usr/bin/env python3
"""Validate the single Fusion module repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from validate_module_integrity import validate_all as validate_module_integrity

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "Ronghemokuai.sgmodule"
RELEASE = ROOT / "Release" / "Ronghemokuai.sgmodule"
README = ROOT / "README.md"
SOURCES_JSON = ROOT / "Rewrite" / "Remotes" / "sources.json"
CANDIDATES_JSON = ROOT / "Rewrite" / "Remotes" / "candidates.json"
EXPECTED_UPDATE_URL = "#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule"

REQUIRED_MARKERS = (
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
)

REQUIRED_FILES = (
    "README.md",
    "SECURITY.md",
    "LICENSE",
    "CONTRIBUTING.md",
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
    "Rules/aggressive-ad-sources.list",
    "Scripts/app-cleaner.js",
    "Scripts/app-cleaner-active.conf",
    "Scripts/spotify.conf",
    "Scripts/youtube.conf",
    "Scripts/zhihu-enhance.conf",
    "Scripts/zhihu-enhance.js",
    "scripts/build_module.py",
    "scripts/build_release_variants.py",
    "scripts/factory_finalize.py",
    "scripts/validate_profiles.py",
    "scripts/validate_module_integrity.py",
    "scripts/validate_repository.py",
    "reports/multi_release_report.md",
    "reports/module_integrity_report.md",
)

REQUIRED_WORKFLOWS = (
    ".github/workflows/module-factory-build.yml",
    ".github/workflows/daily-module-update.yml",
    ".github/workflows/daily-audit-and-repair.yml",
    ".github/workflows/daily-invalid-source-repair.yml",
    ".github/workflows/upstream-collect.yml",
    ".github/workflows/repository-health.yml",
)

ALLOWED_REMOTE_TYPES = {"RULE-SET", "DOMAIN-SET"}
ALLOWED_POLICIES = {"REJECT", "REJECT-DROP", "DIRECT"}
BLOCKED_URL_TOKENS = ("ghproxy", "mirror", "tinyurl", "bit.ly", "t.co/", "shorturl")
SCRIPT_NAME_RE = re.compile(r"^\s*([^#\s][^=]+?)\s*=")
HOSTNAME_RE = re.compile(r"^\s*hostname\s*=\s*(.+)$")
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path) -> dict:
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def active_lines(text: str):
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            yield stripped


def workflow_builds_fusion(text: str) -> bool:
    compact = re.sub(r"\s+", " ", text)
    return any(
        token in text or token in compact
        for token in (
            "fusion-build-marker: scripts/build_module.py --build --profile fusion",
            "scripts/build_module.py --build --profile fusion",
            "--profile fusion",
            '"--profile", "fusion"',
            "'--profile', 'fusion'",
            "profile=fusion",
        )
    )


def parse_hosts(text: str) -> list[str]:
    hosts: list[str] = []
    for line in text.splitlines():
        match = HOSTNAME_RE.match(line)
        if not match:
            continue
        value = match.group(1).replace("%APPEND%", "")
        hosts.extend(host.strip() for host in value.split(",") if host.strip())
    return hosts


def workflow_has_fusion_build(text: str) -> bool:
    """Accept shell commands and Python subprocess list syntax."""
    normalized = re.sub(r"\s+", " ", text)
    patterns = (
        "--profile fusion",
        "--profile=fusion",
        '"--profile", "fusion"',
        "'--profile', 'fusion'",
        '"--profile","fusion"',
        "'--profile','fusion'",
    )
    return "build_module.py" in text and any(pattern in normalized for pattern in patterns)


def validate_root_release() -> None:
    root_text = read_text(MODULE)
    release_text = read_text(RELEASE)
    if root_text != release_text:
        fail("Ronghemokuai.sgmodule and Release/Ronghemokuai.sgmodule differ")
    for marker in REQUIRED_MARKERS:
        if marker not in root_text:
            fail(f"required marker missing from root module: {marker}")


def validate_single_release_report() -> None:
    report = read_text(ROOT / "reports" / "multi_release_report.md")
    if "单一融合版发布报告" not in report:
        fail("multi_release_report.md must describe the single fusion release")
    if "Ronghemokuai.sgmodule" not in report or "fusion" not in report:
        fail("multi_release_report.md missing fusion release entry")


def validate_remote_schema() -> None:
    data = read_json(SOURCES_JSON)
    urls: set[str] = set()
    for index, item in enumerate(data.get("rule_sets", []), 1):
        for key in ("name", "type", "url", "policy", "enabled", "protected", "purpose"):
            if key not in item:
                fail(f"sources.json rule_sets[{index}] missing {key}")
        if item["type"] not in ALLOWED_REMOTE_TYPES:
            fail(f"sources.json rule_sets[{index}] invalid type: {item['type']}")
        if item["policy"] not in ALLOWED_POLICIES:
            fail(f"sources.json rule_sets[{index}] invalid policy: {item['policy']}")
        url = str(item["url"])
        if not url.startswith("https://"):
            fail(f"sources.json rule_sets[{index}] must use https: {url}")
        if any(token in url.lower() for token in BLOCKED_URL_TOKENS):
            fail(f"sources.json rule_sets[{index}] uses blocked host/token: {url}")
        if url in urls:
            fail(f"duplicate remote source url in sources.json: {url}")
        urls.add(url)

    candidates = read_json(CANDIDATES_JSON)
    if candidates.get("policy", {}).get("search_web") is not False:
        fail("candidates.json policy.search_web must stay false")
    trusted = candidates.get("trusted_repositories", [])
    if not isinstance(trusted, list) or not trusted:
        fail("candidates.json must define trusted_repositories")


def validate_scripts() -> None:
    spotify_text = read_text(ROOT / "Scripts" / "spotify.conf")
    youtube_text = read_text(ROOT / "Scripts" / "youtube.conf")
    app_text = read_text(ROOT / "Scripts" / "app-clean.conf")

    if "spotify-json" not in spotify_text or "spotify-proto" not in spotify_text:
        fail("Scripts/spotify.conf must contain spotify-json and spotify-proto")
    if "youtube.response" not in youtube_text:
        fail("Scripts/youtube.conf must contain youtube.response")
    if "zhihu-enhance" not in read_text(ROOT / "Scripts" / "zhihu-enhance.conf"):
        fail("Scripts/zhihu-enhance.conf must contain zhihu-enhance")
    if not any(token in app_text.lower() for token in ("tieba", "qq-news", "vgtime", "fmz200", "zirawell", "wool_scripts", "app2smile")):
        fail("Scripts/app-clean.conf does not appear to contain app cleanup scripts")

    names: set[str] = set()
    for path in (ROOT / "Scripts").glob("*.conf"):
        for line in active_lines(read_text(path)):
            match = SCRIPT_NAME_RE.match(line)
            if not match:
                continue
            name = match.group(1).strip()
            if name in names:
                fail(f"duplicate script name: {name}")
            names.add(name)


def validate_mitm() -> None:
    text = read_text(MODULE)
    mitm_start = text.find("[MITM]")
    if mitm_start < 0:
        fail("[MITM] missing")
    hosts = parse_hosts(text[mitm_start:])
    if not hosts:
        fail("MITM hostname list is empty")
    for host in ("spclient.wg.spotify.com", "*.spclient.spotify.com"):
        if host not in hosts:
            fail(f"root module missing Spotify MITM hostname: {host}")
    dupes = sorted({host for host in hosts if hosts.count(host) > 1})
    if dupes:
        fail("duplicate MITM hostnames: " + ", ".join(dupes[:20]))


def validate_fusion_profile() -> None:
    fusion = read_text(ROOT / "Rewrite" / "Profiles" / "fusion.conf")
    required_tokens = (
        "name = fusion",
        "Rules/wechat-ad.list",
        "Rules/aggressive-ad-sources.list",
        "Scripts/app2smile-qqnews-stable-plus.conf",
        "Rewrite/Sources/MITM-core.conf",
        "Rewrite/Sources/MITM-app-clean.conf",
        "Rewrite/Sources/MITM-stable-plus.conf",
        "Rewrite/Sources/MITM-extended.conf",
        "single_public_entry = true",
    )
    for token in required_tokens:
        if token not in fusion:
            fail(f"fusion.conf missing required token: {token}")


def validate_files() -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            fail(f"required file missing: {relative}")


def validate_readme_links() -> None:
    text = read_text(README)
    for match in MD_LINK_RE.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        path_part = target.split("#", 1)[0]
        if path_part and not (ROOT / path_part).exists():
            fail(f"README link target missing: {target}")


def validate_workflows() -> None:
    for relative in REQUIRED_WORKFLOWS:
        path = ROOT / relative
        if not path.exists():
            fail(f"required workflow missing: {relative}")
        text = read_text(path)
        if "contents: write" not in text:
            fail(f"workflow must declare contents: write: {relative}")
        if "concurrency:" not in text:
            fail(f"workflow must declare concurrency: {relative}")
        if "git rebase origin/main" not in text:
            fail(f"workflow must retry push after rebase: {relative}")

    for relative in REQUIRED_WORKFLOWS:
        text = read_text(ROOT / relative)
        if not workflow_has_fusion_build(text):
            fail(f"{relative} must build with fusion profile")

    daily = read_text(ROOT / ".github" / "workflows" / "daily-module-update.yml")
    for token in ("build_module.py", "factory_finalize.py", "build_release_variants.py", "validate_repository.py"):
        if token not in daily:
            fail(f"daily-module-update workflow missing command token: {token}")

    for relative in (
        ".github/workflows/daily-module-update.yml",
        ".github/workflows/daily-audit-and-repair.yml",
        ".github/workflows/daily-invalid-source-repair.yml",
        ".github/workflows/upstream-collect.yml",
    ):
        text = read_text(ROOT / relative)
        if 'cron: "0 16 * * *"' not in text and "cron: '0 16 * * *'" not in text:
            fail(f"{relative} must run daily at Beijing 00:00")

    invalid_source = read_text(ROOT / ".github" / "workflows" / "daily-invalid-source-repair.yml")
    for token in ("collect_upstreams.py", "audit_repair_invalid_sources.py", "validate_remote_rule_syntax.py"):
        if token not in invalid_source:
            fail(f"daily-invalid-source-repair workflow missing command token: {token}")
    if "reset --hard origin/main" not in invalid_source:
        fail("daily-invalid-source-repair workflow must regenerate after reset to origin/main before push retry")

    audit = read_text(ROOT / ".github" / "workflows" / "daily-audit-and-repair.yml")
    if "validate_remote_rule_syntax.py" not in audit:
        fail("daily-audit-and-repair workflow missing validate_remote_rule_syntax.py")

    health = read_text(ROOT / ".github" / "workflows" / "repository-health.yml")
    for token in ("generate_stable_plus_promotion_report.py", "create_promotion_pr.py"):
        if token in health:
            fail(f"repository-health workflow must not run legacy promotion command: {token}")

    watcher = read_text(ROOT / ".github" / "workflows" / "workflow-failure-issue.yml")
    if re.search(r"fromJSON\([^)]*cancelled", watcher):
        fail("workflow-failure-issue must not open issues for cancelled runs")
    if "close-resolved-issues" not in watcher:
        fail("workflow-failure-issue must close stale automation issues after successful runs")


def validate_no_tool_traces() -> None:
    for relative in (".claude", "CLAUDE.md"):
        if (ROOT / relative).exists():
            fail(f"tool trace file should not exist: {relative}")


def main() -> None:
    validate_files()
    validate_root_release()
    validate_module_integrity(write_report=True)
    validate_single_release_report()
    validate_remote_schema()
    validate_scripts()
    validate_mitm()
    validate_fusion_profile()
    validate_readme_links()
    validate_workflows()
    validate_no_tool_traces()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
