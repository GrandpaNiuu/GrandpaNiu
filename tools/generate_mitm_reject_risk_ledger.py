#!/usr/bin/env python3
"""Generate an informational MITM/REJECT risk ledger without changing rules."""

from __future__ import annotations

from dataclasses import dataclass
import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "mitm_reject_risk_ledger.md"

SECTION_RE = re.compile(r"^\s*\[([^\]]+)\]\s*$")
HOSTNAME_RE = re.compile(r"^\s*hostname\s*=\s*(.+)$", re.I)


@dataclass(frozen=True)
class RiskCategory:
    key: str
    title: str
    level: str
    tokens: tuple[str, ...]


@dataclass(frozen=True)
class LedgerItem:
    kind: str
    level: str
    category: str
    source: str
    value: str
    reason: str


RISK_CATEGORIES = (
    RiskCategory(
        "payment_bank_wallet",
        "银行 / 支付 / 钱包",
        "high",
        (
            "alipay",
            "wechatpay",
            "tenpay",
            "unionpay",
            "bank",
            "icbc",
            "ccb",
            "cmbchina",
            "abchina",
            "bankcomm",
            "psbc",
            "boc.cn",
            "mbs.boc.cn",
            "wallet",
            "cashier",
            "pay.",
        ),
    ),
    RiskCategory(
        "login_account_auth",
        "登录 / 账号 / 鉴权",
        "high",
        (
            "login",
            "passport",
            "account",
            "auth",
            "oauth",
            "sso",
            "verify",
            "captcha",
            "security",
            "token",
            "cookie",
        ),
    ),
    RiskCategory(
        "video_music_playback",
        "视频 / 音乐播放链路",
        "medium",
        (
            "googlevideo",
            "youtubei",
            "ytimg",
            "bilivideo",
            "hdslb",
            "biliapi",
            "spotify",
            "scdn.co",
            "pscdn.co",
            "music.163",
            "mgtv",
            "youku",
            "iqiyi",
            "qiyi",
            "video",
        ),
    ),
    RiskCategory(
        "image_static_cdn",
        "图片 / 静态 CDN",
        "medium",
        (
            "cdn",
            "alicdn",
            "tbcdn",
            "taobaocdn",
            "jdimg",
            "360buyimg",
            "pddpic",
            "bdimg",
            "biliimg",
            "qpic",
            "gtimg",
            "qlogo",
            "msstatic",
            "zdmimg",
            "image",
            "img",
            "pic",
            "static",
        ),
    ),
    RiskCategory(
        "httpdns",
        "HTTPDNS / DNS",
        "medium",
        ("httpdns", "hdns", "dns.weixin"),
    ),
    RiskCategory(
        "domestic_core_api",
        "国内 App 核心 API",
        "medium",
        (
            "api.biliapi",
            "app.biliapi",
            "api.pinduoduo",
            "acs.m.taobao",
            "api.m.jd",
            "dianping",
            "meituan",
            "amap",
            "baidu",
            "weixin.qq.com",
            "wx.qq.com",
            "servicewechat",
        ),
    ),
)

AD_TOKENS = (
    "ad",
    "ads",
    "advert",
    "splash",
    "tracking",
    "track",
    "analytics",
    "beacon",
    "stat",
    "log",
    "gdt",
)

SCAN_CONF_ROOTS = (
    ROOT / "Rewrite" / "Sources",
    ROOT / "Rewrite" / "Profiles",
    ROOT / "Scripts",
)
SCAN_RULE_ROOTS = (
    ROOT / "Rules",
    ROOT / "Rewrite" / "Sources",
    ROOT / "Scripts",
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def source_files(roots: tuple[Path, ...], suffixes: tuple[str, ...]) -> list[Path]:
    files: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        if root.is_file():
            files.append(root)
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in suffixes:
                files.append(path)
    return sorted(set(files))


def active_lines(path: Path) -> list[tuple[int, str, str]]:
    result: list[tuple[int, str, str]] = []
    section = ""
    for lineno, raw in enumerate(read(path).splitlines(), 1):
        match = SECTION_RE.match(raw)
        if match:
            section = match.group(1).strip()
            continue
        stripped = raw.strip()
        if not stripped or stripped.startswith(("#", ";", "//")):
            continue
        result.append((lineno, section, stripped))
    return result


def matching_categories(value: str) -> list[RiskCategory]:
    lowered = value.lower()
    return [category for category in RISK_CATEGORIES if any(token in lowered for token in category.tokens)]


def level_for(categories: list[RiskCategory], wildcard: bool = False) -> str:
    if any(category.level == "high" for category in categories):
        return "high"
    if categories or wildcard:
        return "medium"
    return "low"


def category_title(categories: list[RiskCategory], wildcard: bool = False) -> str:
    titles = [category.title for category in categories]
    if wildcard:
        titles.append("通配 MITM")
    return " / ".join(titles) if titles else "未分类"


def escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def mitm_items() -> tuple[list[LedgerItem], int]:
    items: list[LedgerItem] = []
    total_hosts = 0
    for path in source_files(SCAN_CONF_ROOTS, (".conf",)):
        for lineno, section, line in active_lines(path):
            if section != "MITM":
                continue
            match = HOSTNAME_RE.match(line)
            if not match:
                continue
            value = match.group(1).replace("%APPEND%", "")
            for host in [part.strip() for part in value.split(",") if part.strip()]:
                total_hosts += 1
                categories = matching_categories(host)
                wildcard = "*" in host
                if not categories and not wildcard:
                    continue
                reason_parts = []
                if categories:
                    reason_parts.append("命中敏感链路关键词")
                if wildcard:
                    reason_parts.append("包含通配 MITM 范围")
                items.append(
                    LedgerItem(
                        kind="MITM",
                        level=level_for(categories, wildcard),
                        category=category_title(categories, wildcard),
                        source=f"{rel(path)}:{lineno}",
                        value=host,
                        reason="；".join(reason_parts),
                    )
                )
    return items, total_hosts


def reject_items() -> tuple[list[LedgerItem], int]:
    items: list[LedgerItem] = []
    total_rejects = 0
    for path in source_files(SCAN_RULE_ROOTS, (".conf", ".list")):
        for lineno, section, line in active_lines(path):
            if "REJECT" not in line.upper() and " - reject" not in line.lower():
                continue
            total_rejects += 1
            categories = matching_categories(line)
            if not categories:
                lowered = line.lower()
                if any(token in lowered for token in AD_TOKENS):
                    continue
                categories = [
                    RiskCategory(
                        "manual_review",
                        "未分类 REJECT",
                        "medium",
                        (),
                    )
                ]
            items.append(
                LedgerItem(
                    kind="REJECT",
                    level=level_for(categories),
                    category=category_title(categories),
                    source=f"{rel(path)}:{lineno}" if section else f"{rel(path)}:{lineno}",
                    value=line,
                    reason="命中敏感链路关键词" if categories[0].key != "manual_review" else "非明确广告关键词，需人工复核",
                )
            )
    return items, total_rejects


def render_table(items: list[LedgerItem]) -> list[str]:
    lines = [
        "| 类型 | 风险 | 分类 | 来源 | 条目 | 标记原因 |",
        "|---|---|---|---|---|---|",
    ]
    if not items:
        lines.append("| - | - | - | - | - | - |")
        return lines
    for item in sorted(items, key=lambda row: (row.kind, row.level != "high", row.category, row.source, row.value)):
        lines.append(
            "| "
            + " | ".join(
                [
                    item.kind,
                    item.level,
                    escape_table(item.category),
                    f"`{escape_table(item.source)}`",
                    f"`{escape_table(item.value)}`",
                    escape_table(item.reason),
                ]
            )
            + " |"
        )
    return lines


def main() -> int:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8)))
    mitm, total_mitm = mitm_items()
    rejects, total_rejects = reject_items()
    high_count = sum(1 for item in mitm + rejects if item.level == "high")
    medium_count = sum(1 for item in mitm + rejects if item.level == "medium")

    lines = [
        "# MITM / REJECT 风险台账",
        "",
        f"- 生成时间：{now.strftime('%Y-%m-%d %H:%M:%S %z')}",
        f"- 扫描 MITM hostname：{total_mitm}",
        f"- 标记 MITM 风险项：{len(mitm)}",
        f"- 扫描 REJECT / rewrite reject 条目：{total_rejects}",
        f"- 标记 REJECT 风险项：{len(rejects)}",
        f"- 高风险项：{high_count}",
        f"- 中风险项：{medium_count}",
        "",
        "## 使用边界",
        "",
        "- 本台账只标来源和风险，不删除、不注释、不替换任何规则。",
        "- 登录、支付、银行、验证码、视频播放、图片/CDN、核心 API 只能在有真实异常或日志证据时单点复核。",
        "- `high` 代表不应随意扩大 MITM / REJECT 范围；`medium` 代表需要人工复核来源和 App 行为。",
        "",
        "## MITM 风险项",
        "",
        *render_table(mitm),
        "",
        "## REJECT 风险项",
        "",
        *render_table(rejects),
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"MITM/REJECT risk ledger written to {REPORT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
