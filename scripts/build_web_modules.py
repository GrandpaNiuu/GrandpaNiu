#!/usr/bin/env python3
"""Generate Web/modules.html from Release/Modules/README.md."""

from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "Release" / "Modules" / "README.md"
OUTPUT = ROOT / "Web" / "modules.html"
BASE_URL = "https://grandpaniuu.github.io/GrandpaNiu/Release/Modules/"
ROW_RE = re.compile(r"^\| (?P<name>.+?) \| `(?P<file>[^`]+)` \| `(?P<source>[^`]+)` \| (?P<sections>.+?) \|$")


def read_modules() -> list[dict[str, str]]:
    modules: list[dict[str, str]] = []
    if not INDEX.exists():
        return modules
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        match = ROW_RE.match(line.strip())
        if not match or match.group("file") == "File":
            continue
        modules.append(match.groupdict())
    return modules


def module_card(item: dict[str, str]) -> str:
    name = html.escape(item["name"])
    file = html.escape(item["file"])
    source = html.escape(item["source"])
    sections = html.escape(item["sections"])
    url = BASE_URL + item["file"]
    slug = item["file"].removesuffix(".sgmodule")
    install = "shadowrocket://install?module=" + url
    return f"""
        <article class=\"card\" data-url=\"{html.escape(url)}\">
          <h3>{name}</h3>
          <p>来源：<code>{source}</code></p>
          <div class=\"tags\"><span class=\"tag\">{html.escape(slug)}</span><span class=\"tag\">{sections}</span></div>
          <div class=\"actions\">
            <a class=\"badge-btn install\" href=\"{html.escape(install)}\"><span class=\"label\">↪ 安装模块</span><span class=\"name\">Module</span></a>
            <a class=\"badge-btn file\" href=\"../Release/Modules/{file}\"><span class=\"label\">▰ 模块文件</span><span class=\"name\">File</span></a>
            <button class=\"badge-btn gray\" type=\"button\"><span class=\"label\">复制链接</span><span class=\"name\">URL</span></button>
          </div>
        </article>"""


def build_html(modules: list[dict[str, str]]) -> str:
    cards = "\n".join(module_card(item) for item in modules)
    count = len(modules)
    return f"""<!doctype html>
<html lang=\"zh-CN\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">
  <meta name=\"color-scheme\" content=\"dark\">
  <title>GrandpaNiu 独立模块目录</title>
  <style>
    :root{{--bg:#15171d;--line:rgba(255,255,255,.12);--text:#f7f8fb;--muted:#a5a9b8;--blue:#2388d9;--green:#25a162;--gray:#4b5563;--nav:rgba(31,34,44,.86)}}
    *{{box-sizing:border-box}}body{{margin:0;min-height:100%;padding:max(24px,env(safe-area-inset-top)) 16px calc(100px + env(safe-area-inset-bottom));background:radial-gradient(circle at 18% -8%,rgba(35,136,217,.18),transparent 34%),radial-gradient(circle at 92% 0%,rgba(37,161,98,.12),transparent 30%),var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,\"SF Pro Display\",\"PingFang SC\",\"Microsoft YaHei\",Arial,sans-serif}}.wrap{{width:min(100%,980px);margin:0 auto}}header{{padding:10px 0 22px}}.eyebrow{{display:inline-flex;align-items:center;gap:8px;margin-bottom:14px;padding:7px 11px;border:1px solid var(--line);border-radius:999px;color:#d7eaff;background:rgba(35,136,217,.12);font-size:13px;font-weight:800}}h1{{margin:0;font-size:clamp(34px,8.8vw,58px);line-height:1.05;letter-spacing:-.06em;font-weight:900}}.lead{{margin:15px 0 0;color:var(--muted);font-size:clamp(17px,4.2vw,22px);line-height:1.65;font-weight:520}}.notice{{margin:16px 0 0;padding:13px 14px;border-radius:14px;border:1px solid rgba(214,164,77,.26);background:rgba(214,164,77,.09);color:#dfbf82;line-height:1.7;font-size:14px;font-weight:750}}.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:18px}}.card{{border:1px solid var(--line);border-radius:20px;padding:16px;background:linear-gradient(180deg,rgba(255,255,255,.075),rgba(255,255,255,.045));box-shadow:0 14px 34px rgba(0,0,0,.2)}}.card h3{{margin:0 0 8px;font-size:20px;line-height:1.25}}.card p{{margin:0;color:var(--muted);line-height:1.7;font-size:14px}}code{{font-size:12px;color:#cbd5e1;word-break:break-all}}.tags{{display:flex;flex-wrap:wrap;gap:6px;margin:11px 0 0}}.tag{{display:inline-flex;align-items:center;min-height:24px;padding:3px 8px;border:1px solid rgba(255,255,255,.1);border-radius:999px;background:rgba(255,255,255,.07);color:#d1d5db;font-size:12px;font-weight:750}}.actions{{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}}.badge-btn{{display:inline-flex;align-items:stretch;height:32px;color:#fff;text-decoration:none;border:0;border-radius:5px;overflow:hidden;font:inherit;font-size:14px;font-weight:800;line-height:32px;cursor:pointer;box-shadow:inset 0 1px 0 rgba(255,255,255,.18);background:transparent;padding:0}}.badge-btn .label,.badge-btn .name{{display:inline-flex;align-items:center;gap:6px;padding:0 9px;white-space:nowrap}}.badge-btn.install .label{{background:var(--blue)}}.badge-btn.install .name{{background:var(--gray)}}.badge-btn.file .label{{background:var(--green)}}.badge-btn.file .name{{background:var(--gray)}}.badge-btn.gray .label{{background:#6b7280}}.badge-btn.gray .name{{background:#4b5563}}footer{{margin:26px 0 0;color:#7f8494;font-size:13px;line-height:1.7;text-align:center}}.bottom-nav{{position:fixed;left:50%;bottom:max(14px,env(safe-area-inset-bottom));transform:translateX(-50%);width:min(calc(100% - 28px),760px);display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:4px;padding:8px;border:1px solid rgba(255,255,255,.13);border-radius:30px;background:var(--nav);box-shadow:0 18px 48px rgba(0,0,0,.45);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);z-index:10}}.bottom-nav a{{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;min-height:58px;border-radius:22px;color:#e5e7eb;text-decoration:none;font-size:12px;font-weight:750}}.bottom-nav a.active{{color:#58a6ff;background:rgba(47,156,255,.16)}}.nav-icon{{font-size:22px;line-height:1}}@media(max-width:860px){{.grid{{grid-template-columns:1fr}}}}
  </style>
</head>
<body>
  <main class=\"wrap\" id=\"top\">
    <header>
      <div class=\"eyebrow\">🐮 GrandpaNiu · Release Modules</div>
      <h1>独立模块目录</h1>
      <p class=\"lead\">当前共 {count} 个独立模块。主入口仍然推荐 Fusion；这里适合高级用户按 App 单独导入和测试。</p>
      <div class=\"notice\">不要同时导入太多独立模块。普通用户优先使用主融合模块。</div>
    </header>
    <section class=\"grid\">{cards}
    </section>
    <footer>本页面由 scripts/build_web_modules.py 从 Release/Modules/README.md 生成。</footer>
  </main>
  <nav class=\"bottom-nav\" aria-label=\"底部导航\"><a class=\"active\" href=\"#top\"><span class=\"nav-icon\">⌂</span><span>顶部</span></a><a href=\"../import.html\"><span class=\"nav-icon\">↪</span><span>主模块</span></a><a href=\"../android.html\"><span class=\"nav-icon\">▱</span><span>Android</span></a></nav>
  <script>document.addEventListener('click',function(e){{const b=e.target.closest('button');if(!b)return;const card=b.closest('[data-url]');if(!card)return;navigator.clipboard.writeText(card.dataset.url).then(function(){{alert('已复制')}}).catch(function(){{prompt('复制模块链接',card.dataset.url)}});}});</script>
</body>
</html>
"""


def main() -> None:
    modules = read_modules()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(build_html(modules), encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT.relative_to(ROOT)} with {len(modules)} modules")


if __name__ == "__main__":
    main()
