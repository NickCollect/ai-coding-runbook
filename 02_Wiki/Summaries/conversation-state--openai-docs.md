---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/conversation-state.md
source_url: https://platform.openai.com/docs/guides/conversation-state
title: "OpenAI — Conversation State 管理"
summarized_at: 2026-05-05
entities_referenced: [Compaction]
concepts_referenced: [Context-window]
---

## 核心要点

OpenAI 提供三种管理多 turn 对话状态的方式。

### 方式一：手动管理

将上一轮的 messages 作为参数传入：

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "user", "content": "knock knock."},
        {"role": "assistant", "content": "Who's there?"},
        {"role": "user", "content": "Orange."},
    ],
)
```

### 方式二：Conversations API

创建持久对话对象，可跨 session/设备/job 复用：

```python
conversation = openai.conversations.create()
response = openai.responses.create(
    model="gpt-4.1",
    input=[{"role": "user", "content": "What are the 5 Ds of dodgeball?"}],
    conversation="conv_689667905b048191b4740501625afd940c7533ace33a2dab"
)
```

**与 response 对象不同**：Conversation 对象无 30 天 TTL，持久保存。

### 方式三：`previous_response_id`

```python
second_response = client.responses.create(
    model="gpt-4o-mini",
    previous_response_id=response.id,
    input=[{"role": "user", "content": "explain why this is funny."}],
)
```

注意：链中所有历史 input token 仍按 input token 计费。

### Context window 管理

- `gpt-4o-2024-08-06`：最大输出 16,384 tokens，context window 128K
- 长对话使用 compaction 管理：server-side（`context_management` 参数）或手动（`/responses/compact`）

### 数据保留

- Response 对象默认保存 **30 天**（可在 dashboard 查看日志）
- `store: false` 禁用保留
- Conversation 对象：无 30 天 TTL
- OpenAI **不使用** API 数据训练模型（除非显式同意）
