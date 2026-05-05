# MCP Python SDK

The **Model Context Protocol (MCP)** allows applications to provide context for LLMs in a standardized way, separating the concerns of providing context from the actual LLM interaction.

This Python SDK implements the full MCP specification, making it easy to:

- **Build MCP servers** that expose resources, prompts, and tools
- **Create MCP clients** that can connect to any MCP server
- **Use standard transports** like stdio, SSE, and Streamable HTTP

If you want to read more about the specification, please visit the [MCP documentation](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/MCP documentation).

## Quick Example

Here's a simple MCP server that exposes a tool, resource, and prompt:

```python title="server.py"
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Test Server", json_response=True)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    return f"Write a {style} greeting for someone named {name}."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

Run the server:

```bash
uv run --with mcp server.py
```

Then open the [MCP Inspector](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/MCP Inspector) and connect to `http://localhost:8000/mcp`:

```bash
npx -y @modelcontextprotocol/inspector
```

## Getting Started

<!-- TODO(Marcelo): automatically generate the follow references with a header on each of those files. -->
1. **[Install](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/Install)** the MCP SDK
2. **[Learn concepts](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/Learn concepts)** - understand the three primitives and architecture
3. **[Explore authorization](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/Explore authorization)** - add security to your servers
4. **[Use low-level APIs](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/Use low-level APIs)** - for advanced customization

## API Reference

Full API documentation is available in the [API Reference](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/API Reference).
