---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/1730-sdks-tiering-system.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/1730-sdks-tiering-system.md
title: "SEP-1730: SDKs tiering system"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-10-29 | Authors: Inna Harper, Felix Weinberger**

Establishes a three-tier classification for MCP SDKs to give users objective signals about feature support, maintenance commitment, and quality.

**Tier 1: Fully Supported**
- All conformance tests pass (100%)
- New protocol features land before each spec release (within the 2-week RC → release window)
- Triage issues within 2 business days; resolve security/critical bugs within 7 days
- Stable releases with documented versioning
- Comprehensive docs with examples for all features
- Published dependency update policy

**Tier 2: Commitment to be Fully Supported**
- 80% conformance tests pass
- New protocol features within 6 months
- Active issue tracking, ≥1 stable release
- Basic docs covering core features
- Published roadmap toward Tier 1 (or transparent statement of intent to remain Tier 2 indefinitely)

**Tier 3: Experimental**
- No feature-completeness guarantees
- No stable release requirement
- No timeline commitments
- Suitable for niche/specialized implementations

**Conformance testing**: simplified initial version — each SDK ships an "Everything" example server (similar to `modelcontextprotocol/servers/src/everything`) implementing a defined spec; a Conformance Test Client runs test cases against it (execute tools, get prompts, get completions, get resource templates, receive notifications). Gradual move toward full conformance later (tracked in #1627).

**Tier advancement**: maintainers self-assess → submit application with evidence → 2-week community review → automated conformance + GitHub stats validation → MCP-maintainer decision.

**Tier relegation**: auto-validation if conformance fails for 4 weeks (Tier 1) or >20% of tests fail for 4 weeks (Tier 2); or if issues unaddressed for 2 months.

**Why three tiers**: Tier 1 ensures fully-supported choice; Tier 2 provides clear improvement path; Tier 3 allows experimentation without barriers.

Implementation timeline: simplified conformance suite Nov 4, 2025; SDK self-assessments Nov 14; initial assignments before the November spec release. Adopted in the November 2025 release as part of SDK Support Standardization.
