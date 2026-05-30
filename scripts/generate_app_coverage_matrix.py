#!/usr/bin/env python3
"""Generate an approximate App/service coverage matrix."""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "app_coverage_matrix.md"

APPS = {
    "Spotify": ["spotify", "spclient"],
    "YouTube": ["youtube", "googlevideo", "youtubei"],
    "知乎": ["zhihu", "zhihu.com", "zhihu-enhance"],
    "Bilibili": ["bilibili", "biliapi"],
    "微博": ["weibo"],
    "百度贴吧": ["tieba", "tiebac"],
    "小红书": ["xiaohongshu", "xhscdn", "edith"],
    "酷安": ["coolapk"],
    "淘宝": ["taobao", "tmall"],
    "闲鱼": ["goofish", "idle"],
    "京东": ["jd.com", "jdcloud", "jingdong"],
    "拼多多": ["pinduoduo", "yangkeduo"],
    "美团": ["meituan"],
    "大众点评": ["dianping"],
    "饿了么": ["ele.me", "eleme"],
    "滴滴": ["diditaxi", "xiaojukeji", "didi"],
    "12306": ["12306"],
    "高德地图": ["amap"],
    "百度地图": ["map.baidu", "baidu.com"],
    "网易云音乐": ["music.163", "netease"],
    "喜马拉雅": ["ximalaya", "xmly"],
    "小宇宙": ["xiaoyuzhou"],
    "斗鱼": ["douyu"],
    "Reddit": ["reddit"],
}

SOURCE_GROUPS = [
    ("Rule", list((ROOT / "Rules").glob("*.list"))),
    ("Script", list((ROOT / "Scripts").glob("*.conf"))),
    ("URL Rewrite", [ROOT / "Rewrite" / "Sources" / "URL-Rewrite.conf"]),
    ("Header Rewrite", [ROOT / "Rewrite" / "Sources" / "Header-Rewrite.conf"]),
    ("Body Rewrite", [ROOT / "Rewrite" / "Sources" / "Body-Rewrite.conf"]),
    ("Map Local", [ROOT / "Rewrite" / "Sources" / "Map-Local.conf"]),
    ("MITM", [ROOT / "Rewrite" / "Sources" / "MITM.conf"]),
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def source_hits(keywords: list[str]) -> tuple[set[str], set[str]]:
    methods: set[str] = set()
    files: set[str] = set()
    lowered_keywords = [item.lower() for item in keywords]
    for method, paths in SOURCE_GROUPS:
        for path in paths:
            text = read(path)
            lowered = text.lower()
            if any(keyword in lowered for keyword in lowered_keywords):
                methods.add(method)
                files.add(str(path.relative_to(ROOT)).replace("\\", "/"))
    sources = json.loads(read(ROOT / "Rewrite" / "Remotes" / "sources.json") or "{}")
    remote_text = json.dumps(sources, ensure_ascii=False).lower()
    if any(keyword in remote_text for keyword in lowered_keywords):
        methods.add("Remote Rule")
        files.add("Rewrite/Remotes/sources.json")
    return methods, files


def strength(app: str, methods: set[str]) -> str:
    if app in {"Spotify", "YouTube", "知乎"} and ("Script" in methods or "MITM" in methods):
        return "重点专项"
    if "Script" in methods or "Body Rewrite" in methods or "Map Local" in methods:
        return "明确覆盖"
    if "Rule" in methods or "URL Rewrite" in methods or "MITM" in methods:
        return "局部覆盖"
    if "Remote Rule" in methods:
        return "远程规则覆盖"
    return "待确认"


def risk(methods: set[str]) -> str:
    if "MITM" in methods or "Script" in methods or "Body Rewrite" in methods:
        return "高"
    if "URL Rewrite" in methods or "Map Local" in methods:
        return "中"
    return "低"


def main() -> None:
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
    lines = [
        "# App 覆盖矩阵",
        "",
        f"- 日期：{today}",
        "- 说明：本报告由静态关键词扫描生成，覆盖强度用于维护参考，不代表完整功能承诺。",
        "",
        "| App / 服务 | 覆盖方式 | 覆盖强度 | 风险等级 | 来源文件 | 是否需要手动测试 |",
        "|---|---|---|---|---|---|",
    ]
    for app, keywords in APPS.items():
        methods, files = source_hits(keywords)
        method_text = ", ".join(sorted(methods)) if methods else "待确认"
        file_text = "<br>".join(sorted(files)) if files else "待人工确认"
        risk_level = risk(methods)
        need_test = "是" if risk_level in {"中", "高"} or app in {"Spotify", "YouTube", "知乎"} else "按需"
        lines.append(f"| {app} | {method_text} | {strength(app, methods)} | {risk_level} | {file_text} | {need_test} |")
    lines += [
        "",
        "## 后续改进",
        "",
        "- 新增 App 规则或脚本后，应补充关键词映射。",
        "- 高风险项需要在 Shadowrocket 中手动验证登录、支付、验证码和核心播放链路。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"App coverage matrix written to {REPORT}")


if __name__ == "__main__":
    main()
