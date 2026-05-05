---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/plugins/mcp-spec/README.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/plugins/mcp-spec/README.md
title: "MCP Spec plugin for Claude (skills bundle)"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Skill, MCP-server, Slash-command]
concepts_referenced: []
---

A Claude Code / Cowork plugin shipped from inside the spec repo, bundling skills for researching and contributing to the MCP specification.

**Install**: `/plugin marketplace add modelcontextprotocol/modelcontextprotocol` in Claude Code; or in Cowork via Customize → Browse Plugins → Personal → Add marketplace from GitHub.

**Skills available**:

1. `/search-mcp-github <topic>` — searches across MCP GitHub discussions, issues, and pull requests (org-level discussions, spec-level discussions/issues/PRs). Searches both open AND closed items, important for understanding past decisions and historical context.
2. `/draft-sep <idea>` — researches and drafts a Specification Enhancement Proposal conforming to the SEP governance process. Gates whether the idea is SEP-worthy, interviews the author, checks existing spec coverage and prior art, then fills the template's required and optional sections and writes `seps/0000-{slug}.md`. Optionally opens a draft PR, backfills the SEP number, runs `npm run generate:seps` and `npm run format:docs`. Prerequisite: must be run from a local clone (the skill reads `seps/TEMPLATE.md` and writes into `seps/`). Asks clarifying questions (SEP type, breaking-change status, prototype, prior discussion, sponsor, security) before writing.
