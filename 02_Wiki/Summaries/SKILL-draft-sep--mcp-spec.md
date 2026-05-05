---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/plugins/mcp-spec/skills/draft-sep/SKILL.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/plugins/mcp-spec/skills/draft-sep/SKILL.md
title: "draft-sep skill: produce a Specification Enhancement Proposal"
summarized_at: 2026-05-05
entities_referenced: [Skill, MCP-server, Slash-command]
concepts_referenced: []
---

User-invocable Skill (`name: draft-sep`, `arguments: [idea]`) that walks an author through producing an MCP Specification Enhancement Proposal conforming to `docs/community/sep-guidelines.mdx` and `seps/TEMPLATE.md`. Six phases — gate, interview, research, draft, checkpoint, optional PR — must be completed in order; do not start writing until gate, interview, and research are complete.

**Prerequisite**: must run from a local clone of `modelcontextprotocol/modelcontextprotocol` (or fork). Verifies `seps/TEMPLATE.md` exists; determines the **canonical remote** (origin if it points to upstream, else `upstream`); fetches and ensures local `main` is current.

**Phase 1 — Gate**: redirect away if the idea is bug fix, typo, doc clarification, example, or minor schema fix. Proceed if it's a new/changed protocol feature, breaking change, governance/process change, or anything controversial enough to need a design document.

**Phase 2 — Interview** (six questions): SEP type (Standards Track / Extensions Track / Informational / Process — Extensions Track requires WG and Extension Maintainer commitment plus reference implementation per SEP-2133); breaking change?; prototype status (working prototype required for `accepted`, complete reference implementation required for `final`); where was it discussed (Discord/WG/IG link becomes consensus evidence); author + sponsor (sponsor is required to enter `draft` status; absent → `Sponsor: None` and 6-month dormant clock starts); security implications.

**Phase 3 — Research** (six steps with findings captured): current spec coverage via `SearchModelContextProtocol` MCP server tool (or grep `docs/specification/draft/`); prior art via `/search-mcp-github`; overlapping SEPs via grep `seps/*.md`; design-principle and roadmap fit; schema touch-points via grep `schema/draft/schema.ts`; read 2-3 Final SEPs as exemplars.

**Phase 4 — Draft**: read `seps/TEMPLATE.md`, write `seps/0000-{slug}.md`. Required sections must be filled (write "none identified" with reasoning rather than omitting). Preamble notes: `Status:` left blank (sponsor sets it), `Type:` from Q1, `Created:` today, `Author(s):` and `Sponsor:` from Q5, `PR:` placeholder filled in Phase 6.

**Phase 5 — Checkpoint**: tell user the file path + one-line summary of each section. **Ask** before opening PR.

**Phase 6 — Open PR** (only with explicit yes): SEP-1850 amend-based flow — branch from canonical/main, commit, push to `origin`, open draft PR, capture PR number, rename file `0000-{slug}.md` → `{N}-{slug}.md`, fix SEP number in title, fill PR link, run `npm run generate:seps` and `npm run format:docs`, amend commit, force-push. If sponsor is None, tag 1-2 maintainers from `MAINTAINERS.md` and share in Discord.
