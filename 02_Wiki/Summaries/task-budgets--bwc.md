---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/task-budgets.md
source_url: https://platform.claude.com/docs/en/build-with-claude/task-budgets
title: "Task budgets"
summarized_at: 2026-05-05
entities_referenced: [Effort, Messages-API]
concepts_referenced: [Agentic-loop]
---

Task budgets give Claude an **advisory token budget for the full agentic loop** (thinking + tool calls + tool results + output). The model sees a server-injected countdown and self-regulates pacing to finish gracefully as the budget is consumed. Public beta on **Claude Opus 4.7 only**. Header: `task-budgets-2026-03-13`. ZDR-eligible.

## When to use

- Agentic workflows with multiple tool calls / decisions.
- You want Claude to self-regulate token spend on long-horizon work.
- Predictable per-task cost or latency ceiling.
- You want graceful wrap-up (summarize findings, report progress) rather than mid-action cutoff.

Complements (does not replace) `effort`:
- `effort` = how thoroughly Claude reasons per step.
- `task_budget` = total work cap across the agentic loop.

## API shape

```json
{
  "output_config": {
    "effort": "high",
    "task_budget": {"type": "tokens", "total": 64000}
  }
}
```

`task_budget` fields:

| Field | Notes |
|---|---|
| `type` | Always `"tokens"` |
| `total` | Total tokens for the loop (thinking + tool calls + tool results + output) |
| `remaining` | Optional. Carry-over from prior request. Defaults to `total`. |

## Critical gotcha — countdown semantics

**Countdown reflects tokens Claude has processed in the current agentic loop, NOT tokens you resend between turns.**

If your client sends full conversation history each follow-up AND decrements `remaining` to mirror it client-side, the model will see an under-reported budget → countdown drops faster than reality → Claude wraps up earlier than the actual budget allows.

**Recommendation:** set a generous `total` and let the model self-regulate against the server-tracked countdown — don't try to mirror it client-side.

## Worked example logic

In a loop with `total: 100000` + `bash` tool:
- Turn 1: Claude generates ~5000 tokens (thinking + tool_use). Countdown ends at ≈ 95000.
- Turn 2: client resends full history + tool_result. Budget only decrements by what Claude **generates this turn**, not by the resent history bytes.
