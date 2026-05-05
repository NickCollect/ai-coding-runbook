# Streaming API responses

<!-- source: https://platform.openai.com/docs/guides/streaming-responses -->

By default, the OpenAI API generates the entire output before sending it back. Streaming lets you start processing the beginning of the model's output while it continues generating.

Uses server-sent events (SSE) with `stream=True`.

## Enable streaming

```python
response = client.responses.create(
    model="gpt-5.5",
    input="Tell me a story",
    stream=True,
)

for event in response:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
```

## Key event types

```
- response.created          (once)
- response.output_text.delta  (multiple, text chunks)
- response.completed        (once)
- error
```

Full event taxonomy:
- `ResponseCreatedEvent`, `ResponseInProgressEvent`, `ResponseFailedEvent`, `ResponseCompletedEvent`
- `ResponseOutputItemAdded`, `ResponseOutputItemDone`
- `ResponseContentPartAdded`, `ResponseContentPartDone`
- `ResponseOutputTextDelta`, `ResponseOutputTextAnnotationAdded`, `ResponseTextDone`
- `ResponseRefusalDelta`, `ResponseRefusalDone`
- `ResponseFunctionCallArgumentsDelta`, `ResponseFunctionCallArgumentsDone`
- `ResponseFileSearchCallInProgress/Searching/Completed`
- `ResponseCodeInterpreterInProgress/CallCodeDelta/CallCodeDone/Interpreting/Completed`

## Advanced use cases

- **Streaming function calls**: see function-calling guide
- **Streaming structured output**: see structured-outputs guide

## Moderation risk

Streaming partial completions makes content moderation more difficult. Partial completions may be harder to evaluate for policy violations.

## WebSocket mode

For persistent WebSocket transport with incremental inputs via `previous_response_id`, see the Responses API WebSocket mode guide.
