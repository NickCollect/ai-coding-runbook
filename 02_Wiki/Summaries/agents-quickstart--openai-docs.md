---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/agents/quickstart.md
source_url: https://platform.openai.com/docs/guides/agents/quickstart
title: "OpenAI — Agents SDK Quickstart"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Subagent]
concepts_referenced: [Agentic-loop, Tool-use]
---

## 核心要点

Agents SDK 快速入门，5分钟内跑起第一个 agent。

### 安装

```bash
# TypeScript
npm install @openai/agents zod

# Python
pip install openai-agents

export OPENAI_API_KEY=sk-...
```

### 最简 agent

```python
from agents import Agent, Runner

agent = Agent(
    name="History tutor",
    instructions="You answer history questions clearly and concisely.",
    model="gpt-5.5",
)

result = await Runner.run(agent, "When did the Roman Empire fall?")
print(result.final_output)
```

### 添加 function tool

```python
@function_tool
def history_fun_fact() -> str:
    """Return a short history fact."""
    return "Sharks are older than trees."
```

### 多 specialist + handoffs

```python
triage_agent = Agent(
    name="Homework triage",
    instructions="Route each homework question to the right specialist.",
    handoffs=[history_tutor, math_tutor],
)
result = await Runner.run(triage_agent, "Who was the first president of the United States?")
print(result.last_agent.name)
```

### 查看 traces

首次运行后打开 [Traces dashboard](https://platform.openai.com/traces) 查看模型调用、tool 调用、handoff 和 guardrail。

### 推荐阅读顺序

1. Agent definitions → 2. Using tools → 3. Running agents → 4. Orchestration
