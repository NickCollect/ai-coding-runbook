---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/overview.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
title: "Tool use with Claude"
summarized_at: 2026-05-05
entities_referenced: [Tool-use, Web-search-tool, Code-execution-tool, Web-fetch-tool, Tool-search-tool-API, Bash-tool-API, Text-editor-tool, Messages-API, MCP-server]
concepts_referenced: [Agentic-loop]
---

Entry-point overview for tool use on the Claude API. Tool use lets Claude call functions you define or that Anthropic provides; Claude decides when to call a tool based on the user's request and the tool's description, then returns either a structured `tool_use` block (for client tools) or executes server-side (for server tools).

**Two execution modes—where the code runs is the primary distinction:**

- **Client tools** (user-defined tools, plus Anthropic-schema tools like the [[Bash-tool-API]] and [[Text-editor-tool]]) run in your application. Claude responds with `stop_reason: "tool_use"` and one or more `tool_use` blocks; your code executes the operation and you send back a `tool_result`.
- **Server tools** ([[Web-search-tool]], [[Code-execution-tool]], [[Web-fetch-tool]], [[Tool-search-tool-API]]) run on Anthropic's infrastructure. You see results directly without handling execution.

**Quick example.** A `web_search_20260209` server tool added to `tools` answers "What's the latest on the Mars rover?" with `model: claude-opus-4-7` via the [[Messages-API]]. cURL, ant CLI, Python SDK, and TypeScript SDK examples shown.

**Schema conformance.** Add `strict: true` to a tool definition to guarantee Claude's tool calls always match the schema exactly. (Linked to "Strict tool use" doc.)

**MCP integration.** For connecting to [[MCP-server]] s use the MCP connector. For building your own MCP client, see modelcontextprotocol.io.

**Capability claim.** "Tool access is one of the highest-leverage primitives you can give an agent." Cited evidence: on LAB-Bench FigQA (scientific figure interpretation) and SWE-bench (real-world software engineering), even basic tool access produces outsized capability gains, often surpassing human-expert baselines.

**Behavior on missing parameters.** If the user's prompt lacks values for required tool parameters, Opus is far more likely than Sonnet to recognize the missing parameter and ask a clarifying question. Sonnet may instead infer a reasonable value—example: a `get_weather` call where Sonnet may infer `{"location": "New York, NY", "unit": "fahrenheit"}` from a prompt that provided no location. This behavior is not guaranteed; it is more pronounced on weaker models and ambiguous prompts.

**Pricing model.** Tool use is priced based on (1) total input tokens including the `tools` parameter, (2) output tokens, (3) for server tools additional usage-based charges (e.g., web search per-search). Client tools are priced like any other API request.

**Tool-use system prompt overhead.** When `tools` is non-empty, the API automatically injects a tool-use system prompt. Token counts vary by model and `tool_choice`:

| Model | `auto` / `none` | `any` / `tool` |
|---|---|---|
| Opus 4.7, 4.6, 4.5, 4.1, 4 | 346 | 313 |
| Sonnet 4.6, 4.5, 4 | 346 | 313 |
| Sonnet 3.7 (deprecated) | 346 | 313 |
| Haiku 4.5 | 346 | 313 |
| Haiku 3.5, Haiku 3 | 264 | 340 |
| Opus 3 (deprecated) | 530 | 281 |
| Sonnet 3 | 159 | 235 |

If no tools are provided, `tool_choice: none` adds 0 system-prompt tokens. These counts add to the normal `tools` parameter overhead (names, descriptions, schemas) and to `tool_use` / `tool_result` block tokens. Total cost is reflected in the response's `usage` metrics.

**Where to go next.** Three paths offered: (1) the conceptual "How tool use works" doc which covers the [[Agentic-loop]], where tools run, and when to use tools; (2) the build-a-tool-using-agent tutorial; (3) the Tool reference directory for all Anthropic-provided tools and their properties.
