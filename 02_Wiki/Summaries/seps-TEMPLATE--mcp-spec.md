---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/TEMPLATE.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/TEMPLATE.md
title: "SEP template (canonical structure)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Standard template every Specification Enhancement Proposal must follow.

**Header preamble**: `Status` (Draft → In-Review → Accepted → Rejected → Withdrawn → Final → Superseded → Dormant); `Type` (Standards Track | Informational | Process — note Extensions Track was added by SEP-2133 but not yet backfilled here); `Created` date; `Author(s)` with email and `@github-username`; `Sponsor` (`@github-username` or `None` if seeking sponsor); `PR` link.

**Required sections** (above the `---` rule):

- **Abstract** — ~200-word technical summary
- **Motivation** — why the change is needed; why current spec is inadequate. SEPs without sufficient motivation may be rejected outright.
- **Specification** — detailed enough to allow competing interoperable implementations. For protocol changes: new message formats, endpoints/methods, behavioral requirements, error handling. For process changes: procedures, roles, timelines.
- **Rationale** — why these design decisions; alternates considered; references to prior art; objections; consensus evidence.
- **Backward Compatibility** — required when introducing incompatibilities; describe what breaks, severity, transition handling, migration paths. State explicitly if there are no concerns.
- **Security Implications** — new attack surface, privacy, auth changes, validation needs. State explicitly if none.
- **Reference Implementation** — link or describe; required before `Final` status. "Rough consensus and running code" guides protocol resolution.

**Optional sections**: Performance Implications, Testing Plan, Alternatives Considered, Open Questions, Acknowledgments.
