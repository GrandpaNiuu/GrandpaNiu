#!/usr/bin/env python3
"""Generate compatibility aliases for Release artifacts."""

from __future__ import annotations

import argparse
import configparser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "Rewrite" / "Generator" / "Generate.conf"
LEGACY_CONFIG = ROOT / "Rewrite" / "Generate.conf"


def repo_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def load_config(path: Path) -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    cfg.optionxform = str
    if path.exists():
        cfg.read(path, encoding="utf-8")
    return cfg


def get_output(cfg: configparser.ConfigParser, key: str, fallback: str) -> Path:
    if cfg.has_option("output", key):
        return repo_path(cfg.get("output", key).strip())
    return repo_path(fallback)


def copy_text(src: Path, dst: Path) -> None:
    if not src.exists():
        raise SystemExit(f"missing source artifact: {src.relative_to(ROOT)}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
    print(f"wrote {dst.relative_to(ROOT)} from {src.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Release compatibility aliases.")
    parser.add_argument("--config", default=DEFAULT_CONFIG.relative_to(ROOT).as_posix() if DEFAULT_CONFIG.exists() else LEGACY_CONFIG.relative_to(ROOT).as_posix())
    args = parser.parse_args()

    cfg = load_config(repo_path(args.config))
    release = get_output(cfg, "release", "Release/Ronghemokuai.sgmodule")
    alias = get_output(cfg, "alias", "Release/Module.sgmodule")
    copy_text(release, alias)


if __name__ == "__main__":
    main()
