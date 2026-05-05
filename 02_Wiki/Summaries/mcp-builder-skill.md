---
type: summary
source: 01_Raw/github/anthropics/skills/skills/mcp-builder/SKILL.md
title: "anthropics/skills: mcp-builder SKILL.md"
summarized_at: 2026-05-05
entities_referenced: [Skill, MCP-server]
concepts_referenced: []
---

Skill for creating high-quality MCP (Model Context Protocol) servers — Python (FastMCP) or Node/TypeScript (MCP SDK). Triggers on building MCP servers to integrate external APIs.

**Quality measure**: how well it enables LLMs to accomplish real-world tasks.

**4-phase workflow**:

**Phase 1 — Deep Research and Planning**:
- API coverage vs workflow tools: balance comprehensive endpoint coverage with specialized workflow tools. When uncertain, prioritize comprehensive coverage.
- Tool naming: clear/descriptive, consistent prefixes (`github_create_issue`, `github_list_repos`), action-oriented.
- Context management: concise descriptions; filter/paginate results.
- Actionable error messages with specific suggestions.
- Study MCP spec at `https://modelcontextprotocol.io/sitemap.xml` (then fetch `.md`).

**Recommended stack**:
- Language: **TypeScript** (high-quality SDK, MCPB compat, AI models good at TS, static typing).
- Transport: **Streamable HTTP** for remote (stateless JSON, simpler scale), **stdio** for local.

**Framework docs** to load via WebFetch:
- TypeScript: `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md` + `reference/node_mcp_server.md`.
- Python: `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md` + `reference/python_mcp_server.md`.
- Best practices: `reference/mcp_best_practices.md`.

**Phase 2 — Implementation**: project structure (per language guide), shared utilities (API client + auth, error handling, response formatting JSON/Markdown, pagination). Per tool: input schema (Zod TS / Pydantic Python with constraints + descriptions), output schema (define `outputSchema` for structured data; use `structuredContent`), description, async impl with proper errors and pagination, annotations (`readOnlyHint`/`destructiveHint`/`idempotentHint`/`openWorldHint`).

**Phase 3 — Review and Test**: code quality (DRY, consistent errors, full type coverage, clear descriptions). Build/test: TypeScript via `npm run build` + MCP Inspector (`npx @modelcontextprotocol/inspector`); Python via `python -m py_compile` + Inspector.

**Phase 4 — Create Evaluations**: test whether LLMs can effectively use the server on realistic complex questions. Process: tool inspection → content exploration (READ-ONLY) → 10-question generation → answer verification (solve each yourself).

**Question requirements**: independent, read-only, complex (multiple tool calls + deep exploration), realistic (real human use case), verifiable (single clear answer string-comparable), stable (won't change over time).

**Output XML format**:
```xml
<evaluation>
  <qa_pair>
    <question>...</question>
    <answer>...</answer>
  </qa_pair>
</evaluation>
```

**Reference library**: load `mcp_best_practices.md` first; SDK docs during Phase 1/2; lang-specific guides during Phase 2; evaluation guide during Phase 4.
