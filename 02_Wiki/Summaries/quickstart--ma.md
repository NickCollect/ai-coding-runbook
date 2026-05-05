---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/quickstart.md
source_url: https://platform.claude.com/docs/en/managed-agents/quickstart
title: "Get started with Claude Managed Agents"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, Session-API, Environment-API, Anthropic-SDK-Python, Anthropic-SDK-TypeScript, Streaming-API]
concepts_referenced: []
---

End-to-end quickstart for creating your first [[Managed-agent]]: create agent → set up environment → start session → stream agent responses. **All Managed Agents API requests require the `managed-agents-2026-04-01` beta header** (SDK auto-sets).

**Core concepts** (recap):
- *Agent*: model + system prompt + tools + MCP servers + skills.
- *Environment*: configured container template (packages, network access).
- *Session*: a running agent instance within an environment.
- *Events*: messages exchanged between your app and the agent.

Tip: `/claude-api managed-agents-onboard` in Claude Code provides an interactive guided setup.

**Prerequisites.** Anthropic Console account and API key.

**Install the `ant` CLI.** Three install paths:
- macOS: `brew install anthropics/tap/ant`.
- Linux/WSL: download from `github.com/anthropics/anthropic-cli/releases` (e.g., v1.3.2 release tar).
- From source: `go install github.com/anthropics/anthropic-cli/cmd/ant@latest` (Go 1.22+).

**Install the SDK.** [[Anthropic-SDK-Python]]: `pip install anthropic`. [[Anthropic-SDK-TypeScript]]: `npm install @anthropic-ai/sdk`. Java: `com.anthropic:anthropic-java:2.27.0`. Go: `go get github.com/anthropics/anthropic-sdk-go`. C#: `dotnet add package Anthropic`. Ruby: `bundle add anthropic`. PHP: `composer require anthropic-ai/sdk`. Set `ANTHROPIC_API_KEY` environment variable.

**Steps for first session:**

1. **Create an agent.** `POST /v1/agents` with `name`, `model: "claude-opus-4-7"`, `system` ("You are a helpful coding assistant. Write clean, well-documented code."), and `tools: [{"type": "agent_toolset_20260401"}]`. Response gives `agent.id` and `agent.version` (starts at 1).

2. **Create an [[Environment-API]] environment.** Cloud container with default packages and unrestricted networking (or limited—see Environments doc). Returns `environment.id`.

3. **Start a [[Session-API]] session.** `POST /v1/sessions` with `agent: agent.id` (string = latest version) or `{type: "agent", id: ..., version: ...}` (object = pinned version), and `environment_id: environment.id`. Returns `session.id`.

4. **Send user events and receive agent events** via `/v1/sessions/{id}/events` and the [[Streaming-API]] stream endpoint. The session executes the agent loop autonomously: model decides on tool calls, harness runs them in the container, sends back results, model continues. You see `agent.message`, `agent.thinking`, `agent.tool_use`, `agent.tool_result` events as they happen, plus `session.status_*` events for state transitions.

5. **Steer or interrupt.** Send additional `user.message` events to add new instructions. Send `user.interrupt` to stop mid-execution.

Once the session reaches `session.status_idle`, the agent has completed its current task and is waiting for input. Files written by the agent to `/mnt/session/outputs/` can be retrieved via the Files API scoped to the session.

The doc walks through the `agent` create call in cURL, ant CLI, Python, TypeScript, C#, Go, Java, PHP, Ruby, then implicitly chains the same shape across environments + sessions in the linked deeper-dive pages.
