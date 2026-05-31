#!/usr/bin/env python3
"""Audit high-risk REJECT rules without changing module sources."""

from __future__ import annotations

import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REJECT = ROOT / "Rules" / "reject.list"
DIRECT = ROOT / "Rules" / "direct.list"
REPORT = ROOT / "reports" / "reject_risk_report.md"

RISK_TOKENS = {
    "图片 / CDN": [
        "qpic.cn",
        "gtimg.cn",
        "qlogo.cn",
        "wxapp.tc.qq.com",
        "alicdn.com",
        "pddpic.com",
        "360buyimg.com",
        "jdimg.com",
        "biliimg.com",
        "hdslb.com",
        "meituan.net",
        "dpfile.com",
    ],
    "HTTPDNS": ["httpdns", "dns.weixin"],
    "微信 / 支付 / 银行": [
        "wxs.qq.com",
        "wx.qq.com",
        "weixin.qq.com",
        "servicewechat.com",
        "wechatpay.cn",
        "alipay",
        "bank",
        "cmbchina",
        "icbc",
        "ccb.com",
        "boc.cn",
    ],
    "国内核心 API": [
        "api.biliapi",
        "app.biliapi",
        "api.pinduoduo",
        "acs.m.taobao",
        "api.m.jd",
        "dianping",
        "amap",
        "baidu",
        "meituan",
    ],
}

AD_TOKENS = [
    "ad",
    "ads",
    "advert",
    "gdt",
    "tracking",
    "track",
    "analytics",
    "stat",
    "log",
    "beacon",
    "splash",
]

CHECKLIST = [
    "qpic.cn",
    "gtimg.cn",
    "qlogo.cn",
    "wxs.qq.com",
    "wx.qq.com",
    "weixin.qq.com",
    "servicewechat.com",
    "wxapp.tc.qq.com",
    "wechatpay.cn",
    "alicdn.com",
    "pddpic.com",
    "360buyimg.com",
    "jdimg.com",
    "biliimg.com",
    "hdslb.com",
    "meituan.net",
    "dpfile.com",
    "httpdns",
    "dns.weixin",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def active_lines(path: Path) -> list[str]:
    lines: list[str] = []
    for line in read(path).splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            lines.append(stripped)
    return lines


def is_reject(line: str) -> bool:
    return "REJECT" in line.upper()


def token_hit(line: str, tokens: list[str]) -> bool:
    lowered = line.lower()
    return any(token.lower() in lowered for token in tokens)


def classify(lines: list[str]) -> dict[str, list[str]]:
    buckets = {
        "明确广告域": [],
        "图片 / CDN": [],
        "HTTPDNS": [],
        "微信 / 支付 / 银行": [],
        "国内核心 API": [],
        "不确定规则": [],
    }
    for line in lines:
        if not is_reject(line):
            continue
        matched = False
        for bucket, tokens in RISK_TOKENS.items():
            if token_hit(line, tokens):
                buckets[bucket].append(line)
                matched = True
        if matched:
            continue
        if token_hit(line, AD_TOKENS):
            buckets["明确广告域"].append(line)
        else:
            buckets["不确定规则"].append(line)
    return buckets


def direct_status(token: str, direct_text: str) -> str:
    return "已精确保护或覆盖" if token.lower() in direct_text.lower() else "未发现"


def render_items(items: list[str], limit: int = 120) -> list[str]:
    if not items:
        return ["- 无"]
    out = [f"- `{item}`" for item in items[:limit]]
    if len(items) > limit:
        out.append(f"- 其余 {len(items) - limit} 条已省略")
    return out


def main() -> None:
    reject_lines = active_lines(REJECT)
    direct_text = read(DIRECT)
    buckets = classify(reject_lines)
    risky_total = sum(len(buckets[name]) for name in ["图片 / CDN", "HTTPDNS", "微信 / 支付 / 银行", "国内核心 API", "不确定规则"])
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")

    lines = [
        "# REJECT 风险审计报告",
        "",
        f"生成时间：{now}",
        "",
        "本报告只做分类审计，不会自动删除、注释或替换任何规则。高风险项需要先确认 Shadowrocket 日志和真实 App 行为，再做 source-first 修复。",
        "",
        "## 总览",
        "",
        f"- 活跃 REJECT 规则数：{len([line for line in reject_lines if is_reject(line)])}",
        f"- 明确广告域：{len(buckets['明确广告域'])}",
        f"- 图片 / CDN 风险：{len(buckets['图片 / CDN'])}",
        f"- HTTPDNS 风险：{len(buckets['HTTPDNS'])}",
        f"- 微信 / 支付 / 银行风险：{len(buckets['微信 / 支付 / 银行'])}",
        f"- 国内核心 API 风险：{len(buckets['国内核心 API'])}",
        f"- 不确定规则：{len(buckets['不确定规则'])}",
        f"- 需要人工复核总数：{risky_total}",
        "",
        "## 重点风险域检查",
        "",
        "| 域名 / 关键词 | direct.list 状态 | reject.list 命中 | 建议 |",
        "|---|---|---:|---|",
    ]
    reject_text = "\n".join(reject_lines).lower()
    for token in CHECKLIST:
        hit_count = sum(1 for line in reject_lines if token.lower() in line.lower() and is_reject(line))
        if token in {"httpdns", "dns.weixin"}:
            advice = "人工复核，不建议 pre-matching REJECT"
        elif token in {"wxs.qq.com", "wx.qq.com", "weixin.qq.com", "servicewechat.com", "wechatpay.cn"}:
            advice = "默认保护，不直接 REJECT"
        elif "pic" in token or "img" in token or token in {"gtimg.cn", "qlogo.cn", "alicdn.com", "hdslb.com", "meituan.net", "dpfile.com"}:
            advice = "默认 DIRECT 或人工复核，不建议 REJECT"
        else:
            advice = "人工复核"
        lines.append(f"| `{token}` | {direct_status(token, direct_text)} | {hit_count} | {advice} |")

    sections = [
        ("明确广告域：可保留 REJECT", "明确广告域"),
        ("图片 / CDN：默认 DIRECT 或人工复核，不建议 REJECT", "图片 / CDN"),
        ("HTTPDNS：人工复核，不建议 pre-matching REJECT", "HTTPDNS"),
        ("微信 / 支付 / 银行：默认保护，不直接 REJECT", "微信 / 支付 / 银行"),
        ("国内核心 API：不建议 REJECT", "国内核心 API"),
        ("不确定规则：pending / manual-review", "不确定规则"),
    ]
    for title, key in sections:
        lines += ["", f"## {title}", ""]
        lines += render_items(buckets[key])

    lines += [
        "",
        "## 处理边界",
        "",
        "- 不批量删除规则。",
        "- 不新增 `DOMAIN-SUFFIX,qq.com,DIRECT` 这类过宽保护。",
        "- 微信、支付、银行、图片 CDN 只能做精确保护。",
        "- 如果需要修复，优先修改 `Rules/direct.list` 的精确 `DIRECT,pre-matching` 或单条注释高风险 REJECT，并重新构建。",
        "- 没有真实日志和手测记录时，保持 manual-review。",
        "",
    ]
    write(REPORT, "\n".join(lines))
    print(f"Reject risk report written to {REPORT}")


if __name__ == "__main__":
    main()
