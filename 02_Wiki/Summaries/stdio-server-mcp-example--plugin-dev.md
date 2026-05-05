---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/mcp-integration/examples/stdio-server.json
title: "plugin-dev: mcp-integration stdio-server.json example"
summarized_at: 2026-05-05
entities_referenced: [Plugin, MCP-server]
concepts_referenced: []
---

Example `.mcp.json` showing three stdio MCP server configs from `plugin-dev`'s `mcp-integration` skill examples.

**Examples**:

1. `filesystem` — official `@modelcontextprotocol/server-filesystem` via npx, scoped to `${CLAUDE_PROJECT_DIR}` with `LOG_LEVEL: info`.

2. `database` — custom server at `${CLAUDE_PLUGIN_ROOT}/servers/db-server.js` with `--config ${CLAUDE_PLUGIN_ROOT}/config/db.json` arg, env vars `DATABASE_URL` (passed through) and `DB_POOL_SIZE: 10`.

3. `custom-tools` — Python `python -m my_mcp_server --port 8080` with `API_KEY: ${CUSTOM_API_KEY}` env var and `DEBUG: false`.

**Patterns shown**:
- npm package-based servers (`npx -y <pkg>`)
- Plugin-shipped servers (`${CLAUDE_PLUGIN_ROOT}/servers/...`)
- Python servers (`python -m`)
- Env var passthrough (`${API_KEY}`)
- Config injection via args
- Project-aware paths (`${CLAUDE_PROJECT_DIR}`)
