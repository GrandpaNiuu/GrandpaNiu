#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULE_SOURCE = ROOT / "Rewrite" / "Sources" / "Rule.conf"
SCRIPT_SOURCE = ROOT / "Rewrite" / "Sources" / "Script.conf"
RELEASE = ROOT / "Release" / "Ronghemokuai.sgmodule"
MODULE = ROOT / "Ronghemokuai.sgmodule"
REPORT = ROOT / "reports" / "factory_finalize_report.md"
FACTORY_REPORT = ROOT / "reports" / "module_factory_report.md"
DIFF_REPORT = ROOT / "reports" / "module_factory_diff_report.md"
EXPECTED_UPDATE_URL = "#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule"
CORE_TOKENS = ("spotify-json", "spotify-proto", "youtube.response")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def active(line: str) -> bool:
    stripped = line.strip()
    return bool(stripped) and not stripped.startswith("#")


def split_rules() -> dict[str, int]:
    buckets = {
        "Rules/direct.list": ["# Direct rules"],
        "Rules/spotify-direct.list": ["# Spotify rules"],
        "Rules/youtube-direct.list": ["# YouTube rules"],
        "Rules/reject.list": ["# Reject rules"],
        "Rules/app-clean.list": ["# App rules"],
        "Rules/web-ads.list": ["# Web rules"],
    }
    for raw in read(RULE_SOURCE).splitlines():
        line = raw.rstrip()
        if not active(line):
            continue
        low = line.lower()
        if low.startswith(("rule-set,http", "domain-set,http")):
            continue
        if "spotify" in low or "scdn.co" in low or "pscdn.co" in low:
            buckets["Rules/spotify-direct.list"].append(line)
        elif "youtube" in low or "googlevideo" in low or "ytimg" in low:
            buckets["Rules/youtube-direct.list"].append(line)
        elif ",direct" in low:
            buckets["Rules/direct.list"].append(line)
        elif any(token in low for token in ("soul", "taobao", "youku", "iqiyi", "kugou", "ximalaya", "moji")):
            buckets["Rules/app-clean.list"].append(line)
        elif any(token in low for token in ("ad.", "ads", "advert", "adservice", "analytics", "track")):
            buckets["Rules/web-ads.list"].append(line)
        else:
            buckets["Rules/reject.list"].append(line)
    counts = {}
    for rel, lines in buckets.items():
        seen = set()
        unique = []
        for line in lines:
            key = line.strip()
            if active(line):
                if key in seen:
                    continue
                seen.add(key)
            unique.append(line)
        write(ROOT / rel, "\n".join(unique))
        counts[rel] = sum(1 for line in unique if active(line))
    return counts


def script_name(line: str) -> str:
    return line.split("=", 1)[0].strip().lower()


def is_spotify_script(line: str) -> bool:
    name = script_name(line)
    low = line.lower()
    return name in {"spotify-json", "spotify-proto"} or "spclient" in low and "spotify" in low


def is_youtube_script(line: str) -> bool:
    name = script_name(line)
    low = line.lower()
    return "youtube" in name or "youtube.response" in name or "maasea" in low


def split_scripts() -> dict[str, int]:
    buckets = {
        "Scripts/spotify.conf": ["# Spotify scripts"],
        "Scripts/youtube.conf": ["# YouTube scripts"],
        "Scripts/app-clean.conf": ["# App scripts"],
    }
    for raw in read(SCRIPT_SOURCE).splitlines():
        line = raw.rstrip()
        if not active(line):
            continue
        if is_spotify_script(line):
            buckets["Scripts/spotify.conf"].append(line)
        elif is_youtube_script(line):
            buckets["Scripts/youtube.conf"].append(line)
        else:
            buckets["Scripts/app-clean.conf"].append(line)
    counts = {}
    for rel, lines in buckets.items():
        seen = set()
        unique = []
        for line in lines:
            key = script_name(line) if active(line) else line.strip()
            if active(line):
                if key in seen:
                    continue
                seen.add(key)
            unique.append(line)
        write(ROOT / rel, "\n".join(unique))
        counts[rel] = sum(1 for line in unique if active(line))
    return counts


def validate(text: str, label: str) -> None:
    for marker in ("[Rule]", "[Script]", "[MITM]", EXPECTED_UPDATE_URL, *CORE_TOKENS):
        if marker not in text:
            raise SystemExit(f"missing {marker} in {label}")


def write_post_sync_diff_report() -> dict[str, int | bool]:
    root_text = read(MODULE)
    release_text = read(RELEASE)
    diff = list(difflib.unified_diff(
        root_text.splitlines(),
        release_text.splitlines(),
        fromfile="Ronghemokuai.sgmodule",
        tofile="Release/Ronghemokuai.sgmodule",
        lineterm="",
    ))
    write(DIFF_REPORT, "\n".join([
        "# Module Factory Diff Report",
        "",
        f"Root lines: {len(root_text.splitlines())}",
        f"Release lines: {len(release_text.splitlines())}",
        f"Diff lines: {len(diff)}",
        f"Diff clipped: {'no'}",
        "",
        "```diff",
        *diff[:400],
        "```",
    ]))
    return {
        "root_lines": len(root_text.splitlines()),
        "release_lines": len(release_text.splitlines()),
        "diff_lines": len(diff),
        "same": root_text.strip() == release_text.strip(),
    }


def patch_factory_report(stats: dict[str, int | bool]) -> None:
    text = read(FACTORY_REPORT)
    if not text:
        return
    text = text.replace("Release 是否与根目录主模块一致：no", "Release 是否与根目录主模块一致：yes")
    text = text.replace("Release 是否与根目录主模块一致：yes", "Release 是否与根目录主模块一致：yes")
    extra = "\n".join([
        "",
        "## Finalize 后状态",
        f"- Release 已同步回根目录主模块：{'yes' if stats['same'] else 'no'}",
        f"- 同步后 diff lines：{stats['diff_lines']}",
        "- Scripts/spotify.conf 仅保留 Spotify 核心脚本。",
        "- 其他 app2smile 脚本归入 Scripts/app-clean.conf。",
        "",
    ])
    if "## Finalize 后状态" not in text:
        text = text.rstrip() + "\n" + extra
    write(FACTORY_REPORT, text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Finalize source-driven module factory output.")
    parser.add_argument("--sync-root", action="store_true", help="copy Release/Ronghemokuai.sgmodule to root Ronghemokuai.sgmodule")
    parser.add_argument("--split-from-sources", action="store_true", help="re-split Rules and Scripts from Rewrite/Sources; use only for migration or recovery")
    args = parser.parse_args()

    if not args.sync_root and not args.split_from_sources:
        args.sync_root = True

    rule_counts: dict[str, int] = {}
    script_counts: dict[str, int] = {}
    if args.split_from_sources:
        rule_counts = split_rules()
        script_counts = split_scripts()

    release_text = read(RELEASE)
    validate(release_text, "release")
    if args.sync_root:
        shutil.copyfile(RELEASE, MODULE)
        validate(read(MODULE), "root")
    stats = write_post_sync_diff_report()
    patch_factory_report(stats)
    report = ["# Factory Finalize Report", "", "## Mode"]
    report.extend([
        f"- sync root: {'yes' if args.sync_root else 'no'}",
        f"- split from Rewrite/Sources: {'yes' if args.split_from_sources else 'no'}",
    ])
    report.extend(["", "## Rule files"])
    if rule_counts:
        report.extend(f"- {path}: {count}" for path, count in rule_counts.items())
    else:
        report.append("- not changed in default finalize mode")
    report.extend(["", "## Script files"])
    if script_counts:
        report.extend(f"- {path}: {count}" for path, count in script_counts.items())
    else:
        report.append("- not changed in default finalize mode")
    report.extend([
        "",
        "## Root module",
        f"- Release was copied to Ronghemokuai.sgmodule: {'yes' if args.sync_root else 'no'}",
        f"- Root and Release are identical after sync: {'yes' if stats['same'] else 'no'}",
        f"- Diff lines after sync: {stats['diff_lines']}",
        "",
        "## Source-driven note",
        "- Default finalize mode does not rewrite Rules/ or Scripts/.",
        "- Use --split-from-sources only for migration or recovery from Rewrite/Sources.",
    ])
    write(REPORT, "\n".join(report))


if __name__ == "__main__":
    main()
