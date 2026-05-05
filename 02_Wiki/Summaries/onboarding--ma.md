---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/onboarding.md
source_url: https://platform.claude.com/docs/en/managed-agents/onboarding
title: "Prototype in Console"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, Session-API, MCP-server, Skill-API]
concepts_referenced: []
---

How to create and test [[Managed-agent]] s visually in the Console without writing API calls. Console produces the same `/v1/agents` and `/v1/sessions` resources as the API but lets you iterate on configuration interactively before writing code. **Requires `managed-agents-2026-04-01` beta header.**

**Visual interface walks through each agent field.**
- *Model and system prompt*: pick a model and write the system prompt in a full-width editor.
- *MCP servers*: add remote [[MCP-server]] s by URL and authenticate your agent to take action on your behalf (uses the vault flow internally for storing credentials).
- *Tools*: extend capabilities using the pre-built agent toolset and/or MCP tools.
- *Skills*: attach Anthropic or custom [[Skill-API]] skills from the organization's library.

As you configure, **Console shows the equivalent API request alongside the visual form**—copy it into your code once satisfied.

**Inline session runner.** After configuring, start a test [[Session-API]] session directly inside Console, send messages, and watch the event stream without leaving the page. This is the fastest way to verify your system prompt and tool selection produce the expected behavior—you can iterate in seconds rather than wiring up a full SDK setup just to spot-check.

**Prototype-to-code path.**
1. Configure and test in Console.
2. Copy the agent ID from Console output.
3. Reference it in your code when creating sessions:
```python
session = client.beta.sessions.create(
    agent="agent_01J8XkN5uT3vHpLqRfWdY2",
    environment_id="env_01K2mPsT7hNwR4jXuLvCqD8",
    title="My first session",
)
```

The agent created via Console is identical to one created via API—same versioning, archiving, lifecycle. Console is purely a configuration UI on top of the same backend resources.

This page is essentially the Console-specific entry path for managed-agents users; the rest of the docs (agent setup, environments, sessions, events, etc.) cover the API-side concepts in depth, all of which Console exposes through forms.
