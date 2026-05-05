# Running agents

<!-- source: https://platform.openai.com/docs/guides/agents/running-agents -->

## The agent loop

One SDK run = one application-level turn. The runner loops until a real stopping point:

1. Call the current agent's model with the prepared input
2. Inspect the model output
3. If model produced tool calls → execute them and continue
4. If model handed off to another specialist → switch agents and continue
5. If model produced a final answer with no more tool work → return result

## Conversation state strategies

| Strategy | Where state lives | Best for | What you pass next turn |
|---|---|---|---|
| Manual replay | Your application | Small chat loops, maximum control | The replay-ready history |
| `session` | Your storage + SDK | Persistent chat, resumable runs | The same session |
| `conversationId` | OpenAI Conversations API | Shared state across workers/services | Same conversation ID + only new turn |
| `previous_response_id` | OpenAI Responses API | Lightest server-managed continuation | Last response ID + only new turn |

Pick one strategy per conversation. Mixing local replay with server-managed state can duplicate context.

```python
# Using sessions for persistent state
from agents import Agent, Runner, SQLiteSession

agent = Agent(name="Tour guide", instructions="Answer with compact travel facts.")
session = SQLiteSession("conversation_123")

first_turn = await Runner.run(agent, "What city is the Golden Gate Bridge in?", session=session)
second_turn = await Runner.run(agent, "What state is it in?", session=session)
```

## Streaming

```python
from agents import Agent, Runner
from openai.types.responses import ResponseTextDeltaEvent

agent = Agent(name="Planet guide", instructions="Answer with short facts.")

stream = Runner.run_streamed(agent, "Give me three short facts about Saturn.")

async for event in stream.stream_events():
    if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
        print(event.data.delta, end="", flush=True)

print(f"\nFinal: {stream.final_output}")
```

Streaming rules:
- Wait for stream to finish before treating run as settled
- If run pauses for approval, resolve `interruptions` and resume from `state` (not a fresh turn)
- If you cancel mid-turn, resume from `state` if you want the same turn to continue

## Handling pauses and failures

Two classes of non-happy-path outcomes:
- **Runtime/validation failures**: max-turn limits, guardrail exceptions, tool errors
- **Expected pauses**: human approval requests — treat as paused runs, NOT new turns

Treating approvals as paused runs (not new turns) keeps turn counts, history, and continuation IDs consistent.
