---
type: summary
source: 01_Raw/anthropic.com/engineering/building-effective-agents.md
source_url: https://www.anthropic.com/engineering/building-effective-agents
title: "Building effective agents"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, MCP-server]
concepts_referenced: [Agentic-loop, Tool-use]
---

Foundational Anthropic engineering post (Dec 19, 2024) on practical agent-building patterns. Headline finding from working with dozens of teams: the most successful LLM agent implementations use **simple, composable patterns** rather than complex frameworks. Start with the simplest solution; add complexity only when needed.

**Architectural distinction.** All LLM-orchestrated systems are "agentic systems," but split into:
- **Workflows** — LLMs and tools orchestrated through predefined code paths (predictable, consistent).
- **Agents** — LLMs dynamically direct their own processes and tool usage (flexible, model-driven, but trade latency/cost for performance).

For many applications, optimizing single LLM calls with retrieval and in-context examples is enough — no agent needed.

**Frameworks: caution.** Lists Claude Agent SDK, AWS Strands Agents SDK, Rivet, Vellum. They simplify low-level work (LLM calls, tool parsing, chaining) but add abstraction that obscures prompts/responses and tempts overengineering. Recommendation: start by calling the LLM API directly — many patterns are a few lines of code. If using a framework, understand the underlying code.

**Foundational building block: the augmented LLM** — an LLM with retrieval, tools, memory. Modern Claude actively uses these: generates own search queries, picks tools, decides what to retain. Suggests Model Context Protocol (MCP) as one integration approach.

**Workflow patterns** (with when-to-use guidance):
- **Prompt chaining** — sequence of LLM calls, each processing the previous output, with optional gate checks. For tasks cleanly decomposable into fixed subtasks (e.g., write outline → check criteria → write doc).
- **Routing** — classify input, dispatch to specialized prompts/models. Good for distinct categories (different customer-service intents; route easy queries to Haiku, hard ones to Sonnet).
- **Parallelization** — sectioning (independent subtasks in parallel) or voting (same task multiple times for confidence). Good for guardrails (one model answers, another screens), parallel evals, code-vulnerability review.
- **Orchestrator-workers** — central LLM dynamically breaks tasks down and delegates to worker LLMs. Subtasks are *not* pre-defined (key difference from parallelization). Good for coding (unknown number of file changes), complex search.
- **Evaluator-optimizer** — generator + critic loop. Good when criteria are clear and human-articulated feedback would help (literary translation, multi-round search).

**Agents** (covered later in the post): autonomous loops where the model plans, acts, observes, repeats, with environmental feedback (tool outputs, code execution results, human checkpoints). Use when problems are open-ended, steps are hard to predict in advance, you can trust the model's decision-making at scale, and you have ways to verify progress.

**Two domains where customers found particular value** (Appendix 1, referenced): customer support (clear success criteria, conversational flow, programmatic actions); coding agents (verifiable outputs via tests, well-defined problem scope, iterative refinement). The post became canonical reference; later expanded by [effective-context-engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) and [effective-harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) posts.
