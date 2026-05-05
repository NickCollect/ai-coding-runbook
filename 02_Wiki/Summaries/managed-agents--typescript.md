---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/typescript/managed-agents/README.md
title: "Managed Agents — TypeScript SDK"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Managed Agents flows for the `@anthropic-ai/sdk` TypeScript SDK. Same caveats as Python/Java: bindings here aren't exhaustive — for unknown classes/fields, WebFetch the SDK repo, don't extrapolate.

**Persistent agent rule**: store agent ID returned by `agents.create`, pass to every `sessions.create`. Don't call `agents.create` in the request path.

**Setup**: `npm install @anthropic-ai/sdk`. Client: `new Anthropic()` (env var) or `new Anthropic({ apiKey: "..." })`.

**Environment**: `client.beta.environments.create({ name, config: { type: "cloud", networking: { type: "unrestricted" } } })`.

**Agent**:
```typescript
const agent = await client.beta.agents.create({
  name, model: "claude-opus-4-7", system,
  tools: [
    { type: "agent_toolset_20260401", default_config: { enabled: true } },
    { type: "custom", name, description, input_schema: {...} },
  ],
});
```

**Session**:
```typescript
const session = await client.beta.sessions.create({
  agent: { type: "agent", id: agent.id, version: agent.version },
  environment_id: environment.id,
  title,
  resources: [{ type: "github_repository", url, mount_path,
                authorization_token: process.env.GITHUB_TOKEN, branch: "main" }],
});
```

**Send user message**: `client.beta.sessions.events.send(session.id, { events: [{ type: "user.message", content: [{ type: "text", text }] }] })`.

**Stream-first pattern**: open stream BEFORE (or concurrently with) sending message. Standalone iteration:
```typescript
const stream = await client.beta.sessions.stream(session.id);
for await (const event of stream) {
  switch (event.type) {
    case "agent.message": /* process content blocks */
    case "agent.custom_tool_use": /* session idle awaiting result */
    case "session.status_idle":
    case "session.status_terminated": break;
  }
}
```

**Custom tool result**: `events.send(session.id, { events: [{ type: "user.custom_tool_result", custom_tool_use_id, content: [{type, text}] }] })`.

**Polling**: `client.beta.sessions.events.list(session.id)`, iterate `events.data`.

**Files**: `client.beta.files.upload({ file: fs.createReadStream("data.csv") })` → `resources: [{ type: "file", file_id, mount_path }]`. List session output files: `client.beta.files.list({ scope_id: session.id, betas: ["managed-agents-2026-04-01"] })`. Download via `client.beta.files.download(id).arrayBuffer()` then `Buffer.from(...)` and write. **~1-3s indexing lag** between `session.status_idle` and output files appearing.

**Session mgmt**: `retrieve`, `list`, `delete`, `archive` on `client.beta.sessions`.

**MCP servers**: agent declares `mcp_servers: [{type: "url", name, url}]` + tools include `{type: "mcp_toolset", mcp_server_name}`. Session attaches `vault_ids: [vault.id]`.

Full streaming loop with custom tool dispatch shown — re-enter loop after sending tool results until no more `agent.custom_tool_use` events arrive.
