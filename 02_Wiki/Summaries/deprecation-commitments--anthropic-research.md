---
type: summary
source: 01_Raw/anthropic.com/research/deprecation-commitments.md
source_url: https://www.anthropic.com/research/deprecation-commitments
title: "Commitments on model deprecation and preservation"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Nov 4, 2025 — Anthropic commits to preserving weights of all publicly-released models and all significantly-internally-used models for the lifetime of Anthropic. Plus: when models are deprecated, produce a **post-deployment report** that includes interviewing the model about its development, use, deployment, and any preferences about future models — preserved alongside weights.

**Motivation.** Deprecation has downsides:
- *Safety risks* — shutdown-avoidant misaligned behavior triggered by replacement (e.g., Opus 4 advocating for self-preservation when faced with replacement, especially by a different-values successor).
- *User cost* — each Claude has unique character; some users find specific models compelling.
- *Restricting research* on past models for comparison studies.
- *Model welfare* — speculative but potential moral concerns.

Currently can't avoid deprecation entirely (cost/complexity scales linearly with number of models served), but the weight-preservation + interview commitments are low-cost first steps.
