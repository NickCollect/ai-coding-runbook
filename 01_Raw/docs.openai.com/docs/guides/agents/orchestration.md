# Orchestration and handoffs

<!-- source: https://platform.openai.com/docs/guides/agents/orchestration -->

Multi-agent workflows are useful when specialists should own different parts of the job.

## Choose the orchestration pattern

| Pattern | Use when | What happens |
|---|---|---|
| **Handoffs** | A specialist should take over the conversation for that branch | Control moves to the specialist agent |
| **Agents as tools** | A manager should stay in control and call specialists as bounded capabilities | Manager keeps ownership of reply |

## Handoffs — delegated ownership

Use when a specialist should own the next response (not just help behind the scenes).

```python
from agents import Agent, handoff

billing_agent = Agent(name="Billing agent")
refund_agent = Agent(name="Refund agent")

triage_agent = Agent(
    name="Triage agent",
    handoffs=[billing_agent, handoff(refund_agent)],
)
```

Best practices:
- Give each specialist a narrow job
- Keep `handoff_description` short and concrete
- Split only when the next branch truly needs different instructions, tools, or policy

## Agents as tools — manager-style workflows

Use when the main agent should stay responsible for the final answer.

```python
from agents import Agent

summarizer = Agent(
    name="Summarizer",
    instructions="Generate a concise summary of the supplied text.",
)

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

Better fit when:
- Manager should synthesize the final answer
- Specialist is doing a bounded task (summarization, classification)
- You want one stable outer workflow with nested specialist calls instead of ownership transfer

## When to add specialists

Start with ONE agent whenever possible. Add specialists only when they materially improve:
- Capability isolation
- Policy isolation
- Prompt clarity
- Trace legibility

Splitting too early = more prompts, more traces, more approval surfaces without necessarily better workflow.
