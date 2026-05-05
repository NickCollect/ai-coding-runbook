---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/src/memory/README.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/src/memory/README.md
title: "Knowledge Graph Memory MCP server"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

TypeScript MCP server implementing **persistent memory via a local knowledge graph** — lets Claude (or any MCP client) remember information about the user across chats.

**Core concepts**:

- **Entities** — primary nodes. Each has a unique name (identifier), entityType (e.g., "person", "organization", "event"), and a list of observations. Example: `{name: "John_Smith", entityType: "person", observations: ["Speaks fluent Spanish"]}`.
- **Relations** — directed connections between entities, stored in active voice. Example: `{from: "John_Smith", to: "Anthropic", relationType: "works_at"}`.
- **Observations** — discrete pieces of info attached to specific entities. Stored as strings; can be added/removed independently; should be atomic (one fact per observation).

**API tools** include `create_entities` (array of entity objects), and additional tools (continued beyond this excerpt) for `create_relations`, `add_observations`, `delete_entities`, `delete_observations`, `delete_relations`, `read_graph`, `search_nodes`, `open_nodes`, etc. — full CRUD on the knowledge graph plus query/search.

This is one of the more popular reference servers since it gives MCP clients a simple persistence mechanism for cross-session memory without requiring an external database.
