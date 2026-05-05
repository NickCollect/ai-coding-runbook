# Reasoning models

<!-- source: https://platform.openai.com/docs/guides/reasoning -->

Reasoning models like GPT-5.5 use internal reasoning tokens before producing a response. This helps the model plan, use tools effectively, inspect alternatives, recover from ambiguity, and solve harder multi-step tasks.

**Best for**: complex problem solving, coding, scientific reasoning, multi-step agentic workflows.

Start with `gpt-5.5` for most reasoning workloads. For highest intelligence with more latency, use `gpt-5.5-pro`. For lower cost, `gpt-5.4`. For lowest cost/latency, `gpt-5.4-mini`.

Reasoning models work better with the Responses API (vs Chat Completions API).

## Reasoning effort

The `reasoning.effort` parameter controls how much the model "thinks":

| Effort | Best for |
|---|---|
| `none` | Latency-critical tasks with no reasoning benefit. Voice, fast retrieval, classification. |
| `low` | Efficient reasoning with modest latency increase. Data analysis, drafting, execution-oriented coding, customer support. |
| `medium` | Default. Quality and reliability. Planning, complex reasoning. Agentic coding, research. |
| `high` | Hard reasoning, complex debugging, deep planning. High-value tasks. |
| `xhigh` | Deep research, async workflows, very long rollouts. Security/code review, enterprise productivity. |

Default for `gpt-5.5` is `medium`.

## How reasoning works

Reasoning models introduce **reasoning tokens** in addition to input and output tokens. Reasoning tokens are used to "think" but are NOT visible via API. They still occupy space in the context window and are billed as output tokens.

gpt-5.5 and gpt-5.4 support **interleaved thinking** — the model can generate visible output tokens before and in between thinking, and can think between tool calls.

## Token usage details

Reasoning token count is visible in the usage object under `output_tokens_details.reasoning_tokens`.

```json
{
  "usage": {
    "input_tokens": 75,
    "output_tokens": 1186,
    "output_tokens_details": { "reasoning_tokens": 1024 },
    "total_tokens": 1261
  }
}
```

## Managing context window

- Reasoning models may generate anywhere from a few hundred to tens of thousands of reasoning tokens
- Recommend reserving at least **25,000 tokens** for reasoning and outputs when starting
- Use `max_output_tokens` to limit total tokens (includes reasoning + output)
- If context limit reached, response `status` will be `incomplete` with `incomplete_details.reason = "max_output_tokens"`

## Keeping reasoning items in context

When doing function calling with reasoning models, pass back any reasoning items returned with the last function call. This allows the model to continue its reasoning process efficiently.

Simplest approach: use `previous_response_id` parameter to chain responses automatically.

## Reasoning summaries

You can view a summary of the model's reasoning using the `summary` parameter in the `reasoning` object:
- `"auto"` — most detailed summarizer available for the model
- `"concise"` — shorter summary
- `"detailed"` — full detailed summary

Summary appears in the `summary` array in the `reasoning` output item.

## Prompting reasoning models

Reasoning-capable GPT-5 models work best when you:
- Give a clear goal, strong constraints, and explicit output contract
- Do NOT prescribe every intermediate step
- Treat `reasoning.effort` as a tuning knob for performance
- For agentic workflows, define what "done" looks like and how the model should verify its work
