#!/usr/bin/env python3
"""Generate a conservative change impact report from local file timestamps."""

from __future__ import annotations

import datetime as dt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "change_impact_report.md"

APP_KEYWORDS = {
    "Spotify": ["spotify", "spclient"],
    "YouTube": ["youtube", "googlevideo"],
    "知乎": ["zhihu"],
    "Bilibili": ["bilibili", "biliapi"],
    "微博": ["weibo"],
    "百度贴吧": ["tieba"],
    "小红书": ["xiaohongshu", "xhscdn"],
    "酷安": ["coolapk"],
    "淘宝": ["taobao"],
    "闲鱼": ["goofish", "idle"],
    "京东": ["jd"],
    "拼多多": ["pinduoduo", "yangkeduo"],
    "美团": ["meituan"],
    "大众点评": ["dianping"],
    "饿了么": ["ele.me", "eleme"],
    "滴滴": ["didi", "xiaojukeji"],
    "12306": ["12306"],
    "高德地图": ["amap"],
    "百度地图": ["map.baidu"],
    "网易云音乐": ["music.163"],
    "喜马拉雅": ["ximalaya", "xmly"],
    "小宇宙": ["xiaoyuzhou"],
    "斗鱼": ["douyu"],
    "Reddit": ["reddit"],
}


def tracked_files() -> list[Path]:
    paths: list[Path] = []
    for pattern in [
        "Rules/*.list",
        "Scripts/*.conf",
        "Scripts/*.js",
        "Rewrite/Sources/*.conf",
        "Rewrite/Remotes/*.json",
        "Rewrite/Profiles/*.conf",
        ".github/workflows/*.yml",
        "docs/*.md",
        "*.md",
    ]:
        paths.extend(ROOT.glob(pattern))
    return sorted(set(path for path in paths if path.is_file()), key=lambda p: p.stat().st_mtime, reverse=True)


def layer_for(path: Path) -> str:
    rel = str(path.relative_to(ROOT)).replace("\\", "/")
    if rel.startswith("Rules/"):
        return "Rules"
    if rel.startswith("Scripts/"):
        return "Scripts"
    if rel.startswith("Rewrite/Sources/MITM"):
        return "MITM"
    if rel.startswith("Rewrite/Sources/"):
        return "Rewrite/Sources"
    if rel.startswith("Rewrite/Remotes/"):
        return "Remotes"
    if rel.startswith("Rewrite/Profiles/"):
        return "Profiles"
    if rel.startswith(".github/workflows/"):
        return "Workflows"
    if rel.startswith("docs/") or rel in {"README.md", "CHANGELOG.md", "SECURITY.md", "CONTRIBUTING.md", "LICENSE"}:
        return "README/docs"
    return "Other"


def app_hits(paths: list[Path]) -> list[str]:
    text = "\n".join(path.read_text(encoding="utf-8", errors="replace").lower() for path in paths[:30])
    hits = [app for app, keywords in APP_KEYWORDS.items() if any(keyword.lower() in text for keyword in keywords)]
    return hits or ["待人工确认"]


def main() -> None:
    files = tracked_files()
    recent = files[:30]
    rels = [str(path.relative_to(ROOT)).replace("\\", "/") for path in recent]
    layers = sorted({layer_for(path) for path in recent})
    apps = app_hits(recent)
    rel_text = "\n".join(rels).lower()
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# 变更影响报告",
        "",
        f"- 生成时间：{today}",
        "- 说明：无 git 工作树时，本报告基于最近修改文件时间生成；如需精确变更，请结合提交 diff 人工确认。",
        "",
        "## 本次修改文件",
        "",
    ]
    lines += [f"- `{rel}`" for rel in rels] or ["- 待人工确认"]
    lines += [
        "",
        "## 影响的模块层",
        "",
    ]
    lines += [f"- {layer}" for layer in layers] or ["- 待人工确认"]
    lines += ["", "## 可能影响的 App", ""]
    lines += [f"- {app}" for app in apps]
    lines += [
        "",
        "## 风险判断",
        "",
        f"- 是否涉及脚本：{'是' if 'Scripts' in layers else '否'}",
        f"- 是否涉及 MITM：{'是' if 'MITM' in layers else '否'}",
        f"- 是否涉及 Body Rewrite：{'是' if 'body-rewrite' in rel_text.lower() else '否'}",
        f"- 是否涉及远程规则源：{'是' if 'Remotes' in layers else '否'}",
        f"- 是否需要测试 Spotify：{'是' if 'Spotify' in apps or 'Scripts' in layers or 'MITM' in layers else '按需'}",
        f"- 是否需要测试 YouTube：{'是' if 'YouTube' in apps or 'Scripts' in layers or 'MITM' in layers else '按需'}",
        f"- 是否需要测试知乎：{'是' if '知乎' in apps or 'Scripts' in layers else '按需'}",
        f"- 是否需要测试登录/支付/验证码：{'是' if any(layer in layers for layer in ['Scripts', 'MITM', 'Rewrite/Sources']) else '按需'}",
        "",
        "## 回滚建议",
        "",
        "- 优先回滚最近一次提交。",
        "- 若主模块导入异常，可用 `backup/Ronghemokuai.stable.sgmodule` 人工恢复。",
        "- 回滚后运行 `build_module.py --build --profile stable`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Change impact report written to {REPORT}")


if __name__ == "__main__":
    main()
