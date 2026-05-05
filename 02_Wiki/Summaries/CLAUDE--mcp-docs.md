---
type: summary
source: 01_Raw/github/modelcontextprotocol/docs/CLAUDE.md
source_url: https://github.com/modelcontextprotocol/docs/blob/main/CLAUDE.md
title: "MCP docs repo: Claude Code documentation guidelines"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Style/process guide for editing the (now-deprecated) `modelcontextprotocol/docs` Mintlify documentation site.

**Build commands**: `mintlify dev` for local preview; deployment is automatic on PR merge to `main`.

**Style guidelines**: follow existing MDX formatting and components; clear, concise, technically accurate prose; include practical code examples; test all links and code samples; maintain structural consistency with existing docs.

**CLI command formatting**: use a two-line format with the prompt on its own line — `$ claude` followed by `> /command`.

**Tutorial structure**: use the headings "When to use", "Steps", and "Tips".

**Branch naming**: prefix with `ashwin/` (e.g., `ashwin/add-mcp-cli-docs`).

**File organization**: place new pages in appropriate sections (concepts, tutorials, etc.); update `docs.json` when adding new pages; use `kebab-case.mdx` filenames; include proper frontmatter.

**Standards**: prioritize user understanding over technical completeness; document basic syntax + concrete examples; for image-analysis examples, quote the path argument: `$ claude "Analyze this image: /path/to/image.png"`.
