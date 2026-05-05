---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/2149-working-group-charter-template.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/2149-working-group-charter-template.md
title: "SEP-2149: WG/IG governance + charter template"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Process | Created: 2025-01-15 | Authors: David Soria Parra, Sarah Novotny | Sponsor: David Soria Parra**

Companion to SEP-2148 (contributor ladder). Establishes shared governance rules and a standardized charter template for Working Groups (WGs) and Interest Groups (IGs). Addresses community feedback about unclear authority delegation and inconsistent processes across groups.

**Two parts**:

### Part 1: Group Governance (rules all groups must follow)

- **Leadership** — Leads (WGs) / Facilitators (IGs); Member-status minimum; sponsored by 2+ Core Maintainers or 1 Lead Maintainer. WG Leads commit 2-3 hrs/week.
- **Leadership responsibilities** — meetings/agendas/notes within 48 hours; member list maintenance in `modelcontextprotocol/access`; broad representative recruitment. WG Leads additionally drive SEPs through resolution; triage/close in-scope SEPs (with documented rationale; authors can appeal); maintain WG roadmap; quarterly status updates.
- **Participation tiers** — Observer / Participant / WG Member / Lead. WG Members earned via 3 months of sustained participation, nomination, no objections in 7 days.
- **Decision-making** (WGs):
  1. **Lazy consensus** (default) — propose with 5-day (minor) or 10-day (significant) deadline; silence is consent; any WG Member may block with documented objection
  2. **Formal vote** — triggered by block or by Lead/3+ WG Members; quorum 50% of active members; simple majority for routine, 2/3 for scope changes; CM feedback advisory unless explicitly binding
  3. **Escalation to Core Maintainers**
- **Escalation** — direct CM escalation for: scope disputes, authority disputes, cross-group conflicts, CoC issues, membership disputes. Designated CM (without shared org affiliation with parties) resolves; initial response within 5 business days.
- **Meetings** — leads set frequency; all open to community; published 7 days ahead on `meet.modelcontextprotocol.io`; agendas + notes in GitHub Discussions Meeting Notes category.
- **Reporting** — WGs provide quarterly updates (end of Jan/Apr/Jul/Oct); IGs no formal reporting.
- **Lifecycle** — WG formation: PR for `docs/community/<name>/overview.mdx` (Maintainer approval) + charter PR (Core Maintainer approval). IG formation: template in `#wg-ig-group-creation`, reviewed by CM, sponsored by 2+ CMs or 1 LM. Retirement: by Lead/CM with rationale + Core/Lead Maintainer approval; or auto-retirement when work stops.

### Part 2: Charter Template (per-group structure)

9 sections required: Group Type (WG or IG); Mission Statement (2-3 sentences); Scope (in/out, related groups); Leadership (table); **Authority & Decision Rights** (WG only — explicit authority table); Membership; Operations; Deliverables & Success Metrics (WG only); Changelog. Stored at `docs/community/<group-name>/charter.mdx`.

**Rationale**: separating fixed governance from per-group charter prevents accidental process divergence; explicit authority tables address the "unclear authority" pain point (WGs only — IGs produce recommendations, not binding decisions); tiered participation enables low-commitment learning + formal accountability; lazy consensus default reduces meeting burden.

**Transition for existing groups**: grandfathered, but must produce conforming charter within **8 weeks** or face retirement.

Modeled on Kubernetes governance, adapted for MCP.
