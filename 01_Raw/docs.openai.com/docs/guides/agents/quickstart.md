# Agents SDK Quickstart

<!-- source: https://platform.openai.com/docs/guides/agents/quickstart -->

## Install

```bash
# TypeScript
npm install @openai/agents zod

# Python
pip install openai-agents

export OPENAI_API_KEY=sk-...
```

## Create and run your first agent

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

## Add a function tool

```python
from agents import Agent, Runner, function_tool

@function_tool
def history_fun_fact() -> str:
    """Return a short history fact."""
    return "Sharks are older than trees."

agent = Agent(
    name="History tutor",
    instructions="Answer history questions clearly. Use history_fun_fact when it helps.",
    tools=[history_fun_fact],
)
```

## Add specialist agents with handoffs

```python
from agents import Agent, Runner

history_tutor = Agent(
    name="History tutor",
    handoff_description="Specialist for history questions.",
    instructions="Answer history questions clearly and concisely.",
)

math_tutor = Agent(
    name="Math tutor",
    handoff_description="Specialist for math questions.",
    instructions="Explain math step by step and include worked examples.",
)

triage_agent = Agent(
    name="Homework triage",
    instructions="Route each homework question to the right specialist.",
    handoffs=[history_tutor, math_tutor],
)

result = await Runner.run(triage_agent, "Who was the first president of the United States?")
print(result.final_output)
print(result.last_agent.name)
```

## Inspect traces

After first run works, open the [Traces dashboard](https://platform.openai.com/traces) to inspect model calls, tool calls, handoffs, and guardrails.

## Recommended reading order

1. **Agent definitions** — shape one specialist cleanly
2. **Using tools** — hosted tools, function tools, agents-as-tools
3. **Running agents** — agent loop, streaming, continuation strategies
4. **Orchestration** — when specialists should take over
