# Candidate App Modules

本目录用于保存第一批待审查 App 模块候选源。这里的文件**不进入当前公开 Fusion 模块**，也不会生成 `Release/Modules/`，除非后续人工审查后移动到 `Rewrite/Sources/Apps/`。

## 第一批候选

```text
tieba.conf             # 百度贴吧
baidupan.conf          # 百度网盘
baidu-wenku.conf       # 百度文库
ximalaya.conf          # 喜马拉雅
qqmusic.conf           # QQ 音乐
keep.conf              # Keep
reddit.conf            # Reddit
cainiao.conf           # 菜鸟裹裹
goofish.conf           # 闲鱼
caiyun-weather.conf    # 彩云天气
moji-weather.conf      # 墨迹天气
didi.conf              # 滴滴出行
china-unicom.conf      # 中国联通
ithome.conf            # IT之家
terabox.conf           # TeraBox
xiaoyuzhou.conf        # 小宇宙 FM
qishui-music.conf      # 汽水音乐
railway12306.conf      # 12306
weread.conf            # 微信读书
netease-mail.conf      # 网易邮箱大师
```

## 晋级规则

候选模块进入正式 `Rewrite/Sources/Apps/` 前必须完成：

```text
1. 上游来源核对
2. Surge 语法转换
3. MITM hostname 审计
4. 登录 / 支付 / 播放 / 图片 / 评论 / 搜索等关键链路测试
5. 误杀回归测试
6. 回滚路径确认
```

## 晋级路径

```text
Rewrite/Sources/Candidates/Apps/<name>.conf
        ↓
Rewrite/Sources/Apps/<name>.conf
        ↓
Release/Modules/<name>.sgmodule
```

不要直接修改 `Release/`。
