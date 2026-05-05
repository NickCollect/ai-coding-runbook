---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/typescript-v2-preview.md
source_url: https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview
title: "TypeScript SDK V2 interface (preview)"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK]
concepts_referenced: []
---

Preview of the V2 TypeScript Agent SDK — an **unstable**, simpler alternative to V1's single async-generator pattern. APIs may change before stabilizing.

Three core concepts:
- `unstable_v2_createSession({ model })` — start a multi-turn session.
- `unstable_v2_resumeSession(sessionId, { model })` — resume a previous session by ID.
- `unstable_v2_prompt(prompt, { model })` — one-shot single-turn convenience helper.

The session interface separates input from output:
```ts
interface SDKSession {
  readonly sessionId: string;
  send(message: string | SDKUserMessage): Promise<void>;
  stream(): AsyncGenerator<SDKMessage, void>;
  close(): void;
}
```

Why it matters: in V1, both input and output flow through one async generator, requiring an `async function*` input stream and yield coordination for multi-turn convos. V2 makes each turn a discrete `send()` then `stream()` cycle — easier to interleave logic between turns.

Cleanup: supports TypeScript 5.2+ `await using` for automatic close, or explicit `session.close()`.

Resume flow: capture `sessionId` from any received message, store it, later call `unstable_v2_resumeSession(id, ...)` to continue. Bundled native CLI binary is included as an optional dep.

Feature gaps vs V1 (must use V1 for): session forking (`forkSession`), some advanced streaming-input patterns. Feedback channel: GitHub Issues on `anthropics/claude-code`.
