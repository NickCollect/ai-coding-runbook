---
type: summary
source: 01_Raw/github/openai/openai-python/helpers.md
source_url: https://github.com/openai/openai-python/blob/main/helpers.md
title: "openai-python — SDK Helpers (Structured Outputs, Streaming, Polling)"
summarized_at: 2026-05-05
entities_referenced: ["OpenAI", "Pydantic"]
concepts_referenced: ["Structured Outputs", "Pydantic model", "pydantic_function_tool", "streaming helpers", "ChatCompletionStream", "AssistantEventHandler", "polling helpers", "vector stores"]
---

Python SDK helper methods.

## Structured Outputs
- client.chat.completions.parse(): Pydantic-integrated wrapper over .create()
- Pass Pydantic model class as response_format; SDK auto-generates JSON schema and parses response back
- openai.pydantic_function_tool(ModelClass): use Pydantic model for function tool definitions
- Restrictions: raises LengthFinishReasonError / ContentFilterFinishReasonError; only strict tools

## Streaming Helpers (Chat Completions)
- client.chat.completions.stream(...) returns ChatCompletionStream (context manager required)
- Events: ChunkEvent, ContentDeltaEvent, ContentDoneEvent, RefusalDeltaEvent, RefusalDoneEvent, FunctionToolCallArgumentsDeltaEvent, FunctionToolCallArgumentsDoneEvent, LogprobsContentDeltaEvent/DoneEvent, LogprobsRefusalDeltaEvent/DoneEvent
- Methods: get_final_completion(), until_done()

## Assistant Streaming
- client.beta.threads.runs.stream() / create_and_run_stream() / submit_tool_outputs_stream()
- Subclass AssistantEventHandler and override: on_text_created, on_text_delta, on_tool_call_created, etc.
- Methods: current_event(), current_run(), get_final_run(), get_final_run_steps(), get_final_messages()

## Polling Helpers
create_and_run_poll(), runs.create_and_poll(), runs.submit_tool_outputs_and_poll(), vector_stores.files.upload_and_poll(), vector_stores.file_batches.create_and_poll(), vector_stores.file_batches.upload_and_poll(), videos.create_and_poll()
poll_interval_ms parameter controls polling frequency.
