---
type: concept
name: Agentic-loop
aliases: [agent loop, agentic loop, tool use loop]
category: concept
status: ga
created: 2026-05-05
---

## 一句话定义

Claude agent 的核心循环：思考 → 调工具 → 看结果 → 再思考

## 关键属性

- 三阶段循环：gather context → take action → verify results；阶段会混合进行，loop 适配任务类型（问题=偏 context 收集；bug fix=完整循环重复；refactor=偏 verification）[[how-claude-code-works]]
- 单 turn 定义：receive prompt → Claude emit text + 可选 tool call → SDK 执行 tool → 结果 feed back → 重复，直到 Claude 输出无 tool call 的 AssistantMessage + 终结的 ResultMessage [[agent-loop]]
- Loop 终止由 ResultMessage 的 `subtype` 标识：`success` / `error_max_turns` / `error_max_budget_usd` / `error_during_execution` / `error_max_structured_output_retries`；只有 `success` 才有 `result` 字段 [[agent-loop]]
- 控制开关：`max_turns`（封顶 tool-use 轮数）、`max_budget_usd`（成本封顶）、`effort`（low/medium/high/xhigh/max；Opus 4.7 推荐 xhigh）、`permission_mode` [[agent-loop]]
- 5 种核心 message 类型：SystemMessage（带 `subtype: "init"` / `"compact_boundary"`）/ AssistantMessage / UserMessage（含 tool result + checkpoint UUID）/ StreamEvent / ResultMessage [[agent-loop]]
- Read-only tool（包括 MCP 标 `readOnlyHint` 的）loop 内**并发执行**；state-modifying 串行；custom tool 默认串行 [[agent-loop]]
- Built-in tool 分四类：file ops（Read/Edit/Write）、search（Glob/Grep）、execution（Bash）、web（WebSearch/WebFetch），加 orchestration（Agent/Skill/AskUserQuestion/TodoWrite/ToolSearch）[[how-claude-code-works]] [[agent-loop]]
- 与 Client SDK 的本质差别：Client SDK 要你自己写 tool loop；Agent SDK 帮你跑 loop；Managed Agents 把 loop 跑在 Anthropic infra [[overview--agent-sdk]]
- 三大上下文管理 hook 在 loop 边缘运行而**不消耗 context**：PreToolUse / PostToolUse / Stop / SessionStart / SessionEnd / UserPromptSubmit 等 [[agent-loop]] [[hooks]]
- PreToolUse hook 可短路一次 tool call（return `permissionDecision: "deny"`），是干预 loop 的官方钩子 [[hooks]]
- Loop 内 prompt cache 自动启用；stable prefix（system prompt / CLAUDE.md / tool defs）被 cache，CLAUDE.md 在每个 request 重新注入 [[agent-loop]] [[cost-tracking]]
- 接近 context 上限自动 compact：emit `compact_boundary` system message，summarize 旧 history；可用 PreCompact hook（带 `trigger: "manual"|"auto"`）或 `/compact` 自定义 [[agent-loop]] [[context-window]]
- Trace 层级（OTel）：`claude_code.interaction`（一轮 turn）→ `claude_code.llm_request`（每次 API 调用）+ `claude_code.tool`（每个 tool 调用）+ `claude_code.hook`；subagent 通过 Task tool 调起的 spans 嵌在 parent 的 `claude_code.tool` 下 [[observability]] [[monitoring-usage]]
- Parallel tool call 会产生**多个共享同一 ID** 的 assistant message + 相同 usage，cost 计算时必须按 message ID dedupe，避免双计 [[cost-tracking]]

## 出现来源

_22 summaries reference this entity_:

- [[agent-design]]
- [[agent-loop]]
- [[best-practices]]
- [[context-window]]
- [[cost-tracking]]
- [[custom-tools--agent-sdk]]
- [[features-overview]]
- [[glossary]]
- [[hooks]]
- [[hooks--agent-sdk]]
- [[how-claude-code-works]]
- [[managed-agents-overview--claude-api-skill]]
- [[monitoring-usage]]
- [[observability]]
- [[overview--agent-sdk]]
- [[quickstart--agent-sdk]]
- [[sessions--agent-sdk]]
- [[sub-agents]]
- [[subagents--agent-sdk]]
- [[tool-use--python]]
- [[tool-use--typescript]]
- [[typescript--agent-sdk]]

## 相关

- [[Context-window]] — loop 每轮都要管 context（cache / compact / 决定加载什么）
- [[Tool-use]] — loop 的每一轮以 tool call → result → 下一轮形式推进
- [[Hooks]] — 在 loop lifecycle 的固定点 deterministic 触发，不消耗 context
- [[Subagent]] — 用独立 context 跑子 loop，把子任务 summary 回 main loop
- [[Permission-mode]] — 决定 loop 中每个 tool 是否执行 / 询问 / 拒绝
- [[Agent-SDK]] — SDK 把 loop 抽象成 `query()` async iterator
- [[Checkpointing]] — loop 中每个 file edit 自动 snapshot，可回滚
