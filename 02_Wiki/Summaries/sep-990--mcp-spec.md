---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md
title: "SEP-990: Enterprise IdP policy controls (Cross App Access)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-06-04 | Author: Aaron Parecki (@aaronpk)**

Defines an authorization extension enabling secure MCP authorization within enterprise environments by leveraging existing enterprise identity infrastructure. Augments the existing OAuth profile rather than replacing it; clients can opt in when needed.

**Goals**:
- For end users: removes the need to manually connect/authorize the MCP client to individual services within their organization
- For enterprise admins: enables visibility and control over which MCP servers are usable inside the org

**Flow** (high-level Mermaid sequence in the SEP): user logs into IdP via browser → IdP issues an Authorization Code → client exchanges for ID Token → client exchanges ID Token for an **ID-JAG** (ID JWT Authorization Grant); IdP evaluates org policy → returns ID-JAG → client uses ID-JAG at the MCP Authorization Server which validates and issues the MCP Access Token → MCP API calls proceed normally.

End-to-end implementation example exists at `oktadev/okta-cross-app-access-mcp`. Backward compatible (extension to existing OAuth profile). Adopted in the November 2025 spec release as part of the **Authorization Extensions** family alongside SEP-1046 (OAuth client credentials).
