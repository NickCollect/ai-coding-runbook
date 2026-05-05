---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/compaction.md
source_url: https://platform.openai.com/docs/guides/compaction
title: "OpenAI — Compaction（上下文压缩）"
summarized_at: 2026-05-05
entities_referenced: [Compaction]
concepts_referenced: [Context-window]
---

## 核心要点

Compaction 在保留后续 turn 所需状态的前提下压缩 context 大小，平衡质量、成本与延迟。

### 两种使用方式

**1. Server-side compaction（自动触发）**

```python
response = client.responses.create(
    model="gpt-5.3-codex",
    input=conversation,
    store=False,
    context_management=[{"type": "compaction", "compact_threshold": 200000}],
)
```

- rendered token 数超过阈值时服务端自动压缩
- 无需单独调用 `/responses/compact`
- 响应流包含加密的 compaction item
- `store=False` 时 ZDR 友好

**延迟优化**：追加输出 item 后可丢弃最新 compaction item 之前的内容，最新 compaction item 已携带必要 context。

**2. 独立 compact 端点（手动控制）**

```python
compacted = client.responses.compact(
    model="gpt-5.5",
    input=long_input_items_array,
)
next_input = [
    *compacted.output,   # 直接使用压缩输出
    {"type": "message", "role": "user", "content": user_input_message()},
]
```

- 完全无状态，ZDR 友好
- **不要修剪** `/responses/compact` 的输出 —— 将返回的完整窗口传给下一次调用
- 发送的 context window 仍需在模型 context 限制内

### 两种对话策略

| 策略 | 模式 |
|---|---|
| Stateless input-array chaining | 将输出 item（包含 compaction item）追加到下一次输入数组 |
| `previous_response_id` chaining | 每 turn 只传新用户消息 + 该 ID |
