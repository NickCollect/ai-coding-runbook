---
type: summary
source: 01_Raw/anthropic.com/news/claude-opus-4-1.md
source_url: https://www.anthropic.com/news/claude-opus-4-1
title: "Claude Opus 4.1"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Enterprise-gateway, Extended-thinking]
concepts_referenced: []
---

Claude Opus 4.1 released Aug 5, 2025. Upgrade to Opus 4 on agentic tasks, real-world coding, and reasoning. Anthropic flagged "substantially larger improvements" coming in subsequent weeks (Sonnet 4.5 followed Sep 29).

**Performance.** State-of-the-art coding at **74.5% on SWE-bench Verified**. Improved deep-research and data-analysis skills, especially detail tracking and agentic search.

**Partner reports.**
- GitHub: improvements across most capabilities, particularly multi-file refactoring.
- Rakuten: pinpoints exact corrections in large codebases without unnecessary changes or bugs.
- Windsurf: 1 standard deviation improvement over Opus 4 on junior-developer benchmark — same magnitude leap as Sonnet 3.7 → Sonnet 4.

**Availability.** Paid Claude users + Claude Code + API + Amazon Bedrock + Google Cloud Vertex AI. Model ID `claude-opus-4-1-20250805`. Pricing unchanged from Opus 4 ($15/$75 per M tokens).

**Methodology notes.** Claude 4 family uses simple SWE-bench scaffold with two tools (bash + str-replace file editor) — no longer using the third "planning tool" from Claude 3.7 Sonnet. Reports scores out of full 500 problems (vs OpenAI's 477-problem subset). TAU-bench uses prompt addendum encouraging extended-thinking + tool use; max steps raised from 30 to 100 to accommodate reasoning. Benchmarks like SWE-bench/Terminal-Bench reported without extended-thinking; TAU-bench/GPQA/MMMLU/MMMU/AIME with up to 64K thinking tokens. Recommendation: upgrade from Opus 4 to Opus 4.1 for all uses.
