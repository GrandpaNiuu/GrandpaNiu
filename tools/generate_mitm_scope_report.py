#!/usr/bin/env python3
"""Generate a categorized MITM hostname scope report."""

from __future__ import annotations

from collections import Counter, defaultdict
import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "Release" / "Ronghemokuai.sgmodule"
REPORT = ROOT / "reports" / "mitm_scope_report.md"
HOSTNAME_RE = re.compile(r"^\s*hostname\s*=\s*(.+)$")

CATEGORIES = [
    ("payment_bank_wallet", ("wechatpay", "alipay", "bank", "icbc", "ccb", "cmbchina", "abchina", "boc", "psbc", "wallet")),
    ("login_account_auth", ("passport", "login", "auth", "captcha", "verify", "account")),
    ("video_music_playback", ("youtube", "googlevideo", "bili", "bilivideo", "hdslb", "spotify", "mgtv", "youku", "music.163")),
    ("image_static_cdn", ("alicdn", "tbcdn", "taobaocdn", "jdimg", "360buyimg", "pddpic", "bdimg", "qpic", "gtimg", "msstatic", "zdmimg")),
    ("httpdns", ("httpdns", "hdns")),
    ("shopping_life", ("taobao", "tmall", "jd.com", "pinduoduo", "yangkeduo", "meituan", "dianping", "ele.me")),
    ("social_content", ("weibo", "zhihu", "xiaohongshu", "soulapp", "tieba", "coolapk", "reddit")),
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def hosts(text: str) -> list[str]:
    result: list[str] = []
    in_mitm = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped == "[MITM]":
            in_mitm = True
            continue
        if in_mitm and stripped.startswith("[") and stripped.endswith("]"):
            break
        if not in_mitm:
            continue
        match = HOSTNAME_RE.match(line)
        if not match:
            continue
        value = match.group(1).replace("%APPEND%", "")
        result.extend(host.strip() for host in value.split(",") if host.strip())
    return result


def base_domain(host: str) -> str:
    cleaned = host.strip().lstrip("*.").lower()
    parts = [part for part in cleaned.split(".") if part]
    return ".".join(parts[-2:]) if len(parts) >= 2 else cleaned


def category_for(host: str) -> str:
    lowered = host.lower()
    for name, tokens in CATEGORIES:
        if any(token in lowered for token in tokens):
            return name
    return "other_app_or_service"


def main() -> None:
    host_list = hosts(read(MODULE))
    categories: dict[str, list[str]] = defaultdict(list)
    wildcard_count = 0
    for host in host_list:
        categories[category_for(host)].append(host)
        if host.startswith("*."):
            wildcard_count += 1
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    base_counts = Counter(base_domain(host) for host in host_list)
    lines = [
        "# MITM Scope Report",
        "",
        f"- Generated at: {now}",
        f"- Total hostnames: {len(host_list)}",
        f"- Wildcard hostnames: {wildcard_count}",
        f"- Unique base domains: {len(base_counts)}",
        "",
        "## Category Counts",
        "",
        "| Category | Hosts |",
        "|---|---:|",
    ]
    for name in [item[0] for item in CATEGORIES] + ["other_app_or_service"]:
        lines.append(f"| `{name}` | {len(categories.get(name, []))} |")
    lines.extend(["", "## Top Base Domains", ""])
    for domain, count in base_counts.most_common(40):
        lines.append(f"- `{domain}`: {count}")
    lines.extend([
        "",
        "## Maintenance Notes",
        "",
        "- This report is informational and does not change MITM behavior.",
        "- Payment, bank, login, video playback and CDN categories should be narrowed only with real breakage evidence.",
        "- Broad wildcard entries should keep a clear source path and rollback path in `Rewrite/Registry.md`.",
        "",
    ])
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"MITM scope report written to {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
