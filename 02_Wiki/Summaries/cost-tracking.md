---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/cost-tracking.md
source_url: https://code.claude.com/docs/en/agent-sdk/cost-tracking
title: "Track cost and usage (Agent SDK)"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK]
concepts_referenced: [Agentic-loop, Prompt-caching]
---

How to read token usage and cost estimates from the Claude Agent SDK (Python + TypeScript).

Key facts:
- `total_cost_usd` / `costUSD` are **client-side estimates** computed from a price table bundled at build time. Not authoritative; do not bill end users from these. Use the Anthropic Usage and Cost API for billing.
- Scopes: `query()` call → contains multiple **steps** (request/response cycles). A **session** is multiple `query()` calls linked by session ID via `resume`.
- Each `query()` ends with one **result message** carrying cumulative `total_cost_usd` and `usage`. Read this once for the call total — works on success or error.
- TypeScript: per-step usage on `message.message.usage` + `message.message.id`; per-model on `result.modelUsage`.
- Python: per-step usage on `AssistantMessage.usage` + `message_id`; per-model on `ResultMessage.model_usage`.
- **Parallel tool calls** produce multiple assistant messages sharing the same ID with identical usage. Always **deduplicate by ID** to avoid double-counting.
- SDK does not provide session-level totals across multiple `query()` calls — accumulate `total_cost_usd` yourself.
- Cache fields in `usage`: `cache_creation_input_tokens` (higher rate) + `cache_read_input_tokens` (reduced rate). Prompt caching is automatic — no config needed.
- Default cache TTL is 5 min; set env `ENABLE_PROMPT_CACHING_1H=1` for 1-hour TTL (higher write cost, more reads). Required for short-session workloads on Bedrock/Vertex/Foundry. Claude subscription users get 1-hour automatically.
- Output token discrepancies on same-ID messages: prefer the highest value or the result message.
