---
type: concept
name: Context-window
aliases: [context window, 上下文窗口]
category: concept
status: ga
created: 2026-05-05
---

## 一句话定义

Claude 的 input + output token 上限（Opus 4.7 是 1M）

## 关键属性

- 包含：history + file contents + command outputs + CLAUDE.md + auto memory + skills + system instructions [[how-claude-code-works]] [[context-window]]
- Session 启动时即占用：system prompt ~4.2K tokens、auto memory `MEMORY.md` 首 200 行 / 25KB ~680 tokens、environment info ~280、MCP 名 ~120（schema 走 tool search）、skill descriptions ~450、user CLAUDE.md ~320 + project CLAUDE.md ~1.8K [[context-window]]
- 文件 read 是消耗大头；path-scoped rules（`.claude/rules/*.md` 带 `paths:` frontmatter）只在 Claude 读到匹配文件时 auto-load [[context-window]]
- MCP tool **定义默认 deferred**，只有名字占 context；`ENABLE_TOOL_SEARCH=auto` 在合并 token 超过 context 10% 时启用，`auto:N` 自定义阈值，<10 个 tool 时关掉反而更快 [[how-claude-code-works]] [[tool-search--agent-sdk]]
- Tool search 适用 Sonnet 4+ / Opus 4+；**Haiku 不支持**；catalog 上限 10000 tool，每次搜返回 3-5 个 [[tool-search--agent-sdk]]
- Skills 走"description 常驻 + body on-demand"；`disable-model-invocation: true` 连 description 都不进 context [[context-window]] [[how-claude-code-works]]
- Subagent 拿独立 context window：自带 system prompt（无 main session auto memory）、独立 CLAUDE.md 计费、独立 MCP+skills、parent 给的 task prompt；只把最终 text + 小 metadata 回 main [[context-window]] [[sub-agents]]
- Auto-compact 触发：先清旧 tool outputs，再 summarize 对话；project-root CLAUDE.md + auto memory 从盘上 reload；conversation-only 指令丢失，要持久必须写到 CLAUDE.md；nested CLAUDE.md / 带 `paths:` 的 rules 在 compact 后丢，下次读到对应文件再 lazy load [[context-window]] [[how-claude-code-works]]
- 调用过的 skill body 在 compact 后 re-inject，单 skill cap 5K / 总 25K，超出按 oldest 丢弃，所以**关键指令放 SKILL.md 顶部** [[context-window]]
- Thrashing 防护：若单一巨大文件 / output 导致 compact 后立即又满，Claude Code 自动 abort 几次重试 [[how-claude-code-works]]
- Bang command（`!cmd`）的 command 本体 + 输出**双双进入** context 作为下一条 message 前缀 [[context-window]]
- 检查工具：`/context` 显示 live 分类 + 优化建议；`/memory` 看加载的 CLAUDE.md 与 auto memory；`/mcp` 显示每个 server 的 context cost [[context-window]] [[how-claude-code-works]]
- Opus 4.7 context window 1M tokens（input + output 上限合计）[[2026-w17]]
- Context window 是 Claude Code 几乎所有 best practice 的根本约束："context fills fast and performance degrades as it does"，多数实操技巧都来自管理它 [[best-practices]]

## 出现来源

_30 summaries reference this entity_:

- [[2026-w17]]
- [[agent-design]]
- [[agent-loop]]
- [[agent-teams]]
- [[amazon-bedrock]]
- [[best-practices]]
- [[checkpointing]]
- [[claude-api-skill]]
- [[claude-code-features]]
- [[claude-code-on-the-web]]
- [[context-window]]
- [[costs]]
- [[custom-tools--agent-sdk]]
- [[desktop]]
- [[env-vars]]
- [[errors]]
- [[features-overview]]
- [[glossary]]
- [[google-vertex-ai]]
- [[how-claude-code-works]]
- [[managed-agents-core]]
- [[mcp--agent-sdk]]
- [[memory]]
- [[model-config]]
- [[sessions--agent-sdk]]
- [[slash-commands--agent-sdk]]
- [[sub-agents]]
- [[subagents--agent-sdk]]
- [[tool-search--agent-sdk]]
- [[troubleshooting]]

## 相关

- [[Memory]] — CLAUDE.md / auto memory 是 context 的两大持久来源
- [[Skill]] — description 常驻 / body on-demand 的核心 context-saving 机制
- [[Subagent]] — 独立 context window，把工作隔离不污染 main
- [[Agentic-loop]] — 每轮循环都要管 context（清旧 / compact / 决定加载什么）
- [[Agent-team]] — 各 teammate 独立 context，token 成本远高于 subagent
- [[Hooks]] — `hookSpecificOutput.additionalContext` 是 hook 注入 context 的官方通道
