---
type: entity
name: Memory
aliases: [memory system, Claude Code memory]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 跨 session 的持久 memory（用户偏好、项目知识等）

## 关键属性

- 两套机制并存：**CLAUDE.md**（用户写的指令/规则）与 **Auto memory**（Claude 写的学习/模式，per-worktree）；两者均每 session 作为 context 加载，是建议而非强制 [[memory]] [[glossary]]
- CLAUDE.md scope 四层（specific overrides general）：managed policy（OS 级路径，无法 exclude）→ project (`./CLAUDE.md` 或 `./.claude/CLAUDE.md`)→ user (`~/.claude/CLAUDE.md`)→ local (`./CLAUDE.local.md`，gitignored) [[memory]] [[claude-directory]]
- 加载方式：从 cwd 沿目录树向上读所有 `CLAUDE.md` + `CLAUDE.local.md` 全部拼接（不覆盖），filesystem-root → cwd 顺序；同目录 `CLAUDE.local.md` 接 `CLAUDE.md` 之后；子目录的 CLAUDE.md 在 Claude 读子目录文件时 lazy-load [[memory]]
- 写作建议：每文件 <200 行（更长 adherence 变差）；用 markdown headers + bullets；具体优于模糊（"Use 2-space indentation" 优于 "Format properly"）；用 `claudeMdExcludes` 设置跳过无关祖先文件（managed policy 无法 exclude） [[memory]] [[best-practices]]
- `@import` 语法：`@README` / `@docs/foo.md` / `@~/.claude/...`；recursive 最大深度 5；相对路径解析以文件位置为基准；首次外部 import 触发 approval dialog，拒绝后静默 disable [[memory]]
- AGENTS.md 桥接：Claude Code **只读 CLAUDE.md**；要复用 AGENTS.md 须建 CLAUDE.md 并 `@AGENTS.md` import [[memory]]
- `/init` 自动 scaffold CLAUDE.md：分析 codebase 生成；已存在文件时建议改进而非覆盖；`CLAUDE_CODE_NEW_INIT=1` 启用多阶段交互流程（先选 artifacts → subagent 探索 codebase → reviewable proposal） [[memory]]
- `.claude/rules/` 模块化：`.md` 文件，无 `paths:` frontmatter 时跟 CLAUDE.md 一样 launch 加载；带 `paths:` glob 时只在 Claude 读匹配文件时载入；user `~/.claude/rules/` 比 project rules 先加载（project 优先级更高）；symlink 支持，环检测 [[memory]]
- 一次性 / 任务专属指令应用 **Skill** 而非 rule —— skill 仅在被 invoke 或 description 命中时加载 [[memory]]
- Auto memory（v2.1.59+ 默认开启）：存于 `~/.claude/projects/<project>/memory/`，按 git repo 派生，所有 worktree + 子目录共享一份；非 git 项目以项目根为单位 [[memory]] [[glossary]]
- Auto memory 布局：`MEMORY.md` 索引（每 session 加载前 200 行 / 25 KB）+ topic 文件（如 `debugging.md`，按需加载）；纯 markdown，可手编辑；UI 显示 "Writing memory" / "Recalled memory" [[memory]] [[glossary]]
- Auto memory 可控开关：`/memory` UI / `autoMemoryEnabled: false` 项目关 / `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` 全局关；`autoMemoryDirectory` 自定义路径（必须绝对或 `~/`），仅接受 user/policy/`--settings` scope，**拒绝 project/local**（防 cloned repo 把写入引到敏感路径） [[memory]] [[settings]]
- Auto memory **machine-local**，不跨 Mac/cloud env 同步；同一 repo 不同 worktree 共享一份 [[memory]]
- Subagent 可有自己的 auto memory [[memory]]
- Settings vs CLAUDE.md 分工：settings = 技术强制（deny tools / sandbox / env / forceLoginMethod）；CLAUDE.md = 行为引导（style / compliance reminders / instructions） [[memory]] [[best-practices]]
- Compaction 后行为：project-root CLAUDE.md 从磁盘重读；nested CLAUDE.md 在下次读子目录文件时 lazy 重载；**仅在对话里讲过的指令会丢失** —— 要持久化必须写入 CLAUDE.md [[memory]]
- 排查工具：`/memory` 验证文件已加载；`InstructionsLoaded` hook 可记日志；脚本场景用 `--append-system-prompt`（每次调用都得传，但适合脚本） [[memory]]
- 企业部署：managed CLAUDE.md 走 OS-level managed-policy 路径（macOS `/Library/Application Support/ClaudeCode/CLAUDE.md` / Linux `/etc/claude-code/CLAUDE.md` / Windows `C:\Program Files\ClaudeCode\CLAUDE.md`），通过 MDM / Group Policy / Ansible 推送，**无法被 `claudeMdExcludes` 排除** [[memory]] [[settings]]
- CLAUDE.md HTML 块级注释在注入前会被剥离（代码块内保留），可用于留 maintainer 笔记 [[memory]]

## 出现来源

_48 summaries reference this entity_:

- [[README--explanatory-output-style]]
- [[admin-setup]]
- [[agent-creation-prompt]]
- [[agent-creation-system-prompt]]
- [[agent-loop]]
- [[agent-teams]]
- [[auto-mode-config]]
- [[best-practices]]
- [[champion-kit]]
- [[changelog]]
- [[changelog--claude-code-repo]]
- [[claude-code-features]]
- [[claude-code-on-the-web]]
- [[claude-directory]]
- [[code-architect]]
- [[code-review]]
- [[code-review--plugin-command]]
- [[code-review--readme]]
- [[code-reviewer]]
- [[code-simplifier--plugin-agent]]
- [[commands]]
- [[communications-kit]]
- [[complete-agent-examples]]
- [[context-window]]
- [[costs]]
- [[debug-your-config]]
- [[desktop]]
- [[env-vars]]
- [[errors]]
- [[features-overview]]
- [[github-actions]]
- [[gitlab-ci-cd]]
- [[glossary]]
- [[hooks-guide]]
- [[how-claude-code-works]]
- [[learning-output-style--readme]]
- [[memory]]
- [[migration-guide]]
- [[modifying-system-prompts]]
- [[output-styles]]
- [[overview--agent-sdk]]
- [[overview--claude-code]]
- [[settings]]
- [[skills]]
- [[standard-plugin]]
- [[sub-agents]]
- [[subagents--agent-sdk]]
- [[third-party-integrations]]

## 相关

- [[Settings]] — `autoMemoryDirectory` / `autoMemoryEnabled` / `claudeMdExcludes` 等 memory 控制位均在 settings.json
- [[Skill]] — 任务专属、按需加载的指令应用 skill 而非 CLAUDE.md / rules
- [[Subagent]] — 可拥有独立的 auto memory，避免污染主上下文
- [[Hooks]] — `InstructionsLoaded` hook 用于排查"哪个 CLAUDE.md / rule 被加载了"
- [[Context-window]] — CLAUDE.md / auto memory 都占用 context；compaction 后部分会丢
- [[Agentic-loop]] — memory 是 agentic loop 跨 turn 持久化指令的主要载体
