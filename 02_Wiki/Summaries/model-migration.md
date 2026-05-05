---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/model-migration.md
title: "Model Migration Guide (claude-api shared)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Extended-thinking]
---

Migration guide for moving existing code to newer Claude models. Covers breaking changes, deprecated parameters, drop-in replacements for retired models. Note: only first ~80 lines sampled — full file is large.

**TL;DR**: change model ID string. If using `budget_tokens` → switch to `thinking: {type: "adaptive"}`. Assistant prefills 400 on Opus 4.6 + Sonnet 4.6 — switch to prefill replacements (most often `output_config.format`). Sonnet 4.5 → Sonnet 4.6: set `effort` explicitly (4.6 defaults to `high`). Remove beta headers `effort-2025-11-24` and `fine-grained-tool-streaming-2025-05-14` (GA on 4.6); remove `interleaved-thinking-2025-05-14` once on adaptive thinking. Drop back from `client.beta.messages.create` to `client.messages.create`. Dial back aggressive "CRITICAL: YOU MUST" tool instructions — 4.6 follows system prompt much more closely.

**Step 0 — Confirm migration scope**: **NEVER edit before confirming scope**. Even imperative-sounding requests like "migrate my codebase", "upgrade to Sonnet 4.6", "migrate to Opus 4.7" are AMBIGUOUS — ask for: (1) entire working directory, (2) specific subdirectory, or (3) specific file/list. Surface as single clarifying question.

For large repos, run breakdown query first:
```sh
rg -l "<old-model-id>" --type-not md | cut -d/ -f1 | sort | uniq -c | sort -rn
```
Present like "Found 217 references across 3 directories: api/ (130), api-go/ (62), routing/ (25). Which to migrate?"

Confirm `git status` clean before surveying.

**Step 1 — Classify each file** into 4 buckets:
1. **Calls API/SDK** (`client.messages.create(model=…)`) → swap ID + apply breaking-change checklist
2. **Defines/serves the model** (registries, OpenAPI specs, routing/queue configs, model-policy enums) → old entry STAYS. Ask: add new alongside / leave alone / retire old. **If can't ask, default to (a) add alongside + flag.**
3. **References ID as opaque string** (UI fallback, capability-gate substring checks, generic test fixtures, label parsers, env defaults) → usually swap, but check sub-cases first
4. **Suffixed variant ID** (`claude-X-fast`, `-1024k`, `-200k`, `[1m]`, dated snapshots) → deployment/routing identifiers, not public model ID. Verify in registry first; if no equivalent, leave + flag.

**Bucket 3 sub-cases** before swapping a string ref:
- **Capability gate** (`if 'opus-4-6' in model_id:`) → ADD new ID alongside, don't replace. Old model still served + still has capability.
- **Registry-assert test** (`assert "claude-X" in supported_models`) → add assertion for new alongside; keep old.
- **Frozen/generated snapshot** → regenerate, don't hand-edit
- **Coupled to a definer** (integration test passing model auth via shared `conftest`, asserts on billing-tier/rate-limit-group enum, generated SKU/pricing catalog) → verify definer has new-model entry first; if not, add seed entry (reuse nearest tier as placeholder); if can't confidently do that, ask user. **DO NOT skip the test** — swap without populating definer = runtime fail.

For tests specifically: breaking parameters (`temperature`, `top_p`, `budget_tokens`) usually absent; expect mostly clean breaking-change scan results.

**Pre-flight grep**: many codebases tag must-change spots with `MODEL LAUNCH`, `KEEP IN SYNC`, `@model-update`. Grep for repo's convention BEFORE the broad model-ID grep — markers point at load-bearing changes.

(Remainder includes per-SDK syntax reference table, destination/retired-model replacement matrix, breaking-changes-by-source-model tables, Opus 4.7 migration checklist with `[BLOCKS]` / `[TUNE]` tags, verification steps — not sampled.)
