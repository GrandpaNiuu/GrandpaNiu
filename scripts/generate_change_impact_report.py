#!/usr/bin/env python3
"""Generate a change impact report.

The script prefers git diff for precision. If git history is unavailable in the
runtime, it falls back to recent file timestamps and states that clearly.
"""

from __future__ import annotations

import datetime as dt
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "change_impact_report.md"

APP_KEYWORDS = {
    "Spotify": ["spotify", "spclient"],
    "YouTube": ["youtube", "googlevideo", "youtubei"],
    "知乎": ["zhihu", "zhihu-enhance"],
    "Bilibili": ["bilibili", "biliapi"],
    "微博": ["weibo"],
    "百度贴吧": ["tieba"],
    "小红书": ["xiaohongshu", "xhscdn", "edith"],
    "酷安": ["coolapk"],
    "淘宝": ["taobao", "tmall"],
    "闲鱼": ["goofish", "idle"],
    "京东": ["jd", "jingdong"],
    "拼多多": ["pinduoduo", "yangkeduo"],
    "美团": ["meituan"],
    "大众点评": ["dianping"],
    "饿了么": ["ele.me", "eleme"],
    "滴滴": ["didi", "xiaojukeji"],
    "12306": ["12306"],
    "高德地图": ["amap"],
    "百度地图": ["map.baidu"],
    "网易云音乐": ["music.163", "netease"],
    "喜马拉雅": ["ximalaya", "xmly"],
    "小宇宙": ["xiaoyuzhou"],
    "斗鱼": ["douyu"],
    "Reddit": ["reddit"],
}

TRACKED_PATTERNS = [
    "Rules/*.list",
    "Scripts/*.conf",
    "Scripts/*.js",
    "Rewrite/Sources/*.conf",
    "Rewrite/Remotes/*.json",
    "Rewrite/Profiles/*.conf",
    ".github/workflows/*.yml",
    "scripts/*.py",
    "docs/*.md",
    "reports/*.md",
    "*.md",
    "LICENSE",
]


def run_git(args: list[str]) -> tuple[bool, str]:
    proc = subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True)
    text = (proc.stdout + proc.stderr).strip()
    return proc.returncode == 0, text


def git_changed_files() -> tuple[str, list[str], list[str], list[str], str]:
    ok, names = run_git(["diff", "--name-status", "HEAD~1..HEAD"])
    if not ok or not names:
        return fallback_changed_files()
    added: list[str] = []
    modified: list[str] = []
    deleted: list[str] = []
    changed: list[str] = []
    for line in names.splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        status, path = parts[0], parts[-1]
        changed.append(path)
        if status.startswith("A"):
            added.append(path)
        elif status.startswith("D"):
            deleted.append(path)
        else:
            modified.append(path)
    _, diff_text = run_git(["diff", "HEAD~1..HEAD"])
    return "git diff 精准模式", added, modified, deleted, diff_text


def fallback_changed_files() -> tuple[str, list[str], list[str], list[str], str]:
    paths: list[Path] = []
    for pattern in TRACKED_PATTERNS:
        paths.extend(ROOT.glob(pattern))
    recent = sorted(set(path for path in paths if path.is_file()), key=lambda p: p.stat().st_mtime, reverse=True)[:30]
    rels = [str(path.relative_to(ROOT)).replace("\\", "/") for path in recent]
    text = "\n".join(path.read_text(encoding="utf-8", errors="replace") for path in recent)
    return "fallback 最近修改时间模式", [], rels, [], text


def layer_for(rel: str) -> str:
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
    if rel.startswith("docs/") or rel.startswith("reports/") or rel in {"README.md", "CHANGELOG.md", "SECURITY.md", "CONTRIBUTING.md", "LICENSE"}:
        return "README/docs"
    if rel.startswith("scripts/"):
        return "Scripts/maintenance"
    return "Other"


def app_hits(text: str, files: list[str]) -> list[str]:
    combined = (text + "\n" + "\n".join(files)).lower()
    hits = [app for app, keywords in APP_KEYWORDS.items() if any(keyword.lower() in combined for keyword in keywords)]
    return hits or ["待人工确认"]


def bullet(items: list[str]) -> list[str]:
    return [f"- `{item}`" for item in items] if items else ["- 无"]


def main() -> None:
    mode, added, modified, deleted, diff_text = git_changed_files()
    changed = sorted(set(added + modified + deleted))
    layers = sorted({layer_for(path) for path in changed})
    apps = app_hits(diff_text, changed)
    rel_text = "\n".join(changed).lower() + "\n" + diff_text.lower()
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# 变更影响报告",
        "",
        f"- 生成时间：{today}",
        f"- 变更识别模式：{mode}",
        "",
        "## 本次修改文件",
        "",
    ]
    lines += bullet(changed)
    lines += ["", "## 新增文件", ""] + bullet(added)
    lines += ["", "## 删除文件", ""] + bullet(deleted)
    lines += ["", "## 修改文件", ""] + bullet(modified)
    lines += ["", "## 影响的模块层", ""]
    lines += [f"- {layer}" for layer in layers] or ["- 待人工确认"]
    lines += ["", "## 可能影响的 App", ""]
    lines += [f"- {app}" for app in apps]
    lines += [
        "",
        "## 风险判断",
        "",
        f"- 是否涉及脚本：{'是' if 'Scripts' in layers or 'Scripts/maintenance' in layers else '否'}",
        f"- 是否涉及 MITM：{'是' if 'MITM' in layers or 'mitm' in rel_text else '否'}",
        f"- 是否涉及 Body Rewrite：{'是' if 'body-rewrite' in rel_text or 'body rewrite' in rel_text else '否'}",
        f"- 是否涉及远程规则源：{'是' if 'Remotes' in layers or 'sources.json' in rel_text or 'candidates.json' in rel_text else '否'}",
        f"- 是否需要测试 Spotify：{'是' if 'Spotify' in apps or 'Scripts' in layers or 'MITM' in layers else '按需'}",
        f"- 是否需要测试 YouTube：{'是' if 'YouTube' in apps or 'Scripts' in layers or 'MITM' in layers else '按需'}",
        f"- 是否需要测试知乎：{'是' if '知乎' in apps or 'Scripts' in layers or 'zhihu' in rel_text else '按需'}",
        f"- 是否需要测试登录/支付/验证码：{'是' if any(layer in layers for layer in ['Scripts', 'MITM', 'Rewrite/Sources']) else '按需'}",
        "",
        "## 回滚建议",
        "",
        "- 优先回滚最近一次提交。",
        "- 若主模块导入异常，优先回滚最近一次 Fusion 输出提交。",
        "- 回滚后运行 `build_module.py --build --profile fusion`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Change impact report written to {REPORT}")


if __name__ == "__main__":
    main()
