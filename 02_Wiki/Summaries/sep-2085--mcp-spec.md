---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/2085-governance-succession-and-amendment.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/2085-governance-succession-and-amendment.md
title: "SEP-2085: Governance succession and amendment procedures"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Process | Created: 2025-12-05 | Author + Sponsor: David Soria Parra**

Adds two missing procedures to MCP governance: **Lead Maintainer succession** and **governance amendment**. Establishes them now while leadership is stable so future scenarios have clear guidance.

**Succession**:
- Begins on the Lead Maintainer's written notice OR determination by remaining Lead Maintainer(s) or Core Maintainers that the LM cannot continue
- If 1+ Lead Maintainer(s) remain: they appoint a successor (majority vote if multiple); remaining LM(s) continue to govern until appointed
- If NO Lead Maintainers remain: Core Maintainers appoint a successor by majority vote within **30 days**; project operates by 2/3 Core Maintainer vote during the interregnum

**Amendment** to the governance structure:
- Only Lead Maintainers may propose
- Must be approved by **2/3 of all Core Maintainers**
- Proposals must be in writing with rationale, specific amendment language, **5-day minimum comment period** before voting, recorded vote of Core Maintainers

**Rationale**:
- Succession: continuity, fallback authority, time-bound (30-day cap), supermajority interim governance ensures broad support during transition
- Amendment: limiting proposal authority to LMs prevents governance churn while allowing those with deepest investment to drive changes; 2/3 CM approval ensures broad support; 5-day window is short enough to allow ≥1 bi-weekly meeting cycle while enabling timely decisions

**Alternatives rejected**: open elections (slow/disruptive in critical transitions), amendment by any maintainer (instability), 30-day comment periods (excessive given existing meeting cadence).

Implementation: adds Succession and Amendment sections to `docs/community/governance.mdx`. Backward compatible (additive). No direct security implications (indirectly supports security via continuous responsible stewardship).
