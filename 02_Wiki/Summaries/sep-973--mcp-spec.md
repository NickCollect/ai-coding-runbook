---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/973-expose-additional-metadata-for-implementations-res.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/973-expose-additional-metadata-for-implementations-res.md
title: "SEP-973: Expose icons + websiteUrl on Implementation/Tool/Resource/Prompt"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-07-15 | Author: @jesselumarie**

Adds two optional fields to `Implementation`: `icons` (array) and `websiteUrl`. The `icons` field is also added to `Tool`, `Resource`, and `Prompt` schemas — enabling clients to display visual affordances and direct links to documentation.

**Icon interface**: `src` (URI to icon resource or base64 data URI), `mimeType` (optional override), `sizes` (optional, e.g. `48x48`, `any`, or multiple `48x48 96x96`). Clients **MUST** support `image/png` and `image/jpeg`; **SHOULD** support `image/svg+xml` (with security caution since SVGs can contain JavaScript) and `image/webp`. Consumers MUST ensure URLs come from trusted domains.

**Implementation interface** extends `BaseMetadata` with `version`, optional `icons`, optional `websiteUrl`. Both fields optional → fully backward compatible (existing implementations ignored fields fall back to existing behavior). Builds on web-manifest (MDN) prior art and consolidates prior PRs #417 and #862.

No new security implications.
