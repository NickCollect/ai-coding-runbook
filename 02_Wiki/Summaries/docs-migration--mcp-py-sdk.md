---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/docs/migration.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/docs/migration.md
title: "Python SDK v1 → v2 migration guide"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Comprehensive migration guide covering all breaking changes from v1 to v2 of the MCP Python SDK.

**Notable removals/replacements**:
- `streamablehttp_client` removed → use `streamable_http_client` (now returns 2-tuple `(read, write)`; takes `httpx.AsyncClient` for headers/timeout/auth/follow_redirects). `get_session_id` callback gone — use httpx event hooks if needed
- Type aliases removed: `Content` → `ContentBlock`; `ResourceReference` → `ResourceTemplateReference`; `Cursor` → use `str` directly; internal `MethodT`/`RequestParamsT`/`NotificationParamsT` removed
- **Field names: camelCase → snake_case** for Python attribute access (`isError` → `is_error`, `nextCursor` → `next_cursor`, `inputSchema` → `input_schema`, `mimeType` → `mime_type`, etc.). JSON wire format unchanged via Pydantic aliases. Constructor still accepts old names since `populate_by_name=True`.
- `ClientSessionGroup.call_tool()`: `args` → `arguments`
- `ClientSession` list methods (`list_resources`, `list_tools`, etc.): `cursor` parameter removed → use `params=PaginatedRequestParams(cursor=...)`
- `get_server_capabilities()` → `session.initialize_result` property (returns full `InitializeResult` with capabilities, server_info, instructions, protocol_version)
- `McpError` → `MCPError`; new constructor: `MCPError(code, message, data=None)` (no longer wraps `ErrorData`); `MCPError.from_error_data(...)` for conversion
- **`FastMCP` → `MCPServer`** (under `mcp.server.mcpserver` instead of `mcp.server.fastmcp`); all submodules moved correspondingly
- `mount_path` parameter removed (use ASGI `root_path` via Starlette `Mount`)
- Transport-specific parameters (`host`, `port`, `sse_path`, `message_path`, `streamable_http_path`, `json_response`, `stateless_http`, `event_store`, `retry_interval`, `transport_security`) moved from `MCPServer` constructor to `run()` / `sse_app()` / `streamable_http_app()` methods
- `MCPServer.get_context()` removed → use `ctx: Context` parameter injection
- `MCPServer.call_tool()`, `read_resource()`, `get_prompt()` accept optional `context: Context | None`
- `Context.log()/.info()/...`: `message` → `data` (any JSON-serializable); `extra` removed; now accepts all 8 RFC-5424 levels
- Union types (`ClientRequest`, `ServerRequest`, `ClientNotification`, `ServerNotification`, `ClientResult`, `ServerResult`, `JSONRPCMessage`) no longer `RootModel` subclasses → use `TypeAdapter` instances (e.g., `client_request_adapter.validate_python(data)`); no more `.root` access; no wrapper call when constructing
- `RequestParams.Meta` Pydantic model → `RequestParamsMeta` TypedDict (dict access via `.get("progress_token")`)
- `RequestContext` split into `ClientRequestContext` (in `mcp.client.context`) and `ServerRequestContext` (in `mcp.server.context`); type parameters reduced from 3 to 1; high-level `Context` similarly simplified
- `mcp.shared.progress` module removed (`ProgressContext`, `progress()` context manager) → use `Context.report_progress()` or `session.send_progress_notification()`
- `create_connected_server_and_client_session` → use `mcp.client.Client(server)` directly
- Resource URI: `AnyUrl` → `str` (allows relative paths like `users/me`)

**Lowlevel `Server` changes**:
- Constructor parameters after `name` are now keyword-only
- Type parameter reduced from 2 to 1 (`Server[LifespanResultT]`)
- `request_handlers` and `notification_handlers` dicts removed
- Decorator-based handler registration (`@server.list_tools()`, `@server.call_tool()`, etc.) replaced with constructor `on_*` kwargs (`on_list_tools=..., on_call_tool=...`). Handlers receive `(ctx: ServerRequestContext, params)` and return full result types — no more bare-list / dict / shorthand auto-wrapping. Full handler-mapping table provided in the doc.
- Auto return-value wrapping removed (`call_tool` no longer wraps dict→`structured_content`+JSON `TextContent`; `read_resource` no longer wraps `Iterable[ReadResourceContents]`; `list_tools`/`list_resources`/`list_prompts` no longer wrap bare lists)
- `request_context` property and `request_ctx` contextvar removed — context passed to handlers as first arg
- Experimental task handler decorators removed → pass via `enable_tasks(on_get_task=..., ...)`

**Bug fixes**: `subscribe` capability now correctly reported when `on_subscribe_resource` registered. Top-level MCP types no longer accept arbitrary extra fields (matches spec — extras allowed only in `_meta`).

**New features**: `streamable_http_app()` available directly on lowlevel `Server` (not just `MCPServer`); lowlevel `Server.session_manager` property exposed.
