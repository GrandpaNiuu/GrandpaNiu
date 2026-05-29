# 模块工厂完整流程

本文件用于说明当前仓库的完整模块工厂流程。

## 总体目标

仓库最终采用以下模式：

```text
Profiles + Remotes + Rules + Scripts + Rewrite/Sources
        ↓
scripts/build_module.py
        ↓
Release/Ronghemokuai.sgmodule
        ↓
scripts/factory_finalize.py
        ↓
Ronghemokuai.sgmodule
```

也就是说：

- `Profiles` 决定构建模式。
- `Remotes` 提供机器可读的远程规则源。
- `Rules` 提供本地规则源。
- `Scripts` 提供脚本源。
- `Rewrite/Sources` 提供模块区块片段。
- `Release` 保存生成后的发布副本。
- 根目录 `Ronghemokuai.sgmodule` 是最终正式导入入口。

## 目录职责

| 目录 / 文件 | 作用 |
|---|---|
| `Rewrite/Profiles/*.conf` | 构建配置，例如 stable / full |
| `Rewrite/Remotes/sources.json` | 机器可读远程规则源清单 |
| `Rules/*.list` | 本地规则源，参与 `[Rule]` 构建 |
| `Scripts/*.conf` | 脚本源，参与 `[Script]` 构建 |
| `Rewrite/Sources/*.conf` | 主模块拆分片段和 Rewrite / MITM 来源 |
| `scripts/build_module.py` | 读取各类源文件并生成 Release 模块 |
| `scripts/factory_finalize.py` | 拆分规则和脚本，并把 Release 同步到根目录主模块 |
| `Release/Ronghemokuai.sgmodule` | 生成后的发布副本 |
| `Ronghemokuai.sgmodule` | Shadowrocket / Surge 正式导入入口 |
| `reports/module_factory_report.md` | 工厂构建报告 |
| `reports/module_factory_diff_report.md` | Release 与根目录主模块差异报告 |
| `reports/factory_finalize_report.md` | 最终同步和拆分报告 |

## 构建流程

### 1. 读取根目录主模块

工作流先执行：

```text
python3 scripts/build_module.py --extract-from-root --build --profile stable
```

它会把根目录主模块拆分到：

```text
Rewrite/Sources/Meta.conf
Rewrite/Sources/Rule.conf
Rewrite/Sources/URL-Rewrite.conf
Rewrite/Sources/Header-Rewrite.conf
Rewrite/Sources/Body-Rewrite.conf
Rewrite/Sources/Map-Local.conf
Rewrite/Sources/Script.conf
Rewrite/Sources/MITM.conf
```

### 2. 读取 profile

默认读取：

```text
Rewrite/Profiles/stable.conf
```

profile 决定哪些来源参与构建：

```text
Rules/
Scripts/
Rewrite/Remotes/sources.json
Rewrite/Sources/
```

### 3. 读取远程源

机器可读远程源来自：

```text
Rewrite/Remotes/sources.json
```

生成器会把启用的 `RULE-SET` / `DOMAIN-SET` 转换为 Surge / Shadowrocket 可识别规则。

### 4. 读取 Rules

规则源来自：

```text
Rules/spotify-direct.list
Rules/youtube-direct.list
Rules/reject.list
Rules/app-clean.list
Rules/web-ads.list
```

这些内容会参与 `[Rule]` 区块构建。

### 5. 读取 Scripts

脚本源来自：

```text
Scripts/spotify.conf
Scripts/youtube.conf
Scripts/app-clean.conf
```

这些内容会参与 `[Script]` 区块构建。

### 6. 读取 Rewrite/Sources

模块片段来自：

```text
Rewrite/Sources/URL-Rewrite.conf
Rewrite/Sources/Header-Rewrite.conf
Rewrite/Sources/Body-Rewrite.conf
Rewrite/Sources/Map-Local.conf
Rewrite/Sources/MITM.conf
```

同时保留 `Rule.conf` 和 `Script.conf` 作为过渡兼容来源，避免一次性迁移造成丢失。

### 7. 生成 Release

生成结果写入：

```text
Release/Ronghemokuai.sgmodule
```

生成时会校验：

```text
[Rule]
[Script]
[MITM]
spotify-json
spotify-proto
youtube.response
update-url
```

### 8. 最终同步根目录主模块

工作流随后执行：

```text
python3 scripts/factory_finalize.py
```

它会：

1. 从 `Rewrite/Sources/Rule.conf` 拆分规则到 `Rules/`。
2. 从 `Rewrite/Sources/Script.conf` 拆分脚本到 `Scripts/`。
3. 校验 `Release/Ronghemokuai.sgmodule`。
4. 把 `Release/Ronghemokuai.sgmodule` 同步到根目录 `Ronghemokuai.sgmodule`。
5. 生成 `reports/factory_finalize_report.md`。

## 自动工作流

完整流程由以下工作流执行：

```text
.github/workflows/module-factory-build.yml
```

手动运行路径：

```text
Actions
→ Module Factory Build
→ Run workflow
```

该工作流会提交：

```text
Ronghemokuai.sgmodule
Rewrite/Sources/
Release/Ronghemokuai.sgmodule
Rules/
Scripts/
reports/module_factory_report.md
reports/module_factory_diff_report.md
reports/factory_finalize_report.md
```

## 安全校验

构建和同步过程中必须保留：

```text
[Rule]
[Script]
[MITM]
spotify-json
spotify-proto
youtube.response
#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule
```

缺少任意一项时，流程应直接失败，避免提交损坏模块。

## 当前框架状态

当前仓库已经具备完整流程：

```text
源文件参与构建
Release 生成
Release 同步根目录主模块
Rules / Scripts 自动拆分
报告生成
Actions 自动提交
```

仍需人工观察：

- 首次运行后 `reports/module_factory_diff_report.md` 的差异是否合理。
- `reports/factory_finalize_report.md` 的规则 / 脚本拆分数量是否合理。
- Shadowrocket 导入后 Spotify / YouTube 是否正常。

## 不加入的内容

不加入 `.claude` 和 `CLAUDE.md`。

原因：这类文件是特定工具配置，会增加公开仓库中的工具痕迹，不影响模块工厂流程本身。
