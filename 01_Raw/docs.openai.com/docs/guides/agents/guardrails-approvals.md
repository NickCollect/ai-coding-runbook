# Guardrails and human review

<!-- source: https://platform.openai.com/docs/guides/agents/guardrails-approvals -->

## Choose the right control

| Use case | Control |
|---|---|
| Block disallowed user requests before main model runs | Input guardrails |
| Validate/redact final output before it leaves the system | Output guardrails |
| Check arguments or results around a function tool call | Tool guardrails |
| Pause before side effects (cancellations, edits, shell commands, sensitive MCP actions) | Human-in-the-loop approvals |

## Input guardrails

Run before the main agent — fast validation step to catch bad inputs early.

```python
from agents import Agent, GuardrailFunctionOutput, InputGuardrailTripwireTriggered, input_guardrail

@input_guardrail
async def math_guardrail(ctx, agent, input):
    result = await Runner.run(guardrail_agent, input, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_math_homework,
    )

agent = Agent(
    name="Customer support",
    instructions="Help customers with support questions.",
    input_guardrails=[math_guardrail],
)

try:
    await Runner.run(agent, "Can you solve 2x + 3 = 11 for me?")
except InputGuardrailTripwireTriggered:
    print("Guardrail blocked the request.")
```

Use blocking execution when starting the main agent is too costly or risky. Use parallel guardrails when lower latency matters more.

## Human-in-the-loop approvals

Tools can require approval before execution. The run pauses until you approve or reject.

```python
from agents import Agent, Runner, function_tool

@function_tool(needs_approval=True)
async def cancel_order(order_id: int) -> str:
    return f"Cancelled order {order_id}"

agent = Agent(
    name="Support agent",
    instructions="Handle support requests and ask for approval when needed.",
    tools=[cancel_order],
)

result = await Runner.run(agent, "Cancel order 123.")

if result.interruptions:
    state = result.to_state()
    for interruption in result.interruptions:
        state.approve(interruption)
    result = await Runner.run(agent, state)

print(result.final_output)
```

## Approval lifecycle

1. Run records an approval interruption instead of executing the tool
2. Result returns `interruptions` + resumable `state`
3. Your application approves or rejects the pending items
4. Resume the same run from `state` (NOT a new user turn)

If review takes time: serialize `state`, store it, resume later. Same run, same state.

## Important scope rules

- **Input guardrails** run only for the first agent in the chain
- **Output guardrails** run only for the agent that produces the final output
- **Tool guardrails** run on the specific function tools they're attached to

For checks around every custom tool call in a manager-style workflow, put validation next to the tool, not just at the agent level.

## Streaming + approvals

Streaming doesn't create a separate approval system. If a streamed run pauses: wait for it to settle → inspect `interruptions` → resolve approvals → resume from same `state`.
