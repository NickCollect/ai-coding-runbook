---
type: summary
source: 01_Raw/anthropic.com/engineering/april-23-postmortem.md
source_url: https://www.anthropic.com/engineering/april-23-postmortem
title: "An update on recent Claude Code quality reports"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Effort, Memory]
concepts_referenced: [Extended-thinking, Prompt-caching]
---

Postmortem (Apr 23, 2026) on three separate changes degrading Claude Code, the Claude Agent SDK, and Claude Cowork between March and April 2026. The Anthropic API itself was not affected. All three issues resolved by April 20 (v2.1.116). Anthropic reset usage limits for all subscribers as compensation.

**Issue 1 — Default reasoning effort change.** March 4: Claude Code default reasoning effort changed `high` → `medium` to reduce very long latency in `high` mode (UI appearing frozen). Affected Sonnet 4.6 and Opus 4.6. Internal evals showed medium had slightly lower intelligence with significantly less latency, no long-tail latency spikes, and better usage-limit utilization — but most users didn't change the default and reported Claude Code felt less intelligent. Reverted April 7. New defaults: `xhigh` for Opus 4.7, `high` for all other models. Effort levels are exposed via `/effort` slash-command and sent to Messages API as the `effort` parameter.

**Issue 2 — Caching optimization that dropped prior reasoning.** March 26: shipped change to clear old extended-thinking blocks from sessions idle >1 hour, using the `clear_thinking_20251015` API header with `keep:1`. Bug: instead of clearing once, it cleared on every turn for the rest of the session. Compounding effect — even reasoning from the current turn was dropped if a follow-up came mid-tool-use. Symptoms: Claude appeared forgetful, repetitive, made odd tool choices. Also caused cache misses → faster usage-limit drain (a separate user complaint stream). Fixed April 10 in v2.1.101. Took >1 week to root-cause; passed multiple human/automated code reviews, unit tests, e2e tests, and dogfooding. Notably: Code Review (Opus 4.7) found the bug retroactively when given full repo context; Opus 4.6 didn't.

**Issue 3 — Verbosity-reduction system-prompt change.** April 16: added `"Length limits: keep text between tool calls to ≤25 words. Keep final responses to ≤100 words unless the task requires more detail."` to address Opus 4.7's verbosity. After multiple weeks of internal testing showed no regressions, shipped alongside Opus 4.7 launch. Broader-eval ablations later showed a 3% drop on both Opus 4.6 and 4.7; reverted April 20. Affected all three: Sonnet 4.6, Opus 4.6, Opus 4.7.

**Going forward.** Ensure more internal staff use the exact public Claude Code build (vs internal versions). Improve and ship Code Review tooling. Tighter system-prompt change controls: per-model eval suites for every prompt change, ablations to understand each line's impact, new tooling for prompt-change review/audit, model-specific gating in CLAUDE.md, soak periods, broader eval suites and gradual rollouts for any change that could trade off intelligence. Created @ClaudeDevs on X for explanation threads.
