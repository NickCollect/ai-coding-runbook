---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/mcp-integration/references/tool-usage.md
title: "Using MCP Tools in Commands and Agents"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Slash-command, Subagent, Plugin]
concepts_referenced: []
---

Reference doc on consuming MCP tools from Claude Code plugin commands and agents.

**Tool naming convention**: `mcp__plugin_<plugin-name>_<server-name>__<tool-name>`. Example: `mcp__plugin_asana_asana__asana_create_task`. Discover via `/mcp` (shows all servers, tools, schemas, full names).

**Pre-allowing tools in commands**:
```yaml
---
allowed-tools: ["mcp__plugin_asana_asana__asana_create_task",
                "mcp__plugin_asana_asana__asana_search_tasks"]
---
```
Wildcard `mcp__plugin_asana_asana__*` works but use sparingly.

**Agents** have broader tool access — don't need pre-allowed lists; can use any tool Claude deems necessary. Document expected tools in agent body.

**Tool-call patterns**:
1. Simple — validate → call → check errors → confirm.
2. Sequential — chain calls (search → create-if-missing → add-metadata).
3. Batch — loop calls + track success/failure → summary.
4. Error handling — retry on rate-limit/network (max 3); on persistent failure tell user + suggest config check.

**Schemas**: each MCP tool ships its own JSON schema (`{name, description, inputSchema: {type, properties, required}}`). Claude auto-structures tool input from schema.

**Response handling**: extract relevant data on success; classify errors (auth/rate-limit/validation) and translate to user-friendly messages without leaking internals; for batches report partial success ("Successfully processed 8 of 10").

**Performance**:
- Batch: single `search` with filters > many individual `get_item` calls.
- Cache results across operations.
- Parallel calls for independent tools (Claude handles automatically).

**UX**: provide progress feedback ("Searching Asana tasks..."); warn before long ops; user-friendly errors with remediation steps.

**Test scenarios**: success calls, missing auth, invalid params, non-existent resources, empty results, max results, special chars, concurrency.

**Common patterns**:
- CRUD operations bundle (create/read/update/delete tools allowlisted together).
- Search and process (search → filter → transform → present).
- Multi-step workflow (setup → validate → chain MCP calls → verify → report).

**Troubleshooting**: tools not available → check `/mcp`, exact tool names, restart after config changes. Calls failing → auth, schema mismatch, missing required params, `claude --debug` logs.
