---
type: entity
name: Output-style
aliases: [output style, output styles]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 输出格式的定制化风格

## 关键属性

- **修改 Claude Code 的 system prompt** 来设定 role / tone / 输出格式，同时保留核心能力（Bash、文件 I/O、TodoWrite）；可以**关掉默认 software-engineering 部分**（与 CLAUDE.md / `--append-system-prompt` 不同） [[output-styles]] [[glossary]]
- 三种内置 style：**Default**（现行 SE 系统 prompt）、**Explanatory**（在编码任务间插入 educational "Insights"）、**Learning**（学习模式，Claude 分享 Insights 同时插入 `TODO(human)` 让 user 写策略性代码块） [[output-styles]]
- 自定义 style：Markdown 文件 + frontmatter（`name` / `description` / `keep-coding-instructions: false`）；`keep-coding-instructions` 默认 `false`，**会 exclude** 默认编码指令（如 "verify code with tests"），设为 `true` 才保留 [[output-styles]]
- 存放位置：`~/.claude/output-styles/`（user）、`.claude/output-styles/`（project），plugin 通过 `output-styles/` 目录打包发布 [[output-styles]]
- 切换：`/config` → Output style 菜单 → 写到 `.claude/settings.local.json`；或直接在任意 settings 设 `outputStyle`；**下一次 session 启动生效**（保持稳定以利 prompt caching） [[output-styles]]
- Token 影响：input token 因更长 system prompt 而增（首次后由 prompt caching 抵消）；Explanatory + Learning 设计上产更长回复（output token 多） [[output-styles]]
- 与 CLAUDE.md / `--append-system-prompt` 区别：output style 可**关掉**默认 prompt 部分；CLAUDE.md 是作为 *user message* 接在默认 system prompt 后；`--append-system-prompt` 仅追加不删除 [[output-styles]] [[glossary]]
- 与 Subagent 区别：output style 影响主 agent loop / system prompt；Subagent 是任务调用的、有自己的 model / tools / when-to-use 上下文 [[output-styles]]
- 与 Skill 区别：output style 改的是 **Claude 怎么回复**（选定后一直生效）；Skill 是任务专属 prompt，通过 `/skill-name` 或自动 relevance 加载 [[output-styles]]
- Plugin 替代实现路径：把 deprecated 的 `Explanatory` / `Learning` style 用 `SessionStart` hook 重新实现并打包发布（`explanatory-output-style` / `learning-output-style` plugin）—— 比 output style 更灵活、可分发但有 token 成本 [[README--explanatory-output-style]] [[learning-output-style--readme]]
- Plugin 实现细节：`SessionStart` hook 跑 `${CLAUDE_PLUGIN_ROOT}/hooks-handlers/session-start.sh` 注入 instructions；空 matcher = 每次 session 启动都触发 [[learning-output-style--hooks]]
- 设计权衡：raw 文档明确建议 —— **超出软件开发范围的 output style 更应做成 subagent**（改 system prompt）而非 SessionStart hook（追加 prompt） [[README--explanatory-output-style]]
- Insight 格式（Explanatory / Learning style 推荐）：用 `★ Insight ──...──` 框格式给 2-3 个 codebase-specific 教育要点，不写通用编程概念 [[README--explanatory-output-style]] [[learning-output-style--readme]]
- 状态：Explanatory output style 已 deprecated，被 plugin 形式替代；Learning style 是 unshipped 形态、目前通过 plugin 提供 [[learning-output-style--readme]]

## 出现来源

_17 summaries reference this entity_:

- [[README--explanatory-output-style]]
- [[changelog--claude-code-repo]]
- [[claude-directory]]
- [[commands]]
- [[context-window]]
- [[discover-plugins]]
- [[explanatory-output-style--plugin-manifest]]
- [[glossary]]
- [[hooks--explanatory-output-style]]
- [[learning-output-style--hooks]]
- [[learning-output-style--readme]]
- [[learning-output-style-plugin-json]]
- [[modifying-system-prompts]]
- [[output-styles]]
- [[plugins]]
- [[plugins-reference]]
- [[settings]]

## 相关

- [[Settings]] — `outputStyle` key 在 settings.json 中持久化选定的 style
- [[Plugin]] — plugin 通过 `output-styles/` 目录打包；deprecated style 用 plugin + SessionStart hook 重生
- [[Hooks]] — `SessionStart` hook 是替代 output style 注入指令的常见模式
- [[Subagent]] — 超出软件开发范围的 style 更应做成 subagent（改 system prompt）
- [[Skill]] — Skill 影响"做什么"（任务调用），output style 影响"怎么回复"（一直生效）
- [[Memory]] — CLAUDE.md 是 user message 形式追加，与 output style 改 system prompt 互补
