---
type: summary
source: 01_Raw/anthropic.com/engineering/claude-think-tool.md
source_url: https://www.anthropic.com/engineering/claude-think-tool
title: 'The "think" tool: Enabling Claude to stop and think in complex tool use situations'
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Extended-thinking, Tool-use]
---

Originally published Mar 20, 2025; updated Dec 15, 2025 with a deprecation-style note: extended-thinking has improved enough that Anthropic now recommends extended-thinking over a dedicated think tool in most cases.

**What the "think" tool is.** A simple tool definition (from τ-Bench) that lets Claude append a "thought" to the log mid-response — no DB change, no new info, just designated scratchpad space. Implementation is one tool spec with a `thought: string` property.

**Distinction from extended-thinking.** Extended-thinking happens *before* generation begins — Claude considers/iterates on a plan up front. The "think" tool runs *during* response generation — Claude stops to evaluate whether it has enough information to proceed, especially after digesting tool-call results. The think tool's reasoning is more focused on *new* information Claude has just discovered.

**When to use which (per the original post).**
- Extended-thinking: simpler tool use (non-sequential, straightforward instruction following), and pure reasoning tasks like coding/math/physics with no tools.
- Think tool: complex tool calls with carefully analyzed outputs, long chains of tool calls, policy-heavy environments with detailed guidelines, sequential decisions where each step builds on previous and mistakes are costly.

**Evaluation on τ-Bench.** Customer-service agent benchmark with airline and retail domains, evaluated via pass^k (probability *all* k independent trials succeed — measures reliability/consistency, harder than pass@k).

Configurations: baseline / extended-thinking only / "think" tool alone / "think" tool + optimized prompt.

Results on **airline domain**: think+prompt = 0.570 pass^1 vs baseline 0.370 — a **54% relative improvement**. Think+prompt outperformed extended-thinking alone (0.412) and think alone (0.404). At k=5, think+prompt held 0.340 vs baseline 0.100.

**Retail domain**: think alone = 0.812 vs baseline 0.783 (smaller delta — easier domain).

**Optimized prompt** (airline) tells Claude to use think as a scratchpad to (a) list specific rules that apply, (b) check if all required info is collected, (c) verify planned action complies with policies, (d) iterate over tool results for correctness — with worked examples like "User wants to cancel flight ABC123 / Need to verify: user ID, reservation ID, reason / Check cancellation rules: within 24h?, ticket class, insurance / Verify no segments flown / Plan: collect missing info, verify rules, get confirmation."

**Takeaway (2025 update).** Use extended-thinking by default; the think-tool pattern remains historically interesting and can still help in narrow agentic tool-loop scenarios, but extended-thinking with better integration is now the recommended path.
