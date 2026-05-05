---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/blog/archetypes/default.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/archetypes/default.md
title: "MCP blog Hugo archetype (default post template)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Hugo archetype file used by `hugo new posts/<slug>.md` to scaffold new MCP blog posts. Defines required frontmatter: title (auto-derived from filename), date, `draft: true`, one-sentence SEO `description` (PaperMod theme uses this for `BlogPosting.description` and `<meta name="description">`; falls back to first ~70 words of body), `author` array (each entry becomes a `schema.org` Person in `BlogPosting.author`), `tags`, and an optional `cover.image` field for JSON-LD/OpenGraph preview images (placed under `static/posts/<slug>/`). Pure scaffolding — not user-facing content.
