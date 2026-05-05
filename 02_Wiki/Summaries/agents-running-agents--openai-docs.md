---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/agents/running-agents.md
source_url: https://platform.openai.com/docs/guides/agents/running-agents
title: "OpenAI — Agents SDK: Running Agents"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Subagent, Streaming-API]
concepts_referenced: [Agentic-loop, Context-window]
---

## 核心要点

Agents SDK 的 runner 实现 agent loop，支持多种对话状态策略和 streaming。

### Agent loop 步骤

1. 用准备好的 input 调用当前 agent 的模型
2. 检查模型输出
3. 有 tool call → 执行并继续
4. handoff → 切换 agent 并继续
5. 有最终回答且无更多 tool work → 返回结果

### 对话状态策略

| 策略 | 状态存储位置 | 适用场景 | 下次传入 |
|---|---|---|---|
| Manual replay | 应用程序 | 小型对话循环 | replay-ready history |
| `session` | 存储 + SDK | 持久对话、可恢复 run | 同一 session |
| `conversationId` | Conversations API | 跨 worker/服务的共享状态 | 同一 ID + 新 turn |
| `previous_response_id` | Responses API | 最轻量服务端管理 | 上一 response ID + 新 turn |

**同一对话选一种策略**，混用本地 replay 和服务端管理可能导致 context 重复。

### Streaming 示例

```python
stream = Runner.run_streamed(agent, "Give me three short facts about Saturn.")

async for event in stream.stream_events():
    if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
        print(event.data.delta, end="", flush=True)
```

### 暂停与失败处理

- **Runtime/validation failures**：max-turn 限制、guardrail 异常、tool 错误
- **Expected pauses**：human approval 请求 → 视为**暂停的 run**，不是新 turn

将 approval 视为暂停 run（而非新 turn）可保持 turn 计数、history 和 continuation ID 的一致性。
