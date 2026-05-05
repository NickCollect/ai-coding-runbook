---
type: entity
name: Tool-runner
aliases: [tool runner / beta_tool / betaZodTool / runner abstraction]
category: api-feature
status: beta
created: 2026-05-05
---

## 一句话定义

Anthropic SDK 的 [[Agentic-loop]] 抽象 —— 自动处理 tool 调用 + 结果回传 + 状态管理 + type safety，解放手写 loop。

## 关键属性

- **可用 SDK**：beta in Python / TypeScript / Ruby [[tool-runner--at]] [[Anthropic-SDK-Python]] [[Anthropic-SDK-TypeScript]]
- **何时用**：大多 tool-use 实现；**手动 loop 仅在 human-in-the-loop / 自定义 logging / 条件执行 时用** [[tool-runner--at]]
- **自动**：执行 tool、request/response cycle、conversation state、type safety + validation [[tool-runner--at]]
- **支持自动 [[Compaction]]**：超 token threshold 自动总结，长跑 agent 突破 [[Context-window]] [[tool-runner--at]]
- **Tool 定义**：
  - Python：`@beta_tool` decorator（`@beta_async_tool` for async client）—— 从函数 args + docstring 提 JSON schema；type hints → param type；docstring → desc；Args section → per-param desc；自动 `additionalProperties: false`
  - TS：两路 —— `betaZodTool({name, description, inputSchema: z.object({...}), run: async (input) => ...})`（推荐，Zod 3.25.0+，runtime validation）或 `betaTool()`（无 runtime validation，自己 validate inside `run`）
  - Ruby：subclass `Anthropic::BaseTool` + `doc` + `input_schema` [[tool-runner--at]]
- **Tool 返回**：必须 content block 或 array（text / image / document）；string 自动转 text block；JSON 编码成 string；数字/bool 必须 stringify [[tool-runner--at]]
- **Iterating**：runner 可迭代，yield Claude 消息；每轮 check tool use、跑 tool、回结果、yield next；Claude 不再调 tool 自动结束；可 `break` 早停 [[tool-runner--at]]
- **Final-message-only**：Python `runner.until_done()` / TS `await runner` / Ruby `runner.run_until_finished` [[tool-runner--at]]
- **Advanced controls**：
  - `generate_tool_call_response()` / `generateToolResponse()`：检查 auto-appended 结果用于 logging
  - `set_messages_params(...)` / `setMessagesParams(...)`：定制下一 API call params (e.g., bump max_tokens)
  - `append_messages(...)` / `pushMessages(...)`：注入额外消息
  - Ruby：`next_message` / `feed_messages` / `params` [[tool-runner--at]]
- **Debugging**：tool exception 自动捕获 → `tool_result` is_error: true（默认仅 message）；`ANTHROPIC_LOG=info|debug` 全 stack trace [[tool-runner--at]]
- **拦截 errors**：iterate runner 检 `tool_response.content.is_error` → raise 中断 或 log 继续 [[tool-runner--at]]
- **修改 tool 结果**：常用于加 `cache_control: {"type": "ephemeral"}` 启用 [[Prompt-caching]] 大 tool output；Python re-append `runner.append_messages(message, tool_response)` 防 auto-append；TS in-place mutate；Ruby `runner.params[:messages].last` 改 [[tool-runner--at]]
- **Streaming**：`stream=true` 返回 stream object per iteration；用 [[Streaming-API]] event types；Ruby `runner.each_streaming` + case match [[tool-runner--at]]
- **Code 量对比**：手动 ~30 行 vs runner ~15 行 [[tool-runner--at]]

## 出现来源

_11 summaries reference this entity_ ——
- [[tool-runner--at]] / [[tool-use-overview--at]] / [[tool-reference--at]]
- [[helpers--anthropic-sdk-py]] / [[README--anthropic-sdk-py]] / [[README--anthropic-sdk-ts]]
- [[handle-tool-calls--at]] / [[parallel-tool-use--at]]

## 相关

- [[Tool-use]] / [[Agent-SDK]]（Agent SDK 是更高层 vs Tool-runner 是 raw SDK 的便利包装）
- [[Anthropic-SDK-Python]] / [[Anthropic-SDK-TypeScript]] —— host
- [[Compaction]] / [[Prompt-caching]] / [[Streaming-API]] —— 集成 features
