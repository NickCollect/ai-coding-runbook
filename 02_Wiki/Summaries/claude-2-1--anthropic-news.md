---
type: summary
source: 01_Raw/anthropic.com/news/claude-2-1.md
source_url: https://www.anthropic.com/news/claude-2-1
title: "Introducing Claude 2.1"
summarized_at: 2026-05-05
entities_referenced: [Messages-API]
concepts_referenced: [Context-window, Tool-use]
---

Nov 21, 2023 — Claude 2.1 announced. Three headline improvements:

1. **200K-token context window** (industry first, up from 100K). ~150,000 words / 500+ pages. Use cases: entire codebases, S-1s, *The Iliad*. Long latency expected to decrease over time.
2. **2× decrease in hallucination rates** vs Claude 2.0. Tested on factual questions probing model weaknesses; 2.1 more likely to demur ("I don't know") than fabricate ("Montero is the fifth most populous city in Bolivia"). On document comprehension, 30% reduction in incorrect answers, 3-4× lower rate of mistakenly concluding a doc supports a claim.
3. **Tool use beta** — Claude can integrate with user APIs/processes, orchestrate developer-defined functions, search web sources, query private knowledge bases. Examples: calculator for numerical reasoning, NL → structured API calls, DB/web search Q&A, simple software actions, product recommendations.

System prompts also added. Available via Console API and powering claude.ai. Pricing updated alongside this release for cost efficiency.
