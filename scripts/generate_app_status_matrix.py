#!/usr/bin/env python3
"""Generate an App status matrix from automated repository evidence."""

from __future__ import annotations

import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "app_status_matrix.md"

APPS = [
    ("Spotify", "音乐", ["spotify", "spclient"], "中"),
    ("YouTube", "视频", ["youtube", "youtubei", "googlevideo"], "中"),
    ("知乎", "内容社区", ["zhihu", "zhihu-enhance"], "中"),
    ("Bilibili", "视频", ["bilibili", "biliapi", "hdslb"], "中"),
    ("微博", "社交", ["weibo"], "中"),
    ("百度贴吧", "社交", ["tieba", "tiebac"], "中"),
    ("小红书", "社交电商", ["xiaohongshu", "xhscdn", "edith"], "中"),
    ("酷安", "工具社区", ["coolapk"], "中"),
    ("淘宝", "电商", ["taobao", "tmall", "alicdn"], "高"),
    ("闲鱼", "电商", ["goofish", "idle"], "中"),
    ("京东", "电商", ["jd.com", "jingdong", "360buyimg", "jdimg"], "高"),
    ("拼多多", "电商", ["pinduoduo", "yangkeduo", "pddpic"], "高"),
    ("美团", "本地生活", ["meituan"], "高"),
    ("大众点评", "本地生活", ["dianping", "dpfile"], "高"),
    ("饿了么", "本地生活", ["ele.me", "eleme"], "高"),
    ("滴滴", "出行", ["diditaxi", "xiaojukeji", "didi"], "高"),
    ("12306", "出行", ["12306"], "高"),
    ("高德地图", "地图", ["amap"], "高"),
    ("百度地图", "地图", ["map.baidu", "baidu.com"], "高"),
    ("网易云音乐", "音乐", ["music.163", "netease"], "中"),
    ("喜马拉雅", "音频", ["ximalaya", "xmly"], "中"),
    ("小宇宙", "音频", ["xiaoyuzhou"], "中"),
    ("斗鱼", "直播", ["douyu"], "中"),
    ("Reddit", "社交", ["reddit"], "低"),
    ("微信", "社交 / 支付 / 小程序 / 图片", ["weixin", "wechat", "wxs.qq.com", "servicewechat", "wechatpay", "qpic", "gtimg", "qlogo"], "高"),
    ("支付宝", "支付", ["alipay"], "高"),
    ("银行 / 验证码", "安全敏感", ["bank", "captcha", "verify", "passport"], "高"),
    ("图片 CDN", "资源加载", ["qpic", "gtimg", "alicdn", "pddpic", "360buyimg", "jdimg", "biliimg", "hdslb", "dpfile"], "高"),
    ("小程序资源", "微信生态", ["servicewechat", "wxapp.tc.qq.com"], "高"),
]

SOURCE_FILES = {
    "Rule": [ROOT / "Rules"],
    "Script": [ROOT / "Scripts"],
    "Rewrite": [ROOT / "Rewrite" / "Sources"],
    "MITM": [
        ROOT / "Rewrite" / "Sources" / "MITM-core.conf",
        ROOT / "Rewrite" / "Sources" / "MITM-app-clean.conf",
        ROOT / "Rewrite" / "Sources" / "MITM-stable-plus.conf",
        ROOT / "Rewrite" / "Sources" / "MITM-extended.conf",
    ],
    "Remote": [ROOT / "Rewrite" / "Remotes" / "sources.json"],
}

PROFILE_FILES = {
    "fusion": ROOT / "Rewrite" / "Profiles" / "fusion.conf",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def collect_text(path: Path) -> str:
    if not path.exists():
        return ""
    if path.is_file():
        return read(path)
    return "\n".join(read(item) for item in path.rglob("*") if item.is_file())


def source_hits(keywords: list[str]) -> tuple[list[str], list[str]]:
    methods: list[str] = []
    files: list[str] = []
    lowered_keywords = [item.lower() for item in keywords]
    for method, paths in SOURCE_FILES.items():
        matched = False
        for path in paths:
            text = collect_text(path).lower()
            if any(keyword in text for keyword in lowered_keywords):
                matched = True
                if path.is_dir():
                    for item in path.rglob("*"):
                        if item.is_file() and any(keyword in read(item).lower() for keyword in lowered_keywords):
                            files.append(item.relative_to(ROOT).as_posix())
                else:
                    files.append(path.relative_to(ROOT).as_posix())
        if matched:
            methods.append(method)
    return sorted(set(methods)), sorted(set(files))


def profile_hits(files: list[str]) -> list[str]:
    result: list[str] = []
    for profile, path in PROFILE_FILES.items():
        text = read(path)
        if any(file_name in text for file_name in files):
            result.append(profile)
    return result


def automation_status(methods: list[str]) -> str:
    return "自动门禁覆盖" if methods else "未发现自动覆盖"


def release_decision(risk: str, methods: list[str]) -> str:
    if not methods:
        return "不进入发布输出"
    if risk == "高":
        return "保留保护优先、需可回滚源头"
    return "随 Fusion 自动门禁发布"


def rollback_path(files: list[str]) -> str:
    if not files:
        return "从候选或对应源文件移除后重建"
    roots = sorted({file.split("/", 1)[0] for file in files})
    return "回滚 " + "、".join(roots) + " 中对应源头后重建"


def main() -> None:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    rows: list[str] = []
    for app, category, keywords, base_risk in APPS:
        methods, files = source_hits(keywords)
        profiles = profile_hits(files)
        risk = "高" if app in {"微信", "支付宝", "银行 / 验证码", "图片 CDN", "小程序资源"} else base_risk
        rows.append(
            "| {app} | {category} | {methods} | {profiles} | {status} | {risk} | {source} | {allowed} | {rollback} | {note} |".format(
                app=app,
                category=category,
                methods=", ".join(methods) if methods else "未发现",
                profiles=", ".join(profiles) if profiles else "未确认",
                status=automation_status(methods),
                risk=risk,
                source="automated_quality_evidence.md / 静态扫描",
                allowed=release_decision(risk, methods),
                rollback=rollback_path(files),
                note="覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入",
            )
        )

    lines = [
        "# App 状态矩阵",
        "",
        f"生成时间：{now}",
        "",
        "本矩阵是自动化质量总览。状态只表达仓库源头是否被自动扫描覆盖，以及是否满足可回滚、可审计的发布边界。",
        "",
        "| App 名称 | 所属类别 | 覆盖来源 | 所属入口 | 自动状态 | 风险等级 | 证据来源 | 发布策略 | 回滚路径 | 备注 |",
        "|---|---|---|---|---|---|---|---|---|---|",
        *rows,
        "",
        "## 发布边界",
        "",
        "- 静态覆盖不得写成效果承诺。",
        "- 用户反馈不是发布阻断门禁；它只作为 Issue、回滚或修复输入。",
        "- 高风险 App 保持保护规则优先、回滚路径明确、自动门禁通过。",
        "- Fusion 是唯一公开入口；兼容目录只由构建器同步。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"App status matrix written to {REPORT}")


if __name__ == "__main__":
    main()
