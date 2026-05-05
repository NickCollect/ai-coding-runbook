---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/1850-pr-based-sep-workflow.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/1850-pr-based-sep-workflow.md
title: "SEP-1850: PR-based SEP workflow"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Process | Created: 2025-11-20 | Accepted: 2025-11-28 (8-0-0 unanimous Discord vote) | Authors: Nick Cooper (@nickcoai), David Soria Parra (@davidsp) | Sponsor: David Soria Parra**

Formalizes the move of SEPs from GitHub Issues to **pull requests** that store proposals as markdown files in `seps/{NUMBER}-{slug}.md`. The PR number becomes the SEP number.

**Motivation**: issue-based process had dispersed content (proposal in issue body, implementation in separate PR — two numbers for the same SEP), no version history, unclear status management. File-based approach provides Git's review tooling, history, searchability, and a single thread of discussion.

**Author workflow** (5 steps):
1. Draft as `seps/0000-{slug}.md` using the SEP template
2. Open PR adding the file
3. Once PR number is known, amend the commit to rename `0000-{slug}.md` → `{N}-{slug}.md` and update header (`SEP-{N}` and `PR: #{N}`)
4. Find a sponsor from `MAINTAINERS.md`; tag potential sponsors
5. Sponsor agrees → assigns themselves and updates status to `Draft`

**Sponsor responsibilities**: review and feedback; request changes; manage status transitions (file `Status:` field + matching PR labels kept in sync); communicate via PR comments; initiate `In-Review`; raise to Core Maintainers (ensure SEP is presented at meeting with author/sponsor); ensure quality before advancing; track reference implementations until `Final`.

**Status flow**: `Draft → In-Review → Accepted → Final`; terminal states `Rejected` / `Withdrawn` / `Superseded` / `Dormant`. **Dormant**: SEP without sponsor for 6 months → Core Maintainers may close PR and mark dormant.

**Status management via labels**: sponsors apply PR labels matching the SEP's `Status:` field (`draft`, `in-review`, `accepted`, `final`); markdown is canonical (versioned with proposal); labels enable easy filtering.

**Backward compatibility**: existing issue-based SEPs remain valid and need no migration; future SEPs use the file location; maintainers may optionally backfill historical SEPs into `seps/`.

This SEP itself was the first using the new format — also standardized the SEP file structure (Abstract, Motivation, Specification, Rationale, Backward Compatibility, Security Implications, Reference Implementation).
