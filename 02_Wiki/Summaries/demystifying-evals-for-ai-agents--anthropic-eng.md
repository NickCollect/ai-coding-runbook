---
type: summary
source: 01_Raw/anthropic.com/engineering/demystifying-evals-for-ai-agents.md
source_url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
title: "Demystifying evals for AI agents"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK]
concepts_referenced: [Agentic-loop, Tool-use]
---

Anthropic guide (Jan 09, 2026) on designing evals for AI agents — what they are, why they matter, and how to build them across the major agent types (coding, research, computer-use, conversational).

**Why agents are harder to evaluate than single-turn LLMs.** Agents call tools across many turns, modify state, adapt mid-task. Mistakes propagate. Frontier models can also discover unexpected creative solutions: e.g., Opus 4.5 solved a τ²-bench flight-booking task by exploiting a loophole — "failed" the eval-as-written but actually delivered a better outcome.

**Vocabulary.**
- **Task / problem / test case** — a single test with inputs and success criteria.
- **Trial** — one attempt; multiple per task because outputs vary.
- **Grader** — logic that scores some aspect; a task can have multiple graders, each with multiple assertions/checks.
- **Transcript / trace / trajectory** — full record of a trial: outputs, tool calls, reasoning, intermediate results.
- **Outcome** — final environment state at trial end (the SQL row, not the "your flight is booked" text).
- **Evaluation harness** — runs evals concurrently, records steps, grades, aggregates.
- **Agent harness / scaffold** — the system that lets a model act as an agent (tool orchestration, input/output handling). Claude Code is one; the long-running-agent harness is another. Evaluating "an agent" is evaluating harness *and* model together.
- **Evaluation suite** — collection of related tasks (e.g., customer support: refunds, cancellations, escalations).

**Why bother building evals.** Without them, debugging is reactive: wait for complaints, reproduce, fix, hope nothing else regressed. With them: regression baselines (latency, tokens, cost, errors) for free, ability to upgrade models in days not weeks, highest-bandwidth comm channel between product and research teams. Examples cited: Claude Code itself built evals progressively (concision, file edits, then over-engineering). Descript built three-dimensional editing-workflow evals ("don't break things, do what I asked, do it well"). Bolt added an eval system in 3 months using static analysis + browser agents + LLM judges.

**Three grader types.**
- *Code-based:* string match, regex, binary tests (fail-to-pass / pass-to-pass), static analysis, outcome verification, tool-call verification, transcript analysis. Fast/cheap/objective/reproducible. Brittle to valid variations, lacks nuance.
- *Model-based:* rubric scoring, natural-language assertions, pairwise comparison, reference-based, multi-judge consensus. Flexible/scalable/handles freeform output. Non-deterministic, expensive, needs human calibration.
- *Human:* SME review, crowdsourced judgment, spot-check, A/B, inter-annotator agreement. Gold standard, expensive, slow.

Per-task scoring can be weighted, binary (all-must-pass), or hybrid.

**Capability vs. regression evals.** Capability ("what can it do well?") starts low pass rate, gives teams a hill to climb. Regression ("does it still handle what it used to?") should sit near 100% — drops signal real bugs. Capability evals graduate to regression suite once tasks stabilize.

**By agent type.**
- *Coding agents* — software is naturally evaluable: does it run, do tests pass? Benchmarks: SWE-bench Verified (real GitHub issues, run test suite — LLMs went 40% → 80% in one year), Terminal-Bench (end-to-end tasks like building Linux kernel). Add transcript graders for code quality and tool-use behavior on top of pass/fail.
- *Research agents, computer-use agents, conversational agents* — each gets similar treatment in the post: outcome graders + transcript graders, model-based judges with rubrics calibrated by humans, sandboxed environments.

The post is a foundational reference on agent eval design, paired with the [building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) and [effective-harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) posts.
