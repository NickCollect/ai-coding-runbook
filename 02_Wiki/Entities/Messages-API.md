---
type: entity
name: Messages-API
aliases: [messages / messages.create / Messages endpoint / /v1/messages]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

Anthropic 主要的 chat completion REST endpoint —— `POST /v1/messages`，所有 Claude 模型对话能力的入口。

## 关键属性

- **Endpoint**：`POST https://api.anthropic.com/v1/messages` [[create--msg-api]] [[working-with-messages--bwc]]
- **Required headers**：`x-api-key`、`anthropic-version: 2023-06-01`、`content-type: application/json` [[working-with-messages--bwc]]
- **Required body**：`model`、`max_tokens`、`messages: [{role: "user"|"assistant", content}]` [[working-with-messages--bwc]] [[create--msg-api]]
- **Stateless**：每次请求需要发送完整对话历史；synthetic assistant message 合法 [[working-with-messages--bwc]]
- **Response**：`{id, type, role, content[], model, stop_reason, stop_sequence, usage: {input_tokens, output_tokens, cache_creation_input_tokens, cache_read_input_tokens}}` [[working-with-messages--bwc]]
- **Stop reasons**：`end_turn` / `max_tokens` / `stop_sequence` / `tool_use` / `pause_turn` / `refusal` 等 [[handling-stop-reasons--bwc]]
- **Tool use 集成**：`tools[]` + `tool_choice` + 响应中 `tool_use` block + 下一轮 `tool_result` [[Tool-use]] [[create--msg-api]]
- **Vision / PDF / Files**：`content` 支持 `image` / `document` block，三种 source（base64 / url / file_id） [[Vision]] [[PDF-support]] [[Files-API]]
- **Streaming**：`stream: true` 切到 SSE 模式（详见 [[Streaming-API]]） [[streaming--bwc]]
- **Extended thinking**：`thinking: {type, budget_tokens}` 启用思考模式（Opus 4.7 起强制 adaptive） [[Extended-thinking]]
- **Prompt caching**：`cache_control: {type: "ephemeral"}` 复用 prompt 前缀（5m / 1h 两档） [[Prompt-caching]]
- **Adaptive thinking** + **Effort**：`thinking: {type: "adaptive"}` + `effort: low|medium|high` 自动调思考 budget [[Adaptive-thinking]] [[Effort]]
- **Compaction** + **Context editing**：长 context 自动压缩 / 主动编辑 [[Compaction]] [[Context-editing]]
- **Citations**：`citations.enabled: true` on document blocks，response 自动 attach `citations[]` [[Citations-API]]
- **Structured outputs**：`output_config.format` 强制 JSON schema（与 citations 互斥） [[Structured-outputs]]
- **Server tools**：内置 `code_execution` / `web_search` / `web_fetch` / `memory` / `text_editor` / `bash` 等（Anthropic-managed） [[Code-execution-tool]] [[Web-search-tool]] [[Web-fetch-tool]] [[Memory-tool]] [[Text-editor-tool]] [[Bash-tool-API]]
- **Async batch**：`POST /v1/messages/batches`（50% 价格） [[Batches-API]]
- **Token 预估**：`POST /v1/messages/count_tokens` [[Token-counting]]
- **Beta endpoint**：`POST /v1/beta/messages/create` 同 schema 加 beta features [[messages-create--beta-api]]
- **跨平台**：直 API、Bedrock、Vertex AI、Foundry 同 schema（详见 [[Enterprise-gateway]]）

## 出现来源

_62 summaries reference this entity_ — 主要：

- [[create--msg-api]] / [[messages--api-index]]
- [[messages-create--beta-api]] / [[messages-index--beta-api]]
- [[working-with-messages--bwc]] / [[overview--bwc]]
- [[get-started--platform]] / [[intro--platform]]
- [[batch-processing--bwc]] / [[streaming--bwc]] / [[vision--bwc]] / [[pdf-support--bwc]] / [[citations--bwc]]
- [[extended-thinking--bwc]] / [[prompt-caching--bwc]] / [[adaptive-thinking--bwc]] / [[effort--bwc]]
- [[structured-outputs--bwc]] / [[token-counting--bwc]] / [[handling-stop-reasons--bwc]]
- [[compaction--bwc]] / [[context-editing--bwc]] / [[search-results--bwc]] / [[fast-mode--bwc]]
- [[task-budgets--bwc]] / [[multilingual-support--bwc]] / [[api-and-data-retention--bwc]]
- [[claude-in-amazon-bedrock--bwc]] / [[claude-on-vertex-ai--bwc]] / [[claude-in-microsoft-foundry--bwc]]
- [[tool-use-overview--at]] / [[handle-tool-calls--at]] / [[define-tools--at]] / [[parallel-tool-use--at]]
- [[fine-grained-tool-streaming--at]] / [[programmatic-tool-calling--at]] / [[strict-tool-use--at]]
- [[README--anthropic-sdk-py]] / [[api--anthropic-sdk-py]] / [[helpers--anthropic-sdk-py]]
- 等

## 相关

- [[Streaming-API]] —— SSE 增量返回
- [[Batches-API]] —— 异步批量
- [[Token-counting]] —— pre-flight token 估算
- [[Tool-use]] —— tools array + tool_use/tool_result block
- [[Extended-thinking]] / [[Prompt-caching]] / [[Adaptive-thinking]] / [[Effort]] / [[Compaction]] / [[Context-editing]] / [[Citations-API]] / [[Structured-outputs]] / [[Vision]] / [[PDF-support]] / [[Files-API]] / [[Search-results]] —— 所有围绕 Messages 的 feature
- [[Anthropic-SDK-Python]] / [[Anthropic-SDK-TypeScript]] —— 官方 client SDK
- [[Managed-agent]] —— 高层 agent harness（与 Messages 平行的两条产品线）
- [[Enterprise-gateway]] —— Bedrock/Vertex/Foundry deployment
- [[Completions-API]] —— legacy text completions（建议迁移到 Messages）
