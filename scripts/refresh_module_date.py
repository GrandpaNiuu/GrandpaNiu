#!/usr/bin/env python3
"""Refresh the Fusion module metadata date using Beijing time."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "Rewrite" / "Sources" / "Meta.conf"
REPORT = ROOT / "reports" / "daily_update_report.md"
BEIJING = timezone(timedelta(hours=8))


def today_beijing() -> str:
    return datetime.now(BEIJING).strftime("%Y-%m-%d")


def refresh_module_date(date_text: str, write_report: bool = True) -> None:
    text = META.read_text(encoding="utf-8")
    if re.search(r"^#!desc=", text, flags=re.M):
        text = re.sub(r"^#!desc=.*$", f"#!desc={date_text} / fusion", text, flags=re.M)
    else:
        text = f"#!desc={date_text} / fusion\n" + text

    if re.search(r"^# update-date:", text, flags=re.M):
        text = re.sub(r"^# update-date:.*$", f"# update-date: {date_text}", text, flags=re.M)
    else:
        lines = text.splitlines()
        insert_at = 0
        for index, line in enumerate(lines):
            if line.startswith("#!"):
                insert_at = index + 1
        lines.insert(insert_at, f"# update-date: {date_text}")
        text = "\n".join(lines) + "\n"

    META.write_text(text, encoding="utf-8", newline="\n")

    if write_report:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(
            "\n".join(
                [
                    "# Daily module update report",
                    "",
                    f"- Date: {date_text}",
                    "- Timezone: Asia/Shanghai",
                    "- Profile: fusion",
                    "- Entry: Ronghemokuai.sgmodule",
                    "",
                ]
            ),
            encoding="utf-8",
            newline="\n",
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Refresh Fusion module metadata date.")
    parser.add_argument("--date", default=today_beijing(), help="date to write, defaults to current Beijing date")
    parser.add_argument("--no-report", action="store_true", help="do not update reports/daily_update_report.md")
    args = parser.parse_args()
    refresh_module_date(args.date, write_report=not args.no_report)
    print(f"Refreshed module date: {args.date}")


if __name__ == "__main__":
    main()
