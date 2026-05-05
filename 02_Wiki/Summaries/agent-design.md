---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/agent-design.md
title: "Agent Design Patterns (claude-api shared)"
summarized_at: 2026-05-05
entities_referenced: [Skill, MCP-server]
concepts_referenced: [Tool-use, Extended-thinking, Context-window, Prompt-caching, Agentic-loop]
---

Decision heuristics for building agents on the Claude API. Note: only first ~80 lines sampled — full file covers context management, parallelization, caching strategies.

**Model parameters**:
- **Adaptive thinking** (`thinking: {type: "adaptive"}`): Claude controls when/how much to think; auto-interleaves between tool calls; no token budget to tune
- **Effort** (`output_config: {effort: ...}`): tradeoff thoroughness vs token efficiency. Lower → fewer/consolidated tool calls, less preamble. `medium` balanced; `max` when correctness > cost

**Designing tool surface — Bash vs dedicated tools**:
- Bash gives broad leverage but harness only sees opaque command string
- Dedicated tool = action-specific hook with typed args harness can intercept/gate/render/audit
- **Promote to dedicated tool when**: security boundary (gate hard-to-reverse actions like `send_email`), staleness checks (edit can reject if file changed since read), rendering (custom UI), scheduling (mark parallel-safe so harness can parallelize)
- **Rule of thumb**: start with bash for breadth; promote when need to gate, render, audit, or parallelize

**Anthropic-provided tools**:
- **Bash** (client) — Claude emits, harness executes; reference impl provided
- **Text editor** (client) — view/create/edit files
- **Computer use** (client OR server) — GUI/web/visual; self-hosted env or Anthropic-hosted
- **Code execution** (server) — sandbox container with built-in file + bash sub-tools
- **Web search / fetch** (server) — Anthropic executes, returns with citations
- **Memory** (client) — `/memories` directory, you implement storage backend

Client-side: Anthropic defines (name/schema/usage), your harness executes (reference impl provided). Server-side: declared in `tools`, runs entirely on Anthropic infra.

**Programmatic tool calling (PTC)**: Claude composes calls into a script that runs in code execution container. Tool calls pause script, execute (client or server), return result to running code (NOT to Claude's context). Final output only returns to Claude. Token cost scales with final output, not intermediates. Use when many sequential calls or large intermediate results.

**Scaling tool/instruction set**:
- **Tool search** — many tools, only few relevant per request; load schemas on demand. Tool definitions appended (preserves cache)
- **Skills** — task-specific instructions loaded only when relevant (folder with SKILL.md; description in context, full file read on demand)

**Long-running agents — managing context**:
- **Context editing** — old tool results / completed thinking cleared based on configurable thresholds
- **Compaction** — earlier context summarized server-side into compaction block

(Remainder covers cache strategy, more patterns — not sampled.)
