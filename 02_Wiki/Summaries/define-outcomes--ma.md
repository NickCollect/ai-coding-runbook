---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/define-outcomes.md
source_url: https://platform.claude.com/docs/en/managed-agents/define-outcomes
title: "Define outcomes"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, Session-API, Files-API]
concepts_referenced: []
---

**Research Preview feature** (request access). Outcomes elevate a session from *conversation* to *work*: define what "done" looks like and how to measure quality, and the agent self-evaluates and iterates until it's met. **Requires both `managed-agents-2026-04-01` and `managed-agents-2026-04-01-research-preview` beta headers.**

**Mechanism.** When you define an outcome, the harness automatically provisions a *grader* that evaluates the artifact against a rubric. The grader uses a separate context window to avoid being influenced by the main agent's implementation choices. It returns per-criterion breakdowns: confirmation that the rubric is satisfied, or specific gaps to address. That feedback is handed back to the agent for the next iteration cycle.

**Rubric.** A markdown document with explicit, gradeable criteria. Required. *Tip:* structure as "The CSV contains a price column with numeric values" rather than "The data looks good"—the grader scores each criterion independently, so vague criteria produce noisy evaluations. *Bootstrap trick:* if you don't have a rubric, give Claude an example of a known-good artifact and ask it to analyze what makes it good, then turn that analysis into a rubric.

Example rubric (DCF Model): sections like "Revenue Projections" (uses 5 yrs historical data, projects ≥5 yrs forward, growth assumptions stated), "Cost Structure" (COGS/opex separate, margins consistent), "Discount Rate" (WACC with stated assumptions), "Terminal Value" (perpetuity or exit multiple, growth ≤ long-term GDP), "Output Quality" (single .xlsx with labeled sheets, separate Assumptions sheet, sensitivity analysis).

Pass the rubric inline as text on `user.define_outcome`, or upload via the [[Files-API]] (requires `files-api-2025-04-14` beta header) for reuse across sessions.

**Initiating an outcome.** Create a [[Session-API]] session, then send a `user.define_outcome` event:

```json
{
  "type": "user.define_outcome",
  "description": "Build a DCF model for Costco in .xlsx",
  "rubric": {"type": "file", "file_id": "file_01..."},
  "max_iterations": 5
}
```

Alternative rubric form: `{"type": "text", "content": "..."}`. `max_iterations` defaults to 3, max 20. The agent starts working on receipt—no additional `user.message` event is needed. The event is echoed back with `processed_at` and `outcome_id`.

**Outcome events on the stream.**
- `agent.*` events show progress (messages, tool use).
- `span.outcome_evaluation_*` events are emitted *only for outcome sessions*: start (with 0-indexed `iteration`), ongoing (heartbeat—grader's reasoning is opaque), end (with `result`).
- You can still send `user.message` events to direct work as it progresses, but it's optional—the agent knows to work until it has exhausted iterations or achieved the outcome.
- `user.interrupt` pauses current outcome and marks `outcome_evaluation_end.result` as `interrupted`, allowing a new outcome.
- After final evaluation, the session can continue conversationally OR a new outcome can be kicked off; the session retains history of the prior outcome.

**Evaluation `result` values:**
- `satisfied`: session transitions to `idle`.
- `needs_revision`: agent starts a new iteration cycle.
- `max_iterations_reached`: no more evaluation cycles. Agent may run one final revision before transitioning to idle.
- `failed`: rubric fundamentally doesn't match the task (e.g., description and rubric contradict each other).
- `interrupted`: only emitted if `outcome_evaluation_start` already fired before the interrupt.

**One outcome at a time.** Chain multiple outcomes by sending a new `user.define_outcome` after the previous outcome's terminal event.

**Status checking.** Listen on the events stream for `span.outcome_evaluation_end`, OR poll `GET /v1/sessions/:id` and read `outcome_evaluations[].result`.

**Retrieving deliverables.** Agent writes output files to `/mnt/session/outputs/` inside the container. Once the session is idle, fetch via the Files API scoped to the session: `GET /v1/files?scope_id={session_id}` then download by `file_id`.
