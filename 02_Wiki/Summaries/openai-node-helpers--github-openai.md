---
type: summary
source: 01_Raw/github/openai/openai-node/helpers.md
source_url: https://github.com/openai/openai-node/blob/main/helpers.md
title: "openai-node — SDK Helpers (Structured Outputs, Streaming, Polling)"
summarized_at: 2026-05-05
entities_referenced: ["OpenAI", "Zod", "Next.js", "Express"]
concepts_referenced: ["Structured Outputs", "Zod schema", "zodResponseFormat", "zodFunction", "streaming helpers", "ChatCompletionStreamingRunner", "runTools", "assistant streaming", "polling helpers", "vector stores", "ParsedChatCompletion"]
---

SDK helper methods beyond the basic API wrappers.

## Structured Outputs
- client.chat.completions.parse() — TypeScript-type-integrated wrapper over .create()
- zodResponseFormat(schema, name) — wrap Zod schema; auto-converts to JSON Schema, parses response back
- zodFunction({name, parameters}) — Zod schema for function tools
- Restrictions vs .create(): raises LengthFinishReasonError / ContentFilterFinishReasonError; only strict function tools

## Streaming Helpers
- openai.chat.completions.stream() returns ChatCompletionStreamingRunner (events, async iterator, accumulates chunks)
- openai.chat.completions.runTools({...}) — auto-calls JS functions for tool calls, loops until complete
- stream.abort() to cancel; maxChatCompletions option (default 10)

## Chat Events (.on(event, handler))
connect, chunk, chatCompletion, message, content, content.delta, content.done, refusal.delta, refusal.done, tool_calls.function.arguments.delta/.done, logprobs.content.delta/.done, logprobs.refusal.delta/.done, finalChatCompletion, finalContent, finalMessage, error, abort, totalUsage, end

## Assistant Streaming
- openai.beta.threads.runs.stream() / createAndRunStream() / submitToolOutputsStream()
- Events: runStepCreated/Delta/Done, messageCreated/Delta/Done, textCreated/Delta/Done, toolCallCreated/Delta/Done, end
- Methods: currentEvent(), currentRun(), currentMessageSnapshot(), finalMessages(), finalRunSteps()

## Polling Helpers
createAndRunPoll(), runs.createAndPoll(), runs.submitToolOutputsAndPoll(), vectorStores.files.uploadAndPoll(), vectorStores.fileBatches.uploadAndPoll()

## Bulk Upload
openai.vectorStores.fileBatches.uploadAndPoll(vectorStore.id, {files: fileList})
