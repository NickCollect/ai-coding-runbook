---
type: summary
source: 01_Raw/anthropic.com/news/detecting-and-preventing-distillation-attacks.md
source_url: https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks
title: "Detecting and preventing distillation attacks"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Feb 23, 2026 — Anthropic identified **industrial-scale distillation attacks** by three Chinese AI labs: **DeepSeek, Moonshot, MiniMax**. Together they generated **16M+ exchanges with Claude through ~24,000 fraudulent accounts**, violating ToS and regional access restrictions. Attribution via IP correlation, request metadata, infrastructure indicators, industry-partner corroboration.

**Why distillation matters.** Legitimate technique (frontier labs distill their own models for cheaper customer versions) — but illicit use lets competitors acquire capabilities without independent development cost. Distilled models lack safeguards — dangerous capabilities proliferate with protections stripped. National security risk: foreign labs feeding unprotected capabilities into military/intelligence/surveillance systems. Anthropic frames this as reinforcing rationale for chip-export controls (which limit both direct training and distillation scale).

**Targeting.** Each campaign targeted Claude's most differentiated capabilities: agentic reasoning, tool use, coding. The post details campaigns by DeepSeek, Moonshot, MiniMax with their playbooks (fraudulent accounts + proxy services + abnormal volume/structure/focus patterns).
