#!/usr/bin/env python3
"""Build Android rule formats from Android sources and safe iOS rule fragments.

Android clients cannot consume Shadowrocket/Surge Script, MITM or Rewrite
sections. This builder only migrates rule types that Android rule engines can
represent safely, and only from explicit REJECT rules when reading iOS app
source fragments.
"""

from __future__ import annotations

import ipaddress
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MIHOMO_ROOT = ROOT / "Android" / "mihomo"
MIHOMO_DIR = MIHOMO_ROOT / "apps"
SING_BOX_ROOT = ROOT / "Android" / "sing-box"
SING_BOX_DIR = SING_BOX_ROOT / "apps"
ADGUARD_ROOT = ROOT / "Android" / "adguard"
ADGUARD_DIR = ADGUARD_ROOT / "apps"
V2RAYNG_ROOT = ROOT / "Android" / "v2rayng"
V2RAYNG_DIR = V2RAYNG_ROOT / "apps"
IOS_REJECT = ROOT / "Rules" / "reject.list"
IOS_APP_SOURCES = ROOT / "Rewrite" / "Sources" / "Apps"
AGGRESSIVE_ADS = ROOT / "Rules" / "aggressive-ads.list"
ANDROID_EXTRA_RULE_FILES = (
    ROOT / "Rules" / "app-clean.list",
    ROOT / "Rules" / "web-ads.list",
    ROOT / "Rules" / "qingrex-miniapp-app-ad.list",
    ROOT / "Rules" / "wechat-ad.list",
)
REPORT = ROOT / "reports" / "android_rules_report.md"
BRANCH_MANIFEST = ROOT / "Android" / "branches.json"
PUBLIC_BASE = "https://grandpaniuu.github.io/GrandpaNiu"

SUPPORTED_TYPES = {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD", "IP-CIDR", "IP-CIDR6"}
IOS_REJECT_NAME = "iOS-Compatible-Reject"
IOS_APP_COMPAT_NAME = "iOS-App-Compatible-Reject"
IOS_REWRITE_COMPAT_NAME = "iOS-Rewrite-Compatible-Reject"
ANDROID_AD_SDK_COMPAT_NAME = "Android-Ad-SDK-Compatible-Reject"
ANDROID_REPO_COMPAT_NAME = "Repo-Compatible-Reject"
MAIN_ADS_NAME = "GrandpaNiu-Ads"

SECTION_RE = re.compile(r"^\s*\[([^\]]+)\]\s*$")
REJECT_POLICIES = {
    "REJECT",
    "REJECT-DROP",
    "REJECT-IMG",
    "REJECT-TINYGIF",
    "REJECT-DICT",
    "REJECT-ARRAY",
    "REJECT-200",
}
REWRITE_REJECT_ACTIONS = (
    " - reject",
    " reject",
    "reject-200",
    "reject-array",
    "reject-dict",
    "reject-img",
    "reject-ttl",
    "reject-tinygif",
)
DOMAIN_LIKE_RE = re.compile(r"(?<![A-Za-z0-9_-])((?:[A-Za-z0-9-]+(?:\\\.|\.))+[A-Za-z]{2,})(?![A-Za-z0-9_-])")
URL_SCHEME_RE = re.compile(r"https?:(?:\\?/){2}")
AD_HOST_HINTS = (
    "ad",
    "ads",
    "adx",
    "advert",
    "advertise",
    "adproxy",
    "adservice",
    "banner",
    "cupid",
    "marketing",
    "market",
    "popup",
    "promotion",
    "promo",
    "rtb",
    "ssp",
    "splash",
    "pangolin",
    "gdt",
    "bugly",
    "crash",
    "analytics",
    "apm",
    "track",
    "trace",
    "stat",
    "stats",
    "monitor",
    "log",
)
KNOWN_ANDROID_AD_NETWORK_SUFFIXES = (
    "adsmogo.com",
    "adview.cn",
    "adview.com",
    "alimama.com",
    "allyes.com",
    "anythinktech.com",
    "app-measurement.com",
    "appsflyer.com",
    "bugly.qq.com",
    "cnzz.com",
    "doubleclick.net",
    "domob.cn",
    "gdt.qq.com",
    "googleadservices.com",
    "googlesyndication.com",
    "gtags.net",
    "iad.apple.com",
    "inmobi.cn",
    "irs01.com",
    "miaozhen.com",
    "mob.com",
    "mmstat.com",
    "moatads.com",
    "openx.net",
    "pangle.io",
    "pangolin-sdk-toutiao.com",
    "quantserve.com",
    "scorecardresearch.com",
    "sigmob.cn",
    "sigmob.com",
    "talkingdata.com",
    "tanx.com",
    "taboola.com",
    "umeng.com",
    "umengcloud.com",
    "umtrack.com",
    "unityads.unity3d.com",
    "vungle.com",
    "wrating.com",
    "youmi.net",
)

# Keep media, login, payment and broad CDN paths out of Android REJECT outputs.
PROTECTED_VALUE_TOKENS = (
    "alipay",
    "ysepay",
    "unionpay",
    "shouqianba",
    "95516",
    "cup.com.cn",
    "wechatpay",
    "tenpay",
    "bank",
    "icbc",
    "ccb",
    "abchina",
    "boc",
    "cmbchina",
    "cmbc",
    "cpic.com.cn",
    "bankcomm",
    "psbc",
    "login",
    "passport",
    "auth",
    "captcha",
    "verify",
    "vip.",
    "googlevideo",
    "youtubei",
    "video.qq.com",
    "biliapi.com",
    "biliapi.net",
    "grpc.biliapi.net",
    "api.bilibili.com",
    "app.bilibili.com",
    "api.live.bilibili.com",
    "api.iqiyi.com",
    "access.if.iqiyi.com",
    "bilivideo",
    "hdslb",
    "biliimg",
    "bilibili.com",
    "spotify.com",
    "scdn.co",
    "danmu",
    "acs.youku.com",
    "youku-acs",
    "amdc.m.youku.com",
    "alicdn.com",
    "tbcdn.cn",
    "jdimg.com",
    "360buyimg.com",
    "pddpic.com",
    "gtimg.cn",
    "qpic.cn",
    "httpdns",
    "hdns",
    "dnspod",
    "weixin.qq.com",
    "wx.qq.com",
    "wxs.qq.com",
    "weixinbridge",
    "servicewechat.com",
    "wechat",
    "tpns.qq.com",
    "lc.map.baidu.com",
    "api.zuihuimai.com",
    "ehaier.com",
)


def normalize_rule(rule_type: str, value: str) -> dict[str, str] | None:
    rule_type = rule_type.strip().upper()
    value = value.strip().strip("'\"")
    if rule_type not in SUPPORTED_TYPES or not value:
        return None

    if rule_type in {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD"}:
        value = value.lstrip(".").rstrip(".").lower()
        if any(char in value for char in (" ", "/", "\\", ":", ",")):
            return None
        if "*" in value or value.startswith("-"):
            return None
        if not re.search(r"[a-z0-9]", value):
            return None
    else:
        try:
            value = str(ipaddress.ip_network(value, strict=False))
        except ValueError:
            return None
    return {"type": rule_type, "value": value}


def protected_value(value: str) -> bool:
    low = value.lower()
    return any(token in low for token in PROTECTED_VALUE_TOKENS)


def dedupe_sort(rules: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    result: list[dict[str, str]] = []
    for rule in rules:
        key = (rule["type"], rule["value"].lower())
        if key in seen:
            continue
        seen.add(key)
        result.append(rule)
    result.sort(key=lambda item: (item["type"], item["value"].lower()))
    return result


def active(line: str) -> bool:
    stripped = line.strip()
    return bool(stripped) and not stripped.startswith("#")


def parse_mihomo_file(path: Path) -> list[dict[str, str]]:
    rules: list[dict[str, str]] = []
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not active(line) or line == "payload:":
            continue
        if line.startswith("-"):
            line = line[1:].strip()
        if "," not in line:
            continue
        rule_type, value = [part.strip() for part in line.split(",", 1)]
        rule = normalize_rule(rule_type, value)
        if rule and not protected_value(rule["value"]):
            rules.append(rule)
    return dedupe_sort(rules)


def parse_ios_reject_rules() -> list[dict[str, str]]:
    if not IOS_REJECT.exists():
        return []
    rules: list[dict[str, str]] = []
    for raw_line in IOS_REJECT.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not active(line) or "," not in line:
            continue
        parts = [part.strip() for part in line.split(",")]
        if len(parts) < 2:
            continue
        rule = normalize_rule(parts[0], parts[1])
        if rule and not protected_value(rule["value"]):
            rules.append(rule)
    return dedupe_sort(rules)


def rule_section_lines(path: Path) -> list[str]:
    current = ""
    lines: list[str] = []
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.rstrip()
        match = SECTION_RE.match(line)
        if match:
            current = match.group(1).strip()
            continue
        if current == "Rule":
            lines.append(line)
    return lines


def section_lines(path: Path, section_name: str) -> list[str]:
    current = ""
    lines: list[str] = []
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.rstrip()
        match = SECTION_RE.match(line)
        if match:
            current = match.group(1).strip()
            continue
        if current == section_name:
            lines.append(line)
    return lines


def reject_policy(parts: list[str]) -> bool:
    return any(part.strip().upper() in REJECT_POLICIES for part in parts[2:])


def parse_ios_app_rule_line(line: str) -> dict[str, str] | None:
    if not active(line) or "," not in line:
        return None
    parts = [part.strip() for part in line.split(",")]
    if len(parts) < 3 or not reject_policy(parts):
        return None
    rule = normalize_rule(parts[0], parts[1])
    if rule and not protected_value(rule["value"]):
        return rule
    return None


def parse_ios_app_compatible_rules() -> tuple[list[dict[str, str]], dict[str, int]]:
    rules: list[dict[str, str]] = []
    source_counts: dict[str, int] = {}
    if not IOS_APP_SOURCES.exists():
        return [], {}
    for path in sorted(IOS_APP_SOURCES.glob("*.conf"), key=lambda item: item.name.lower()):
        if path.name.startswith("_"):
            continue
        local_rules: list[dict[str, str]] = []
        for line in rule_section_lines(path):
            rule = parse_ios_app_rule_line(line)
            if rule:
                local_rules.append(rule)
        local_rules = dedupe_sort(local_rules)
        if local_rules:
            source_counts[path.stem] = len(local_rules)
            rules.extend(local_rules)
    return dedupe_sort(rules), source_counts


def ios_rewrite_source_files() -> list[Path]:
    paths: list[Path] = []
    if IOS_APP_SOURCES.exists():
        paths.extend(path for path in IOS_APP_SOURCES.glob("*.conf") if not path.name.startswith("_"))
    sources_root = ROOT / "Rewrite" / "Sources"
    if sources_root.exists():
        paths.extend(sources_root.glob("URL-Rewrite*.conf"))
    return sorted({path.resolve(): path for path in paths}.values(), key=lambda item: item.as_posix().lower())


def rewrite_reject_line(line: str) -> bool:
    if not active(line):
        return False
    lowered = line.lower()
    return any(action in lowered for action in REWRITE_REJECT_ACTIONS)


def normalize_domain_candidate(value: str) -> str | None:
    host = value.replace(r"\.", ".").lower().strip(".")
    if not host or "." not in host:
        return None
    labels = host.split(".")
    if len(labels) < 2:
        return None
    if any(not label or not re.fullmatch(r"[a-z0-9-]+", label) for label in labels):
        return None
    if labels[-1].isdigit():
        return None
    return host


def extract_domains_from_rewrite(line: str) -> list[str]:
    domains: list[str] = []
    seen: set[str] = set()
    for scheme_match in URL_SCHEME_RE.finditer(line):
        rest = line[scheme_match.end():]
        cut = len(rest)
        for marker in (r"\/", "/", r"\?", "?", " ", "$", '"', "'"):
            index = rest.find(marker)
            if index >= 0:
                cut = min(cut, index)
        host_part = rest[:cut]
        for match in DOMAIN_LIKE_RE.finditer(host_part):
            host = normalize_domain_candidate(match.group(1))
            if not host or host in seen:
                continue
            seen.add(host)
            domains.append(host)
    return domains


def ad_like_host(host: str) -> bool:
    labels = host.lower().split(".")
    compact = host.lower()
    for label in labels:
        if label in AD_HOST_HINTS:
            return True
        if label.startswith(("ad", "ads", "adx", "ssp", "rtb")):
            return True
    return any(token in compact for token in ("doubleclick", "googlesyndication", "googleadservices", "pangolin", "gdt"))


def parse_ios_rewrite_compatible_rules() -> tuple[list[dict[str, str]], dict[str, int]]:
    rules: list[dict[str, str]] = []
    source_counts: dict[str, int] = {}
    for path in ios_rewrite_source_files():
        local_rules: list[dict[str, str]] = []
        for line in section_lines(path, "URL Rewrite"):
            if not rewrite_reject_line(line):
                continue
            for host in extract_domains_from_rewrite(line):
                if not ad_like_host(host):
                    continue
                rule = normalize_rule("DOMAIN", host)
                if rule and not protected_value(rule["value"]):
                    local_rules.append(rule)
        local_rules = dedupe_sort(local_rules)
        if local_rules:
            source_counts[path.relative_to(ROOT).as_posix()] = len(local_rules)
            rules.extend(local_rules)
    return dedupe_sort(rules), source_counts


def parse_repo_rule_file(path: Path) -> list[dict[str, str]]:
    rules: list[dict[str, str]] = []
    if not path.exists():
        return rules
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not active(line) or "," not in line:
            continue
        parts = [part.strip() for part in line.split(",")]
        if len(parts) < 3 or not reject_policy(parts):
            continue
        rule = normalize_rule(parts[0], parts[1])
        if rule and not protected_value(rule["value"]):
            rules.append(rule)
    return dedupe_sort(rules)


def parse_repo_compatible_rules() -> tuple[list[dict[str, str]], dict[str, int]]:
    rules: list[dict[str, str]] = []
    source_counts: dict[str, int] = {}
    for path in ANDROID_EXTRA_RULE_FILES:
        local_rules = parse_repo_rule_file(path)
        if local_rules:
            source_counts[path.name] = len(local_rules)
            rules.extend(local_rules)
    return dedupe_sort(rules), source_counts


def known_android_ad_network(value: str) -> bool:
    low = value.lower()
    return any(low == suffix or low.endswith("." + suffix) for suffix in KNOWN_ANDROID_AD_NETWORK_SUFFIXES)


def parse_android_ad_sdk_rules() -> list[dict[str, str]]:
    rules: list[dict[str, str]] = []
    if not AGGRESSIVE_ADS.exists():
        return rules
    for raw_line in AGGRESSIVE_ADS.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not active(line) or "," not in line:
            continue
        parts = [part.strip() for part in line.split(",")]
        if len(parts) < 3 or not reject_policy(parts):
            continue
        if parts[0].strip().upper() not in {"DOMAIN", "DOMAIN-SUFFIX"}:
            continue
        rule = normalize_rule(parts[0], parts[1])
        if not rule or protected_value(rule["value"]):
            continue
        if ad_like_host(rule["value"]) or known_android_ad_network(rule["value"]):
            rules.append(rule)
    return dedupe_sort(rules)


def render_mihomo(rules: list[dict[str, str]], header: list[str] | None = None) -> str:
    lines = ["payload:"]
    if header:
        lines.extend(f"  # {line}" for line in header)
        lines.append("")
    lines.extend(f"  - {rule['type']},{rule['value']}" for rule in rules)
    return "\n".join(lines).rstrip() + "\n"


def render_sing_box(rules: list[dict[str, str]]) -> str:
    bucket: dict[str, list[str]] = {"domain": [], "domain_suffix": [], "domain_keyword": [], "ip_cidr": []}
    for rule in rules:
        if rule["type"] == "DOMAIN":
            bucket["domain"].append(rule["value"])
        elif rule["type"] == "DOMAIN-SUFFIX":
            bucket["domain_suffix"].append(rule["value"])
        elif rule["type"] == "DOMAIN-KEYWORD":
            bucket["domain_keyword"].append(rule["value"])
        elif rule["type"] in {"IP-CIDR", "IP-CIDR6"}:
            bucket["ip_cidr"].append(rule["value"])
    payload = {"version": 1, "rules": [{key: values for key, values in bucket.items() if values}]}
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def render_adguard(rules: list[dict[str, str]], header: list[str] | None = None) -> str:
    lines: list[str] = []
    if header:
        lines.extend(f"! {line}" for line in header)
        lines.append("")
    for rule in rules:
        value = rule["value"]
        if rule["type"] in {"DOMAIN", "DOMAIN-SUFFIX"}:
            lines.append(f"||{value}^")
        elif rule["type"] == "DOMAIN-KEYWORD":
            lines.append(f"/{value}/")
    deduped: list[str] = []
    seen: set[str] = set()
    for line in lines:
        key = line.lower()
        if key in seen:
            continue
        seen.add(key)
        deduped.append(line)
    return "\n".join(deduped).rstrip() + "\n"


def render_v2rayng(rules: list[dict[str, str]]) -> str:
    domains: list[str] = []
    ips: list[str] = []
    for rule in rules:
        value = rule["value"]
        if rule["type"] == "DOMAIN":
            domains.append(f"full:{value}")
        elif rule["type"] == "DOMAIN-SUFFIX":
            domains.append(f"domain:{value}")
        elif rule["type"] == "DOMAIN-KEYWORD":
            domains.append(f"keyword:{value}")
        elif rule["type"] in {"IP-CIDR", "IP-CIDR6"}:
            ips.append(value)
    route: dict[str, object] = {"type": "field", "outboundTag": "block"}
    if domains:
        route["domain"] = domains
    if ips:
        route["ip"] = ips
    payload = {"routing": {"rules": [route]}}
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def write_if_changed(path: Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8", errors="replace") == content:
        return False
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def write_android_formats(app_name: str, rules: list[dict[str, str]]) -> None:
    header = [f"Generated Android rules for {app_name}.", "Source: Android app layer and safe iOS-compatible REJECT rules."]
    write_if_changed(MIHOMO_DIR / f"{app_name}.yaml", render_mihomo(rules, header))
    write_if_changed(SING_BOX_DIR / f"{app_name}.json", render_sing_box(rules))
    write_if_changed(ADGUARD_DIR / f"{app_name}.txt", render_adguard(rules, header))
    write_if_changed(V2RAYNG_DIR / f"{app_name}-routing.json", render_v2rayng(rules))


def write_main_outputs(rules: list[dict[str, str]], app_count: int) -> None:
    header = [
        "GrandpaNiu Android main rules.",
        "Generated from Android/mihomo/apps plus safe iOS/Fusion compatible REJECT rules.",
        f"App source files included: {app_count}.",
        "Script, MITM, Rewrite and media-chain rules are not migrated to Android.",
    ]
    write_if_changed(MIHOMO_ROOT / f"{MAIN_ADS_NAME}.yaml", render_mihomo(rules, header))
    write_if_changed(SING_BOX_ROOT / f"{MAIN_ADS_NAME}.json", render_sing_box(rules))
    write_if_changed(ADGUARD_ROOT / "GrandpaNiu-DNS.txt", render_adguard(rules, header))
    write_if_changed(V2RAYNG_ROOT / "GrandpaNiu-v2rayng-routing.json", render_v2rayng(rules))


def active_adguard_rule_count(rules: list[dict[str, str]]) -> int:
    rendered = render_adguard(rules)
    return len([line for line in rendered.splitlines() if line.strip() and not line.startswith("!")])


def write_branch_manifest(rules: list[dict[str, str]], app_count: int, generated: str) -> None:
    main_count = len(rules)
    adguard_count = active_adguard_rule_count(rules)
    manifest = {
        "generated": f"{generated} Asia/Shanghai",
        "source_of_truth": "Android/mihomo/apps/*.yaml + safe iOS/Fusion/repo compatible REJECT rules",
        "sync_policy": (
            "Mihomo, sing-box and v2rayNG are generated from the same canonical Android rule set. "
            "AdGuard is generated from the same source as the DNS-compatible projection."
        ),
        "app_source_files": app_count,
        "canonical_rule_count": main_count,
        "branches": [
            {
                "id": "mihomo",
                "name": "Mihomo / Clash Meta / FlClash",
                "target": "Android/mihomo/GrandpaNiu-Ads.yaml",
                "release_target": "Release/Android/mihomo/GrandpaNiu-Ads.yaml",
                "public_url": f"{PUBLIC_BASE}/Android/mihomo/GrandpaNiu-Ads.yaml",
                "sync_with": "mihomo",
                "projection": "full",
                "rule_count": main_count,
            },
            {
                "id": "sing-box",
                "name": "sing-box",
                "target": "Android/sing-box/GrandpaNiu-Ads.json",
                "release_target": "Release/Android/sing-box/GrandpaNiu-Ads.json",
                "public_url": f"{PUBLIC_BASE}/Android/sing-box/GrandpaNiu-Ads.json",
                "sync_with": "mihomo",
                "projection": "full",
                "rule_count": main_count,
            },
            {
                "id": "adguard",
                "name": "AdGuard DNS / AdGuard Home",
                "target": "Android/adguard/GrandpaNiu-DNS.txt",
                "release_target": "Release/Android/adguard/GrandpaNiu-DNS.txt",
                "public_url": f"{PUBLIC_BASE}/Android/adguard/GrandpaNiu-DNS.txt",
                "sync_with": "mihomo",
                "projection": "dns-domain",
                "rule_count": adguard_count,
                "source_rule_count": main_count,
            },
            {
                "id": "v2rayng",
                "name": "v2rayNG / V2Ray / Xray routing",
                "target": "Android/v2rayng/GrandpaNiu-v2rayng-routing.json",
                "release_target": "Release/Android/v2rayng/GrandpaNiu-v2rayng-routing.json",
                "public_url": f"{PUBLIC_BASE}/Android/v2rayng/GrandpaNiu-v2rayng-routing.json",
                "sync_with": "mihomo",
                "projection": "full",
                "rule_count": main_count,
            },
        ],
    }
    write_if_changed(BRANCH_MANIFEST, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")


def generate_report(
    stats: list[dict[str, str | int]],
    ios_app_counts: dict[str, int],
    ios_rewrite_counts: dict[str, int],
    ad_sdk_count: int,
    repo_counts: dict[str, int],
    main_count: int,
) -> None:
    now = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# Android rules build report",
        "",
        f"- generated: {now} Asia/Shanghai",
        f"- app rule files: {len(stats)}",
        f"- main Android rules: {main_count}",
        f"- source: Android/mihomo/apps/*.yaml",
        f"- iOS common source: Rules/reject.list -> {IOS_REJECT_NAME}",
        f"- iOS app source: Rewrite/Sources/Apps/*.conf [Rule] REJECT -> {IOS_APP_COMPAT_NAME}",
        f"- iOS rewrite source: Rewrite/Sources URL Rewrite reject hostnames -> {IOS_REWRITE_COMPAT_NAME}",
        f"- Android ad SDK source: Rules/aggressive-ads.list safe ad-network subset -> {ANDROID_AD_SDK_COMPAT_NAME} ({ad_sdk_count})",
        f"- repo rule source: Rules/app-clean.list + Rules/web-ads.list + Rules/qingrex-miniapp-app-ad.list + Rules/wechat-ad.list -> {ANDROID_REPO_COMPAT_NAME}",
        "- exported formats: Mihomo / sing-box / AdGuard / v2rayNG",
        "- sync branches: sing-box, AdGuard and v2rayNG are generated from the Mihomo source layer during the same build.",
        "- safety: Script, MITM, Rewrite, DIRECT/PROXY and protected media/payment/login rules are not migrated.",
        "",
        "| App | Rules | Outputs |",
        "|---|---:|---|",
    ]
    for item in sorted(stats, key=lambda row: str(row["name"]).lower()):
        lines.append(f"| {item['name']} | {item['count']} | yes |")
    lines.extend([
        "",
        "## iOS app source coverage",
        "",
        "| Source app | Migrated reject rules |",
        "|---|---:|",
    ])
    if ios_app_counts:
        for slug, count in sorted(ios_app_counts.items()):
            lines.append(f"| {slug} | {count} |")
    else:
        lines.append("| none | 0 |")
    lines.extend([
        "",
        "## iOS URL Rewrite source coverage",
        "",
        "| Source file | Migrated reject host rules |",
        "|---|---:|",
    ])
    if ios_rewrite_counts:
        for source, count in sorted(ios_rewrite_counts.items()):
            lines.append(f"| {source} | {count} |")
    else:
        lines.append("| none | 0 |")
    lines.extend([
        "",
        "## Repository rule source coverage",
        "",
        "| Source file | Migrated reject rules |",
        "|---|---:|",
    ])
    if repo_counts:
        for source, count in sorted(repo_counts.items()):
            lines.append(f"| {source} | {count} |")
    else:
        lines.append("| none | 0 |")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    if not MIHOMO_DIR.exists():
        raise SystemExit("missing Android/mihomo/apps source directory")

    ios_common = parse_ios_reject_rules()
    if ios_common:
        write_if_changed(
            MIHOMO_DIR / f"{IOS_REJECT_NAME}.yaml",
            render_mihomo(ios_common, ["Generated from Rules/reject.list safe Android-compatible rules."]),
        )

    ios_app_compatible, ios_app_counts = parse_ios_app_compatible_rules()
    if ios_app_compatible:
        write_if_changed(
            MIHOMO_DIR / f"{IOS_APP_COMPAT_NAME}.yaml",
            render_mihomo(
                ios_app_compatible,
                ["Generated from Rewrite/Sources/Apps/*.conf [Rule] REJECT entries.", "Protected media, login and payment domains are excluded."],
            ),
        )

    ios_rewrite_compatible, ios_rewrite_counts = parse_ios_rewrite_compatible_rules()
    if ios_rewrite_compatible:
        write_if_changed(
            MIHOMO_DIR / f"{IOS_REWRITE_COMPAT_NAME}.yaml",
            render_mihomo(
                ios_rewrite_compatible,
                [
                    "Generated from safe iOS URL Rewrite reject hostnames.",
                    "Only ad-like hostnames are migrated; path-specific core APIs are excluded.",
                ],
            ),
        )

    ad_sdk_compatible = parse_android_ad_sdk_rules()
    if ad_sdk_compatible:
        write_if_changed(
            MIHOMO_DIR / f"{ANDROID_AD_SDK_COMPAT_NAME}.yaml",
            render_mihomo(
                ad_sdk_compatible,
                [
                    "Generated from the safe ad-network subset of Rules/aggressive-ads.list.",
                    "Broad keywords, URL regex, media, payment, login and CDN-protected values are excluded.",
                ],
            ),
        )

    repo_compatible, repo_counts = parse_repo_compatible_rules()
    if repo_compatible:
        write_if_changed(
            MIHOMO_DIR / f"{ANDROID_REPO_COMPAT_NAME}.yaml",
            render_mihomo(
                repo_compatible,
                [
                    "Generated from safe repository rule sources for Android.",
                    "Aggressive, DIRECT, Script, MITM, Rewrite and protected media/payment/login rules are excluded.",
                ],
            ),
        )

    stats: list[dict[str, str | int]] = []
    all_rules: list[dict[str, str]] = []
    for source in sorted(MIHOMO_DIR.glob("*.yaml"), key=lambda path: path.name.lower()):
        app_name = source.stem
        rules = parse_mihomo_file(source)
        if not rules:
            continue
        write_android_formats(app_name, rules)
        all_rules.extend(rules)
        stats.append({"name": app_name, "count": len(rules)})

    main_rules = dedupe_sort(all_rules)
    if not main_rules:
        raise SystemExit("no Android rules generated")
    write_main_outputs(main_rules, len(stats))
    generated = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S")
    write_branch_manifest(main_rules, len(stats), generated)
    generate_report(stats, ios_app_counts, ios_rewrite_counts, len(ad_sdk_compatible), repo_counts, len(main_rules))
    print(f"Android rule formats generated: {len(stats)} app file(s), {len(main_rules)} main rule(s).")


if __name__ == "__main__":
    main()
