---
type: summary
source: 01_Raw/anthropic.com/news/3-5-models-and-computer-use.md
source_url: https://www.anthropic.com/news/3-5-models-and-computer-use
title: "Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku"
summarized_at: 2026-05-05
entities_referenced: [Computer-use, Messages-API, Enterprise-gateway]
concepts_referenced: [Tool-use]
---

Oct 22, 2024 — Three announcements:
1. **Upgraded Claude 3.5 Sonnet** with across-the-board gains, particularly in agentic coding. SWE-bench Verified 33.4% → 49.0% (highest of any publicly available model, including reasoning models like o1-preview). TAU-bench retail 62.6% → 69.2%, airline 36.0% → 46.0%. Same price/speed as predecessor.
2. **Claude 3.5 Haiku** — matches Claude 3 Opus on many evals, similar speed to prior Haiku. SWE-bench Verified 40.6%. Pricing later revised (Dec 3) to $0.80/$4 per M tokens. Released later in October as text-only with image input to follow.
3. **Computer use (public beta)** — Claude 3.5 Sonnet is **first frontier model with public-beta computer use**: looks at a screen, moves cursor, clicks, types. Works on real software (Chrome, LibreOffice, VS Code). On OSWorld, Claude 3.5 Sonnet scored **14.9% screenshot-only** (next-best AI: 7.8%); 22.0% with more steps. Anthropic taught general computer skills rather than purpose-built tools — same approach as humans use.

Early adopters: Asana, Canva, Cognition, DoorDash, Replit (using computer use for Replit Agent app evaluation), The Browser Company. Tasks span dozens to hundreds of steps.

**Safety.** Joint pre-deployment evals with US AISI and UK AISI. ASL-2 standard remains appropriate. Computer-use safety addressed via new classifiers that detect harmful usage; Anthropic acknowledges new vector for spam/misinformation/fraud. Available on API + Bedrock + Vertex AI.
