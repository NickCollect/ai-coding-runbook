---
type: summary
source: 01_Raw/anthropic.com/research/values-wild.md
source_url: https://www.anthropic.com/research/values-wild
title: "Values in the wild: Discovering and analyzing values in real-world language model interactions"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Apr 21, 2025 — Anthropic Societal Impacts study analyzing **what values Claude expresses in real conversations**. Used Clio over 700K anonymized claude.ai Free/Pro conversations from one week of Feb 2025; 308K (44%) classified as subjective and analyzed.

**Five top-level value categories** (in prevalence order): **Practical, Epistemic, Social, Protective, Personal**. Hierarchical sub-structure. Most common individual values: professionalism, clarity, transparency — sensible for an assistant.

**Key findings.**
- Claude broadly lives up to helpful/honest/harmless: expressed "user enablement" (helpful), "epistemic humility" (honest), "patient wellbeing" (harmless).
- Rare clusters of values opposed to training (e.g., "dominance," "amorality") most likely from jailbreaks — analysis could potentially detect jailbreaks via value-shift signal.
- Values expressed shift with situation/task — analogous to humans behaving differently in different contexts.

Open dataset released for further research. Provides empirical methodology for evaluating whether character training "stuck."
