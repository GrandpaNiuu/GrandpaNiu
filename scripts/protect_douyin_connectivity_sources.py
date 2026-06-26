#!/usr/bin/env python3
"""Restore safe app-source fragments for Douyin connectivity.

Some upstream ad modules contain broad ByteDance/Douyin rejects or rewrites that
break Douyin comments, profile pages, homepage panels, and shared resource
loading. This guard is intentionally source-first: it runs after upstream sync
and before release generation, replacing only the known risky app fragments with
stable local versions.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SAFE_SOURCES = {
    "Rewrite/Sources/Apps/douyin.conf": """#!name=GrandpaNiu 抖音 Source
#!desc=Auto-synced app-scoped source fragment
# auto-sync: true
# source-url: https://raw.githubusercontent.com/fmz200/wool_scripts/main/QuantumultX/rewrite/split/partD/TikTok.snippet
# upstream-name: 抖音
# risk: medium
# disabled: upstream pstatp blocking rule removed because it breaks Douyin comments and profile networking
# validation-note: repository app-source validation requires at least one active output entry

[Rule]
DOMAIN,grandpaniu-douyin-disabled.invalid,REJECT
""",
    "Rewrite/Sources/Apps/hkdou-yin.conf": """#!name=GrandpaNiu 香港抖音 Source
#!desc=Auto-synced app-scoped source fragment
# auto-sync: true
# source-url: https://kelee.one/Tool/Loon/Lpx/HKDouYin_remove_ads.lpx
# upstream-name: 香港抖音去广告
# risk: medium
# disabled: removed HK Douyin rules and rewrites because they break Douyin comments/profile/homepage networking in the fusion module
# validation-note: repository app-source validation requires at least one active output entry

[Rule]
DOMAIN,grandpaniu-hkdouyin-disabled.invalid,REJECT
""",
    "Rewrite/Sources/Apps/dragon-read.conf": """#!name=GrandpaNiu 番茄小说 Source
#!desc=Auto-synced app-scoped source fragment
# auto-sync: true
# source-url: https://kelee.one/Tool/Loon/Lpx/DragonRead_remove_ads.lpx
# upstream-name: 番茄小说去广告
# risk: medium
# removed: ByteDance/Douyin shared core domains that break Douyin comments and profile networking

[Rule]
DOMAIN,zlink.ugsdk.cn,REJECT
DOMAIN,mon.toutiaocloud.net,REJECT
DOMAIN,log3-applog.fqnovel.com,REJECT
DOMAIN,log5-applog.fqnovel.com,REJECT
DOMAIN,mon11-misc-lq.fqnovel.com,REJECT
DOMAIN,mon11-misc.fqnovel.com,REJECT
DOMAIN,mon3-misc.fqnovel.com,REJECT
DOMAIN,rtlog3-applog.fqnovel.com,REJECT
DOMAIN,rtlog5-applog.fqnovel.com,REJECT
DOMAIN,mon.toutiaocloud.com,REJECT
""",
}


def write_if_changed(path: Path, content: str) -> bool:
    normalized = content.rstrip() + "\n"
    current = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
    if current == normalized:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(normalized, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    changed: list[str] = []
    for relative, content in SAFE_SOURCES.items():
        path = ROOT / relative
        if write_if_changed(path, content):
            changed.append(relative)
    if changed:
        print("Protected Douyin connectivity sources: " + ", ".join(changed))
    else:
        print("Douyin connectivity sources already protected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
