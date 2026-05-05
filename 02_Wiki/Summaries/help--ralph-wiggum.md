---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/ralph-wiggum/commands/help.md
title: "/ralph-wiggum:help (plugin slash command)"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Hooks, Plugin]
concepts_referenced: []
---

Help command for the `ralph-wiggum` plugin — implements the **Ralph Wiggum technique** (continuous AI loops, pioneered by Geoffrey Huntley). The same prompt is fed to Claude repeatedly; "self-referential" aspect comes from Claude seeing its own previous work in files + git history (NOT from feeding output back as input).

**Core concept**:
```bash
while :; do
  cat PROMPT.md | claude-code --continue
done
```

**Each iteration**: Claude receives same prompt → works/modifies files → tries to exit → Stop hook intercepts and feeds same prompt → Claude sees previous work → iteratively improves until completion.

Tagline: "deterministically bad in an undeterministic world" — failures are predictable, enabling systematic improvement through prompt tuning.

**Commands**:
- `/ralph-loop <PROMPT> [--max-iterations <n>] [--completion-promise <text>]` — start a Ralph loop. Examples: `/ralph-loop "Refactor the cache layer" --max-iterations 20`, `/ralph-loop "Add tests" --completion-promise "TESTS COMPLETE"`. Mechanics: creates `.claude/.ralph-loop.local.md` state file → user works → on exit attempt, stop hook intercepts → same prompt fed back → Claude sees prior work → continues until promise detected or max iterations.
- `/cancel-ralph` — removes the loop state file, reports cancellation with iteration count.

**Completion signal**: Claude must output `<promise>TASK COMPLETE</promise>` (or whatever phrase). Stop hook looks for `<promise>` tag. Without it OR `--max-iterations`, Ralph runs infinitely.

**Self-reference mechanism**: NOT Claude talking to itself. Same prompt repeated; Claude's work persists in files; each iteration sees previous attempts; builds incrementally.

**When to use**: well-defined tasks with clear success criteria, tasks needing iteration/refinement, iterative development with self-correction, greenfield projects.

**Not for**: tasks needing human judgment/design decisions, one-shot operations, unclear success criteria, debugging production issues.

**Refs**: original technique <https://ghuntley.com/ralph/>, Ralph Orchestrator <https://github.com/mikeyobrien/ralph-orchestrator>.
