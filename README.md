<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Shadowrocket 模块安装</title>

<style>
    body{
        margin:40px 20px;
        background:#111;
        color:#fff;
        font-family:-apple-system,BlinkMacSystemFont,sans-serif;
    }

    .card{
        max-width:520px;
        margin:auto;
        background:#1c1c1e;
        border:1px solid #2c2c2e;
        border-radius:14px;
        padding:24px;
    }

    h2{
        margin-top:0;
        font-size:24px;
    }

    .desc{
        color:#a1a1aa;
        line-height:1.7;
        margin-bottom:24px;
    }

    .install-btn{
        display:flex;
        align-items:center;
        justify-content:center;
        gap:8px;
        width:100%;
        height:52px;
        border-radius:12px;
        background:#007aff;
        color:#fff;
        text-decoration:none;
        font-size:17px;
        font-weight:600;
        transition:.2s;
    }

    .install-btn:active{
        transform:scale(.98);
        opacity:.9;
    }

    .tip{
        margin-top:18px;
        font-size:14px;
        color:#8e8e93;
        line-height:1.7;
    }

    .manual{
        margin-top:28px;
        padding-top:20px;
        border-top:1px solid #2c2c2e;
    }

    .manual-title{
        margin-bottom:10px;
        font-size:15px;
        color:#fff;
        font-weight:600;
    }

    .url-box{
        word-break:break-all;
        background:#2c2c2e;
        padding:12px;
        border-radius:10px;
        color:#d1d5db;
        font-size:13px;
        line-height:1.6;
    }

    .copy-btn{
        margin-top:12px;
        width:100%;
        height:44px;
        border:none;
        border-radius:10px;
        background:#2c2c2e;
        color:#fff;
        font-size:15px;
    }
</style>
</head>

<body>

<div class="card">

    <h2>🛠️ Shadowrocket 自用模块</h2>

    <div class="desc">
        点击下方按钮即可自动唤起 Shadowrocket 并导入模块。
    </div>

    <a
        class="install-btn"
        href="shadowrocket://addmodule?url=https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/ziyong.module"
    >
        🚀 一键安装模块
    </a>

    <div class="tip">
        💡 如果点击无反应：<br><br>
        1. 请确认已安装 Shadowrocket<br>
        2. 请使用 iPhone 自带 Safari 浏览器打开<br>
        3. 微信 / QQ / Telegram 内置浏览器可能会拦截跳转
    </div>

    <div class="manual">

        <div class="manual-title">
            手动导入链接
        </div>

        <div class="url-box" id="moduleUrl">
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/ziyong.module
        </div>

        <button class="copy-btn" onclick="copyUrl()">
            📋 复制模块链接
        </button>

    </div>

</div>

<script>
function copyUrl() {

    const text =
    'https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/ziyong.module';

    navigator.clipboard.writeText(text);

    alert('已复制模块链接');
}

// 部分浏览器需要 JS 主动触发
function installModule() {

    window.location.href =
    'shadowrocket://addmodule?url=https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/ziyong.module';
}
</script>

</body>
</html>