---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/2243-http-standardization.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/2243-http-standardization.md
title: "SEP-2243: HTTP header standardization for Streamable HTTP transport"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2026-02-04 | Author: MCP Transports Working Group**

Mirrors critical routing/context information from the JSON-RPC payload into standard HTTP headers so load balancers, proxies, observability tools, and WAFs can route MCP traffic without deep packet inspection.

**Standard headers** (required for compliance):

| Header | Source | Required for |
|---|---|---|
| `Mcp-Method` | `method` field | All requests and notifications |
| `Mcp-Name` | `params.name` or `params.uri` | `tools/call`, `resources/read`, `prompts/get` requests |

Header names are case-insensitive; values must match the body — servers MUST reject mismatches with HTTP 400 + JSON-RPC `-32001` (`HeaderMismatch`). Prevents components-of-truth divergence (load balancer routes on header, server executes on body).

**Custom headers from tool parameters** (`x-mcp-header` schema extension): tool authors can mark a parameter with `"x-mcp-header": "Region"` so the value gets mirrored into `Mcp-Param-Region`. Example: a Cloud Spanner `execute_sql` tool with `region` parameter — load balancer routes to Oregon vs Belgium cluster from the header without parsing JSON body. Multi-tenant SaaS uses `Mcp-Param-TenantId`. Priority-based handling uses `Mcp-Param-Priority`.

**Constraints on `x-mcp-header` values**: non-empty, ASCII only (excluding space/colon), case-insensitively unique within `inputSchema`, only for primitive types (number/string/boolean). Clients MUST reject tool definitions violating these.

**Value encoding**: per RFC 9110, header values must be visible ASCII + space + tab. Use **Base64 sentinel format** (`=?base64?{value}?=`) for unsafe values: leading/trailing whitespace, non-ASCII, control characters. Safe ASCII values stay readable. Prefix is case-insensitive.

**Server validation**: must validate header/body match; reject Base64 decode failures; reject invalid characters. Clients support `x-mcp-header` (mandatory); servers may optionally use it.

**Rationale highlights**: chose headers over path-based routing (backward compat — existing servers stay valid; framework neutrality; unlimited values; no URL length limits). Chose sentinel-wrapping over separate header name (avoids namespace doubling) over implicit-encoding (intermediaries can't tell without schema) over always-encode (defeats the readability purpose). Scope limited to tools because resources/prompts lack JSON Schema extensibility today (potential future extension).

Conformance test cases enumerated for case sensitivity, header/body mismatch, special characters, x-mcp-header conflicts, encoding edge cases, type restrictions, Base64 decoding, null/missing values.
