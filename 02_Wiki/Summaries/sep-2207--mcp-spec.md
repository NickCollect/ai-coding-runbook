---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/2207-oidc-refresh-token-guidance.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/2207-oidc-refresh-token-guidance.md
title: "SEP-2207: OIDC refresh token guidance"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Accepted | Type: Standards Track | Created: 2026-02-04 | Author: Wils Dawson (@wdawson) | Sponsor: Paul Carleton**

Provides guidance for MCP implementations on **refresh token issuance and requests**, particularly when Authorization Servers support the OIDC `offline_access` scope. Bridges the OAuth 2.1 / OIDC gap that's blocking real-world MCP deployments.

**Problem**: in pure OAuth 2.1 there's no standard mechanism for clients to explicitly request refresh tokens — AS decides based on client metadata. In OIDC (and many AS implementations adopting the convention), clients use the `offline_access` scope to explicitly request them. This creates ecosystem-wide problems: major MCP clients (Cursor, Claude, VS Code) aren't asking for refresh tokens because they don't know whether the AS supports/expects/requires `offline_access`; resource servers shouldn't include `offline_access` in their metadata since it's not a resource concern; AS behavior varies inconsistently.

**Client requirements**:
- Clients SHOULD include `refresh_token` in their `grant_types` client metadata
- When AS metadata's `scopes_supported` contains `offline_access`, clients MAY add `offline_access` to the scope list
- Clients MUST NOT assume they'll receive a refresh token even with these signals

**Resource server requirements**:
- SHOULD NOT include `offline_access` in `WWW-Authenticate` header's `scope` parameter
- SHOULD NOT include `offline_access` in `scopes_supported` in Protected Resource Metadata
- (Reasoning: refresh tokens aren't a resource requirement; this would semantically misrepresent the resource)

**Why not always issue refresh tokens?** OAuth 2.1 requires clients to register their grant types. Clients without `refresh_token` either can't store them securely or have no mechanism to use them — issuing them would waste AS resources and create security risks.

Fully backward compatible. Reference implementations forthcoming in TS and Python SDKs. Acknowledgments: Aaron Parecki (OAuth/OIDC), Paul Carleton (MCP auth), Simon Russell (OIDC deployment experience).
