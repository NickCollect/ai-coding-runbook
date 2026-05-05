---
type: summary
source: 01_Raw/github/anthropics/skills/skills/internal-comms/SKILL.md
title: "Skill: internal-comms"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Skill from `anthropics/skills`. Triggers when user asks for any internal company communication: 3P updates (Progress/Plans/Problems), company newsletters, FAQs, status reports, leadership updates, project updates, incident reports.

**Workflow**:
1. Identify communication type from request
2. Load the appropriate guideline file from `examples/`:
   - `3p-updates.md` — Progress/Plans/Problems team updates
   - `company-newsletter.md` — company-wide newsletters
   - `faq-answers.md` — FAQ responses
   - `general-comms.md` — anything else
3. Follow specific instructions in that file for formatting, tone, content gathering

If communication type doesn't match any guideline, ask for clarification.

**Keywords** (for triggering): 3P updates, company newsletter, company comms, weekly update, faqs, common questions, updates, internal comms.

Demonstrates the **dispatch-by-type-to-reference-file** pattern — SKILL.md is a thin router; per-type detail lives in `examples/` (loaded only when matched).
