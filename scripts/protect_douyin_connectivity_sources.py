#!/usr/bin/env python3
"""Restore safe source fragments for Douyin connectivity.

Some upstream ad modules contain broad ByteDance/Douyin/ZijieAPI/SNSSDK rejects
or rewrites that break Douyin comments, search, profile pages, homepage panels,
and shared resource loading. This guard is intentionally source-first: it runs
after upstream sync and before release generation, replacing the known risky
fragments with stable local versions.
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
    "Rewrite/Sources/Misc/android-compatible-ads.conf": """#!name=GrandpaNiu Android Compatible Ads
#!desc=Low-risk Android branch ad rules merged back into iOS Fusion

[Rule]
# Generated from Android main branch gap analysis.
# Only ad/tracking-like REJECT rules are included.
# Login, payment, banking, captcha, video playback, image/CDN and ambiguous non-ad domains are excluded.
# ByteDance/Douyin/ZijieAPI/SNSSDK shared endpoints are excluded because broad rejects break Douyin comments, search and profile pages.
DOMAIN,ad.e.waimai.sankuai.com,REJECT,pre-matching
DOMAIN,ad.jiemian.com,REJECT,pre-matching
DOMAIN,ad.partner.gifshow.com,REJECT,pre-matching
DOMAIN,ad.qtfm.cn,REJECT,pre-matching
DOMAIN,ad.snailsleep.net,REJECT,pre-matching
DOMAIN,ad.v3mh.com,REJECT,pre-matching
DOMAIN,adash.m.taobao.com,REJECT,pre-matching
DOMAIN,adashbc.m.taobao.com,REJECT,pre-matching
DOMAIN,adclick.tencentmusic.com,REJECT,pre-matching
DOMAIN,adlaunch.qtfm.cn,REJECT,pre-matching
DOMAIN,ads-partner.cdn.bcebos.com,REJECT,pre-matching
DOMAIN,ads.youtube.com,REJECT,pre-matching
DOMAIN,adservice.google.com,REJECT,pre-matching
DOMAIN,adx.36kr.com,REJECT,pre-matching
DOMAIN,api-ad.kajicam.com,REJECT,pre-matching
DOMAIN,api.e.kuaishou.com,REJECT,pre-matching
DOMAIN,applog.uc.cn,REJECT,pre-matching
DOMAIN,c2.gdt.qq.com,REJECT,pre-matching
DOMAIN,e.kuaishou.com,REJECT,pre-matching
DOMAIN,ios.bugly.qq.com,REJECT,pre-matching
DOMAIN,jp.ad.gameley.com,REJECT,pre-matching
DOMAIN,mi.gdt.qq.com,REJECT,pre-matching
DOMAIN,monitor.music.qq.com,REJECT,pre-matching
DOMAIN,open.e.kuaishou.com,REJECT,pre-matching
DOMAIN,pagead-googlehosted.l.google.com,REJECT,pre-matching
DOMAIN,partnerad.l.doubleclick.net,REJECT,pre-matching
DOMAIN,popup-api.b612kaji.com,REJECT,pre-matching
DOMAIN,report.meituan,REJECT,pre-matching
DOMAIN,retcode.taobao.com,REJECT,pre-matching
DOMAIN,rmonitor.qq.com,REJECT,pre-matching
DOMAIN,static.doubleclick.net,REJECT,pre-matching
DOMAIN,t.gdt.qq.com,REJECT,pre-matching
DOMAIN,tmeadquic.y.qq.com,REJECT,pre-matching
DOMAIN,tns.simba.taobao.com,REJECT,pre-matching
DOMAIN,tpstelemetry.tencent.com,REJECT,pre-matching
DOMAIN,umengacs.m.taobao.com,REJECT,pre-matching
DOMAIN,v.gdt.qq.com,REJECT,pre-matching
DOMAIN,v2.gdt.qq.com,REJECT,pre-matching
DOMAIN,win.gdt.qq.com,REJECT,pre-matching
DOMAIN,wmlog.meituan.com,REJECT,pre-matching
DOMAIN,www.googleadservices.com,REJECT,pre-matching
DOMAIN,zjres-ad.kajicam.com,REJECT,pre-matching
DOMAIN-KEYWORD,bili-ad,REJECT,pre-matching
DOMAIN-KEYWORD,doubleclick,REJECT,pre-matching
DOMAIN-KEYWORD,googleads,REJECT,pre-matching
DOMAIN-KEYWORD,googlesyndication,REJECT,pre-matching
DOMAIN-KEYWORD,jd-ad,REJECT,pre-matching
DOMAIN-KEYWORD,kuaishou-ad,REJECT,pre-matching
DOMAIN-KEYWORD,kwai-ad,REJECT,pre-matching
DOMAIN-KEYWORD,pdd-ad,REJECT,pre-matching
DOMAIN-KEYWORD,weibo-ad,REJECT,pre-matching
DOMAIN-KEYWORD,xhs-ad,REJECT,pre-matching
DOMAIN-KEYWORD,xiaohongshu-ad,REJECT,pre-matching
DOMAIN-KEYWORD,zhihu-ad,REJECT,pre-matching
DOMAIN-SUFFIX,adkwai.com,REJECT,pre-matching
DOMAIN-SUFFIX,admobile.top,REJECT,pre-matching
DOMAIN-SUFFIX,ads.union.jd.com,REJECT,pre-matching
DOMAIN-SUFFIX,adukwai.com,REJECT,pre-matching
DOMAIN-SUFFIX,zhihu-web-analytics.zhihu.com,REJECT,pre-matching
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
