---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/ralph-wiggum/README.md
title: "ralph-wiggum plugin README"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Slash-command, Hooks]
concepts_referenced: []
---

The `ralph-wiggum` plugin implements the Ralph Wiggum technique (Geoffrey Huntley's "Ralph is a Bash loop") — iterative self-referential AI development loops, but **inside the current Claude Code session** via a Stop hook (no external bash loops needed). Named after Ralph Wiggum from The Simpsons (persistent iteration despite setbacks).

**Mechanism** (`hooks/stop-hook.sh`): intercepts Claude's exit attempt → blocks exit → feeds same prompt back. Loop continues until Claude outputs the completion promise OR hits `--max-iterations`. Files persist between iterations; Claude reads modified files + git history to autonomously improve.

**Commands**:
- `/ralph-loop "<prompt>" --max-iterations <n> --completion-promise "<text>"` — start loop. Both options recommended; `--max-iterations` is the safety net.
- `/cancel-ralph` — cancel active loop.

Example:
```
/ralph-loop "Build a REST API for todos. Requirements: CRUD, validation, tests. Output <promise>COMPLETE</promise> when done." --completion-promise "COMPLETE" --max-iterations 50
```

**Prompt best practices**:
1. Clear completion criteria — list specific deliverables + completion promise.
2. Incremental phased goals — break complex tasks into Phase 1/2/3.
3. Self-correction — TDD-style: failing tests → implement → run → debug if fail → refactor → repeat → output completion.
4. Always set `--max-iterations` — `--completion-promise` uses exact string matching (single condition only); iterations limit is your real safety mechanism.

**Philosophy**: iteration > perfection; failures are data ("deterministically bad" = predictable + informative); operator skill matters (good prompts > magic model); persistence wins.

**Good for**: well-defined tasks with clear success criteria, iteration/refinement (test-pass loops), greenfield (walk-away tasks), tasks with auto-verification (tests/linters).

**Bad for**: tasks needing human judgment/design, one-shot operations, unclear success criteria, production debugging.

**Real-world results cited**: 6 repositories overnight in YC hackathon testing; one $50k contract for $297 API costs; entire programming language ("cursed") in 3 months.

References: original technique https://ghuntley.com/ralph/; Ralph Orchestrator https://github.com/mikeyobrien/ralph-orchestrator.
