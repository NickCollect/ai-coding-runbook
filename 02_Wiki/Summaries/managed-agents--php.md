---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/php/managed-agents/README.md
title: "Managed Agents — PHP"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

PHP SDK patterns for Anthropic Managed Agents (Beta). Install: `composer require "anthropic-ai/sdk"`.

Same persistence model as other languages: agents created once via `$client->beta->agents->create(...)`, ID stored, reference in every `->sessions->create(...)`. Agent updates (`->beta->agents->update(...)`) create new immutable versions.

**Setup**:
1. Environment: `$client->beta->environments->create(name:..., config: ['type'=>'cloud', 'networking'=>['type'=>'unrestricted']])`.
2. Agent: `$client->beta->agents->create(name, model:'claude-opus-4-7', system:..., tools:[BetaManagedAgentsAgentToolset20260401Params::with(type:'agent_toolset_20260401')])`.
3. Session: `$client->beta->sessions->create(agent: ['type'=>'agent','id'=>$agent->id,'version'=>$agent->version], environmentID: $environment->id, title: ...)`.

Patterns mirror the Go README (see `managed-agents--go.md` summary for the full conceptual model: stream-first ordering, vault-based MCP credentials, GitHub repo resources, etc.) — this file is a condensed PHP-syntax variant. For bindings/methods not shown, README directs readers to WebFetch the PHP SDK repo or `shared/live-sources.md` rather than guess.
