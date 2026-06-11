#!/usr/bin/env python3
"""Generate initial per-app module files from the built fusion module."""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELEASE_MODULE = ROOT / "Release" / "Ronghemokuai.sgmodule"
MODULES_DIR = ROOT / "Release" / "Modules"
REPORT = ROOT / "reports" / "release_modules_report.md"
BASE_URL = "https://grandpaniuu.github.io/GrandpaNiu/Release/Modules"

SECTION_ORDER = ["Rule", "URL Rewrite", "Header Rewrite", "Body Rewrite", "Map Local", "Script", "MITM"]


@dataclass(frozen=True)
class ModuleSpec:
    slug: str
    name: str
    keywords: tuple[str, ...]


SPECS = [
    ModuleSpec("spotify", "GrandpaNiu Spotify", ("spotify", "spclient", "scdn.co", "pscdn.co")),
    ModuleSpec("youtube", "GrandpaNiu YouTube", ("youtube", "youtu.be", "googlevideo", "ytimg", "maasea")),
    ModuleSpec("zhihu", "GrandpaNiu Zhihu", ("zhihu", "zhihu-enhance")),
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def split_sections(text: str) -> tuple[list[str], dict[str, list[str]]]:
    meta: list[str] = []
    sections: dict[str, list[str]] = {name: [] for name in SECTION_ORDER}
    current: str | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("[") and line.endswith("]"):
            name = line[1:-1]
            current = name if name in sections else None
            continue
        if current is None:
            meta.append(line)
        else:
            sections[current].append(line)
    return meta, sections


def matches(line: str, spec: ModuleSpec) -> bool:
    low = line.lower()
    return any(keyword.lower() in low for keyword in spec.keywords)


def active(line: str) -> bool:
    stripped = line.strip()
    return bool(stripped) and not stripped.startswith("#")


def filter_regular_lines(lines: list[str], spec: ModuleSpec) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for raw in lines:
        line = raw.strip()
        if not active(line) or not matches(line, spec):
            continue
        if line in seen:
            continue
        seen.add(line)
        out.append(line)
    return out


def filter_mitm(lines: list[str], spec: ModuleSpec) -> list[str]:
    hosts: list[str] = []
    seen: set[str] = set()
    for raw in lines:
        line = raw.strip()
        if not line.startswith("hostname") or "=" not in line:
            continue
        value = line.split("=", 1)[1].replace("%APPEND%", "")
        for host in value.split(","):
            clean = host.strip()
            if not clean or clean in seen:
                continue
            if matches(clean, spec):
                seen.add(clean)
                hosts.append(clean)
    if not hosts:
        return []
    return ["hostname = %APPEND% " + ",".join(hosts)]


def module_text(spec: ModuleSpec, sections: dict[str, list[str]]) -> tuple[str, dict[str, int]]:
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        f"#!name={spec.name}",
        f"#!desc=Generated per-app module from GrandpaNiu fusion output",
        f"#!update-url={BASE_URL}/{spec.slug}.sgmodule",
        f"# generated-at: {today}",
    ]
    counts: dict[str, int] = {}
    for section in SECTION_ORDER:
        if section == "MITM":
            body = filter_mitm(sections[section], spec)
        else:
            body = filter_regular_lines(sections[section], spec)
        if not body:
            continue
        lines.extend(["", f"[{section}]", *body])
        counts[section] = len(body)
    lines.append("")
    return "\n".join(lines), counts


def make_index(summary: list[tuple[ModuleSpec, dict[str, int]]]) -> str:
    lines = [
        "# Release Modules",
        "",
        "Generated per-app module outputs.",
        "",
        "| Module | File | Sections |",
        "|---|---|---|",
    ]
    for spec, counts in summary:
        section_text = ", ".join(f"{name}:{count}" for name, count in counts.items()) or "empty"
        lines.append(f"| {spec.name} | `{spec.slug}.sgmodule` | {section_text} |")
    lines.append("")
    return "\n".join(lines)


def make_report(summary: list[tuple[ModuleSpec, dict[str, int]]]) -> str:
    lines = [
        "# Release modules report",
        "",
        f"- Source: `{RELEASE_MODULE.relative_to(ROOT).as_posix()}`",
        f"- Output directory: `{MODULES_DIR.relative_to(ROOT).as_posix()}`",
        f"- Generated modules: {len(summary)}",
        "",
    ]
    for spec, counts in summary:
        lines.append(f"## {spec.name}")
        if counts:
            for section, count in counts.items():
                lines.append(f"- {section}: {count}")
        else:
            lines.append("- No matching source lines")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    text = read(RELEASE_MODULE)
    if not text:
        raise SystemExit(f"missing release module: {RELEASE_MODULE}")
    _, sections = split_sections(text)
    summary: list[tuple[ModuleSpec, dict[str, int]]] = []
    for spec in SPECS:
        content, counts = module_text(spec, sections)
        write(MODULES_DIR / f"{spec.slug}.sgmodule", content)
        summary.append((spec, counts))
    write(MODULES_DIR / "README.md", make_index(summary))
    write(REPORT, make_report(summary))
    print(f"Built {len(summary)} per-app modules in {MODULES_DIR}")


if __name__ == "__main__":
    main()
