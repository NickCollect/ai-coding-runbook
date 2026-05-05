---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact.md
source_url: https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/redact
title: "Redact Memory Version"
summarized_at: 2026-05-05
entities_referenced: [Memory-store]
concepts_referenced: []
---

`POST /v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact` — redact (scrub) the content of a stored memory version.

**Path params:** `memory_store_id`, `memory_version_id`. No request body documented. Use this when historical content must be removed for compliance/PII reasons while keeping the version record itself intact. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
