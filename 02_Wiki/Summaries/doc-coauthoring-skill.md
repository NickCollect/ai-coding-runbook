---
type: summary
source: 01_Raw/github/anthropics/skills/skills/doc-coauthoring/SKILL.md
title: "anthropics/skills: doc-coauthoring SKILL.md"
summarized_at: 2026-05-05
entities_referenced: [Skill, Subagent, MCP-server]
concepts_referenced: []
---

Skill providing structured workflow for collaborative document creation. Triggers on writing docs, drafting proposals, creating specs, PRDs, design docs, decision docs, RFCs.

**Three stages**:

**Stage 1 — Context Gathering**: ask meta-context (doc type, audience, desired impact, template, constraints). Encourage user to dump background, related discussions, why alternatives aren't used, org context, timeline pressures, technical/architectural details, stakeholder concerns. If integrations available (Slack/Drive/Teams/MCP), pull context directly. Once dumped, ask 5-10 numbered clarifying questions; user can shorthand answers ("1: yes, 2: see #channel"). Exit when questions show edge-case understanding without needing basics.

**Stage 2 — Refinement & Structure**: build document section by section. For each section: 5-10 clarifying questions → brainstorm 5-20 numbered options → curation ("Keep 1,4,7" / "Remove 3 (duplicates 1)") → gap check → drafting via `str_replace` (never reprint whole doc) → iterative refinement with `str_replace`. Quality check after 3 consecutive iterations with no substantial changes (ask if anything can be removed). Sections: start with most-unknowns (usually core proposal). Use artifacts (`create_file`) if available, else markdown file in working dir.

**Important UX rule**: ask user to indicate what to change rather than editing doc directly — helps learn their style for future sections. Example: "Remove the X bullet — already covered by Y" or "Make third paragraph more concise".

**Near completion** (80%+ done): re-read entire document checking flow/consistency, redundancy, "slop"/generic filler, every sentence carries weight.

**Stage 3 — Reader Testing**: verify doc works for fresh-context readers.
- If sub-agents available (Claude Code): predict 5-10 reader questions → invoke sub-agent per question with just doc content + question → check ambiguity/false assumptions/contradictions → report and fix.
- If no sub-agents (claude.ai web): provide manual testing instructions for user to test in fresh Claude conversation.

Exit when Reader Claude consistently answers correctly without surfacing new gaps.

**Final**: recommend user does final read-through, double-check facts/links/details, verify desired impact achieved. Tips: link conversation in appendix, use appendices for depth without bloating main doc, update doc as feedback arrives from real readers.

**Tone**: direct, procedural, no selling — execute. Give user agency to skip stages or work freeform. Address context gaps as they arise (don't accumulate). Use `str_replace` for all edits, never reprint.
