---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/blog/content/posts/client_registration/index.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/client_registration/index.md
title: "Blog post: Evolving OAuth Client Registration in MCP (2025-08-22)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Paul Carleton (Core Maintainer) explains why MCP's adoption of OAuth 2.1 surfaced two distinct authorization-flow challenges and proposes complementary solutions.

**Background**: MCP authorization needs both a **client name** and a **redirect URL** that the auth server can trust to prevent malicious clients from impersonating legitimate ones (e.g., fake "Claude Desktop" on the consent screen). MCP's pattern of users connecting to arbitrary servers via URL means the unbounded set of clients × auth servers makes traditional pre-registration impossible.

**Goals identified**: clients shouldn't pre-register with every auth server; users shouldn't manually specify client IDs; auth servers want trusted metadata, single client ID per app, selective allow/deny, no unbounded database.

**Two distinct challenges** previously conflated:

### Challenge 1: Operational limitations of Dynamic Client Registration (DCR)
Open `/register` endpoint causes unbounded database growth, client expiry "black hole" (no way to invalidate without open-redirect risk), per-instance fragmentation (Windows + macOS Claude Desktop = two records), DoS vulnerability via unauthenticated writes. Clients must manage extra state and have no way to verify if a client ID is still valid.

**Solution: Client ID Metadata Documents (CIMD)** — instead of a registration step, the client ID is itself an HTTPS metadata URL (`client_id=https://app.com/oauth.json`). Auth server fetches metadata on-demand (cacheable). Pioneered by Bluesky. Sidesteps unbounded DB, no expiry management, naturally per-app, no unauthenticated write endpoint. Cost: clients need to host the metadata — trivial for web apps, requires backend infra for desktop apps.

### Challenge 2: Client identity and impersonation
Independent of DCR-vs-CIMD. Spectrum mapped on attacker cost vs mitigation complexity:
- **Domain-based attacks** (low cost, low mitigation) — register malicious callback URL claiming to be "Claude Desktop"; mitigate with trusted-domain restrictions / unknown-domain warnings.
- **Localhost impersonation** (medium cost) — malicious app on `localhost:8080` impersonating a legitimate desktop client. Desktop apps can't hold secrets.
- **Platform-attested apps** (high cost, future work) — OS attests software legitimacy.

**Solution: Software Statements** for desktop apps — client hosts a JWKS on its backend, auth-server-side verifies a short-lived signed JWT included in the OAuth flow. Raises bar significantly for impersonation. Works with both DCR AND CIMD (complementary, not competing).

**Future**: platform-level attestation (macOS/Windows/Android attesting binary identity).

**Path forward**: add CIMD support in favor of DCR (keep DCR for backward compat), layer software statements optionally for trust. Tracked in SEP-991 (CIMD) and SEP-1032 (Software Statements with DCR). Note: this post predates the November 2025 spec release that ultimately adopted CIMD via SEP-991.
