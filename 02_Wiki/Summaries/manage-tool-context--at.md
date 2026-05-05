---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context
title: "Manage tool context"
summarized_at: 2026-05-05
entities_referenced: [Tool-use, Tool-search-tool-API, Prompt-caching, Context-editing]
concepts_referenced: [Context-window]
---

Decision guide for choosing among four approaches that reduce tool-related context bloat. Tool definitions and accumulated `tool_result` blocks consume the [[Context-window]]; long-running agents with many tools or many turns can exhaust available context before the task is finished. Each approach targets a different source of pressure.

**The four approaches:**

| Approach | What it reduces | When it fits |
|---|---|---|
| Tool search ([[Tool-search-tool-API]]) | Tool definitions loaded upfront | Large toolsets (20+) where most tools aren't needed every turn |
| Programmatic tool calling | `tool_result` round-trips | Chains of tool calls that can execute as a single script |
| Prompt caching ([[Prompt-caching]]) | *Token cost* of repeated tool definitions | Stable toolsets across many requests |
| Context editing ([[Context-editing]]) | Old `tool_result` blocks in history | Long conversations where early results are no longer relevant |

**Tool search.** Keeps tool definitions out of context until Claude asks for them. Instead of sending 50 tool schemas upfront, send a single `tool_search` tool and let Claude discover the rest on demand. Trade-off: small added latency (one extra turn for lookup) for a large baseline-context reduction.

**Programmatic tool calling.** Collapses a sequence of tool calls into a single code block that Claude writes and Anthropic's code execution sandbox runs. Rather than five round-trips of `tool_use`/`tool_result`, Claude emits one script that calls all five functions from inside the sandbox—**intermediate results never enter conversation history.**

**Prompt caching.** Doesn't reduce context tokens, but reduces what you *pay* on subsequent requests. Cache stable tool definitions once and reuse the cached prefix. Right choice when the toolset is large but fixed.

**Context editing.** Removes old `tool_result` blocks from conversation history once they've served their purpose. A long agent loop might produce hundreds of intermediate results that were useful at the time but are now dead weight. Trim them without restarting the conversation.

**Combining approaches.** They compose. A long-running agent might use tool search to keep the toolset lean, prompt caching to amortize the cost of remaining definitions, and context editing to trim stale results as conversation grows. No conflict.

**Recommended starting point for a high-volume agent:**
1. Enable [[Prompt-caching]] on tool definitions from day one. Cache writes carry a 25% markup over base input pricing, paying back on the second cache hit.
2. Add [[Tool-search-tool-API]] once your toolset grows past roughly 20 tools or your baseline context usage becomes noticeable.
3. Add [[Context-editing]] once individual conversations run long enough that early results become irrelevant.
4. Consider programmatic tool calling if you notice repetitive chains of small tool calls that could run as a single batch.

This is essentially a navigation page; the four linked deep dives carry the implementation details.
