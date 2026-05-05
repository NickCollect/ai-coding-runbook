---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/overview.md
source_url: https://platform.claude.com/docs/en/managed-agents/overview
title: "Claude Managed Agents overview"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, Messages-API, Session-API, Environment-API, MCP-server, Skill-API]
concepts_referenced: []
---

Conceptual overview of Claude [[Managed-agent]] s: a pre-built, configurable agent harness that runs in managed infrastructure. Best for long-running tasks and asynchronous work. Compared to the [[Messages-API]] (direct model prompting, custom agent loops, fine-grained control), Managed Agents provides the harness, infrastructure, and runtime—you stop building your own agent loop, tool execution, and runtime, and get a fully managed environment where Claude can read files, run commands, browse the web, and execute code securely. Built-in prompt caching, compaction, and other performance optimizations.

**Four core concepts.**
- **Agent**: model + system prompt + tools + MCP servers + skills (versioned, reusable).
- **Environment**: configured container template (pre-installed packages, network access).
- **Session**: a running agent instance within an environment, performing a specific task and generating outputs.
- **Events**: messages exchanged between your application and the agent (user turns, tool results, status updates).

**End-to-end flow.**
1. Create an agent (model + system prompt + tools + [[MCP-server]] s + [[Skill-API]] skills). Reference by ID across many sessions.
2. Create an [[Environment-API]] environment (cloud container with pre-installed packages, network rules, mounted files).
3. Start a [[Session-API]] session referencing your agent + environment.
4. Send events; Claude autonomously executes tools and streams back results via SSE. Event history is persisted server-side and can be fetched in full.
5. Steer or interrupt mid-execution by sending additional user events.

**When to use.** Long-running execution (tasks taking minutes to hours with multiple tool calls); cloud infrastructure (secure containers with packages + network); minimal infrastructure on your side (no need to build your own loop, sandbox, or tool execution layer); stateful sessions (persistent file systems and conversation history across multiple interactions).

**Supported tools.** Bash (shell commands in container); file operations (read, write, edit, glob, grep); web search + web fetch; [[MCP-server]] s (external tool providers).

**Beta access.** All Managed Agents endpoints require `managed-agents-2026-04-01` beta header (SDK auto-sets). Outcomes and multiagent are research-preview features—request access. Behaviors may be refined between releases to improve outputs.

**Rate limits (per org).**
- Create endpoints (agents, sessions, environments, etc.): **300/min**.
- Read endpoints (retrieve, list, stream, etc.): **600/min**.

Plus standard org-level spend limits and tier-based rate limits.

**Branding guidelines for partners.** Use of Claude branding is optional.
- *Allowed:* "Claude Agent" (preferred for dropdown menus); "Claude" (when in a menu already labeled "Agents"); "{YourAgentName} Powered by Claude".
- *Not permitted:* "Claude Code" / "Claude Code Agent"; "Claude Cowork" / "Claude Cowork Agent"; Claude Code-branded ASCII art or visual elements that mimic Claude Code.

Your product should maintain its own branding and not appear to be Claude Code, Claude Cowork, or any other Anthropic product. Branding compliance questions go to the Anthropic sales team.
