---
source_url: https://cursor.com/docs/sdk/typescript
---

# Cursor SDK

### Public beta

The TypeScript SDK is in public beta. APIs may change before general
availability.

The `@cursor/sdk` package lets you call Cursor's agent from your own code. The same agent that runs in the Cursor IDE, CLI, and web app is now scriptable from TypeScript.

## Overview

The SDK wraps local and cloud runtimes behind one interface. You write the same code regardless of where the agent runs.

| Runtime                   | What it does                                                                                                       | When to use                                                                                                                |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| **Local**                 | Runs the agent inline in your Node process. Files come from disk.                                                  | Dev scripts and CI checks against a working tree.                                                                          |
| **Cloud (Cursor-hosted)** | Runs in an isolated VM with your repo cloned in. Cursor runs the VMs.                                              | When the caller doesn't have the repo, you want many agents in parallel, or runs need to survive the caller disconnecting. |
| **Cloud (self-hosted)**   | Same shape, but you run the VMs via a [self-hosted pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md). | Same reasons as Cursor-hosted, plus code, secrets, and build artifacts must stay in your environment.                      |

Runtime is picked by which key you pass to `Agent.create()` (`local` or `cloud`). Use the same `CURSOR_API_KEY` for either.

For the REST API, see the [Cloud Agents API](https://cursor.com/docs/cloud-agent/api/endpoints.md).

## Authentication

Set `CURSOR_API_KEY` (or pass `apiKey`) before creating an agent.

The SDK accepts user API keys and service account API keys for both local and cloud runs. Team Admin API keys are not yet supported.

- **User API key** from [Cursor Dashboard → Integrations](https://cursor.com/dashboard/integrations)
- **Service account API key** from [Team settings](https://cursor.com/dashboard/team-settings). See [Service accounts](https://cursor.com/docs/account/enterprise/service-accounts.md)

```bash
export CURSOR_API_KEY="your-key"
```

## Usage and billing

SDK runs follow the same pricing, request pools, and Privacy Mode rules as runs from the IDE and Cloud Agents. Spend shows up in your team's [usage dashboard](https://cursor.com/dashboard/usage) under the SDK tag.

## Core concepts

| Concept        | Description                                                                                                        |
| :------------- | :----------------------------------------------------------------------------------------------------------------- |
| **Agent**      | Durable container that holds conversation state, workspace config, and settings. Survives across multiple prompts. |
| **Run**        | One prompt submission. Owns its own stream, status, result, and cancellation.                                      |
| **SDKMessage** | Normalized stream events emitted during a run. Same shape across all runtimes.                                     |

## Installation

```bash
npm install @cursor/sdk
```

## Quick start

The fastest way in: a local agent against your current working tree, streaming events as they come in. Cloud setup is in [Creating agents](https://cursor.com/docs/sdk/typescript.md#creating-agents) below.

```typescript
import { Agent } from "@cursor/sdk";

const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2" },
  local: { cwd: process.cwd() },
});

const run = await agent.send("Summarize what this repository does");

for await (const event of run.stream()) {
  console.log(event);
}
```

Each event is a discriminated `SDKMessage`. [Streaming](https://cursor.com/docs/sdk/typescript.md#streaming) shows how to extract assistant text, handle tool calls, and clean up with `await using`. For a one-shot prompt (create, run, dispose), see [Agent.prompt()](https://cursor.com/docs/sdk/typescript.md#agentprompt).

## Creating agents

```typescript
function Agent.create(options: AgentOptions): Promise<SDKAgent>;
```

`Agent.create()` validates options and returns a handle immediately. Pass either `local` or `cloud` to pick a runtime.

```typescript
// Local agent
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2" },
  local: { cwd: "/path/to/repo" },
});

// Cloud agent
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2" },
  cloud: {
    repos: [{ url: "https://github.com/your-org/your-repo", startingRef: "main" }],
    autoCreatePR: true,
  },
});
```

`agent.agentId` is populated immediately. Local agents get an `agent-<uuid>` ID; cloud agents get a `bc-<uuid>` ID.

Cloud agents started by the SDK are filtered out of the default agent list. To
view them in Cursor Web or a Cursor window, click **Filter > Source > SDK**.

### Session environment variables

For cloud agents, pass `cloud.envVars` when a run needs short-lived credentials or other values that should live only with that agent.

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  cloud: {
    repos: [{ url: "https://github.com/your-org/your-repo" }],
    envVars: {
      STAGING_API_TOKEN: process.env.STAGING_API_TOKEN!,
    },
  },
});
```

These values are encrypted at rest, injected into the cloud agent's shell, and deleted with the agent. `envVars` can't be used with a caller-supplied `agentId`; omit `agentId` and read the server-minted ID from `agent.agentId`. Variable names can't start with `CURSOR_`.

### Model parameters

Use `model.params` to pass per-model options such as reasoning effort or max mode. Parameter ids and values vary by model. Use [`Cursor.models.list()`](https://cursor.com/docs/sdk/typescript.md#cursormodelslist) to discover supported parameters and preset variants for your account.

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: {
    id: "composer-2",
    params: [{ id: "thinking", value: "high" }],
  },
  local: { cwd: process.cwd() },
});
```

### SDKAgent

The handle returned by `Agent.create()` and `Agent.resume()`.

```typescript
interface SDKAgent {
  readonly agentId: string;
  readonly model: ModelSelection | undefined;

  send(message: string | SDKUserMessage, options?: SendOptions): Promise<Run>;
  close(): void;
  reload(): Promise<void>;
  [Symbol.asyncDispose](): Promise<void>;

  listArtifacts(): Promise<SDKArtifact[]>;
  downloadArtifact(path: string): Promise<Buffer>;
}
```

| Member                  | Description                                                                                                                                                                  |
| :---------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agentId`               | Stable agent identifier. `agent-<uuid>` for local, `bc-<uuid>` for cloud.                                                                                                    |
| `model`                 | Current model selection. Updates after every successful `send({ model })`. `undefined` until something sets it (including resumed agents whose caller did not pass `model`). |
| `send`                  | Start a new run with the given prompt. Returns a `Run` handle.                                                                                                               |
| `close`                 | Begin disposal without awaiting. Fire-and-forget.                                                                                                                            |
| `reload`                | Re-read filesystem config (hooks, project MCP, subagents) without disposing.                                                                                                 |
| `[Symbol.asyncDispose]` | Async disposal. Pair with `await using` for automatic cleanup.                                                                                                               |
| `listArtifacts`         | List files produced by the agent (cloud only; local returns empty).                                                                                                          |
| `downloadArtifact`      | Download a file by path (cloud only; local throws).                                                                                                                          |

### Agent.prompt()

```typescript
function Agent.prompt(message: string, options?: AgentOptions): Promise<RunResult>;
```

One-shot convenience: creates an agent, sends a single prompt, waits for the run to finish, and disposes.

```typescript
const result = await Agent.prompt("What does the auth middleware do?", {
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2" },
  local: { cwd: process.cwd() },
});
```

## Sending messages

Each `agent.send()` returns a `Run`. The agent retains conversation context across runs; the run is the unit of work for one prompt.

### Run

```typescript
type RunStatus = "running" | "finished" | "error" | "cancelled";
type RunOperation = "stream" | "wait" | "cancel" | "conversation";

interface Run {
  readonly id: string;
  readonly agentId: string;
  readonly status: RunStatus;
  readonly result?: string;
  readonly model?: ModelSelection;
  readonly durationMs?: number;
  readonly git?: RunGitInfo;
  readonly createdAt?: number;

  stream(): AsyncGenerator<SDKMessage, void>;
  wait(): Promise<RunResult>;
  cancel(): Promise<void>;
  conversation(): Promise<ConversationTurn[]>;

  supports(operation: RunOperation): boolean;
  unsupportedReason(operation: RunOperation): string | undefined;
  onDidChangeStatus(listener: (status: RunStatus) => void): () => void;
}

interface RunGitInfo {
  branches: Array<{ repoUrl: string; branch?: string; prUrl?: string }>;
}

interface RunResult {
  id: string;
  status: "finished" | "error" | "cancelled";
  result?: string;
  model?: ModelSelection;
  durationMs?: number;
  git?: RunGitInfo;
}
```

### Streaming

```typescript
const run = await agent.send("Find the bug in src/auth.ts");

for await (const event of run.stream()) {
  switch (event.type) {
    case "assistant":
      for (const block of event.message.content) {
        if (block.type === "text") process.stdout.write(block.text);
      }
      break;
    case "thinking":
      process.stdout.write(event.text);
      break;
    case "tool_call":
      console.log(`[tool] ${event.name}: ${event.status}`);
      break;
    case "status":
      console.log(`[status] ${event.status}`);
      break;
  }
}

// Follow-up. Full context is retained.
const run2 = await agent.send("Fix it and add a regression test");
await run2.wait();
```

To send images alongside text:

```typescript
const run = await agent.send({
  text: "What's in this screenshot?",
  images: [{ data: base64Png, mimeType: "image/png" }],
});
```

### Waiting without streaming

```typescript
const result = await run.wait();

console.log(result.status);      // "finished" | "error" | "cancelled"
console.log(result.result);      // final assistant text, if any
console.log(result.model);       // resolved ModelSelection used for this run
console.log(result.durationMs);
console.log(result.git);         // { branches: [{ repoUrl, branch?, prUrl? }] } on cloud
```

### Cancelling a run

```typescript
await run.cancel();
```

Cancels the run. The status moves to `"cancelled"`, the live stream aborts, in-flight tool calls stop, and `run.wait()` resolves with `status: "cancelled"`. Partial output (assistant text written so far) stays on the Run object.

Cancel is supported on running local and cloud runs and is a no-op if the run already finished.

### Reading run state

```typescript
console.log(run.status);  // "running" | "finished" | "error" | "cancelled"

const stop = run.onDidChangeStatus((status) => {
  console.log(`status changed to ${status}`);
});
// Call `stop()` to remove the listener.

// Structured per-turn view of the conversation accumulated in this run
const turns = await run.conversation();
```

`run.conversation()` returns the run's `ConversationTurn[]` (an agent turn with steps, or a shell turn with command and output). Use it to render or persist the run's structured history without subscribing to the live stream.

### Per-run model override

The `model` you pass to `agent.send()` overrides the agent's selection for that run, then becomes sticky: subsequent sends without an override continue to use the new model. To switch back, pass another `model` override or read the current selection from `agent.model`.

```typescript
const run = await agent.send("Plan the refactor", {
  model: { id: "composer-2", params: [{ id: "thinking", value: "high" }] },
});

console.log(agent.model);  // updated to the override after the send succeeds
```

`run.model` and `result.model` reflect the selection that this specific run actually used and are immutable once the run starts.

### Streaming raw deltas

`run.stream()` yields normalized `SDKMessage` events. For lower-level updates (per-token text, tool-call args streaming in, thinking deltas, step boundaries), pass `onDelta` and `onStep` callbacks to `send()`:

```typescript
const run = await agent.send("Refactor the utils module", {
  onDelta: ({ update }) => {
    if (update.type === "text-delta") process.stdout.write(update.text);
    if (update.type === "thinking-delta") process.stdout.write(update.text);
  },
  onStep: ({ step }) => {
    console.log(`[step] ${step.type}`);
  },
});
```

The callbacks are awaited before the next update is processed, so you can apply backpressure. `InteractionUpdate` covers `text-delta`, `thinking-delta`, `thinking-completed`, `tool-call-started`, `tool-call-completed`, `partial-tool-call`, `token-delta`, `step-started`, `step-completed`, `turn-ended`, and a handful of summary and shell-output deltas.

### Per-send options

| Property      | Type                                          | Description                                                                                                                                                             |
| :------------ | :-------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`       | `ModelSelection`                              | Per-send model override. If omitted, uses `agent.model`. Sticky: a successful send updates `agent.model`.                                                               |
| `mcpServers`  | `Record<string, McpServerConfig>`             | Inline MCP server definitions. Fully replaces creation-time servers for this run.                                                                                       |
| `onStep`      | `(args: { step }) => void \| Promise<void>`   | Callback after each completed conversation step (text, thinking, or tool batch).                                                                                        |
| `onDelta`     | `(args: { update }) => void \| Promise<void>` | Callback per raw `InteractionUpdate`.                                                                                                                                   |
| `local.force` | `boolean`                                     | Local agents only. Defaults to `false`. Expire a stuck active run before starting this message. Cloud returns `409 agent_busy` server-side, so no equivalent is needed. |

***

The next three sections are detailed reference for `SDKMessage`, `InteractionUpdate`, and `ConversationTurn`. Skim or skip on a first read; [Resuming agents](https://cursor.com/docs/sdk/typescript.md#resuming-agents) picks up the narrative.

## Stream events

Events from `run.stream()`. Discriminate on `type`. All events include `agent_id` and `run_id`.

```typescript
type SDKMessage =
  | SDKSystemMessage
  | SDKUserMessageEvent
  | SDKAssistantMessage
  | SDKThinkingMessage
  | SDKToolUseMessage
  | SDKStatusMessage
  | SDKTaskMessage
  | SDKRequestMessage;
```

| `type`        | Description                                                                                      | Key fields                                                    |
| :------------ | :----------------------------------------------------------------------------------------------- | :------------------------------------------------------------ |
| `"system"`    | Init metadata. Emitted once at the start of a run.                                               | `subtype?` (`"init"`), `model?`, `tools?`                     |
| `"user"`      | Echo of the user prompt for this run.                                                            | `message.content: TextBlock[]`                                |
| `"assistant"` | Model text output.                                                                               | `message.content: (TextBlock \| ToolUseBlock)[]`              |
| `"thinking"`  | Reasoning content.                                                                               | `text`, `thinking_duration_ms?`                               |
| `"tool_call"` | Tool invocation lifecycle. Emitted at start with `args`, then again on completion with `result`. | `call_id`, `name`, `status`, `args?`, `result?`, `truncated?` |
| `"status"`    | Cloud run lifecycle transitions.                                                                 | `status`, `message?`                                          |
| `"task"`      | Task-level milestones and summaries.                                                             | `status?`, `text?`                                            |
| `"request"`   | Awaiting user input or approval.                                                                 | `request_id`                                                  |

Result data (final text, model, duration, git metadata) lives on the `Run` object after the stream completes. Use `run.wait()` to read it.

> **Tool call schema is not stable.** The `args` and `result` payloads on `tool_call` events reflect each tool's internal shape and can change as tools evolve. Tool names can also be renamed or replaced. Treat `args` and `result` as `unknown` and parse defensively. The event envelope (`type`, `call_id`, `name`, `status`) is stable.

### Message types

```typescript
interface SDKSystemMessage {
  type: "system";
  subtype?: "init";
  agent_id: string;
  run_id: string;
  model?: ModelSelection;
  tools?: string[];
}

interface SDKUserMessageEvent {
  type: "user";
  agent_id: string;
  run_id: string;
  message: { role: "user"; content: TextBlock[] };
}

interface SDKAssistantMessage {
  type: "assistant";
  agent_id: string;
  run_id: string;
  message: {
    role: "assistant";
    content: Array<TextBlock | ToolUseBlock>;
  };
}

interface SDKThinkingMessage {
  type: "thinking";
  agent_id: string;
  run_id: string;
  text: string;
  thinking_duration_ms?: number;
}

interface SDKToolUseMessage {
  type: "tool_call";
  agent_id: string;
  run_id: string;
  call_id: string;
  name: string;
  status: "running" | "completed" | "error";
  args?: unknown;
  result?: unknown;
  truncated?: { args?: boolean; result?: boolean };
}

interface SDKStatusMessage {
  type: "status";
  agent_id: string;
  run_id: string;
  status: "CREATING" | "RUNNING" | "FINISHED" | "ERROR" | "CANCELLED" | "EXPIRED";
  message?: string;
}

interface SDKTaskMessage {
  type: "task";
  agent_id: string;
  run_id: string;
  status?: string;
  text?: string;
}

interface SDKRequestMessage {
  type: "request";
  agent_id: string;
  run_id: string;
  request_id: string;
}

interface TextBlock {
  type: "text";
  text: string;
}

interface ToolUseBlock {
  type: "tool_use";
  id: string;
  name: string;
  input: unknown;
}
```

`SDKToolUseMessage` is emitted twice for most tool calls: first with `status: "running"` and `args` populated, then again on completion with `status: "completed"` (or `"error"`) and `result` populated. `truncated` flags whether the SDK truncated `args` or `result` because the payload was too large.

`SDKStatusMessage` covers cloud-side lifecycle transitions. `CREATING` covers VM provisioning and repo cloning; `RUNNING` is the agent doing work; the rest are terminal.

## Interaction updates

`InteractionUpdate` is the raw delta type passed to the `onDelta` callback on `agent.send()`. Updates are finer-grained than `SDKMessage` events: text streams in token-by-token, tool calls report partial state as args accumulate, thinking arrives as it happens.

```typescript
type InteractionUpdate =
  | TextDeltaUpdate
  | ThinkingDeltaUpdate
  | ThinkingCompletedUpdate
  | ToolCallStartedUpdate
  | ToolCallCompletedUpdate
  | PartialToolCallUpdate
  | TokenDeltaUpdate
  | StepStartedUpdate
  | StepCompletedUpdate
  | TurnEndedUpdate
  | UserMessageAppendedUpdate
  | SummaryUpdate
  | SummaryStartedUpdate
  | SummaryCompletedUpdate
  | ShellOutputDeltaUpdate;
```

### Update types

```typescript
interface TextDeltaUpdate {
  type: "text-delta";
  text: string;
}

interface ThinkingDeltaUpdate {
  type: "thinking-delta";
  text: string;
}

interface ThinkingCompletedUpdate {
  type: "thinking-completed";
  thinkingDurationMs: number;
}

interface ToolCallStartedUpdate {
  type: "tool-call-started";
  callId: string;
  toolCall: ToolCall;
  modelCallId: string;
}

interface PartialToolCallUpdate {
  type: "partial-tool-call";
  callId: string;
  toolCall: ToolCall;
  modelCallId: string;
}

interface ToolCallCompletedUpdate {
  type: "tool-call-completed";
  callId: string;
  toolCall: ToolCall;
  modelCallId: string;
}

interface TokenDeltaUpdate {
  type: "token-delta";
  tokens: number;
}

interface StepStartedUpdate {
  type: "step-started";
  stepId: number;
}

interface StepCompletedUpdate {
  type: "step-completed";
  stepId: number;
  stepDurationMs: number;
}

interface TurnEndedUpdate {
  type: "turn-ended";
  usage?: {
    inputTokens: number;
    outputTokens: number;
    cacheReadTokens: number;
    cacheWriteTokens: number;
  };
}

interface UserMessageAppendedUpdate {
  type: "user-message-appended";
  userMessage: UserMessage;
}

interface SummaryUpdate {
  type: "summary";
  summary: string;
}

interface SummaryStartedUpdate {
  type: "summary-started";
}

interface SummaryCompletedUpdate {
  type: "summary-completed";
}

interface ShellOutputDeltaUpdate {
  type: "shell-output-delta";
  event: Record<string, unknown>;
}
```

`PartialToolCallUpdate` is emitted as the model streams arguments into a tool call before it commits. The same stability disclaimer that applies to `SDKToolUseMessage.args` applies here.

## Conversation types

The structured per-turn view of a run, returned by `run.conversation()` and used in the `onStep` callback's argument.

```typescript
type ConversationTurn =
  | { type: "agentConversationTurn"; turn: AgentConversationTurn }
  | { type: "shellConversationTurn"; turn: ShellConversationTurn };

interface AgentConversationTurn {
  userMessage?: UserMessage;
  steps: ConversationStep[];
}

interface ShellConversationTurn {
  shellCommand?: ShellCommand;
  shellOutput?: ShellOutput;
}

type ConversationStep =
  | { type: "assistantMessage"; message: AssistantMessage }
  | { type: "toolCall"; message: ToolCall }
  | { type: "thinkingMessage"; message: ThinkingMessage };

interface AssistantMessage {
  text: string;
}

interface ThinkingMessage {
  text: string;
  thinkingDurationMs?: number;
}

interface UserMessage {
  text: string;
}

interface ShellCommand {
  command: string;
  workingDirectory?: string;
}

interface ShellOutput {
  stdout: string;
  stderr: string;
  exitCode: number;
}
```

`ToolCall` is a discriminated union over every built-in tool (shell, edit, read, write, glob, grep, ls, semSearch, mcp, task, and others). Its shape is internal-facing; see the [stability note](https://cursor.com/docs/sdk/typescript.md#stream-events) under Stream events.

## Resuming agents

```typescript
function Agent.resume(agentId: string, options?: Partial<AgentOptions>): Promise<SDKAgent>;
```

Use `Agent.resume()` to reattach to an existing agent by ID. Common flows: reconnecting to a long-running cloud agent that was kicked off earlier, or continuing a conversation after the local process restarted. Runtime is auto-detected from the ID prefix (`bc-` is cloud, anything else is local).

```typescript
await using agent = await Agent.resume("bc-abc123", {
  apiKey: process.env.CURSOR_API_KEY!,
});

const run = await agent.send("Also update the changelog");
await run.wait();
```

`agent.model` is `undefined` on resume unless you pass `model` again. Inline `mcpServers` are not persisted across resume — they often carry secrets and live in memory only. Pass them again on resume, or use file-based MCP config (`.cursor/mcp.json` + `local.settingSources`) for servers that should survive.

## Inspecting agents and runs

List, fetch, and reload past agents. List endpoints return `{ items, nextCursor? }` for cursor-based pagination.

### Agent.list()

```typescript
function Agent.list(options?: ListAgentsOptions): Promise<ListResult<SDKAgentInfo>>;

type ListAgentsOptions = {
  limit?: number;
  cursor?: string;
} & (
  | { runtime?: undefined }
  | { runtime: "local"; cwd?: string }
  | {
      runtime: "cloud";
      prUrl?: string;
      includeArchived?: boolean;
      apiKey?: string;
    }
);
```

```typescript
const { items, nextCursor } = await Agent.list({
  runtime: "local",
  cwd: process.cwd(),
});
```

### Agent.get()

```typescript
function Agent.get(agentId: string, options?: GetAgentOptions): Promise<SDKAgentInfo>;

interface GetAgentOptions {
  cwd?: string;       // local routing
  apiKey?: string;    // cloud routing
}
```

Runtime is auto-detected from the agent ID prefix (`bc-` → cloud, otherwise local).

### Agent.listRuns()

```typescript
function Agent.listRuns(agentId: string, options?: ListRunsOptions): Promise<ListResult<Run>>;

type ListRunsOptions = {
  limit?: number;
  cursor?: string;
} & (
  | { runtime?: "local"; cwd?: string }
  | { runtime: "cloud"; apiKey?: string }
);
```

### Agent.getRun()

```typescript
function Agent.getRun(runId: string, options?: GetRunOptions): Promise<Run>;

type GetRunOptions =
  | { runtime?: "local"; cwd?: string }
  | { runtime: "cloud"; agentId: string; apiKey?: string };
```

Cloud `getRun` requires the parent `agentId`.

### Cloud agent lifecycle

Cloud agents stay in your team's workspace until you archive or delete them. `Agent.list({ runtime: "cloud" })` hides archived agents by default; pass `includeArchived: true` to see them. Filter by `prUrl` to find the agent that opened a specific pull request.

```typescript
function Agent.archive(agentId: string, options?: AgentOperationOptions): Promise<void>;
function Agent.unarchive(agentId: string, options?: AgentOperationOptions): Promise<void>;
function Agent.delete(agentId: string, options?: AgentOperationOptions): Promise<void>;

interface AgentOperationOptions {
  cwd?: string;
  apiKey?: string;
}
```

```typescript
await Agent.archive(agentId);     // soft-delete; transcript stays readable
await Agent.unarchive(agentId);   // restore an archived agent
await Agent.delete(agentId);      // permanent; subsequent reads return 404
```

### SDKAgentInfo

The metadata shape returned by `Agent.list()` and `Agent.get()`.

```typescript
type SDKAgentInfo = {
  agentId: string;
  name: string;
  summary: string;
  lastModified: number;
  status?: "running" | "finished" | "error";
  createdAt?: number;
  archived?: boolean;
} & (
  | { runtime?: undefined }
  | { runtime: "local"; cwd?: string }
  | {
      runtime: "cloud";
      env?: { type: "cloud" | "pool" | "machine"; name?: string };
      repos?: string[];
    }
);
```

## The Cursor namespace

Account-level and catalog reads. All methods take an optional `{ apiKey }` and otherwise fall back to `CURSOR_API_KEY`.

### Cursor.me()

```typescript
function Cursor.me(options?: CursorRequestOptions): Promise<SDKUser>;

interface CursorRequestOptions {
  apiKey?: string;
}

interface SDKUser {
  apiKeyName: string;
  userEmail?: string;
  createdAt: string;
}
```

### Cursor.models.list()

```typescript
function Cursor.models.list(options?: CursorRequestOptions): Promise<SDKModel[]>;

type SDKModel = ModelListItem;

interface ModelListItem {
  id: string;
  displayName: string;
  description?: string;
  parameters?: ModelParameterDefinition[];
  variants?: ModelVariant[];
}

interface ModelParameterDefinition {
  id: string;
  displayName?: string;
  values: Array<{ value: string; displayName?: string }>;
}

interface ModelVariant {
  params: ModelParameterValue[];
  displayName: string;
  description?: string;
  isDefault?: boolean;
}
```

Use `Cursor.models.list()` to discover valid `model` ids and per-model `params` before calling `Agent.create()` or `agent.send()`. Parameters are model-specific. Common examples include reasoning effort and max mode.

```typescript
const models = await Cursor.models.list();
const composer = models.find((model) => model.id === "composer-2");

console.log(composer?.parameters);
// [
//   {
//     id: "thinking",
//     displayName: "Thinking",
//     values: [
//       { value: "low", displayName: "Low" },
//       { value: "high", displayName: "High" },
//     ],
//   },
// ]
```

Pass selected parameter values through `model.params`. Preset `variants` already contain valid `params`, so you can copy them into a model selection.

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: {
    id: "composer-2",
    params: [{ id: "thinking", value: "high" }],
  },
  local: { cwd: process.cwd() },
});
```

### Cursor.repositories.list()

```typescript
function Cursor.repositories.list(options?: CursorRequestOptions): Promise<SDKRepository[]>;

interface SDKRepository {
  url: string;
}
```

Returns the GitHub repositories connected for the calling user's team. Cloud only.

## MCP servers

Agents can pick up MCP servers from several sources. Inline definitions in `Agent.create()` or `agent.send()` are the most common path. File-based and dashboard-managed configs are also supported.

### What gets loaded

**Local agents** load servers from up to five sources, with first-match-wins precedence on conflicting names:

1. `mcpServers` on `agent.send()`. Fully replaces creation-time servers for that run (not merged).
2. `mcpServers` on `Agent.create()`. Used when no per-send override is provided.
3. Plugin servers, if `local.settingSources` includes `"plugins"`.
4. Project servers from `.cursor/mcp.json`, if `local.settingSources` includes `"project"`.
5. User servers from `~/.cursor/mcp.json`, if `local.settingSources` includes `"user"`.

Without `local.settingSources`, only inline servers are loaded. If a local MCP server requires OAuth login, the SDK can't prompt you to sign in. It only works if you've already signed in to that server from the Cursor app, in which case the SDK reuses that saved login.

**Cloud agents** load servers from:

1. `mcpServers` on `agent.send()`. Fully replaces creation-time servers for that run (not merged).
2. `mcpServers` on `Agent.create()`. Used when no per-send override is provided.
3. Your user and team MCP servers from [cursor.com/agents](https://cursor.com/agents).

If an inline server doesn't include `auth` or `headers` and you've previously authorized that server URL on cursor.com/agents, runs authenticated with a personal API token reuse those OAuth tokens automatically. Service account API keys cannot fall back to user auth as they are not associated with a user.

`local.settingSources` does not apply to cloud agents.

### Local

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "auto" },
  local: { cwd: process.cwd() },
  mcpServers: {
    docs: {
      type: "http",
      url: "https://example.com/mcp",
      auth: {
        CLIENT_ID: "client-id",
        scopes: ["read", "write"],
      },
    },
    filesystem: {
      type: "stdio",
      command: "npx",
      args: ["-y", "@modelcontextprotocol/server-filesystem", process.cwd()],
      cwd: process.cwd(),
    },
  },
});
```

### Cloud

Cloud agents can receive authenticated MCP configs inline too. Use HTTP auth when Cursor should proxy a remote MCP through the backend. Use stdio `env` when the server runs inside the cloud VM and reads credentials from environment variables.

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2" },
  cloud: {
    repos: [{ url: "https://github.com/your-org/your-repo", startingRef: "main" }],
  },
  mcpServers: {
    linear: {
      type: "http",
      url: "https://mcp.linear.app/sse",
      headers: {
        Authorization: `Bearer ${process.env.LINEAR_API_KEY!}`,
      },
    },
    figma: {
      type: "http",
      url: "https://api.figma.com/mcp",
      auth: {
        CLIENT_ID: process.env.FIGMA_CLIENT_ID!,
        CLIENT_SECRET: process.env.FIGMA_CLIENT_SECRET!,
        scopes: ["file_content:read"],
      },
    },
    github: {
      type: "stdio",
      command: "npx",
      args: ["-y", "@modelcontextprotocol/server-github"],
      env: {
        GITHUB_TOKEN: process.env.GITHUB_TOKEN!,
      },
    },
  },
});
```

Use `headers` for static API keys or Bearer tokens — Cursor passes them through on every request. Use `auth` for OAuth-protected servers. For cloud, Cursor runs the OAuth flow once server-side and reuses the token across runs. Locally, the SDK can't open a browser to sign you in; it only reuses tokens you've already obtained by signing in through the Cursor app.

- HTTP `headers` and `auth` are handled by Cursor's backend. Sensitive fields are redacted and do not enter the VM.
- Stdio `env` values are passed into the VM because the server runs there. Treat them like any other runtime secret.
- OAuth for MCP servers configured on cursor.com/agents stays per-user, even for team-level servers.

See [MCP](https://cursor.com/docs/mcp.md) for the full config format and [Cloud Agent capabilities](https://cursor.com/docs/cloud-agent/capabilities.md#mcp-tools) for cloud-specific behavior.

## Subagents

Define named subagents that the main agent spawns via the `Agent` tool. Pass them inline:

```typescript
const agent = await Agent.create({
  model: { id: "composer-2" },
  apiKey: process.env.CURSOR_API_KEY!,
  local: { cwd: process.cwd() },
  agents: {
    "code-reviewer": {
      description: "Expert code reviewer for quality and security.",
      prompt: "Review code for bugs, security issues, and proven approaches.",
      model: "inherit",
    },
    "test-writer": {
      description: "Writes tests for code changes.",
      prompt: "Write comprehensive tests for the given code.",
    },
  },
});
```

Subagents committed to the repo at `.cursor/agents/*.md` (with `name`, `description`, and optional `model` frontmatter) are also picked up. Inline definitions override file-based ones with the same name.

## Hooks

Hooks are file-based only. There is no programmatic hook callback. Hooks are a project policy boundary, not a per-run knob.

- **Local:** Add `.cursor/hooks.json` to the repo passed as `local.cwd`, or add `~/.cursor/hooks.json` for user-level hooks.
- **Cloud:** Commit `.cursor/hooks.json` and its scripts to the repo passed in `cloud.repos`. SDK-created cloud agents load project hooks automatically. On Enterprise plans, they also run team hooks and enterprise-managed hooks.

See [Hooks](https://cursor.com/docs/hooks.md) for the configuration format and [Cloud Agents hooks support](https://cursor.com/docs/cloud-agent.md#hooks-support) for cloud behavior.

## Artifacts

List and download files from the agent's workspace.

```typescript
interface SDKArtifact {
  path: string;
  sizeBytes: number;
  updatedAt: string;
}
```

```typescript
const artifacts: SDKArtifact[] = await agent.listArtifacts();

for (const artifact of artifacts) {
  console.log(artifact.path, artifact.sizeBytes);
}

const buffer = await agent.downloadArtifact(artifacts[0].path);
```

Artifact support is runtime-dependent. Local SDK agents currently return no artifacts and throw for `downloadArtifact`.

## Resource management

Always dispose agents when done. The cleanest pattern is `await using`:

```typescript
await using agent = await Agent.create({ /* ... */ });
// disposed automatically when the block exits
```

To dispose explicitly:

```typescript
await agent[Symbol.asyncDispose]();
```

`agent.close()` starts disposal without awaiting. `agent.reload()` picks up filesystem config changes (hooks, project MCP, subagents) without disposing.

## Configuration reference

### AgentOptions

| Property     | Type                                                                                                    | Default                                                             | Description                                                                                                                            |
| :----------- | :------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------- |
| `model`      | `ModelSelection`                                                                                        | Required for local; cloud falls back to the server-resolved default | Model to use. See [`ModelSelection`](https://cursor.com/docs/sdk/typescript.md#modelselection).                                        |
| `apiKey`     | `string`                                                                                                | `CURSOR_API_KEY` env                                                | User API key or service account key. Team Admin keys are not yet supported.                                                            |
| `name`       | `string`                                                                                                | Auto-generated                                                      | Human-readable agent name surfaced as `title` in `Agent.list()` / `Agent.get()`.                                                       |
| `local`      | `{ cwd?: string \| string[]; settingSources?: SettingSource[]; sandboxOptions?: { enabled: boolean } }` |                                                                     | Local agent config. `settingSources` picks ambient settings layers: `"project"`, `"user"`, `"team"`, `"mdm"`, `"plugins"`, or `"all"`. |
| `cloud`      | `CloudOptions`                                                                                          |                                                                     | Cloud agent config.                                                                                                                    |
| `mcpServers` | `Record<string, McpServerConfig>`                                                                       |                                                                     | Inline MCP server definitions.                                                                                                         |
| `agents`     | `Record<string, AgentDefinition>`                                                                       |                                                                     | Subagent definitions.                                                                                                                  |
| `agentId`    | `string`                                                                                                | Auto-generated                                                      | Durable agent ID. Pass to keep a stable ID across invocations.                                                                         |

### CloudOptions

| Property              | Type                                                                                                        | Default             | Description                                                                                                                                                       |
| :-------------------- | :---------------------------------------------------------------------------------------------------------- | :------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `env`                 | `{ type: "cloud"; name?: string } \| { type: "pool"; name?: string } \| { type: "machine"; name?: string }` | `{ type: "cloud" }` | Execution environment. `cloud` uses Cursor-hosted VMs; `pool` and `machine` target a [self-hosted pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md). |
| `repos`               | `Array<{ url: string; startingRef?: string; prUrl?: string }>`                                              |                     | Repositories to clone into the VM. Pass `prUrl` to attach the agent to an existing PR.                                                                            |
| `workOnCurrentBranch` | `boolean`                                                                                                   | `false`             | Push commits to the existing branch instead of a new one.                                                                                                         |
| `autoCreatePR`        | `boolean`                                                                                                   | `false`             | Open a PR when the run finishes.                                                                                                                                  |
| `skipReviewerRequest` | `boolean`                                                                                                   | `false`             | Skip requesting the calling user as a reviewer on the PR.                                                                                                         |

### AgentDefinition

| Property      | Type                                               | Default     | Description                                                                                     |
| :------------ | :------------------------------------------------- | :---------- | :---------------------------------------------------------------------------------------------- |
| `description` | `string`                                           | *required*  | When to use this subagent. Shown to the parent agent so it knows when to spawn.                 |
| `prompt`      | `string`                                           | *required*  | System prompt for the subagent.                                                                 |
| `model`       | `ModelSelection \| "inherit"`                      | `"inherit"` | Model override. Pass `"inherit"` to use the parent's selection.                                 |
| `mcpServers`  | `Array<string \| Record<string, McpServerConfig>>` |             | MCP servers available to this subagent. Names reference servers from the parent's `mcpServers`. |

### ModelSelection

```typescript
interface ModelSelection {
  id: string;
  params?: ModelParameterValue[];
}

interface ModelParameterValue {
  id: string;
  value: string;
}
```

`id` is the model identifier (for example, `"composer-2"`). `params` carries per-model parameters such as reasoning effort. Use [`Cursor.models.list()`](https://cursor.com/docs/sdk/typescript.md#cursormodelslist) to discover valid ids, parameter definitions, and preset variants for your account.

### McpServerConfig

```typescript
type McpServerConfig =
  // stdio
  | {
      type?: "stdio";
      command: string;
      args?: string[];
      env?: Record<string, string>;
      cwd?: string;       // local only; cloud rejects this field
    }
  // HTTP / SSE
  | {
      type?: "http" | "sse";
      url: string;
      headers?: Record<string, string>;   // passed through; Authorization here works
      auth?: {
        CLIENT_ID: string;
        CLIENT_SECRET?: string;
        scopes?: string[];
      };
    };
```

For HTTP servers running in the cloud, `headers` and `auth` are handled by Cursor's backend. Sensitive fields are redacted before the VM sees them. For stdio servers in the cloud, `env` values are passed into the VM (treat them like any runtime secret).

### SDKUserMessage

```typescript
interface SDKUserMessage {
  text: string;
  images?: SDKImage[];
}
```

The structured form of `agent.send()`'s message argument. Use it to send images alongside text.

### SDKImage

```typescript
type SDKImage =
  | { url: string; dimension?: SDKImageDimension }
  | { data: string; mimeType: string; dimension?: SDKImageDimension };

interface SDKImageDimension {
  width: number;
  height: number;
}
```

Pass either a remote `url` or base64 `data` with a `mimeType`.

### SettingSource

```typescript
type SettingSource =
  | "project"
  | "user"
  | "team"
  | "mdm"
  | "plugins"
  | "all";
```

Controls which on-disk settings layers a local agent loads. Cloud agents always load `project` / `team` / `plugins` and ignore this field.

| Value       | Source                                  |
| :---------- | :-------------------------------------- |
| `"project"` | `.cursor/` in the workspace             |
| `"user"`    | `~/.cursor/`                            |
| `"team"`    | Team settings synced from the dashboard |
| `"mdm"`     | MDM-managed enterprise settings         |
| `"plugins"` | Plugin-provided settings                |
| `"all"`     | Shorthand for all of the above          |

### ListResult

```typescript
interface ListResult<T> {
  items: T[];
  nextCursor?: string;
}
```

Returned by `Agent.list()` and `Agent.listRuns()`. `nextCursor` is absent when there are no more pages.

## Errors

All SDK errors extend `CursorAgentError`. Use `isRetryable` to drive retry logic.

```typescript
class CursorAgentError extends Error {
  readonly isRetryable: boolean;
  readonly code?: string;
  readonly cause?: unknown;
  readonly protoErrorCode?: string;
}
```

| Error                          | When                                                                   |
| :----------------------------- | :--------------------------------------------------------------------- |
| `AuthenticationError`          | Invalid API key, not logged in, insufficient permissions.              |
| `RateLimitError`               | Too many requests or usage limits exceeded.                            |
| `ConfigurationError`           | Invalid model, bad request parameters.                                 |
| `IntegrationNotConnectedError` | Creating a cloud agent for a repo whose SCM provider is not connected. |
| `NetworkError`                 | Service unavailable, timeout.                                          |
| `UnknownAgentError`            | Catch-all for unclassified server or runtime errors.                   |

### IntegrationNotConnectedError

```typescript
class IntegrationNotConnectedError extends ConfigurationError {
  readonly provider: string;   // e.g. "github", "gitlab", "azuredevops"
  readonly helpUrl: string;    // dashboard link to reconnect
}
```

Use `helpUrl` to point the user at the right reconnect flow. New providers will be added without an SDK release.

### UnsupportedRunOperationError

```typescript
class UnsupportedRunOperationError extends Error {
  readonly operation: RunOperation;
}
```

Thrown when a `Run` operation is not available on the current runtime. Use `run.supports(operation)` and `run.unsupportedReason(operation)` to check before calling.

## Known limitations

- Inline `mcpServers` are not persisted across `Agent.resume()`. Pass them again on resume if needed.
- Artifact download is not implemented for local agents (`agent.listArtifacts()` returns an empty list and `agent.downloadArtifact()` throws).
- `local.settingSources` (and the file-based MCP / subagent paths it gates) does not apply to cloud agents. Cloud always loads `project` / `team` / `plugins`.
- Hooks are file-based only (`.cursor/hooks.json`). No programmatic callbacks.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
