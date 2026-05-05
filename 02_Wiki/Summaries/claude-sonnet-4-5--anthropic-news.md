---
type: summary
source: 01_Raw/anthropic.com/news/claude-sonnet-4-5.md
source_url: https://www.anthropic.com/news/claude-sonnet-4-5
title: "Introducing Claude Sonnet 4.5"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Agent-SDK, Checkpointing, IDE-integration, Memory, Computer-use, Context-editing]
concepts_referenced: []
---

Claude Sonnet 4.5 launched Sep 29, 2025. Best coding model in the world; strongest model for building complex agents; best at using computers; substantial gains in reasoning and math. Most aligned frontier model Anthropic has released. Same pricing as Sonnet 4 — $3/$15 per M tokens.

**Released alongside the model:**
- **Claude Code checkpoints** — saves progress, instant rollback (one of most-requested features).
- Refreshed terminal interface; native VS Code extension.
- API: **context editing** + **memory tool** — agents run longer, handle more complexity.
- Apps: code execution + file creation (spreadsheets, slides, docs) directly in conversation.
- **Claude for Chrome** extension available to Max users from waitlist.
- **Claude Agent SDK** — same infrastructure powering Claude Code now exposed to developers ("the building blocks we use ourselves").

**Performance.** State-of-the-art on SWE-bench Verified. **OSWorld 61.4%** (vs Sonnet 4's 42.2% four months earlier). Sustained focus for **30+ hours** on complex multi-step tasks. Domain experts in finance/law/medicine/STEM saw dramatic improvements vs Opus 4.1.

**Customer reports.**
- Cursor: SOTA coding performance, especially on longer-horizon tasks.
- GitHub Copilot: "amplifies core strengths," big gains on multi-step reasoning + code comprehension.
- HackerOne (Hai security agents): vulnerability intake time -44%, accuracy +25%.
- Harvey (legal): SOTA on most complex litigation tasks.
- Augment Code: 9% → 0% error rate on internal code-editing benchmark vs Sonnet 4.

**Availability.** Everywhere; model ID `claude-sonnet-4-5`.
