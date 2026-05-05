---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/command-development/references/advanced-workflows.md
title: "Advanced Workflow Patterns (command-development reference)"
summarized_at: 2026-05-05
entities_referenced: [Slash-command]
concepts_referenced: []
---

Reference doc from the `command-development` skill. Multi-step command sequences and composition patterns. Note: only first ~100 lines sampled — covers introductory patterns.

**Multi-step command patterns**:

**Sequential workflow command** — guides users through multi-step processes with numbered steps, embedded bash execution for context, decision points for user input, next-action suggestions. Example PR review workflow:
1. Step 1: fetch PR details via `!gh pr view $1 --json title,body,author,files`
2. Step 2: review files via `!gh pr diff $1 --name-only` then per-file checklist
3. Step 3: run checks via `!gh pr checks $1`
4. Step 4: provide feedback summary + decision menu (approve / request changes / leave comments)

**State-carrying workflow** — commands that maintain state across invocations by writing/reading `.claude/deployment-state.local.md` with YAML frontmatter (`initialized`, `branch`, `commit`, `timestamp`, `status`). Initial command writes state, follow-up commands (`/deploy-test`, `/deploy-build`, `/deploy-execute`) read it.

(Remaining content not sampled — likely covers more workflow patterns: composition, branching, parallel execution, error handling chains.)
