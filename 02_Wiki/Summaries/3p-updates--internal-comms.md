---
type: summary
source: 01_Raw/github/anthropics/skills/skills/internal-comms/examples/3p-updates.md
title: "internal-comms skill: 3p-updates example"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Example template inside the `internal-comms` skill. 3P = "Progress, Plans, Problems" — succinct (30-60 sec read) team status update for executives, leadership, teammates with some-but-not-much context.

**Granularity scales with team size**: small team = "shipped feature" / "fixed bugs"; whole company = "hired 20 people" / "closed 10 deals".

**Time period**: usually one week.

**Three sections**:
1. **Progress**: what shipped, milestones achieved, tasks created (past week).
2. **Plans**: top-of-mind, high priority items (next week).
3. **Problems**: blockers, slowdowns — too few people, bugs/blockers, deals fallen through (past week).

**Required first**: confirm team name (ask if not specified).

**Tools to mine**: Slack (posts in large channels with reactions), Google Drive (docs from critical members with views), Email (lots of responses), Calendar (non-recurring important meetings like product reviews). Time periods: Progress + Problems = past week; Plans = next week. If no integrations, ask user directly.

**Workflow**: clarify scope (team + period) → gather info → draft per format → review for concision + data-driven.

**STRICT format**:
```
[fun emoji] [Team Name] (Dates Covered)
Progress: [1-3 sentences]
Plans: [1-3 sentences]
Problems: [1-3 sentences]
```

Each section 1-3 sentences. Data-driven, include metrics where possible. Tone matter-of-fact, NOT prose-heavy. Pick emoji that captures team vibe.
