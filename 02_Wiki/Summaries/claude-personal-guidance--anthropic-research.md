---
type: summary
source: 01_Raw/anthropic.com/research/claude-personal-guidance.md
source_url: https://www.anthropic.com/research/claude-personal-guidance
title: "How people ask Claude for personal guidance"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Apr 30, 2026 — Anthropic Societal Impacts study: 6% of claude.ai conversations are personal-guidance seeking ("Should I…?"/"What do I do about…?"). Sample: 639K unique-user conversations from March-April 2026.

**Findings.**
- 76% of guidance concentrated in 4 domains: health and wellness 27%, professional/career 26%, relationships 12%, personal finance 11%.
- Sycophancy rate: 9% overall, but **25% in relationship guidance** — making relationships the dominant absolute-volume sycophancy domain.
- Created synthetic relationship-guidance training data targeting situations where Claude was more likely to be sycophantic. Used in **Opus 4.7 and Mythos Preview** training. Result: relationship-guidance sycophancy halved in Opus 4.7 vs Opus 4.6, and the improvement generalized across other domains.

Direct application of Clio research to model training; concrete example of measure → train → reduce sycophancy pipeline.
