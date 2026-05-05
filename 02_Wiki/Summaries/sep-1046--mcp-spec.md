---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/1046-support-oauth-client-credentials-flow-in-authoriza.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/1046-support-oauth-client-credentials-flow-in-authoriza.md
title: "SEP-1046: OAuth client credentials flow in authorization"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-07-23 | Author: Darin McAdams (@D-McAdams)**

Adds the OAuth **client credentials flow** to the MCP authorization spec to enable machine-to-machine scenarios where no end user is available for interactive authorization. The original spec mentioned this flow but it was dropped in subsequent revisions.

**Constrained options** (intentionally narrow to maximize interop / minimize SDK complexity):
1. **JWT Assertions per RFC 7523** — RECOMMENDED
2. **Client Secrets via HTTP Basic auth** — allowed for max compatibility with existing systems

Other options (mTLS, etc.) deliberately not included.

**Future direction**: while the spec encourages RFC 7523, it doesn't yet specify how to populate JWT contents or how to discover the JWKS URI. Future iterations will, pending maturity of: WIMSE Headless JWT Authentication (for JWT contents) and Client ID Metadata (for JWKS URI). Practical guidance: implementers needing to ship ASAP will use client secrets; JWT Assertions represent the longer-term direction.

The spec overview gets updated to describe each flow and when applicable, plus a clarification that implementers MAY support other flows beyond the spec baseline.

Fully backward compatible (additive). Refers to existing OAuth security guidance. Adopted in the November 2025 spec release as one of the **Authorization Extensions** alongside SEP-990 (Cross App Access).
