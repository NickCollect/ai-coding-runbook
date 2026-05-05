---
type: summary
source: 01_Raw/anthropic.com/research/measuring-agent-autonomy.md
source_url: https://www.anthropic.com/research/measuring-agent-autonomy
title: "Measuring AI agent autonomy in practice"
summarized_at: 2026-05-05
entities_referenced: [Permission-mode]
concepts_referenced: []
---

Feb 18, 2026 — Anthropic Societal Impacts study analyzing **how people grant autonomy to agents** in real-world Claude Code and public-API use. Used Clio over millions of human-agent interactions.

**Findings.**
- **Claude Code working autonomously for longer.** Among longest-running sessions, length nearly doubled in 3 months — from <25 min to >45 min. Smooth across model releases — suggests existing models are capable of more autonomy than they exercise.
- **Experienced users auto-approve more, interrupt more often.** New users: ~20% sessions in full auto-approve. Experienced: >40%.
- **Agent-initiated stops matter.** Claude Code stops to ask for clarification more than 2× as often as humans interrupt it on most-complex tasks.
- **Risky-domain usage is emerging but not yet at scale.** Most actions low-risk and reversible. Software engineering ~50% of agentic activity; emerging in healthcare, finance, cybersecurity.

**Methodological note.** Operationalized "agent" as "AI system equipped with tools that allow it to take actions" — focused on tools used. No reliable way to associate independent API requests into "sessions" — open challenge.

**Conclusion.** Effective oversight requires new post-deployment monitoring infrastructure + new human-AI interaction paradigms.
