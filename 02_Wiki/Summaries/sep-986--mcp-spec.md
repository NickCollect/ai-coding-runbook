---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/986-specify-format-for-tool-names.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/986-specify-format-for-tool-names.md
title: "SEP-986: Specify format for tool names"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Tool-use]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-07-16 | Author: kentcdodds**

Standardizes the allowed format for MCP tool names to remove implementation divergence:

- 1–64 characters
- Case-sensitive
- Allowed characters: `A-Z`, `a-z`, `0-9`, `_`, `-`, `.`, `/`
- **SHOULD NOT** contain spaces, commas, or other special characters
- **SHOULD** be unique within their namespace
- Examples: `getUser`, `user-profile/update`, `DATA_EXPORT_v2`, `admin.tools.list`

**Rationale**: communities and clients (VS Code, Claude) have already converged on this character set; allows hierarchical/namespaced names via `/` and `.`; supports both human-readable and machine-generated names; restricting spaces/commas avoids parsing ambiguity; 64-char cap is generous but prevents abuse.

**Not strictly backward compatible** for tools using disallowed characters or exceeding length: existing non-conforming names SHOULD be supported as aliases for at least one major version with a deprecation warning. Tool authors SHOULD update docs/code; a migration guide SHOULD be provided. Implementation: enforce validation at registration time. No security implications.
