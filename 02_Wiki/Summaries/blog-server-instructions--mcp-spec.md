---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/blog/content/posts/2025-11-03-using-server-instructions.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2025-11-03-using-server-instructions.md
title: "Blog post: Server Instructions — Giving LLMs a user manual for your server (2025-11-03)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Ola Hungerford (Maintainer) makes the case for **server instructions** — an underused MCP feature where the server returns prose context about how to use its tools, surfaced in `InitializeResult` and typically injected into the host's system prompt.

**Problem**: tools are like a workbench — LLMs can use them, but cross-tool relationships ("always use validate_schema → create_backup → migrate_schema for safe migrations"), rate limits, fallback patterns, and when to use elicitation aren't expressible in individual tool descriptions or prompts alone. Cramming everything into descriptions burns context tokens and overwhelms model attention.

**Implementation variability caveat**: not all hosts inject instructions into the system prompt — implementation is host-defined. Test before relying on it. **No instructions are better than poorly written instructions** because they may be injected without further filtering.

**Real-world example**: applied server instructions to the official GitHub MCP server. With the `pull_requests` toolset enabled, instructions push the model toward the optimal three-step PR review workflow (`create_pending_pull_request_review` → `add_comment_to_pending_review` → `submit_pending_pull_request_review`) instead of the simpler-but-worse single-step `create_and_submit_pull_request_review`. Code snippet shows toolset-conditional `GenerateInstructions` in Go.

**Quantitative results** (40 GitHub PR review sessions, 20 with / 20 without instructions): GPT-5-Mini went from 20% to 80% optimal-pattern adherence (+60%); Claude Sonnet-4 was already at 100% without instructions. Overall +25% improvement. Demonstrates instructions matter especially for models that don't naturally find the optimal pattern.

**Tips for server developers**: capture cross-feature relationships, document operational patterns (rate limits, caching), specify constraints, write model-agnostic instructions. **Anti-patterns**: don't repeat tool descriptions, don't include marketing claims, don't include unrelated behavioral instructions ("talk like a pirate"), don't write a 500-word manual.

**Limitations**: instructions can't guarantee behavior (LLM rolls dice), can't fix bad tool design, can't change model personality. Don't use for security-critical actions — those should be deterministic rules or hooks.

**Client implementer guidance**: expose instructions to users for transparency; allow review/enable/disable; document client behavior. Demo path uses the Everything reference server.
