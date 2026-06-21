# AI Maintenance Worklog

## 2026-06-21 02:58 - Work Record

### Task

Expanded overseas / international app-service ad cleanup coverage from public GitHub upstream modules and kept the additions under daily upstream sync.

### Start State

- Branch: `repair/upstream-app-sync`
- Git status summary: clean before this pass
- Expected scope: `Rewrite/Remotes/app-modules.json`, selected `Rewrite/Sources/Apps/*.conf`, upstream sync converter protection, generated Release/Web/Android/Windows outputs, reports, source indexes, and AI maintenance records

### Actual Changes

- Added 9 new direct-commit upstream app records:
  - `aol`
  - `go-com`
  - `lycos`
  - `mac-keeper`
  - `new-relic`
  - `openmultimedia`
  - `outlook`
  - `sape`
  - `yahoo`
- Synced those sources from `fmz200/wool_scripts` into `Rewrite/Sources/Apps/`.
- Added protected conversion filters for `dcapps.disney.go.com` and `seavideo-ak.espn.go.com` so Go.com upstream sync does not import Disney / ESPN video-core REJECT lines.
- Regenerated Fusion, Release Modules, Android, Windows v2rayN, Web catalog, checksums, generated script bundle, and reports through the Builder.
- Updated `Rewrite/Sources/Apps/README.md`, `PROJECT_STATE.md`, `AI_HANDOFF.md`, `docs/ai/TASKS.md`, `docs/ai/DECISIONS.md`, and `docs/ai/RISK_LOG.md`.

### Test Result

- `python -m py_compile scripts/sync_upstream_app_modules.py scripts/build_release_modules.py Rewrite/Generator/Builder.py` passed.
- `python scripts/sync_upstream_app_modules.py --no-kelee --id aol --id go-com --id lycos --id mac-keeper --id new-relic --id openmultimedia --id outlook --id sape --id yahoo` passed with 9 updated, 0 blocked, and 0 errors.
- `python Rewrite/Generator/Builder.py --profile fusion --release --check` passed.
- Builder output: 398 per-app modules, 0 empty modules, repository validation passed, profile validation passed, script aggregation validation passed, script bundle sandbox passed, upstream risk gate passed, Android format check passed, and governance extension validation passed.
- `git diff --check` passed.
- `python scripts/quality_gate.py` passed.

### Risk

- Medium. The new modules are mostly rule-only, but Yahoo adds an exact MITM hostname and Go.com required playback-core filtering.
- Broad high-risk platform candidates were intentionally skipped: Adobe activation/licensing, Apple / Google Safe Browsing, Microsoft CRL, and Amazon AWS core service hosts.
- Remaining risk: real app behavior is still manually tested by the owner. If a new foreign source breaks normal networking, disable or narrow the single affected `Rewrite/Sources/Apps/<slug>.conf` and its upstream record first.

### Self-Review

- What was not good enough: the first candidate list treated some platform-service snippets as normal foreign app modules even though they contained activation, Safe Browsing, CRL, or cloud-core endpoints.
- What I changed to reduce that risk: inspected candidate contents before adding, skipped broad platform snippets, and added converter-level Go.com video/core protection before syncing.
- What I would check first next time: scan each foreign candidate for platform security, licensing, playback, and cloud-service tokens before counting it as usable coverage.

### Next Step

- Commit and push if final diff review remains clean.

## 2026-06-21 00:22 - Work Record

### Task

Bulk-added missing GitHub app ad-cleaning modules into the GrandpaNiu app module factory and kept them under daily upstream sync.

### Start State

- Branch: `repair/upstream-app-sync`
- Git status summary: clean before this pass
- Expected scope: `Rewrite/Remotes/app-modules.json`, `Rewrite/Sources/Apps/`, upstream sync converter, generated Release/Web/Android/Windows outputs, reports, and AI maintenance records

### Actual Changes

- Added 94 new direct-commit upstream records to `Rewrite/Remotes/app-modules.json`.
- Synced 94 new app source fragments into `Rewrite/Sources/Apps/`.
- Added protected upstream conversion filters for `apd-pcdnwxlogin`, `msync-im`, and `ossgw.alicdn.com` in `scripts/sync_upstream_app_modules.py`.
- Regenerated Fusion, Release Modules, Android, Windows v2rayN, Web catalog, checksums, and reports through the Builder.
- Updated `Rewrite/Sources/Apps/README.md`, `Rewrite/Registry.md`, `Web/registry.md`, `PROJECT_STATE.md`, `AI_HANDOFF.md`, `docs/ai/TASKS.md`, and `docs/ai/RISK_LOG.md`.

### Test Result

- `python -m py_compile scripts/sync_upstream_app_modules.py scripts/build_release_modules.py Rewrite/Generator/Builder.py` passed.
- `python scripts/sync_upstream_app_modules.py --no-kelee ...` synced the selected new modules with 0 blocked modules after retrying one transient GitHub raw fetch failure.
- `python Rewrite/Generator/Builder.py --profile fusion --release --check` passed.
- Builder output: 389 per-app modules, 0 empty modules, repository validation passed, profile validation passed, script aggregation validation passed, script bundle sandbox passed, upstream risk gate passed, Android format check passed, and governance extension validation passed.

### Risk

- Medium to high. This pass adds many app-scoped rules and MITM/script entries at once.
- Mitigation: no VIP/member unlock, payment bypass, login bypass, token/cookie rewrite, receipt forgery, or account-sharing modules were intentionally added.
- Mitigation: protected login/message/CDN entries are filtered during conversion.
- Remaining risk: real app behavior is still manually tested by the owner. If an app breaks, disable or narrow the single affected `Rewrite/Sources/Apps/<slug>.conf` first.

### Self-Review

- What was not good enough: the first sync allowed protected CDN/login-looking lines from upstream into two new app files before the risk scan.
- What I changed to reduce that risk: added converter-level protected filters and regenerated the affected sources before building.
- What I would check first next time: run the protected-token scan before committing any converted source files, especially after bulk imports.

### Next Step

- Run final quality gate and diff review.
- Commit and push if validation remains clean.

## 2026-06-20 22:58 - Work Record

### Task

Added a required AI self-review habit for future maintenance work.

### Start State

- Branch: `repair/upstream-app-sync`
- Git status summary: clean before this pass
- Expected scope: AI maintenance process documents only

### Actual Changes

- Added `docs/ai/SELF_REVIEW.md`.
- Updated `AGENTS.md` to require the self-review before final response, commit, or push.
- Updated `PROJECT_STATE.md`, `AI_HANDOFF.md`, `docs/ai/TASKS.md`, and `docs/ai/DECISIONS.md`.
- No business rules, generated outputs, Android files, Windows files, Web files, reports, or workflow runtime logic were changed.

### Test Result

- `git diff --check` passed.
- `python scripts/validate_repository.py` passed.

### Risk

- Low. This is a process/documentation-only change.

### Self-Review

- What was not good enough: the repository had strong startup and validation rules, but no explicit end-of-task self-critique habit.
- What I changed to reduce that risk: added a reusable self-review checklist and wired it into `AGENTS.md`, handoff, tasks, decisions, and worklog expectations.
- What I would check first next time: whether the latest worklog entry includes a real self-review instead of only listing commands.

### Next Step

- Run documentation validation, then commit and push if clean.

## 2026-06-20 22:41 - Work Record

### Task

Checked failed repository workflows and repaired the latest `Module Factory Build` failure.

### Start State

- Branch: `repair/upstream-app-sync`
- Git status summary: clean before this repair
- Expected scope: workflow/governance validation script and AI maintenance records

### Actual Changes

- Updated `scripts/validate_governance_extensions.py`.
- Updated `PROJECT_STATE.md`, `AI_HANDOFF.md`, `docs/ai/TASKS.md`, `docs/ai/DECISIONS.md`, and this worklog.
- No rules, app sources, generated Release files, Android outputs, Windows outputs, Web files, or report outputs were changed in the main worktree.

### Root Cause

The latest `Module Factory Build` failed because `scripts/validate_governance_extensions.py` still required the old `fusion-build-marker: scripts/build_module.py --build --profile fusion` workflow marker. The workflow now uses the preferred Builder entrypoint, so the validation script rejected a correct workflow.

### Test Result

- `python -m py_compile scripts/validate_governance_extensions.py scripts/validate_repository.py scripts/repository_health_check.py Rewrite/Generator/Builder.py` passed.
- `python scripts/validate_governance_extensions.py` passed.
- `python scripts/validate_repository.py` passed.
- In a repository-external worktree, `python Rewrite/Generator/Builder.py --profile fusion --release --check` passed.
- In a repository-external worktree, `python scripts/quality_gate.py` passed.

### Risk

- Low. The fix changes validation logic only and does not change module rules or generated outputs.
- The temporary worktree under `../_codex_private_logs/GrandpaNiu/` is local-only and must not be committed.

### Next Step

- Commit and push the CI repair, then confirm GitHub Actions rerun status.

## 2026-06-20 22:12 - Work Record

### Task

Recorded the owner instruction that rule changes must require real app abnormal behavior, client logs, packet captures, or another reproducible signal.

### Start State

- Branch: `repair/upstream-app-sync`
- Git status summary: documentation and workflow cleanup already in progress
- Expected scope: AI maintenance records only

### Actual Changes

- Updated `PROJECT_STATE.md`, `AI_HANDOFF.md`, `docs/ai/DECISIONS.md`, `docs/ai/RISK_LOG.md`, and `docs/ai/TASKS.md`.
- No rules, scripts, generated outputs, Android files, Windows files, Web files, reports, or workflow files were changed by this note.

### Test Result

- `git diff --check` passed.
- Workflow text scan found no `git add -A` and confirmed Builder usage where expected.
- `python -m py_compile scripts/validate_repository.py scripts/repository_health_check.py Rewrite/Generator/Builder.py` passed.
- `python scripts/validate_repository.py` passed.
- Full build was not run in the main worktree because this pass intentionally avoids refreshing generated outputs.

### Risk

- Low. This is a maintenance-record clarification only.

### Next Step

- Owner approved commit and push after validation.

## 2026-06-20 22:09 - 工作记录

### 本次任务

先做文档和 workflow 小修：

- 记录当前“工作树干净、本地领先 1 commit、本次只读体检已完成”。
- 将旧四版本文档统一改为 Fusion 单模块策略，历史四版本只作为 deprecated / legacy reference。
- 不碰规则，只把 `reject_risk_report.md` 中的高风险 REJECT 项整理成待复核清单。
- workflow 优先把宽泛 `git add -A` 改成明确路径，并逐步统一构建入口。

### 开始前状态

- 分支：`repair/upstream-app-sync`
- git status 摘要：工作树干净
- 本地领先：比 `origin/main` 领先 1 个提交
- 预计修改范围：
  - `PROJECT_STATE.md`
  - `AI_HANDOFF.md`
  - `docs/ai/*`
  - `docs/FOUR_PROFILE_GOVERNANCE.md`
  - `docs/LOCAL_ENV_SETUP.md`
  - `docs/ROADMAP.md`
  - `docs/MAINTENANCE_PLAYBOOK.md`
  - `.github/workflows/*.yml`

### 实际修改

- 更新 AI 维护记录，记录只读体检、当前分支状态、未 push 的本地领先提交。
- 重写旧四版本相关文档，将 Stable / Stable Plus / Lite / Full 标记为 deprecated / legacy reference。
- 在 `docs/ai/RISK_LOG.md` 中整理待复核清单：
  - 2 条银行 / 支付风险
  - 7 条图片 / CDN 风险
  - 9 条国内核心 API 风险
- workflow 小修：
  - 将 6 处 `git add -A` 改成明确路径。
  - 将 selected daily/audit/collect 构建步骤逐步切到 `Rewrite/Generator/Builder.py --profile fusion --release`。

### 测试结果

- 待执行最终 diff 和轻量检查。
- 本次不运行会刷新生成物的主仓库构建命令。

### 风险

- 未修改 `Rules/`，所以待复核 REJECT 风险只是记录，不改变模块行为。
- workflow 修改会影响自动提交范围，必须检查 YAML 文本和 `git add -A` 是否已清除。
- 旧四版本文档被替换为 Fusion 策略说明，属于文档策略更新。

### 下一步

- 检查 `git diff --stat`、`git diff --name-only`。
- 检查是否仍存在 workflow `git add -A`。
- 只做不会刷新生成物的轻量验证。

## 2026-06-20 21:40 - 工作记录

### 本次任务

执行格式修复后的验证，不修改业务代码。

### 开始前状态

- 分支：`repair/upstream-app-sync`
- git status 摘要：仅 `.gitignore` 和 AI 维护文档有未提交修改
- 预计修改范围：
  - `PROJECT_STATE.md`
  - `AI_HANDOFF.md`
  - `docs/ai/TASKS.md`
  - `docs/ai/WORKLOG.md`

### 实际修改

- 更新 `PROJECT_STATE.md`：记录格式修复后的验证结果。
- 更新 `AI_HANDOFF.md`：记录本次验证已在仓库外临时副本中通过。
- 更新 `docs/ai/TASKS.md`：将当前格式修复任务标记为 validated，等待 owner 审查和可选提交。
- 更新 `docs/ai/WORKLOG.md`：追加本条验证记录。

### 测试结果

先执行并确认：

```bash
git status
git diff --stat
git diff --name-only
```

确认修改范围只包含：

- `.gitignore`
- `AGENTS.md`
- `PROJECT_STATE.md`
- `AI_HANDOFF.md`
- `docs/ai/DECISIONS.md`
- `docs/ai/RISK_LOG.md`
- `docs/ai/TASKS.md`
- `docs/ai/WORKLOG.md`

随后在仓库外临时副本运行：

```bash
python scripts/quality_gate.py
python scripts/validate_repository.py
python scripts/repository_health_check.py
```

结果：全部通过。

说明：第一次执行验证时误在主工作树运行，导致生成物刷新；这些由验证产生的 `Android/`、`Release/`、`Scripts/generated/`、`reports/` 改动已撤回。第二次验证已正确切换到仓库外临时副本，主工作树最终仍只保留允许范围内的文档和 `.gitignore` 改动。

### 风险

- 业务风险低。
- 本次不保留任何业务文件、生成物、Android、Windows、Web、reports 或 workflow 改动。
- 临时验证目录位于 `../_codex_private_logs/GrandpaNiu/`，不提交到 Git。

### 下一步

- 由 owner 审查 diff。
- 如果确认无误，可提交。

建议提交信息：

```text
docs: normalize AI maintenance records
```

## 2026-06-20 12:22 - 工作记录

### 本次任务

修复 AI 维护记录和 `.gitignore` 的 Markdown / ignore 规则格式问题。

本次只允许修改维护文档和 `.gitignore`，不修改规则、脚本、Release、Android、Windows、Web、reports 或 workflow 业务逻辑。

### 开始前状态

- 分支：`repair/upstream-app-sync`
- git status 摘要：干净
- 预计修改范围：
  - `.gitignore`
  - `AGENTS.md`
  - `PROJECT_STATE.md`
  - `AI_HANDOFF.md`
  - `docs/ai/TASKS.md`
  - `docs/ai/DECISIONS.md`
  - `docs/ai/RISK_LOG.md`
  - `docs/ai/WORKLOG.md`

### 实际修改

- 修改 `.gitignore`：
  - 恢复和确认多行格式。
  - 增加 `.env.*`、`_codex_private_logs/`、`*.local.md` 等本地私有记录和本地文件忽略规则。
- 修改 `AGENTS.md`：
  - 统一标题、列表和命令代码块。
  - 增加“不要自动 commit / push”的规则。
  - 增加“AI maintenance Markdown files must remain readable Markdown”的规则。
- 修改 `PROJECT_STATE.md`、`AI_HANDOFF.md`、`TASKS.md`、`DECISIONS.md`、`RISK_LOG.md`：
  - 统一 Markdown 结构。
  - 补充本次格式维护状态和风险说明。
- 修改 `docs/ai/WORKLOG.md`：
  - 恢复为可读的标准 Markdown 工作记录。

### 测试结果

- 已执行：

```bash
git status
git branch --show-current
```

- 本次未运行业务构建。
- 原因：本次只修改 AI 维护文档和 `.gitignore`，不改变构建脚本、规则源、Release 输出、Android 输出、Windows 输出、Web 输出、reports 或 workflow 业务逻辑。

### 风险

- 业务风险低。
- 主要风险是文档格式再次被压缩，所以已在 `AGENTS.md` 和 `RISK_LOG.md` 中增加可读 Markdown 规则。

### 下一步

- 由 owner 检查 diff。
- 如果确认无误，可提交。

建议提交信息：

```text
docs: normalize AI maintenance records
```

## 2026-06-20 11:58 - 工作记录

### 本次任务

建立 GrandpaNiu 仓库的 AI 维护记录制度，只做初始快照，不修改业务代码。

### 开始前状态

- 分支：`repair/upstream-app-sync`
- git status 摘要：干净
- 预计修改范围：
  - `AGENTS.md`
  - `PROJECT_STATE.md`
  - `AI_HANDOFF.md`
  - `docs/ai/*`
  - 仓库上一级本地私有记录目录

### 实际修改

- 修改文件：
  - `AGENTS.md`
  - `PROJECT_STATE.md`
  - `AI_HANDOFF.md`
  - `docs/ai/TASKS.md`
  - `docs/ai/DECISIONS.md`
  - `docs/ai/RISK_LOG.md`
  - `docs/ai/WORKLOG.md`
- 修改原因：为后续 AI 或新对话接手项目提供固定记录、风险规则、任务状态和交接入口。

### 测试结果

- 已执行初始仓库结构扫描。
- 已执行 `git status --short`，开始前工作树干净。
- 已执行 `git branch --show-current`，当前分支为 `repair/upstream-app-sync`。

### 风险

- 本次只新增和更新维护文档，不触碰规则、脚本、Release 产物、Android 输出、Windows 输出或 workflow 业务逻辑。
- 后续任何 AI 修改业务逻辑前必须先读取本记录体系。

### 下一步

- 提交维护记录文件。
- 后续修改必须追加 `docs/ai/WORKLOG.md`，并按需要更新 `TASKS`、`DECISIONS`、`RISK_LOG`、`PROJECT_STATE` 和 `AI_HANDOFF`。
## 2026-06-21 06:44 - App 源语法与长期维护加固

### 本次任务

对仓库执行证据优先的完整自检，修复可复现的 App 独立模块语法问题，并加强每日失效源审计和质量门禁。

### 开始前状态

- 分支：`repair/upstream-app-sync`
- 基线提交：`66b30090`
- git status 摘要：开始时干净；审计脚本随后刷新了两份报告
- 预计修改范围：App 上游转换器、App 源验证器、相关测试/门禁、受影响源、生成产物和维护记录

### 实际修改

- 新增 `scripts/validate_app_sources.py`，逐个验证 398 个 App 源和 398 个 Release App 模块。
- 修复 `scripts/sync_upstream_app_modules.py` 的混合 Rule、307 重定向、Header Rewrite、裸域名、Map Local、远程数据内联和重复脚本名转换。
- 从已登记上游重同步 17 个受影响 App 源；未新增未知上游或猜测规则。
- 将 App 源验证接入 Builder、质量门禁、治理校验、仓库健康和自动化证据。
- 将失效源审计扩展到 App 源，并用 12 路上限并发检查唯一 URL，避免每日 workflow 串行超时。
- 通过 Builder 重新生成 Fusion、Release Modules、Android、Windows、Web 和 reports。

### 测试结果

- 14 项单元测试通过。
- `python scripts/validate_app_sources.py`：398 个源、398 个 Release 模块、0 语法错误。
- `python Rewrite/Generator/Builder.py --profile fusion --release --check`：通过，398 个模块、0 empty。
- `python scripts/quality_gate.py`：通过。
- 仓库健康报告：0 blocking issue；Root / Release 一致；无重复脚本名；无重复 MITM hostname。

### 风险

- 未修改登录、支付、银行、验证码、视频播放或图片/CDN 的策略。
- RedNote、Weibo、Zhihu 在重同步前保留了回滚备份。
- 静态检查不能证明所有国内外 App 的真机行为；后续只依据实际异常和日志做 source-first 单点修复。

### Self-Review

- What was not good enough: 旧门禁只验证 Fusion 成品，独立 App 模块可带着错误发布；首次扩展失效源审计时也需要评估请求规模。
- What I changed to reduce that risk: 增加源/Release 双层阻断验证、转换单测、有限并发和高风险备份。
- What I would check first next time: 先运行 App 源验证和 Builder，再检查 Actions 的 Module Factory Build 与 Upstream app module sync 实际结果。

### 下一步

- 提交并推送本次修改。
- 观察远端 Module Factory Build、Upstream app module sync 和 Repository Health。
- 只有出现真实 App 异常或日志证据时才调整具体流量规则。

## 2026-06-21 07:24 - 质量门禁与自动发布加固

### 本次任务

继续对仓库做证据驱动的自检，修复可复现的自动化假绿和 workflow 并发写入风险，不改动 App 流量规则。

### 开始前状态

- 分支：`repair/upstream-app-sync`
- 基线提交：`173a92eb`
- git status 摘要：工作树干净
- 预计修改范围：质量门禁、工作流提交逻辑、验证脚本、测试和 AI 记录

### 实际修改

- 修复 `quality_gate.py` 顺序：最后一次 profile 重建后再校验 bundle 语法、聚合一致性和运行时沙箱。
- freshness 改为 `--strict`，阻断报告过期时 CI 必须失败。
- 9 个维护 workflow 使用按 workflow/ref 隔离的 `module-maintenance-*` 并发锁。远程 #555 证明单一全局锁会取消较早的 pending 运行，因此不再共享一个固定 group。
- 仅保留 `Module Factory Build` 的 push 验收；每日审计和计划更新只保留 schedule/manual 触发。
- 重写 `commit_generated_changes.sh`：仅暂存显式路径，push 失败后 fetch + rebase + retry，冲突时停止而不覆盖。
- 移除维护自动化中的 `git reset --hard` 和 `git add -A`。
- 增加 freshness 顺序、workflow 契约和本地裸 Git 远端提交集成测试。
- 修复 `workflow-failure-issue.yml` 的 shell heredoc 命令替换；Issue #248 中被清空的状态名和恢复命令现在由 Python 安全写入 Markdown。

### 测试结果

- 20 项单元/集成测试通过。
- 10 个 workflow YAML 全部可解析。
- `bash -n scripts/commit_generated_changes.sh` 通过。
- `python Rewrite/Generator/Builder.py --profile fusion --release --check` 通过。
- `python scripts/quality_gate.py` 通过，并且使用严格 freshness。
- 398 个 App 模块、0 empty、17 个远程源 0 warning。

### 风险

- 未修改 Rules、App 源、MITM、登录、支付、银行、验证码、视频或 CDN 策略。
- 不能用静态语法检查代替全部 App 真机联网验证。
- 新提交助手遇到 rebase 冲突会主动失败，交给故障 issue 流程处理，不会自动覆盖。

### Self-Review

- What was not good enough: 上一次只看到质量门禁返回成功，没有立即对照 freshness 报告的阻断数；第一版并发修复又误用了全局 group，直到远程 #555 被取消才证明该设计不成立。
- What I changed to reduce that risk: 把报告语义、进程退出码、隔离并发锁、单一 push 验收和提交助手都写成自动回归测试。
- What I would check first next time: 先看远端 Module Factory Build 是否绿色，再检查定时工作流是否在共享并发锁下顺序运行。

### 下一步

- 审查最终 diff，刷新健康与 freshness 报告。
- 提交并推送后核对 GitHub Actions。
## 2026-06-22 02:33 - 每日工作流跨任务写入冲突修复

### 本次任务

检查 2026-06-22 的每日工作失败，修复真实故障并确保不同维护 workflow 不再并行发布旧快照。

### 开始前状态

- 分支：`repair/upstream-app-sync`
- 基线提交：`05ba8813`
- 同步远端后基线：`376713d4`
- git status 摘要：开始时工作树干净，本地落后远端 4 个自动维护提交，已用 fast-forward 同步
- 预计修改范围：workflow、自动化锁、验证脚本、回归测试、AI 记录；不改业务规则

### 实际修改

- 审计今天所有 Actions：除 invalid-rule audit 定时运行外，其余每日维护与 Pages 成功。
- 确认失败 run `27913047570` 的审计和 Fusion 构建步骤成功，仅提交步骤失败。
- 根据运行时序与提交历史确认根因：GitHub 将不同 schedule 延迟到同一分钟，两个 writer 从同一提交生成，后提交者在安全 rebase 时遇到生成文件冲突。
- 新增 `tools/acquire_automation_lock.sh` 和 `tools/release_automation_lock.sh`。
- 9 个写入型 workflow 在生成前获取远端锁、快进到最新 main，并在所有结果下释放锁。
- 更新仓库验证和健康摘要，要求每个 writer 同时具备锁获取、无条件释放、显式路径提交与安全 rebase。
- 增加真实裸 Git 集成测试，验证第二个 writer 被阻止并在锁释放后快进继续。
- 初版路径曾放在 `scripts/`；自检发现 Windows 会与 `Scripts/` 大小写折叠，提交到 Linux 会找不到文件，因此在提交前移至 `tools/` 并重新完成验证。

### 测试结果

- Shell 语法：3 个维护脚本通过 `bash -n`。
- 10 个 workflow YAML 文件通过 PyYAML 解析。
- 13 项自动化专项测试通过。
- 完整质量门禁通过：21 项测试、398 个 App 源、398 个 Release 模块、0 empty、3806 个源条目。
- Fusion：6097 行；Android：941 条主规则；17 个远程源 0 warning。
- 仓库健康：0 blocking issue；报告新鲜度：14 fresh、0 stale/missing。
- 三个公开 Fusion 入口内容一致。

### 风险

- 本次不修改 Rules、App 源、MITM、登录、支付、银行、验证码、播放或 CDN 策略。
- 远端锁 stale threshold 为 1 小时；若未来单个任务接近或超过 1 小时，应先评估超时阈值。
- 仍需下一次 scheduled invalid-rule audit 作为远端最终确认，Issue #249 应在成功后自动关闭。

### Self-Review

- What was not good enough: 先前只用按 workflow 隔离的 concurrency，能避免同名任务互相取消，却没有覆盖不同 workflow 被 GitHub 延迟到同一时刻的写入冲突；初版锁脚本路径也忽略了 Windows 对 `Scripts/` / `scripts/` 的大小写折叠。
- What I changed to reduce that risk: 增加跨 workflow 原子远端锁、所有情况下释放、stale 回收、workflow 契约检查、真实 Git 并发测试，并把脚本移到无大小写歧义的 `tools/`。
- What I would check first next time: 先看下一次 invalid-rule audit 的 Acquire/Release lock 步骤和 Issue #249 状态，再看其他 writer 是否有等待锁但最终成功的记录。

### 下一步

- 提交并推送本次自动化修复。
- 检查由 push 触发的 Module Factory Build。
- 等待或手动触发 invalid-rule audit，确认 Issue #249 自动关闭。
