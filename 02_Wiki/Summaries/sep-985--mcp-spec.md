---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/985-align-oauth-20-protected-resource-metadata-with-rf.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/985-align-oauth-20-protected-resource-metadata-with-rf.md
title: "SEP-985: Align OAuth Protected Resource Metadata with RFC 9728"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-07-16 | Author: sunishsheth2009**

Brings the MCP spec's handling of OAuth 2.0 Protected Resource Metadata in line with **RFC 9728 Section 5**, which says use of the `WWW-Authenticate` header to convey resource metadata is `MAY`, not `MUST`. The current spec required clients to discover metadata via the `WWW-Authenticate` header; this SEP relaxes that to allow well-known URL discovery as an alternative.

**Updated rules**: Clients **MUST** interpret the `WWW-Authenticate` header AND fall back to probing for metadata at `/.well-known/oauth-protected-resource` if absent. Servers **SHOULD** return the `WWW-Authenticate` header (deviating from the RFC's `MAY` to make incremental authorization easier — e.g., scope-additional WWW-Authenticate challenges).

**Rationale**: large-scale multi-tenant deployments with centralized auth services find injecting `WWW-Authenticate` headers from backend services non-trivial (separation of concerns + infrastructure complexity). Pros for server developers: avoid complex header injection. Cons for clients: must implement metadata-probing fallback logic (added complexity).

Fully backward compatible: existing `WWW-Authenticate` support stays; `.well-known/...` is already MUST-supported in MCP; well-supporting clients gain interoperability.
