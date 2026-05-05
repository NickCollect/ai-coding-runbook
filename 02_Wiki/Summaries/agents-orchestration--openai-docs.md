---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/agents/orchestration.md
source_url: https://platform.openai.com/docs/guides/agents/orchestration
title: "OpenAI — Agents SDK: Orchestration 与 Handoffs"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Agent-SDK]
concepts_referenced: [Agentic-loop, Agent-team]
---

## 核心要点

多 agent 工作流有两种主要编排模式：handoff（委托所有权）和 agents-as-tools（管理者模式）。

### 两种模式对比

| 模式 | 适用场景 | 效果 |
|---|---|---|
| **Handoffs** | specialist 应接管当前对话分支 | 控制权转移给 specialist |
| **Agents as tools** | manager 保持控制，specialist 作为有界能力调用 | manager 保留对回复的所有权 |

### Handoff 示例

```python
from agents import Agent, handoff

triage_agent = Agent(
    name="Triage agent",
    handoffs=[billing_agent, handoff(refund_agent)],
)
```

最佳实践：给每个 specialist 分配窄职责；`handoff_description` 简短具体；仅在确实需要不同指令/工具/策略时才拆分。

### Agents as tools 示例

```python
main_agent = Agent(
    name="Research assistant",
    tools=[
        summarizer.as_tool(
            tool_name="summarize_text",
            tool_description="Generate a concise summary of the supplied text.",
        )
    ],
)
```

适合 manager 需要综合最终答案、specialist 执行有界任务（摘要、分类）的场景。

### 何时增加 specialist

**尽量从单个 agent 开始**。仅当 specialist 能实质性改善以下方面时再拆分：
- 能力隔离、策略隔离、prompt 清晰度、trace 可读性

过早拆分 = 更多 prompt、更多 trace、更多审批面，未必带来更好工作流。
