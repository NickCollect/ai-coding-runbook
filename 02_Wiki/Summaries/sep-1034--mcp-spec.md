---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/1034--support-default-values-for-all-primitive-types-in.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/1034--support-default-values-for-all-primitive-types-in.md
title: "SEP-1034: Default values for all primitive types in elicitation schemas"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-07-22 | Author: Tapan Chugh**

Adds optional `default` to all primitive types in elicitation schemas (`StringSchema`, `NumberSchema`, `EnumSchema`), extending the existing support that only covered `BooleanSchema`. Enables servers to pre-populate elicited form fields for natural interactions.

**Real-world example**: an `email_reply` tool simplifies its signature by elicitng recipients/cc with sensible defaults — e.g., `recipients: "alice@company.com, bob@company.com"`, `cc: "john@company.com"` pulled from the original thread.

**Schema changes**: `StringSchema`, `NumberSchema`, `EnumSchema` each gain `default?` of the appropriate type. For `EnumSchema`, default must be one of the valid enum values. Clients that support defaults SHOULD pre-populate; clients that don't MAY ignore.

**Rationale**: follows precedent from `BooleanSchema` rather than inventing new mechanisms; optional → backward compatible; minimal client-implementation overhead (~10 lines of code in `fast-agent` reference impl).

**Alternatives rejected**: server-side templates (adds complexity), separate request type for forms with defaults (fragments API), required defaults (breaks existing).

Fully backward compatible. No new security concerns; existing guidance against requesting sensitive data still applies.
