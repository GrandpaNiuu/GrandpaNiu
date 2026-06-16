#!/usr/bin/env python3
"""Migrate low-risk cleaners to app-cleaner active.

This script removes only old entries now covered by Scripts/app-cleaner.js.

Batch 1: QQ News, VGTime.
Batch 2: SQKB, 163News, XiaoHeiHe, Manner, Chaoge.
Batch 3: SMZDM, Taobao, JuneYaoAir, DDXQ, ZSGJ.
Batch 4: KKMH, Goofish, XMly, Didi.
Batch 5: generic low-risk JSON ad-field cleaner endpoints.
Batch 6: Douyu, SPTCC, Youdao Dict, Maimai.

It applies the same cleanup to Scripts/app-clean.conf and Rewrite/Sources/Script.conf
so source_script_compat does not reintroduce old entries during builds.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    ROOT / "Scripts" / "app-clean.conf",
    ROOT / "Rewrite" / "Sources" / "Script.conf",
]
REPORT = ROOT / "reports" / "script_dedupe_report.md"
ROLLBACK = ROOT / "reports" / "script_consolidation_rollback_report.md"
ACTIVE_ENTRY = ROOT / "Scripts" / "app-cleaner-active.conf"
REMOVED_NAMES = {
    "cmp_block_097_ad": "QQ News app2smile entry",
    "cmp_allad_046_txnews": "QQ News zirawell entry",
    "cmp_block_098_vgtime": "VGTime app2smile entry",
    "legacy_safe_qqnews": "Legacy QQ News duplicate entry",
    "cmp_allad_011_sqkb": "SQKB JSON ad cleaner",
    "cmp_allad_015_163news": "163News JSON ad cleaner",
    "cmp_allad_022_xiaoheihe": "XiaoHeiHe JSON ad cleaner",
    "cmp_allad_043_manner": "Manner JSON ad cleaner",
    "cmp_allad_044_chaoge": "Chaoge JSON ad cleaner",
    "cmp_allad_013_smzdm": "SMZDM detail module cleaner",
    "cmp_allad_014_taobao": "Taobao poplayer cleaner",
    "cmp_allad_016_juneyaoair": "JuneYaoAir popup cleaner",
    "cmp_allad_020_ddxq": "DDXQ user page cleaner",
    "cmp_allad_021_mygolbs": "ZSGJ text replacement cleaner",
    "cmp_allad_002_kkmh": "KKMH JSON cleaner",
    "cmp_allad_008_goofish": "Goofish JSON cleaner",
    "cmp_allad_009_xmly": "XMly JSON cleaner",
    "cmp_allad_010_didi": "Didi JSON cleaner",
    "cmp_allad_018_coolapk": "Generic JSON ad-field cleaner",
    "cmp_allad_023_dianping": "Generic JSON ad-field cleaner",
    "cmp_allad_029_amap": "Generic JSON ad-field cleaner",
    "cmp_allad_030_babytree": "Generic JSON ad-field cleaner",
    "cmp_allad_032_mafengwo": "Generic JSON ad-field cleaner",
    "cmp_allad_033_gaoding": "Generic JSON ad-field cleaner",
    "cmp_allad_034_pdd": "Generic JSON ad-field cleaner",
    "cmp_allad_035_qidian": "Generic JSON ad-field cleaner",
    "cmp_allad_036_kuaishou": "Generic JSON ad-field cleaner",
    "cmp_allad_037_freshippo": "Generic JSON ad-field cleaner",
    "cmp_allad_038_xunlei": "Generic JSON ad-field cleaner",
    "cmp_allad_039_cainiao": "Generic JSON ad-field cleaner",
    "cmp_allad_040_zhuanzhuan": "Generic JSON ad-field cleaner",
    "cmp_allad_041_baidumap": "Generic JSON ad-field cleaner",
    "cmp_allad_042_ehaier": "Generic JSON ad-field cleaner",
    "cmp_allad_045_xiaoyuzhoufm": "Generic JSON ad-field cleaner",
    "cmp_allad_047_peiyinxiu": "Generic JSON ad-field cleaner",
    "cmp_allad_048_jd": "Generic JSON ad-field cleaner",
    "cmp_allad_049_meituan": "Generic JSON ad-field cleaner",
    "cmp_allad_050_reddit": "Generic JSON ad-field cleaner",
    "cmp_allad_051_boohee": "Generic JSON ad-field cleaner",
    "cmp_allad_052_360cam": "Generic JSON ad-field cleaner",
    "cmp_allad_053_fliggy": "Generic JSON ad-field cleaner",
    "cmp_allad_054_1314zhilv": "Generic JSON ad-field cleaner",
    "cmp_allad_055_adunion": "Generic JSON ad-field cleaner",
    "cmp_allad_056_ppx": "Generic JSON ad-field cleaner",
    "cmp_allad_059_quda": "Generic JSON ad-field cleaner",
    "cmp_allad_060_maimai": "Generic JSON ad-field cleaner",
    "cmp_allad_061_foliday": "Generic JSON ad-field cleaner",
    "cmp_allad_062_tuhu": "Generic JSON ad-field cleaner",
    "cmp_allad_063_163youdao": "Generic JSON ad-field cleaner",
    "cmp_allad_064_ys7": "Generic JSON ad-field cleaner",
    "cmp_allad_065_flyert": "Generic JSON ad-field cleaner",
    "cmp_allad_067_guiderank": "Generic JSON ad-field cleaner",
    "cmp_allad_068_mishop": "Generic JSON ad-field cleaner",
    "cmp_allad_069_qbb": "Generic JSON ad-field cleaner",
    "cmp_allad_071_51cto": "Generic JSON ad-field cleaner",
    "cmp_allad_073_meituanwm": "Generic JSON ad-field cleaner",
    "cmp_allad_076_ithome": "Generic JSON ad-field cleaner",
    "cmp_allad_077_eleme": "Generic JSON ad-field cleaner",
    "cmp_allad_078_duitang": "Generic JSON ad-field cleaner",
    "cmp_allad_079_51job": "Generic JSON ad-field cleaner",
    "cmp_allad_081_usmile": "Generic JSON ad-field cleaner",
    "cmp_block_086_ad": "Generic JSON ad-field cleaner",
    "cmp_block_089_ad": "Generic JSON ad-field cleaner",
    "cmp_block_091_app": "Generic JSON ad-field cleaner",
    "cmp_block_092_ad": "Generic JSON ad-field cleaner",
    "cmp_block_093_ad": "Generic JSON ad-field cleaner",
    "cmp_block_094_ad": "Generic JSON ad-field cleaner",
    "cmp_block_096_ad": "Generic JSON ad-field cleaner",
    "cmp_allad_057_douyu": "Douyu JSON cleaner",
    "cmp_allad_058_sptcc": "SPTCC JSON cleaner",
    "cmp_block_099_ad": "Youdao Dict JSON cleaner",
    "cmp_block_090_ad": "Maimai JSON cleaner",
}
PROTECTED_NAMES = {
    "spotify-upstream",
    "youtube.response",
    "zhihu-enhance",
    "cmp_block_084_json",
    "cmp_block_085_proto",
    "cmp_allad_001_weibo",
    "cmp_allad_003_keep",
    "cmp_allad_004_soul",
    "cmp_allad_005_mgtv",
    "cmp_allad_006_tflj",
    "cmp_allad_007_cotti",
    "cmp_allad_012_dushu365",
    "cmp_allad_017_xiaohongshu",
    "cmp_allad_019_zhihu",
    "cmp_allad_024_12306",
    "cmp_allad_025_rrtv",
    "cmp_allad_026_163music",
    "cmp_allad_027_airchina",
    "cmp_allad_028_xmgtv",
    "cmp_allad_031_baidutieba",
    "cmp_allad_066_wjx",
    "cmp_allad_070_sogou",
    "cmp_allad_072_baidutieba",
    "cmp_allad_074_adunion",
    "cmp_allad_075_umetrip",
    "cmp_allad_080_yunda",
    "cmp_block_082_12306",
    "cmp_block_083_ad",
    "cmp_block_087_ad",
    "cmp_block_088_ad",
    "cmp_block_095_rrtv_json",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def script_name(line: str) -> str:
    if "=" not in line:
        return ""
    return line.split("=", 1)[0].strip()


def clean_file(path: Path) -> list[str]:
    original = read(path)
    kept: list[str] = []
    removed: list[str] = []
    for line in original.splitlines():
        name = script_name(line)
        if name in PROTECTED_NAMES:
            kept.append(line)
            continue
        if name in REMOVED_NAMES:
            removed.append(line)
            continue
        kept.append(line)
    if removed:
        write(path, "\n".join(kept).rstrip() + "\n")
    return removed


def main() -> None:
    active = read(ACTIVE_ENTRY)
    if "app-cleaner-active-json-clean" not in active:
        raise SystemExit("Active app-cleaner entry missing: Scripts/app-cleaner-active.conf")
    if "app-cleaner.js" not in active:
        raise SystemExit("Active app-cleaner entry does not point to Scripts/app-cleaner.js")

    removed_by_file: dict[str, list[str]] = {}
    for target in TARGETS:
        removed_by_file[target.relative_to(ROOT).as_posix()] = clean_file(target)

    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    total_removed = sum(len(items) for items in removed_by_file.values())
    app_clean_removed = len(removed_by_file.get("Scripts/app-clean.conf", []))
    planned = [name for name in REMOVED_NAMES if not name.startswith("legacy_")]

    report = [
        "# 脚本去重与 app-cleaner active 迁移报告",
        "",
        f"生成时间：{now}",
        "",
        "## 本次迁移",
        "",
        "- 迁移范围：Batch 1-6 低风险 JSON / 字段清理融合",
        "- 新承接入口：`Scripts/app-cleaner-active.conf` / `app-cleaner-active-json-clean`",
        "- 新承接脚本：`Scripts/app-cleaner.js`",
        f"- 计划替换旧入口数量：{len(planned)}",
        f"- Scripts/app-clean.conf 本次移除旧入口数量：{app_clean_removed}",
        f"- 所有源文件合计本次移除旧入口数量：{total_removed}",
        "- 新增 active 入口数量：1",
        "- 说明：这是大批量融合，但保留高风险和复杂脚本独立运行。",
        "",
        "## 移除的旧入口",
        "",
    ]
    for file_name, removed in removed_by_file.items():
        report += [f"### `{file_name}`", ""]
        if removed:
            for line in removed:
                name = script_name(line)
                report += [f"#### `{name}`", "", f"- 说明：{REMOVED_NAMES.get(name, '旧入口')}", "", "```text", line, "```", ""]
        else:
            report += ["- 无，目标旧入口已不存在。", ""]
    report += [
        "## 不变范围",
        "",
        "- 不动 Spotify。",
        "- 不动 YouTube。",
        "- 不动知乎增强与知乎 R-Store 条目。",
        "- 不动 Tieba JSON / proto。",
        "- 不动微博、Keep、Soul、Cotti、RRTV、网易云音乐、12306、航旅纵横、搜狗输入法、韵达等复杂或高风险条目。",
        "- 不动登录、支付、验证码、银行相关条目。",
        "- 不合并复杂加密、持久化配置、会员权益、binary-body 脚本。",
        "",
    ]
    write(REPORT, "\n".join(report).rstrip() + "\n")

    rollback = [
        "# 脚本瘦身回滚报告",
        "",
        f"生成时间：{now}",
        "",
        "## 回滚条件",
        "",
        "如果本批 App 在 Stable 中出现页面异常、广告残留加重、JSON 解析异常、加载失败，应回滚本次迁移。",
        "",
        "## 回滚步骤",
        "",
        "1. 从 `Rewrite/Profiles/stable.conf` 移除 `app_cleaner_active = Scripts/app-cleaner-active.conf`。",
        "2. 从 `Rewrite/Profiles/stable-plus.conf` 移除 `app_cleaner_active = Scripts/app-cleaner-active.conf`。",
        "3. 将下方旧入口恢复到对应文件。",
        "4. 重新运行 build / finalize / build_release_variants / validate。",
        "",
        "## 需要恢复的旧入口",
        "",
    ]
    for file_name, removed in removed_by_file.items():
        rollback += [f"### `{file_name}`", ""]
        if removed:
            for line in removed:
                rollback += ["```text", line, "```", ""]
        else:
            rollback += ["- 当前脚本运行时没有新移除旧入口；如需回滚，请从 Git 历史恢复旧入口。", ""]
    rollback += [
        "## 验证命令",
        "",
        "```bash",
        "python3 scripts/build_module.py --build --profile fusion",
        "python3 scripts/factory_finalize.py --sync-root",
        "python3 scripts/build_release_variants.py",
        "python3 scripts/validate_repository.py",
        "python3 scripts/validate_profiles.py",
        "python3 scripts/repository_health_check.py",
        "```",
        "",
    ]
    write(ROLLBACK, "\n".join(rollback).rstrip() + "\n")
    print(f"Low-risk app-cleaner migration complete. planned={len(planned)}, removed={total_removed}, app_clean_removed={app_clean_removed}")


if __name__ == "__main__":
    main()
