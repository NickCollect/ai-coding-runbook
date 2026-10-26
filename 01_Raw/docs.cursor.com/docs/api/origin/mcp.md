---
source_url: https://cursor.com/docs/api/origin/mcp
fetched_at: 2026-10-26T05:39:59.171928+00:00
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

The server speaks MCP over stateless streamable HTTP and supports tools only. Send each JSON-RPC message as a `POST` with `Content-Type: application/json`, and expect plain JSON back, with no sessions or server-sent event streams.

## Permissions

Tool calls are attributed to you; from Grok Bot they show as "`<your name>` via Grok Bot". Your access and the client's [scopes](https://cursor.com/docs/api/origin/reference/scopes.md) both limit what a tool can do, under the same permission checks and rate limits as the equivalent [Origin API](https://cursor.com/docs/api/origin.md) request (see [Authentication](https://cursor.com/docs/api/origin/reference/authentication.md) and [Acting on behalf of users](https://cursor.com/docs/api/origin/acting-as-users.md)). Some write actions, such as approving a pull request, are available only in Grok Bot.

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

## Results

A tool that succeeds returns its data as JSON in the text content and again as the structured content. A tool that returns an image, such as `get_pull_request_attachment`, adds an `image` content block after the text, with the bytes base64-encoded and their `mimeType`; the JSON describes the image and says how it was delivered.

## Pull request attachments

Images and recordings pasted into a pull request description, review, or comment appear in `pull_request_read` as upload URLs on cursor.com. Those URLs need a signed-in browser, so an agent fetches one with `get_pull_request_attachment`, naming the pull request and the URL exactly as it was returned. The server fetches only the pull request page's own upload URLs, only when the URL appears in that pull request's text, and only for a caller who can read the pull request. Small images come back inline; larger images, recordings, and other files come back as a short-lived URL the agent can fetch without further credentials. The size limit is in the [tool reference](https://cursor.com/docs/api/origin/mcp/tools.md#get_pull_request_attachment).

## Pagination

List tools page like the Origin API: pass the returned `nextPageToken` as `pageToken`, with the same filters, to read the next page. See [Pagination](https://cursor.com/docs/api/origin/reference/pagination.md).


---

## Sitemap

[Origin API docs index](https://cursor.com/docs/api/origin/llms.txt)
