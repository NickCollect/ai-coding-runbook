---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/994-shared-communication-practicesguidelines.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/994-shared-communication-practicesguidelines.md
title: "SEP-994: MCP Community Communication Practices"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Process | Created: 2025-07-17 | Author: @localden**

Establishes the MCP project's communication strategy and framework. Defines official contributor channels, usage guidelines per channel, and decision-documentation requirements.

**Three primary channels**:

1. **Discord** — real-time / ad-hoc discussion among **contributors** (NOT general MCP support). Public channels by default for community engagement, SDK and tooling discussions, WG/IG discussions, onboarding, office hours. Private channels reserved for security incidents (CVEs, vulnerabilities), people matters (maintainer / CoC discussions), urgent coordination. **All technical and governance decisions must be documented publicly in GitHub.**

2. **GitHub Discussions** — structured long-form discussion: roadmap planning, announcements/release comms, community polls/consensus-building, contextualized feature requests.

3. **GitHub Issues** — actionable items: bug reports with repro steps, doc improvements, CI/CD/infra issues, release tasks/milestones.

Security-sensitive issues follow the separate process in `SECURITY.md`.

**Decision records**: technical decisions in GitHub Issues + SEPs; spec changes in MCP website changelog; process changes in community docs; governance decisions in Issues + SEPs. Documentation includes decision makers, background/motivation, options considered, rationale, implementation steps.

**Rationale**: public by default → transparency; private when necessary → security/personal; channel separation → discussions stay organized and searchable; documentation requirements → decisions preserved and discoverable.

Result: published at `modelcontextprotocol.io/community/communication`. Set the stage for SEP-1302 (WG/IG governance).
