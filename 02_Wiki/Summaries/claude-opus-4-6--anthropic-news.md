---
type: summary
source: 01_Raw/anthropic.com/news/claude-opus-4-6.md
source_url: https://www.anthropic.com/news/claude-opus-4-6
title: "Introducing Claude Opus 4.6"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Compaction, Adaptive-thinking, Effort, Agent-team, Context-window]
concepts_referenced: []
---

Claude Opus 4.6 announced Feb 5, 2026. Smartest model upgrade focused on coding (planning, sustaining agentic tasks, larger codebases, code review/debugging skills). **First Opus-class model with a 1M-token context window in beta.**

**Benchmarks.**
- State-of-the-art on **Terminal-Bench 2.0** (agentic coding).
- Leads all frontier models on **Humanity's Last Exam** (multi-disciplinary reasoning).
- On **GDPval-AA** (real-world economically valuable knowledge work — finance, legal, etc.) outperforms next-best industry model GPT-5.2 by ~144 Elo points and Opus 4.5 by 190 Elo.
- Best on **BrowseComp** (hard-to-find online info).

**Safety profile** — as good or better than any frontier model; low rates of misaligned behavior across evaluations. Full system card published.

**Product-side launches with the model.**
- **Claude Code**: assemble *agent teams* to work on tasks together.
- **API**: *compaction* (auto context summarization for long-running tasks); *adaptive thinking* (model picks contextual cues for how much extended thinking to use); new *effort* controls.
- **Claude in Excel**: substantial upgrades.
- **Claude in PowerPoint**: research preview release.
- Default effort for Opus 4.6: high (recommend dialing to medium if overthinking; controlled via `/effort`).

**Availability.** claude.ai + API + all major cloud platforms. Model ID `claude-opus-4-6`. Pricing unchanged: $5/$25 per M tokens. Cowork now uses Opus 4.6 for autonomous multitasking.

**Partner quotes.** Notion: "strongest model Anthropic has shipped." GitHub: unlocking long-horizon coding workflows. Replit: huge leap for agentic planning, parallel tools/subagents. Asana: best for navigating large codebases. Cognition: increased Devin Review bug-catching rates.
