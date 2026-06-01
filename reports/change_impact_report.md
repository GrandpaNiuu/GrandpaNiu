# 变更影响报告

- 生成时间：2026-06-02 06:01:01 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `Android/adguard/GrandpaNiu-DNS.txt`
- `Android/adguard/README.md`
- `Android/mihomo/GrandpaNiu-Ads.yaml`
- `Android/mihomo/GrandpaNiu-Android-Full.yaml`
- `Android/mihomo/README-With-Proxy.md`
- `Android/mihomo/README.md`
- `Android/sing-box/GrandpaNiu-Ads.json`
- `Android/sing-box/README.md`
- `Android/v2rayng/GrandpaNiu-v2rayng-routing.json`
- `Android/v2rayng/README.md`
- `README.md`
- `android.html`
- `docs/android-user-guide.md`

## 新增文件

- `Android/adguard/GrandpaNiu-DNS.txt`
- `Android/adguard/README.md`
- `Android/mihomo/GrandpaNiu-Ads.yaml`
- `Android/mihomo/GrandpaNiu-Android-Full.yaml`
- `Android/mihomo/README-With-Proxy.md`
- `Android/mihomo/README.md`
- `Android/sing-box/GrandpaNiu-Ads.json`
- `Android/sing-box/README.md`
- `Android/v2rayng/GrandpaNiu-v2rayng-routing.json`
- `Android/v2rayng/README.md`
- `android.html`
- `docs/android-user-guide.md`

## 删除文件

- 无

## 修改文件

- `README.md`

## 影响的模块层

- Other
- README/docs

## 可能影响的 App

- YouTube
- 知乎
- Bilibili
- 小红书
- 淘宝
- 拼多多
- 美团
- 大众点评
- 滴滴
- 12306
- 高德地图
- 百度地图
- 网易云音乐
- 喜马拉雅
- 斗鱼

## 风险判断

- 是否涉及脚本：否
- 是否涉及 MITM：是
- 是否涉及 Body Rewrite：是
- 是否涉及远程规则源：否
- 是否需要测试 Spotify：按需
- 是否需要测试 YouTube：是
- 是否需要测试知乎：是
- 是否需要测试登录/支付/验证码：按需

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，可用 `backup/Ronghemokuai.stable.sgmodule` 人工恢复。
- 回滚后运行 `build_module.py --build --profile stable`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
