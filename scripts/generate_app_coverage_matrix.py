#!/usr/bin/env python3
"""Generate an App/service coverage and test matrix."""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "app_coverage_matrix.md"
MANUAL_LOG = ROOT / "reports" / "manual_test_log.md"

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

TEST_ITEMS = {
    "Spotify": "连续播放、切歌、搜索、歌单加载",
    "YouTube": "首页、搜索、播放、Shorts、评论区",
    "知乎": "首页、回答页、搜索、评论、点赞、收藏",
    "Bilibili": "首页、搜索、播放页、评论区",
    "淘宝": "首页、搜索、商品详情、购物车、订单页",
    "闲鱼": "首页、搜索、商品详情、聊天入口",
    "京东": "首页、搜索、商品详情、购物车、订单页",
    "拼多多": "首页、搜索、商品详情、订单页",
    "美团": "首页、搜索、店铺页、下单前置页面",
    "大众点评": "首页、搜索、店铺页、评价页",
    "饿了么": "首页、搜索、店铺页、下单前置页面",
    "滴滴": "首页、定位、路线、订单查询",
    "12306": "首页、车票查询、订单查询",
    "高德地图": "首页、搜索、路线规划",
    "百度地图": "首页、搜索、路线规划",
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


def risk(app: str, methods: set[str]) -> str:
    if app in {"Spotify", "YouTube", "知乎"}:
        return "高"
    if "MITM" in methods or "Body Rewrite" in methods:
        return "高"
    if "Script" in methods or "URL Rewrite" in methods or "Map Local" in methods:
        return "中"
    return "低"


def test_status(app: str) -> tuple[str, str]:
    text = read(MANUAL_LOG)
    if not text or app not in text:
        return "未测", "未测试"
    for line in text.splitlines():
        if app in line and "|" in line:
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) >= 10 and cells[-1] in {"是", "否"}:
                date = cells[0] or "未测试"
                result = cells[7] or "未测"
                passed = cells[-1]
                if passed == "是" and result != "未测试":
                    return "已测通过", date
                if result not in {"未测试", ""} and passed == "否":
                    return "有异常", date
    return "未测", "未测试"


def main() -> None:
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
    lines = [
        "# App 覆盖矩阵",
        "",
        f"- 日期：{today}",
        "- 说明：本报告由静态关键词扫描生成，覆盖强度用于维护参考，不代表完整功能承诺。",
        "- 测试状态来自 `reports/manual_test_log.md`；没有真实记录时默认未测。",
        "",
        "| App / 服务 | 覆盖方式 | 覆盖强度 | 风险等级 | 来源文件 | 测试状态 | 最近测试日期 | 需要测试项目 | 备注 |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for app, keywords in APPS.items():
        methods, files = source_hits(keywords)
        method_text = ", ".join(sorted(methods)) if methods else "待确认"
        file_text = "<br>".join(sorted(files)) if files else "待人工确认"
        risk_level = risk(app, methods)
        status, date = test_status(app)
        test_item = TEST_ITEMS.get(app, "首页、搜索、详情页、核心流程")
        note = "高风险项需手动复测" if risk_level == "高" else "按需复测"
        lines.append(
            f"| {app} | {method_text} | {strength(app, methods)} | {risk_level} | {file_text} | {status} | {date} | {test_item} | {note} |"
        )
    lines += [
        "",
        "## 风险等级规则",
        "",
        "- 低：只涉及 Rule / Remote Rule，不涉及 MITM、Script 或 Body Rewrite。",
        "- 中：涉及 URL Rewrite / Map Local / Script，但不直接命中敏感风险域。",
        "- 高：涉及 MITM、Body Rewrite、大型 JSON、视频播放链路、账号相关接口，或属于 Spotify / YouTube / 知乎等核心链路。",
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
