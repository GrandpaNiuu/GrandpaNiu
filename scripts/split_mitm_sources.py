#!/usr/bin/env python3
"""Split MITM hostname source into risk-level files and generate a report.

This script is conservative: it does not remove hostnames. It classifies the
existing Rewrite/Sources/MITM.conf list into core, app-clean and extended files
so profiles can consume reviewed split sources without deleting the original
rollback source.
"""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Rewrite" / "Sources" / "MITM.conf"
CORE = ROOT / "Rewrite" / "Sources" / "MITM-core.conf"
APP = ROOT / "Rewrite" / "Sources" / "MITM-app-clean.conf"
EXTENDED = ROOT / "Rewrite" / "Sources" / "MITM-extended.conf"
REPORT = ROOT / "reports" / "mitm_split_report.md"
HOSTNAME_RE = re.compile(r"^\s*hostname\s*=\s*(.+)$")

CORE_KEYWORDS = (
    "spotify", "spclient", "youtube", "youtubei", "googlevideo", "ytimg", "zhihu", "zhimg"
)
APP_KEYWORDS = (
    "weibo", "xiaohongshu", "xhscdn", "edith", "taobao", "tmall", "goofish", "jd", "jingdong",
    "pinduoduo", "yangkeduo", "meituan", "dianping", "ele.me", "eleme", "amap", "map.baidu",
    "baidu.com", "ximalaya", "xmly", "bilibili", "biliapi", "tieba", "coolapk", "163", "douyu",
    "xiaoyuzhou", "reddit"
)
SENSITIVE_KEYWORDS = (
    "bank", "cmb", "icbc", "ccb", "abc", "boc", "psbc", "pay", "payment", "alipay", "wxpay",
    "wechat", "login", "captcha", "verify", "verification", "passport", "account", "token", "cookie",
    "certificate", "cert", "security"
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
        # Remove the marker before splitting. Otherwise "%APPEND% host" can
        # become a fake hostname and later generate duplicate %APPEND% markers.
        value = match.group(1).replace("%APPEND%", "")
        for item in value.split(","):
            host = item.strip()
            if host and host not in seen:
                seen.add(host)
                hosts.append(host)
    return hosts


def contains(host: str, keywords: tuple[str, ...]) -> bool:
    lowered = host.lower()
    return any(keyword in lowered for keyword in keywords)


def classify(hosts: list[str]) -> tuple[list[str], list[str], list[str], list[str]]:
    core: list[str] = []
    app: list[str] = []
    extended: list[str] = []
    sensitive: list[str] = []
    for host in hosts:
        if contains(host, SENSITIVE_KEYWORDS):
            sensitive.append(host)
        if contains(host, CORE_KEYWORDS):
            core.append(host)
        elif contains(host, APP_KEYWORDS):
            app.append(host)
        else:
            extended.append(host)
    return core, app, extended, sensitive


def render_mitm_file(title: str, hosts: list[str]) -> str:
    if not hosts:
        return f"# {title}\n# No hostname classified yet.\nhostname = %APPEND%\n"
    return f"# {title}\n# Generated from Rewrite/Sources/MITM.conf by scripts/split_mitm_sources.py.\nhostname = %APPEND% {','.join(hosts)}\n"


def main() -> None:
    hosts = parse_hosts(read(SOURCE))
    core, app, extended, sensitive = classify(hosts)
    dupes: list[str] = []

    write(CORE, render_mitm_file("MITM core layer: Spotify / YouTube / Zhihu and core playback/script hostnames", core))
    write(APP, render_mitm_file("MITM app-clean layer: common App ad-clean hostnames", app))
    write(EXTENDED, render_mitm_file("MITM extended layer: low-frequency or review-required hostnames", extended))

    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# MITM 分层报告",
        "",
        f"生成时间：{now}",
        "",
        f"- 原 MITM hostname 总数：{len(hosts)}",
        f"- core 数量：{len(core)}",
        f"- app-clean 数量：{len(app)}",
        f"- extended 数量：{len(extended)}",
        "- 未分类数量：0（未命中 core/app-clean 的 hostname 已进入 extended）",
        f"- 是否存在重复 hostname：{'是' if dupes else '否'}",
        f"- 疑似包含支付 / 登录 / 验证码 / 银行相关 hostname：{'是' if sensitive else '否'}",
        "- stable 使用哪些 MITM 文件：MITM-core.conf + MITM-app-clean.conf",
        "- lite 使用哪些 MITM 文件：MITM-core.conf",
        "- full 使用哪些 MITM 文件：MITM-core.conf + MITM-app-clean.conf + MITM-extended.conf",
        "- 回滚路径：保留 Rewrite/Sources/MITM.conf 原始完整列表；如 stable 出现漏拦截，可临时移除 profile 的 [mitm] 分层配置回到 legacy MITM.conf。",
        "",
        "## 分层文件",
        "",
        "- `Rewrite/Sources/MITM-core.conf`",
        "- `Rewrite/Sources/MITM-app-clean.conf`",
        "- `Rewrite/Sources/MITM-extended.conf`",
        "",
        "## 疑似敏感 hostname（前 100 条）",
        "",
    ]
    lines += [f"- `{host}`" for host in sensitive[:100]] or ["- 无"]
    if len(sensitive) > 100:
        lines.append(f"- 其余 {len(sensitive) - 100} 条省略")
    lines += [
        "",
        "## 风险说明",
        "",
        "- 本脚本只做分层，不删除 hostname。",
        "- 分层结果是关键词分类，不等于人工安全确认。",
        "- 切换 profile 使用分层 MITM 后，必须测试 Spotify、YouTube、知乎、登录、支付和验证码。",
        "- 疑似敏感 hostname 不应默认进入 stable；必要时保留在 extended 或删除。",
        "",
    ]
    write(REPORT, "\n".join(lines))
    print(f"MITM split files and report written under {ROOT}")


if __name__ == "__main__":
    main()
