---
type: summary
source: 01_Raw/anthropic.com/research/petri-open-source-auditing.md
source_url: https://www.anthropic.com/research/petri-open-source-auditing
title: "Petri: An open-source auditing tool to accelerate AI safety research"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Oct 6, 2025 — **Petri (Parallel Exploration Tool for Risky Interactions)** open-sourced. Automated agent that tests target AI systems through diverse multi-turn conversations involving simulated users and tools, then scores and summarizes target behavior.

**Process.** Researchers provide seed instructions in natural language describing scenarios; Petri operates each in parallel — auditor agent makes plan, interacts with target in tool-use loop. LLM judges score transcripts across multiple safety dimensions; surface most concerning for human review.

**Already used in production.** Claude 4 + Sonnet 4.5 system cards (situational awareness, whistleblowing, self-preservation behaviors). Head-to-head comparison with OpenAI. Alignment-auditing-agents research. UK AISI used pre-release version to test Sonnet 4.5.

**Pilot run.** 14 frontier models × 111 seed instructions covering: deception, sycophancy, encouragement of user delusion, cooperation with harmful requests. Designed to support both one-off exploration and systematic benchmarking.
