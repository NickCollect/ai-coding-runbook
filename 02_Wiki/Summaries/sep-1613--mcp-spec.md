---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/1613-establish-json-schema-2020-12-as-default-dialect-f.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/1613-establish-json-schema-2020-12-as-default-dialect-f.md
title: "SEP-1613: JSON Schema 2020-12 as default dialect for MCP"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-10-06 | Author: Ola Hungerford**

Establishes **JSON Schema 2020-12** as the default dialect for embedded schemas within MCP messages (tool `inputSchema`/`outputSchema` and elicitation `requestedSchema`). Schemas may declare alternative dialects via `$schema`. Resolves ambiguity that was causing validation failures and SDK divergence between draft-07 and 2020-12.

**Specification**:
- Embedded schemas **MUST** conform to JSON Schema 2020-12 when no `$schema` is present
- Schemas **MAY** include explicit `$schema` for a different dialect
- Schemas **MUST** be valid for their declared/default dialect; `inputSchema` MUST NOT be `null`
- For tools with no parameters, valid forms: `true`, `{}`, `{ "type": "object" }`, or `{ "type": "object", "additionalProperties": false }`
- Servers MUST generate 2020-12 by default; clients MUST validate per declared dialect and support at least 2020-12

**Why 2020-12**: Python SDK (via Pydantic) and Go SDK already prefer/use it; modern features (better validation, composition); community preference per PR #655 discussion; current stable JSON Schema version.

**Migration**: existing schemas without `$schema` default to 2020-12. Schemas using draft-07-specific keywords need updates: `dependencies` → `dependentSchemas` + `dependentRequired`; positional array validation → `prefixItems`. Migration strategy: add explicit `$schema` for draft-07 during transition, then update.

Open question: the spec generator script uses `typescript-json-schema` (draft-07 only). Short-term fix: patch to 2020-12 after generation; long-term: switch generators.

Related: SEP-1330 (enum schemas, depends on this); SEP-834 (full 2020-12 support, follow-up). Adopted in the November 2025 spec release.
