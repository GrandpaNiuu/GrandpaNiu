#!/usr/bin/env python3
"""Generate Stable Plus promotion candidate report.

The script does not promote anything automatically. It only inspects
MITM-stable-plus.conf and manual_test_log.md, then writes a report showing which
App groups are eligible, blocked, or still untested.
"""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUS_MITM = ROOT / "Rewrite" / "Sources" / "MITM-stable-plus.conf"
MANUAL_LOG = ROOT / "reports" / "manual_test_log.md"
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
    "bank", "payment", "pay", "captcha", "passport", "token", "cookie", "security",
    "alipay", "wxpay", "login", "verify", "verification"
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
    result: list[str] = []
    for host in hosts:
        lowered = host.lower()
        if any(keyword.lower() in lowered for keyword in keywords):
            result.append(host)
    return result


def has_sensitive(hosts: list[str]) -> bool:
    for host in hosts:
        lowered = host.lower()
        if any(token in lowered for token in SENSITIVE_TOKENS):
            return True
    return False


def test_status_for_group(log: str, group_name: str, apps: list[str]) -> tuple[str, str]:
    matched_lines: list[str] = []
    for line in log.splitlines():
        if "|" not in line or "Stable Plus" not in line:
            continue
        haystack = line.lower()
        if group_name.lower() in haystack or any(app.lower() in haystack for app in apps):
            matched_lines.append(line)
    if not matched_lines:
        return "未找到测试记录", "没有 Stable Plus 对应该 App 组的测试行"

    # Order matters: rows with "未测试" also normally have 是否通过=否.
    # They are untested, not actual failures.
    untested = [line for line in matched_lines if "未测试" in line]
    failed = [line for line in matched_lines if "| 失败 |" in line]
    partial = [line for line in matched_lines if "| 部分通过 |" in line]
    passed = [line for line in matched_lines if "| 通过 |" in line and line.rstrip().endswith("| 是 |")]

    if failed:
        return "阻断", "存在失败记录，不能晋级 Stable"
    if partial:
        return "部分通过", "存在部分通过记录，需要继续测试，不能晋级 Stable"
    if untested:
        return "未测试", "仍为未测试，不能晋级 Stable"
    if passed:
        return "通过", "Stable Plus 记录显示通过，可进入人工复核晋级候选"
    return "待复核", "存在记录但无法自动判断，需要人工复核"


def main() -> None:
    hosts = parse_hosts(read(PLUS_MITM))
    log = read(MANUAL_LOG)
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")

    rows: list[str] = []
    eligible: list[str] = []
    blocked: list[str] = []
    for group_name, spec in APP_GROUPS.items():
        group_hosts = hosts_for_group(hosts, spec["keywords"])
        status, reason = test_status_for_group(log, group_name, spec["apps"])
        sensitive = has_sensitive(group_hosts)
        candidate = status == "通过" and group_hosts and not sensitive
        if candidate:
            eligible.append(group_name)
        else:
            blocked.append(group_name)
        rows.append(
            f"| {group_name} | {', '.join(spec['apps'])} | {len(group_hosts)} | {'是' if sensitive else '否'} | {status} | {'是' if candidate else '否'} | {reason} |"
        )

    lines = [
        "# Stable Plus 晋级候选报告",
        "",
        f"生成时间：{now}",
        "",
        "本报告只生成晋级建议，不自动修改 `MITM-app-clean.conf`，也不会把 Stable Plus 或 Full 自动合并进 Stable。",
        "",
        "## 总体结论",
        "",
        f"- Stable Plus hostname 总数：{len(hosts)}",
        f"- 可进入人工复核的候选组：{len(eligible)}",
        f"- 暂不可晋级组：{len(blocked)}",
        "- 晋级前必须确认 Stable 已通过核心流程测试。",
        "- 任一登录、验证码、支付前置、订单页异常都不能晋级。",
        "",
        "## 候选矩阵",
        "",
        "| App 组 | App / 服务 | 匹配 hostname 数 | 是否含敏感词 | Stable Plus 测试状态 | 可进入晋级复核 | 原因 |",
        "|---|---|---:|---|---|---|---|",
        *rows,
        "",
        "## 可进入人工复核候选",
        "",
    ]
    lines += [f"- {item}" for item in eligible] if eligible else ["- 无"]
    lines += [
        "",
        "## 晋级操作边界",
        "",
        "- 本报告不自动晋级。",
        "- 晋级只能单项进行，不允许把整个 Stable Plus 合并进 Stable。",
        "- 晋级目标是 `Rewrite/Sources/MITM-app-clean.conf`。",
        "- 晋级后必须重新生成四个 Release 版本。",
        "- 晋级后必须重新运行 `validate_repository.py`、`validate_profiles.py`、`repository_health_check.py`。",
        "",
        "## 目前结论",
        "",
        "如果测试记录仍为未测试，则所有 App 组都不能晋级 Stable。",
        "",
    ]
    write(REPORT, "\n".join(lines))
    print(f"Stable Plus promotion report written to {REPORT}")


if __name__ == "__main__":
    main()
