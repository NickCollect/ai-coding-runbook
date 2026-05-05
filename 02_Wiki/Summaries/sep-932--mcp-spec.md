---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/932-model-context-protocol-governance.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/932-model-context-protocol-governance.md
title: "SEP-932: MCP Governance"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Process | Created: 2025-07-08 | Author: David Soria Parra**

Establishes the formal MCP governance model. Defines a hierarchical structure (Contributors → Maintainers → Core Maintainers → Lead Maintainers — patterned after Python, PyTorch, Rust) and the SEP process.

**Roles**:
- **Contributors** — anyone filing issues/PRs/discussion. No formal membership.
- **Maintainers** — manage specific components (SDKs, docs, repos). Appointed by Core Maintainers; have write/admin on their repos.
- **Core Maintainers** — deep MCP knowledge; responsible for protocol direction; bi-weekly meetings; can veto maintainer decisions by majority.
- **Lead Maintainers** — Justin Spahr-Summers and David Soria Parra; can veto any decision; appoint/remove Core Maintainers; admin all infrastructure.

**Membership tied to individuals, not companies** — prevents single-org capture, maintains continuity when individuals change employers.

**SEP process** ensures all protocol changes get thorough review, community input, design documentation, and an implementation precedent.

This SEP introduced the foundational structure later expanded by SEP-994 (communication), SEP-1302 (WGs/IGs), SEP-1850 (PR-based SEP workflow), SEP-2085 (succession + amendment), SEP-2148 (contributor ladder), SEP-2149 (group governance template).
