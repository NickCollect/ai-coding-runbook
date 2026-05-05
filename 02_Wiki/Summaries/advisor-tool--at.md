---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool
title: "Advisor tool"
summarized_at: 2026-05-05
entities_referenced: [Advisor-tool, Tool-use, Prompt-caching, Web-search-tool, Batches-API, Token-counting, Context-editing]
concepts_referenced: [Extended-thinking]
---

The [[Advisor-tool]] pairs a faster, lower-cost **executor model** with a higher-intelligence **advisor model** that the executor can consult mid-generation. The advisor reads the executor's full transcript (system prompt, all tools, all turns, all tool results), produces a plan or course correction (typically 400–700 text tokens, 1,400–1,800 total including thinking), and the executor continues. Beta header: `advisor-tool-2026-03-01`. Eligible for ZDR.

**Why use it.** Long-horizon agentic workloads (coding agents, computer use, multi-step research) where most turns are mechanical but having an excellent plan is crucial. You get close to advisor-solo quality while bulk generation runs at executor rates. Two recommended pairings: Sonnet executor + Opus advisor (quality lift at similar/lower total cost vs. Sonnet alone); Haiku executor + Opus advisor (step-up in intelligence below cost of moving executor to Opus). Poor fit: single-turn Q&A, pass-through model pickers, workloads where every turn needs the advisor's full capability.

**Model compatibility.** Advisor must be at least as capable as executor. Currently the only valid advisor is Claude Opus 4.7. Valid executors: Haiku 4.5, Sonnet 4.6, Opus 4.6, Opus 4.7. Invalid pairs return `400 invalid_request_error`.

**Mechanism.** Tool definition: `{type: "advisor_20260301", name: "advisor", model: "claude-opus-4-7"}`. When the executor invokes it: (1) executor emits a `server_tool_use` block with empty `input` (the executor signals timing; the server supplies context); (2) Anthropic runs a separate sub-inference on the advisor model server-side, passing the full transcript; (3) result returns as an `advisor_tool_result` block; (4) executor continues. All inside one `/v1/messages` request—no extra round trips. The advisor itself runs without tools and without context management; thinking blocks are dropped before the result returns.

**Tool parameters.** `max_uses` (default unlimited) caps per-request advisor calls; once hit, further calls return `advisor_tool_result_error` with `error_code: "max_uses_exceeded"`. `caching: {"type": "ephemeral", "ttl": "5m" | "1h"}` enables advisor-side caching (on/off switch, not a breakpoint marker).

**Result variants.** `advisor_tool_result.content` is a discriminated union: `advisor_result` with `text` (plaintext, e.g. from Opus 4.7) or `advisor_redacted_result` with `encrypted_content` (opaque blob; server decrypts on the next turn). Round-trip the content verbatim on subsequent turns. Branch on `content.type` if switching advisor models mid-conversation.

**Error codes.** `max_uses_exceeded`, `too_many_requests` (advisor sub-inference rate-limited), `overloaded`, `prompt_too_long` (transcript exceeds advisor context window), `execution_time_exceeded`, `unavailable`. The request itself does not fail—the executor just continues without further advice. Advisor rate limits draw from the same per-model bucket as direct calls to that model.

**Multi-turn.** Pass full assistant content (including `advisor_tool_result` blocks) back. If you remove the advisor tool from `tools` while the message history still contains advisor result blocks, the API returns `400 invalid_request_error`. To bound advisor calls across a conversation, count client-side; when capping, remove the tool **and** strip all `advisor_tool_result` blocks from history.

**Streaming.** Advisor sub-inference does not stream. The executor's stream pauses at the `server_tool_use` block close; SSE pings ~every 30s during long pauses. The result arrives in a single `content_block_start` (no deltas), then executor output resumes. A `message_delta` event carries the updated `usage.iterations`.

**Billing.** Advisor calls are reported in `usage.iterations[]` with `type: "advisor_message"`, billed at advisor model rates. Top-level `usage` reflects executor only. Top-level `output_tokens` sums all executor iterations; `input_tokens` and `cache_read_input_tokens` reflect only the first executor iteration. `max_tokens` applies to executor output only—it does not bound advisor tokens.

**Caching.** Two layers. Executor-side: `advisor_tool_result` blocks are cacheable with `cache_control` like any other content block. Advisor-side: enable via the tool's `caching` field. Advisor's prompt grows monotonically across calls, so prefix is stable. Break-even point: roughly three advisor calls per conversation. Keep setting consistent across a conversation. Warning: [[Context-editing]]'s `clear_thinking` with `keep` value other than `"all"` shifts the advisor's quoted transcript and causes advisor-side cache misses (cost-only, not a quality issue). Default with [[Extended-thinking]] enabled is `keep: {type: "thinking_turns", value: 1}` on earlier Opus/Sonnet and all Haiku; on Opus 4.5+ and Sonnet 4.6+ default is keep all.

**Tool composition.** Composes with other server-side and client-side tools (e.g., [[Web-search-tool]] + advisor + custom bash tool). [[Batches-API]] supported—`usage.iterations` reported per item. [[Token-counting]] returns only executor's first-iteration tokens; for an advisor estimate, call `count_tokens` separately with the advisor model. `clear_tool_uses` not yet fully compatible with advisor blocks. `pause_turn`: a dangling advisor call ends with `stop_reason: "pause_turn"`; advisor executes on resumption.

**Best practices.** Built-in tool description nudges executor to call the advisor early and when stuck. For coding tasks, prepend a suggested system prompt block (timing guidance + how to weight the advice) for highest intelligence at near-Sonnet cost. A one-line conciseness instruction (`The advisor should respond in under 100 words and use enumerated steps`) cuts advisor output ~35–45% in internal tests. Pair Sonnet executor at medium [[Effort]] with Opus advisor for Sonnet-default-equivalent intelligence at lower cost.

**Limitations.** No streaming; no built-in conversation cap; `max_tokens` doesn't bound advisor; Anthropic Priority Tier honored per model—need Priority Tier on the advisor model specifically.
