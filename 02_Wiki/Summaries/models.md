---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/models.md
title: "Claude Model Catalog"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Extended-thinking]
---

Authoritative model ID catalog for the Claude API. Cardinal rule: **only use exact model IDs listed; never guess or construct**. Use aliases (e.g. `claude-opus-4-7`) over full date-suffixed IDs wherever available.

**Programmatic discovery** for live capability data — preferred over the cached tables when answering "what's the context window for X" / "does X support thinking" / "which models support Y":
```python
m = client.models.retrieve("claude-opus-4-7")
m.id, m.display_name, m.max_input_tokens, m.max_tokens   # typed attrs
caps = m.capabilities                                     # untyped dict
caps["image_input"]["supported"]
caps["thinking"]["types"]["adaptive"]["supported"]
caps["effort"]["max"]["supported"]
caps["structured_outputs"]["supported"]

# filter all models — iterate the page directly (auto-paginates), do NOT use .data
[m for m in client.models.list() if m.capabilities["thinking"]["types"]["adaptive"]["supported"] and m.max_input_tokens >= 200_000]
```
Top-level fields are typed; `capabilities` is dict (use bracket access, no `.get()` needed since every leaf has `supported: true|false`). TS SDK has the same method names + auto-pagination.

Raw HTTP: `GET /v1/models/<id>` with `x-api-key` + `anthropic-version: 2023-06-01`.

**Current models** (recommended):
| Friendly | Alias | Full ID | Context | Max output | Status |
|---|---|---|---|---|---|
| Claude Opus 4.7 | `claude-opus-4-7` | — | 1M | 128K | Active |
| Claude Opus 4.6 | `claude-opus-4-6` | — | 1M | 128K | Active |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | — | 1M | 64K | Active |
| Claude Haiku 4.5 | `claude-haiku-4-5` | `claude-haiku-4-5-20251001` | 200K | 64K | Active |

**Model descriptions**:
- Opus 4.7 — most capable; long-horizon agentic work, knowledge work, vision, memory. **Adaptive thinking only**; sampling parameters and `budget_tokens` REMOVED. 1M context at standard pricing (no long-context premium). Breaking changes — see `shared/model-migration.md`.
- Opus 4.6 — previous-gen Opus. Adaptive thinking recommended. 128K max output requires streaming for large outputs. 1M context.
- Sonnet 4.6 — best speed/intelligence balance. Adaptive thinking. 1M context. 64K output.
- Haiku 4.5 — fastest, cheapest.

**Legacy (still active)**: Opus 4.5/4.1/4.0, Sonnet 4.5/4.0.

**Deprecated (retiring)**: Claude Haiku 3 retires Apr 19, 2026.

**Retired (no longer available)**: Sonnet 3.7, Haiku 3.5, Opus 3, Sonnet 3.5 (both versions), Sonnet 3, Claude 2.1, Claude 2.0.

**User-request resolver**:
| User says... | Use |
|---|---|
| "opus", "most powerful" | `claude-opus-4-7` |
| "sonnet", "balanced" | `claude-sonnet-4-6` |
| "haiku", "fast", "cheap" | `claude-haiku-4-5` |
| "sonnet 3.7" / "sonnet 3.5" / "haiku 3.5" / "haiku 3" | RETIRED/DEPRECATED → suggest current equivalent |
