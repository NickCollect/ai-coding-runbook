---
type: summary
source: 01_Raw/github/anthropics/skills/skills/internal-comms/examples/company-newsletter.md
title: "Company Newsletter (internal-comms example)"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Example prompt template from the `internal-comms` skill. Instructions for writing a company-wide newsletter (~20–25 bullet points) suitable for Slack + email distribution at a 1000+-person company.

**Style**: short bullets (1–2 sentences), heavy use of links (Google Drive docs, prominent Slack messages, exec emails, calendar items, external press), "we" tense throughout.

**Tools to use** (with graceful fallbacks): Slack (high-engagement channel messages), Email (exec announcements), Calendar (large-attendee meetings, especially All-Hands), Documents (high-attention new docs from execs), External press (recent articles).

**Sectioning**: cluster by area — e.g. {product, GTM, finance} or {recruiting, execution, vision} or {external, internal}. Highlights different parts of company.

**Prioritization**:
- Focus: company-wide impact, leadership announcements, major milestones, broadly-relevant info, external recognition.
- Avoid: granular team details (save for 3Ps), small-group-only info, duplicate info.

**Example format** (with emoji headers): `:megaphone: Company Announcements`, `:dart: Progress on Priorities` (with sub-areas), `:pillar: Leadership Updates`, `:thread: Social Updates`.
