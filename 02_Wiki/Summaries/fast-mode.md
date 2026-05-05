---
type: summary
source: 01_Raw/code.claude.com/docs/en/fast-mode.md
source_url: https://code.claude.com/docs/en/fast-mode
title: "Speed up responses with fast mode"
summarized_at: 2026-05-05
entities_referenced: [Fast-mode, Settings, Enterprise-gateway]
concepts_referenced: []
---

Fast mode is a high-speed configuration for **Claude Opus 4.6** (NOT a different model). 2.5x faster, higher cost. Same quality. Not available on Opus 4.7 or other models. **Research preview** — pricing/availability subject to change. Requires Claude Code v2.1.36+.

**Pricing**: $30/$150 per MTok (input/output). Flat across the full 1M context window.

**Toggle**: `/fast` (Tab to confirm) in CLI or VS Code extension. Or `"fastMode": true` in settings.json. Visual: `↯` icon next to prompt; switches to Opus 4.6 if on different model. Disabling with `/fast` keeps you on Opus 4.6 (use `/model` to switch back).

**Cost gotcha**: switching mid-conversation pays full fast-mode uncached input price for **entire conversation context**. Enable from session start for best efficiency.

**When to use**: rapid iteration, live debugging, tight-deadline interactive work. **Skip for**: long autonomous tasks, batch/CI, cost-sensitive workloads.

**Fast mode vs effort level**: orthogonal. Fast mode = same quality, lower latency, higher cost. Lower effort = less thinking, faster, potentially lower quality. Combine for max speed on simple tasks.

**Requirements**:
- NOT available on Bedrock / Vertex / Foundry. Only Anthropic Console API + Claude subscription plans (via extra usage).
- **Extra usage** must be enabled (Console billing for individuals; admin for Team/Enterprise).
- Tokens billed directly to extra usage even if plan has remaining usage.
- **Team/Enterprise**: disabled by default; admin must enable in Admin Settings → Claude Code (or Console for API).
- Disable entirely with `CLAUDE_CODE_DISABLE_FAST_MODE=1`.

**Per-session opt-in** (Team/Enterprise): set `fastModePerSessionOptIn: true` in managed settings — each session starts with fast mode off; users explicitly enable with `/fast`. Preference still saved.

**Rate limit behavior**: separate from standard Opus 4.6. On exhaustion: auto-falls-back to standard Opus 4.6, `↯` icon turns gray, auto-re-enables when cooldown expires. Manual `/fast` to disable cooldown.
