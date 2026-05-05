---
type: summary
source: 01_Raw/github/anthropics/skills/skills/mcp-builder/reference/python_mcp_server.md
title: "mcp-builder skill: python_mcp_server reference"
summarized_at: 2026-05-05
entities_referenced: [Skill, MCP-server]
concepts_referenced: []
---

Python implementation guide inside the `mcp-builder` skill. Uses MCP Python SDK + FastMCP.

**Key imports**: `from mcp.server.fastmcp import FastMCP`, `from pydantic import BaseModel, Field, field_validator, ConfigDict`, `from typing import Optional, List, Dict, Any`, `from enum import Enum`, `import httpx`.

**Server init**: `mcp = FastMCP("service_mcp")`. Naming convention `{service}_mcp` (lowercase underscores). Examples: `github_mcp`, `jira_mcp`, `stripe_mcp`. General (not feature-tied), descriptive of service, no version numbers/dates.

**Tool registration**: `@mcp.tool(name="...", annotations={...})` decorator on async function taking Pydantic model as input. snake_case names with service context (`slack_send_message` not `send_message`).

**Pydantic v2 features**:
- `model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True, extra='forbid')`.
- `field_validator` (not deprecated `validator`); requires `@classmethod` decorator + type hints.
- `model_dump()` not deprecated `dict()`.

**Annotations**: `title`, `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`.

**Response format options**: support `markdown` (human-readable, headers/lists, human timestamps, "@john (U123456)" format, omit verbose metadata) AND `json` (complete structured data, all fields, consistent types) via `ResponseFormat` Enum.

**Pagination**: `limit` + `offset` Pydantic fields with constraints. Return `{total, count, offset, items, has_more, next_offset}`.

**Error handling**: `_handle_api_error(e)` helper returning consistent strings for `httpx.HTTPStatusError` (404, 403, 429, generic), `httpx.TimeoutException`, generic.

**Shared utilities**: `_make_api_request(endpoint, method, **kwargs)` with `httpx.AsyncClient` async context manager, 30s timeout, `raise_for_status`.

**Async/await everywhere** for I/O. Type hints throughout. Comprehensive docstrings with explicit type info, schema, examples, error handling.

**Advanced FastMCP features**:
- **Context injection**: `async def tool(query, ctx: Context)` — `ctx.report_progress(0.25, "...")`, `ctx.log_info/error/debug`, `ctx.elicit(prompt, input_type)`, `ctx.fastmcp.name`, `ctx.read_resource(uri)`.
- **Resource registration**: `@mcp.resource("file://documents/{name}")` with URI templates. Use Resources for simple-param data access; Tools for complex ops with validation/logic.
- **Structured output types**: TypedDict, dataclass, Pydantic models — FastMCP serializes automatically.
- **Lifespan management**: `@asynccontextmanager` `app_lifespan` setup/teardown. `mcp = FastMCP("...", lifespan=app_lifespan)`. Access via `ctx.request_context.lifespan_state["db"]`.
- **Transports**: `mcp.run()` (stdio default) or `mcp.run(transport="streamable_http", port=8000)`.

**Best practices**: extract common functionality (DRY), centralize error handling, type hints + Pydantic models, async context managers, group imports (stdlib/third-party/local), specific exceptions, UPPER_CASE module constants.

**Quality checklist** ~80 items grouped: strategic design, implementation quality, tool config (annotations + Pydantic + docstrings), advanced features, code quality, testing.
