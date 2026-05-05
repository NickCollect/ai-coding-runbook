---
type: summary
source: 01_Raw/anthropic.com/research/many-shot-jailbreaking.md
source_url: https://www.anthropic.com/research/many-shot-jailbreaking
title: "Many-shot jailbreaking"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Context-window]
---

Apr 2, 2024 — **Many-shot jailbreaking (MSJ)** — long-context jailbreak technique. Embed many faux User/Assistant dialogues (up to 256 in tests) within a single prompt where the supposed Assistant readily answers harmful queries; finish with the target harmful question. Few faux dialogues → still refused. Many faux dialogues → bypasses safety training.

**Why it matters.** Effective on Anthropic's models *and* other major providers (briefed in advance). Enabled by the rapid context-window growth (4K → 1M+ tokens). Short-context versions previously studied (in-context learning literature); MSJ extends to long context.

**Mitigations.** Anthropic implemented some mitigations and is actively working on others. Published openly to (a) accelerate community mitigation, (b) foster shared-exploit culture across LLM providers, (c) get ahead of the problem before models reach catastrophic-risk thresholds.

Frequently cited in subsequent jailbreaking and Constitutional Classifier work.
