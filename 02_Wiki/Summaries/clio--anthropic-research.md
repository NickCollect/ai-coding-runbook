---
type: summary
source: 01_Raw/anthropic.com/research/clio.md
source_url: https://www.anthropic.com/research/clio
title: "Clio: A system for privacy-preserving insights into real-world AI use"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Dec 12, 2024 — **Clio** (Claude insights and observations) — automated tool for privacy-preserving analysis of real-world Claude usage. Powers Anthropic's many "how people use Claude" studies; enables bottom-up pattern discovery (vs traditional top-down red-teaming).

**Process.** All powered by Claude (not human analysts):
1. Extract facets (topic, turn count, language) from each conversation.
2. Semantic clustering by theme.
3. Cluster description (excludes private details).
4. Hierarchy building for interactive exploration.

**Privacy-first defense in depth.** Claude instructed to exclude private details when extracting; minimum-user-count threshold so low-frequency topics can't be exposed; final Claude verification check that summaries don't contain identifying info.

**Top use cases on Claude.ai (1M conversation analysis).** "Web and mobile application development" >10% of conversations. Educational uses >7%. Business strategy/operations ~6%.

Foundational tool referenced across nearly every "usage analysis" Anthropic post (values-wild, election analysis, support/advice/companionship, threat-intelligence reports).
