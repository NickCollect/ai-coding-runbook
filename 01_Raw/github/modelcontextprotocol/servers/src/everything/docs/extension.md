# Everything Server - Extension Points

**[Architecture](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/Architecture)
| [Project Structure](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/Project Structure)
| [Startup Process](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/Startup Process)
| [Server Features](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/Server Features)
| Extension Points
| [How It Works](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/everything/docs/How It Works)**

## Adding Tools

- Create a new file under `tools/` with your `registerXTool(server)` function that registers the tool via `server.registerTool(...)`.
- Export and call it from `tools/index.ts` inside `registerTools(server)`.

## Adding Prompts

- Create a new file under `prompts/` with your `registerXPrompt(server)` function that registers the prompt via `server.registerPrompt(...)`.
- Export and call it from `prompts/index.ts` inside `registerPrompts(server)`.

## Adding Resources

- Create a new file under `resources/` with your `registerXResources(server)` function using `server.registerResource(...)` (optionally with `ResourceTemplate`).
- Export and call it from `resources/index.ts` inside `registerResources(server)`.
