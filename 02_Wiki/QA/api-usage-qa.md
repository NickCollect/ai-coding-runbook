---
type: qa
topic: api-usage
created: 2026-05-05
sources:
  - 02_Wiki/Comparison/streaming-comparison.md
  - 02_Wiki/Comparison/tool-use-comparison.md
  - 02_Wiki/Comparison/agentic-sdk-comparison.md
  - 02_Wiki/Comparison/context-caching-comparison.md
  - 02_Wiki/Synthesis/structured-output-guide.md
  - 02_Wiki/Synthesis/mcp-integration-guide.md
  - 02_Wiki/Synthesis/prompt-caching-strategy.md
---

# API Usage Q&A

## Q: Claude 和 OpenAI 的 streaming 事件格式有什么不同？
**A:** Claude 使用 **6 种具名阶段事件**（`message_start` → `content_block_start` → `content_block_delta` → `content_block_stop` → `message_delta` → `message_stop`），以 `message_stop` 表示结束。OpenAI Responses API 使用 **20+ 种点分层级事件名**（如 `response.output_text.delta`），以 `data: [DONE]` 结束。Gemini 无命名事件，每个 chunk 是完整 `GenerateContentResponse` 的增量，通过 `finish_reason` 非空判断结束。
*来源：[[streaming-comparison]]*

---

## Q: 怎么在 Claude 里强制 JSON 输出？
**A:** 推荐用 **native structured outputs**：在请求中设置 `output_config.format.type: "json_schema"` 并提供 schema，底层 constrained decoding 硬保证输出符合 schema。注意：同时开启 citations 时不兼容（400 错误）。Legacy 方法：使用 `strict: true` 的 tool use 并强制 `tool_choice` 到该 tool，但不如 native 方式严格。
*来源：[[structured-output-guide]]*

---

## Q: OpenAI Structured Outputs 和 JSON mode 区别？
**A:** **Structured Outputs**（`json_schema` + `strict: true`）：constrained decoding，硬保证输出完全符合 schema，所有字段必须 `required`，`additionalProperties: false`。**JSON mode**（`json_object`）：仅保证合法 JSON，不保证任何 schema 合规，需在 prompt 里明确要求输出 JSON 否则可能有前缀文字。OpenAI 官方建议能用 Structured Outputs 就不用 JSON mode。
*来源：[[structured-output-guide]]*

---

## Q: 并行 tool call 在 Claude 怎么工作？
**A:** Claude 默认启用并行工具调用：单次响应 `content` 数组可包含多个 `tool_use` 块，每个有唯一 `id`。**关键规则**：所有 `tool_result` 块必须合并进**同一条 user 消息**，顺序任意——分成多条 user 消息会导致 Claude 减少后续并行调用频率。禁止并行：在 `tool_choice` 对象里加 `"disable_parallel_tool_use": true`。
*来源：[[tool-use-comparison]]*

---

## Q: Claude 的 cache_control 放在哪里？
**A:** 两种方式：(1) **Automatic 模式**（推荐多轮对话）：在请求 body **顶层**加 `"cache_control": {"type": "ephemeral"}`，系统自动应用断点到最后一个可缓存块。(2) **Explicit 模式**（精细控制）：在具体 content block 上添加 `"cache_control": {"type": "ephemeral"}`，最多允许 4 个断点。缓存覆盖顺序：`tools → system → messages`。
*来源：[[prompt-caching-strategy]]、[[Prompt-caching]]*

---

## Q: Gemini context caching 最少需要多少 token？
**A:** 按模型不同：**Gemini 2.5 Flash**：1,024 tokens；**Gemini 2.5 Pro**：4,096 tokens；**Gemini 3 Flash preview**：1,024 tokens；**Gemini 3 Pro preview**：4,096 tokens。低于门槛时不缓存（implicit 模式静默跳过）。
*来源：[[prompt-caching-strategy]]、[[context-caching-comparison]]*

---

## Q: MCP 的 stdio transport 和 HTTP transport 区别？
**A:** **stdio**：在本地以子进程方式运行，适合需要直接系统访问的工具；不支持自动重连，连接断开需手动重启。**Streamable HTTP**（推荐）：适合远程服务器，支持 SSE 流式传输，自动重连（最多 5 次指数退避）；Claude Code 和 OpenAI Responses API 均支持。旧版 HTTP+SSE 已废弃，新项目用 `--transport http` 而非 `--transport sse`。
*来源：[[mcp-integration-guide]]*

---

## Q: Claude Agent SDK 的 session 是什么？
**A:** Session 将对话历史持久化为 JSONL 文件（非文件系统快照）。使用场景：(1) 继续最近 session：`continue_conversation=True`（Python）/ `continue: true`（TS）；(2) 恢复指定历史 session：`resume=session_id`；(3) 分叉不同路径：`fork` 选项，原 session 不变；(4) 内存模式（TS only）：`persistSession: false`。Subagent 始终启动全新对话，不继承父 session 历史。
*来源：[[agentic-sdk-comparison]]*

---

## Q: OpenAI handoff 和 Claude subagent 对比？
**A:** **OpenAI handoff**：控制权移交给 specialist agent，specialist 完全接管后续对话，适合"多专家接力"场景。**Claude subagent**：父 agent 派发子任务，子 agent 在隔离 context 中完成并返回最终消息，父 agent 始终保持控制权。OpenAI 的 "agents-as-tools" 模式（`agent.as_tool()`）与 Claude subagent 更类似——manager 调用 specialist 但保持控制权。Gemini 无官方 SDK，依赖第三方框架实现多 agent 协作。
*来源：[[agentic-sdk-comparison]]*

---

## Q: 哪个 vendor 的 function calling 支持最严格的 schema 验证？
**A:** **OpenAI** 和 **Claude** 均支持 `strict: true` 硬 schema 验证（constrained decoding）。OpenAI strict 模式额外要求所有字段 `required` 且 `additionalProperties: false`。Claude `strict: true` 同样强制 schema 合规，但允许 optional 字段。**Gemini** 使用 OpenAPI schema 子集，不支持 strict 模式（仅 `mode: VALIDATED` 近似）。综合最严格：OpenAI strict + Claude strict 旗鼓相当；Gemini 弱于前两者。
*来源：[[tool-use-comparison]]、[[structured-output-guide]]*
