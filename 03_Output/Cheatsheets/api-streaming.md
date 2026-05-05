---
type: cheatsheet
topic: api-streaming
updated: 2026-05-05
---

# API Streaming Quick Reference

---

## 协议层对比

| | Claude | OpenAI (Responses API) | Gemini |
|---|---|---|---|
| **协议** | SSE | SSE | SSE (`?alt=sse`) |
| **流结束标志** | `message_stop` 事件 | `data: [DONE]` | 连接关闭 / `finish_reason` 非空 |
| **事件模型** | 6 种具名阶段事件 | 20+ 种点分层级事件 | 无命名事件，每 chunk 是完整 Response 增量 |
| **启用方式** | `"stream": True` | `stream=True` | `generate_content_stream()` |

---

## 事件类型

### Claude 事件序列

```
message_start          → 含 id、model、usage(input_tokens only)
  content_block_start  → index + block type (text/thinking/tool_use/...)
    content_block_delta → delta.type: text_delta | thinking_delta | input_json_delta | ...
    content_block_delta ...
  content_block_stop   → index
  content_block_start  → index+1 ...
message_delta          → stop_reason, stop_sequence, 累计 usage(output_tokens 在这里)
message_stop           → 无额外字段
```

### OpenAI 关键事件（Responses API）

| 事件 | 说明 |
|---|---|
| `response.created` | 响应对象创建 |
| `response.output_text.delta` | **文本增量**（主要消费事件） |
| `response.output_text.done` | 文本块完成 |
| `response.function_call_arguments.delta` | Tool call 参数增量 |
| `response.function_call_arguments.done` | Tool call 参数完整 |
| `response.completed` | 整个响应完成，含完整 usage |
| `response.failed` | 失败 |

### Gemini 事件（扁平 chunk）

无命名事件类型；每个 chunk 是完整 `GenerateContentResponse` 片段：
```python
chunk.text                              # 文本增量
chunk.candidates[0].finish_reason      # 非空 = 流结束
chunk.usage_metadata                   # 仅最后一个 chunk 有
```

---

## Usage 数据位置

| | Claude | OpenAI | Gemini |
|---|---|---|---|
| **input tokens** | `message_start.usage.input_tokens` | `response.completed` 事件 | 最后一个 chunk 的 `usage_metadata` |
| **output tokens** | `message_delta.usage.output_tokens` | `response.completed` 事件 | 最后一个 chunk 的 `usage_metadata` |
| **cached tokens** | `message_start.usage.cache_read_input_tokens` | `response.completed` → `prompt_tokens_details.cached_tokens` | 最后一个 chunk 的 `usage_metadata.cached_content_token_count` |

---

## Tool Call Streaming

| | Claude | OpenAI | Gemini |
|---|---|---|---|
| **开始信号** | `content_block_start` (type=`tool_use`) | `response.output_item.added` | chunk 中 `parts[n].function_call` 出现 |
| **参数增量** | `content_block_delta` (type=`input_json_delta`) | `response.function_call_arguments.delta` | not documented in source |
| **完成信号** | `content_block_stop` | `response.function_call_arguments.done` | `finish_reason` 非空 |
| **参数累积** | 需手动拼接 `partial_json` 片段 | 需手动累积，`done` 后 parse | SDK 自动聚合 |
| **Fine-grained mode** | ✅ `eager_input_streaming: true`（beta，参数未验证完即推送） | ❌ | ❌ |

---

## SDK Helper 模式（Python）

### Claude

```python
# 同步流式 — .text_stream 自动过滤只返回文本
with client.messages.stream(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

final_msg = stream.get_final_message()  # 自动累积，含完整 usage
print(final_msg.usage.output_tokens)

# 异步
async with client.messages.stream(...) as stream:
    async for text in stream.text_stream:
        print(text, end="", flush=True)
```

> 思考块 (thinking) 和 tool use 块需监听原始事件：`event.type == "content_block_start"`

### OpenAI

```python
# Responses API
response = client.responses.create(
    model="gpt-5.5",
    input="Tell me a story",
    stream=True,
)
for event in response:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)

# Agents SDK 流式
from agents import Runner
from openai.types.responses import ResponseTextDeltaEvent

stream = Runner.run_streamed(agent, "Explain Saturn.")
async for event in stream.stream_events():
    if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
        print(event.data.delta, end="", flush=True)
```

### Gemini

```python
response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents=["Explain how AI works"]
)
for chunk in response:
    print(chunk.text, end="")
# 流结束后 response.text 可用（SDK 自动聚合）
```

---

## Common Gotchas

1. **Claude `stop_reason` 流式模式下延迟**
   `message_start` 时 `stop_reason` 为 null；直到 `message_delta` 事件才填充。不要在 `message_start` 读 stop_reason。

2. **OpenAI Responses API vs Chat Completions API 事件格式不同**
   旧版 Chat Completions 用 `choices[0].delta`；新版 Responses API 用 `response.output_text.delta`。混用会出错。

3. **Gemini usage 只在最后一个 chunk**
   中间 chunk 的 `usage_metadata` 为空或不准确，只取最后一个 chunk 的值。

4. **Claude fine-grained tool streaming 可能返回不完整 JSON**
   `eager_input_streaming: true` 时若遭遇 `max_tokens` 截断，调用方会收到不完整 JSON，需自行处理解析错误。

5. **流式输出内容审核有延迟**（OpenAI）
   流式输出无法在显示前做完整内容过滤，建议对最终输出再跑一次 moderation，或实时监控 delta。
   Claude `stop_reason == "refusal"` 表示 streaming classifier 介入。

6. **Gemini function calling 流式增量行为未充分文档化**
   当前官方 raw 文档未详细说明 tool call streaming 的增量事件格式，生产使用前建议实测。
