---
type: summary
source: 01_Raw/code.claude.com/docs/en/model-config.md
source_url: https://code.claude.com/docs/en/model-config
title: "Model configuration"
summarized_at: 2026-05-05
entities_referenced: [Settings, Skill, Subagent, Enterprise-gateway]
concepts_referenced: [Extended-thinking, Prompt-caching, Context-window]
---

**Model selection**: configure with model alias OR full model name (Anthropic API: full name; Bedrock: inference profile ARN; Foundry: deployment name; Vertex: version name).

**Aliases**:
- `default` — clears overrides, reverts to recommended (Max/Team Premium → Opus 4.7; Pro/Team Std/Enterprise/API → Sonnet 4.6; Bedrock/Vertex/Foundry → Sonnet 4.5).
- `best` ≡ `opus`, `sonnet`, `opus`, `haiku`.
- `sonnet[1m]` / `opus[1m]` — 1M context window variants.
- `opusplan` — Opus during plan mode, Sonnet during execution. (Plan-mode Opus runs at standard 200K context; 1M upgrade NOT applied to opusplan.)

On Anthropic API: `opus` → Opus 4.7, `sonnet` → Sonnet 4.6. On Bedrock/Vertex/Foundry: `opus` → Opus 4.6, `sonnet` → Sonnet 4.5 (newer via full name or env vars). Opus 4.7 requires Claude Code v2.1.111+. **April 23, 2026**: default for Enterprise pay-as-you-go and API users changes to Opus 4.7.

**Set model** (priority order): `/model` in session > `claude --model` > `ANTHROPIC_MODEL` env > `model` in settings. As of v2.1.117, project-pinned model in `.claude/settings.json` triggers writing your override to `.claude/settings.local.json` so it persists.

**Restrict via** `availableModels` array in managed/policy settings. **Default option in picker NOT affected** by `availableModels` — always available, resolves to subscription tier default. To fully control: combine `availableModels` + `model` (initial) + `ANTHROPIC_DEFAULT_*_MODEL` env vars (control what aliases/Default resolves to). Multi-level merging dedupes.

**Effort levels** (Opus 4.7: low/medium/high/xhigh/max; Opus 4.6 + Sonnet 4.6: low/medium/high/max). Default `xhigh` on Opus 4.7, `high` on others. Higher levels persist across sessions; `max` is session-only unless set via `CLAUDE_CODE_EFFORT_LEVEL`. Set via `/effort`, `/model` slider, `--effort`, env var, settings, or `effort` in skill/subagent frontmatter. Env var > config > model default.

**`ultrathink` keyword** in prompt → in-context deeper reasoning request without changing session effort. Other phrases ("think hard" etc) NOT recognized.

**Adaptive reasoning**: Opus 4.7 always uses adaptive (no fixed budget). Opus 4.6/Sonnet 4.6 can revert with `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` + `MAX_THINKING_TOKENS`.

**Extended thinking**: toggle Option+T (alwaysThinkingEnabled), `MAX_THINKING_TOKENS=0` to disable. Thinking output collapsed; Ctrl+O to view as gray italic. API users get redacted blocks unless `showThinkingSummaries: true`. Charged regardless.

**Extended context (1M)**: Opus 4.7, Opus 4.6, Sonnet 4.6 support. Max/Team/Enterprise: Opus 1M included; Sonnet via extra usage. Pro: both via extra usage. API: full access. Disable: `CLAUDE_CODE_DISABLE_1M_CONTEXT=1`. Pricing: standard, no premium beyond 200K. Append `[1m]` to alias or full ID.

**Custom model option**: `ANTHROPIC_CUSTOM_MODEL_OPTION` adds one entry to `/model` picker. Plus `_NAME` and `_DESCRIPTION` for display. No validation — accepts any string.

**Env vars** (full model names): `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL` (also background functionality), `CLAUDE_CODE_SUBAGENT_MODEL`. `ANTHROPIC_SMALL_FAST_MODEL` deprecated.

**Pin for Bedrock/Vertex/Foundry**: pin all three model env vars before rollout — without pinning, new model releases cause Foundry errors and Bedrock/Vertex fallback notices. Append `[1m]` for extended context (stripped before sending).

**Customize pinned display + capabilities** via `_NAME`, `_DESCRIPTION`, `_SUPPORTED_CAPABILITIES`. Capabilities: `effort`, `xhigh_effort` (v2.1.111+), `max_effort`, `thinking`, `adaptive_thinking`, `interleaved_thinking`. When set, listed enabled, others disabled.

**Override per version**: `modelOverrides` setting maps Anthropic model IDs → provider-specific strings. Allows multiple versions in same family. `availableModels` allowlist matches on Anthropic ID, not override.

**Prompt caching disable**: `DISABLE_PROMPT_CACHING=1` (global), or per-tier `_HAIKU/_SONNET/_OPUS` variants.
