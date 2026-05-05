---
type: summary
source: 01_Raw/anthropic.com/engineering/managed-agents.md
source_url: https://www.anthropic.com/engineering/managed-agents
title: "Scaling Managed Agents: Decoupling the brain from the hands"
summarized_at: 2026-05-04
entities_referenced: [Managed-agent, Session-API, Environment-API, MCP-server, Vault, Agent-SDK]
concepts_referenced: [Agentic-loop, Context-window, Prompt-caching]
---

Anthropic engineering post (Apr 08, 2026) introducing **Managed Agents** — a hosted service on the Claude Platform that runs long-horizon agents through a small set of stable interfaces. Architecture motivated by an OS-style insight: *harnesses encode assumptions that go stale as models improve* (e.g., context resets needed for Sonnet 4.5's "context anxiety" became dead weight on Opus 4.5).

**The OS analogy.** Just as `read()` works the same on 1970s disk packs and modern SSDs because OS abstractions virtualized hardware into `process` and `file`, Managed Agents virtualize agent components: **session** (append-only event log), **harness** (loop calling Claude + routing tool calls), **sandbox** (execution environment). Each can be swapped without disturbing the others. Anthropic is opinionated about *interface shape*, not implementation.

**Pets vs. cattle problem.** Initial design coupled session + harness + sandbox in one container. Benefits: direct file syscalls, no service boundaries. Costs: container = "pet" — if it failed, session was lost; debugging required a shell inside the container that often held user data; harness assumed everything Claude worked on lived inside, breaking VPC integration.

**Decoupling the brain from the hands.**
- *Harness leaves the container.* Sandbox is called via `execute(name, input) → string`. Container becomes cattle: failures are tool-call errors passed back to Claude; new container provisioned on demand via `provision({resources})`.
- *Harness becomes cattle too.* Session log lives outside the harness. On crash: `wake(sessionId)` → `getSession(id)` → resume from last event. During the agent loop, harness writes via `emitEvent(id, event)`.

**Security boundary.** Coupled design meant Claude-generated code ran in the same container as credentials — prompt injection only had to convince Claude to read its own env. Structural fix: tokens never reachable from the sandbox where Claude's code runs. Two patterns: (1) bundle auth with resource (e.g., git access token used to clone the repo at sandbox init, wired into local git remote — push/pull work without agent handling token); (2) for custom tools, store OAuth tokens in a Vault, MCP calls go through a dedicated proxy keyed by session token. The harness is never aware of credentials.

**The session is not the context window.** Long-horizon tasks exceed context; standard fixes (compaction, memory tool, context trimming) involve irreversible decisions about what to keep. In Managed Agents, the session is a **context object outside the context window**, durably stored. `getEvents()` lets the brain interrogate context — pick up from where it stopped, rewind a few events, re-read context before a specific action. Fetched events can be transformed in the harness before going to Claude (cache-hit-rate optimization, context engineering). Session guarantees durability and interrogability; harness owns context strategy.

**Many brains, many hands.**
- *Many brains.* Decoupling lets brains scale by starting many stateless harnesses, connecting to hands only if needed. Sessions that don't need a sandbox don't pay container provisioning cost. **p50 TTFT dropped ~60%, p95 over 90%.**
- *Many hands.* Each hand is a tool: name + input → string. Same interface for any custom tool, any MCP server, Anthropic's own tools. Harness doesn't know whether the sandbox is a container, a phone, or a Pokémon emulator. No hand is coupled to any brain — brains can pass hands to one another.

**Framing.** Managed Agents is a "meta-harness" — opinionated about interfaces (session manipulation, sandbox computation, scaling to many brains/hands), unopinionated about specific harness running on top. Claude Code is one supported harness; task-specific harnesses are equally fine. Authors: Lance Martin, Gabe Cemaj, Michael Cohen.
