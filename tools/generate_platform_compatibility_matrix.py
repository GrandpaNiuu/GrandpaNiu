#!/usr/bin/env python3
"""Generate a platform compatibility matrix for GrandpaNiu outputs."""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "platform_compatibility_matrix.md"


def exists(path: str) -> str:
    return "存在" if (ROOT / path).exists() else "缺失"


def count_app_modules() -> int:
    directory = ROOT / "Release" / "Modules"
    return len(list(directory.glob("*.sgmodule"))) if directory.exists() else 0


def android_branches() -> list[dict]:
    path = ROOT / "Android" / "branches.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    branches = data.get("branches", [])
    return branches if isinstance(branches, list) else []


def table(rows: list[list[str]]) -> list[str]:
    out = ["| 平台 / 客户端 | 推荐入口 | 支持能力 | 不支持 / 限制 | 状态 |", "|---|---|---|---|---|"]
    out.extend("| " + " | ".join(cell.replace("|", "\\|") for cell in row) + " |" for row in rows)
    return out


def main() -> int:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    branches = android_branches()
    branch_rows = [
        f"- `{branch.get('id')}`：`{branch.get('target')}` / `{branch.get('release_target')}`，规则数 `{branch.get('rule_count')}`"
        for branch in branches
        if isinstance(branch, dict)
    ]
    rows = [
        [
            "iOS Shadowrocket",
            "`https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule`",
            "Rule、URL/Header/Body Rewrite、Map Local、Script、MITM、二进制 body 参数",
            "依赖 Shadowrocket 模块解析能力；需要用户本机证书和可用策略组",
            exists("Ronghemokuai.sgmodule"),
        ],
        [
            "Surge",
            "`Release/Ronghemokuai.sgmodule` 或 App 独立模块",
            "Surge 风格 section 大体兼容；适合做规则和模块参考",
            "Shadowrocket 特有参数或客户端行为不能保证完全等价",
            exists("Release/Ronghemokuai.sgmodule"),
        ],
        [
            "Android Mihomo / Clash Meta / Clash Mi",
            "`Android/mihomo/GrandpaNiu-Ads.yaml`；完整配置参考 `Android/mihomo/GrandpaNiu-Android-Full.yaml`",
            "域名、关键词、IP、REJECT / DIRECT / PROXY 路由投影",
            "不能执行 iOS Script、MITM、Body Rewrite、Map Local；Clash Meta / Clash Mi 建议关闭分应用代理",
            exists("Android/mihomo/GrandpaNiu-Ads.yaml"),
        ],
        [
            "Android sing-box",
            "`Android/sing-box/GrandpaNiu-Ads.json`",
            "规则集 JSON 投影，适合路由 / 域名层拦截",
            "不能执行 iOS Script、MITM、Rewrite；只代表可迁移规则层",
            exists("Android/sing-box/GrandpaNiu-Ads.json"),
        ],
        [
            "Android AdGuard / DNS",
            "`Android/adguard/GrandpaNiu-DNS.txt`",
            "DNS / 域名过滤层",
            "不能处理路径级、body 级、脚本级净化；可能弱于 iOS 模块",
            exists("Android/adguard/GrandpaNiu-DNS.txt"),
        ],
        [
            "Android v2rayNG / V2Ray / Xray",
            "`Android/v2rayng/GrandpaNiu-v2rayng-routing.json`",
            "routing.rules 层拦截和直连 / 代理尾部规则",
            "不能执行 iOS Rewrite / Script；不是完整 App 净化模块",
            exists("Android/v2rayng/GrandpaNiu-v2rayng-routing.json"),
        ],
        [
            "Windows v2rayN",
            "`Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json`",
            "v2rayN 自定义路由 JSON 数组",
            "仅路由层；导入到 v2rayN 自定义规则，不是 iOS 模块",
            exists("Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json"),
        ],
        [
            "Release App Modules",
            "`Release/Modules/*.sgmodule`",
            f"按 App 拆分的独立模块，共 {count_app_modules()} 个",
            "用于单 App 调试和引用；公开主入口仍是 Fusion 单模块",
            exists("Release/Modules/README.md"),
        ],
    ]
    lines = [
        "# 平台兼容矩阵",
        "",
        f"- 生成时间：{now}",
        "",
        "## 核心结论",
        "",
        "- iOS Fusion 是主公开入口，具备最完整的 Rewrite / Script / MITM 能力。",
        "- Android 与 Windows 输出是规则投影，主要解决路由和域名层广告拦截，不能承诺 iOS 脚本效果。",
        "- App 独立模块用于排查和精细导入，不是新的多版本路线。",
        "",
        *table(rows),
        "",
        "## Android 分支",
        "",
        *(branch_rows or ["- 未发现 Android 分支清单。"]),
        "",
        "## 使用边界",
        "",
        "- 不要把 Android / Windows 输出当作完整 iOS 模块使用。",
        "- 不要为了兼容 Android / Windows 而把 iOS 高风险 MITM 或脚本逻辑硬转过去。",
        "- 当某 App 发生无网络、无法登录、无法播放、图片空白时，优先定位具体平台输出和源文件，再做单点调整。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Platform compatibility matrix written to {REPORT.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
