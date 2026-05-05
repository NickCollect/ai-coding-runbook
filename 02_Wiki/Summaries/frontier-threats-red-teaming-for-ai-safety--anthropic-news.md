---
type: summary
source: 01_Raw/anthropic.com/news/frontier-threats-red-teaming-for-ai-safety.md
source_url: https://www.anthropic.com/news/frontier-threats-red-teaming-for-ai-safety
title: "Frontier Threats Red Teaming for AI Safety"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Jul 26, 2023 — Anthropic's approach to **frontier-threats red teaming** in dual-use national-security domains. Initial test project: biological risks. 150+ hours with top biosecurity experts (Gryphon Scientific) using a bespoke secure interface without trust/safety monitoring.

**Findings.** Current frontier models can sometimes produce sophisticated, accurate, expert-level biological knowledge. Models more capable as they get larger; tool access likely advances biology capabilities further. Unmitigated LLMs could accelerate bad-actor bioweapon misuse vs internet-only baseline; effects small today but growing relatively fast — potentially actualized in next 2-3 years rather than 5+.

**Mitigations work.** Training-process changes (e.g., Constitutional AI) reduce harmful outputs. Classifier-based filters make multi-step harmful information harder to chain together. Both deployed in production frontier models.

**Process recommendation.** Domain experts (100+ hours) + LLM experts collaboratively probe; build automated, repeatable evaluations from expert knowledge; partner with trusted third parties under strong infosec because the information itself is sensitive.
