# Everything Server – Architecture

**Architecture
| [Project Structure](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/Project Structure)
| [Startup Process](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/Startup Process)
| [Server Features](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/Server Features)
| [Extension Points](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/Extension Points)
| [How It Works](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/How It Works)**

This documentation summarizes the current layout and runtime architecture of the `src/everything` package.
It explains how the server starts, how transports are wired, where tools, prompts, and resources are registered, and how to extend the system.

## High‑level Overview

### Purpose

A minimal, modular MCP server showcasing core Model Context Protocol features. It exposes simple tools, prompts, and resources, and can be run over multiple transports (STDIO, SSE, and Streamable HTTP).

### Design

A small “server factory” constructs the MCP server and registers features.
Transports are separate entry points that create/connect the server and handle network concerns.
Tools, prompts, and resources are organized in their own submodules.

### Multi‑client

The server supports multiple concurrent clients. Tracking per session data is demonstrated with
resource subscriptions and simulated logging.

## Build and Distribution

- TypeScript sources are compiled into `dist/` via `npm run build`.
- The `build` script copies `docs/` into `dist/` so instruction files ship alongside the compiled server.
- The CLI bin is configured in `package.json` as `mcp-server-everything` → `dist/index.js`.

## [Project Structure](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/Project Structure)

## [Startup Process](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/Startup Process)

## [Server Features](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/Server Features)

## [Extension Points](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/Extension Points)

## [How It Works](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/How It Works)
