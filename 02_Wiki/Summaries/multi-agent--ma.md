---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/multi-agent.md
source_url: https://platform.claude.com/docs/en/managed-agents/multi-agent
title: "Multiagent sessions"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, Session-API, MCP-server]
concepts_referenced: []
---

**Research Preview feature** (request access). Multi-agent orchestration lets one [[Managed-agent]] coordinate with others to complete complex work. Agents can act in parallel with their own isolated context, improving output quality and time to completion. **Requires `managed-agents-2026-04-01` beta header plus the research-preview header.**

**How it works.** All agents share the same container and filesystem, but each agent runs in its own session **thread**—a context-isolated event stream with its own conversation history.
- The **coordinator** reports activity in the **primary thread** (same as the session-level event stream).
- Additional threads are spawned at runtime when the coordinator decides to delegate.
- Threads are **persistent**: the coordinator can send a follow-up to an agent it called earlier, and that agent retains everything from its previous turns.

Each agent uses its own configuration (model, system prompt, tools, [[MCP-server]] s, skills) as defined when that agent was created. Tools and context are NOT shared across agents—only the filesystem.

**What to delegate (good fits).** Multiagent works best when the overall goal has multiple well-scoped, specialized sub-tasks:
- *Code review*: a reviewer agent with focused system prompt and read-only tools.
- *Test generation*: a test agent that writes and runs tests without touching production code.
- *Research*: a search agent with web tools that summarizes findings back to the coordinator.

**Declaring callable agents.** When defining the coordinator, list IDs of agents it's permitted to call in `callable_agents`:
```json
{
  "name": "Engineering Lead",
  "model": "claude-opus-4-7",
  "system": "You coordinate engineering work. Delegate code review to the reviewer agent and test writing to the test agent.",
  "tools": [{"type": "agent_toolset_20260401"}],
  "callable_agents": [
    {"type": "agent", "id": "agent_reviewer", "version": 3},
    {"type": "agent", "id": "agent_test_writer", "version": 1}
  ]
}
```

Each callable agent entry pins both `id` and `version`—when the coordinator delegates, it gets exactly that pinned version, making multi-agent compositions reproducible.

**Event surface.** During a multi-agent [[Session-API]] session, you receive the standard `agent.*` event types plus:
- `session.thread_created`: coordinator spawned a new thread.
- `session.thread_idle`: a thread finished its current work.
- `agent.thread_message_sent` / `agent.thread_message_received`: messages flowing between coordinator and worker threads.

The primary-thread events look like a single agent's stream; the additional threads' events are interleaved or available via separate thread-scoped queries depending on the SDK helper used.

**Practical patterns.** A common shape: coordinator agent does planning + thread orchestration with light tool access; worker agents do specialized execution with rich tool access (e.g., one with bash + filesystem, another with web tools, another with MCP servers like GitHub or Slack). Filesystem sharing lets a worker write a file that the coordinator or another worker reads, providing a side channel for large data without passing it through chat content.

The page focuses on the coordinator declaration mechanism; runtime behavior (how the coordinator decides when to delegate, how threads idle, etc.) is governed by the agent's system prompt and the model's reasoning—not a programmatic delegation API.
