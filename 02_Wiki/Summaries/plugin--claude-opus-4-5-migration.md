---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/claude-opus-4-5-migration/.claude-plugin/plugin.json
title: "Plugin manifest: claude-opus-4-5-migration"
summarized_at: 2026-05-05
entities_referenced: [Plugin]
concepts_referenced: []
---

Plugin manifest for the `claude-opus-4-5-migration` plugin. Minimal plugin.json schema:

```json
{
  "name": "claude-opus-4-5-migration",
  "version": "1.0.0",
  "description": "Migrate your code and prompts from Sonnet 4.x and Opus 4.1 to Opus 4.5.",
  "author": { "name": "William Hu", "email": "whu@anthropic.com" }
}
```

Plugin's purpose: migrate code/prompts from Sonnet 4.x and Opus 4.1 to Opus 4.5. The plugin's body content (skills like `effort.md` references doc) describes Opus 4.5–specific recommendations such as `effort: "high"` and the `effort-2025-11-24` beta flag.
