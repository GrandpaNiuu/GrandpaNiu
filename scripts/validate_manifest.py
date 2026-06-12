#!/usr/bin/env python3
"""Validate Rewrite/Manifest.conf file references and factory structure."""

from __future__ import annotations

import configparser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "Rewrite" / "Manifest.conf"
REQUIRED_SECTIONS = [
    "module",
    "generator",
    "sections",
    "rules",
    "scripts",
    "mitm",
    "app_sources",
    "remote_sources",
    "release",
    "web",
    "registry",
    "safety",
]
OPTIONAL_MISSING_OUTPUTS = {
    "Release/Module.sgmodule",
    "Web/modules.html",
}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_manifest() -> configparser.ConfigParser:
    if not MANIFEST.exists():
        raise SystemExit("ERROR: missing Rewrite/Manifest.conf")
    cfg = configparser.ConfigParser()
    cfg.optionxform = str
    cfg.read(MANIFEST, encoding="utf-8")
    return cfg


def looks_like_path(value: str) -> bool:
    if "://" in value:
        return False
    if value.lower() in {"true", "false", "yes", "no", "fusion", "grandpaniu fusion", "融合模块"}:
        return False
    return any(token in value for token in ("/", ".conf", ".py", ".json", ".md", ".html", ".sgmodule", ".list", ".txt"))


def validate_sections(cfg: configparser.ConfigParser) -> list[str]:
    errors: list[str] = []
    for section in REQUIRED_SECTIONS:
        if not cfg.has_section(section):
            errors.append(f"missing section [{section}]")
    return errors


def validate_paths(cfg: configparser.ConfigParser) -> list[str]:
    errors: list[str] = []
    for section in cfg.sections():
        for key, value in cfg.items(section):
            path_value = value.strip()
            if not looks_like_path(path_value):
                continue
            path = ROOT / path_value
            if path.exists():
                continue
            if path_value in OPTIONAL_MISSING_OUTPUTS:
                continue
            errors.append(f"missing path [{section}] {key} = {path_value}")
    return errors


def validate_app_template(cfg: configparser.ConfigParser) -> list[str]:
    errors: list[str] = []
    template_value = cfg.get("app_sources", "template", fallback="Rewrite/Sources/Apps/_TEMPLATE.conf")
    template = ROOT / template_value
    if not template.exists():
        errors.append(f"missing app source template: {template_value}")
    return errors


def main() -> None:
    cfg = load_manifest()
    errors = []
    errors.extend(validate_sections(cfg))
    errors.extend(validate_paths(cfg))
    errors.extend(validate_app_template(cfg))

    if errors:
        print("Manifest validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print(f"Manifest validation passed: {rel(MANIFEST)}")


if __name__ == "__main__":
    main()
