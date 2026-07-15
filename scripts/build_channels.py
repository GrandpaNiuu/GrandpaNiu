#!/usr/bin/env python3
"""Build legacy compatibility channel directories.

Fusion remains the only public release strategy. Stable mirrors the current
Fusion artifacts for old links only; Beta and Canary remain empty placeholders.
"""

from __future__ import annotations

import argparse
import configparser
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATOR_CONFIG = ROOT / "Rewrite" / "Generator" / "Generate.conf"
LEGACY_CONFIG = ROOT / "Rewrite" / "Generate.conf"


@dataclass(frozen=True)
class Channel:
    name: str
    directory: Path
    enabled: bool
    description: str


def repo_path(value: str) -> Path:
    path = Path(value.strip())
    return path if path.is_absolute() else ROOT / path


def load_config(path: Path) -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    cfg.optionxform = str
    if path.exists():
        cfg.read(path, encoding="utf-8")
    return cfg


def get_output(cfg: configparser.ConfigParser, key: str, fallback: str) -> Path:
    if cfg.has_option("output", key):
        return repo_path(cfg.get("output", key))
    return repo_path(fallback)


def parse_bool(value: str, default: bool = False) -> bool:
    if value == "":
        return default
    return value.strip().lower() in {"1", "true", "yes", "on", "enabled"}


def default_channels() -> list[Channel]:
    return [
        Channel("Stable", ROOT / "Release" / "Stable", True, "Deprecated compatibility mirror of the current Fusion release; not a public version choice."),
        Channel("Beta", ROOT / "Release" / "Beta", False, "Reserved channel for less conservative builds."),
        Channel("Canary", ROOT / "Release" / "Canary", False, "Reserved channel for high-risk experimental builds."),
    ]


def load_channels(cfg: configparser.ConfigParser) -> list[Channel]:
    if not cfg.has_section("channels"):
        return default_channels()
    channels: list[Channel] = []
    for name, raw in cfg.items("channels"):
        parts = [part.strip() for part in raw.split("|", 2)]
        if len(parts) < 2:
            continue
        directory = repo_path(parts[0])
        enabled = parse_bool(parts[1])
        description = parts[2] if len(parts) > 2 else "Release channel."
        channels.append(Channel(name.title(), directory, enabled, description))
    return channels or default_channels()


def copy_if_exists(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(src.read_text(encoding="utf-8", errors="replace"), encoding="utf-8", newline="\n")
    return True


def channel_status(channel: Channel) -> str:
    if channel.enabled and channel.name.lower() == "stable":
        return "legacy-compatible"
    return "enabled" if channel.enabled else "reserved"


def write_channel_readme(channel: Channel, copied: list[str]) -> None:
    channel.directory.mkdir(parents=True, exist_ok=True)
    status = channel_status(channel)
    lines = [
        f"# {channel.name} Channel",
        "",
        channel.description,
        "",
        f"- Status: `{status}`",
    ]
    if copied:
        lines.append(f"- Artifacts: {', '.join(f'`{item}`' for item in copied)}")
    else:
        lines.append("- Artifacts: not generated for this channel yet.")
    lines.append("")
    (channel.directory / "README.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Release channel directories.")
    parser.add_argument("--config", default=GENERATOR_CONFIG.relative_to(ROOT).as_posix() if GENERATOR_CONFIG.exists() else LEGACY_CONFIG.relative_to(ROOT).as_posix())
    args = parser.parse_args()

    cfg = load_config(repo_path(args.config))
    release_module = get_output(cfg, "release", "Release/Ronghemokuai.sgmodule")
    release_alias = get_output(cfg, "alias", "Release/Module.sgmodule")
    rules = get_output(cfg, "rules", "Release/Rules.conf")
    rules_group = get_output(cfg, "rules_group", "Release/RulesGroup.conf")

    for channel in load_channels(cfg):
        copied: list[str] = []
        if channel.enabled:
            for src, filename in [
                (release_module, "Ronghemokuai.sgmodule"),
                (release_alias if release_alias.exists() else release_module, "Module.sgmodule"),
                (rules, "Rules.conf"),
                (rules_group, "RulesGroup.conf"),
            ]:
                if copy_if_exists(src, channel.directory / filename):
                    copied.append(filename)
        write_channel_readme(channel, copied)
        print(f"wrote {channel.directory.relative_to(ROOT)} ({channel_status(channel)})")


if __name__ == "__main__":
    main()
