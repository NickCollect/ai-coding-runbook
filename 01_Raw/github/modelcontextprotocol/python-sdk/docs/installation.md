# Installation

The Python SDK is available on PyPI as [`mcp`](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/`mcp`) so installation is as simple as:

=== "pip"

    ```bash
    pip install mcp
    ```
=== "uv"

    ```bash
    uv add mcp
    ```

The following dependencies are automatically installed:

- [`httpx`](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/`httpx`): HTTP client to handle HTTP Streamable and SSE transports.
- [`httpx-sse`](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/`httpx-sse`): HTTP client to handle SSE transport.
- [`pydantic`](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/`pydantic`): Types, JSON schema generation, data validation, and [more](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/more).
- [`starlette`](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/`starlette`): Web framework used to build the HTTP transport endpoints.
- [`python-multipart`](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/`python-multipart`): Handle HTTP body parsing.
- [`sse-starlette`](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/`sse-starlette`): Server-Sent Events for Starlette, used to build the SSE transport endpoint.
- [`pydantic-settings`](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/`pydantic-settings`): Settings management used in MCPServer.
- [`uvicorn`](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/`uvicorn`): ASGI server used to run the HTTP transport endpoints.
- [`jsonschema`](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/`jsonschema`): JSON schema validation.
- [`pywin32`](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/docs/`pywin32`): Windows specific dependencies for the CLI tools.

This package has the following optional groups:

- `cli`: Installs `typer` and `python-dotenv` for the MCP CLI tools.
