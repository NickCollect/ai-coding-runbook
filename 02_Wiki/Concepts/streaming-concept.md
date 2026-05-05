---
name: Streaming
type: concept
aliases: [Token Streaming, Server-Sent Events, SSE Streaming, Incremental Output]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Streaming（流式输出）

LLM 在生成完整回答之前，逐步向客户端发送 token 的传输模式，使用户无需等待全部生成完毕即可开始阅读，显著改善感知延迟（TTFT — Time to First Token）。

## 核心机制

LLM 的生成是自回归的（逐 token 串行），而非一次性生成完整输出。Streaming 利用这一特性，通过 **Server-Sent Events（SSE）** 协议将每个 token（或若干 token 的 delta）实时推送给客户端。

**事件序列（以 Claude 为例）**：
```
message_start → content_block_start → content_block_delta* → content_block_stop → message_delta → message_stop
```

- `content_block_delta`：主体数据事件，包含 `text_delta`（文本）、`thinking_delta`（推理）、`input_json_delta`（工具调用参数）
- `message_delta`：携带最终 `stop_reason` 和用量统计

**为什么需要 streaming**：
1. **UX 感知延迟**：用户在首个 token 到达时即可开始阅读，体感比等待全量输出快得多
2. **大 max_tokens 防超时**：非流式请求在大输出时会因 HTTP 连接超时而失败；SDK 通常强制大 max_tokens 请求走流式

## 跨厂商实现

**Claude**：`stream: true` 参数启用；SDK 提供高级 helper（Python: `with client.messages.stream(...) as stream: for text in stream.text_stream`；TS: `.stream(...).on("text", cb)`）；Extended Thinking 的 `thinking_delta` 也通过 SSE 流式传输。

**OpenAI**：`stream: true`；Chat Completions 和 Responses API 均支持；推理模型的内部 CoT 不流式暴露。

**Gemini**：`generateContentStream()` 方法；Live API（Gemini 2.0）支持双向实时音频/视频流，超越文本 SSE 范式。

## 关键参数 / API 表面

| 参数/方法 | 说明 |
|---|---|
| `stream: true` | 启用 SSE 流式模式 |
| `text_stream` (Python SDK) | 仅文本的异步迭代器 |
| `get_final_message()` | 累积 stream 为完整 Message 对象 |
| `content_block_delta.type` | `text_delta` / `thinking_delta` / `input_json_delta` / `signature_delta` |

## 使用场景

**应该用 streaming**：
- 所有面向用户的交互（chatbot、copilot）
- `max_tokens` > ~32k 的请求（避免 HTTP 超时）
- 需要部分结果早期可用（如流式代码执行）

**不需要 streaming**：
- 批量处理（后台任务，延迟不敏感）→ 用 [[batch-processing-concept]]
- 只需最终结果的自动化 pipeline（延迟不重要）

**注意**：流式模式中 `usage` 统计通常在 `message_delta` 事件中才出现，不是第一个事件。

## 相关

- [[Streaming-API]] — Claude 流式 API entity 档案
- [[batch-processing-concept]] — 流式的对立选择：延迟换吞吐
- [[extended-thinking-concept]] — 推理模式的 thinking delta 通过 stream 传输

## 出现来源

- [[streaming--bwc]]
- [[events-and-streaming--ma]]
- [[streaming-responses--openai-docs]]
