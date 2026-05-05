---
type: summary
source: 01_Raw/anthropic.com/news/claude-3-7-sonnet.md
source_url: https://www.anthropic.com/news/claude-3-7-sonnet
title: "Claude 3.7 Sonnet and Claude Code"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, IDE-integration, Enterprise-gateway]
concepts_referenced: [Extended-thinking]
---

Feb 24, 2025 — **Claude 3.7 Sonnet** announced as Anthropic's most intelligent model to date and **first hybrid reasoning model on the market**. Both ordinary LLM and reasoning model in one — pick when Claude answers normally vs thinks longer. API users control the *thinking budget* (any N up to 128K output tokens). Same price as predecessors: $3 per M input / $15 per M output (including thinking tokens).

**Distinctive philosophy.** Reasoning is an integrated capability of the frontier model, not a separate model. Anthropic optimized less for math/CS competition problems, more for real-world business tasks. Standard mode = upgraded Claude 3.5 Sonnet; extended-thinking mode = self-reflects before answering. Same prompting works in both modes. Visible extended thinking exposed to users.

**Performance.** SOTA on SWE-bench Verified (real-world software issues) and TAU-bench (real-world tasks with user/tool interactions). Strong on coding and front-end web. Cursor: best-in-class real-world coding. Cognition: better than any other model at planning code changes. Vercel: exceptional precision for complex agent workflows. Replit: builds sophisticated web apps where other models stall. Canva: superior design taste, drastically reduced errors.

**Claude Code launched alongside** as limited research preview — Anthropic's first agentic coding tool, command-line. Active collaborator: search/read code, edit files, write/run tests, commit/push to GitHub, use CLI tools. Already indispensable for Anthropic's own team, especially TDD, complex debugging, large refactors. Tasks completed in single pass that would normally take 45+ min manual work.

**Other.** GitHub integration available on all Claude plans. 45% reduction in unnecessary refusals vs predecessor. System card covers RSP evals, computer-use prompt-injection risks, and reasoning-model safety benefits (transparency into model decision-making). Available on Claude (Free/Pro/Team/Enterprise), Developer Platform, Bedrock, Vertex AI; extended-thinking available everywhere except free tier.
