---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/quickstart.md
source_url: https://code.claude.com/docs/en/agent-sdk/quickstart
title: "Agent SDK Quickstart"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Permission-mode]
concepts_referenced: [Agentic-loop]
---

End-to-end walkthrough: install SDK → write buggy `utils.py` → run an agent that finds and fixes the bugs autonomously.

**Prereqs**: Node 18+ or Python 3.10+, Anthropic account.

**Install**: `npm install @anthropic-ai/claude-agent-sdk`, or Python via `uv add claude-agent-sdk` / `pip3 install claude-agent-sdk`. Set `ANTHROPIC_API_KEY` (or Bedrock/Vertex/Foundry env vars).

**Pattern**: `query({prompt, options})` with `allowedTools: ["Read", "Edit", "Glob"]` + `permissionMode: "acceptEdits"`. The `async for` loop streams messages: Claude reasoning → tool call → tool result → next iteration. SDK handles tool execution, context management, retries.

**Permission modes** (key reference):
| Mode | Behavior | Use case |
|---|---|---|
| `acceptEdits` | Auto-approves file edits + common FS bash, asks for others | Trusted dev workflows |
| `dontAsk` | Denies anything not in allowedTools | Locked-down headless |
| `auto` (TS only) | Model classifier approves/denies per tool call | Autonomous w/ guardrails |
| `bypassPermissions` | All tools without prompts | Sandboxed CI |
| `default` | Requires `canUseTool` callback | Custom approval flows |

**Tool combinations** mapped to capability:
- Read/Glob/Grep → read-only analysis
- Read/Edit/Glob → analyze + modify
- Read/Edit/Bash/Glob/Grep → full automation

**Customizations shown**: add `WebSearch`, override `systemPrompt` (e.g., "senior Python developer, follow PEP 8"), enable `Bash` for "write tests, run them, fix failures" workflows.

**Gotcha (Opus 4.7)**: Older SDK versions fail with `API Error: 400 ... "thinking.type.enabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort"`. Upgrade to Agent SDK v0.2.111+ to use `claude-opus-4-7`.

**Streaming vs batch**: example uses streaming for live progress; for background jobs see streaming-vs-single-mode doc.
