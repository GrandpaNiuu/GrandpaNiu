#!/usr/bin/env python3
"""Validate the module factory generation plan.

The preferred config is Rewrite/Generator/Generate.conf. Rewrite/Generate.conf is
kept as a legacy mirror for older commands and fallback behavior. This check
prevents the two files from drifting silently.
"""

from __future__ import annotations

import configparser
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFERRED = ROOT / "Rewrite" / "Generator" / "Generate.conf"
LEGACY = ROOT / "Rewrite" / "Generate.conf"

REQUIRED_SECTIONS = {
    "profile",
    "include",
    "rules",
    "scripts",
    "remotes",
    "misc_sources",
    "app_sources",
    "output",
    "builder",
    "checks",
    "release_modules",
    "channels",
    "safety",
}

# The legacy file is allowed to omit the self-check entry so that older copies
# can still be read as a fallback. All other parsed values must match.
LEGACY_OPTION_EXCEPTIONS = {("checks", "validate_generator_config")}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_config(path: Path) -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    cfg.optionxform = str
    if not path.exists():
        raise FileNotFoundError(rel(path))
    cfg.read(path, encoding="utf-8")
    return cfg


def section_items(cfg: configparser.ConfigParser, section: str) -> dict[str, str]:
    if not cfg.has_section(section):
        return {}
    return {key: value.strip() for key, value in cfg.items(section)}


def comparable_items(cfg: configparser.ConfigParser, section: str) -> dict[str, str]:
    return {
        key: value
        for key, value in section_items(cfg, section).items()
        if (section, key) not in LEGACY_OPTION_EXCEPTIONS
    }


def script_values(cfg: configparser.ConfigParser) -> list[str]:
    values: list[str] = []
    for section in ("builder", "checks"):
        for value in section_items(cfg, section).values():
            item = value.strip()
            if item.endswith(".py") or ".py " in item:
                values.append(item.split()[0])
    return values


def validate_required_sections(cfg: configparser.ConfigParser) -> list[str]:
    present = set(cfg.sections())
    return sorted(REQUIRED_SECTIONS - present)


def validate_mirror(preferred: configparser.ConfigParser, legacy: configparser.ConfigParser) -> list[str]:
    errors: list[str] = []
    preferred_sections = set(preferred.sections())
    legacy_sections = set(legacy.sections())

    for section in sorted(preferred_sections - legacy_sections):
        errors.append(f"legacy config missing section [{section}]")
    for section in sorted(legacy_sections - preferred_sections):
        errors.append(f"legacy config has extra section [{section}]")

    for section in sorted(preferred_sections & legacy_sections):
        preferred_items = comparable_items(preferred, section)
        legacy_items = comparable_items(legacy, section)
        for key in sorted(preferred_items.keys() - legacy_items.keys()):
            errors.append(f"legacy config missing option [{section}] {key}")
        for key in sorted(legacy_items.keys() - preferred_items.keys()):
            errors.append(f"legacy config has extra option [{section}] {key}")
        for key in sorted(preferred_items.keys() & legacy_items.keys()):
            if preferred_items[key] != legacy_items[key]:
                errors.append(f"config mismatch [{section}] {key}: {preferred_items[key]!r} != {legacy_items[key]!r}")
    return errors


def validate_script_paths(cfg: configparser.ConfigParser) -> list[str]:
    errors: list[str] = []
    for value in sorted(set(script_values(cfg))):
        path = ROOT / value
        if not path.exists():
            errors.append(f"missing configured script: {value}")
    return errors


def main() -> int:
    try:
        preferred = read_config(PREFERRED)
        legacy = read_config(LEGACY)
    except FileNotFoundError as exc:
        print(f"ERROR: missing config file: {exc}", file=sys.stderr)
        return 1

    errors: list[str] = []
    missing = validate_required_sections(preferred)
    for section in missing:
        errors.append(f"preferred config missing required section [{section}]")

    errors.extend(validate_mirror(preferred, legacy))
    errors.extend(validate_script_paths(preferred))

    if errors:
        print("Generator config validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Generator config validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
