#!/usr/bin/env python3
"""Unified entry point for the GrandpaNiu module factory.

The generator prefers the complete Rewrite/Generator/Generate.conf plan, then
falls back to the legacy Rewrite/Generate.conf mirror. Existing scripts remain
the implementation layer; this file is the stable factory entrypoint.
"""

from __future__ import annotations

import argparse
import configparser
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PYTHON = sys.executable
GENERATOR_CONFIG = ROOT / "Rewrite" / "Generator" / "Generate.conf"
LEGACY_CONFIG = ROOT / "Rewrite" / "Generate.conf"
DEFAULT_CONFIG = GENERATOR_CONFIG if GENERATOR_CONFIG.exists() else LEGACY_CONFIG


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def config_path(value: str | None) -> Path:
    if not value:
        return DEFAULT_CONFIG
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def load_config(path: Path) -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    cfg.optionxform = str
    if path.exists():
        cfg.read(path, encoding="utf-8")
    return cfg


def get_cfg(cfg: configparser.ConfigParser, section: str, key: str, fallback: str) -> str:
    if cfg.has_option(section, key):
        return cfg.get(section, key).strip()
    return fallback


def command(script: str, *args: str) -> list[str]:
    return [PYTHON, str(ROOT / script), *args]


def existing_command(script: str, *args: str) -> list[str] | None:
    path = ROOT / script
    if not path.exists():
        print(f"skip missing script: {script}")
        return None
    return command(script, *args)


def print_command(cmd: list[str]) -> None:
    printable = [cmd[0], rel(Path(cmd[1])), *cmd[2:]]
    print("$ " + " ".join(printable))


def run(cmd: list[str], dry_run: bool) -> None:
    print_command(cmd)
    if dry_run:
        return
    subprocess.run(cmd, cwd=ROOT, check=True)


def script_value_items(cfg: configparser.ConfigParser, section: str) -> list[str]:
    if not cfg.has_section(section):
        return []
    scripts: list[str] = []
    for _, value in cfg.items(section):
        item = value.strip()
        if item.endswith(".py") or ".py " in item:
            scripts.append(item)
    return scripts


def build_plan(cfg: configparser.ConfigParser, profile: str, release: bool, check: bool, config_file: Path) -> list[list[str]]:
    build_script = get_cfg(cfg, "builder", "build_script", "scripts/build_module.py")
    finalize_script = get_cfg(cfg, "builder", "finalize_script", "scripts/factory_finalize.py")
    release_report_script = get_cfg(cfg, "builder", "release_report_script", "scripts/build_release_variants.py")
    release_rules_script = get_cfg(cfg, "builder", "release_rules_script", "scripts/build_release_rules.py")
    release_modules_script = get_cfg(cfg, "builder", "release_modules_script", "scripts/build_release_modules.py")
    release_aliases_script = get_cfg(cfg, "builder", "release_aliases_script", "scripts/build_release_aliases.py")
    release_channels_script = get_cfg(cfg, "builder", "release_channels_script", "scripts/build_channels.py")
    release_android_script = get_cfg(cfg, "builder", "release_android_script", "scripts/build_release_android.py")
    web_modules_script = get_cfg(cfg, "builder", "web_modules_script", "scripts/build_web_modules.py")
    web_catalog_script = get_cfg(cfg, "builder", "web_catalog_script", "scripts/build_web_catalog.py")
    release_checksums_script = get_cfg(cfg, "builder", "release_checksums_script", "scripts/build_checksums.py")
    release_summary_script = get_cfg(cfg, "builder", "release_summary_script", "scripts/build_release_summary.py")

    steps: list[list[str]] = [
        command(build_script, "--build", "--profile", profile),
    ]

    if release:
        release_steps: list[list[str] | None] = [
            existing_command(finalize_script, "--sync-root"),
            existing_command(release_report_script),
            existing_command(release_rules_script),
            existing_command(release_modules_script, "--config", rel(config_file)),
            existing_command(release_aliases_script, "--config", rel(config_file)),
            existing_command(release_channels_script, "--config", rel(config_file)),
            existing_command(release_android_script, "--config", rel(config_file)),
            existing_command(web_modules_script),
            existing_command(web_catalog_script),
            existing_command(release_checksums_script),
            existing_command(release_summary_script),
        ]
        steps.extend(step for step in release_steps if step is not None)

    if check:
        for script in script_value_items(cfg, "checks"):
            step = existing_command(script)
            if step is not None:
                steps.append(step)

    return steps


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the GrandpaNiu module factory pipeline.")
    parser.add_argument("--config", default=rel(DEFAULT_CONFIG), help="Generation config path. Default: Rewrite/Generator/Generate.conf")
    parser.add_argument("--profile", default=None, help="Profile name under Rewrite/Profiles. Defaults to [profile] active")
    parser.add_argument("--release", action="store_true", help="Finalize Release output and generate release artifacts")
    parser.add_argument("--check", action="store_true", help="Run validation scripts listed in the config")
    parser.add_argument("--dry-run", action="store_true", help="Print commands without executing them")
    args = parser.parse_args()

    cfg_path = config_path(args.config)
    cfg = load_config(cfg_path)
    profile = args.profile or get_cfg(cfg, "profile", "active", "fusion")

    for step in build_plan(cfg, profile, args.release, args.check, cfg_path):
        run(step, args.dry_run)


if __name__ == "__main__":
    main()
