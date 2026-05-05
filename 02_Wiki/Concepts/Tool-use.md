---
type: concept
name: Tool-use
aliases: [function calling, tool calling]
category: concept
status: ga
created: 2026-05-05
note: cross-product entity (referenced by P1 summaries; full enrichment in P2 with API docs)
---

## 一句话定义

Claude 通过结构化输出调用外部工具的协议（Anthropic 称 tool use，业界叫 function calling）

## 关键属性

- 工具定义结构：`name` + `description` + `input_schema`（JSON Schema）；最佳实践用描述性 name（`get_weather`、`search_database`），写详细描述（Claude 用它选工具），每个 property 都加 description，固定值用 `enum`，`required` 只列真正必填 [[tool-use-concepts]]
- `tool_choice` 四种：`{"type":"auto"}`（默认，Claude 自决）、`{"type":"any"}`（必须用至少一个）、`{"type":"tool","name":"..."}`（强制用指定）、`{"type":"none"}`（禁用） [[tool-use-concepts]]
- 默认允许并行 tool calls；加 `"disable_parallel_tool_use": true` 强制单 turn 最多一个 tool call [[tool-use-concepts]]
- Tool Runner（推荐）：SDK 自动跑 agentic loop——调 API、解析 tool_use、执行 handler、回填 result、循环；Python / TS / Java / Go / Ruby / PHP SDK 都支持（beta）；schemas 由函数签名自动生成 [[tool-use-concepts]] [[tool-use--python]] [[tool-use--typescript]]
- Python 用 `@beta_tool` 装饰 typed function 喂给 `client.beta.messages.tool_runner()`；async 走 `@beta_async_tool` + `async def`；`tool_runner` 本身是 sync（返回 runner，非 coroutine） [[tool-use--python]]
- TypeScript 用 `betaZodTool` + Zod schema + `run` async function 喂给 `client.beta.messages.toolRunner()`；handler 入参由 Zod 自动类型推导 [[tool-use--typescript]]
- 手写 manual loop（细粒度控制 / 自定义日志 / 人工审批）：循环到 `stop_reason === "end_turn"`；总要 append 完整 `response.content` 保留 `tool_use` blocks；每个 `tool_result` 必须带匹配 `tool_use_id` [[tool-use-concepts]] [[tool-use--typescript]]
- Server-side tools（code execution / web search 等）跑在 server-side sampling loop，默认 10 iterations；命中上限返回 `stop_reason: "pause_turn"`，重发"用户原 message + 助手响应"即续跑（**不要**追加 "Continue." user message） [[tool-use-concepts]]
- MCP 工具集成：Python `pip install anthropic[mcp]` + `async_mcp_tool(t, mcp_client)` 把 MCP tools 转成 Anthropic 类型喂 tool runner；用于 local MCP server / prompts / resources / 精细控制 MCP 连接 [[tool-use--python]] [[tool-use-concepts]]
- Agent SDK 的 in-process MCP server 用 `tool()` 定义自定义工具：TS `tool(name, description, zodSchema, handler, {annotations?})`，Python `@tool(name, description, schema, annotations=...)`；handler 返回 `content` 数组 + 可选 `isError` [[custom-tools--agent-sdk]]
- Tool annotations（metadata，非强制）：`readOnlyHint`（默认 false，让 Claude 把 read-only 工具批量并行）、`destructiveHint`（默认 true）、`idempotentHint`、`openWorldHint` [[custom-tools--agent-sdk]]
- 自定义 tool 通过 `createSdkMcpServer` (TS) / `create_sdk_mcp_server` (Python) 打包；fully qualified name = `mcp__{server_name}__{tool_name}`；用 wildcard `mcp__weather__*` 在 `allowedTools` 一次放行 [[custom-tools--agent-sdk]]
- Anthropic 把 "tool use" 与业界 "function calling" 视为同义术语，部分 docs 混用 [[custom-tools--agent-sdk]]
- Tool 数量过多时每 turn 都会消耗 context——超过约几十个时改用 Tool Search 按需加载 [[custom-tools--agent-sdk]]
- **API server-managed tools**（在 Anthropic 端跑，不需 client 实现）：[[Code-execution-tool]] / [[Web-search-tool]] / [[Web-fetch-tool]] / [[Memory-tool]] / [[Text-editor-tool]] / [[Bash-tool-API]] / [[Computer-use-tool-API]] / [[Tool-search-tool-API]] / [[Advisor-tool]]；与 client-side tool 用法一致，但执行在 server side，部分支持 dynamic filtering [[tool-use-overview--at]] [[server-tools--at]]
- **Client-side tools**（你 app 实现执行）：custom tools + 部分 schema-defined（如 [[Bash-tool-API]] / [[Text-editor-tool]] 既可作为 server-managed 内置 [[Code-execution-tool]] 的 sub-tool，也可作为独立 client-side tool） [[bash-tool--at]] [[text-editor-tool--at]]
- **[[Tool-runner]] SDK 抽象**：自动处理 agentic loop + 错误 + type safety + auto compaction；Python `@beta_tool` / TS `betaZodTool` / Ruby `BaseTool` subclass [[tool-runner--at]]
- **`strict: true`** + **[[Structured-outputs]]** = grammar 强制 tool input schema 验证 [[strict-tool-use--at]]
- **Parallel tool calls** + `disable_parallel_tool_use` 控制并行 [[parallel-tool-use--at]]
- **Programmatic tool calling**：Claude 通过 [[Code-execution-tool]] 用 Python 程序式调 tool（不直接 emit `tool_use`） [[programmatic-tool-calling--at]]
- **Fine-grained tool streaming**：tool input 也增量流（默认 buffered） [[fine-grained-tool-streaming--at]]
- **Build-a-tool-using agent** 教程：完整 e2e 示例 [[build-a-tool-using-agent--at]]


## 出现来源

_18 summaries reference this entity_:

- [[agent-design]]
- [[claude-api--csharp]]
- [[claude-api-go]]
- [[claude-api-php]]
- [[claude-api-ruby]]
- [[claude-api-skill]]
- [[custom-tools--agent-sdk]]
- [[examples--curl]]
- [[managed-agents-tools]]
- [[mcp--agent-sdk]]
- [[overview--agent-sdk]]
- [[streaming--python]]
- [[streaming--typescript]]
- [[tool-search--agent-sdk]]
- [[tool-use--python]]
- [[tool-use--typescript]]
- [[tool-use-concepts]]
- [[typescript--agent-sdk]]

## 相关

- [[Agentic-loop]] — tool use 是 agentic loop 的核心机制：每次 Claude emit `tool_use`，外部 runtime 执行后回填 `tool_result`，直到 `end_turn`
- [[MCP-server]] — MCP 是 tool use 的协议级扩展：MCP server 暴露的 tools / prompts / resources 转换后喂给 tool runner
- [[Agent-SDK]] — Agent SDK 把 in-process MCP server + custom tools + built-in tools 统一为同一套 `mcp__server__tool` 命名空间
- [[Prompt-caching]] — tools 在 prompt 渲染顺序最前；改 tools 集会让全部 cache 失效，所以 tool 集应稳定 + 序列化时 sort by name
- [[Context-window]] — 每个工具定义每 turn 都消耗 context，工具多时用 Tool Search 按需加载
