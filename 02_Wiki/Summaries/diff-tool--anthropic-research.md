---
type: summary
source: 01_Raw/anthropic.com/research/diff-tool.md
source_url: https://www.anthropic.com/research/diff-tool
title: 'A "diff" tool for AI: Finding behavioral differences in new models'
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Mar 13, 2026 — Anthropic Fellows extends **model diffing** to its most general case: comparing models with entirely different architectures. Software analogue: programmers don't audit million-line codebases from scratch; they use diff to review only changed lines.

**Use cases (prior work).** Understanding how chat models change during fine-tuning; revealing hidden backdoors; finding undesirable emergent behaviors. New contribution: cross-architecture diffing.

**Caveats.** Not a silver bullet — single diff surfaces thousands of features, only a fraction may correspond to meaningful behavioral risks. Acts as high-recall screening tool for researcher attention. Among thousands of candidates, identified concepts that act as switches for specific behaviors. Reduces "auditing a model from scratch" to a more tractable problem.
