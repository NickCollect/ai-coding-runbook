---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/python/claude-api/tool-use.md
title: "Claude API — Tool Use (Python)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: [Tool-use, Agentic-loop]
---

Python tool-use reference for `claude-api` skill. Covers conceptual overview separately at `shared/tool-use-concepts.md`. Note: only first ~80 lines sampled.

**Tool runner (recommended)** — Beta in Python SDK. Use `@beta_tool` decorator on typed functions, pass them to `client.beta.messages.tool_runner()`:

```python
import anthropic
from anthropic import beta_tool

client = anthropic.Anthropic()

@beta_tool
def get_weather(location: str, unit: str = "celsius") -> str:
    """Get current weather for a location.

    Args:
        location: City and state, e.g., San Francisco, CA.
        unit: Temperature unit, either "celsius" or "fahrenheit".
    """
    return f"72°F and sunny in {location}"

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-7",
    max_tokens=16000,
    tools=[get_weather],
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
)

# Each iteration yields a BetaMessage; stops when Claude is done
for message in runner:
    print(message)
```

**Async**: use `@beta_async_tool` with `async def` functions.

**Tool runner benefits**: no manual loop (SDK handles tool-call → result → next-call), type-safe inputs via decorators, schemas auto-generated from function signatures, iteration auto-stops when Claude has no more tool calls.

**MCP tool conversion helpers** (Beta) via `pip install anthropic[mcp]` (Python 3.10+). `async_mcp_tool(t, mcp_client)` converts MCP tools to Anthropic types for use with tool runner. Use this for local MCP servers, prompts, resources, or more control over MCP connection. (Claude API also supports `mcp_servers` parameter for direct remote MCP connection.)

Example with `stdio_client(StdioServerParameters(command="mcp-server"))` + `ClientSession` to wire MCP tools into the tool runner. **Note**: `tool_runner` is sync (returns the runner, not a coroutine).

(Remainder: manual tool loop pattern, more MCP examples — not sampled.)
