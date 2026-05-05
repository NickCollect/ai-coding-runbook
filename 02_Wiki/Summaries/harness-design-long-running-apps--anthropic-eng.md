---
type: summary
source: 01_Raw/anthropic.com/engineering/harness-design-long-running-apps.md
source_url: https://www.anthropic.com/engineering/harness-design-long-running-apps
title: "Harness design for long-running application development"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Skill, MCP-server]
concepts_referenced: [Agentic-loop, Compaction, Context-window, Agent-team]
---

Anthropic Labs post (Mar 24, 2026) by Prithvi Rajasekaran on pushing Claude further at long-running autonomous frontend design and full-stack application development. Builds on the [effective-harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) work and Anthropic's frontend-design skill, both of which hit ceilings.

**Inspiration: GAN-like multi-agent structure.** A **generator** agent produces work; an **evaluator** agent grades it; the feedback loop drives the generator toward stronger outputs. Key insight: separating doer from judge is a strong lever — even though the evaluator is still a generous-by-default LLM, it's far more tractable to tune a *standalone* evaluator to be skeptical than to make the generator self-critical.

**Two failure modes addressed.**
- *Coherence loss / "context anxiety"* — some models (Sonnet 4.5 strongly) wrap up prematurely as they approach what they think is their context limit. Solved by **context resets** (clear context entirely, fresh agent + structured handoff). Differs from compaction (in-place summary, same agent) — reset gives the new agent a clean slate. Opus 4.5 largely removed this behavior, allowing the harness to drop context resets and rely on Agent-SDK automatic compaction.
- *Agent self-flattery* — agents praise their own work even on mediocre outputs, especially on subjective tasks like design.

**Frontend design experiment: making subjective quality gradable.** Four criteria given to both generator and evaluator:
1. *Design quality* — coherent whole, distinct mood/identity.
2. *Originality* — custom decisions, not template/AI-slop ("purple gradients over white cards" called out as failure).
3. *Craft* — typography, spacing, color, contrast.
4. *Functionality* — usability independent of aesthetics.

Design and originality weighted higher (Claude was already competent on craft/functionality, weak on aesthetic risk-taking). Evaluator calibrated with few-shot examples and detailed score breakdowns. Generator built on Agent-SDK; evaluator used Playwright MCP to interact with the live page (navigate, screenshot, score, write critique). 5-15 iterations, up to 4-hour wall-clock. Generator instructed to either refine or pivot aesthetic between iterations.

Results: scores improved over iterations before plateauing; even the first iteration was noticeably better than no-prompt baseline (criteria-language alone steered the model). Evaluator phrasing like "the best designs are museum quality" produced visual convergence — wording matters. Notable example: a Dutch art museum site that, on the 10th cycle, scrapped a polished dark landing page and reimagined the site as a 3D CSS-perspective room with checkered floor, free-form artwork on walls, doorway-based navigation.

**Three-agent architecture for full-stack coding.**
- **Planner** — takes 1-4-sentence prompt, expands into ambitious product spec focused on product context and high-level design (not granular tech details — those would cascade as errors). Asked to weave AI features into specs.
- **Generator** — works in sprints, one feature at a time. Stack: React + Vite + FastAPI + SQLite (later Postgres). Self-evaluates at sprint end. Uses git for version control.
- **Evaluator** — uses Playwright MCP to click through the running app like a user, testing UI / API endpoints / DB states. Grades each sprint against criteria adapted from frontend (product depth, functionality, visual design, code quality). Each criterion has a hard threshold; below it = sprint fails, generator gets detailed feedback.

**Sprint contract negotiation.** Before each sprint, generator and evaluator agree on what "done" looks like (proposed by generator, reviewed by evaluator, iterated until agreement). Bridges high-level spec and testable implementation. File-based communication (one writes, other reads/responds via files).

**Cost / quality data point.** Prompt: "Create a 2D retro game maker with level editor, sprite editor, entity behaviors, playable test mode."
- Solo harness: 20 min, $9. Output looked plausible but: wasted layout, rigid workflow, no UI guidance for required entity-creation order, broken entity-runtime wiring → entities appear but don't respond to input.
- Full harness: 6 hr, $200 (20× more expensive). Difference in output quality immediately apparent.

**Takeaway.** Generator-evaluator separation, weighted subjective grading criteria, and sprint-contract negotiation enable autonomous multi-hour app builds with consistent end-to-end functionality. As models improve (Opus 4.5 → presumably 4.7+), some scaffolding (context resets) becomes unnecessary; orchestration complexity drops.
