#!/usr/bin/env python3
"""Build v2rayN custom routing output from the Android v2rayNG route."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Android" / "v2rayng" / "GrandpaNiu-v2rayng-routing.json"
OUTPUT = ROOT / "Windows" / "v2rayN" / "GrandpaNiu-v2rayN-custom-routing.json"
README = ROOT / "Windows" / "v2rayN" / "README.md"


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_source_rules() -> list[dict[str, object]]:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    rules = data.get("routing", {}).get("rules", [])
    if not isinstance(rules, list) or not rules:
        raise SystemExit(f"missing routing.rules in {rel(SOURCE)}")
    return [rule for rule in rules if isinstance(rule, dict)]


def convert_ad_rule(rule: dict[str, object]) -> dict[str, object]:
    converted: dict[str, object] = {}
    for key in ("type", "domain", "ip", "outboundTag"):
        if key in rule:
            converted[key] = rule[key]
    if "type" not in converted:
        converted["type"] = "field"
    if "outboundTag" not in converted:
        converted["outboundTag"] = "block"
    converted["enabled"] = True
    converted["remarks"] = "GrandpaNiu 广告拦截"
    return converted


def direct_rule(key: str, value: str) -> dict[str, object]:
    return {
        "type": "field",
        key: [value],
        "outboundTag": "direct",
        "enabled": True,
        "remarks": "国内直连",
    }


def fallback_rule() -> dict[str, object]:
    return {
        "type": "field",
        "port": "0-65535",
        "outboundTag": "proxy",
        "enabled": True,
        "remarks": "其他全部代理",
    }


def build_rules() -> list[dict[str, object]]:
    rules = [convert_ad_rule(rule) for rule in read_source_rules()]
    rules.extend([
        direct_rule("domain", "geosite:private"),
        direct_rule("domain", "geosite:cn"),
        direct_rule("ip", "geoip:private"),
        direct_rule("ip", "geoip:cn"),
        fallback_rule(),
    ])
    return rules


def readme_text() -> str:
    url = "https://grandpaniuu.github.io/GrandpaNiu/Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json"
    raw = "https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json"
    return "\n".join([
        "# GrandpaNiu v2rayN 自定义路由",
        "",
        "本目录是 Windows v2rayN 专用路由输出，由 `Android/v2rayng/GrandpaNiu-v2rayng-routing.json` 自动转换生成。",
        "",
        "## 导入地址",
        "",
        f"- GitHub Pages: `{url}`",
        f"- Raw GitHub: `{raw}`",
        "",
        "## v2rayN 导入方法",
        "",
        "快捷路径：路由设置 → 自定义规则 → 从 URL 或剪贴板导入",
        "",
        "1. 打开 v2rayN。",
        "2. 进入路由设置。",
        "3. 打开自定义规则。",
        "4. 选择从 URL 导入，或先复制 JSON 内容后从剪贴板导入。",
        "5. 粘贴上面的导入地址。",
        "6. 保存路由设置，必要时重启当前配置。",
        "",
        "## 规则顺序",
        "",
        "1. GrandpaNiu 广告拦截规则使用 `outboundTag: block`。",
        "2. `geosite:private` 和 `geosite:cn` 走 `direct`。",
        "3. `geoip:private` 和 `geoip:cn` 走 `direct`。",
        "4. 最后的兜底规则会把其他全部流量交给 `proxy`。",
        "",
        "不要手动维护生成后的 JSON；需要刷新时运行 `scripts/build_windows_v2rayn.py`，或通过 `Rewrite/Generator/Builder.py --profile fusion --release` 统一生成。",
        "",
    ])


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(build_rules(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    README.write_text(readme_text(), encoding="utf-8", newline="\n")
    print(f"Built {rel(OUTPUT)} from {rel(SOURCE)}")


if __name__ == "__main__":
    main()
