---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/php/claude-api.md
title: "claude-api skill: PHP SDK reference"
summarized_at: 2026-05-05
entities_referenced: [Skill, Enterprise-gateway]
concepts_referenced: [Tool-use, Extended-thinking, Prompt-caching]
---

PHP SDK reference inside the `claude-api` skill. Official Anthropic PHP SDK with beta tool runner via `$client->beta->messages->toolRunner()`, `StructuredOutputModel` helpers, Bedrock/Vertex/Foundry support. Agent SDK NOT available.

**Install**: `composer require "anthropic-ai/sdk"`.

**Client**: `new Client(apiKey: getenv("ANTHROPIC_API_KEY"))`.
- **Bedrock**: `Bedrock\Client::fromEnvironment(region: 'us-east-1')` (constructor private; static factory).
- **Vertex**: `Vertex\Client::fromEnvironment(location: 'us-east5', projectId: 'my-project-id')` (parameter is `location`, NOT `region`).
- **Foundry**: `Foundry\Client::withCredentials(authToken: ..., baseUrl: '...')`.

**Basic message**: `$client->messages->create(model: 'claude-opus-4-7', maxTokens: 16000, messages: [['role' => 'user', 'content' => '...']])`. Content is array of polymorphic blocks (TextBlock, ToolUseBlock, ThinkingBlock). **ALWAYS guard `$block->type === 'text'` before accessing `->text`** — accessing `->text` on a ThinkingBlock throws.

**Streaming**: requires SDK v0.5.0+ for named parameters. `createStream(...)` then `foreach ($stream as $event)`, check `$event instanceof RawContentBlockDeltaEvent && $event->delta instanceof TextDelta`.

**Tool runner (beta)**: `BetaRunnableTool` with `definition` array + `run` closure. `$client->beta->messages->toolRunner(...)` returns iterable of messages.

**Manual loop**: tools as PHP arrays. **SDK uses camelCase keys** (`inputSchema`, `toolUseID`, `stopReason`) and auto-maps to API snake_case on wire — since v0.5.0. Loop: `while ($response->stopReason === 'tool_use')` → walk content for `ToolUseBlock`s → build tool_result array → append assistant + user turns → re-call `messages->create`.

**Extended thinking**: `thinking: ['type' => 'adaptive']`. Walk content for `ThinkingBlock` (preserve `$block->signature` verbatim in multi-turn). Old `['type' => 'enabled', 'budgetTokens' => N]` deprecated.

**Prompt caching**: `system:` takes array of text blocks; set `cacheControl` on last. 1h TTL: `'cacheControl' => ['type' => 'ephemeral', 'ttl' => '1h']`. Top-level `cacheControl:` on `messages->create()` auto-places. Verify via `$message->usage->cacheCreationInputTokens` / `cacheReadInputTokens`.

**Structured outputs** (recommended): define class implementing `StructuredOutputModel`, use `StructuredOutputModelTrait`, `#[Constrained(description: '...')]` attribute. `outputConfig: ['format' => Person::class]`. Get parsed: `$message->parsedOutput()`. Nullable types (`?string`) become optional. Or raw schema via `outputConfig: ['format' => ['type' => 'json_schema', 'schema' => [...]]]`.

**Beta features**: `betas:` is NOT a param on `$client->messages->create()` — only on the **beta namespace** `$client->beta->messages->create()`. Example: MCP servers via `mcpServers:` + `betas: ['mcp-client-2025-11-20']`.

**Server-side tools** (GA, both paths): non-beta types under `Anthropic\Messages\` (e.g. `ToolBash20250124`, `WebSearchTool20260209`, `ToolTextEditor20250728`, `CodeExecutionTool20260120`); beta variants prefixed `Beta` under `Anthropic\Beta\Messages\`. No `betas:` header needed for these.
