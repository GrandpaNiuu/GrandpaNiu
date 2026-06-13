#!/usr/bin/env python3
"""Generate a risk-layer promotion candidate report from automated evidence."""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUS_MITM = ROOT / "Rewrite" / "Sources" / "MITM-stable-plus.conf"
REPORT = ROOT / "reports" / "stable_plus_promotion_report.md"
HOSTNAME_RE = re.compile(r"^\s*hostname\s*=\s*(.+)$")

APP_GROUPS = {
    "视频娱乐": {
        "apps": ["爱奇艺", "AcFun", "芒果 TV", "咪咕视频", "虎牙", "快手"],
        "keywords": ["iqiyi", "acfun", "mgtv", "miguvideo", "huya", "kuaishou", "kwai", "gifshow", "ksapisrv"],
    },
    "电商消费": {
        "apps": ["得物", "唯品会", "当当", "转转", "什么值得买", "永辉"],
        "keywords": ["dewu", "appvipshop", "dangdang", "zhuanzhuan", "smzdm", "yonghuivip"],
    },
    "餐饮消费": {
        "apps": ["瑞幸", "麦当劳", "星巴克"],
        "keywords": ["lkcoffee", "mcd", "starbucks"],
    },
    "出行旅游": {
        "apps": ["携程", "去哪儿", "途家", "途牛", "航旅纵横", "飞常准", "南航", "东航"],
        "keywords": ["trip", "qunar", "tujia", "tuniu", "umetrip", "variflight", "csair", "ceair"],
    },
    "内容资讯": {
        "apps": ["豆瓣", "LOFTER", "虎嗅", "澎湃", "华尔街见闻", "人民 App", "ZAKER"],
        "keywords": ["douban", "lofter", "huxiu", "thepaper", "wallstreetcn", "wallstcn", "peopleapp", "myzaker"],
    },
    "招聘职场": {
        "apps": ["猎聘", "BOSS 直聘", "51job", "猪八戒"],
        "keywords": ["liepin", "zhipin", "51job", "zbj"],
    },
    "学习办公": {
        "apps": ["有道", "WPS", "金山文档", "超星", "粉笔"],
        "keywords": ["youdao", "wps", "kdocs", "chaoxing", "fenbi"],
    },
    "云盘工具": {
        "apps": ["阿里云盘", "天翼云盘", "迅雷", "向日葵"],
        "keywords": ["alipan", "189.cn", "xunlei", "oray"],
    },
    "汽车硬件": {
        "apps": ["汽车之家", "易车", "比亚迪", "小鹏", "小牛", "米家", "Zepp", "萤石", "Petkit"],
        "keywords": ["autohome", "yiche", "bydauto", "xiaopeng", "niu.com", "mi.com", "zepp", "ys7", "petkit"],
    },
}

SENSITIVE_TOKENS = (
    "bank",
    "payment",
    "pay",
    "captcha",
    "passport",
    "token",
    "cookie",
    "security",
    "alipay",
    "wxpay",
    "login",
    "verify",
    "verification",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def parse_hosts(text: str) -> list[str]:
    hosts: list[str] = []
    seen: set[str] = set()
    for line in text.splitlines():
        match = HOSTNAME_RE.match(line)
        if not match:
            continue
        value = match.group(1).replace("%APPEND%", "")
        for raw in value.split(","):
            host = raw.strip()
            if host and host not in seen:
                seen.add(host)
                hosts.append(host)
    return hosts


def hosts_for_group(hosts: list[str], keywords: list[str]) -> list[str]:
    return [host for host in hosts if any(keyword.lower() in host.lower() for keyword in keywords)]


def has_sensitive(hosts: list[str]) -> bool:
    return any(any(token in host.lower() for token in SENSITIVE_TOKENS) for host in hosts)


def main() -> None:
    hosts = parse_hosts(read(PLUS_MITM))
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")

    rows: list[str] = []
    eligible: list[str] = []
    blocked: list[str] = []
    for group_name, spec in APP_GROUPS.items():
        group_hosts = hosts_for_group(hosts, spec["keywords"])
        sensitive = has_sensitive(group_hosts)
        candidate = bool(group_hosts) and not sensitive
        if candidate:
            eligible.append(group_name)
        else:
            blocked.append(group_name)
        reason = "无敏感词且存在可审计 hostname" if candidate else "无 hostname 或含敏感词，保持风险层"
        rows.append(
            f"| {group_name} | {', '.join(spec['apps'])} | {len(group_hosts)} | {'是' if sensitive else '否'} | {'是' if candidate else '否'} | {reason} |"
        )

    lines = [
        "# 风险层晋级候选报告",
        "",
        f"生成时间：{now}",
        "",
        "本报告只生成自动化晋级建议，不自动修改公开入口，也不依赖人工设备记录。任何晋级都必须通过质量门禁并保留回滚路径。",
        "",
        "## 总体结论",
        "",
        f"- 风险层 hostname 总数：{len(hosts)}",
        f"- 可进入 PR 候选组：{len(eligible)}",
        f"- 暂不可晋级组：{len(blocked)}",
        "- 晋级前必须运行 `python scripts/quality_gate.py`。",
        "",
        "## 候选矩阵",
        "",
        "| App 组 | App / 服务 | 匹配 hostname 数 | 是否含敏感词 | 可进入 PR 候选 | 原因 |",
        "|---|---|---:|---|---|---|",
        *rows,
        "",
        "## 可进入 PR 候选",
        "",
    ]
    lines += [f"- {item}" for item in eligible] if eligible else ["- 无"]
    lines += [
        "",
        "## 晋级操作边界",
        "",
        "- 本报告不自动晋级。",
        "- 晋级只能单项进行，不允许把整个风险层合并进公开入口。",
        "- 晋级目标必须是源头文件，不允许直接手改 Release 成品。",
        "- 晋级后必须运行完整质量门禁。",
        "",
    ]
    write(REPORT, "\n".join(lines))
    print(f"Stable Plus promotion report written to {REPORT}")


if __name__ == "__main__":
    main()
