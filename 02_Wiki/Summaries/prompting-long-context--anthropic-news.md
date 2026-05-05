---
type: summary
source: 01_Raw/anthropic.com/news/prompting-long-context.md
source_url: https://www.anthropic.com/news/prompting-long-context
title: "Prompt engineering for Claude's long context window"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Context-window]
---

Sep 23, 2023 — Quantitative case study on two prompting techniques to improve Claude's recall over long (100K-token) contexts:

1. **Extracting reference quotes** relevant to the question before answering.
2. **Supplementing the prompt with examples** of correctly answered questions about other sections of the document.

Methodology: built a "randomized collage" of multiple-choice Q&A from a post-training-cutoff government document. Used Claude to generate questions (with hand-written few-shot examples to avoid pitfalls — questions answerable from training, token-counting questions, hint-leaking answers, ambiguous "this document" references). Foundational early Anthropic guidance for working with long context windows; many of the techniques later codified in the docs.
