# Using tools

<!-- source: https://platform.openai.com/docs/guides/tools -->

When generating model responses or building agents, you can extend capabilities using built-in tools, function calling, tool search, and remote MCP servers.

Only `gpt-5.4` and later models support `tool_search`.

## Available tools

| Tool | Description |
|---|---|
| Function calling | Call custom code to give the model access to additional data and capabilities |
| Web search | Include data from the Internet in model response generation |
| Remote MCP | Give the model access to new capabilities via Model Context Protocol (MCP) servers |
| Skills | Upload and reuse versioned skill bundles in hosted shell environments |
| Shell | Run shell commands in hosted containers or in your own local runtime |
| Computer use | Create agentic workflows that enable a model to control a computer interface |
| Image generation | Generate or edit images using GPT Image |
| File search | Search the contents of uploaded files for context when generating a response |
| Tool search | Dynamically load relevant tools into the model's context to optimize token usage |

## Usage in the API

Enable tool access by specifying configurations in the `tools` parameter. The model automatically decides whether to use a configured tool based on the prompt.

You can explicitly control this behavior with the `tool_choice` parameter.

## Remote MCP example

```python
resp = client.responses.create(
    model="gpt-5.5",
    tools=[
        {
            "type": "mcp",
            "server_label": "dmcp",
            "server_description": "A Dungeons and Dragons MCP server.",
            "server_url": "https://dmcp-server.deno.dev/sse",
            "require_approval": "never",
        },
    ],
    input="Roll 2d4+1",
)
```

## Usage in the Agents SDK

In the Agents SDK, tools are wired into the agent definition:
- Attach hosted tools, function tools, or hosted MCP tools directly on the agent
- Expose a specialist as a tool when a manager should stay in control of the user-facing reply

```python
from agents import function_tool

@function_tool
def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    return f"The weather in {city} is sunny."
```

## Tool search

Tool search (`tool_search`) lets the model search for relevant tools, add them to the model context, and use them dynamically. This is useful when you have a large ecosystem of tools and want to avoid loading all of them upfront (which counts against the context window).

Only `gpt-5.4` and later models support tool search.
