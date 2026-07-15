#!/usr/bin/env python3
"""Generate a false-positive review queue from existing risk ledgers."""

from __future__ import annotations

import datetime as dt
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MITM_REJECT_LEDGER = ROOT / "reports" / "mitm_reject_risk_ledger.md"
REJECT_RISK_REPORT = ROOT / "reports" / "reject_risk_report.md"
PROTECTED_LEDGER = ROOT / "reports" / "protected_traffic_ledger.md"
REPORT = ROOT / "reports" / "false_positive_review_report.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def split_markdown_row(line: str) -> list[str]:
    """Split a Markdown row while restoring escaped pipe characters."""
    value = line.strip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|"):
        value = value[:-1]

    cells: list[str] = []
    current: list[str] = []
    index = 0
    while index < len(value):
        char = value[index]
        if char == "\\" and index + 1 < len(value) and value[index + 1] == "|":
            current.append("|")
            index += 2
            continue
        if char == "|":
            cells.append("".join(current))
            current = []
        else:
            current.append(char)
        index += 1
    cells.append("".join(current))
    return cells


def parse_risk_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in text.splitlines():
        if not line.startswith("| MITM") and not line.startswith("| REJECT"):
            continue
        parts = [part.strip().strip("`") for part in split_markdown_row(line)]
        if len(parts) < 6:
            continue
        if len(parts) >= 7:
            output_status, entry, reason = parts[4:7]
        else:
            output_status, entry, reason = "unclassified", parts[4], parts[5]
        rows.append(
            {
                "type": parts[0],
                "risk": parts[1],
                "category": parts[2],
                "source": parts[3],
                "output_status": output_status,
                "entry": entry,
                "reason": reason,
            }
        )
    return rows


def table(rows: list[dict[str, str]], columns: list[str]) -> list[str]:
    if not rows:
        return ["_None._"]
    out = ["| " + " | ".join(columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"]
    for row in rows:
        out.append("| " + " | ".join(str(row.get(column, "")).replace("|", "\\|") for column in columns) + " |")
    return out


def section_count(text: str, title: str) -> int:
    match = re.search(rf"### {re.escape(title)}\n(?P<body>.*?)(?:\n### |\Z)", text, re.S)
    if not match:
        return 0
    return sum(1 for line in match.group("body").splitlines() if line.strip().startswith("- `") or line.strip().startswith("- DOMAIN"))


def main() -> int:
    risk_rows = parse_risk_rows(read(MITM_REJECT_LEDGER))
    by_risk = Counter(row["risk"] for row in risk_rows)
    by_type = Counter(row["type"] for row in risk_rows)
    by_category = Counter(row["category"] for row in risk_rows)
    high_rows = [row for row in risk_rows if row["risk"] == "high"]
    medium_rows = [row for row in risk_rows if row["risk"] == "medium"]
    reject_text = read(REJECT_RISK_REPORT)
    protected_exists = PROTECTED_LEDGER.exists()
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    category_rows = [{"category": category, "count": count} for category, count in by_category.most_common()]
    lines = [
        "# 误伤复核队列报告",
        "",
        f"- 生成时间：{now}",
        f"- 风险台账条目：{len(risk_rows)}",
        f"- high：{by_risk['high']}",
        f"- medium：{by_risk['medium']}",
        f"- MITM：{by_type['MITM']}",
        f"- REJECT：{by_type['REJECT']}",
        f"- 保护链路台账：{'存在' if protected_exists else '缺失'}",
        "",
        "## 复核原则",
        "",
        "- 本报告只生成复核队列，不自动修改规则。",
        "- 只有出现真实 App 异常、Shadowrocket 日志、抓包证据或可复现失败时，才做 source-first 单点调整。",
        "- 先定位具体源文件，再优先缩小规则；不要批量删除，也不要用宽泛白名单掩盖问题。",
        "- 修改后必须运行完整质量门禁。",
        "",
        "## 风险分类统计",
        "",
        *table(category_rows, ["category", "count"]),
        "",
        "## reject_risk_report 待复核摘要",
        "",
        f"- 银行 / 支付：{section_count(reject_text, 'Bank / Payment')}",
        f"- 图片 / CDN：{section_count(reject_text, 'Image / CDN')}",
        f"- 国内核心 API：{section_count(reject_text, 'Domestic Core API')}",
        "",
        "## high 优先复核队列",
        "",
        *table(high_rows[:120], ["type", "risk", "category", "source", "output_status", "entry", "reason"]),
        "",
        "## medium 抽样复核队列",
        "",
        *table(medium_rows[:120], ["type", "risk", "category", "source", "output_status", "entry", "reason"]),
        "",
        "## 建议处理流程",
        "",
        "1. 用户反馈具体 App 和现象后，先搜索本报告的 `entry` 或 `source`。",
        "2. 同时查看 `reports/protected_traffic_ledger.md` 是否已有保护链路。",
        "3. 如果是误伤，优先在最小源文件里注释、缩窄或添加精确保护。",
        "4. 运行 `python scripts/quality_gate.py`。",
        "5. 在 `docs/ai/RISK_LOG.md` 记录证据、处理结论和回滚路径。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"False-positive review report written to {REPORT.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
