---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/blog/content/posts/2026-03-09-roadmap-update.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2026-03-09-roadmap-update.md
title: "Blog post: The 2026 MCP Roadmap (2026-03-09)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

David Soria Parra publishes the updated 2026 roadmap, organized around **priority areas** (not release dates) — reflecting that Working Groups are now the primary vehicle for protocol development.

**Top-four priority areas** (where SEPs receive expedited review and most maintainer capacity goes):

1. **Transport Evolution and Scalability** — evolve Streamable HTTP for horizontal scaling without state, plus standard `.well-known` metadata format so registries/crawlers learn server capability without connecting. Explicit decision: **not adding more official transports this cycle** — keeping the set small per MCP design principles.

2. **Agent Communication** — Tasks primitive (SEP-1686) shipped experimentally; needs lifecycle iteration: retry semantics on transient failure, expiry policies for retained results. Pattern is "ship experimental, gather production feedback, iterate" for other parts of MCP too.

3. **Governance Maturation** — every SEP currently requires full Core Maintainer review, regardless of domain — that's a bottleneck. Goal: documented **contributor ladder** (clear path from community participant to maintainer) and a **delegation model** so trusted Working Groups can accept SEPs in their domain. Core retains strategic oversight.

4. **Enterprise Readiness** — least defined of the four (intentionally). Pain points: audit trails, SSO-integrated auth, gateway behavior, configuration portability. **Enterprise WG does not yet exist** — call for someone to lead/join. Most enterprise work expected to land as **extensions** rather than core spec changes (don't make base protocol heavier for everyone else).

**SEP prioritization clarity**: SEPs aligned with priority areas move fastest. Outside-priority SEPs aren't rejected but face longer reviews and a higher bar for justification. Tip: bring SEPs with WG backing.

**On the Horizon section** (work the maintainers care about but aren't actively standing up): triggers and event-driven updates, streamed/reference-based result types, deeper security/auth, maturing extensions ecosystem. Active proposals already in review: SEP-1932 (DPoP), SEP-1933 (Workload Identity Federation).

**Get involved**: join a Working Group (the WG page lists what's active), propose a SEP, start an extension. Easiest first step: join a WG meeting.
