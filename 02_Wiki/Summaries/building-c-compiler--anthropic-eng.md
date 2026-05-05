---
type: summary
source: 01_Raw/anthropic.com/engineering/building-c-compiler.md
source_url: https://www.anthropic.com/engineering/building-c-compiler
title: "Building a C compiler with a team of parallel Claudes"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Permission-mode]
concepts_referenced: [Agent-team, Agentic-loop, Context-window]
---

Nicholas Carlini (Anthropic Safeguards) describes "agent teams" — multiple Claude instances working in parallel on a shared codebase without active human intervention. Stress-test: 16 agents writing a Rust-based C compiler from scratch. Result over 2 weeks: nearly 2,000 Claude Code sessions, 2B input tokens, 140M output tokens, ~$20K total, producing a 100K-line compiler that builds bootable Linux 6.9 on x86, ARM, RISC-V — and can compile QEMU, FFmpeg, SQLite, Postgres, Redis. 99% pass rate on most compiler test suites including GCC torture test. Compiles and runs Doom.

**Long-running harness.** A bash `while true` loop calling `claude --dangerously-skip-permissions -p "$(cat AGENT_PROMPT.md)" --model claude-opus-X-Y` (resembling "Ralph-loop"). Each iteration picks up the next task; runs forever. Container, not host. Claude is told to break the problem into small pieces, track work, decide what to do next, and never stop. (Once Claude `pkill -9 bash`-d itself.)

**Parallelism via git locks.** Bare git repo on host; each agent gets a Docker container with the repo mounted at `/upstream`, clones into `/workspace`, pushes when done. Sync: each agent writes a lock file to `current_tasks/` (e.g. `parse_if_statement.txt`); git's atomicity forces collision losers to pick a different task. Frequent merge conflicts; Claude resolves them. No orchestration agent, no inter-agent comms beyond git.

**Lessons.**
- *Write extremely high-quality tests* — Claude solves what you measure; bad verifiers → wrong solutions. Continuous integration with strict regression enforcement was critical late-stage when new features kept breaking old ones.
- *Put yourself in Claude's shoes* — fresh container, no context. Maintain extensive READMEs and progress files updated frequently. Test output: ≤ a few lines stdout, log details to file. Logs use `ERROR <reason>` on one line for grep-friendliness. Pre-compute aggregate stats so Claude doesn't recompute.
- *Time blindness* — Claude can't tell time. Default `--fast` mode runs 1% or 10% deterministic-per-agent random sample so each VM identifies regressions but the team covers all files.
- *Make parallelism easy* — when many independent tests fail, parallelism is trivial. Linux-kernel compilation is one giant task, so initially all 16 agents hit the same bug. Fix: use GCC as known-good oracle, randomly compile most kernel files with GCC and only the rest with Claude's compiler; binary-search to localize remaining bugs. Then add delta-debugging for file-pair interactions.
- *Multi-role specialization* — one agent dedupes code, one improves compiler perf, one improves emitted-code perf, one critiques Rust design quality, one writes docs.

**Limitations.** No 16-bit x86 (calls out to GCC for real-mode). No assembler/linker — demo used GCC's. Not a drop-in replacement.

Framed as a capability benchmark across the Claude 4 series: Opus 4 barely produced a functional compiler; Opus 4.5 was the first to pass large test suites but couldn't build real projects; Opus 4.6 reaches Linux-kernel scale. The post is forward-looking — what current models *barely* do, future models will reliably do.
