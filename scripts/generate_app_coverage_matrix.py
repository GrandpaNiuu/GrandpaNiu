#!/usr/bin/env python3
"""Generate an App/service static coverage matrix."""

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

OBSERVATION_ITEMS = {
    "Spotify": "播放、切歌、搜索、歌单加载由用户反馈或 Issue 观察，不作为自动门禁。",
    "YouTube": "首页、搜索、播放、Shorts、评论区由用户反馈或 Issue 观察，不作为自动门禁。",
    "知乎": "首页、回答页、搜索、评论、点赞、收藏由用户反馈或 Issue 观察，不作为自动门禁。",
    "淘宝": "首页、搜索、商品详情、购物车、订单页由用户反馈或 Issue 观察，不作为自动门禁。",
    "京东": "首页、搜索、商品详情、购物车、订单页由用户反馈或 Issue 观察，不作为自动门禁。",
    "拼多多": "首页、搜索、商品详情、订单页由用户反馈或 Issue 观察，不作为自动门禁。",
}


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
                files.add(path.relative_to(ROOT).as_posix())
    sources = json.loads(read(ROOT / "Rewrite" / "Remotes" / "sources.json") or "{}")
    remote_text = json.dumps(sources, ensure_ascii=False).lower()
    if any(keyword in remote_text for keyword in lowered_keywords):
        methods.add("Remote Rule")
        files.add("Rewrite/Remotes/sources.json")
    return methods, files


def strength(app: str, methods: set[str]) -> str:
    if app in {"Spotify", "YouTube", "知乎"} and ("Script" in methods or "MITM" in methods):
        return "重点覆盖"
    if "Script" in methods or "Body Rewrite" in methods or "Map Local" in methods:
        return "明确覆盖"
    if "Rule" in methods or "URL Rewrite" in methods or "MITM" in methods:
        return "局部覆盖"
    if "Remote Rule" in methods:
        return "远程规则覆盖"
    return "待确认"


def risk(app: str, methods: set[str]) -> str:
    if app in {"Spotify", "YouTube", "知乎"}:
        return "高"
    if "MITM" in methods or "Body Rewrite" in methods:
        return "高"
    if "Script" in methods or "URL Rewrite" in methods or "Map Local" in methods:
        return "中"
    return "低"


def automation_status(methods: set[str]) -> str:
    return "自动扫描已覆盖" if methods else "自动扫描未命中"


def main() -> None:
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
    lines = [
        "# App 覆盖矩阵",
        "",
        f"- 日期：{today}",
        "- 说明：本报告由静态关键词扫描生成，覆盖强度用于维护参考，不代表完整功能承诺。",
        "- 质量来源：发布门禁只依赖 `reports/automated_quality_evidence.md` 和可重复运行的自动化校验。",
        "",
        "| App / 服务 | 覆盖方式 | 覆盖强度 | 风险等级 | 来源文件 | 自动证据状态 | 观察项目 | 备注 |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for app, keywords in APPS.items():
        methods, files = source_hits(keywords)
        method_text = ", ".join(sorted(methods)) if methods else "待确认"
        file_text = "<br>".join(sorted(files)) if files else "待补充源头"
        risk_level = risk(app, methods)
        observation = OBSERVATION_ITEMS.get(app, "首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。")
        note = "高风险项必须保留保护规则和回滚路径" if risk_level == "高" else "按自动门禁维护"
        lines.append(
            f"| {app} | {method_text} | {strength(app, methods)} | {risk_level} | {file_text} | {automation_status(methods)} | {observation} | {note} |"
        )
    lines += [
        "",
        "## 风险等级规则",
        "",
        "- 低：只涉及 Rule / Remote Rule，不涉及 MITM、Script 或 Body Rewrite。",
        "- 中：涉及 URL Rewrite / Map Local / Script，但不直接命中敏感风险域。",
        "- 高：涉及 MITM、Body Rewrite、大型 JSON、视频播放链路、账号相关接口，或属于 Spotify / YouTube / 知乎等核心链路。",
        "",
        "## 处理原则",
        "",
        "- 覆盖存在不等于效果承诺。",
        "- 用户反馈进入 Issue 或变更记录，但不作为发布阻断门禁。",
        "- 发布前以自动化质量证据和可回滚源头为准。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"App coverage matrix written to {REPORT}")


if __name__ == "__main__":
    main()
