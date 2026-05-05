---
type: summary
source: 01_Raw/anthropic.com/engineering/AI-resistant-technical-evaluations.md
source_url: https://www.anthropic.com/engineering/AI-resistant-technical-evaluations
title: "Designing AI-resistant technical evaluations"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Tristan Hume, lead on Anthropic's performance optimization team, describes three iterations of a take-home test for performance engineering candidates and what each Claude model release forced him to redesign. Since early 2024 over 1,000 candidates have completed the take-home; dozens were hired (including engineers who brought up the Trainium cluster).

The original test (Nov 2023) used a Python simulator for a fake TPU-like accelerator with VLIW, SIMD, multicore, manually managed scratchpad memory and hot-reloading Perfetto traces. The task was a parallel tree traversal — deliberately not deep-learning flavored — starting from a serial implementation with a hidden bug. 4-hour window (later 2). Design goals: representative, high-signal (wide scoring distribution, never finished by even strong candidates), no domain knowledge required, fun, and explicitly AI-allowed.

Each Claude release defeated the test. Claude 3.7 Sonnet made delegating-to-Claude-Code a >50%-of-candidates winning strategy. Claude Opus 4 (May 2025) outperformed almost all humans within 4 hours. Claude Opus 4.5 matched the best human performance within 2 hours, even compared against humans heavily steering Claude 4. Hume rejected banning AI (enforcement, doesn't reflect job reality) and rejected raising the bar to "substantially outperform Claude Code alone" (humans steering Claude would just sit and watch).

Iterations: V2 used Opus 4 to identify where the problem got hard, removed multicore, shortened to 2 hours. V3 attempted a register-transposition / bank-conflict problem (Claude solved it). The final approach moved away from pure optimization toward problems that test debugging, systems design, performance analysis and verification — areas where current performance engineers actually spend time, but harder to test objectively without context.

The post frames a broader claim: AI-resistant evaluations are increasingly hard, not because models can do anything, but because they can do most well-bounded coding tasks given a clean spec and a fast feedback loop. Anthropic is releasing the original take-home as an open challenge — best-human-with-unlimited-time still beats Opus 4.5, so anyone who can beat Opus 4.5 is invited to apply.
