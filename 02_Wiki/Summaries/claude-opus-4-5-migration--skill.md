---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/claude-opus-4-5-migration/skills/claude-opus-4-5-migration/SKILL.md
title: "claude-opus-4-5-migration (skill)"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: [Extended-thinking]
---

Skill (`SKILL.md`) for migrating prompts and code from Sonnet 4.0 / Sonnet 4.5 / Opus 4.1 → Opus 4.5. Updates model strings + adjusts prompts for known Opus 4.5 behavioral differences. **Does NOT migrate Haiku 4.5.**

**Workflow**:
1. Search codebase for model strings + API calls
2. Update model strings to Opus 4.5 (per platform)
3. Remove unsupported beta headers
4. Add `effort` parameter set to `"high"` (see `references/effort.md`)
5. Summarize changes
6. Tell user: "If you encounter any issues with Opus 4.5, let me know and I can help adjust your prompts."

**Beta header removal**: `context-1m-2025-08-07` not yet supported with Opus 4.5; leave a comment noting this.

**Target model strings**:
| Platform | Opus 4.5 |
|---|---|
| Anthropic API | `claude-opus-4-5-20251101` |
| AWS Bedrock | `anthropic.claude-opus-4-5-20251101-v1:0` |
| Vertex AI | `claude-opus-4-5@20251101` |
| Azure Foundry | `claude-opus-4-5-20251101` |

**Source replacements**: includes Sonnet 4.0 (`claude-sonnet-4-20250514` etc.), Sonnet 4.5 (`claude-sonnet-4-5-20250929`), Opus 4.1 (`claude-opus-4-1-20250422`).

**Prompt adjustments** (only apply if user explicitly requests OR reports specific issue — by default just update model strings):

1. **Tool overtriggering** — Opus 4.5 more responsive to system prompts. Soften aggressive language: `CRITICAL:` → remove/soften; `You MUST` → `You should`; `ALWAYS do X` → `Do X`; `NEVER skip` → `Don't skip`; `REQUIRED` → soften. **Only on tool-triggering instructions.**
2. **Over-engineering prevention** — adds `references/prompt-snippets.md` content if user reports unwanted files / excess abstraction / unrequested features
3. **Code exploration** — Opus 4.5 can be too conservative; add snippet if user reports proposing fixes without inspecting code
4. **Frontend design** — add aesthetics snippet if user requests improved frontend or reports generic outputs
5. **Thinking sensitivity** — when extended thinking NOT enabled (default — no `thinking` parameter), Opus 4.5 particularly sensitive to "think" word + variants. Replace with "consider," "believe," "evaluate."

**Snippet integration guidelines**: don't just append. Use XML tags (e.g., `<code_guidelines>`, `<tool_usage>`) to organize. Match existing prompt style. Place snippets in logical locations (coding guidelines near other coding instructions).
