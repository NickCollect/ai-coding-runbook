---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/991-enable-url-based-client-registration-using-oauth-c.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/991-enable-url-based-client-registration-using-oauth-c.md
title: "SEP-991: URL-based client registration via OAuth Client ID Metadata Documents"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-07-07 | Authors: Paul Carleton (@pcarleton), Aaron Parecki (@aaronpk)**

Adopts **OAuth Client ID Metadata Documents (CIMD)** — per `draft-parecki-oauth-client-id-metadata-document-03`, pioneered by Bluesky — as an additional MCP client-registration mechanism. Clients use HTTPS URLs as their `client_id`; the URL points to a JSON document describing the client. The change makes CIMD a `SHOULD` and downgrades DCR to `MAY`.

**Target use case** (the most common in MCP): user wants to connect a client to a server they've discovered, neither client developer nor server operator have heard of each other, both need to establish trust without prior coordination.

**Sequence**: client sends authorization request with `client_id=https://app.com/oauth/metadata.json` → AS detects URL-formatted client_id → AS fetches the metadata → validates `client_id` matches URL, redirect_uris in allowed list, document structure, domain trust policy → if valid, displays consent → continues OAuth flow → caches metadata respecting HTTP headers (max 24h recommended).

**Client requirements**: host metadata at HTTPS URL with path component; metadata must include `client_id` (matching URL exactly), `client_name`, `redirect_uris`, `token_endpoint_auth_method` (`none` for public clients; can use `private_key_jwt` since metadata can include public keys).

**Server requirements**: SHOULD fetch metadata when encountering URL-formatted client_ids; MUST validate matching client_id; SHOULD cache; MUST validate redirect URIs match the metadata document. Discovery: `client_id_metadata_document_supported: true` in OAuth metadata.

**Risks documented**: localhost URL impersonation (cannot be fully prevented by CIMD alone — same risk as DCR; deferred to future platform attestation or short-lived JWT signing); SSRF (mitigate by URL/IP validation); DDoS (low amplification, aggressive caching mitigates); CIMD spec maturity (still draft; commit to evolving with it); client implementation burden (need an HTTPS endpoint — trivial for web apps, requires backend for desktop); fragmentation of auth approaches.

Fully backward compatible alongside existing pre-registration and DCR. Prototype implementation at `modelcontextprotocol/typescript-sdk PR 839`. Adopted in the November 2025 spec release as the new default for the open-ecosystem case.
