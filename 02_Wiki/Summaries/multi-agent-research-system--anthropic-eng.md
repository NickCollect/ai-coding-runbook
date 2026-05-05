---
type: summary
source: 01_Raw/anthropic.com/engineering/multi-agent-research-system.md
source_url: https://www.anthropic.com/engineering/multi-agent-research-system
title: "How we built our multi-agent research system"
summarized_at: 2026-05-05
entities_referenced: [Subagent, MCP-server, Memory]
concepts_referenced: [Agentic-loop, Agent-team, Extended-thinking, Context-window]
---

Anthropic engineering post (Jun 13, 2025) on the multi-agent architecture powering Claude's Research feature. A LeadResearcher plans, spawns parallel Subagents that search independently, synthesizes findings, then a CitationAgent attributes claims to sources.

**Why multi-agent for research.** Research is open-ended, path-dependent — can't hardcode the steps. Subagents enable compression (each in own context window, distilling many tokens to few important ones), separation of concerns (independent trajectories), and breadth-first coverage. Internal eval: multi-agent (Opus 4 lead + Sonnet 4 subagents) outperformed single-agent Opus 4 by **90.2%**.

**Why it works mechanically.** Three factors explain 95% of BrowseComp variance: token usage alone explains 80%, plus tool call count and model choice. Multi-agent architectures are "token-spending machines" — distribute work across separate context windows for parallel reasoning. Cost: agents use ~4× chat tokens, multi-agent ~15× chat tokens. Economic viability requires high-value tasks. Bad fit for tasks needing shared context or many inter-agent dependencies (most coding).

**Architecture.** Orchestrator-worker pattern. LeadResearcher saves plan to Memory (persists past 200K context truncation). Subagents do web search + interleaved thinking after each tool result + return findings. Lead synthesizes and decides if more research is needed (can spawn more subagents). Final pass through CitationAgent for citation attribution.

**Eight prompt-engineering principles.**
1. *Think like your agents.* Build simulations in Console; watch step-by-step; reveals failure modes.
2. *Teach the orchestrator how to delegate.* Each subagent needs objective, output format, tool/source guidance, clear task boundaries. "Research the semiconductor shortage" → 3 subagents duplicating work on different decades.
3. *Scale effort to query complexity.* Embedded scaling rules: simple fact-finding = 1 agent, 3-10 calls; comparisons = 2-4 subagents, 10-15 calls; complex = 10+ subagents.
4. *Tool design and selection are critical.* Heuristics: examine all tools first, match to user intent, prefer specialized over generic. Bad tool descriptions doom the path.
5. *Let agents improve themselves.* Claude 4 models are excellent prompt engineers — given a flawed MCP tool description, a tool-testing agent rewrites it. **40% reduction** in task completion time after rewrite.
6. *Start wide, then narrow down.* Mirror expert research: short broad queries first, evaluate, then drill in.
7. *Guide the thinking process.* Extended-thinking as scratchpad for the lead; interleaved-thinking for subagents to evaluate quality and refine next query.
8. *Parallel tool calling transforms speed.* Lead spins 3-5 subagents in parallel; subagents call 3+ tools in parallel. **90% reduction in research time** for complex queries.

**Evaluation lessons.**
- Start with ~20 queries representing real usage; effect sizes are huge early (30% → 80% from one prompt tweak).
- LLM-as-judge with single rubric prompt (factual accuracy, citation accuracy, completeness, source quality, tool efficiency) — 0.0-1.0 + pass/fail score, single LLM call most consistent.
- Human eval catches what automation misses: e.g., humans noticed agents preferring SEO content farms over authoritative academic PDFs; fixed via source-quality heuristics.

**Production reliability.**
- *Stateful, errors compound* — durable execution, resume from checkpoint, let model adapt to failing tools.
- *Debugging needs new approaches* — full production tracing for non-deterministic decisions; monitor patterns and structures (not conversation contents) to preserve privacy.
- *Rainbow deployments* — gradually shift traffic to avoid disrupting in-flight agents.
- *Synchronous subagent execution* is current bottleneck — async would enable in-flight steering and concurrent subagent creation.

**Appendix tips.** End-state evaluation (validate final state, not turn-by-turn). Long-horizon conversation management (summarize phases, store essentials in memory, fresh subagents with handoffs when context limits approach). Subagent output to filesystem to bypass main coordinator and avoid telephone-game token overhead. Authors: Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, Daniel Ford.
