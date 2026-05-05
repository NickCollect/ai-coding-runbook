---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works
title: "How tool use works"
summarized_at: 2026-05-05
entities_referenced: [Tool-use, Bash-tool-API, Text-editor-tool, Computer-use-tool-API, Memory-tool, Web-search-tool, Web-fetch-tool, Code-execution-tool, Tool-search-tool-API]
concepts_referenced: [Agentic-loop]
---

Conceptual explainer for tool use: the contract between application and model, where tools execute, the agentic loop pattern, and when (or when not) to use tools.

**The tool-use contract.** Tool use is a contract: you specify available operations and their I/O shapes; Claude decides when and how to call them. The model never executes anything itself—it emits a structured request, your code (or Anthropic's servers) runs the operation, and the result flows back into the conversation. This makes the model behave less like a text generator and more like a function caller. Engineers with classical API experience can integrate tool use the same way they would any typed interface: define the schema, handle the callback, return a result.

**Where tools run.** Three buckets, distinguished by *where the code executes*:

1. **User-defined tools (client-executed).** You write the schema, you execute the code, you return results. *The vast majority of tool-use traffic.* Response contains a `tool_use` block; your application extracts arguments, runs the operation, sends back a `tool_result` block. Claude never sees your implementation, only the schema and the result.

2. **Anthropic-schema tools (client-executed).** Anthropic publishes the schemas for common dev operations: [[Bash-tool-API]], [[Text-editor-tool]], [[Computer-use-tool-API]], [[Memory-tool]]. Execution model is identical to user-defined—your code runs the operation. The reason to use them instead of custom equivalents: **the schemas are trained-in.** Claude was optimized on thousands of successful trajectories using these exact signatures, so it calls them more reliably and recovers from errors more gracefully than a custom equivalent would.

3. **Server-executed tools.** [[Web-search-tool]], [[Web-fetch-tool]], [[Code-execution-tool]], [[Tool-search-tool-API]]. Anthropic runs the code. You enable the tool in the request; the server handles everything else. You never construct a `tool_result` for these. The response contains `server_tool_use` blocks showing what ran and what came back, but execution is already complete by the time you see them. Your job: enable the tool and read the final answer.

**The [[Agentic-loop]] (client tools).** Client-executed tools require your application to drive a `while`-loop keyed on `stop_reason`:

1. Send request with `tools` array and user message.
2. Claude responds with `stop_reason: "tool_use"` and one or more `tool_use` blocks.
3. Execute each tool. Format outputs as `tool_result` blocks.
4. Send a new request containing original messages + assistant's response + a user message with the `tool_result` blocks.
5. Repeat from step 2 while `stop_reason == "tool_use"`.

The loop exits on any other stop reason: `"end_turn"` (final answer), `"max_tokens"`, `"stop_sequence"`, or `"refusal"`.

**The server-side loop.** Server tools run their own loop inside Anthropic's infrastructure. A single request might trigger several web searches or code executions before the response returns. The model searches, reads, decides to search again, iterates until done—all without your application participating. The internal loop has an iteration limit; when hit, the response comes back with `stop_reason: "pause_turn"` instead of `"end_turn"`. Re-send the conversation including the paused response to let the model continue.

**When to use tools.** Tools fit when the task requires something the model can't do from text alone:
- *Actions with side effects:* sending email, writing files, updating records.
- *Fresh or external data:* current prices, today's weather, database contents.
- *Structured guaranteed-shape outputs:* when you need a JSON object with specific fields rather than prose that happens to contain the info.
- *Calling existing systems:* databases, internal APIs, file systems—the bridge between natural-language requests and the systems that fulfill them.

> "The tell that you should be using tools: if you're writing a regex to extract a decision from model output, that decision should have been a tool call. Parsing free-form text to recover structured intent is a sign the structure belongs in the schema."

**When not to use tools.** Model can answer from training alone (summarization, translation, general knowledge); one-shot Q&A with no side effects; tool-calling latency would dominate a trivial response.

**Choosing between approaches** (decision matrix):
- *User-defined client tools*: custom business logic, internal APIs, proprietary data—you handle execution + the agentic loop.
- *Anthropic-schema client tools*: standard dev operations (bash, file editing, browser control)—you handle execution; Claude calls reliably because the schema is trained-in.
- *Server-executed tools*: web search, code sandbox, web fetch—Anthropic handles execution; you get results directly.
