---
name: Streaming API 跨厂商对比
type: comparison
created: 2026-05-05
vendors: [Claude, OpenAI, Gemini]
sources:
  - 01_Raw/platform.claude.com/docs/en/api/messages.md
  - 01_Raw/docs.openai.com/docs/guides/streaming-responses.md
  - 01_Raw/ai.google.dev/gemini-api/docs/text-generation.md
  - 01_Raw/github/anthropics/skills/skills/claude-api/python/claude-api/streaming.md
  - 01_Raw/github/anthropics/skills/skills/claude-api/typescript/claude-api/streaming.md
---

# Streaming API 跨厂商对比

三大 LLM 厂商（Claude / OpenAI / Gemini）的 streaming 机制横向对比。

---

## 一、协议层：Server-Sent Events（SSE）

三家均基于 **SSE**（Server-Sent Events）传输流式响应，HTTP 连接持续开放，服务端逐块推送 `data:` 行。

| 厂商 | 底层协议 | 流结束标志 |
|------|---------|-----------|
| **Claude** | SSE，每事件一行 `data: {...}` | `message_stop` 事件 |
| **OpenAI** | SSE，每事件一行 `data: {...}` | `data: [DONE]` |
| **Gemini** | SSE（REST endpoint: `?alt=sse`）| 连接关闭 |

**Claude** 用具名事件类型区分不同阶段；**OpenAI** 用点分层级事件名（如 `response.output_text.delta`）；**Gemini** 每个 chunk 是完整 `GenerateContentResponse` 的增量，结构较扁平。

---

## 二、Claude 事件模型（详细）

来源：`01_Raw/platform.claude.com/docs/en/api/messages.md`（`stream: true` 时触发）

启用方式：请求体加 `"stream": true`。

### 事件序列

```
message_start
  → content_block_start (index=0, type=text|thinking|tool_use|...)
    → content_block_delta (index=0, delta.type=text_delta|thinking_delta|input_json_delta|...)
    → content_block_delta ...
  → content_block_stop (index=0)
  → content_block_start (index=1, ...)
    → ...
  → content_block_stop (index=1)
message_delta (stop_reason, stop_sequence, 累计 usage)
message_stop
```

### 各事件携带内容

| 事件 | 携带内容 |
|------|---------|
| `message_start` | 完整 `Message` 对象（空 content）；含 `id`、`model`、`usage`（此时 usage 仅有 input_tokens，output_tokens=0） |
| `content_block_start` | `index`（内容块索引）+ `content_block`（TextBlock / ThinkingBlock / ToolUseBlock 等，此时为空壳） |
| `content_block_delta` | `index` + `delta`（`text_delta` / `thinking_delta` / `signature_delta` / `citations_delta` / `input_json_delta`） |
| `content_block_stop` | `index`（该块流完） |
| `message_delta` | `delta`（含 `stop_reason`、`stop_sequence`、`stop_details`）+ 累计 `usage`（output_tokens 在此处） |
| `message_stop` | 仅含 `type: "message_stop"`，无其他字段 |

**重要**：`stop_reason` 在非流式模式始终非 null；流式模式中 `message_start` 时为 null，`message_delta` 时才填充。

---

## 三、OpenAI 事件模型（详细）

来源：`01_Raw/docs.openai.com/docs/guides/streaming-responses.md`

启用方式：`stream=True`（Python）。底层 SSE，每条以 `data:` 前缀，流结束为 `data: [DONE]`。

### 完整事件分类（Responses API）

**Lifecycle events**
- `response.created` — 响应对象创建（一次）
- `response.in_progress` — 响应处理中
- `response.completed` — 完整响应结束（一次）
- `response.failed` — 失败

**Output events**
- `response.output_item.added` / `response.output_item.done`
- `response.content_part.added` / `response.content_part.done`
- `response.output_text.delta` — 文本增量（**主要消费事件**）
- `response.output_text.annotation.added` — 注释
- `response.output_text.done`
- `response.refusal.delta` / `response.refusal.done`
- `response.function_call_arguments.delta` — 函数调用参数增量
- `response.function_call_arguments.done`
- `response.file_search_call.in_progress` / `.searching` / `.completed`
- `response.code_interpreter.in_progress` / `.call_code.delta` / `.call_code.done` / `.interpreting` / `.completed`

**注意**：OpenAI 的 Responses API 与旧版 Chat Completions API 事件格式不同，旧版用 `choices[0].delta`。

---

## 四、Gemini 事件模型（详细）

来源：`01_Raw/ai.google.dev/gemini-api/docs/text-generation.md`

启用方式：Python 用 `generate_content_stream()`；REST 用 `:streamGenerateContent?alt=sse`。

### Chunk 结构

Gemini streaming 的每个 chunk 是完整 `GenerateContentResponse` 对象的增量片段：

```python
for chunk in response:
    print(chunk.text, end="")
    # chunk.candidates[0].content.parts[0].text
    # chunk.candidates[0].finish_reason  # 最后一个 chunk 才有
    # chunk.usage_metadata  # 最后一个 chunk 才有
```

Gemini **没有命名事件类型**；每个 chunk 自带 `candidates[0].content.parts` 结构，通过 `finish_reason` 是否非空判断流是否结束。

---

## 五、Tool Call 流式行为对比

### Claude：Tool Use Streaming

来源：`01_Raw/github/anthropics/skills/skills/claude-api/python/claude-api/streaming.md`

- `content_block_start` 时 `content_block.type == "tool_use"`，携带 `id` 和 `name`（input 为空）
- `content_block_delta` 时 `delta.type == "input_json_delta"`，逐步发送 input JSON 片段（不保证完整 JSON，需累积）
- `content_block_stop` 后 input 完整，可执行工具
- **Fine-grained tool streaming**（beta）：通过 `eager_input_streaming: true` 在参数仍在生成时就开始流式推送，类型按飞行推断

Python SDK 的 tool runner 当前返回完整消息；需要 per-token streaming + tools 的场景须手动 loop。

### OpenAI：Function Call Streaming

来源：`01_Raw/docs.openai.com/docs/guides/streaming-responses.md`

- `response.function_call_arguments.delta` 事件逐步输出 arguments JSON
- `response.function_call_arguments.done` 时 arguments 完整

### Gemini：Function Call Streaming

Gemini function calling 的流式行为在当前 raw 文档中 **未单独记录**。`text-generation.md` 仅展示了文本 streaming 示例。工具调用在 chunk 结构中出现为 `parts[n].function_call`，但流式增量行为的详细规范在当前 raw 中未找到。

---

## 六、SDK Helper 模式

### Claude — Python SDK

来源：`01_Raw/github/anthropics/skills/skills/claude-api/python/claude-api/streaming.md`

```python
# 同步
with client.messages.stream(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

# 获取完整消息（含 usage）
final_msg = stream.get_final_message()
print(final_msg.usage.output_tokens)

# 异步
async with client.messages.stream(...) as stream:
    async for text in stream.text_stream:
        print(text, end="", flush=True)
```

`.text_stream` 自动过滤只返回文本增量；思考块（thinking）和 tool use 块需监听 `event.type == "content_block_start"` 等原始事件。

### Claude — TypeScript SDK

来源：`01_Raw/github/anthropics/skills/skills/claude-api/typescript/claude-api/streaming.md`

```typescript
const stream = client.messages.stream({
  model: "claude-opus-4-7",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello" }]
});

for await (const event of stream) {
  if (event.type === "content_block_delta" &&
      event.delta.type === "text_delta") {
    process.stdout.write(event.delta.text);
  }
}
```

Tool use streaming 需搭配 `betaZodTool` helper + outer loop over tool runner iterations。

### OpenAI — Python SDK

来源：`01_Raw/docs.openai.com/docs/guides/streaming-responses.md`

```python
response = client.responses.create(
    model="gpt-5.5",
    input="Tell me a story",
    stream=True,
)

for event in response:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
```

Agents SDK 流式：

```python
from agents import Agent, Runner
from openai.types.responses import ResponseTextDeltaEvent

stream = Runner.run_streamed(agent, "Give me three short facts about Saturn.")
async for event in stream.stream_events():
    if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
        print(event.data.delta, end="", flush=True)
```

来源：`01_Raw/docs.openai.com/docs/guides/agents/running-agents.md`

### Gemini — Python SDK

来源：`01_Raw/ai.google.dev/gemini-api/docs/text-generation.md`

```python
from google import genai

client = genai.Client()

response = client.models.generate_content_stream(
    model="gemini-3-flash-preview",
    contents=["Explain how AI works"]
)
for chunk in response:
    print(chunk.text, end="")
```

JavaScript：

```javascript
const response = await ai.models.generateContentStream({
  model: "gemini-3-flash-preview",
  contents: "Explain how AI works",
});
for await (const chunk of response) {
  console.log(chunk.text);
}
```

---

## 七、横向对比表

| 维度 | Claude | OpenAI (Responses API) | Gemini |
|------|--------|----------------------|--------|
| **事件模型** | 具名阶段事件（6种 raw event types） | 点分层级命名事件（20+种） | 无命名事件，每块为完整 Response 增量 |
| **Tool call streaming** | `input_json_delta` 增量 JSON；fine-grained beta | `function_call_arguments.delta` 逐步输出 | 当前 raw 未详细记录增量行为 |
| **Usage 报告位置** | `message_delta` 事件（流末尾） | `response.completed` 事件 | 最后一个 chunk 的 `usage_metadata` |
| **流结束标志** | `message_stop` 事件 | `data: [DONE]` | 连接关闭 / `finish_reason` 非空 |
| **SDK `.stream()` helper** | Python: `client.messages.stream()` + `.text_stream`；TS: 同名方法 | Python: `stream=True` 参数；Agents: `Runner.run_streamed()` | `generate_content_stream()` |
| **累积方式** | `get_final_message()` 自动累积 | 手动累积 delta 或等 `response.completed` | SDK 自动聚合，`response.text` 在流后可用 |
| **思考块 streaming** | `thinking_delta` / `signature_delta` | 不适用（reasoning 不暴露 tokens） | `thinkingConfig` 控制，thinking tokens 不在流中直接暴露 |

---

## 八、内容审核注意事项

**OpenAI**（来源：`01_Raw/docs.openai.com/docs/guides/streaming-responses.md`）：流式输出无法在显示前做完整内容过滤，建议对最终输出再跑一次 moderation，或实时监控 delta 事件。Markdown 流式渲染也存在视觉跳动和 XSS 风险。

**Claude**：`stop_reason == "refusal"` 表示 streaming classifier 介入（来源：`01_Raw/platform.claude.com/docs/en/api/messages.md`，stop_reason 包含 `"refusal"` 值）。

**Gemini**：safety_ratings 在最后一个 chunk 的 `candidates[0]` 中出现，流式渲染中间状态不保证安全评级完整。
