#!/usr/bin/env python3
"""Generate per-app module files.

Module definitions are read from the selected generator config [release_modules].
Each value uses this format:

slug = Display Name | keyword1, keyword2, keyword3

After configured modules are loaded, Rewrite/Sources/Apps/*.conf is scanned and
any unregistered source file is auto-discovered as a conservative release
module. This keeps app source files useful without forcing every low-risk
addition into the generator config by hand.

This script only writes Release/Modules outputs and its report. Cross-artifact
follow-up builds such as Android mirrors and Web catalogs are owned by
Rewrite/Generator/Builder.py so the release pipeline has a single scheduler.

If Rewrite/Sources/Apps/<slug>.conf exists, that app source file is used as the
module source. Otherwise the builder falls back to extracting matching lines from
Release/Ronghemokuai.sgmodule.
"""

from __future__ import annotations

import argparse
import configparser
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "Rewrite" / "Generate.conf"
RELEASE_MODULE = ROOT / "Release" / "Ronghemokuai.sgmodule"
DEFAULT_MODULES_DIR = ROOT / "Release" / "Modules"
DEFAULT_APP_SOURCES_DIR = ROOT / "Rewrite" / "Sources" / "Apps"
REPORT = ROOT / "reports" / "release_modules_report.md"
BASE_URL = "https://grandpaniuu.github.io/GrandpaNiu/Release/Modules"
SECTION_ORDER = ["Rule", "URL Rewrite", "Header Rewrite", "Body Rewrite", "Map Local", "Script", "MITM"]
AUTO_KEYWORDS = {
    "pinduoduo": ("pinduoduo", "yangkeduo", "pddpic", "pddcdn"),
    "jd": ("jd.com", "jdimg", "360buyimg"),
    "taobao": ("taobao", "tmall", "alicdn", "tbcdn", "taobaocdn", "mmstat"),
    "netease-music": ("music.163.com", "music.126.net", "netease"),
    "mgtv": ("mgtv", "bz.mgtv.com"),
    "huya": ("huya", "msstatic"),
    "yiche": ("yiche",),
    "pcauto": ("pcauto", "pconline"),
    "umetrip": ("umetrip", "variflight"),
    "xiaopeng": ("xiaopeng",),
    "youku": ("youku", "ykccn"),
    "quark": ("quark",),
    "meituan": ("meituan", "dianping", "sankuai"),
    "amap": ("amap",),
    "gaode": ("amap",),
    "wps": ("wps", "ksosoft"),
    "baidu": ("baidu", "bdimg"),
    "soul": ("soulapp",),
    "zdm": ("smzdm", "zdmimg"),
    "zuoyebang": ("zuoyebang",),
}


@dataclass(frozen=True)
class ModuleSpec:
    slug: str
    name: str
    keywords: tuple[str, ...]
    auto_discovered: bool = False


@dataclass(frozen=True)
class ModuleBuild:
    spec: ModuleSpec
    counts: dict[str, int]
    source: str


FALLBACK_SPECS = [
    ModuleSpec("spotify", "GrandpaNiu Spotify", ("spotify", "spclient", "scdn.co", "pscdn.co")),
    ModuleSpec("youtube", "GrandpaNiu YouTube", ("youtube", "youtu.be", "googlevideo", "ytimg", "maasea")),
    ModuleSpec("zhihu", "GrandpaNiu Zhihu", ("zhihu", "zhihu-enhance")),
]


def repo_path(path: str | Path) -> Path:
    p = Path(path)
    return p if p.is_absolute() else ROOT / p


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


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


def title_from_slug(slug: str) -> str:
    return " ".join(part.upper() if part in {"jd", "wps"} else part.capitalize() for part in slug.split("-"))


def name_from_source(path: Path, slug: str) -> str:
    for raw in read(path).splitlines():
        line = raw.strip()
        if line.startswith("#!name="):
            name = line.split("=", 1)[1].strip()
            if name:
                return name
    return f"GrandpaNiu {title_from_slug(slug)}"


def load_specs(cfg: configparser.ConfigParser, app_dir: Path) -> tuple[list[ModuleSpec], int, int]:
    if not cfg.has_section("release_modules"):
        return FALLBACK_SPECS, len(FALLBACK_SPECS), 0
    specs: list[ModuleSpec] = []
    for slug, value in cfg.items("release_modules"):
        spec = parse_spec(slug, value)
        if spec is not None:
            specs.append(spec)
    if not specs:
        return FALLBACK_SPECS, len(FALLBACK_SPECS), 0

    seen = {spec.slug for spec in specs}
    auto_count = 0
    if app_dir.exists():
        for path in sorted(app_dir.glob("*.conf")):
            slug = path.stem
            if slug in seen:
                continue
            keywords = AUTO_KEYWORDS.get(slug, (slug,))
            specs.append(ModuleSpec(slug, name_from_source(path, slug), tuple(keywords), True))
            seen.add(slug)
            auto_count += 1
    return specs, len(specs) - auto_count, auto_count


def output_dir(cfg: configparser.ConfigParser) -> Path:
    if cfg.has_option("output", "modules_dir"):
        return repo_path(cfg.get("output", "modules_dir"))
    return DEFAULT_MODULES_DIR


def app_sources_dir(cfg: configparser.ConfigParser) -> Path:
    if cfg.has_option("output", "app_sources_dir"):
        return repo_path(cfg.get("output", "app_sources_dir"))
    return DEFAULT_APP_SOURCES_DIR


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


def extract_sections(fusion_sections: dict[str, list[str]], spec: ModuleSpec) -> dict[str, list[str]]:
    selected: dict[str, list[str]] = {}
    for section in SECTION_ORDER:
        body = filter_mitm(fusion_sections[section], spec) if section == "MITM" else filter_regular_lines(fusion_sections[section], spec)
        if body:
            selected[section] = body
    return selected


def module_text(spec: ModuleSpec, sections: dict[str, list[str]]) -> tuple[str, dict[str, int]]:
    lines = [
        f"#!name={spec.name}",
        "#!desc=Generated per-app module from GrandpaNiu app source or fusion output",
        f"#!update-url={BASE_URL}/{spec.slug}.sgmodule",
    ]
    counts: dict[str, int] = {}
    for section in SECTION_ORDER:
        body = [line.strip() for line in sections.get(section, []) if active(line)]
        if not body:
            continue
        lines.extend(["", f"[{section}]", *body])
        counts[section] = len(body)
    lines.append("")
    return "\n".join(lines), counts


def source_sections(spec: ModuleSpec, app_dir: Path, fusion_sections: dict[str, list[str]]) -> tuple[dict[str, list[str]], str]:
    app_source = app_dir / f"{spec.slug}.conf"
    if app_source.exists():
        _, sections = split_sections(read(app_source))
        return sections, rel(app_source)
    return extract_sections(fusion_sections, spec), rel(RELEASE_MODULE)


def make_index(summary: list[ModuleBuild]) -> str:
    lines = [
        "# Release Modules",
        "",
        "Generated per-app module outputs. These are diagnostic and convenience slices of the single public fusion module, not separate product versions.",
        "",
        "| Module | File | Source | Sections |",
        "|---|---|---|---|",
    ]
    for item in summary:
        section_text = ", ".join(f"{name}:{count}" for name, count in item.counts.items()) or "empty"
        lines.append(f"| {item.spec.name} | `{item.spec.slug}.sgmodule` | `{item.source}` | {section_text} |")
    lines.append("")
    return "\n".join(lines)


def make_report(summary: list[ModuleBuild], manual_count: int, auto_count: int, skipped: list[tuple[ModuleSpec, str]], modules_dir: Path) -> str:
    auto_generated = sum(1 for item in summary if item.spec.auto_discovered)
    lines = [
        "# Release modules report",
        "",
        "- Public release strategy: single fusion module only",
        f"- Fusion fallback source: `{rel(RELEASE_MODULE)}`",
        f"- Output directory: `{rel(modules_dir)}`",
        f"- Manual modules: {manual_count}",
        f"- Auto-discovered modules: {auto_count}",
        f"- Auto-discovered generated modules: {auto_generated}",
        f"- Total module specs: {manual_count + auto_count}",
        f"- Generated modules: {len(summary)}",
        f"- Skipped empty modules: {len(skipped)}",
        "",
    ]
    for item in summary:
        lines.append(f"## {item.spec.name}")
        lines.append(f"- Source: `{item.source}`")
        lines.append(f"- Discovery: {'auto' if item.spec.auto_discovered else 'manual'}")
        for section, count in item.counts.items():
            lines.append(f"- {section}: {count}")
        lines.append("")
    if skipped:
        lines.append("## Skipped empty modules")
        for spec, source in skipped:
            lines.append(f"- {spec.name} (`{spec.slug}`) from `{source}`")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate configured per-app release modules.")
    parser.add_argument("--config", default=DEFAULT_CONFIG.relative_to(ROOT).as_posix(), help="Generation config path")
    args = parser.parse_args()

    cfg = load_config(repo_path(args.config))
    modules_dir = output_dir(cfg)
    app_dir = app_sources_dir(cfg)
    specs, manual_count, auto_count = load_specs(cfg, app_dir)
    include_empty = bool_cfg(cfg, "output", "include_empty_modules", False)

    text = read(RELEASE_MODULE)
    if not text:
        raise SystemExit(f"missing release module: {RELEASE_MODULE}")
    _, fusion_sections = split_sections(text)

    summary: list[ModuleBuild] = []
    skipped: list[tuple[ModuleSpec, str]] = []
    for spec in specs:
        sections, source = source_sections(spec, app_dir, fusion_sections)
        content, counts = module_text(spec, sections)
        if not counts and not include_empty:
            skipped.append((spec, source))
            continue
        write(modules_dir / f"{spec.slug}.sgmodule", content)
        summary.append(ModuleBuild(spec, counts, source))

    write(modules_dir / "README.md", make_index(summary))
    write(REPORT, make_report(summary, manual_count, auto_count, skipped, modules_dir))
    print(f"Built {len(summary)} per-app modules in {modules_dir}; skipped {len(skipped)} empty modules")


if __name__ == "__main__":
    main()
