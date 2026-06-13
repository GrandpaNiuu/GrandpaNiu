# GrandpaNiu v2rayN 自定义路由

本目录是 Windows v2rayN 专用路由输出，由 `Android/v2rayng/GrandpaNiu-v2rayng-routing.json` 自动转换生成。

## 导入地址

- GitHub Pages: `https://grandpaniuu.github.io/GrandpaNiu/Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json`
- Raw GitHub: `https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json`

## v2rayN 导入方法

快捷路径：路由设置 → 自定义规则 → 从 URL 或剪贴板导入

1. 打开 v2rayN。
2. 进入路由设置。
3. 打开自定义规则。
4. 选择从 URL 导入，或先复制 JSON 内容后从剪贴板导入。
5. 粘贴上面的导入地址。
6. 保存路由设置，必要时重启当前配置。

## 规则顺序

1. GrandpaNiu 广告拦截规则使用 `outboundTag: block`。
2. `geosite:private` 和 `geosite:cn` 走 `direct`。
3. `geoip:private` 和 `geoip:cn` 走 `direct`。
4. 最后的兜底规则会把其他全部流量交给 `proxy`。

不要手动维护生成后的 JSON；需要刷新时运行 `scripts/build_windows_v2rayn.py`，或通过 `Rewrite/Generator/Builder.py --profile fusion --release` 统一生成。
