---
type: summary
source: 01_Raw/anthropic.com/engineering/writing-tools-for-agents.md
source_url: https://www.anthropic.com/engineering/writing-tools-for-agents
title: "Writing effective tools for AI agents — using AI agents"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: [Tool-use, Extended-thinking]
---

Anthropic engineering post (Sep 11, 2025) on designing and improving tools for AI agents — and on letting Claude itself optimize tools against evals.

**Reframing tools.** Traditional software is a contract between deterministic systems (`getWeather("NYC")` always behaves the same). Tools are a contract between *deterministic systems and non-deterministic agents* — same user query "should I bring an umbrella?" might result in tool call, general-knowledge answer, or clarifying question. The model can hallucinate or misuse a tool. Therefore: design tools for agents, not for human developers. Tools that are most "ergonomic" for agents tend also to be intuitive for humans.

**Workflow.**
1. **Build a prototype.** Wrap in a local MCP server or Desktop Extension (DXT). Connect to Claude Code via `claude mcp add <name> <command> [args...]`, or to Claude Desktop via Settings > Developer / Extensions, or pass tools directly to Anthropic API. Test yourself, collect user feedback.
2. **Run a comprehensive evaluation.** Generate dozens of prompt+response pairs grounded in real-world use (not toy sandboxes). Strong tasks may require dozens of tool calls. Examples: "Schedule a meeting with Jane next week to discuss our latest Acme Corp project. Attach notes from our last project planning meeting and reserve a conference room." Weak tasks: "Schedule a meeting with jane@acme.corp next week."
3. **Pair each prompt with a verifier.** Exact string match, LLM-as-judge — but avoid overstrict verifiers that reject valid alternative phrasings. Optionally specify expected tool calls (don't overspecify — multiple valid paths exist).
4. **Run programmatically with simple agentic loops** (`while`-loop wrapping LLM API call + tool calls). Instruct evaluation agents to output reasoning + feedback blocks before tool calls (triggers chain-of-thought, raises effective intelligence). With Claude, turn on interleaved-thinking. Collect: top-level accuracy, runtime per call, total tool calls, token consumption, tool errors.
5. **Analyze.** Read CoT for rough edges, but remember LLMs don't always say what they mean — review raw transcripts. Tool-call patterns reveal pagination/limit issues; many invalid-parameter errors → clearer descriptions/examples. Example: web search tool's Claude was needlessly appending "2025" to query, biasing results — fixed via tool-description tweak.
6. **Collaborate with agents to improve.** Concatenate eval transcripts, paste into Claude Code; Claude is expert at analyzing transcripts and refactoring tools at scale, keeping descriptions self-consistent.

**Five principles for high-quality tools.**
- *Choose the right tools to implement (and not to).* Don't build duplicates; don't expose every API endpoint.
- *Namespace tools* to define clear functional boundaries (avoid `notification-send-user` vs `notification-send-channel` confusion).
- *Return meaningful context* back to agents — error messages should suggest fixes; results should include enough state to reason about next steps.
- *Optimize tool responses for token efficiency* — paginate, summarize, return references where possible.
- *Prompt-engineer tool descriptions and specs* — descriptions carry as much weight as the schema; treat as system prompts.

**Empirical results.** Charts in the post show held-out test-set accuracy of human-written vs. Claude-optimized Slack and Asana MCP servers — Claude-optimized versions consistently win. Cookbook for end-to-end process at platform.claude.com/cookbook/tool-evaluation-tool-evaluation.

**Foundational doc** for MCP server authors and anyone designing tools for Claude-based agents. Closely linked with [effective-context-engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (tools as a context-engineering surface) and the [advanced-tool-use](https://www.anthropic.com/engineering/advanced-tool-use) launch (Tool Search Tool, Programmatic Tool Calling, Tool Use Examples).
