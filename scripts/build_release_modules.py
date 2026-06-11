#!/usr/bin/env python3
"""Generate per-app module files from the built fusion module.

Module definitions are read from Rewrite/Generate.conf [release_modules].
Each value uses this format:

slug = Display Name | keyword1, keyword2, keyword3
"""

from __future__ import annotations

import argparse
import configparser
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "Rewrite" / "Generate.conf"
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


FALLBACK_SPECS = [
    ModuleSpec("spotify", "GrandpaNiu Spotify", ("spotify", "spclient", "scdn.co", "pscdn.co")),
    ModuleSpec("youtube", "GrandpaNiu YouTube", ("youtube", "youtu.be", "googlevideo", "ytimg", "maasea")),
    ModuleSpec("zhihu", "GrandpaNiu Zhihu", ("zhihu", "zhihu-enhance")),
]


def repo_path(path: str | Path) -> Path:
    p = Path(path)
    return p if p.is_absolute() else ROOT / p


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def load_config(path: Path) -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    cfg.optionxform = str
    if path.exists():
        cfg.read(path, encoding="utf-8")
    return cfg


def bool_cfg(cfg: configparser.ConfigParser, section: str, key: str, default: bool = False) -> bool:
    if cfg.has_option(section, key):
        return cfg.getboolean(section, key)
    return default


def parse_spec(slug: str, value: str) -> ModuleSpec | None:
    if "|" not in value:
        return None
    name, raw_keywords = value.split("|", 1)
    keywords = tuple(item.strip() for item in raw_keywords.split(",") if item.strip())
    if not keywords:
        return None
    return ModuleSpec(slug.strip(), name.strip(), keywords)


def load_specs(cfg: configparser.ConfigParser) -> list[ModuleSpec]:
    if not cfg.has_section("release_modules"):
        return FALLBACK_SPECS
    specs: list[ModuleSpec] = []
    for slug, value in cfg.items("release_modules"):
        spec = parse_spec(slug, value)
        if spec is not None:
            specs.append(spec)
    return specs or FALLBACK_SPECS


def output_dir(cfg: configparser.ConfigParser) -> Path:
    if cfg.has_option("output", "modules_dir"):
        return repo_path(cfg.get("output", "modules_dir"))
    return MODULES_DIR


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
    lines = [
        f"#!name={spec.name}",
        "#!desc=Generated per-app module from GrandpaNiu fusion output",
        f"#!update-url={BASE_URL}/{spec.slug}.sgmodule",
    ]
    counts: dict[str, int] = {}
    for section in SECTION_ORDER:
        body = filter_mitm(sections[section], spec) if section == "MITM" else filter_regular_lines(sections[section], spec)
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


def make_report(summary: list[tuple[ModuleSpec, dict[str, int]]], configured: int, skipped: list[ModuleSpec], modules_dir: Path) -> str:
    lines = [
        "# Release modules report",
        "",
        f"- Source: `{RELEASE_MODULE.relative_to(ROOT).as_posix()}`",
        f"- Output directory: `{modules_dir.relative_to(ROOT).as_posix()}`",
        f"- Configured modules: {configured}",
        f"- Generated modules: {len(summary)}",
        f"- Skipped empty modules: {len(skipped)}",
        "",
    ]
    for spec, counts in summary:
        lines.append(f"## {spec.name}")
        for section, count in counts.items():
            lines.append(f"- {section}: {count}")
        lines.append("")
    if skipped:
        lines.append("## Skipped empty modules")
        for spec in skipped:
            lines.append(f"- {spec.name} (`{spec.slug}`)")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate configured per-app release modules.")
    parser.add_argument("--config", default=DEFAULT_CONFIG.relative_to(ROOT).as_posix(), help="Generation config path")
    args = parser.parse_args()

    cfg = load_config(repo_path(args.config))
    specs = load_specs(cfg)
    modules_dir = output_dir(cfg)
    include_empty = bool_cfg(cfg, "output", "include_empty_modules", False)

    text = read(RELEASE_MODULE)
    if not text:
        raise SystemExit(f"missing release module: {RELEASE_MODULE}")
    _, sections = split_sections(text)

    summary: list[tuple[ModuleSpec, dict[str, int]]] = []
    skipped: list[ModuleSpec] = []
    for spec in specs:
        content, counts = module_text(spec, sections)
        if not counts and not include_empty:
            skipped.append(spec)
            continue
        write(modules_dir / f"{spec.slug}.sgmodule", content)
        summary.append((spec, counts))

    write(modules_dir / "README.md", make_index(summary))
    write(REPORT, make_report(summary, len(specs), skipped, modules_dir))
    print(f"Built {len(summary)} per-app modules in {modules_dir}; skipped {len(skipped)} empty modules")


if __name__ == "__main__":
    main()
