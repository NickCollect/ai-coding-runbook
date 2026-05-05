---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling
title: "Programmatic tool calling"
summarized_at: 2026-05-05
entities_referenced: [Code-execution-tool, Tool-use, Structured-outputs, MCP-server]
concepts_referenced: [Context-window]
---

Programmatic tool calling lets Claude write code that calls your tools programmatically *inside* a [[Code-execution-tool]] container, instead of one model round-trip per tool invocation. Reduces latency for multi-tool workflows and decreases token consumption by allowing Claude to filter or process data before it reaches the [[Context-window]]. On agentic search benchmarks like BrowseComp and DeepSearchQA, "adding programmatic tool calling on top of basic search tools was the key factor that fully unlocked agent performance." **Not eligible for ZDR.**

**Compounds at scale.** Checking budget compliance across 20 employees the traditional way: 20 separate model round-trips, pulling thousands of expense line items into context. Programmatic version: a single script runs all 20 lookups, filters, and returns only the employees who exceeded their limits—shrinking input from hundreds of KB to a handful of lines.

**Requirements.** Tool version `code_execution_20260120` on Opus 4.7/4.6/4.5 and Sonnet 4.6/4.5. Available on Claude API and Microsoft Foundry. Requires the code execution tool to be enabled.

**Mechanism.**
1. Claude writes Python that invokes your tool as a function (with pre/post-processing logic).
2. The code runs in a sandboxed container.
3. When a tool function is called, code execution **pauses** and the API returns a `tool_use` block.
4. You provide the result; code execution continues. **Intermediate results never load into Claude's context.**
5. Final code output reaches Claude.

Custom tools are auto-converted to async Python functions to support parallel calls (`result = await query_database("<sql>")`); the SDK auto-includes the wrapper.

**Key fields.**
- `allowed_callers` on the tool definition: `["direct"]` (default; only Claude calls directly), `["code_execution_20260120"]` (only callable from inside code execution), or both. Pick one or the other—not both—for clearer guidance to Claude.
- `caller` on every `tool_use` block in the response shows how it was invoked: `{type: "direct"}` or `{type: "code_execution_20260120", tool_id: "srvtoolu_..."}`. The `tool_id` references the code execution tool that made the programmatic call.

**Container lifecycle.** Same containers as code execution: 30-day max lifetime, cleaned up after **4.5 minutes idle**, container ID returned in `container.id`, reusable across requests via `container: <id>`. **You must respond to a paused tool call before container expiration**—monitor `expires_at`. If it expires, Claude may treat the call as timed out (`TimeoutError` in stderr) and retry.

**Message formatting restriction (critical).** When responding to a programmatic tool call, the user message must contain **only** `tool_result` blocks—no text content. (The general client-tool rule is "tool_result first, text after"; programmatic tool calls forbid the text entirely.)

**Patterns shown.**
- *Batch processing with loops*: query each region in a Python `for` loop, aggregate inside the script, return only the top region. Reduces 5 model round-trips to 1.
- *Early termination*: check endpoints in a loop, `break` on first healthy. Stops doing work once success criteria met.
- *Conditional tool selection*: choose `read_full_file` vs. `read_file_summary` based on `get_file_info` size.
- *Data filtering*: fetch logs, filter for ERROR, return only last 10 errors. Saves the model from seeing the full log.

**Constraints / incompatibilities.**
- [[Structured-outputs]] (`strict: true`) NOT supported with programmatic calling.
- Cannot force programmatic calling of a specific tool via `tool_choice`.
- `disable_parallel_tool_use: true` not supported.
- Tools provided by an [[MCP-server]] connector cannot currently be called programmatically.

**Token efficiency.** Tool results from programmatic calls are NOT added to Claude's context—only the final code execution output is. Calling 10 tools directly uses ~10x the tokens of calling them programmatically and returning a summary. Tool results from programmatic invocations don't count toward input/output token usage; only the final code execution result and Claude's response count.

**Pricing.** Same as code execution.

**Best practices.** Provide detailed output schema docs in tool descriptions (Claude deserializes results in code, so JSON structure clarity matters). Return structured/parseable data. Keep responses concise. Reuse containers for related requests. Use programmatic calling for: large dataset processing where only aggregates matter; multi-step workflows with 3+ dependent tool calls; filtering/sorting/transformation; tasks where intermediate data shouldn't influence Claude's reasoning; parallel operations across many items. Avoid for: single tool calls; tools needing immediate user feedback; very fast operations where overhead outweighs benefit.

**Why it works.** Claude's training includes extensive code exposure—when tools appear as callable functions in a code execution environment, Claude can naturally chain operations, process large outputs efficiently (filter, write to files, return summaries), and reduce latency by eliminating re-sampling between tool calls. This enables workflows impractical with traditional tool use—e.g., processing 1M+ token files programmatically rather than loading everything into conversation context.

**Alternative implementations.** Same pattern can run outside Anthropic's managed code execution: client-side direct execution (simple but executes untrusted code unsafely), self-managed sandboxed execution (safe but complex to maintain), or Anthropic's managed offering (default; safe + opinionated Python env).
