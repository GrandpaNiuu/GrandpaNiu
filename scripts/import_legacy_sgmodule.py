#!/usr/bin/env python3
"""Import legacy Shadowrocket/Surge style rules into a staging area.

This tool is intentionally conservative. It does not modify the active factory
sources, Release files, or the root module. It parses a mixed legacy rule file or
.sgmodule into reviewable fragments under staging/legacy-import/<name>/.

Supported output fragments:
- Rule.conf
- URL-Rewrite.conf
- Header-Rewrite.conf
- Body-Rewrite.conf
- Map-Local.conf
- Script.conf
- MITM.conf
- apps/<AppName>.sgmodule when "# > AppName" markers exist

Typical use:
  python3 scripts/import_legacy_sgmodule.py path/to/legacy.sgmodule
  python3 scripts/import_legacy_sgmodule.py path/to/legacy.conf --name app2smile
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_ROOT = ROOT / "staging" / "legacy-import"
SECTION_ORDER = ["Rule", "URL Rewrite", "Header Rewrite", "Body Rewrite", "Map Local", "Script", "MITM"]
SECTION_RE = re.compile(r"^\[([^\]]+)\]\s*$")
APP_MARKER_RE = re.compile(r"^#\s*>\s*(.+?)\s*$")
HOSTNAME_RE = re.compile(r"^\s*hostname\s*=\s*(.+)$", re.I)
SCRIPT_LINE_RE = re.compile(r"^[^#\s][^=]{0,120}=\s*type=http-(?:request|response)", re.I)
RULE_TYPES = {
    "DOMAIN",
    "DOMAIN-SUFFIX",
    "DOMAIN-KEYWORD",
    "IP-CIDR",
    "IP-CIDR6",
    "GEOIP",
    "USER-AGENT",
    "URL-REGEX",
    "AND",
    "OR",
    "NOT",
    "PROCESS-NAME",
    "RULE-SET",
    "DOMAIN-SET",
}
URL_REWRITE_ACTIONS = (" url ", " reject", " reject-dict", " reject-array", " 302 ", " 307 ")
HEADER_TOKENS = (
    " request-header ",
    " response-header ",
    " header-del ",
    " header-add ",
    " header-replace ",
    " header-replace-regex ",
    " http-request ",
    " http-response ",
)
BODY_TOKENS = (" body-rewrite ", " response-body ", " request-body ")
MAP_LOCAL_TOKENS = (
    " map-local ",
    " echo-response ",
    " data=",
    " data =",
    " status-code=",
    " status-code =",
    " mock-response ",
    " mock-response=",
    " mock-response =",
)
SCRIPT_TOKENS = (
    " script-request-body ",
    " script-response-body ",
    " script-request-header ",
    " script-response-header ",
    " type=http-request",
    " type=http-response",
    " script-path=",
)


@dataclass
class ParsedModule:
    meta: list[str] = field(default_factory=list)
    sections: dict[str, list[str]] = field(default_factory=lambda: {name: [] for name in SECTION_ORDER})
    app_sections: dict[str, dict[str, list[str]]] = field(default_factory=dict)
    ignored: list[str] = field(default_factory=list)


def stop(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def safe_name(value: str) -> str:
    chars: list[str] = []
    for char in value.strip():
        if char.isalnum() or char in {"-", "_", "."}:
            chars.append(char)
        elif char in {" ", "/", "\\", ":"}:
            chars.append("-")
    name = "".join(chars).strip("-._")
    return name or "legacy"


def read_input(path: Path) -> str:
    if not path.exists():
        stop(f"input file not found: {path}")
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeError as exc:
        stop(f"input must be UTF-8 text: {path}: {exc}")
    except OSError as exc:
        stop(f"cannot read input: {path}: {exc}")


def add_line(target: list[str], line: str) -> None:
    value = line.rstrip()
    if not value:
        return
    if value not in target:
        target.append(value)


def classify_line(line: str, current_section: str | None) -> str | None:
    stripped = line.strip()
    if not stripped:
        return None
    if stripped.startswith("#!") or stripped.startswith("# update-date:"):
        return "META"
    if stripped.startswith("#"):
        return None
    if current_section in SECTION_ORDER:
        return current_section

    lowered = f" {stripped.lower()} "
    first = stripped.split(",", 1)[0].strip().upper()

    if first in RULE_TYPES:
        return "Rule"
    if HOSTNAME_RE.match(stripped):
        return "MITM"
    if SCRIPT_LINE_RE.match(stripped) or any(token in lowered for token in SCRIPT_TOKENS):
        return "Script"
    if stripped.startswith(("http-request ", "http-response ")) or any(token in lowered for token in HEADER_TOKENS):
        return "Header Rewrite"
    if any(token in lowered for token in BODY_TOKENS):
        return "Body Rewrite"
    if any(token in lowered for token in MAP_LOCAL_TOKENS):
        return "Map Local"
    if any(token in lowered for token in URL_REWRITE_ACTIONS):
        return "URL Rewrite"
    return None


def app_bucket(parsed: ParsedModule, app_name: str) -> dict[str, list[str]]:
    safe = safe_name(app_name)
    if safe not in parsed.app_sections:
        parsed.app_sections[safe] = {name: [] for name in SECTION_ORDER}
    return parsed.app_sections[safe]


def parse(text: str) -> ParsedModule:
    parsed = ParsedModule()
    current_section: str | None = None
    current_app: str | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        section_match = SECTION_RE.match(stripped)
        if section_match:
            section = section_match.group(1).strip()
            current_section = section if section in SECTION_ORDER else None
            continue

        app_match = APP_MARKER_RE.match(stripped)
        if app_match:
            current_app = app_match.group(1).strip()
            continue

        target_section = classify_line(line, current_section)
        if target_section is None:
            if stripped and not stripped.startswith("#"):
                add_line(parsed.ignored, line)
            continue
        if target_section == "META":
            add_line(parsed.meta, line)
            continue

        add_line(parsed.sections[target_section], line)
        if current_app:
            add_line(app_bucket(parsed, current_app)[target_section], line)

    return parsed


def render_section_file(lines: list[str]) -> str:
    return "\n".join(lines).strip() + ("\n" if lines else "")


def render_sgmodule(name: str, sections: dict[str, list[str]]) -> str:
    today = datetime.now(timezone(timedelta(hours=8))).date().isoformat()
    parts = [
        f"#!name={name}",
        f"#!desc=legacy import staging {today}",
        "# This file is generated for review only. Do not publish before manual migration.",
    ]
    for section in SECTION_ORDER:
        body = render_section_file(sections.get(section, []))
        if not body.strip():
            continue
        parts.append(f"[{section}]")
        parts.append(body.rstrip())
    return "\n".join(parts).rstrip() + "\n"


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def make_report(name: str, source: Path, parsed: ParsedModule) -> str:
    now = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# Legacy sgmodule import report",
        "",
        f"- Import name: {name}",
        f"- Source: {source.as_posix()}",
        f"- Generated at: {now}",
        "- Status: staging only; no factory source, Release, or root module was changed.",
        "- Mock, data and status-code lines are preserved as raw Map Local lines. The importer does not escape quotes or validate embedded JSON.",
        "",
        "## Section counts",
        "",
        "| Section | Lines |",
        "|---|---:|",
    ]
    for section in SECTION_ORDER:
        lines.append(f"| {section} | {len(parsed.sections.get(section, []))} |")
    lines.extend(["", "## App fragments", ""])
    if parsed.app_sections:
        lines.extend(["| App | Active sections | Total lines |", "|---|---|---:|"])
        for app, sections in sorted(parsed.app_sections.items()):
            active = [section for section in SECTION_ORDER if sections.get(section)]
            total = sum(len(sections.get(section, [])) for section in SECTION_ORDER)
            lines.append(f"| {app} | {', '.join(active) if active else 'none'} | {total} |")
    else:
        lines.append("No # > AppName markers found.")
    lines.extend(["", "## Ignored lines", ""])
    if parsed.ignored:
        lines.append("```text")
        lines.extend(parsed.ignored[:200])
        if len(parsed.ignored) > 200:
            lines.append(f"... clipped {len(parsed.ignored) - 200} more lines")
        lines.append("```")
    else:
        lines.append("No ignored active lines.")
    lines.extend([
        "",
        "## Manual migration checklist",
        "",
        "1. Review every generated fragment before copying into Rules/, Scripts/, or Rewrite/Sources/.",
        "2. Do not move staging output directly into Release or the root module.",
        "3. Rebuild with scripts/build_module.py and run scripts/validate_repository.py after migration.",
        "4. Keep complex Script, MITM, Header Rewrite, Body Rewrite and Map Local entries under manual review.",
        "",
    ])
    return "\n".join(lines)


def write_staging(parsed: ParsedModule, source: Path, output_root: Path, name: str) -> Path:
    target = output_root / safe_name(name)
    target.mkdir(parents=True, exist_ok=True)
    for section in SECTION_ORDER:
        filename = section.replace(" ", "-") + ".conf"
        write_text(target / filename, render_section_file(parsed.sections.get(section, [])))
    if parsed.meta:
        write_text(target / "Meta.conf", render_section_file(parsed.meta))
    if parsed.ignored:
        write_text(target / "ignored-lines.txt", render_section_file(parsed.ignored))
    for app, sections in sorted(parsed.app_sections.items()):
        write_text(target / "apps" / f"{app}.sgmodule", render_sgmodule(app, sections))
    write_text(target / "import_report.md", make_report(name, source, parsed))
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse a legacy mixed module/rule file into staging fragments.")
    parser.add_argument("input", help="Legacy .sgmodule/.conf/.list file to parse")
    parser.add_argument("--name", help="Import name. Defaults to input file stem.")
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT_ROOT), help="Output root. Defaults to staging/legacy-import")
    args = parser.parse_args()

    source = Path(args.input).expanduser()
    if not source.is_absolute():
        source = ROOT / source
    name = args.name or source.stem
    parsed = parse(read_input(source))
    output_path = write_staging(parsed, source.relative_to(ROOT) if source.is_relative_to(ROOT) else source, Path(args.output_root), name)
    print(f"Legacy import staged at: {output_path.relative_to(ROOT) if output_path.is_relative_to(ROOT) else output_path}")


if __name__ == "__main__":
    main()
