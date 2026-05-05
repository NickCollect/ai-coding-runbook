# Everything MCP Server
**[Architecture](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/Architecture)
| [Project Structure](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/Project Structure)
| [Startup Process](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/Startup Process)
| [Server Features](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/Server Features)
| [Extension Points](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/Extension Points)
| [How It Works](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/How It Works)**

This MCP server attempts to exercise all the features of the MCP protocol. It is not intended to be a useful server, but rather a test server for builders of MCP clients. It implements prompts, tools, resources, sampling, and more to showcase MCP capabilities.

## Tools, Resources, Prompts, and Other Features

A complete list of the registered MCP primitives and other protocol features demonstrated can be found in the [Server Features](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/Server Features) document.

## Usage with Claude Desktop (uses [stdio Transport](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/stdio Transport))

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "everything": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-everything"
      ]
    }
  }
}
```

On Windows, use `cmd /c` to launch `npx`:

```json
{
  "mcpServers": {
    "everything": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@modelcontextprotocol/server-everything"
      ]
    }
  }
}
```

## Usage with VS Code

For quick installation, use one of the one-click install buttons below...

[![Install with NPX in VS Code](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/![Install with NPX in VS Code)](https://insiders.vscode.dev/redirect/mcp/install?name=everything&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40modelcontextprotocol%2Fserver-everything%22%5D%7D) [![Install with NPX in VS Code Insiders](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/![Install with NPX in VS Code Insiders)](https://insiders.vscode.dev/redirect/mcp/install?name=everything&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40modelcontextprotocol%2Fserver-everything%22%5D%7D&quality=insiders)

[![Install with Docker in VS Code](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/![Install with Docker in VS Code)](https://insiders.vscode.dev/redirect/mcp/install?name=everything&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22mcp%2Feverything%22%5D%7D) [![Install with Docker in VS Code Insiders](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/![Install with Docker in VS Code Insiders)](https://insiders.vscode.dev/redirect/mcp/install?name=everything&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22mcp%2Feverything%22%5D%7D&quality=insiders)

For manual installation, you can configure the MCP server using one of these methods:

**Method 1: User Configuration (Recommended)**
Add the configuration to your user-level MCP configuration file. Open the Command Palette (`Ctrl + Shift + P`) and run `MCP: Open User Configuration`. This will open your user `mcp.json` file where you can add the server configuration.

**Method 2: Workspace Configuration**
Alternatively, you can add the configuration to a file called `.vscode/mcp.json` in your workspace. This will allow you to share the configuration with others.

> For more details about MCP configuration in VS Code, see the [official VS Code MCP documentation](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/official VS Code MCP documentation).

#### NPX

```json
{
  "servers": {
    "everything": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-everything"]
    }
  }
}
```

On Windows, use:

```json
{
  "servers": {
    "everything": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-everything"]
    }
  }
}
```

## Running from source with [HTTP+SSE Transport](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/HTTP+SSE Transport) (deprecated as of [2025-03-26](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/2025-03-26))

```shell
cd src/everything
npm install
npm run start:sse
```

## Run from source with [Streamable HTTP Transport](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/Streamable HTTP Transport)

```shell
cd src/everything
npm install
npm run start:streamableHttp
```

## Running as an installed package
### Install 
```shell
npm install -g @modelcontextprotocol/server-everything@latest
````

### Run the default (stdio) server
```shell
npx @modelcontextprotocol/server-everything
```

### Or specify stdio explicitly
```shell
npx @modelcontextprotocol/server-everything stdio
```

### Run the SSE server
```shell
npx @modelcontextprotocol/server-everything sse
```

### Run the streamable HTTP server
```shell
npx @modelcontextprotocol/server-everything streamableHttp
```
