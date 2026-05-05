---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/ruby/managed-agents/README.md
title: "Managed Agents — Ruby"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Ruby SDK patterns for Anthropic Managed Agents (Beta). Install: `gem install anthropic`.

Same persistence model as Go/PHP/etc: agents created once, store ID, reference in sessions.

**Ruby SDK quirk — trailing underscores**: SDK uses `system_:` and `send_(` (trailing underscore) to avoid shadowing `Kernel#system` and `Kernel#send`. Use these forms throughout managed-agents code.

**Setup**:
1. Environment: `client.beta.environments.create(name:..., config: {type:"cloud", networking:{type:"unrestricted"}})`.
2. Agent: `client.beta.agents.create(name:..., model::"claude-opus-4-7", system_: "...", tools: [{type:"agent_toolset_20260401"}])`.
3. Session: `client.beta.sessions.create(agent: {type:"agent", id: agent.id, version: agent.version}, environment_id: environment.id, title:...)`.

Updates via `client.beta.agents.update(agent.id, version: agent.version, system_: "...")` — create new immutable versions.

Patterns mirror Go README — see `managed-agents--go.md` summary for full conceptual model.
