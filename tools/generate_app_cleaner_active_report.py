#!/usr/bin/env python3
"""Generate an app-cleaner active entry maintenance report."""

from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT / "Scripts" / "app-cleaner-active.conf"
CLEANER = ROOT / "Scripts" / "app-cleaner.js"
CONFIG = ROOT / "Scripts" / "app-cleaner.config.json"
REPORT = ROOT / "reports" / "app_cleaner_active_report.md"
SCRIPT_ENTRY_RE = re.compile(r"^\s*([^#\s][^=]+?)\s*=\s*(.+)$")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def field(body: str, name: str) -> str:
    match = re.search(rf"{re.escape(name)}=([^,]+)", body)
    return match.group(1).strip() if match else ""


def pattern_alternatives(pattern: str) -> int:
    if not pattern:
        return 0
    return pattern.count("|") + 1


def cleaner_version(text: str) -> str:
    match = re.search(r'const\s+VERSION\s*=\s*"([^"]+)"', text)
    return match.group(1) if match else "unknown"


def config_summary() -> tuple[str, int, str]:
    if not CONFIG.exists():
        return "missing", 0, ""
    try:
        data = json.loads(read(CONFIG))
    except json.JSONDecodeError:
        return "invalid", 0, ""
    groups = data.get("groups", [])
    safety = data.get("safety", {})
    mode = str(data.get("mode", ""))
    default_action = str(safety.get("defaultAction", ""))
    return mode or "unknown", len(groups) if isinstance(groups, list) else 0, default_action


def main() -> None:
    active_text = read(ACTIVE)
    cleaner_text = read(CLEANER)
    entries = []
    for line in active_text.splitlines():
        match = SCRIPT_ENTRY_RE.match(line)
        if not match:
            continue
        name, body = match.group(1).strip(), match.group(2).strip()
        entries.append({
            "name": name,
            "type": field(body, "type"),
            "requires_body": field(body, "requires-body"),
            "script_path": field(body, "script-path"),
            "pattern": field(body, "pattern"),
        })
    mode, groups, default_action = config_summary()
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# App Cleaner Active Report",
        "",
        f"- Generated at: {now}",
        f"- Active entry file: `{ACTIVE.relative_to(ROOT).as_posix()}`",
        f"- Cleaner script: `{CLEANER.relative_to(ROOT).as_posix()}`",
        f"- Cleaner version: `{cleaner_version(cleaner_text)}`",
        f"- Config mode: `{mode}`",
        f"- Config groups: {groups}",
        f"- Default action: `{default_action or 'pass-through by script guard'}`",
        f"- Active entries: {len(entries)}",
        "",
        "## Active Entries",
        "",
        "| Name | Type | Requires body | Pattern alternatives | Script path |",
        "|---|---|---:|---:|---|",
    ]
    for item in entries:
        lines.append(
            f"| `{item['name']}` | `{item['type']}` | {item['requires_body'] or '-'} | "
            f"{pattern_alternatives(item['pattern'])} | `{item['script_path']}` |"
        )
    lines.extend([
        "",
        "## Safety Contract",
        "",
        "- Unknown URLs, invalid JSON, media URLs and unexpected bodies pass through unchanged.",
        "- Login, token, payment, bank, captcha and membership keywords stay in the forbidden keyword list.",
        "- This report is generated; update source files or generator logic instead of editing the report.",
        "",
    ])
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"App cleaner active report written to {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
