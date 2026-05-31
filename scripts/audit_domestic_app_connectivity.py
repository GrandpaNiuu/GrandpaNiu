#!/usr/bin/env python3
"""Audit domestic App connectivity false-positive risks.

This report focuses on common reasons that Chinese apps fail to load images,
open pages, upload media, or send WeChat images after aggressive ad blocking.
It is report-only and does not edit rules.
"""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "domestic_app_connectivity_audit.md"
REJECT = ROOT / "Rules" / "reject.list"
DIRECT = ROOT / "Rules" / "direct.list"
APP_CLEANER_ACTIVE = ROOT / "Scripts" / "app-cleaner-active.conf"
APP_CLEANER = ROOT / "Scripts" / "app-cleaner.js"

RISK_PATTERNS = {
    "wechat-media": ["weixin", "wechat", "wxs.qq.com", "qpic.cn", "gtimg.cn", "qlogo.cn", "weixinbridge"],
    "image-cdn": ["alicdn", "tbcdn", "taobaocdn", "pddpic", "360buyimg", "jdimg", "bdimg", "biliimg", "hdslb", "dpfile", "msstatic", "zdmimg"],
    "httpdns": ["httpdns", "dns.weixin"],
    "domestic-core-api": ["api.biliapi", "app.biliapi", "api.pinduoduo", "acs.m.taobao", "api.m.jd", "meituan", "dianping", "amap", "baidu"],
    "bank-payment": ["cmbchina", "abchina", "ccb.com", "boc.cn", "wechatpay", "alipay", "bank", "pay"],
}

BROAD_ACTIVE_TOKENS = [
    "qq\\.com", "gtimg", "qpic", "alicdn", "pddpic", "jdimg", "360buyimg", "bdimg", "biliimg", "hdslb", "meituan\\.net"
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def active_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip() and not line.lstrip().startswith("#")]


def contains_any(text: str, tokens: list[str]) -> bool:
    lower = text.lower()
    return any(token.lower() in lower for token in tokens)


def collect_reject_risks() -> dict[str, list[str]]:
    risks = {name: [] for name in RISK_PATTERNS}
    for line in active_lines(read(REJECT)):
        if "REJECT" not in line:
            continue
        for name, tokens in RISK_PATTERNS.items():
            if contains_any(line, tokens):
                risks[name].append(line)
    return risks


def direct_covers(token: str) -> bool:
    text = read(DIRECT).lower()
    return token.lower() in text


def active_broad_hits() -> list[str]:
    text = read(APP_CLEANER_ACTIVE)
    hits = []
    for token in BROAD_ACTIVE_TOKENS:
        try:
            if re.search(token, text, re.I):
                hits.append(token)
        except re.error:
            if token.lower() in text.lower():
                hits.append(token)
    return hits


def cleaner_risk_notes() -> list[str]:
    text = read(APP_CLEANER)
    notes = []
    if "banner" in text and "GENERIC_DROP_KEYS" in text:
        notes.append("app-cleaner contains banner logic; verify generic cleaner is conservative and does not remove ordinary homepage image modules.")
    if "promotion" in text and "GENERIC_DROP_KEYS" in text:
        notes.append("app-cleaner contains promotion logic; verify ordinary promotion/feature entrances are not dropped unless explicitly ad-marked.")
    if "isMediaLikeRequest" not in text:
        notes.append("app-cleaner lacks media request bypass; image/video responses may be processed accidentally.")
    if "content-type" not in text.lower():
        notes.append("app-cleaner does not inspect content-type; non-JSON media should be protected.")
    return notes


def main() -> None:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    risks = collect_reject_risks()
    broad = active_broad_hits()
    notes = cleaner_risk_notes()
    direct_checks = {
        "wechat-media": ["weixin.qq.com", "wxs.qq.com", "qpic.cn", "gtimg.cn", "qlogo.cn"],
        "image-cdn": ["alicdn.com", "pddpic.com", "360buyimg.com", "jdimg.com", "biliimg.com", "meituan.net"],
    }

    lines = [
        "# 国内 App 联网与加载误伤风险排查报告",
        "",
        f"生成时间：{now}",
        "",
        "本报告用于排查国内 App 图片加载失败、页面加载不完整、微信不能发图片等问题。报告只分析，不自动修改规则。",
        "",
        "## 初步结论模板",
        "",
        "- 如果 `reject.list` 命中微信媒体、图片 CDN、HTTPDNS 或核心 API，优先怀疑规则误杀。",
        "- 如果 `app-cleaner-active.conf` 使用宽域名匹配，优先怀疑脚本入口误伤。",
        "- 如果 `app-cleaner.js` 通用 cleaner 删除普通 `banner / promotion / sections`，优先怀疑融合逻辑误伤。",
        "- 如果 `node --check` 通过，通常不是代码语法问题，而是规则或清理逻辑问题。",
        "",
        "## Direct 保护覆盖检查",
        "",
        "| 类别 | 检查项 | direct.list 是否包含 |",
        "|---|---|---|",
    ]
    for category, tokens in direct_checks.items():
        for token in tokens:
            lines.append(f"| {category} | `{token}` | {'是' if direct_covers(token) else '否'} |")

    lines += [
        "",
        "## Reject 风险命中",
        "",
    ]
    for name, items in risks.items():
        lines += [f"### {name}", ""]
        if not items:
            lines.append("- 无")
        else:
            for item in items[:80]:
                lines.append(f"- `{item}`")
            if len(items) > 80:
                lines.append(f"- 其余 {len(items) - 80} 条省略")
        lines.append("")

    lines += [
        "## app-cleaner active 宽匹配风险",
        "",
    ]
    if broad:
        for item in broad:
            lines.append(f"- `{item}`")
    else:
        lines.append("- 未发现高风险宽匹配 token。")

    lines += [
        "",
        "## app-cleaner 逻辑风险提示",
        "",
    ]
    if notes:
        for note in notes:
            lines.append(f"- {note}")
    else:
        lines.append("- 未发现明显通用清理器风险提示。")

    lines += [
        "",
        "## 建议排查顺序",
        "",
        "1. 先确认 `node --check Scripts/app-cleaner.js` 是否通过。",
        "2. 再看 Shadowrocket 日志中具体命中 REJECT、MITM 还是 Script。",
        "3. 如果命中 REJECT，优先单条加入 Direct pre-matching 或注释该 REJECT。",
        "4. 如果命中 Script，收窄 `app-cleaner-active.conf` 或增加媒体 bypass。",
        "5. 如果命中 MITM，检查该 hostname 是否应从 stable MITM 层移到 stable-plus 或 full。",
        "6. 不要一次性删除大量规则；国内 App 联网问题应逐域名单条修复。",
        "",
    ]
    write(REPORT, "\n".join(lines))
    print(f"Domestic App connectivity audit written to {REPORT}")


if __name__ == "__main__":
    main()
