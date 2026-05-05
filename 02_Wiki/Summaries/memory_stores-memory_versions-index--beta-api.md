---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/memory_stores/memory_versions.md
source_url: https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions
title: "Memory Versions"
summarized_at: 2026-05-05
entities_referenced: [Memory-store]
concepts_referenced: []
---

Sub-resource page for **Memory Versions** inside a Memory Store, rooted at `/v1/memory_stores/{memory_store_id}/memory_versions`. Every memory write produces a new immutable version snapshot; this sub-resource exposes the audit/redaction surface for that history.

**Endpoints on this page:**

- `GET .../memory_versions` — List versions.
- `GET .../memory_versions/{memory_version_id}` — Retrieve a single version (with `view: basic|full`).
- `POST .../memory_versions/{memory_version_id}/redact` — Redact the content of an already-stored version (e.g. for compliance).

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
