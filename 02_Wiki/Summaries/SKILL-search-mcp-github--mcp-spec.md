---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/plugins/mcp-spec/skills/search-mcp-github/SKILL.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/plugins/mcp-spec/skills/search-mcp-github/SKILL.md
title: "search-mcp-github skill: discover prior MCP discussion"
summarized_at: 2026-05-05
entities_referenced: [Skill, MCP-server, Slash-command]
concepts_referenced: []
---

User-invocable Skill (`name: search-mcp-github`, `arguments: [topic]`) that searches the MCP GitHub org for prior discussion of a topic across PRs, issues, and discussions.

**Where to search** (in priority order):
1. **MCP Docs MCP server** (`mcp-docs` → `SearchModelContextProtocol` tool) — prefer first for current spec content / API references / protocol concepts
2. **Spec PRs and Issues** via `gh search prs` / `gh search issues` (defaults to open + closed)
3. **Spec Discussions** at `modelcontextprotocol/modelcontextprotocol/discussions` (no `gh search discussions` exists — must use GraphQL via `gh api graphql`)
4. **Org Discussions** at `orgs/modelcontextprotocol/discussions` (GraphQL)

For historical decisions, prioritize **merged PRs and closed issues** over open ones.

**Search term variants**: GitHub does NOT split camelCase tokens — `ToolAnnotations` and `Tool Annotations` return almost entirely different results. Always search **both**: camelCase (matches identifiers in code/schema) and space-separated (matches natural language). Skip kebab-case (tokenizes on hyphens, behaves like space form, noisier).

**Deep-diving a PR**: when a result looks highly relevant and you need to understand WHY a change was made (not just WHAT), look at: general PR conversation (`/issues/{pr}/comments`), inline review comments (`/pulls/{pr}/comments`), and top-level review bodies (`/pulls/{pr}/reviews`). The `author_association` field (REST) / `authorAssociation` (GraphQL) identifies maintainers — `MEMBER` or `OWNER` are maintainers.

**Output format**: PRs/issues/discussions formatted with link + title + status + date + brief summary. **Notable maintainer quotes** quoted directly with attribution and footnotes when they reveal design intent, set direction, reject/redirect approaches, or clarify intended semantics. **Footnotes** collected at end with concrete URLs.

**General strategy**: generate variants → use `SearchModelContextProtocol` tool first → expand variants → search GitHub via `gh` CLI → aggregate → display with summarized results, key insights, and direct attributions.
