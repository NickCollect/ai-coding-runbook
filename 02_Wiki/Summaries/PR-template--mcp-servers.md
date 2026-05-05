---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/.github/pull_request_template.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/.github/pull_request_template.md
title: "MCP servers PR template"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Pull-request template for the `modelcontextprotocol/servers` repo. Notable section: **Publishing Your Server** — explicitly states "We are no longer accepting PRs to add servers to the README" and points to the MCP Server Registry for publication.

Required PR sections: Description, Server details (which server, changes to tools/resources/prompts), Motivation and Context, How Has This Been Tested? (with an LLM client; which scenarios), Breaking Changes (will users need to update their MCP client configurations?), Type of changes (bug fix / new feature / breaking change / documentation update).

**Checklist**: read the MCP Protocol Documentation, follow MCP security best practices, update server README, test with an LLM client, follow repo style guidelines, new and existing tests pass locally, appropriate error handling, document all environment variables and configuration options.
