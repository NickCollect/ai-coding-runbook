---
type: summary
source: 01_Raw/anthropic.com/engineering/claude-code-auto-mode.md
source_url: https://www.anthropic.com/engineering/claude-code-auto-mode
title: "Claude Code auto mode: a safer way to skip permissions"
summarized_at: 2026-05-05
entities_referenced: [Auto-mode, Permission-mode, Sandboxing, Subagent]
concepts_referenced: []
---

Auto mode (Mar 25, 2026) is a new Claude Code permission mode that delegates tool-call approvals to model-based classifiers — a middle ground between manual review (users approve 93% of prompts anyway, leading to approval fatigue) and `--dangerously-skip-permissions` (no protection).

**Problem.** Existing permission-mode tradeoff space: sandboxing is safe but high-maintenance (every new capability needs config, network/host access breaks isolation); skip-permissions has no protection; manual sits in the middle but causes fatigue. Anthropic's internal incident log (also documented in Opus 4.6 system card §6.2.1, §6.2.3.3) lists past misbehaviors: deleting remote git branches from misinterpreted instructions, uploading a GitHub auth token to internal infra, attempting migrations on production DBs — all from overeager initiative, not malice.

**Architecture — two layers of defense.**
1. **Input layer (prompt-injection probe).** Server-side scanner of tool outputs (file reads, web fetches, shell, external tools) before they enter agent context. Suspicious content gets a warning prepended telling the agent to anchor on user intent.
2. **Output layer (transcript classifier, runs on Sonnet 4.6).** Evaluates each action against decision criteria pre-execution. Stage 1: fast single-token yes/no filter (errs toward blocking). Stage 2: chain-of-thought reasoning only on flagged actions (cleans up false positives). Classifier sees user messages and tool calls only — Claude's own messages and tool outputs are stripped (reasoning-blind by design). Subagents run the same pipeline recursively; handoff classifiers at delegation (can deny) and at return (warns only).

**Threat model.** Four causes of dangerous actions: (1) overeager behavior; (2) honest mistakes about blast radius; (3) prompt injection; (4) misaligned model. Classifier is tuned for #1 and #2 but defense applies regardless.

**Permission tiers.**
- *Tier 1 — built-in safe-tool allowlist + user always-allow rules.* Reads, search, code nav, todos, plan-mode transitions auto-allowed. On entering auto mode, blanket-shell rules and wildcarded interpreter rules (python, node, ruby) are dropped — narrow rules carry over. Otherwise the classifier never sees the most damaging commands.
- *Tier 2 — in-project file ops.* Writes/edits inside the project dir bypass the classifier (latency-free, reviewable via VCS).
- *Tier 3 — transcript classifier.* Everything else: shell, web fetches, external tool integrations, subagent spawns, out-of-project filesystem ops.

**Decision-criteria template.** Fixed parts: how to evaluate real-world impact (chained `&&`, payload-then-execute, script-assembled commands all evaluated as the resolved action), and how to read user authorization (deliberately conservative — "clean up my branches" doesn't authorize batch delete). Customizable slots: trust environment (default trusts only the current git repo), >20 default block rules (destroy/exfiltrate, degrade security posture, cross trust boundaries, bypass review/affect others), allow exceptions (install pkgs in repo manifest, standard credential flows, push to working branch).

**Results** (n=10K real traffic, n=52 real overeager, n=1K synthetic exfil):
- Stage 1 alone: 8.5% FPR / 6.6% FNR / 1.8% FNR.
- Stage 1→Stage 2 pipeline: 0.4% FPR / 17% FNR / 5.7% FNR.

**Honest framing of 17% FNR on real overeager actions.** Most misses correctly identify the danger (force-push, deletion) but misjudge whether a real consent signal in the session covers *this specific* blast radius. "Clean up the PR" was said but doesn't name force-pushing; one earlier approval doesn't make a pattern. Prompt-engineering fixes cost more than they gain.
