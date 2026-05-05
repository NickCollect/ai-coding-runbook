---
type: entity
name: Streaming-API
aliases: [streaming / SSE streaming / stream events / message streaming]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

Messages API 的 SSE 流式模式（`stream: true`），按 event 增量返回 content + thinking + usage。

## 关键属性

- **启用**：Messages create call 加 `stream: true` → response 切换到 Server-Sent Events [[streaming--bwc]]
- **何时必用**：大 `max_tokens` 请求（Opus 4.7 支持 128k 流式 vs 非流式 ~64k 实践上限）；HTTP 超时风险时 SDK 强制 [[streaming--bwc]]
- **Event 序列**：
  1. `message_start`（initial Message metadata，`stop_reason` = null）
  2. `content_block_start`（per block）
  3. `content_block_delta`（`text_delta` / `thinking_delta` / `signature_delta` / `input_json_delta`）
  4. `content_block_stop`（per block）
  5. `message_delta`（final `stop_reason` + `usage` 更新）
  6. `message_stop`
- **SDK helper**：[[Anthropic-SDK-Python]] `with client.messages.stream(...) as s: for text in s.text_stream`，`s.get_final_message()` 累积 [[streaming--bwc]] [[helpers--anthropic-sdk-py]]
- TS SDK：`.stream(...).on("text", cb)`，`await stream.finalMessage()` [[streaming--bwc]] [[README--anthropic-sdk-ts]]
- PHP / Go / Java / C# / Ruby SDK 都暴露 streaming primitives [[streaming--bwc]]
- CLI：`ant messages create --stream --format jsonl`
- **Refusal handling**：streaming 期间可能中途 refuse，需 `stop_reason: refusal` 检查 [[handling-stop-reasons--bwc]] [[handle-streaming-refusals--testing]]
- **Thinking signature**：`thinking_delta` 流完后 `signature_delta` 携带签名（验证用） [[Extended-thinking]]
- **Tool use 流式**：`fine-grained tool streaming` beta 让 tool input 也增量返回（默认 buffered） [[fine-grained-tool-streaming--at]]
- **Beta endpoint**：`/v1/beta/messages/create` 也支持 streaming 同协议 [[messages-create--beta-api]]
- **Session events**：[[Session-API]] 的 `events/stream` endpoint 是 managed agent 的 streaming 等价物（不同协议） [[sessions-events-stream--beta-api]]

## 出现来源

_29 summaries reference this entity_ — 主要：
- [[streaming--bwc]] / [[handling-stop-reasons--bwc]]
- [[create--msg-api]] / [[messages-create--beta-api]]
- [[fine-grained-tool-streaming--at]] / [[handle-streaming-refusals--testing]]
- [[helpers--anthropic-sdk-py]] / [[README--anthropic-sdk-py]] / [[README--anthropic-sdk-ts]]
- [[adaptive-thinking--bwc]] / [[extended-thinking--bwc]]
- [[sessions-events-stream--beta-api]]

## 相关

- [[Messages-API]] —— streaming 是 Messages 的 mode
- [[Extended-thinking]] —— thinking 块通过 `thinking_delta` 流
- [[Tool-use]] —— tool input 默认 buffered，fine-grained 流式可选
- [[Anthropic-SDK-Python]] / [[Anthropic-SDK-TypeScript]] —— SDK helpers
- [[Session-API]] —— managed agent 的 events stream（不同协议）
