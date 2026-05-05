---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/1330-elicitation-enum-schema-improvements-and-standards.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/1330-elicitation-enum-schema-improvements-and-standards.md
title: "SEP-1330: Elicitation enum schema standards-compliance + multi-select"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-08-11 | Author: chughtapan**

Improves enum schemas in MCP. Two changes: (1) deprecates the non-standard `enumNames` property in favor of standards-compliant JSON Schema patterns; (2) introduces multi-select enums in addition to single-select.

**New enum types**:
- `UntitledSingleSelectEnumSchema` — `type: "string"`, `enum: string[]`. Plain JSON Schema enum keyword. (No change from existing untitled use.)
- `TitledSingleSelectEnumSchema` — uses `oneOf: [{const, title}]` to attach display titles. Standards-compliant.
- `UntitledMultiSelectEnumSchema` — `type: "array"`, `items.enum`, optional `minItems`/`maxItems`. Lets users pick multiple values without titles.
- `TitledMultiSelectEnumSchema` — `type: "array"`, items with `oneOf: [{const, title}]`. Multi-pick with display titles.
- `LegacyEnumSchema` — preserves the existing `enum` + `enumNames` pattern, marked Legacy until a project-wide deprecation strategy lands.

**Final `EnumSchema`** is a union of all five.

**ElicitResult extension**: `content` may now include `string[]` to return multi-select results — `content?: { [key: string]: string | number | boolean | string[] }`.

**Rationale**: standards-compliant patterns work with existing JSON Schema validators; minimal client overhead (showing checkboxes vs radio buttons differs by ~few lines of code); follows precedent of how Booleans handled defaults.

Schema, TypeScript SDK, and Python SDK PRs linked. Working demo available. Fully backward compatible (existing `enumNames` keeps working). No security implications. Builds on SEP-1613 (JSON Schema 2020-12 default).
