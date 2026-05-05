---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/claude-opus-4-5-migration/skills/claude-opus-4-5-migration/references/effort.md
title: "Effort parameter (beta) — Opus 4.5 migration reference"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Extended-thinking]
---

Reference doc inside the `claude-opus-4-5-migration` plugin's skill — explains the **`effort` API parameter** (beta), which controls how eagerly Claude spends tokens (thinking, text responses, function calls). Recommended setting during migration to Opus 4.5: `effort: "high"` for best performance.

**Levels**:
| Effort | Use case |
|---|---|
| `high` | Best performance, deep reasoning (default) |
| `medium` | Cost/latency vs. performance balance |
| `low` | Simple high-volume queries; significant token savings |

Requires beta header `effort-2025-11-24`.

**API shape** (Python/TS/raw — same payload):
```python
client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    betas=["effort-2025-11-24"],
    output_config={"effort": "high"},
    messages=[...]
)
```

**Effort vs thinking budget** — independent dimensions:
- High effort + no thinking = more tokens, no thinking tokens
- High effort + 32k thinking = more tokens, thinking capped at 32k

**Recommendation order**: pick effort first, then set thinking budget. Best perf = high + high thinking. Cost/latency optimization = medium effort. High-volume simple queries = low effort.
