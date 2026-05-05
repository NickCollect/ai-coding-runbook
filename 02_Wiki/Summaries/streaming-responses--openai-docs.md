---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/streaming-responses.md
source_url: https://platform.openai.com/docs/guides/streaming-responses
title: "OpenAI — 流式响应（Streaming）"
summarized_at: 2026-05-05
entities_referenced: [Streaming-API]
concepts_referenced: []
---

## 核心要点

Streaming 允许客户端在模型生成完整响应之前就开始接收并处理输出，显著降低感知延迟。

### 启用方式

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

底层使用 **Server-Sent Events（SSE）**，每条事件以 `data:` 开头，`data: [DONE]` 标记流结束。

### 关键事件类型

| 事件 | 说明 |
|---|---|
| `response.created` | 响应对象创建 |
| `response.output_text.delta` | 文本增量 |
| `response.output_text.done` | 单个文本 item 完成 |
| `response.completed` | 完整响应结束 |
| `response.failed` | 响应失败 |

完整事件分类：lifecycle events、output events、error events、rate limit events。

### 高级用例

- **流式 function call**：`response.function_call_arguments.delta` 事件逐步输出 arguments JSON
- **流式 Structured Output**：在 `response.output_text.delta` 中逐步构建 JSON，需客户端累积后解析
- **流式图像生成**：`response.image_generation_call.partial_image` 事件发送 base64 编码的 partial image

### 内容审核风险

- 流式输出无法在显示前做完整内容过滤
- 建议对最终完整输出再跑一次 moderation，或实时监控 delta 事件
- 流式渲染 Markdown 可能产生视觉跳动（XSS 风险也需注意）
