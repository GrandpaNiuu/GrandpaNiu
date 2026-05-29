#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULE_SOURCE = ROOT / "Rewrite" / "Sources" / "Rule.conf"
SCRIPT_SOURCE = ROOT / "Rewrite" / "Sources" / "Script.conf"
RELEASE = ROOT / "Release" / "Ronghemokuai.sgmodule"
MODULE = ROOT / "Ronghemokuai.sgmodule"
REPORT = ROOT / "reports" / "factory_finalize_report.md"
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
        low = line.lower()
        name = low.split("=", 1)[0]
        if "spotify" in name or "app2smile" in low:
            buckets["Scripts/spotify.conf"].append(line)
        elif "youtube" in name or "maasea" in low:
            buckets["Scripts/youtube.conf"].append(line)
        else:
            buckets["Scripts/app-clean.conf"].append(line)
    counts = {}
    for rel, lines in buckets.items():
        write(ROOT / rel, "\n".join(lines))
        counts[rel] = sum(1 for line in lines if active(line))
    return counts


def validate(text: str, label: str) -> None:
    for marker in ("[Rule]", "[Script]", "[MITM]", EXPECTED_UPDATE_URL, *CORE_TOKENS):
        if marker not in text:
            raise SystemExit(f"missing {marker} in {label}")


def main() -> None:
    rule_counts = split_rules()
    script_counts = split_scripts()
    release_text = read(RELEASE)
    validate(release_text, "release")
    shutil.copyfile(RELEASE, MODULE)
    validate(read(MODULE), "root")
    report = ["# Factory Finalize Report", "", "## Rule files"]
    report.extend(f"- {path}: {count}" for path, count in rule_counts.items())
    report.extend(["", "## Script files"])
    report.extend(f"- {path}: {count}" for path, count in script_counts.items())
    report.extend(["", "## Root module", "- Release was copied to Ronghemokuai.sgmodule."])
    write(REPORT, "\n".join(report))


if __name__ == "__main__":
    main()
