---
source_url: https://cursor.com/docs/api/origin/mcp
fetched_at: 2026-10-05T06:27:18.971168+00:00
fetch_method: mintlify_md
---

# Origin MCP

Origin is in Early Beta and subject to change.

The Origin MCP server is currently available only in Cursor and [Grok Bot](https://cursor.com/docs/grok-bot.md). Support for other agent harnesses is coming soon.

The Origin MCP server gives agents access to repositories and pull requests hosted on Origin (`origin.cursor.com`). It covers repository browsing and search, commits and branches, pull request reads and writes, reviews and comments, labels, reviewers, and checks. Tools only see repositories hosted on Origin, addressed by their Origin namespace (`owner`) and repository `name`. A repository that mirrors to Origin counts as hosted there.

For every tool, its parameters, limits, and return fields, see the [tool reference](https://cursor.com/docs/api/origin/mcp/tools.md).

## Endpoints

| URL                                          | Tools listed                                                   |
| -------------------------------------------- | -------------------------------------------------------------- |
| `https://api.origin.cursor.com/mcp`          | Every tool the caller can use.                                 |
| `https://api.origin.cursor.com/mcp/readonly` | Read-only tools only. Tools that write are hidden and refused. |

Sending the header `x-mcp-readonly: true` to `/mcp` has the same effect as calling `/mcp/readonly`.

## Transport

The server speaks MCP over stateless streamable HTTP:

- Send each JSON-RPC message as an HTTP `POST` with `Content-Type: application/json`. Other methods get `405`, and other content types get `415`.
- Responses are plain JSON. The server doesn't open server-sent event streams or keep sessions, so every request is independent.
- The server supports the tools capability only: no resources, prompts, or sampling.
- Requests have a size limit and a deadline. An oversized request gets `413`.

## Authentication

Send a bearer token in the `Authorization` header. The server accepts:

- a Cursor user session, as used by Cursor's desktop app, CLI, and agents;
- an Origin App [installation access token](https://cursor.com/docs/api/origin/reference/installation-access-token.md) (`oit_…`);
- an Origin App's signed [app JWT](https://cursor.com/docs/api/origin/reference/app-jwt.md);
- an [installation user token](https://cursor.com/docs/api/origin/acting-as-users.md).

Tools act as the authenticated caller. Each call goes through the same permission checks and rate limits as the equivalent [Origin API](https://cursor.com/docs/api/origin.md) request, so a tool can only do what the caller could do through the API. The [tool reference](https://cursor.com/docs/api/origin/mcp/tools.md) lists the [scopes](https://cursor.com/docs/api/origin/reference/scopes.md) each tool needs. Scope-limited agent sessions don't see tools their scopes would always refuse.

Authentication failures return `401` (missing or invalid credentials), `403` (not allowed), or `503` (temporarily unable to check the credentials).

## Confirmation

Tools that are destructive or hard to undo, such as merging a pull request or dismissing a review, set `_meta["cursor/requiresConfirmation"]: true` in `tools/list`. Cursor clients show an approval prompt before every call to such a tool. Other MCP clients can use the same flag, or the standard `destructiveHint` annotation, to decide when to ask the user.

## Errors

A tool that fails returns a normal MCP tool result with `isError: true`. The text content is a readable message followed by a request ID. The structured content is:

```json
{
  "data": {
    "category": "not_found",
    "message": "…",
    "requestId": "6e0d261c-86a2-4383-89f0-9162c1c10662",
    "retryAfterSeconds": 30,
    "rateLimit": { "limit": "…", "remaining": "…", "reset": "…" }
  }
}
```

`category` is one of `not_found`, `forbidden`, `quota_exceeded`, `conflict`, `validation_error`, or `upstream_failure`. `retryAfterSeconds` and `rateLimit` appear only when the call was rate limited. Include the request ID when reporting a problem.

Unknown tools and invalid parameters return JSON-RPC errors instead of tool results.

## Pagination

List tools take `pageSize` and `pageToken` and return `nextPageToken`. Pass the returned `nextPageToken` as `pageToken` to read the next page; it's absent on the last page. Tools that filter a list, such as [`list_pull_requests`](https://cursor.com/docs/api/origin/mcp/tools.md#list_pull_requests), need the same filters on every page.


---

## Sitemap

[Origin API docs index](https://cursor.com/docs/api/origin/llms.txt)
