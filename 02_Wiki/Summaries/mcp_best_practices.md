---
type: summary
source: 01_Raw/github/anthropics/skills/skills/mcp-builder/reference/mcp_best_practices.md
title: "MCP Server Best Practices"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Reference doc from the `mcp-builder` skill. Best practices for building MCP servers. Note: only first ~100 lines sampled.

**Server naming**:
- Python: `{service}_mcp` (snake_case) — e.g., `slack_mcp`, `github_mcp`, `jira_mcp`
- Node/TypeScript: `{service}-mcp-server` (kebab-case) — e.g., `slack-mcp-server`
- General + descriptive of integrated service; no version numbers in name

**Tool naming**:
- snake_case with service prefix: `{service}_{action}_{resource}`
- Examples: `slack_send_message`, `github_create_issue`
- Action-oriented (verbs first), specific to avoid conflicts with other servers

**Tool design**:
- Descriptions narrowly + unambiguously describe functionality
- Match actual functionality precisely
- Provide annotations: `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`
- Focused + atomic operations

**Response formats** — support both:
- **JSON** (`response_format="json"`): machine-readable, all fields + metadata, consistent types — for programmatic processing
- **Markdown** (`response_format="markdown"`, typically default): human-readable, headers/lists/formatting, human-readable timestamps, display names with IDs in parens, omit verbose metadata

**Pagination** for list tools:
- Always respect `limit` parameter
- Implement `offset` or cursor-based
- Return metadata: `has_more`, `next_offset`/`next_cursor`, `total_count`
- Never load all results into memory
- Default 20-50 items
- Example response shape: `{"total": 150, "count": 20, "offset": 0, "items": [...]}`

**Transport**:
- **Streamable HTTP** for remote servers + multi-client
- **stdio** for local integrations + CLI tools
- **Avoid SSE** (deprecated in favor of streamable HTTP)

(Remainder covers more design patterns + error handling — not sampled.)
