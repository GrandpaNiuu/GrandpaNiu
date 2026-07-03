#!/usr/bin/env python3
"""Check generated Markdown reports for common mojibake markers."""

from __future__ import annotations

import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / "reports"
REPORT = REPORTS_DIR / "report_encoding_report.md"

MOJIBAKE_MARKERS = (
    "\ufffd",
    "锛",
    "鐢",
    "杩",
    "瑙",
    "璇",
    "鍛",
    "妯",
    "绋",
    "鍒",
    "棰",
    "鎶",
    "獙",
    "鏈",
    "閺",
    "鈥",
    "脳",
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def report_files() -> list[Path]:
    if not REPORTS_DIR.exists():
        return []
    return sorted(
        path
        for path in REPORTS_DIR.glob("*.md")
        if path.is_file() and path.name != REPORT.name
    )


def scan_file(path: Path) -> list[str]:
    findings: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    for lineno, line in enumerate(text.splitlines(), 1):
        hits = sorted({marker for marker in MOJIBAKE_MARKERS if marker in line})
        if hits:
            snippet = line.strip().replace("|", "\\|")
            if len(snippet) > 120:
                snippet = snippet[:117] + "..."
            findings.append(f"{rel(path)}:{lineno}: markers={','.join(hits)} text=`{snippet}`")
    return findings


def main() -> int:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8)))
    files = report_files()
    findings: list[str] = []
    for path in files:
        findings.extend(scan_file(path))

    lines = [
        "# 报告编码巡检报告",
        "",
        f"- 生成时间：{now.strftime('%Y-%m-%d %H:%M:%S %z')}",
        f"- 扫描报告数：{len(files)}",
        f"- 乱码命中数：{len(findings)}",
        f"- 结果：{'通过' if not findings else '失败'}",
        "",
        "## 检查边界",
        "",
        "- 本检查只扫描 `reports/*.md` 的 UTF-8 读取得到的真实文本。",
        "- PowerShell 或终端显示乱码不等于文件乱码；以本报告的 UTF-8 读取结果为准。",
        "- 命中时应先修生成脚本，不要手写生成报告。",
        "",
        "## 命中明细",
        "",
    ]
    if findings:
        lines.extend(f"- `{item}`" for item in findings)
    else:
        lines.append("- 无")
    lines.append("")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Report encoding check written to {REPORT.relative_to(ROOT)}")
    if findings:
        raise SystemExit(f"report encoding check failed: {len(findings)} mojibake marker(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
