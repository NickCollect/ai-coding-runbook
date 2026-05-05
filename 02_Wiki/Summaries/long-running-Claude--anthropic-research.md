---
type: summary
source: 01_Raw/anthropic.com/research/long-running-Claude.md
source_url: https://www.anthropic.com/research/long-running-Claude
title: "Long-running Claude for scientific computing"
summarized_at: 2026-05-05
entities_referenced: [Skill, Subagent]
concepts_referenced: [Agent-team]
---

Mar 23, 2026 — Anthropic Discovery team researcher Siddharth Mishra-Sharma describes applying multi-day agentic coding workflows to scientific computing. Concrete example: using Claude Opus 4.6 to **implement a differentiable cosmological Boltzmann solver** ([clax](https://github.com/smsharma/clax) on GitHub) — a JAX implementation predicting Cosmic Microwave Background statistical properties.

**Why hard.** Boltzmann solvers (CLASS, CAMB) are core cosmology infrastructure; a differentiable version (months-to-years of researcher time for groups with full domain expertise) enables gradient-based parameter inference. The author has only high-level domain familiarity.

**Key differences from C-compiler project.** Not parallel-farmable — Boltzmann solver is a deeply coupled pipeline (small numerical errors propagate). Better suited to a single agent working sequentially with subagents and reference-implementation bisection.

**Pattern.**
- *CLAUDE.md* with overall plan and design decisions; Claude treats specially, can edit as it works.
- Set high-level goals (full feature parity with CLASS, fully differentiable, 0.1% accuracy target — typical CLASS-vs-CAMB agreement).
- *CHANGELOG.md* as portable long-term memory (lab notes); Claude instructed in CLAUDE.md to maintain it.
- Run on HPC SLURM cluster, but pattern is environment-agnostic.

Frames a model where scientists shift from conversational tight-leash loops to specifying high-level objectives and unleashing autonomous agent teams.
