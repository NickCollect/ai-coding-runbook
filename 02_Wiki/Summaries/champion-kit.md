---
type: summary
source: 01_Raw/code.claude.com/docs/en/champion-kit.md
source_url: https://code.claude.com/docs/en/champion-kit
title: "Champion kit"
summarized_at: 2026-05-05
entities_referenced: [Skill, Memory, Hooks, Permission-mode]
concepts_referenced: []
---

Playbook for individual engineers advocating Claude Code internally. Three behaviors: (1) share what you discover, (2) be the person people ask, (3) grow the circle.

**Time budget** (intended to be sustainable, ~40min/wk):
- Posting wins: ~15 min/wk (screenshot + 1-2 sentences)
- Public Q&A: ~20 min/wk (answer once, link back when recurring)
- Weekly show-and-tell thread: ~5 min
- Optional pairing: 0-30 min (offer Quickstart link first)

**What to share**: reusable techniques, not status updates. Examples: `@-mention a directory` to surface missing tests; **plan mode** (`Shift+Tab` cycles into it) shows files-to-touch before edit; **Stop hook** for desktop notification on long-task completion; `/init` to generate `CLAUDE.md`. Format: screenshot + 1 line of context.

**Where to share**: `#claude-code` channel, PR descriptions, standups, team wiki.

**Q&A approach**: respond with the actual prompt used, not an explanation. Point at the feature ("Try plan mode, press `Shift+Tab` until you see it") rather than the doc link.

**Common questions** with suggested responses:
- "What to try first" → real but contained task; tedious bug/chore. → `/en/common-workflows`
- "How to trust it with my code" → plan mode; nothing modified until approved. → `/en/permissions`
- "It produced incorrect result" → paste the failure back to Claude (error message, failing test).
- "Doesn't understand our conventions" → run `/init`, populate `CLAUDE.md`. → `/en/memory`
- "Just autocomplete?" → live demo: explain unfamiliar file, trace bug across services, draft migration.
- "Security/data handling?" → defer to admin; don't improvise.

**Patterns to grow adoption**:
- Dedicated `#claude-code` channel; pin Quickstart + one strong example
- Weekly Friday "What did Claude help you with?" thread
- Share custom skills (`.claude/skills/<name>/SKILL.md`, e.g., `/ship` running tests + lint)
- `/team-onboarding` command scans recent sessions/commands/MCP servers and produces a guide newcomers can paste as their first message
- 15-min pairing on first task
- Identify next champion (usually whoever asks the most questions)

**30-day playbook**: Week 1 seed channel + post examples. Week 2 weekly thread + share one skill. Week 3 pair sessions + pinned FAQ. Week 4 hand off — channel answered by people other than you = role done.

**Quick-reference techniques**: provide context (`@file`, `@dir/`, paste errors); plan mode (`Shift+Tab`); `/init` + CLAUDE.md; reusable workflow as `SKILL.md`; Stop hook for long-task notification; recover by pasting failing test back; keep edits surgical ("only change X" or ask for diff).
