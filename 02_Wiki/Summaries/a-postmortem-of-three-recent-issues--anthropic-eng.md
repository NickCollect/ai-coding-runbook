---
type: summary
source: 01_Raw/anthropic.com/engineering/a-postmortem-of-three-recent-issues.md
source_url: https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues
title: "A postmortem of three recent issues"
summarized_at: 2026-05-05
entities_referenced: [Enterprise-gateway]
concepts_referenced: [Context-window]
---

Technical postmortem (Sep 17, 2025) on three overlapping infrastructure bugs that intermittently degraded Claude responses Aug-Sep 2025. Anthropic explicitly states: "We never reduce model quality due to demand, time of day, or server load."

**Bug 1 — Context-window routing error.** Aug 5: some Sonnet 4 requests were misrouted to servers configured for the upcoming 1M-token context-window. Initial impact 0.8%; an Aug 29 load-balancing change escalated this to 16% of Sonnet 4 requests at peak. ~30% of Claude Code users had at least one misrouted message. Routing was "sticky" — once misrouted, follow-ups stayed on the wrong server. Bedrock peak 0.18%, Vertex 0.0004%. Fixed Sep 4, fully rolled out Sep 18.

**Bug 2 — Output corruption.** Aug 25: a TPU-server misconfiguration caused a runtime perf optimization to occasionally assign high probability to tokens that should rarely appear (e.g. Thai/Chinese characters in English replies, syntax errors). Affected first-party Opus 4.1 / Opus 4 (Aug 25-28) and Sonnet 4 (Aug 25-Sep 2). Third-party platforms unaffected. Fixed Sep 2; added detection tests for unexpected character outputs.

**Bug 3 — Approximate top-k XLA:TPU miscompilation.** Aug 25: a token-selection improvement triggered a latent bug in the XLA:TPU compiler. Confirmed for Haiku 3.5; possibly affected a subset of Sonnet 4 / Opus 3. Deep dive: top-p sampling on TPUs uses bf16 for next-token probabilities but the vector processor is fp32-native; `xla_allow_excess_precision=true` caused mismatched precision between operations agreeing on the highest-probability token. A Dec 2024 workaround masked an underlying approximate-top-k bug. Aug 26 rewrite removed that workaround → exposed the deeper bug. Fix: switched to exact top-k with enhanced precision; standardized some ops on fp32 (accepted minor efficiency hit because "model quality is non-negotiable").

**Why detection was hard.** Privacy controls limit engineer access to user interactions, blocking reproduction. Different bugs produced different symptoms on different platforms at different rates → confusing reports. They relied too heavily on noisy evals; the Aug 29 load-balancing change wasn't connected to the spike in negative reports.

**Going forward.** Better monitoring tied to deploys, broader eval coverage, and a commitment to share more technical detail in postmortems like this.
