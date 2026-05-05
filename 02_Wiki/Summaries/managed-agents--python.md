---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/python/managed-agents/README.md
title: "Managed Agents — Python SDK"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Managed Agents flows for the `anthropic` Python SDK. Caveat at top: bindings here aren't exhaustive — for unknown classes/fields, WebFetch the Python SDK repo / Anthropic docs rather than guess.

**Persistent agent rule**: store the agent ID returned by `agents.create` and pass to every subsequent `sessions.create`. Don't call `agents.create` in the request path. Anthropic CLI handles agents/environments from version-controlled YAML.

**Setup**: `pip install anthropic`. Client: `anthropic.Anthropic()` (env var) or with `api_key=`.

**Environment**: `client.beta.environments.create(name=..., config={"type": "cloud", "networking": {"type": "unrestricted"}})`.

**Agent**:
```python
agent = client.beta.agents.create(
    name="...",
    model="claude-opus-4-7",
    system="...",
    tools=[
        {"type": "agent_toolset_20260401", "default_config": {"enabled": True}},
        {"type": "custom", "name": "run_tests", "description": "...",
         "input_schema": {...}},
    ],
)
```

**Session**:
```python
session = client.beta.sessions.create(
    agent={"type": "agent", "id": agent.id, "version": agent.version},
    environment_id=environment.id,
    title="...",
    resources=[{"type": "github_repository", "url": ..., "mount_path": ...,
                "authorization_token": os.environ["GITHUB_TOKEN"], "branch": "main"}],
)
```

**Send user message**: `client.beta.sessions.events.send(session_id=..., events=[{"type": "user.message", "content": [{"type": "text", "text": "..."}]}])`.

**Stream-first pattern (CRITICAL)**: open `client.beta.sessions.stream(...)` BEFORE sending the message — stream only delivers events that occur after it opens; stream-after-send means early events arrive buffered together.

**Stream events** to watch: `agent.message` (text + tool blocks), `agent.custom_tool_use` (session goes idle awaiting result), `session.status_idle`, `session.status_terminated`.

**Custom tool result**: `events.send(events=[{"type": "user.custom_tool_result", "custom_tool_use_id": "sevt_...", "content": [{"type": "text", "text": "..."}]}])`.

**Polling** via `client.beta.sessions.events.list(session_id=...)`. **WARNING**: prefer SDK over raw `requests`/`httpx` — `timeout=(5, 60)` and `httpx.Timeout(120)` are PER-CHUNK timeouts, NOT total. A trickling response can block forever. For wall-clock deadline, use `time.monotonic()` at loop level or `asyncio.wait_for()`.

**Files**: `client.beta.files.upload(file=open("data.csv", "rb"))` → mount with `resources=[{"type": "file", "file_id": file.id, "mount_path": "..."}]`. List session output files: `client.beta.files.list(scope_id=session.id, betas=["managed-agents-2026-04-01"])`. Download: `client.beta.files.download(f.id).write_to_file(...)`. **Note**: ~1-3s indexing lag between `session.status_idle` and output files appearing in `files.list` — retry once or twice.

**Session mgmt**: `retrieve`, `list`, `delete`, `archive` on `client.beta.sessions`.

**MCP servers**: agent declares URL (no auth here — auth goes in a vault); session attaches `vault_ids=[vault.id]`.

Full streaming loop with custom tool dispatch shown — re-enters streaming loop after sending tool results until no more `agent.custom_tool_use` events arrive.
