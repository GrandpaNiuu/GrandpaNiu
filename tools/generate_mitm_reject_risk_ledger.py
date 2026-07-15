#!/usr/bin/env python3
"""Generate an informational MITM/REJECT risk ledger without changing rules."""

from __future__ import annotations

from dataclasses import dataclass
import datetime as dt
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "mitm_reject_risk_ledger.md"
MITM_OPTIMIZATION_REPORT = ROOT / "reports" / "mitm_optimization_report.json"
RELEASE_MODULE = ROOT / "Release" / "Ronghemokuai.sgmodule"

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
    output_status: str
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


def load_mitm_output_evidence() -> tuple[set[str], dict[str, str]]:
    if not MITM_OPTIMIZATION_REPORT.exists():
        return set(), {}
    try:
        data = json.loads(read(MITM_OPTIMIZATION_REPORT))
    except json.JSONDecodeError:
        return set(), {}
    optimized = {
        str(item).strip().lower()
        for item in data.get("optimized_hosts", [])
        if str(item).strip()
    }
    removals = {
        str(item.get("token", "")).strip().lower(): str(item.get("covering_wildcard", "")).strip().lower()
        for item in data.get("semantic_equivalent_removals", [])
        if isinstance(item, dict) and str(item.get("token", "")).strip()
    }
    return optimized, removals


def mitm_output_status(host: str, optimized: set[str], removals: dict[str, str]) -> str:
    normalized = host.strip().lower()
    if normalized in optimized:
        return "final-exact"
    if normalized in removals:
        return f"final-covered-by:{removals[normalized]}"
    return "source-only"


def reject_output_status(line: str, final_lines: set[str]) -> str:
    return "final-exact" if line.strip() in final_lines else "source-only-or-compiled"


def final_active_lines() -> set[str]:
    return {line for _, _, line in active_lines(RELEASE_MODULE)}


def mitm_items(optimized: set[str], removals: dict[str, str]) -> tuple[list[LedgerItem], int]:
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
                        output_status=mitm_output_status(host, optimized, removals),
                        value=host,
                        reason="；".join(reason_parts),
                    )
                )
    return items, total_hosts


def reject_items(compiled_lines: set[str]) -> tuple[list[LedgerItem], int]:
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
                    output_status=reject_output_status(line, compiled_lines),
                    value=line,
                    reason="命中敏感链路关键词" if categories[0].key != "manual_review" else "非明确广告关键词，需人工复核",
                )
            )
    return items, total_rejects


def render_table(items: list[LedgerItem]) -> list[str]:
    lines = [
        "| 类型 | 风险 | 分类 | 来源 | 最终输出状态 | 条目 | 标记原因 |",
        "|---|---|---|---|---|---|---|",
    ]
    if not items:
        lines.append("| - | - | - | - | - | - | - |")
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
                    f"`{escape_table(item.output_status)}`",
                    f"`{escape_table(item.value)}`",
                    escape_table(item.reason),
                ]
            )
            + " |"
        )
    return lines


def main() -> int:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8)))
    optimized_hosts, equivalent_removals = load_mitm_output_evidence()
    compiled_lines = final_active_lines()
    mitm, total_mitm = mitm_items(optimized_hosts, equivalent_removals)
    rejects, total_rejects = reject_items(compiled_lines)
    high_count = sum(1 for item in mitm + rejects if item.level == "high")
    medium_count = sum(1 for item in mitm + rejects if item.level == "medium")
    final_mitm_count = sum(1 for item in mitm if item.output_status.startswith("final-"))
    final_reject_count = sum(1 for item in rejects if item.output_status == "final-exact")

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
        f"- 已映射到最终 MITM 合同的风险项：{final_mitm_count}",
        f"- 最终成品中精确存在的 REJECT 风险项：{final_reject_count}",
        "",
        "## 使用边界",
        "",
        "- 本台账只标来源和风险，不删除、不注释、不替换任何规则。",
        "- `source-only` 表示该源声明不是最终精确 token；它可能被编译器去重、等价覆盖或过滤，不能据此推断客户端行为。",
        "- `source-only-or-compiled` 表示最终成品没有完全相同的文本行；Rewrite 合并等编译转换可能仍保留等价行为。",
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
