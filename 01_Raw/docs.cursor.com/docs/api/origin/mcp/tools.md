---
source_url: https://cursor.com/docs/api/origin/mcp/tools
fetched_at: 2026-10-05T06:27:18.999429+00:00
fetch_method: mintlify_md
---

# Origin MCP tool reference

Every tool the Origin MCP server at `https://api.origin.cursor.com/mcp` lists, in listing order. Parameters are the JSON Schema clients receive from `tools/list`.

| Tool                                                                                                                       | Access                          | Summary                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`get_repository`](https://cursor.com/docs/api/origin/mcp/tools.md#get_repository)                                         | Read-only                       | Get one Origin repository by owner and name, including default branch and mirror state.                                                                                                                    |
| [`list_repositories`](https://cursor.com/docs/api/origin/mcp/tools.md#list_repositories)                                   | Read-only                       | List Origin repositories belonging to an owner slug.                                                                                                                                                       |
| [`list_namespaces`](https://cursor.com/docs/api/origin/mcp/tools.md#list_namespaces)                                       | Read-only                       | List the Origin namespaces (owner slugs) the caller can list repositories in, ordered by slug.                                                                                                             |
| [`create_repository`](https://cursor.com/docs/api/origin/mcp/tools.md#create_repository)                                   | Writes                          | Create an empty Origin-hosted repository.                                                                                                                                                                  |
| [`get_file_contents`](https://cursor.com/docs/api/origin/mcp/tools.md#get_file_contents)                                   | Read-only                       | Read one path at a ref in an Origin-hosted repository.                                                                                                                                                     |
| [`get_git_tree`](https://cursor.com/docs/api/origin/mcp/tools.md#get_git_tree)                                             | Read-only                       | List a git tree in an Origin-hosted repository at a tree SHA, commit SHA, branch, tag, or HEAD: immediate children by default, or the full walk with recursive true.                                       |
| [`grep_contents`](https://cursor.com/docs/api/origin/mcp/tools.md#grep_contents)                                           | Read-only                       | Search file contents across one Origin-hosted repository at a ref, which defaults to the default branch.                                                                                                   |
| [`list_branches`](https://cursor.com/docs/api/origin/mcp/tools.md#list_branches)                                           | Read-only                       | List branch names and tip commit SHAs for an Origin-hosted repository.                                                                                                                                     |
| [`list_commits`](https://cursor.com/docs/api/origin/mcp/tools.md#list_commits)                                             | Read-only                       | List commits from a branch or starting ref in an Origin-hosted repository, optionally filtered by lists of exact git author or committer emails and by inclusive since and until bounds on committer time. |
| [`commit_read`](https://cursor.com/docs/api/origin/mcp/tools.md#commit_read)                                               | Read-only                       | Read one commit in an Origin-hosted repository.                                                                                                                                                            |
| [`compare_commits`](https://cursor.com/docs/api/origin/mcp/tools.md#compare_commits)                                       | Read-only                       | Compare two refs of an Origin-hosted repository relative to their merge base.                                                                                                                              |
| [`list_pull_requests`](https://cursor.com/docs/api/origin/mcp/tools.md#list_pull_requests)                                 | Read-only                       | List pull requests in an Origin-hosted repository, filtered by state, head, author, base, or stackId and sorted by creation or update time in either direction.                                            |
| [`pull_request_read`](https://cursor.com/docs/api/origin/mcp/tools.md#pull_request_read)                                   | Read-only                       | Read one Origin-hosted pull request through a single view: summary, files, commits, reviews, comments, or threads.                                                                                         |
| [`create_pull_request`](https://cursor.com/docs/api/origin/mcp/tools.md#create_pull_request)                               | Writes                          | Create a pull request from an already-pushed branch.                                                                                                                                                       |
| [`update_pull_request`](https://cursor.com/docs/api/origin/mcp/tools.md#update_pull_request)                               | Writes                          | Update a pull request's title, description, and lifecycle through the public fields.                                                                                                                       |
| [`update_pull_request_base`](https://cursor.com/docs/api/origin/mcp/tools.md#update_pull_request_base)                     | Writes                          | Retarget a pull request's base branch, stack it on another pull request, or move it off its stack.                                                                                                         |
| [`merge_pull_request`](https://cursor.com/docs/api/origin/mcp/tools.md#merge_pull_request)                                 | Destructive                     | Merge a pull request or its root-to-target stack prefix.                                                                                                                                                   |
| [`create_pull_request_review`](https://cursor.com/docs/api/origin/mcp/tools.md#create_pull_request_review)                 | Writes content other people see | Submit a comment, approval, or request-changes review on a pull request.                                                                                                                                   |
| [`update_pull_request_review`](https://cursor.com/docs/api/origin/mcp/tools.md#update_pull_request_review)                 | Writes content other people see | Correct the body of an existing pull request review.                                                                                                                                                       |
| [`dismiss_pull_request_review`](https://cursor.com/docs/api/origin/mcp/tools.md#dismiss_pull_request_review)               | Destructive                     | Dismiss a submitted approve or request-changes review.                                                                                                                                                     |
| [`create_pull_request_comment`](https://cursor.com/docs/api/origin/mcp/tools.md#create_pull_request_comment)               | Writes content other people see | Create a general discussion comment on a pull request.                                                                                                                                                     |
| [`create_pull_request_inline_comment`](https://cursor.com/docs/api/origin/mcp/tools.md#create_pull_request_inline_comment) | Writes content other people see | Create a file-level, single-line, or line-range inline comment, optionally against a specific pull request version.                                                                                        |
| [`reply_pull_request_review_thread`](https://cursor.com/docs/api/origin/mcp/tools.md#reply_pull_request_review_thread)     | Writes content other people see | Reply to an existing review thread by thread ID.                                                                                                                                                           |
| [`update_pull_request_review_thread`](https://cursor.com/docs/api/origin/mcp/tools.md#update_pull_request_review_thread)   | Writes content other people see | Resolve or reopen a review thread by thread ID.                                                                                                                                                            |
| [`update_pull_request_comment`](https://cursor.com/docs/api/origin/mcp/tools.md#update_pull_request_comment)               | Writes content other people see | Correct an existing pull request comment body.                                                                                                                                                             |
| [`update_pull_request_labels`](https://cursor.com/docs/api/origin/mcp/tools.md#update_pull_request_labels)                 | Writes                          | Replace every label on a pull request with the provided names.                                                                                                                                             |
| [`create_label`](https://cursor.com/docs/api/origin/mcp/tools.md#create_label)                                             | Writes                          | Create a repository label so update\_pull\_request\_labels can apply it.                                                                                                                                   |
| [`request_pull_request_reviewers`](https://cursor.com/docs/api/origin/mcp/tools.md#request_pull_request_reviewers)         | Writes content other people see | Request reviewers (users and/or groups) on a pull request.                                                                                                                                                 |
| [`remove_pull_request_reviewers`](https://cursor.com/docs/api/origin/mcp/tools.md#remove_pull_request_reviewers)           | Writes content other people see | Remove requested reviewers from a pull request.                                                                                                                                                            |
| [`checks_read`](https://cursor.com/docs/api/origin/mcp/tools.md#checks_read)                                               | Read-only                       | Read checks for one target in an Origin-hosted repository: a pull request, commit, suite, or run.                                                                                                          |

## `get_repository`

Get one Origin repository by owner and name, including default branch and mirror state.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:metadata:read`

### Parameters

| Name    | Type   | Required | Description                                                                                                                                                                       |
| ------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner` | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`  | string | Yes      | Origin repository name within that namespace                                                                                                                                      |

### Returns

`id`, `owner`, `name`, `fullName`, `defaultBranch`, `cloneUrl`, `mirror`

## `list_repositories`

List Origin repositories belonging to an owner slug.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `namespace:repositories:read`

### Parameters

| Name        | Type   | Required | Description                                                                                                                                                                       |
| ----------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `pageSize`  | number | No       |                                                                                                                                                                                   |
| `pageToken` | string | No       |                                                                                                                                                                                   |
| `filter`    | string | No       | Case-insensitive repository name substring                                                                                                                                        |

### Limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.

### Returns

`repositories` (paged), `nextPageToken`

## `list_namespaces`

List the Origin namespaces (owner slugs) the caller can list repositories in, ordered by slug. Each slug is a valid owner for list\_repositories; viewerCanCreateRepositories reports whether creating a repository there would be allowed. An empty list means the caller has no Origin repositories to read; repositories on GitHub or other hosts are not reachable through these tools.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `namespace:repositories:read`

### Parameters

| Name        | Type   | Required | Description |
| ----------- | ------ | -------- | ----------- |
| `pageSize`  | number | No       |             |
| `pageToken` | string | No       |             |

### Limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.

### Returns

`namespaces` (paged), `nextPageToken`

## `create_repository`

Create an empty Origin-hosted repository. Pick an owner from list\_namespaces where viewerCanCreateRepositories is true; omit owner to use the caller's personal namespace, which Origin claims on first use (needs an eligible plan, a Privacy Mode that allows code storage, and no team membership; team members pass their team slug). Both steps are one approval: confirm with the user before calling. defaultBranch defaults to main. Repository names are unique per owner, so retrying after a success fails with a conflict; read the repository with get\_repository instead. Returns the created repository, including cloneUrl.

- **Access:** Writes
- **Asks for confirmation:** Yes
- **On the read-only endpoint:** No
- **Required scopes:** `namespace:repositories:create`

### Parameters

| Name            | Type   | Required | Description                                                                                                                                                                       |
| --------------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`         | string | No       | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`          | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `defaultBranch` | string | No       | Default branch name. Omit for main.                                                                                                                                               |

### Returns

`id`, `owner`, `name`, `fullName`, `defaultBranch`, `cloneUrl`

## `get_file_contents`

Read one path at a ref in an Origin-hosted repository. Files larger than the byte cap are truncated. A directory returns type dir and its immediate children as entries (name, path, type, sha, and size for files) instead of content; entries past the cap are dropped and truncated is set.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:contents:read`

### Parameters

| Name        | Type   | Required | Description                                                                                                                                                                       |
| ----------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`      | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `path`      | string | Yes      |                                                                                                                                                                                   |
| `ref`       | string | No       |                                                                                                                                                                                   |
| `startLine` | number | No       |                                                                                                                                                                                   |
| `endLine`   | number | No       |                                                                                                                                                                                   |

### Limits

- `content` is truncated after 256 KiB.
- A line range covers at most 500 lines.

### Returns

`files` (at most 1), `path`, `content`, `encoding`, `sha`, `truncated`, `type`, `entries` (at most 1000), `name`, `size`

## `get_git_tree`

List a git tree in an Origin-hosted repository at a tree SHA, commit SHA, branch, tag, or HEAD: immediate children by default, or the full walk with recursive true. Each entry is path, mode, type (blob, tree, or commit), sha, and size for blobs. Entries past the cap are dropped and truncated is set; list subtrees non-recursively to see more. get\_file\_contents reads one blob.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:contents:read`

### Parameters

| Name        | Type    | Required | Description                                                                                                                                                                       |
| ----------- | ------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string  | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`      | string  | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `sha`       | string  | Yes      | Tree SHA, commit SHA, branch, tag, or HEAD                                                                                                                                        |
| `recursive` | boolean | No       | True walks the whole tree; omit for immediate children only                                                                                                                       |

### Returns

`sha`, `entries` (at most 1000), `path`, `mode`, `type`, `size`, `truncated`

## `grep_contents`

Search file contents across one Origin-hosted repository at a ref, which defaults to the default branch. The query is a regular expression matched case-sensitively; set literal for exact text, or caseInsensitive to ignore case (regex mode prefixes (?i) for GrepContents). wholeWord applies only with literal; for regex use \b. Returns matching lines plus any requested context lines, capped at 1000 matching occurrences, and sets limitHit when that cap is reached. Each returned line contains its full text, so the occurrence cap does not bound response bytes. There is no pagination. Narrow query, filterPath, includes, or excludes to reach other matches.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:contents:read`

### Parameters

| Name              | Type      | Required | Description                                                                                                                                                                                              |
| ----------------- | --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`           | string    | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it.                        |
| `name`            | string    | Yes      | Origin repository name within that namespace                                                                                                                                                             |
| `query`           | string    | Yes      | Regular expression matched case-sensitively by default. Set literal for exact text, or caseInsensitive to ignore case (regex mode prefixes (?i)). wholeWord applies only with literal; for regex use \b. |
| `ref`             | string    | No       | Branch, tag, or commit to search                                                                                                                                                                         |
| `literal`         | boolean   | No       | Match query as exact text                                                                                                                                                                                |
| `caseInsensitive` | boolean   | No       | Ignore case when matching; regex mode prefixes the query with (?i) for GrepContents, and that prefix counts toward the query UTF-8 cap                                                                   |
| `wholeWord`       | boolean   | No       | Match whole words only; only applied when literal is true. For regex, use \b instead.                                                                                                                    |
| `contextBefore`   | number    | No       | Context lines before each match, at most 10                                                                                                                                                              |
| `contextAfter`    | number    | No       | Context lines after each match, at most 10                                                                                                                                                               |
| `filterPath`      | string    | No       | File or directory to search, relative to the repo root                                                                                                                                                   |
| `includes`        | string\[] | No       | Globs naming the only paths to search                                                                                                                                                                    |
| `excludes`        | string\[] | No       | Globs naming paths to leave out; an exclude beats an include                                                                                                                                             |
| `maxResults`      | number    | No       | Matching occurrences to return, at most 1000. Zero uses the default of 1000                                                                                                                              |

### Limits

- `query` must be set.
- `query` is at most 4 KiB of UTF-8.
- `filterPath` is at most 4 KiB of UTF-8.
- `includes` takes at most 20 items.
- `excludes` takes at most 20 items.
- `includes` is at most 4 KiB of UTF-8.
- `excludes` is at most 4 KiB of UTF-8.
- `maxResults` is clamped to at most 1000.
- `contextBefore` is clamped to at most 10.
- `contextAfter` is clamped to at most 10.

### Returns

`matches` (at most 21000), `path`, `lineNumber`, `line`, `kind`, `submatches` (at most 1000), `limitHit`

## `list_branches`

List branch names and tip commit SHAs for an Origin-hosted repository. Optional prefix filters each page after pagination.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:contents:read`

### Parameters

| Name        | Type   | Required | Description                                                                                                                                                                       |
| ----------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`      | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `pageSize`  | number | No       |                                                                                                                                                                                   |
| `pageToken` | string | No       |                                                                                                                                                                                   |
| `prefix`    | string | No       | Case-sensitive branch name prefix. Applied per page after pagination; keep following nextPageToken even when a page has no matches.                                               |

### Limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.

### Returns

`branches` (paged), `nextPageToken`

## `list_commits`

List commits from a branch or starting ref in an Origin-hosted repository, optionally filtered by lists of exact git author or committer emails and by inclusive since and until bounds on committer time. A commit matches a list when its email equals any listed email, and must match every list and bound that is given. Email and time filters share one scan of at most 1000 commits per page, so a filtered page can be short or empty while nextPageToken is present. Keep paging to reach older matches. Each item is sha, full message, author, committer, parents, and tree. Omits patches. Continuation calls reuse the filters stored in pageToken.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:contents:read`

### Parameters

| Name              | Type      | Required | Description                                                                                                                                                                                                                   |
| ----------------- | --------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`           | string    | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it.                                             |
| `name`            | string    | Yes      | Origin repository name within that namespace                                                                                                                                                                                  |
| `ref`             | string    | No       | Branch or starting commit                                                                                                                                                                                                     |
| `authorEmails`    | string\[] | No       | Only commits whose git author email equals any listed email, case-insensitive. Not names or partial matches. At most 100 distinct emails.                                                                                     |
| `committerEmails` | string\[] | No       | Only commits whose git committer email equals any listed email, case-insensitive. At most 100 distinct emails. Combined with authorEmails, a commit must match both lists.                                                    |
| `since`           | string    | No       | Only commits whose git committer time is at or after this RFC 3339 timestamp, such as 2026-08-01T00:00:00Z. The bound is inclusive and uses committer time, which a rebase or cherry-pick rewrites, not author time.          |
| `until`           | string    | No       | Only commits whose git committer time is at or before this RFC 3339 timestamp, such as 2026-08-31T23:59:59Z. The bound is inclusive. Combined with since and the email filters, a commit must match every filter that is set. |
| `pageSize`        | number    | No       |                                                                                                                                                                                                                               |
| `pageToken`       | string    | No       |                                                                                                                                                                                                                               |

### Limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.
- `authorEmails` takes at most 100 items.
- `committerEmails` takes at most 100 items.

### Returns

`commits` (paged), `nextPageToken`

## `commit_read`

Read one commit in an Origin-hosted repository. Choose a single view: metadata, files, or a bounded patch.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:contents:read`

### Parameters

| Name        | Type   | Required | Description                                                                                                                                                                       |
| ----------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`      | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `sha`       | string | Yes      |                                                                                                                                                                                   |
| `view`      | string | Yes      |                                                                                                                                                                                   |
| `pageSize`  | number | No       |                                                                                                                                                                                   |
| `pageToken` | string | No       |                                                                                                                                                                                   |
| `startLine` | number | No       |                                                                                                                                                                                   |
| `endLine`   | number | No       |                                                                                                                                                                                   |

### Limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.
- `view` is one of `metadata`, `files`, `patch`.
- Long `patch` output is returned in chunks.
- A line range covers at most 500 lines.

### Returns

Set `view` to choose what comes back:

- `metadata`: `sha`, `message`, `author`, `committer`, `stats`, `parents`
- `files`: `files` (paged), `path`, `status`, `additions`, `deletions`, `changes`, `previousFilename`
- `patch`: `patch` (chunked), `truncated`

## `compare_commits`

Compare two refs of an Origin-hosted repository relative to their merge base.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:contents:read`

### Parameters

| Name    | Type   | Required | Description                                                                                                                                                                       |
| ------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner` | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`  | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `base`  | string | Yes      | Ref the comparison starts from                                                                                                                                                    |
| `head`  | string | Yes      | Ref compared against the base                                                                                                                                                     |

### Returns

`mergeBase`, `aheadBy`, `behindBy`, `status`

## `list_pull_requests`

List pull requests in an Origin-hosted repository, filtered by state, head, author, base, or stackId and sorted by creation or update time in either direction. Items are compact summaries (author, timestamps, merged/closedAt/mergedAt, and stack membership when the pull request is stacked); they omit body and diff stats—use pull\_request\_read for those. With stackId, the items are that stack's members in the requested sort order, not stack order; rebuild the tree from each member's stack.parent, and pass state all because the default open state leaves merged members out. Continuation calls must resend those filters with pageToken.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:pull_requests:read`

### Parameters

| Name        | Type   | Required | Description                                                                                                                                                                                                                          |
| ----------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `owner`     | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it.                                                    |
| `name`      | string | Yes      | Origin repository name within that namespace                                                                                                                                                                                         |
| `state`     | string | No       | open (default), closed, or all                                                                                                                                                                                                       |
| `head`      | string | No       | Head branch                                                                                                                                                                                                                          |
| `author`    | string | No       | Actor id (user\_…, app\_…, or sa\_…)                                                                                                                                                                                                 |
| `base`      | string | No       | Base branch, short name or refs/heads/…                                                                                                                                                                                              |
| `stackId`   | string | No       | Stack id (stk\_…) from stack.id on a pull request. Lists only that stack's members, in the requested sort order rather than stack order; rebuild the tree from each member's stack.parent. Pass state all to include merged members. |
| `direction` | string | No       | desc (default) or asc                                                                                                                                                                                                                |
| `sortBy`    | string | No       | created (default) or updated                                                                                                                                                                                                         |
| `pageSize`  | number | No       |                                                                                                                                                                                                                                      |
| `pageToken` | string | No       |                                                                                                                                                                                                                                      |

### Limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.
- `state` is one of `open`, `closed`, `all`.
- `direction` is one of `desc`, `asc`.
- `sortBy` is one of `created`, `updated`.

### Returns

`pullRequests` (paged), `nextPageToken`

## `pull_request_read`

Read one Origin-hosted pull request through a single view: summary, files, commits, reviews, comments, or threads. Summary includes labels, requested reviewers, and stack membership (stack id and parent pull request) when the pull request is stacked. The threads view requires threadIds and pages comments in those threads.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:pull_requests:read`, `repository:pull_requests:reviews:read`

### Parameters

| Name        | Type      | Required | Description                                                                                                                                                                       |
| ----------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string    | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`      | string    | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number`    | number    | Yes      |                                                                                                                                                                                   |
| `view`      | string    | Yes      |                                                                                                                                                                                   |
| `pageSize`  | number    | No       |                                                                                                                                                                                   |
| `pageToken` | string    | No       |                                                                                                                                                                                   |
| `startLine` | number    | No       |                                                                                                                                                                                   |
| `endLine`   | number    | No       |                                                                                                                                                                                   |
| `threadIds` | string\[] | No       | Thread ids for the threads view                                                                                                                                                   |

### Limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.
- `view` is one of `summary`, `files`, `commits`, `reviews`, `comments`, `stack`, `threads`.
- `threadIds` takes at most 20 items.
- Long `patch` output is returned in chunks.
- A line range covers at most 500 lines.

### Returns

Set `view` to choose what comes back:

- `summary`: `number`, `title`, `state`, `draft`, `merged`, `author`, `base`, `head`, `createdAt`, `updatedAt`, `closedAt`, `mergedAt`, `body`, `additions`, `deletions`, `changedFiles`, `stack`, `labels` (at most 100), `requestedReviewers` (at most 100)
- `files`: `files` (paged), `path`, `status`, `additions`, `deletions`, `changes`, `patch` (chunked), `truncated`
- `commits`: `commits` (paged)
- `reviews`: `reviews` (paged), `id`, `body`, `verdict`, `author`, `submittedAt`
- `comments`: `comments` (paged), `id`, `body`, `threadId`, `author`, `createdAt`, `updatedAt`
- `stack` (not yet public): `parent`, `children` (paged), `mergePrefix`, `convergence`
- `threads`: `threads` (paged)

## `create_pull_request`

Create a pull request from an already-pushed branch. To stack it, pass parentPullNumber: the base becomes that pull request's head branch (any other base is rejected), and head must have been built on that branch, meaning the two share a commit beyond the parent's own base. A head built off trunk or from unrelated history is rejected with the rebase to run. A head that has since fallen behind the parent is accepted and the response carries needsRestack, because the pull request cannot land until it is restacked; this tool never restacks. stackParent is the stored parent's number, read back after the create.

- **Access:** Writes
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:write`

### Parameters

| Name               | Type    | Required | Description                                                                                                                                                                       |
| ------------------ | ------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`            | string  | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`             | string  | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `title`            | string  | Yes      |                                                                                                                                                                                   |
| `head`             | string  | Yes      | Already-pushed source branch                                                                                                                                                      |
| `base`             | string  | No       | Target branch the pull request merges into. Required without parentPullNumber; with it, omit this or name the parent's head branch.                                               |
| `body`             | string  | No       |                                                                                                                                                                                   |
| `draft`            | boolean | No       |                                                                                                                                                                                   |
| `parentPullNumber` | number  | No       | Pull request to stack on, by number. Its head branch becomes the base, and head must have been built on that branch.                                                              |

### Returns

`number`, `title`, `state`, `draft`, `head`, `base`, `stackParent`, `needsRestack`

## `update_pull_request`

Update a pull request's title, description, and lifecycle through the public fields. Omit title or body to leave that field unchanged; pass an empty body to clear the description. Lifecycle is state (open or closed) plus draft, sent independently: state closed closes and ignores draft; state open reopens, and without draft true marks ready and publishes an existing draft; draft true reopens as a draft, alone or together with state open; draft false marks ready and reopens a closed pull request. Send one lifecycle field, both, or neither, so a metadata-only update is valid. Metadata and lifecycle together send one public UpdatePullRequest. Origin applies present fields in its documented order; a failure can leave some fields applied, so re-read after an error. merged is not writable, and ready is draft false or state open rather than a state value.

- **Access:** Writes
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:write`

### Parameters

| Name     | Type               | Required | Description                                                                                                                                                                       |
| -------- | ------------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`  | string             | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`   | string             | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number` | number             | Yes      |                                                                                                                                                                                   |
| `title`  | string             | No       | New title. Omit to leave unchanged.                                                                                                                                               |
| `body`   | string             | No       | New description. Omit to leave unchanged. Pass "" to clear.                                                                                                                       |
| `state`  | "open" \| "closed" | No       | open or closed. Omit to leave unchanged.                                                                                                                                          |
| `draft`  | boolean            | No       | Draft flag. Omit to leave unchanged.                                                                                                                                              |

### Limits

- `state` is one of `open`, `closed`.

### Returns

`number`, `title`, `body`, `state`, `draft`

## `update_pull_request_base`

Retarget a pull request's base branch, stack it on another pull request, or move it off its stack. With parentPullNumber, the base becomes that pull request's head branch and the stack parent is set in the same update. With base, the pull request is retargeted to that branch: the head branch of an open pull request makes that pull request the parent, and the default branch or a branch with no open pull request moves it off its stack. Stacking is allowed only when this pull request's branch was built on the parent, meaning the two share a commit beyond the parent's own base; a branch built off trunk or from unrelated history is rejected with the rebase to run. A branch that has fallen behind the parent is accepted and the response carries needsRestack, because the pull request cannot land until it is restacked. This tool stacks and unstacks but never restacks: no commit is rebased or replayed. Returns the stored base and head refs, plus stackParent when stacked.

- **Access:** Writes
- **Asks for confirmation:** Yes
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:write`

### Parameters

| Name               | Type   | Required | Description                                                                                                                                                                       |
| ------------------ | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`            | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`             | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number`           | number | Yes      |                                                                                                                                                                                   |
| `base`             | string | No       | Branch to retarget onto. The default branch or a branch with no open pull request unstacks; the head branch of an open pull request stacks on it. Send this or parentPullNumber.  |
| `parentPullNumber` | number | No       | Pull request to stack on, by number. Its head branch becomes the base. Send this or base.                                                                                         |

### Returns

`number`, `base`, `head`, `stackParent`, `needsRestack`

## `merge_pull_request`

Merge a pull request or its root-to-target stack prefix. Requires the expected head SHA. Optional mergeMethod (merge or squash); omit for the repository's default. skippedDescendants is currently always empty; descendants above a mid-stack merge target remain open.

- **Access:** Destructive
- **Asks for confirmation:** Yes
- **On the read-only endpoint:** No
- **Required scopes:** `repository:contents:write`

### Parameters

| Name              | Type                | Required | Description                                                                                                                                                                       |
| ----------------- | ------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`           | string              | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`            | string              | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number`          | number              | Yes      |                                                                                                                                                                                   |
| `expectedHeadSha` | string              | Yes      |                                                                                                                                                                                   |
| `mergeMethod`     | "merge" \| "squash" | No       | merge or squash. Omit for the repository default.                                                                                                                                 |

### Limits

- `expectedHeadSha` must be set.
- `mergeMethod` is one of `merge`, `squash`.

### Returns

`mergeCommitSha`, `mergedPrefix` (at most 200), `skippedDescendants` (at most 100)

## `create_pull_request_review`

Submit a comment, approval, or request-changes review on a pull request. Inline review comments are unsupported.

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### Parameters

| Name     | Type   | Required | Description                                                                                                                                                                       |
| -------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`  | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`   | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number` | number | Yes      |                                                                                                                                                                                   |
| `event`  | string | Yes      | COMMENT, APPROVE, or REQUEST\_CHANGES                                                                                                                                             |
| `body`   | string | No       |                                                                                                                                                                                   |

### Limits

- `event` is one of `COMMENT`, `APPROVE`, `REQUEST_CHANGES`.

### Returns

`id`, `state`, `body`

## `update_pull_request_review`

Correct the body of an existing pull request review.

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### Parameters

| Name       | Type   | Required | Description                                                                                                                                                                       |
| ---------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`    | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`     | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number`   | number | Yes      |                                                                                                                                                                                   |
| `reviewId` | string | Yes      |                                                                                                                                                                                   |
| `body`     | string | Yes      |                                                                                                                                                                                   |

### Returns

`id`, `state`, `body`

## `dismiss_pull_request_review`

Dismiss a submitted approve or request-changes review.

- **Access:** Destructive
- **Asks for confirmation:** Yes
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### Parameters

| Name       | Type   | Required | Description                                                                                                                                                                       |
| ---------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`    | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`     | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number`   | number | Yes      |                                                                                                                                                                                   |
| `reviewId` | string | Yes      |                                                                                                                                                                                   |
| `message`  | string | Yes      | Reason recorded with the dismissal                                                                                                                                                |

### Returns

`id`, `state`, `dismissal`

## `create_pull_request_comment`

Create a general discussion comment on a pull request.

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### Parameters

| Name     | Type   | Required | Description                                                                                                                                                                       |
| -------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`  | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`   | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number` | number | Yes      |                                                                                                                                                                                   |
| `body`   | string | Yes      |                                                                                                                                                                                   |

### Returns

`id`, `body`

## `create_pull_request_inline_comment`

Create a file-level, single-line, or line-range inline comment, optionally against a specific pull request version.

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### Parameters

| Name               | Type   | Required | Description                                                                                                                                                                       |
| ------------------ | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`            | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`             | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number`           | number | Yes      |                                                                                                                                                                                   |
| `body`             | string | Yes      |                                                                                                                                                                                   |
| `anchor`           | object | Yes      |                                                                                                                                                                                   |
| `anchor.kind`      | string | Yes      | file, line, or range                                                                                                                                                              |
| `anchor.path`      | string | Yes      | Diff path. Deleted path for deletions; head path otherwise                                                                                                                        |
| `anchor.side`      | string | No       | left or right. Required for line and range; omit for file                                                                                                                         |
| `anchor.startLine` | number | No       | 1-based first line. Required for line and range                                                                                                                                   |
| `anchor.endLine`   | number | No       | Inclusive last line. Required for range; omit otherwise                                                                                                                           |
| `versionNumber`    | number | No       | Pull request version. Omit or 0 for latest                                                                                                                                        |

### Limits

- A line range covers at most 500 lines.

### Returns

`threadId`, `id`, `path`, `line`, `body`

## `reply_pull_request_review_thread`

Reply to an existing review thread by thread ID.

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### Parameters

| Name       | Type   | Required | Description                                                                                                                                                                       |
| ---------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`    | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`     | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number`   | number | Yes      |                                                                                                                                                                                   |
| `threadId` | string | Yes      | Thread to reply to, from threadId on pull\_request\_read comments                                                                                                                 |
| `body`     | string | Yes      |                                                                                                                                                                                   |

### Limits

- `threadId` must be set.

### Returns

`id`, `threadId`, `body`, `createdAt`, `updatedAt`

## `update_pull_request_review_thread`

Resolve or reopen a review thread by thread ID.

- **Access:** Writes content other people see
- **Asks for confirmation:** Yes
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### Parameters

| Name       | Type    | Required | Description                                                                                                                                                                       |
| ---------- | ------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`    | string  | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`     | string  | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `threadId` | string  | Yes      | Thread to resolve or reopen, from threadId on pull\_request\_read comments                                                                                                        |
| `resolved` | boolean | Yes      | True resolves the thread; false reopens it                                                                                                                                        |

### Limits

- `threadId` must be set.

### Returns

`threadId`, `resolved`

## `update_pull_request_comment`

Correct an existing pull request comment body.

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### Parameters

| Name        | Type   | Required | Description                                                                                                                                                                       |
| ----------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`      | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `commentId` | string | Yes      | Stable comment id from pull\_request\_read with view comments                                                                                                                     |
| `body`      | string | Yes      |                                                                                                                                                                                   |

### Returns

`id`, `body`, `threadId`, `createdAt`, `updatedAt`

## `update_pull_request_labels`

Replace every label on a pull request with the provided names. Each name must be an existing repository label, spelled exactly, including case; this tool never creates labels. For a label that does not exist yet, call create\_label first, then call this tool. Omitted labels are removed. An empty list removes all labels.

- **Access:** Writes
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:write`

### Parameters

| Name     | Type      | Required | Description                                                                                                                                                                       |
| -------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`  | string    | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`   | string    | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number` | number    | Yes      |                                                                                                                                                                                   |
| `labels` | string\[] | Yes      | Complete replacement label names. Omitted names are removed. An empty list removes all labels.                                                                                    |

### Limits

- `labels` takes at most 100 items.

### Returns

`labels` (at most 100)

## `create_label`

Create a repository label so update\_pull\_request\_labels can apply it. label is the name: 1-50 characters, trimmed, and unique in the repository by exact, case-sensitive spelling, so Bug and bug are different labels; reuse an existing label that differs only in case instead of creating another. color is six hex digits with an optional leading #, such as d73a4a; it defaults to ededed. description is optional, at most 255 characters. A name that already exists returns a conflict; apply that label instead.

- **Access:** Writes
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:labels:write`

### Parameters

| Name          | Type   | Required | Description                                                                                                                                                                       |
| ------------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`       | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`        | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `label`       | string | Yes      | Label name to create, 1-50 characters                                                                                                                                             |
| `color`       | string | No       | Six hex digits, optional leading #; defaults to ededed                                                                                                                            |
| `description` | string | No       | Label description, at most 255 characters                                                                                                                                         |

### Limits

- `label` must be set.

### Returns

`name`, `color`, `description`

## `request_pull_request_reviewers`

Request reviewers (users and/or groups) on a pull request.

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### Parameters

| Name     | Type      | Required | Description                                                                                                                                                                       |
| -------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`  | string    | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`   | string    | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number` | number    | Yes      |                                                                                                                                                                                   |
| `users`  | string\[] | No       | User identifiers: public user\_… id or email                                                                                                                                      |
| `groups` | string\[] | No       | Group identifiers: public grp\_… id, qualified slug, or slug                                                                                                                      |

### Limits

- `users` takes at most 100 items.
- `groups` takes at most 100 items.

### Returns

`users` (at most 100), `groups` (at most 100)

## `remove_pull_request_reviewers`

Remove requested reviewers from a pull request.

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### Parameters

| Name     | Type      | Required | Description                                                                                                                                                                       |
| -------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`  | string    | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`   | string    | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number` | number    | Yes      |                                                                                                                                                                                   |
| `users`  | string\[] | No       | User identifiers: public user\_… id or email                                                                                                                                      |
| `groups` | string\[] | No       | Group identifiers: public grp\_… id, qualified slug, or slug                                                                                                                      |

### Limits

- `users` takes at most 100 items.
- `groups` takes at most 100 items.

### Returns

`status`: one of `completed`.

## `checks_read`

Read checks for one target in an Origin-hosted repository: a pull request, commit, suite, or run. Rollup covers materialized check runs on the current page only and is omitted when nextPageToken is present. Does not fetch external provider logs.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:checks:read`, `repository:pull_requests:read`

### Parameters

| Name                  | Type   | Required | Description                                                                                                                                                                       |
| --------------------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`               | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`                | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `target`              | object | Yes      |                                                                                                                                                                                   |
| `target.type`         | string | Yes      |                                                                                                                                                                                   |
| `target.number`       | number | No       |                                                                                                                                                                                   |
| `target.sha`          | string | No       |                                                                                                                                                                                   |
| `target.checkSuiteId` | string | No       |                                                                                                                                                                                   |
| `target.checkRunId`   | string | No       |                                                                                                                                                                                   |
| `pageSize`            | number | No       |                                                                                                                                                                                   |
| `pageToken`           | string | No       |                                                                                                                                                                                   |

### Limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.
- `target.type` is one of `pull_request`, `commit`, `suite`, `run`.

### Returns

`rollupStatus`, `failing` (paged), `suites` (paged), `runs` (paged), `nextPageToken`


---

## Sitemap

[Origin API docs index](https://cursor.com/docs/api/origin/llms.txt)
