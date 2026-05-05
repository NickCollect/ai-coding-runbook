---
type: summary
source: 01_Raw/anthropic.com/research/trustworthy-agents.md
source_url: https://www.anthropic.com/research/trustworthy-agents
title: "Trustworthy agents in practice"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Apr 9, 2026 — Anthropic Policy post on operationalizing the August 2025 trustworthy-agents framework. Five principles: keep humans in control, align with human values, secure agent interactions, maintain transparency, protect privacy.

**How agents work — four components.**
1. **Model** — intelligence; product of training process.
2. **Harness** — instructions and guardrails (e.g., "flag anything over $100", "never submit expenses without confirmation").
3. **Tools** — services/applications the model can use (email, calendar, expense system).
4. **Environment** — where the agent runs (Claude Code vs Cowork vs other), what files/websites/systems accessible.

Framing: most AI policy conversation centers on the model, but agent behavior depends on all four layers. A well-trained model can still be exploited via poorly configured harness, overly permissive tool, exposed environment. Safeguards must account for all four.

Walks through human-control / alignment / security examples drawn from Claude Cowork and Claude Code product decisions.
