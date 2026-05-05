---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/SKILL.md
title: "anthropics/skills: claude-api SKILL.md"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: [Tool-use, Extended-thinking, Prompt-caching, Context-window]
---

The top-level `claude-api` skill — a routing/orchestration document for building Claude API / Anthropic SDK applications. Triggers when code imports `anthropic`/`@anthropic-ai/sdk`, user asks for the Claude API or Managed Agents, or modifies Claude features (caching, thinking, compaction, tool use, batch, files, citations, memory) or models. SKIPS when file imports OpenAI/other-provider SDKs.

**Default model**: ALWAYS `claude-opus-4-7` unless user names another. Use exact model ID strings (no date suffixes).

**Defaults for Claude API output**:
- Model: `claude-opus-4-7`
- Thinking: `{type: "adaptive"}` for anything remotely complicated
- Streaming: default for long input/output/high `max_tokens` (use `.get_final_message()` / `.finalMessage()` helper)

**Output requirement**: official Anthropic SDK for the project's language; raw HTTP only when explicitly requested or no SDK exists. Never mix SDK + raw HTTP in same project. Never use OpenAI-compatible shims. Never guess SDK usage — get bindings from `{lang}/` files or WebFetch official repos from `shared/live-sources.md`.

**Language detection** (file-based): py → `python/`, ts/tsx → `typescript/`, js/jsx → `typescript/` (same SDK), java/kt/scala → `java/`, go → `go/`, rb → `ruby/`, cs → `csharp/`, php → `php/`. Multiple → ask. Unsupported (Rust/Swift/C++/Elixir) → cURL or reference Python.

**Surface decision tree** (start simple):
- Single LLM call (classification/summarization) → Claude API.
- Workflow with code-controlled logic → Claude API + tool use.
- Custom agent + your tools, you host compute → Claude API agentic loop.
- Server-managed stateful agent with workspace → Managed Agents (NOT on Bedrock/Vertex/Foundry — use Claude API + tool use there).

**Current models cached 2026-04-15**:
| Model | ID | Context | Input/Output $/MTok |
|---|---|---|---|
| Opus 4.7 | `claude-opus-4-7` | 1M | $5/$25 |
| Opus 4.6 | `claude-opus-4-6` | 1M | $5/$25 |
| Sonnet 4.6 | `claude-sonnet-4-6` | 1M | $3/$15 |
| Haiku 4.5 | `claude-haiku-4-5` | 200K | $1/$5 |

**Thinking & effort**:
- **Opus 4.7**: adaptive ONLY (`thinking: {type: "adaptive"}`). `budget_tokens` returns 400. Sampling params (`temperature`, `top_p`, `top_k`) also removed. New `xhigh` effort level (between high and max) is the recommended default.
- **Opus 4.6 / Sonnet 4.6**: adaptive recommended; `budget_tokens` deprecated (transitional escape hatch on 4.6 only, NOT 4.7).
- **Effort GA**: `output_config: {effort: "low"|"medium"|"high"|"xhigh"|"max"}`. `max` Opus-tier only. Default `high`.
- **Opus 4.7 thinking content omitted by default** — opt in with `thinking: {type: "adaptive", display: "summarized"}`.
- **Task Budgets (beta, 4.7)**: `output_config: {task_budget: {type: "tokens", total: N}}` — agent self-moderates, sees countdown. Min 20,000 tokens. Beta header `task-budgets-2026-03-13`.

**Compaction (beta, 4.7/4.6/Sonnet 4.6)**: server-side summarization at default 150K threshold. Beta `compact-2026-01-12`. **Append `response.content` (not just text) back — compaction blocks must be preserved**.

**Prompt caching**: prefix match — any byte change invalidates downstream. Render order: tools → system → messages. Stable content first; volatile after last `cache_control` breakpoint. Max 4 breakpoints. Min cacheable prefix model-dependent (Opus 4096 tokens, Sonnet 4.6/Haiku 4.5 2048, etc.). Verify via `usage.cache_read_input_tokens`.

**Managed Agents (beta)**: third surface. Mandatory flow: Agent (`POST /v1/agents` once → store ID) → Session (`POST /v1/sessions` per run, references agent by ID/version). `model`/`system`/`tools` live on agent NEVER session. **First-party only** (not Bedrock/Vertex/Foundry). Beta header `managed-agents-2026-04-01` (SDK auto). Skills + Files APIs need their own betas. Use `/claude-api managed-agents-onboard` subcommand for guided setup.

**Common pitfalls**: don't truncate inputs; assistant message prefills removed on 4.6/4.7 family (use structured outputs); don't lowball `max_tokens` (16K non-streaming, 64K streaming default); 128K output requires streaming; tool input JSON may have varied escaping (use `json.loads`); use `output_config: {format: ...}` not deprecated `output_format`; don't reimplement SDK helpers; don't redefine SDK types; for migration, ask scope first if not named.
