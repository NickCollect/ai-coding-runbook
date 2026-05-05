---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/user-input.md
source_url: https://code.claude.com/docs/en/agent-sdk/user-input
title: "Handle approvals and user input"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Permission-mode, Hooks, Subagent]
concepts_referenced: []
---

Covers the Agent SDK's `canUseTool` callback — the runtime hook that surfaces both **tool permission requests** and **clarifying questions** (via the built-in `AskUserQuestion` tool) to your application. Distinct from declarative allow/deny rules and the `Hooks` system, which fire earlier in the permission-evaluation chain.

The callback fires when:
1. Claude wants a tool not auto-approved by allow rules / `acceptEdits` / `bypassPermissions`.
2. Claude calls `AskUserQuestion` (check `tool_name == "AskUserQuestion"`).

The callback can stay pending indefinitely; the SDK only cancels on query cancel. For long-running scenarios, the **TypeScript SDK** supports the `defer` hook decision so the process can exit and resume from persisted session — Python does NOT have this.

**Callback args**:
- `toolName` (e.g., `"Bash"`, `"Write"`, `"Edit"`)
- `input` (tool-specific params)
- `options` (TS) / `context` (Python) — includes optional `suggestions` (proposed `PermissionUpdate`s) and a cancellation signal (TS: `AbortSignal`; Python: reserved)

**Response shape**:
| Decision | Python | TypeScript |
|---|---|---|
| Allow | `PermissionResultAllow(updated_input=...)` | `{ behavior: "allow", updatedInput }` |
| Deny | `PermissionResultDeny(message=...)` | `{ behavior: "deny", message }` |

Five practical patterns: **Approve** (pass input through), **Approve with changes** (modify input, e.g., scope `/tmp` → `/tmp/sandbox`; Claude is not told it was modified), **Reject** (with explanatory message Claude reads), **Suggest alternative** (deny + guidance message: "User asked you to compress instead of delete"), **Redirect entirely** (use streaming input to send Claude a new instruction).

**Python gotcha**: `can_use_tool` requires streaming input mode AND a dummy `PreToolUse` hook returning `{"continue_": True}` to keep the stream open — without it the stream closes before the callback can fire.

**Clarifying questions (`AskUserQuestion`)**: especially common in `plan` mode. Available by default; if you restrict `tools`, include `"AskUserQuestion"` explicitly. Each call carries 1-4 questions with 2-4 options each. Question shape: `{question, header (≤12 chars), options: [{label, description}], multiSelect}`.

Response: build `answers` dict mapping `question` text → selected option `label` (multi-select: comma-join labels). Pass through original `questions` array — required for tool processing.

**TS-only previews**: `toolConfig.askUserQuestion.previewFormat: "markdown" | "html"` adds a `preview` field on each option (HTML stripped of `<script>`/`<style>`/`<!DOCTYPE>` before reaching callback). Claude generates previews only when visual comparison helps.

**Free-text input**: present an "Other" choice; use the user's actual typed text as the answer value (not the literal "Other").

**Limitations**: `AskUserQuestion` not available in subagents spawned via the `Agent` tool.

**Other input mechanisms**: streaming input (mid-task interruption / context injection / chat UIs) and custom tools (structured forms, ticket integrations, domain-specific UX).
