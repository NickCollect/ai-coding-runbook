---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/prompt-caching.md
title: "claude-api skill: prompt-caching reference"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: [Prompt-caching]
---

Prompt caching design + optimization reference inside the `claude-api` skill.

**The one invariant**: **prompt caching is a prefix match**. Any byte change anywhere in the prefix invalidates everything after. Cache key = exact bytes up to each `cache_control` breakpoint.

Render order: **`tools` → `system` → `messages`**. A breakpoint on the last system block caches tools+system together.

**Workflow for optimizing existing code**:
1. Trace prompt assembly path.
2. Classify each input by stability: never-changes (early), per-session (after global prefix), per-turn (end), per-request (eliminate or move to very end).
3. Check rendered order matches stability order.
4. Place breakpoints at stability boundaries.
5. Audit for silent invalidators.

**Placement patterns**:
- **Large shared system prompt**: breakpoint on last system text block (caches tools+system).
- **Multi-turn conversations**: breakpoint on last content block of latest user turn.
- **Shared prefix, varying suffix**: breakpoint at end of SHARED portion not whole prompt.
- **Prompts that change from byte 0**: don't cache — pay write premium with no reads.

**Architectural guidance** (matters more than markers):
- Keep system prompt **frozen**. Don't interpolate "current date: X" or "user: Z" — invalidates downstream. Inject dynamic context as later messages.
- Don't change tools or model mid-conversation. Tools at position 0 — add/remove/reorder invalidates entire cache. Caches model-scoped. Serialize tools deterministically (sort by name).
- Fork operations must reuse parent's exact prefix. Sub-agents/summarization must copy `system`/`tools`/`model` verbatim or miss parent's cache.

**Silent invalidators** (grep for these):
- `datetime.now()` / `Date.now()` / `time.time()` in system prompt.
- `uuid4()` / `crypto.randomUUID()` early in content.
- `json.dumps(d)` without `sort_keys=True`; iterating a `set`.
- f-string with session/user ID in system prompt.
- Conditional system sections (`if flag: system += ...`).
- `tools=build_tools(user)` where set varies per user.

**API**:
- `cache_control: {type: "ephemeral"}` — 5-minute TTL default.
- `cache_control: {type: "ephemeral", ttl: "1h"}` — 1-hour TTL.
- Max 4 breakpoints per request.
- Goes on any content block: text/image/tool_use/tool_result/document.
- Top-level `cache_control` on `messages.create()` auto-places on last cacheable.

**Minimum cacheable prefix** (model-dependent — silently won't cache shorter):
| Model | Min |
|---|---|
| Opus 4.7 / 4.6 / 4.5 / Haiku 4.5 | 4096 |
| Sonnet 4.6 / Haiku 3.5 / Haiku 3 | 2048 |
| Sonnet 4.5 / 4.1 / 4 / 3.7 | 1024 |

**Economics**: cache reads ~0.1× base. Writes 1.25× (5min TTL) or 2× (1h TTL). 5min break-even = 2 requests; 1h break-even = 3 requests.

**Verify hits**: `usage.cache_read_input_tokens`, `cache_creation_input_tokens`, `input_tokens` (uncached remainder). Total = sum of all three. If `cache_read_input_tokens` zero across repeated identical prefixes, silent invalidator at work.

**Invalidation hierarchy** (3 cache tiers, changes invalidate own tier + below):
| Change | Tools / System / Messages cache |
|---|---|
| Tool defs (add/remove/reorder) | All invalidated |
| Model switch | All invalidated |
| `speed`, web-search, citations toggle | System+messages invalidated |
| System prompt content | System+messages invalidated |
| `tool_choice`, images, `thinking` toggle | Only messages invalidated |
| Message content | Only messages invalidated |

→ Can change `tool_choice` per request or toggle `thinking` without losing tools+system cache.

**20-block lookback window**: each breakpoint walks backward at most 20 content blocks to find prior cache entry. Long agentic loops (many tool_use/tool_result pairs in one turn) can exceed → silent miss. Fix: place intermediate breakpoint every ~15 blocks.

**Concurrent-request timing**: cache becomes readable only AFTER first response BEGINS streaming. N parallel requests with identical prefixes all pay full price. Fan-out: send 1 → await first streamed token → fire remaining N−1.
