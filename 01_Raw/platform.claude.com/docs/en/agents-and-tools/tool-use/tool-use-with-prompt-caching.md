---
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching
fetched_at: 2026-05-04T16:08:37.669268+00:00
fetch_method: mintlify_md
---

# Tool use with prompt caching

Cache tool definitions across turns and understand what invalidates your cache.

---

This page covers prompt caching for tool definitions: where to place `cache_control` breakpoints, how `defer_loading` preserves your cache, and what invalidates it. For general prompt caching, see [Prompt caching](https://platform.claude.com/docs/en/agents-and-tools/tool-use/Prompt caching).

## cache_control on tool definitions

Place `cache_control: {"type": "ephemeral"}` on the last tool in your `tools` array. This caches the entire tool-definitions prefix, from the first tool through the marked breakpoint:

```json
{
  "tools": [
    {
      "name": "get_weather",
      "description": "Get the current weather in a given location",
      "input_schema": {
        "type": "object",
        "properties": {
          "location": { "type": "string" }
        },
        "required": ["location"]
      }
    },
    {
      "name": "get_time",
      "description": "Get the current time in a given time zone",
      "input_schema": {
        "type": "object",
        "properties": {
          "timezone": { "type": "string" }
        },
        "required": ["timezone"]
      },
      "cache_control": { "type": "ephemeral" }
    }
  ]
}
```

For `mcp_toolset`, the `cache_control` breakpoint lands on the last tool in the set. You don't control tool order within an MCP toolset, so place the breakpoint on the `mcp_toolset` entry itself and the API applies it to the final expanded tool.

## defer_loading and cache preservation

Deferred tools are not included in the system-prompt prefix. When the model discovers a deferred tool through [tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool search), the definition is appended inline as a `tool_reference` block in the conversation history. The prefix is untouched, so prompt caching is preserved.

This means adding tools dynamically through tool search does not break your cache. You can start a conversation with a small set of always-loaded tools (cached), let the model discover additional tools as needed, and keep the same cache hit across every turn.

`defer_loading` also acts independently of grammar construction for [strict mode](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict mode). The grammar builds from the full toolset regardless of which tools are deferred, so prompt caching and grammar caching are both preserved when tools load dynamically.

## What invalidates your cache

The cache follows a prefix hierarchy (`tools` → `system` → `messages`), so a change at one level invalidates that level and everything after it:

| Change | Invalidates |
|---|---|
| Modifying tool definitions | Entire cache (tools, system, messages) |
| Toggling web search or citations | System and messages caches |
| Changing `tool_choice` | Messages cache |
| Changing `disable_parallel_tool_use` | Messages cache |
| Toggling images present/absent | Messages cache |
| Changing thinking parameters | Messages cache |

<Note>
If you need to vary `tool_choice` mid-conversation, consider placing cache breakpoints before the variation point.
</Note>

## Per-tool interaction table

| Tool | Caching considerations |
|---|---|
| [Web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/Web search) | Enabling or disabling invalidates the system and messages caches |
| [Web fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/Web fetch) | Enabling or disabling invalidates the system and messages caches |
| [Code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/Code execution) | Container state is independent of prompt cache |
| [Tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/Tool search) | Discovered tools load as `tool_reference` blocks, preserving prefix cache |
| [Computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/Computer use) | Screenshot presence affects messages cache |
| [Text editor](https://platform.claude.com/docs/en/agents-and-tools/tool-use/Text editor) | Standard client tool, no special caching interaction |
| [Bash](https://platform.claude.com/docs/en/agents-and-tools/tool-use/Bash) | Standard client tool, no special caching interaction |
| [Memory](https://platform.claude.com/docs/en/agents-and-tools/tool-use/Memory) | Standard client tool, no special caching interaction |

## Next steps

<CardGroup cols={3}>
  <Card title="Prompt caching" icon="database" href="/docs/en/build-with-claude/prompt-caching">
    Learn the full prompt caching model, including TTLs and pricing.
  </Card>
  <Card title="Tool search" icon="magnifying-glass" href="/docs/en/agents-and-tools/tool-use/tool-search-tool">
    Load tools on demand without breaking your cache.
  </Card>
  <Card title="Tool reference" icon="book" href="/docs/en/agents-and-tools/tool-use/tool-reference">
    Browse all available tools and their parameters.
  </Card>
</CardGroup>
