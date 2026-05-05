---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/examples/server/src/README-simpleTaskInteractive.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/examples/server/src/README-simpleTaskInteractive.md
title: "TS SDK example: simpleTaskInteractive (tasks + elicitation + sampling)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Demonstrates the MCP **Tasks message queue pattern** with interactive server-to-client requests (elicitation and sampling). Two components:

**Server (`simpleTaskInteractive.ts`)**: exposes two task-based tools:
- `confirm_delete` — uses elicitation to ask the user for confirmation before "deleting" a file
- `write_haiku` — uses sampling to request an LLM to generate a haiku on a topic

**Client (`simpleTaskInteractiveClient.ts`)**: connects to the server and handles elicitation requests (simple y/n terminal prompts) + sampling requests (mock haiku generator).

**Task-based execution** — both tools use `execution.taskSupport: 'required'`, the call-now/fetch-later pattern: client calls tool with `task: { ttl: 60000 }` → server creates task, returns `CreateTaskResult` immediately → client polls via `tasks/result` for final result → server sends elicitation/sampling requests through the task message queue → client handles requests and returns responses → server completes task with final result.

**Message queue pattern**: when a tool needs to interact with the client, it (1) updates task status to `input_required`, (2) enqueues request in the task message queue, (3) waits for response via Resolver, (4) updates status back to `working`, (5) continues processing. The `TaskResultHandler` dequeues messages when the client calls `tasks/result` and routes responses back to waiting Resolvers.
