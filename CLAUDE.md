# GrandpaNiu 仓库维护约定

本文件给 AI 助手、Codex、Claude、ChatGPT 或维护者使用。普通用户不需要阅读。

## 提交标题格式

统一使用：

```text
类型: 简短说明
```

标题要求：

- 使用中文说明，保持简短清楚。
- 不要写无意义标题，例如 `update`、`fix bug`、`修改文件`。
- 一次提交只做一类事情，避免把规则、网页、README、构建产物混在一起。
- 标题不要夸大效果，不写“完美”“永久”“100% 去广告”等绝对表述。

## 常用类型

| 类型 | 使用场景 | 示例 |
|---|---|---|
| `feat:` | 新增规则、新增模块、新增功能 | `feat: 新增某 App 去广告规则` |
| `fix:` | 修复模块、规则、播放、导入、构建错误 | `fix: 修复 Fusion 模块构建问题` |
| `docs:` | 修改 README、说明文档、教程 | `docs: 更新 README 安装说明` |
| `web:` | 修改 GitHub Pages、导入页、跳转页、页面样式 | `web: 调整 Pages 导入页面` |
| `chore:` | 同步 Release、报告、构建产物、杂项维护 | `chore: 同步 Release 构建产物` |
| `refactor:` | 重构脚本或目录，不改变功能 | `refactor: 整理模块构建脚本结构` |
| `test:` | 新增或修复校验、测试、健康检查 | `test: 更新仓库健康检查规则` |
| `ci:` | 修改 GitHub Actions、自动化流程 | `ci: 调整每日构建工作流` |
| `revert:` | 回滚之前的提交 | `revert: 回滚误杀规则变更` |

## 提交正文建议

复杂提交建议写正文，格式如下：

```text
fix: 修复 YouTube 播放异常

- 移除 googlevideo.com 强制直连
- 保留 YouTube 响应脚本去广告
- 避免恢复 UDP/QUIC 拦截规则
```

## AI 协作署名

只有在确实由对应 AI 工具参与撰写或修改时，才添加协作署名。

Claude 参与时可使用：

```text
Co-Authored-By: Claude <noreply@anthropic.com>
```

不要为了显示“AI 撰写”而伪造署名。ChatGPT、Codex 或其他工具参与时，不要硬写 Claude。

## 规则来源原则

广告规则不能靠 AI 凭空编造。新增规则应至少满足一种来源：

- 抓包验证
- 上游公开规则源
- 用户实测反馈
- 已存在规则转换
- 明确可复现的请求域名或路径

AI 可以辅助整理格式、去重、解释风险，但不应随机生成域名或接口。

## 修改范围原则

- 修改 README：使用 `docs:`。
- 修改 `import.html`、`redirect.html`、`android.html`：使用 `web:`。
- 修改 `Rules/`、`Scripts/`、`Rewrite/`：使用 `feat:` 或 `fix:`。
- 仅同步 `Release/`、`reports/`、最终模块产物：使用 `chore:`。
- 修复构建脚本或校验脚本：使用 `fix:`、`refactor:` 或 `test:`。

## 构建产物原则

不要只手动修改最终文件：

```text
Ronghemokuai.sgmodule
Release/Ronghemokuai.sgmodule
```

应优先修改源文件，再运行构建脚本生成最终模块。

推荐流程：

```bash
python scripts/build_module.py --build --profile fusion
python scripts/factory_finalize.py --sync-root
python scripts/build_release_variants.py
python scripts/validate_repository.py
```

## 安全检查

涉及规则、脚本、MITM、Rewrite 的变更，提交前至少检查：

- 不重复 `[Script]` 区块
- 不重复脚本名称
- 不重复 MITM hostname
- 不强行 MITM 视频 CDN，例如 `googlevideo.com`
- 不随意恢复 YouTube UDP/QUIC 拦截
- 不把测试规则直接当稳定规则发布
