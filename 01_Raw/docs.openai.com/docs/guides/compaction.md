# Compaction

<!-- source: https://platform.openai.com/docs/guides/compaction -->

Compaction reduces context size while preserving state needed for subsequent turns. Helps balance quality, cost, and latency as conversations grow.

## Server-side compaction

Enable via `context_management` with `compact_threshold` in `client.responses.create`:

```python
response = client.responses.create(
    model="gpt-5.3-codex",
    input=conversation,
    store=False,
    context_management=[{"type": "compaction", "compact_threshold": 200000}],
)
```

- When rendered token count crosses the threshold, server runs compaction automatically
- No separate `/responses/compact` call needed
- Response stream includes encrypted compaction item
- ZDR-friendly when `store=False`

**Latency tip**: After appending output items, you can drop items that came before the most recent compaction item. The latest compaction item carries the necessary context.

## Standalone compact endpoint (`/responses/compact`)

For explicit control over when compaction happens:

```python
# 1) Compact the current window
compacted = client.responses.compact(
    model="gpt-5.5",
    input=long_input_items_array,
)

# 2) Start next turn by appending new user message
next_input = [
    *compacted.output,  # Use compact output as-is
    {"type": "message", "role": "user", "content": user_input_message()},
]

next_response = client.responses.create(
    model="gpt-5.5",
    input=next_input,
    store=False,
)
```

- Fully stateless and ZDR-friendly
- Send full context window → get new compacted context window
- Do NOT prune `/responses/compact` output — pass the returned window as-is to next call
- The context window you send to `/responses/compact` must still fit within the model's context window

## Two conversation strategies

| Strategy | Pattern |
|---|---|
| Stateless input-array chaining | Append output items (including compaction items) to next input array |
| `previous_response_id` chaining | Pass only the new user message each turn + carry that ID forward |
