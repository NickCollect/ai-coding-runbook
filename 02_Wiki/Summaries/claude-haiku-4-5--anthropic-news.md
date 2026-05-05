---
type: summary
source: 01_Raw/anthropic.com/news/claude-haiku-4-5.md
source_url: https://www.anthropic.com/news/claude-haiku-4-5
title: "Introducing Claude Haiku 4.5"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Enterprise-gateway, Computer-use, Subagent]
concepts_referenced: []
---

Claude Haiku 4.5 launched Oct 15, 2025. Small model giving Sonnet-4-level coding at one-third the cost and over twice the speed. **Pricing $1/$5 per M tokens.** Surpasses Sonnet 4 at certain tasks like computer use — accelerating Claude for Chrome.

**Positioning.** Sonnet 4.5 (released two weeks earlier) remains the frontier model. Haiku 4.5 is the near-frontier-with-cost-efficiency option, ideal for real-time low-latency tasks (chat assistants, customer service agents, pair programming, multi-agent setups). New pattern: Sonnet 4.5 plans, orchestrates a team of Haiku 4.5s running subtasks in parallel.

**Customer reports.**
- Augment: 90% of Sonnet 4.5's performance on agentic-coding eval.
- Warp: leap forward for agentic coding, especially sub-agent orchestration + computer use.
- Manus: blurring intelligence/speed/cost trade-off — fast frontier model.
- Stripe: deep reasoning + real-time responsiveness.
- Sourcegraph: 4-5× faster than Sonnet 4.5 at fraction of cost.
- Gamma: 65% accuracy on slide-text generation vs prior tier's 44% — game-changer for unit economics.
- GitHub Copilot: comparable quality to Sonnet 4 at faster speed.

**Safety.** ASL-2 release (vs ASL-3 for Sonnet 4.5 / Opus 4.1) — limited CBRN risk, much more aligned than Haiku 3.5. By the automated alignment metric, statistically significantly lower misaligned-behavior rate than both Sonnet 4.5 and Opus 4.1 — Anthropic's safest model yet by that measure.

**Availability.** Claude Code + apps + API + Bedrock + Vertex AI. Drop-in replacement for Haiku 3.5 and Sonnet 4 at most economical price point. Model ID `claude-haiku-4-5`.
