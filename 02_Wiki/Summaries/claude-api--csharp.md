---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/csharp/claude-api.md
title: "Claude API — C#"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Tool-use, Extended-thinking, Prompt-caching]
---

C# binding patterns for the official `Anthropic` NuGet SDK. Tool use supported via Messages API; class-annotation tool runner is NOT available — use raw `Tool` definitions with JSON schema. Microsoft.Extensions.AI `IChatClient` integration with function invocation supported.

`dotnet add package Anthropic`. Default `AnthropicClient client = new()` reads `ANTHROPIC_API_KEY` env var.

**Basic message**: `MessageCreateParams` with `Model.ClaudeOpus4_6`, `MaxTokens`, `Messages`. `ContentBlock` is a union; unwrap via `.Value` + `OfType<TextBlock>` OR `TryPick*` idiom.

**Streaming**: `client.Messages.CreateStreaming(...)` yields `RawMessageStreamEvent`. TryPick methods drop `Message`/`Raw` prefix: `TryPickStart`, `TryPickDelta`, `TryPickStop`, `TryPickContentBlockStart/Delta/Stop` (no `TryPickMessageStop`).

**Thinking**: adaptive recommended for 4.6+. `Thinking = new ThinkingConfigAdaptive()`. `ThinkingBlock` precedes `TextBlock` in response Content. `ThinkingConfigEnabled { BudgetTokens = N }` deprecated.

**Tool use**: Use `Tool` (NOT `ToolParam`) with `InputSchema` record. `InputSchema.Type` auto-set; don't override. Implicit conversion to `ToolUnion` via `[...]` collection expression.

**Tool-result round-trip**: NO `.ToParam()` helper — manually reconstruct each `ContentBlock` variant as its `*Param` counterpart. `new ContentBlockParam(block.Json)` compiles but degrades to JSON pass-through with `.Value == null` (TryPick/Validate fail). Process each `TryPickText/Thinking/RedactedThinking/ToolUse` and build matching `*Param`. Thinking signature MUST be preserved or API rejects. One `ToolResultBlockParam` per `ToolUseBlock` ID — API rejects unmatched IDs.

**Beta context editing/compaction**: Beta-namespace prefix is INCONSISTENT. `MessageCreateParams`, `MessageCountTokensParams`, `Role` have NO Beta prefix; everything else (`BetaMessageParam`, `BetaContentBlock`, `BetaToolUseBlock`) does. `Role` collides if both namespaces imported (CS0104) — alias one. `Betas: ["compact-2026-01-12"]`. `BetaContentBlock` is 15-variant union including `Text`, `Thinking`, `RedactedThinking`, `ToolUse`, `ServerToolUse`, `WebSearch/Fetch/CodeExecution/Bash/TextEditor/ToolSearch ToolResult`, `McpToolUse`, `McpToolResult`, `ContainerUpload`, `Compaction`. `Compaction.Content` nullable (server-side failure possible). Round-trip same way as non-beta — no `.ToParam()`.

**Effort**: nested under `OutputConfig.Effort`, NOT top-level. Values: `Effort.Low/Medium/High/Max`. Combine with `ThinkingConfigAdaptive` for cost-quality trade-off.

**Prompt caching**: `System` is `MessageCreateParamsSystem?` (string OR `List<TextBlockParam>`). NO `SystemTextBlockParam`; use plain `TextBlockParam`. Implicit conversion needs concrete `List<TextBlockParam>` (array literals don't convert). `CacheControlEphemeral` auto-sets type. Optional `Ttl = Ttl.Ttl1h` or `Ttl.Ttl5m`. Verify via `response.Usage.CacheCreationInputTokens` / `CacheReadInputTokens`.

**Token counting**: `client.Messages.CountTokens(...)`. `MessageCountTokensParams.Tools` uses different union (`MessageCountTokensTool` vs `ToolUnion`).

**Structured output**: `OutputConfig.Format = new JsonOutputFormat { Schema = ... }`. Type auto-set to `json_schema`.

**PDF input**: `DocumentBlockParam` with `Base64PdfSource`/`UrlPdfSource`/`PlainTextSource`/`ContentBlockSource`. Base64 auto-sets `MediaType = application/pdf`.

**Server tools**: `WebSearchTool20260209`, `ToolBash20250124`, `ToolTextEditor20250728`, `CodeExecutionTool20260120`, `WebFetchTool20260209`, `MemoryTool20250818`. Constructors auto-set name/type. All implicit-convert to `ToolUnion`.

**Files API (Beta)**: `client.Beta.Files.Upload(...)`. `BinaryContent` implicit-converts from `Stream` and `byte[]`. Referencing requires Beta message types (`BetaRequestDocumentBlock` with `BetaFileDocumentSource`); non-beta union has no file-ID variant.
