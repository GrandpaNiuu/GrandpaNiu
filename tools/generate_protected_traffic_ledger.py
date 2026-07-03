#!/usr/bin/env python3
"""Generate a ledger for protected login, payment, playback, CDN, and HTTPDNS traffic."""

from __future__ import annotations

import datetime as dt
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "protected_traffic_ledger.md"

SOURCE_FILES = [
    "Rules/direct.list",
    "Rules/protect-login.list",
    "Rules/protect-payment.list",
    "Rules/protect-video.list",
    "Rules/protect-cdn.list",
    "Rewrite/Sources/Misc/finance-protect.conf",
    "Rewrite/Sources/Misc/video-protect.conf",
    "Rewrite/Sources/Misc/cdn-direct.conf",
    "Rewrite/Sources/Misc/httpdns.conf",
]

CATEGORY_TOKENS = {
    "登录 / 账号": ("login", "passport", "auth", "sso", "account", "wechat", "weixin", "servicewechat", "qlogo"),
    "支付 / 银行 / 订单": ("pay", "wallet", "bank", "alipay", "wechatpay", "tenpay", "icbc", "ccb", "abchina", "boc", "cmbchina", "bankcomm", "psbc", "jdpay"),
    "验证码 / HTTPDNS / 核心 API": ("captcha", "verify", "httpdns", "hdns", "dns.", "biliapi", "zijieapi", "snssdk"),
    "视频 / 音乐播放": ("video", "play", "bilivideo", "hdslb", "mgtv", "youku", "googlevideo", "spotify", "music.163"),
    "图片 / 静态 CDN": ("cdn", "img", "image", "pic", "alicdn", "jdimg", "360buyimg", "bdimg", "biliimg", "gtimg", "qpic", "msstatic", "zdmimg"),
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def active_lines(path: Path) -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    for number, line in enumerate(read(path).splitlines(), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or (stripped.startswith("[") and stripped.endswith("]")):
            continue
        out.append((number, stripped))
    return out


def categories_for(line: str) -> list[str]:
    lowered = line.lower()
    hits = [category for category, tokens in CATEGORY_TOKENS.items() if any(token in lowered for token in tokens)]
    return hits or ["其他保护 / 需人工归类"]


def table(rows: list[dict[str, object]], columns: list[str]) -> list[str]:
    if not rows:
        return ["_None._"]
    out = ["| " + " | ".join(columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"]
    for row in rows:
        out.append("| " + " | ".join(str(row.get(column, "")).replace("|", "\\|") for column in columns) + " |")
    return out


def main() -> int:
    category_counts: Counter[str] = Counter()
    policy_counts: Counter[str] = Counter()
    file_counts: Counter[str] = Counter()
    samples: dict[str, list[dict[str, object]]] = defaultdict(list)
    non_direct: list[dict[str, object]] = []

    for relative in SOURCE_FILES:
        path = ROOT / relative
        for number, line in active_lines(path):
            file_counts[relative] += 1
            policy = "DIRECT" if ",DIRECT" in line.upper() else "REJECT" if "REJECT" in line.upper() else "OTHER"
            policy_counts[policy] += 1
            if policy != "DIRECT":
                non_direct.append({"source": f"{relative}:{number}", "policy": policy, "line": line})
            for category in categories_for(line):
                category_counts[category] += 1
                if len(samples[category]) < 20:
                    samples[category].append({"source": f"{relative}:{number}", "policy": policy, "line": line})

    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    summary_rows = [
        {"category": category, "entries": count}
        for category, count in category_counts.most_common()
    ]
    file_rows = [
        {"source_file": source, "entries": count, "exists": (ROOT / source).exists()}
        for source, count in file_counts.most_common()
    ]
    lines = [
        "# 保护链路台账",
        "",
        f"- 生成时间：{now}",
        f"- 扫描源文件：{len(SOURCE_FILES)}",
        f"- 保护/候选条目：{sum(file_counts.values())}",
        f"- DIRECT 条目：{policy_counts['DIRECT']}",
        f"- 非 DIRECT 条目：{sum(count for policy, count in policy_counts.items() if policy != 'DIRECT')}",
        "",
        "## 使用边界",
        "",
        "- 本报告只记录登录、支付、银行、验证码、视频、图片/CDN、HTTPDNS 等保护链路来源。",
        "- 它不是自动放行清单，也不会修改规则。",
        "- 出现 App 无网络、无法登录、无法播放或图片空白时，先查本台账和 MITM/REJECT 风险台账，再做单点源文件调整。",
        "",
        "## 分类统计",
        "",
        *table(summary_rows, ["category", "entries"]),
        "",
        "## 源文件统计",
        "",
        *table(file_rows, ["source_file", "entries", "exists"]),
        "",
        "## 非 DIRECT 条目提示",
        "",
        "这些条目位于保护相关源文件中，但策略不是 DIRECT。它们可能是 App 特定广告例外，不应自动删除；未来如发生误伤需单点复核。",
        "",
        *table(non_direct[:80], ["source", "policy", "line"]),
        "",
        "## 分类样例",
        "",
    ]
    for category, rows in samples.items():
        lines.extend([f"### {category}", "", *table(rows, ["source", "policy", "line"]), ""])
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Protected traffic ledger written to {REPORT.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
