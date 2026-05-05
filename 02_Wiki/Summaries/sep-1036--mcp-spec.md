---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/1036-url-mode-elicitation-for-secure-out-of-band-intera.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/1036-url-mode-elicitation-for-secure-out-of-band-intera.md
title: "SEP-1036: URL mode elicitation for secure out-of-band interactions"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-07-22 | Authors: Nate Barbettini (@nbarbettini), Wils Dawson (@wdawson)**

Introduces a `url` mode for the existing elicitation client capability, enabling secure out-of-band interactions that bypass the MCP client. Critical for sensitive credential collection, third-party OAuth flows, and payment processing — where data must NEVER pass through the MCP client.

**Two elicitation modes**:
- **form** mode (in-band, existing): server requests structured data via JSON schema; client renders a form
- **url** mode (out-of-band, new): server directs user to an external URL in their browser

**Capability declaration** (breaking change): clients **MUST** specify which modes they support: `"elicitation": { "form": {}, "url": {} }`. Backward compatibility: empty `"elicitation": {}` is equivalent to `form` only.

**URL elicitation request fields**: `url`, `elicitationId` (unique), `message` (human-readable rationale).

**Response**: same three-action model — `accept` / `decline` / `cancel`. The actual interaction happens out-of-band; the client doesn't see the outcome unless the server sends a `notifications/elicitation/complete` notification (which references `elicitationId`).

**URLElicitationRequiredError** (`-32042`): server can return this error when a request can't proceed until elicitation completes — equivalent to sending an `elicitation/create`. Client may auto-retry the failed request after the elicitation completes.

**Why extend elicitation** rather than create new mechanism: both serve the same fundamental purpose (gathering info from users); two parallel mechanisms is confusing.

**Security**: only HTTPS URLs allowed; SSRF prevention; explicit user consent before opening URLs; clearly display target domains; secure browser context that prevents inspection of inputs; servers verify the user completing the flow is the same one who initiated; bind elicitation state to authenticated sessions; rate limiting; logging.

Adopted in the November 2025 spec release.
