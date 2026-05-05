---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/hosting.md
source_url: https://code.claude.com/docs/en/agent-sdk/hosting
title: "Hosting the Agent SDK"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Sandboxing]
concepts_referenced: []
---

How to deploy Claude Agent SDK in production. The SDK is a **long-running stateful process** (not a stateless API call): it maintains a persistent shell, working directory, and tool execution context. This shapes hosting architecture.

Requirements:
- Container-based sandboxing recommended for process isolation, resource limits, network control.
- Runtime: Python 3.10+ or Node.js 18+. Both SDK packages bundle a native Claude Code binary — no separate CLI install needed.
- Resources: ~1 GiB RAM, 5 GiB disk, 1 CPU per instance (tune to workload).
- Network: outbound HTTPS to `api.anthropic.com` plus optional MCP/tool endpoints.

Sandbox providers mentioned: Modal, Cloudflare Sandboxes, Daytona, E2B, Fly Machines, Vercel Sandbox. Self-hosted options (Docker, gVisor, Firecracker) covered in Secure Deployment doc.

Four deployment patterns:
1. **Ephemeral sessions** — one container per task, destroyed on completion. Good for one-off tasks (bug fixes, invoice processing, translation).
2. **Long-running sessions** — persistent containers, often multiple agent processes. Good for proactive agents (email triage, site builder, chatbots).
3. **Hybrid sessions** — ephemeral containers hydrated from saved state via session resumption. Good for project managers, deep research, multi-touch support tickets.
4. **Single containers** — multiple agent processes in one global container. Niche, used for agents collaborating closely (simulations).

FAQ highlights:
- Communicate with sandboxes by exposing HTTP/WebSocket ports.
- Container baseline cost ~5 cents/hr; tokens dominate spend.
- No built-in session timeout — set `maxTurns` to prevent runaway loops.
- Use standard backend logging infra for container monitoring.
