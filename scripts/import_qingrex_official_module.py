#!/usr/bin/env python3
"""Import QingRex mini-program/app ad-removal sgmodule into source layers.

This script keeps the integration source-first. It downloads the upstream module,
extracts section bodies, writes reviewable source files, and emits a small report.
If the download fails but target source files already exist, it keeps the cached
sources so normal builds do not break because of a temporary upstream outage.

Stable safety boundary:
- Do not import the upstream "安全浏览限制解除" block. It is not an ad-removal
  function and can weaken browser/app safety checks.
- Do not import WeChat HTTPDNS rejects, because this repository already keeps
  those under manual review due to image/media false-positive risk.
"""

from __future__ import annotations

import re
import sys
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM_URL = (
    "https://raw.githubusercontent.com/QingRex/LoonKissSurge/refs/heads/main/Surge/Official/"
    "%E5%B0%8F%E7%A8%8B%E5%BA%8F%E5%92%8C%E5%BA%94%E7%94%A8%E6%87%92%E4%BA%BA"
    "%E5%8E%BB%E5%B9%BF%E5%91%8A%E5%90%88%E9%9B%86.official.sgmodule"
)

TARGETS = {
    "Rule": ROOT / "Rules" / "qingrex-miniapp-app-ad.list",
    "URL Rewrite": ROOT / "Rewrite" / "Sources" / "URL-Rewrite-qingrex-miniapp-app-ad.conf",
    "Body Rewrite": ROOT / "Rewrite" / "Sources" / "Body-Rewrite-qingrex-miniapp-app-ad.conf",
    "Map Local": ROOT / "Rewrite" / "Sources" / "Map-Local-qingrex-miniapp-app-ad.conf",
    "Script": ROOT / "Scripts" / "qingrex-miniapp-app-ad.conf",
    "MITM": ROOT / "Rewrite" / "Sources" / "MITM-qingrex-miniapp-app-ad.conf",
}

HEADERS = {
    "Rule": (
        "# QingRex mini-program and app lazy ad removal rule layer\n"
        "# Source module: 小程序和应用懒人去广告合集.official.sgmodule\n"
        "# Scope: app and mini-program ad domain/IP rejects.\n"
        "# Stable safety: non-ad safe-browsing bypass and WeChat HTTPDNS rejects are filtered out.\n"
        "# Rollback: remove qingrex_miniapp_rules from Rewrite/Profiles/stable.conf.\n\n"
    ),
    "URL Rewrite": (
        "# QingRex mini-program and app lazy ad removal URL Rewrite layer\n"
        "# Source module: 小程序和应用懒人去广告合集.official.sgmodule\n"
        "# Scope: mini-program and app ad URL rejects/redirect rules.\n"
        "# Rollback: remove qingrex_miniapp from [url_rewrite] in Rewrite/Profiles/stable.conf.\n\n"
    ),
    "Body Rewrite": (
        "# QingRex mini-program and app lazy ad removal Body Rewrite layer\n"
        "# Source module: 小程序和应用懒人去广告合集.official.sgmodule\n"
        "# Scope: jq body cleanup for selected mini-program ad payloads.\n"
        "# Rollback: remove qingrex_miniapp from [body_rewrite] in Rewrite/Profiles/stable.conf.\n\n"
    ),
    "Map Local": (
        "# QingRex mini-program and app lazy ad removal Map Local layer\n"
        "# Source module: 小程序和应用懒人去广告合集.official.sgmodule\n"
        "# Scope: mock empty ad/config responses for mini-program and app endpoints.\n"
        "# Keep data/status-code lines raw. Do not auto-escape quotes here.\n"
        "# Rollback: remove qingrex_miniapp from [map_local] in Rewrite/Profiles/stable.conf.\n\n"
    ),
    "Script": (
        "# QingRex mini-program and app lazy ad removal Script layer\n"
        "# Source module: 小程序和应用懒人去广告合集.official.sgmodule\n"
        "# Scope: response-body cleaners for selected mini-program endpoints.\n"
        "# External script paths are preserved from the source module and should be reviewed if failures appear.\n"
        "# Rollback: remove qingrex_miniapp from [scripts] in Rewrite/Profiles/stable.conf.\n\n"
    ),
    "MITM": (
        "# QingRex mini-program and app lazy ad removal MITM hostname layer\n"
        "# Source module: 小程序和应用懒人去广告合集.official.sgmodule\n"
        "# Scope: hostname coverage needed by QingRex mini-program/app rewrite, map-local and script rules.\n"
        "# Rollback: remove qingrex_miniapp from [mitm] in Rewrite/Profiles/stable.conf.\n\n"
    ),
}

EXCLUDED_BLOCK_TITLES = {"安全浏览限制解除"}
EXCLUDED_EXACT_RULE_PREFIXES = {
    "DOMAIN,dns.weixin.qq.com.cn,REJECT",
    "DOMAIN,dns.weixin.qq.com,REJECT",
}


def download_text() -> str:
    request = urllib.request.Request(UPSTREAM_URL, headers={"User-Agent": "GrandpaNiu-Module-Factory"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def parse_sections(text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current = "META"
    sections[current] = []
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        match = re.match(r"^\[([^\]]+)\]\s*$", line.strip())
        if match:
            current = match.group(1).strip()
            sections.setdefault(current, [])
        else:
            sections.setdefault(current, []).append(line)
    return sections


def filter_rule_lines(lines: list[str]) -> tuple[list[str], list[str]]:
    filtered: list[str] = []
    excluded: list[str] = []
    current_block_excluded = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#>") or stripped.startswith("# >"):
            title = stripped.lstrip("#").strip().lstrip(">").strip()
            current_block_excluded = title in EXCLUDED_BLOCK_TITLES
            if current_block_excluded:
                excluded.append(line)
                continue
        if current_block_excluded:
            excluded.append(line)
            continue
        if any(stripped.startswith(prefix) for prefix in EXCLUDED_EXACT_RULE_PREFIXES):
            excluded.append(line)
            continue
        filtered.append(line)
    return filtered, excluded


def section_body(section: str, lines: list[str]) -> tuple[str, list[str]]:
    excluded: list[str] = []
    cleaned = list(lines)
    if section == "Rule":
        cleaned, excluded = filter_rule_lines(cleaned)
    while cleaned and not cleaned[0].strip():
        cleaned.pop(0)
    while cleaned and not cleaned[-1].strip():
        cleaned.pop()
    return "\n".join(cleaned).rstrip() + ("\n" if cleaned else ""), excluded


def active_count(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.strip() and not line.lstrip().startswith("#"))


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def write_report(written: dict[str, str], status: str, excluded: list[str]) -> None:
    now = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S")
    report = [
        "# QingRex mini-program/app module import report",
        "",
        f"- Status: {status}",
        f"- Upstream: {UPSTREAM_URL}",
        f"- Generated at: {now}",
        "- Integration: source-first layer, connected through Rewrite/Profiles/stable.conf.",
        "- Rollback: remove qingrex_miniapp* entries from Rewrite/Profiles/stable.conf.",
        "",
        "## Imported sections",
        "",
        "| Section | Target | Active lines |",
        "|---|---|---:|",
    ]
    for section, target in TARGETS.items():
        content = written.get(section, "")
        report.append(f"| {section} | `{target.relative_to(ROOT).as_posix()}` | {active_count(content)} |")
    report.extend([
        "",
        "## Function summary",
        "",
        "- App and mini-program ad domain/IP rejects.",
        "- Mini-program URL reject rules for popups, splash ads, banners and recommendation placements.",
        "- Map Local mock responses for empty ad/config payloads.",
        "- jq Body Rewrite cleanup for selected ad payload fields.",
        "- Response-body script cleaners for selected mini-program endpoints.",
        "- MITM hostname coverage required by these rewrite/map-local/script rules.",
        "",
        "## Excluded from Stable import",
        "",
        "These lines are intentionally not imported into Stable because they are not pure ad-removal entries or have high false-positive risk.",
        "",
    ])
    if excluded:
        report.append("```text")
        report.extend(excluded)
        report.append("```")
    else:
        report.append("No excluded lines.")
    report.append("")
    write_text(ROOT / "reports" / "qingrex_miniapp_import_report.md", "\n".join(report))


def targets_have_content() -> bool:
    return all(path.exists() and path.read_text(encoding="utf-8", errors="ignore").strip() for path in TARGETS.values())


def main() -> None:
    try:
        source = download_text()
        status = "downloaded upstream and regenerated source layers"
    except Exception as exc:
        if targets_have_content():
            written = {section: path.read_text(encoding="utf-8", errors="ignore") for section, path in TARGETS.items()}
            write_report(written, f"kept cached source layers because upstream download failed: {exc}", [])
            print(f"WARN: QingRex upstream download failed; using cached source layers: {exc}")
            return
        print(f"ERROR: QingRex upstream download failed and no cached source layers exist: {exc}", file=sys.stderr)
        raise SystemExit(1)

    parsed = parse_sections(source)
    written: dict[str, str] = {}
    excluded_all: list[str] = []
    for section, target in TARGETS.items():
        body, excluded = section_body(section, parsed.get(section, []))
        excluded_all.extend(excluded)
        content = HEADERS[section] + body
        write_text(target, content)
        written[section] = content
    write_report(written, status, excluded_all)
    print("QingRex source layers imported.")


if __name__ == "__main__":
    main()
