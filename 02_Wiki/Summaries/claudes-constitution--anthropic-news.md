---
type: summary
source: 01_Raw/anthropic.com/news/claudes-constitution.md
source_url: https://www.anthropic.com/news/claudes-constitution
title: "Claude's Constitution"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

May 9, 2023 — **Original Claude Constitution** published. Underpins the Constitutional AI training method. Updated in Jan 2026 (see [claude-new-constitution](https://www.anthropic.com/news/claude-new-constitution)).

**Constitutional AI** uses AI feedback to evaluate outputs against a set of explicit principles, instead of crowd-sourced human comparisons (which face scaling issues, expose contractors to disturbing outputs, are resource-intensive). Two-stage training: (1) model trained to critique and revise its own responses using the principles + few examples; (2) RL phase using AI-generated feedback (RLAIF) instead of human feedback to choose more harmless outputs. Goal: helpful, honest, harmless AI with values transparent and adjustable.

The post lists the principles in full at the end, drawn from sources like UN Declaration of Human Rights, Apple's terms of service, Anthropic-internal research, and other ethical frameworks. Foundational document for Anthropic's alignment approach until the Jan 2026 rewrite.
