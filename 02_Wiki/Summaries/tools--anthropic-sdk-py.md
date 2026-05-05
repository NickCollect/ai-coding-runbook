---
type: summary
source: 01_Raw/github/anthropics/anthropic-sdk-python/tools.md
source_url: https://github.com/anthropics/anthropic-sdk-python/blob/main/tools.md
title: "Anthropic SDK Python — tools.md (tool helpers)"
summarized_at: 2026-05-05
entities_referenced: [Anthropic-SDK-Python, Tool-runner]
concepts_referenced: [Tool-use]
---

Tool-definition helpers in the Python SDK.

**`@beta_tool` decorator.** Decorate a regular Python function with `@beta_tool` (or `@beta_async_tool` for the async client) and the SDK inspects the signature and docstring to derive a JSON Schema input spec. Example: a `sum(left: int, right: int) -> str` function whose docstring documents both args becomes a tool with `name: "sum"`, the docstring summary as `description`, and an `input_schema` listing both parameters with descriptions, types, and titles, and `required: ["left", "right"]`.

**Calling the tool yourself.** Pass `tools=[get_weather.to_dict()]` to `client.beta.messages.create(...)` and handle `tool_use` blocks manually.

**Tool runner.** `client.beta.messages.tool_runner(...)` returns a `BetaToolRunner` iterator that automatically calls tools defined with `@beta_tool`. Each iteration yields a new `BetaMessage` from an API call; iteration stops when no more tool-call content blocks remain. Example pattern:

```py
runner = client.beta.messages.tool_runner(
    max_tokens=1024,
    model="claude-sonnet-4-5-20250929",
    tools=[sum],
    messages=[{"role": "user", "content": "What is 9 + 10?"}],
)
for message in runner:
    rich.print(message)
```

**`ToolError`.** To report a tool error back to the model, raise `ToolError` (from `anthropic.lib.tools`). Unlike a plain exception, `ToolError` accepts content blocks, so the error response can include images or other structured content. A plain exception's `repr()` is sent to the model as a text error and logged; `ToolError` is **not** logged because it represents an intentional error response. Example: a `take_screenshot(url)` tool can raise `ToolError([{"type": "text", ...}, {"type": "image", "source": ...}])` to send both a textual reason and the failure screenshot back to Claude.
