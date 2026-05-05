---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/go/claude-api.md
title: "claude-api skill: Go SDK reference"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: [Tool-use, Extended-thinking, Prompt-caching]
---

Go SDK reference inside the `claude-api` skill. Go SDK supports Claude API + beta tool use via `BetaToolRunner`. Agent SDK NOT yet available for Go.

**Install**: `go get github.com/anthropics/anthropic-sdk-go`.

**Client**: `anthropic.NewClient()` (uses `ANTHROPIC_API_KEY`) or with `option.WithAPIKey(...)`.

**Basic message**: `client.Messages.New(ctx, anthropic.MessageNewParams{Model: anthropic.ModelClaudeOpus4_6, MaxTokens: 16000, Messages: []anthropic.MessageParam{anthropic.NewUserMessage(anthropic.NewTextBlock("..."))})`. Iterate response content via `block.AsAny().(type)` switch on `anthropic.TextBlock`.

**Streaming**: `client.Messages.NewStreaming(...)` then iterate `stream.Next()` switching on `anthropic.ContentBlockDeltaEvent` → `anthropic.TextDelta`. NO `GetFinalMessage()` — accumulate manually: `message := anthropic.Message{}; for stream.Next() { message.Accumulate(stream.Current()) }`.

**Tool runner (beta)**: `toolrunner` package. Define struct with `jsonschema` tags → `toolrunner.NewBetaToolFromJSONSchema(name, desc, func(ctx, input) (BetaToolResultBlockParamContentUnion, error) {...})`. Pass to `client.Beta.Messages.NewToolRunner(...)`. Methods: `RunToCompletion()`, `All()`, `NextMessage()`, streaming variant `NewToolRunnerStreaming()` + `AllStreaming()`. Returns `BetaTextBlock` (note Beta-namespace types).

**Manual loop**: `ToolParam` with `InputSchema: ToolInputSchemaParam{Properties: map[string]any{...}}`. Wrap in `ToolUnionParam{OfTool: &t}`. Append assistant response via `resp.ToParam()`. Walk via `block.AsAny().(type)`. Get tool input as raw JSON: `variant.JSON.Input.Raw()` → unmarshal. Build tool result: `anthropic.NewToolResultBlock(block.ID, result, false)`. Loop while `resp.StopReason == anthropic.StopReasonToolUse`. Tool results in user message via `anthropic.NewUserMessage(toolResults...)`.

**Thinking**: `Thinking: anthropic.ThinkingConfigParamUnion{OfAdaptive: &adaptive}` where `adaptive := anthropic.NewThinkingConfigAdaptiveParam()`. NO `ThinkingConfigParamOfAdaptive` helper. Iterate response with switch on `ThinkingBlock` then `TextBlock`. Old fixed-budget deprecated.

**Prompt caching**: `System: []TextBlockParam{{Text: ..., CacheControl: anthropic.NewCacheControlEphemeralParam()}}`. 1h TTL: `CacheControlEphemeralParam{TTL: anthropic.CacheControlEphemeralTTLTTL1h}`. Top-level `CacheControl` on `MessageNewParams` auto-places. Verify via `resp.Usage.CacheCreationInputTokens` / `CacheReadInputTokens`.

**Server-side tools**: version-suffixed struct names. Wrap in `ToolUnionParam` with matching `Of*` field. Examples: `WebSearchTool20260209Param`, `ToolBash20250124Param`, `ToolTextEditor20250728Param`, `CodeExecutionTool20260120Param`, `WebFetchTool20260209Param`, `MemoryTool20250818Param`, `ToolSearchToolBm25_20251119Param`, `ToolSearchToolRegex20251119Param`.

**PDF input**: `anthropic.NewDocumentBlock(anthropic.Base64PDFSourceParam{Data: b64})`. Other sources: `URLPDFSourceParam`, `PlainTextSourceParam`.

**Files API (beta)**: `client.Beta.Files.Upload(ctx, BetaFileUploadParams{File: anthropic.File(reader, name, contentType), Betas: [...]})`. Methods: `List`, `Delete`, `Download`, `GetMetadata`. Method name is **`Upload`** not `New`/`Create`.

**Compaction (beta)**: `client.Beta.Messages.New` with `ContextManagement: BetaContextManagementConfigParam{Edits: [...]}`. NO `NewBetaAssistantMessage` — use `.ToParam()`. Other edit types: `BetaClearToolUses20250919EditParam`, `BetaClearThinking20251015EditParam`. Beta header `compact-2026-01-12`.
