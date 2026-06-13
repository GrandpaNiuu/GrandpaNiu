#!/usr/bin/env python3
"""Publish Android rule outputs into Release/Android.

The Android source layer remains under Android/. This script mirrors the stable
Android output directories into Release/Android so Release/ is the complete
published artifact layer.
"""

from __future__ import annotations

import argparse
import configparser
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "Rewrite" / "Generate.conf"
ANDROID_ROOT = ROOT / "Android"
REPORT = ROOT / "reports" / "release_android_report.md"
PUBLISH_DIRS = ["mihomo", "sing-box", "adguard", "v2rayng"]
PUBLISH_FILES = ["branches.json"]


def repo_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_config(path: Path) -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    cfg.optionxform = str
    if path.exists():
        cfg.read(path, encoding="utf-8")
    return cfg


def release_android_dir(cfg: configparser.ConfigParser) -> Path:
    if cfg.has_option("output", "android_dir"):
        return repo_path(cfg.get("output", "android_dir"))
    return ROOT / "Release" / "Android"


def copy_tree(src: Path, dst: Path) -> list[Path]:
    copied: list[Path] = []
    if not src.exists():
        return copied
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    copied.extend(path for path in dst.rglob("*") if path.is_file())
    return copied


def build_readme(out_dir: Path, copied: dict[str, list[Path]]) -> str:
    lines = [
        "# Release Android",
        "",
        "Generated Android rule outputs mirrored from `Android/`.",
        "",
        "## Published formats",
        "",
        "| Format | Directory | Files |",
        "|---|---|---:|",
    ]
    for name in PUBLISH_DIRS:
        files = copied.get(name, [])
        lines.append(f"| {name} | `{rel(out_dir / name)}` | {len(files)} |")
    lines.extend([
        "",
        "## Synced rule branches",
        "",
        "- `mihomo`, `sing-box`, `adguard`, and `v2rayng` are generated from the same Android source layer.",
        "- `branches.json` records the synchronized public targets and rule counts.",
        "- AdGuard is the DNS-compatible projection of the same source because AdGuard text filters cannot represent every IP/routing rule.",
        "",
        "## Source of truth",
        "",
        "- Editable Android sources remain under `Android/`.",
        "- Published Android release files are generated into `Release/Android/`.",
        "- Do not edit this directory first; regenerate it through `Rewrite/Generator/Builder.py --release`.",
        "",
    ])
    return "\n".join(lines)


def build_report(out_dir: Path, copied: dict[str, list[Path]]) -> str:
    lines = [
        "# Release Android report",
        "",
        f"- Output directory: `{rel(out_dir)}`",
        f"- Published formats: {len(copied)}",
        "",
        "| Format | Files |",
        "|---|---:|",
    ]
    for name in PUBLISH_DIRS:
        lines.append(f"| {name} | {len(copied.get(name, []))} |")
    lines.extend([
        "",
        "## Branch sync",
        "",
        "- Branch manifest: `Release/Android/branches.json`",
        "- Mihomo, sing-box and v2rayNG are full projections of the canonical Android rules.",
        "- AdGuard is the DNS-compatible projection of the same source.",
    ])
    lines.append("")
    return "\n".join(lines)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish Android outputs under Release/Android.")
    parser.add_argument("--config", default=rel(DEFAULT_CONFIG), help="Generation config path")
    args = parser.parse_args()

    cfg = read_config(repo_path(args.config))
    out_dir = release_android_dir(cfg)
    out_dir.mkdir(parents=True, exist_ok=True)

    copied: dict[str, list[Path]] = {}
    for name in PUBLISH_DIRS:
        copied[name] = copy_tree(ANDROID_ROOT / name, out_dir / name)
    for name in PUBLISH_FILES:
        src = ANDROID_ROOT / name
        if src.exists():
            shutil.copy2(src, out_dir / name)

    write(out_dir / "README.md", build_readme(out_dir, copied))
    write(REPORT, build_report(out_dir, copied))
    print(f"Published Android release outputs to {out_dir}")


if __name__ == "__main__":
    main()
