---
type: summary
source: 01_Raw/platform.claude.com/docs/en/intro.md
source_url: https://platform.claude.com/docs/en/intro
title: "Intro to Claude"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Managed-agent]
concepts_referenced: []
---

Top-level entry page for the platform.claude.com developer docs. Claude is described as "a highly performant, trustworthy, and intelligent AI platform built by Anthropic"—excels at language, reasoning, analysis, coding, and more. Built by Anthropic.

**Latest model generation called out:**
- **Claude Opus 4.7**: most capable model for complex reasoning and agentic coding, "a step-change jump over Claude Opus 4.6".
- **Claude Sonnet 4.6**: frontier intelligence at scale—built for coding, agents, and enterprise workflows.
- **Claude Haiku 4.5**: fastest model with near-frontier intelligence.

For chat with Claude, link to claude.ai.

**Two ways to build with Claude:**

| | [[Messages-API]] | [[Managed-agent]] |
|---|---|---|
| What it is | Direct model prompting access | Pre-built, configurable agent harness that runs in managed infrastructure |
| Best for | Custom agent loops and fine-grained control | Long-running tasks and asynchronous work |

**Recommended path for new developers (4 steps):**
1. *Make your first API call.* Set up environment, install SDK, send first message → get-started quickstart.
2. *Understand the Messages API.* Core request/response structure, multi-turn conversations, system prompts, stop reasons → working-with-messages guide.
3. *Choose the right model.* Compare models by capability and cost → models overview.
4. *Explore features and tools.* Extended thinking, web search, file handling, structured outputs → features overview.

**Develop with Claude—three primary tooling surfaces:**
- *Developer Console*: prototype/test prompts in browser with the Workbench and prompt generator.
- *API Reference*: full Claude API and client SDK documentation.
- *Claude Cookbook*: interactive Jupyter notebooks (PDFs, embeddings, etc.).

**Key capabilities** (linked but not detailed here):
- *Text and code generation*: summarize, answer questions, extract data, translate, explain/generate code.
- *Vision*: process visual input, generate text and code from images.

**Support resources:**
- Help Center (account, billing).
- Service Status (anthropic.status.com).

This page is purely a navigation hub—no API endpoints, no code examples, no parameters. Its function is to land new developers and route them either to the API guides (Messages-API path) or the Managed Agents path based on their use case.
