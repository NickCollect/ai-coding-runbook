---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/2148-contributor-ladder.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/2148-contributor-ladder.md
title: "SEP-2148: MCP Contributor Ladder"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Process | Created: 2026-01-15 | Authors: David Soria Parra (@dsp-ant), Sarah Novotny (@sarahnovotny) | Sponsor: David Soria Parra**

Establishes the formal contributor ladder for MCP, defining roles, responsibilities, and advancement criteria from first-time contributor through Core Maintainer. Companion to SEP-2149 (group governance template).

**Roles** (with min timelines):

| Role | Summary | Min Timeline |
|---|---|---|
| **Contributor** | Anyone who contributes | Immediate |
| **Member** | Established active contributor; GitHub org membership, triage rights, eligible for WG/IG leadership | 2-3 months |
| **Maintainer** | Area steward with operational responsibility; merge rights | 6+ months as Member |
| **Core Maintainer** | Technical leadership; protocol stewardship; final decision authority | By invitation after sustained Maintainer contribution |
| **Lead Maintainer** | Ultimate project authority (founders); reserved for succession only |
| **Community Moderator** | CoC enforcement and community health (parallel track to technical) | Member status + appointment |

Timelines are floors, not targets. Trust is built through demonstrated behavior over time.

**Advancement requirements** (key examples):
- **Member**: ≥1 merged PR / accepted contribution; ongoing engagement; 2FA on GitHub; sponsored by 2 existing Members or Maintainers from **different organizations** (prevents single-org capture) OR by 1 Core/Lead Maintainer
- **Maintainer**: Member ≥6 months; demonstrated leadership in WG / significant initiatives; ability to represent MCP's interests above one's employer's; security and governance onboarding completed
- **Core Maintainer**: sustained Maintainer-level contribution over ≥6 months; cross-organizational trust; deep commitment; nominated by majority of Core Maintainers + Lead Maintainer approval (or direct Lead appointment)

**Inactivity policies**: Members 3 months → emeritus; Maintainers 6 months → emeritus (merge rights revoked); Core Maintainers 6 months → emeritus.

**Decision-making**: delegation as default — decisions made at lowest appropriate level. Core Maintainers handle escalation, cross-cutting issues, spec changes, Maintainer approval. Lead Maintainer handles only contested governance or when CMs can't reach consensus.

**Escalation matrix** spelled out: technical PR disagreement → Maintainer (5 days) → Core Maintainer; WG/IG disputes → Lead → CM (5 days); CM disagreements → Lead Maintainer (10 days); CoC violations → Community Moderator (immediate); security → Core Maintainer / Lead (immediate).

**Multiple contribution pathways recognized**: code (SDK dev, testing, tooling); specification work (drafting, SEP authorship, design); documentation; community building; quality and security.

**WG Lead / IG Facilitator roles**: special form of leadership not requiring Maintainer status; Member status minimum; sponsored by 2+ Core Maintainers or 1 Lead Maintainer; experience valuable for advancement to Maintainer.

**Community Moderator**: parallel role for CoC enforcement; Member status + Core/Lead Maintainer sponsor; recused from incidents involving themselves.

Modeled on Kubernetes community membership structures, adapted for MCP. Implementation: nomination issue templates (checklist appendix in SEP); updated `MAINTAINERS.md` format.
