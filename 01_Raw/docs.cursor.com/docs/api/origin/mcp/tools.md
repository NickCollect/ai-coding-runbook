---
source_url: https://cursor.com/docs/api/origin/mcp/tools
fetched_at: 2026-10-26T05:39:59.179401+00:00
fetch_method: mintlify_md
---

# Origin MCP tool reference

Every tool the Origin MCP server at `https://api.origin.cursor.com/mcp` lists, in listing order. Parameters are the JSON Schema clients receive from `tools/list`.

| Tool                                                                                                                       | Access                              | Summary                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`get_repository`](https://cursor.com/docs/api/origin/mcp/tools.md#get_repository)                                         | Read-only                           | Get one Origin repository by owner and name, including default branch, mirror state, visibility, and merge settings.                                                                                                                                                                                                                                                        |
| [`list_repositories`](https://cursor.com/docs/api/origin/mcp/tools.md#list_repositories)                                   | Read-only                           | List Origin repositories belonging to an owner slug.                                                                                                                                                                                                                                                                                                                        |
| [`list_namespaces`](https://cursor.com/docs/api/origin/mcp/tools.md#list_namespaces)                                       | Read-only                           | List the Origin namespaces (owner slugs) the caller can list repositories in, ordered by slug.                                                                                                                                                                                                                                                                              |
| [`create_repository`](https://cursor.com/docs/api/origin/mcp/tools.md#create_repository)                                   | Writes                              | Create an empty Origin-hosted repository.                                                                                                                                                                                                                                                                                                                                   |
| [`get_file_contents`](https://cursor.com/docs/api/origin/mcp/tools.md#get_file_contents)                                   | Read-only                           | Read one path at a ref in an Origin-hosted repository.                                                                                                                                                                                                                                                                                                                      |
| [`get_git_tree`](https://cursor.com/docs/api/origin/mcp/tools.md#get_git_tree)                                             | Read-only                           | List a git tree in an Origin-hosted repository at a tree SHA, commit SHA, branch, tag, or HEAD.                                                                                                                                                                                                                                                                             |
| [`grep_contents`](https://cursor.com/docs/api/origin/mcp/tools.md#grep_contents)                                           | Read-only                           | Search file contents across one Origin-hosted repository at a ref, which defaults to the default branch.                                                                                                                                                                                                                                                                    |
| [`list_branches`](https://cursor.com/docs/api/origin/mcp/tools.md#list_branches)                                           | Read-only                           | List branch names and tip commit SHAs for an Origin-hosted repository.                                                                                                                                                                                                                                                                                                      |
| [`list_commits`](https://cursor.com/docs/api/origin/mcp/tools.md#list_commits)                                             | Read-only                           | List commits from a branch or starting ref in an Origin-hosted repository, optionally filtered by lists of exact git author or committer emails, by inclusive since and until bounds on committer time, and by a repository path as `git log --full-history -- <path>` does, without following renames, so a merge is listed when the path differs from any of its parents. |
| [`commit_read`](https://cursor.com/docs/api/origin/mcp/tools.md#commit_read)                                               | Read-only                           | Read one commit in an Origin-hosted repository.                                                                                                                                                                                                                                                                                                                             |
| [`compare_commits`](https://cursor.com/docs/api/origin/mcp/tools.md#compare_commits)                                       | Read-only                           | Compare two refs of an Origin-hosted repository relative to their merge base.                                                                                                                                                                                                                                                                                               |
| [`sync_mirror`](https://cursor.com/docs/api/origin/mcp/tools.md#sync_mirror)                                               | Destructive, reaches outside Origin | Sync a mirrored repository from upstream, waiting for a ref or optional SHA.                                                                                                                                                                                                                                                                                                |
| [`list_pull_requests`](https://cursor.com/docs/api/origin/mcp/tools.md#list_pull_requests)                                 | Read-only                           | List pull requests in an Origin-hosted repository, filtered by state, head, author, base, stackId, mergeCommitShas, or inclusive mergedSince/mergedUntil bounds on mergedAt, and sorted by creation or update time in either direction.                                                                                                                                     |
| [`search_pull_requests`](https://cursor.com/docs/api/origin/mcp/tools.md#search_pull_requests)                             | Read-only                           | Search pull requests across the Origin-hosted repositories the caller can read, written in GitHub's pull request search syntax.                                                                                                                                                                                                                                             |
| [`pull_request_read`](https://cursor.com/docs/api/origin/mcp/tools.md#pull_request_read)                                   | Read-only                           | Read one Origin-hosted pull request through a single view: summary, files, commits, reviews, comments, or threads.                                                                                                                                                                                                                                                          |
| [`get_pull_request_attachment`](https://cursor.com/docs/api/origin/mcp/tools.md#get_pull_request_attachment)               | Read-only                           | Fetch one image or file attached to an Origin-hosted pull request.                                                                                                                                                                                                                                                                                                          |
| [`create_pull_request`](https://cursor.com/docs/api/origin/mcp/tools.md#create_pull_request)                               | Writes                              | Create a pull request from an already-pushed branch.                                                                                                                                                                                                                                                                                                                        |
| [`update_pull_request`](https://cursor.com/docs/api/origin/mcp/tools.md#update_pull_request)                               | Writes                              | Update a pull request's title, description, and lifecycle through the public fields.                                                                                                                                                                                                                                                                                        |
| [`update_pull_request_base`](https://cursor.com/docs/api/origin/mcp/tools.md#update_pull_request_base)                     | Writes                              | Retarget a pull request's base branch, stack it on another pull request, or move it off its stack.                                                                                                                                                                                                                                                                          |
| [`merge_pull_request`](https://cursor.com/docs/api/origin/mcp/tools.md#merge_pull_request)                                 | Destructive                         | Merge a pull request, or a stack up to and including it.                                                                                                                                                                                                                                                                                                                    |
| [`create_pull_request_review`](https://cursor.com/docs/api/origin/mcp/tools.md#create_pull_request_review)                 | Writes content other people see     | Submit a comment, approval, or request-changes review on a pull request.                                                                                                                                                                                                                                                                                                    |
| [`update_pull_request_review`](https://cursor.com/docs/api/origin/mcp/tools.md#update_pull_request_review)                 | Writes content other people see     | Correct the body of an existing pull request review.                                                                                                                                                                                                                                                                                                                        |
| [`dismiss_pull_request_review`](https://cursor.com/docs/api/origin/mcp/tools.md#dismiss_pull_request_review)               | Destructive                         | Dismiss a submitted approve or request-changes review.                                                                                                                                                                                                                                                                                                                      |
| [`create_pull_request_comment`](https://cursor.com/docs/api/origin/mcp/tools.md#create_pull_request_comment)               | Writes content other people see     | Create a general discussion comment on a pull request.                                                                                                                                                                                                                                                                                                                      |
| [`create_pull_request_inline_comment`](https://cursor.com/docs/api/origin/mcp/tools.md#create_pull_request_inline_comment) | Writes content other people see     | Create a file-level, single-line, or line-range inline comment, optionally against a specific pull request version.                                                                                                                                                                                                                                                         |
| [`reply_pull_request_review_thread`](https://cursor.com/docs/api/origin/mcp/tools.md#reply_pull_request_review_thread)     | Writes content other people see     | Reply to an existing review thread by thread ID.                                                                                                                                                                                                                                                                                                                            |
| [`update_pull_request_review_thread`](https://cursor.com/docs/api/origin/mcp/tools.md#update_pull_request_review_thread)   | Writes content other people see     | Resolve or reopen a review thread by thread ID.                                                                                                                                                                                                                                                                                                                             |
| [`update_pull_request_comment`](https://cursor.com/docs/api/origin/mcp/tools.md#update_pull_request_comment)               | Writes content other people see     | Correct an existing pull request comment body.                                                                                                                                                                                                                                                                                                                              |
| [`update_pull_request_labels`](https://cursor.com/docs/api/origin/mcp/tools.md#update_pull_request_labels)                 | Writes                              | Replace every label on a pull request with the provided names.                                                                                                                                                                                                                                                                                                              |
| [`create_label`](https://cursor.com/docs/api/origin/mcp/tools.md#create_label)                                             | Writes                              | Create a repository label so update\_pull\_request\_labels can apply it.                                                                                                                                                                                                                                                                                                    |
| [`request_pull_request_reviewers`](https://cursor.com/docs/api/origin/mcp/tools.md#request_pull_request_reviewers)         | Writes content other people see     | Request reviewers (users and/or groups) on a pull request.                                                                                                                                                                                                                                                                                                                  |
| [`remove_pull_request_reviewers`](https://cursor.com/docs/api/origin/mcp/tools.md#remove_pull_request_reviewers)           | Writes content other people see     | Remove requested reviewers from a pull request.                                                                                                                                                                                                                                                                                                                             |
| [`checks_read`](https://cursor.com/docs/api/origin/mcp/tools.md#checks_read)                                               | Read-only                           | Read checks for one target in an Origin-hosted repository: a pull request, commit, suite, or run.                                                                                                                                                                                                                                                                           |
| [`list_rulesets`](https://cursor.com/docs/api/origin/mcp/tools.md#list_rulesets)                                           | Read-only                           | List the rulesets on an Origin-hosted repository as summaries: id, name, kind, enforcement, included and excluded ref name patterns, the rule types present, and the bypass actor count.                                                                                                                                                                                    |
| [`get_ruleset`](https://cursor.com/docs/api/origin/mcp/tools.md#get_ruleset)                                               | Read-only                           | Read one ruleset on an Origin-hosted repository by its id from list\_rulesets: name, description, kind, enforcement, included and excluded ref name patterns, each rule as its ruleType and JSON parameters, and each bypass actor as its kind (user, group, or app), id, and bypassMode.                                                                                   |
| [`get_repository_access`](https://cursor.com/docs/api/origin/mcp/tools.md#get_repository_access)                           | Read-only                           | Read who can access an Origin-hosted repository.                                                                                                                                                                                                                                                                                                                            |

## get\_repository

Get one Origin repository by owner and name, including default branch, mirror state, visibility, and merge settings.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:metadata:read`

### get\_repository parameters

| Name    | Type   | Required | Description                                                                                                                                                                       |
| ------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner` | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`  | string | Yes      | Origin repository name within that namespace                                                                                                                                      |

### get\_repository returns

`id`, `owner`, `name`, `fullName`, `defaultBranch`, `cloneUrl`, `mirror`, `visibility`, `allowMergeCommit`, `allowSquashMerge`, `deleteBranchOnMerge`

## list\_repositories

List Origin repositories belonging to an owner slug.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `namespace:repositories:read`

### list\_repositories parameters

| Name        | Type   | Required | Description                                                                                                                                                                       |
| ----------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `pageSize`  | number | No       |                                                                                                                                                                                   |
| `pageToken` | string | No       |                                                                                                                                                                                   |
| `filter`    | string | No       | Case-insensitive repository name substring                                                                                                                                        |

### list\_repositories limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.

### list\_repositories returns

`repositories` (paged), `nextPageToken`

## list\_namespaces

List the Origin namespaces (owner slugs) the caller can list repositories in, ordered by slug. Each slug is a valid owner for list\_repositories; viewerCanCreateRepositories reports whether creating a repository there would be allowed. An empty list means the caller has no Origin repositories to read; repositories on GitHub or other hosts are not reachable through these tools.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `namespace:repositories:read`

### list\_namespaces parameters

| Name        | Type   | Required | Description |
| ----------- | ------ | -------- | ----------- |
| `pageSize`  | number | No       |             |
| `pageToken` | string | No       |             |

### list\_namespaces limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.

### list\_namespaces returns

`namespaces` (paged), `nextPageToken`

## create\_repository

Create an empty Origin-hosted repository. Pick an owner from list\_namespaces where viewerCanCreateRepositories is true; omit owner to use the caller's personal namespace, which Origin claims on first use (needs an eligible plan, a Privacy Mode that allows code storage, and no team membership; team members pass their team slug). Both steps are one approval: confirm with the user before calling. defaultBranch defaults to main. Repository names are unique per owner, so retrying after a success fails with a conflict; read the repository with get\_repository instead. Returns the created repository, including cloneUrl.

- **Access:** Writes
- **Asks for confirmation:** Yes
- **On the read-only endpoint:** No
- **Required scopes:** `namespace:repositories:create`

### create\_repository parameters

| Name            | Type   | Required | Description                                                                                                                                                                       |
| --------------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`         | string | No       | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`          | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `defaultBranch` | string | No       | Default branch name. Omit for main.                                                                                                                                               |

### create\_repository returns

`id`, `owner`, `name`, `fullName`, `defaultBranch`, `cloneUrl`, `visibility`, `allowMergeCommit`, `allowSquashMerge`, `deleteBranchOnMerge`

## get\_file\_contents

Read one path at a ref in an Origin-hosted repository. Files larger than the byte cap are truncated. A directory returns type dir and its immediate children as entries (name, path, type, sha, and size for files) instead of content; entries past the cap are dropped and truncated is set.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:contents:read`

### get\_file\_contents parameters

| Name        | Type   | Required | Description                                                                                                                                                                       |
| ----------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`      | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `path`      | string | Yes      |                                                                                                                                                                                   |
| `ref`       | string | No       |                                                                                                                                                                                   |
| `startLine` | number | No       |                                                                                                                                                                                   |
| `endLine`   | number | No       |                                                                                                                                                                                   |

### get\_file\_contents limits

- `content` is truncated after 256 KiB.
- A line range covers at most 500 lines.

### get\_file\_contents returns

`files` (at most 1), `path`, `content`, `encoding`, `sha`, `truncated`, `type`, `entries` (at most 1000), `name`, `size`

## get\_git\_tree

List a git tree in an Origin-hosted repository at a tree SHA, commit SHA, branch, tag, or HEAD. sha defaults to HEAD. Immediate children by default, or the full walk with recursive true. Each entry is path, mode, type (blob, tree, or commit), sha, and size for blobs. Entries past the cap are dropped and truncated is set; list subtrees non-recursively to see more. get\_file\_contents reads one blob.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:contents:read`

### get\_git\_tree parameters

| Name        | Type    | Required | Description                                                                                                                                                                       |
| ----------- | ------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string  | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`      | string  | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `sha`       | string  | No       | Tree SHA, commit SHA, branch, tag, or HEAD. Omit for HEAD.                                                                                                                        |
| `recursive` | boolean | No       | True walks the whole tree; omit for immediate children only                                                                                                                       |

### get\_git\_tree returns

`sha`, `entries` (at most 1000), `path`, `mode`, `type`, `size`, `truncated`

## grep\_contents

Search file contents across one Origin-hosted repository at a ref, which defaults to the default branch. The query is a regular expression matched case-sensitively; set literal for exact text, or caseInsensitive to ignore case (regex mode prefixes (?i) for GrepContents). wholeWord applies only with literal; for regex use \b. Returns matching lines plus any requested context lines, capped at 1000 matching occurrences, and sets limitHit when that cap is reached. Each returned line contains its full text, so the occurrence cap does not bound response bytes. There is no pagination. Narrow query, filterPath, includes, or excludes to reach other matches.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:contents:read`

### grep\_contents parameters

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

### grep\_contents limits

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

### grep\_contents returns

`matches` (at most 21000), `path`, `lineNumber`, `line`, `kind`, `submatches` (at most 1000), `limitHit`

## list\_branches

List branch names and tip commit SHAs for an Origin-hosted repository. Optional prefix filters each page after pagination.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:contents:read`

### list\_branches parameters

| Name        | Type   | Required | Description                                                                                                                                                                       |
| ----------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`      | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `pageSize`  | number | No       |                                                                                                                                                                                   |
| `pageToken` | string | No       |                                                                                                                                                                                   |
| `prefix`    | string | No       | Case-sensitive branch name prefix. Applied per page after pagination; keep following nextPageToken even when a page has no matches.                                               |

### list\_branches limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.

### list\_branches returns

`branches` (paged), `nextPageToken`

## list\_commits

List commits from a branch or starting ref in an Origin-hosted repository, optionally filtered by lists of exact git author or committer emails, by inclusive since and until bounds on committer time, and by a repository path as `git log --full-history -- <path>` does, without following renames, so a merge is listed when the path differs from any of its parents. A commit matches a list when its email equals any listed email, and must match every list, bound, and path that is given. A directory path matches when any descendant changes. A filtered page can be short while nextPageToken is present, and is empty with nextPageToken only after 100,000 commits were searched without a match. Keep paging to reach older matches. Each item is sha, full message, author, committer, parents, and tree. Omits patches. Continuation calls reuse the filters stored in pageToken.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:contents:read`

### list\_commits parameters

| Name              | Type      | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------- | --------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`           | string    | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it.                                                                                                                                                                                                                                                                                            |
| `name`            | string    | Yes      | Origin repository name within that namespace                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `ref`             | string    | No       | Branch or starting commit                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `authorEmails`    | string\[] | No       | Only commits whose git author email equals any listed email, case-insensitive. Not names or partial matches. At most 100 distinct emails.                                                                                                                                                                                                                                                                                                                                    |
| `committerEmails` | string\[] | No       | Only commits whose git committer email equals any listed email, case-insensitive. At most 100 distinct emails. Combined with authorEmails, a commit must match both lists.                                                                                                                                                                                                                                                                                                   |
| `since`           | string    | No       | Only commits whose git committer time is at or after this RFC 3339 timestamp, such as 2026-08-01T00:00:00Z. The bound is inclusive and uses committer time, which a rebase or cherry-pick rewrites, not author time.                                                                                                                                                                                                                                                         |
| `until`           | string    | No       | Only commits whose git committer time is at or before this RFC 3339 timestamp, such as 2026-08-31T23:59:59Z. The bound is inclusive. Combined with since and the email filters, a commit must match every filter that is set.                                                                                                                                                                                                                                                |
| `path`            | string    | No       | Only commits that change this repository path, without following renames. A merge is listed when the path differs from any of its parents, as `git log --full-history -- <path>` does. A directory matches when any descendant changes. Surrounding whitespace and empty and . segments are ignored, so leading, trailing, and repeated slashes do not matter; a .. segment is rejected. Combined with email and time filters, a commit must match every filter that is set. |
| `pageSize`        | number    | No       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `pageToken`       | string    | No       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### list\_commits limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.
- `authorEmails` takes at most 100 items.
- `committerEmails` takes at most 100 items.

### list\_commits returns

`commits` (paged), `nextPageToken`

## commit\_read

Read one commit in an Origin-hosted repository. Choose a single view: metadata, files, or a bounded patch. view defaults to metadata.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:contents:read`

### commit\_read parameters

| Name        | Type   | Required | Description                                                                                                                                                                       |
| ----------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`      | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `sha`       | string | Yes      |                                                                                                                                                                                   |
| `view`      | string | No       | metadata (default), files, or a bounded patch                                                                                                                                     |
| `pageSize`  | number | No       |                                                                                                                                                                                   |
| `pageToken` | string | No       |                                                                                                                                                                                   |
| `startLine` | number | No       |                                                                                                                                                                                   |
| `endLine`   | number | No       |                                                                                                                                                                                   |

### commit\_read limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.
- `view` is one of `metadata`, `files`, `patch`.
- Long `patch` output is returned in chunks.
- A line range covers at most 500 lines.

### commit\_read returns

Set `view` to choose what comes back:

- `metadata`: `sha`, `message`, `author`, `committer`, `stats`, `parents`
- `files`: `files` (paged), `path`, `status`, `additions`, `deletions`, `changes`, `previousFilename`
- `patch`: `patch` (chunked), `truncated`

## compare\_commits

Compare two refs of an Origin-hosted repository relative to their merge base. Choose a single view: summary or files. view defaults to summary. Files pages the paths that differ between head and the merge base, including per-file patches. Continuation calls must resend base and head with pageToken; an omitted view still pages files.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:contents:read`

### compare\_commits parameters

| Name        | Type   | Required | Description                                                                                                                                                                       |
| ----------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`      | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `base`      | string | Yes      | Ref the comparison starts from                                                                                                                                                    |
| `head`      | string | Yes      | Ref compared against the base                                                                                                                                                     |
| `view`      | string | No       | summary (default) or files                                                                                                                                                        |
| `pageSize`  | number | No       |                                                                                                                                                                                   |
| `pageToken` | string | No       |                                                                                                                                                                                   |

### compare\_commits limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.
- `view` is one of `summary`, `files`.

### compare\_commits returns

Set `view` to choose what comes back:

- `summary`: `mergeBase`, `aheadBy`, `behindBy`, `status`
- `files`: `files` (paged), `path`, `status`, `additions`, `deletions`, `changes`, `previousFilename`, `patch`

## sync\_mirror

Sync a mirrored repository from upstream, waiting for a ref or optional SHA. Returns completed or pending.

- **Access:** Destructive, reaches outside Origin
- **Asks for confirmation:** Yes
- **On the read-only endpoint:** No
- **Required scopes:** `repository:mirror:sync`

### sync\_mirror parameters

| Name    | Type   | Required | Description                                                                                                                                                                       |
| ------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner` | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`  | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `ref`   | string | Yes      | Full ref to fetch, such as refs/heads/main                                                                                                                                        |
| `sha`   | string | No       | Full commit id to wait for; omit to wait on the ref tip                                                                                                                           |

### sync\_mirror returns

`status`: one of `completed`, `pending`.

## list\_pull\_requests

List pull requests in an Origin-hosted repository, filtered by state, head, author, base, stackId, mergeCommitShas, or inclusive mergedSince/mergedUntil bounds on mergedAt, and sorted by creation or update time in either direction. Items are compact summaries (author, timestamps, merged/closedAt/mergedAt, and stack membership when the pull request is stacked); they omit body and diff stats—use pull\_request\_read for those. With stackId, the items are that stack's members in the requested sort order, not stack order; rebuild the tree from each member's stack.parent, and pass state all because the default open state leaves merged members out. mergeCommitShas matches pull requests whose merge commit equals any listed SHA; pass state merged or all because a merge commit is recorded only after landing. mergedSince and mergedUntil filter on mergedAt; unmerged pull requests never match, so pass state merged or all. Continuation calls must resend those filters with pageToken.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:pull_requests:read`

### list\_pull\_requests parameters

| Name              | Type      | Required | Description                                                                                                                                                                                                                                                                                                         |
| ----------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`           | string    | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it.                                                                                                                                   |
| `name`            | string    | Yes      | Origin repository name within that namespace                                                                                                                                                                                                                                                                        |
| `state`           | string    | No       | open (default), closed, merged, or all                                                                                                                                                                                                                                                                              |
| `head`            | string    | No       | Head branch                                                                                                                                                                                                                                                                                                         |
| `author`          | string    | No       | Actor id (user\_…, app\_…, or sa\_…)                                                                                                                                                                                                                                                                                |
| `base`            | string    | No       | Base branch, short name or refs/heads/…                                                                                                                                                                                                                                                                             |
| `stackId`         | string    | No       | Stack id (stk\_…) from stack.id on a pull request. Lists only that stack's members, in the requested sort order rather than stack order; rebuild the tree from each member's stack.parent. Pass state all to include merged members.                                                                                |
| `mergeCommitShas` | string\[] | No       | Full merge-commit SHAs as returned in mergeCommitSha. A pull request matches when its merge commit equals any listed SHA. At most 100 distinct SHAs. Pass state merged or all; the default open state has no merge commit.                                                                                          |
| `mergedSince`     | string    | No       | Only pull requests whose mergedAt is at or after this RFC 3339 timestamp, such as 2026-08-01T00:00:00Z. The bound is inclusive. Unmerged pull requests never match. Pass state merged or all; the default open state has no mergedAt. Combined with mergedUntil, a pull request must match every bound that is set. |
| `mergedUntil`     | string    | No       | Only pull requests whose mergedAt is at or before this RFC 3339 timestamp, such as 2026-08-31T23:59:59Z. The bound is inclusive. Unmerged pull requests never match.                                                                                                                                                |
| `direction`       | string    | No       | desc (default) or asc                                                                                                                                                                                                                                                                                               |
| `sortBy`          | string    | No       | created (default) or updated                                                                                                                                                                                                                                                                                        |
| `pageSize`        | number    | No       |                                                                                                                                                                                                                                                                                                                     |
| `pageToken`       | string    | No       |                                                                                                                                                                                                                                                                                                                     |

### list\_pull\_requests limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.
- `state` is one of `open`, `closed`, `merged`, `all`.
- `direction` is one of `desc`, `asc`.
- `sortBy` is one of `created`, `updated`.
- `mergeCommitShas` takes at most 100 items.

### list\_pull\_requests returns

`pullRequests` (paged), `nextPageToken`

## search\_pull\_requests

Search pull requests across the Origin-hosted repositories the caller can read, written in GitHub's pull request search syntax. A query combines qualifiers (is:open, is:merged, is:draft, author:, review-requested:, reviewed-by:, label:, base:, head:, and created:, updated:, merged: or closed: with a date or range), bare words and quoted phrases matched against text, the operators AND, OR and NOT (or a leading -), parentheses, and one sort: such as sort:updated-desc. repo:owner/name, org: or user: choose the repositories searched; otherwise owner and name choose one. A search reads one namespace (one org or user) at a time: a query whose repo:, org: and user: name more than one is refused, and so is one that names none without owner and name, so add org:NAME. A session limited to specific repositories, such as a cloud agent's, searches only those repositories; if a search is refused for not naming them, name them with repo:owner/name or with owner and name. Results come from a search index and are eventually consistent: a pull request created or changed moments ago can be missing or stale, so read your own writes with list\_pull\_requests or pull\_request\_read. Items are the compact list\_pull\_requests summaries plus each pull request's repository, without stack.parent. totalCount is exact unless totalCountIsLowerBound is set. A query Origin cannot answer fails with its problems, each with its query\[start:end] span when it has one: every qualifier the parser rejects before it stops is named, along with at most one conflict across the whole search such as a second sort:, and a malformed query (such as one with an unclosed quote) names only how it is written. A query that parses is then checked in stages, and only the first stage that finds a problem is named: a second namespace, then a person Origin does not know, then a qualifier that search cannot answer, such as is:queued. Continuation calls must resend the same query, owner and name with pageToken. Examples: org:acme is:open review-requested:@me, or repo:acme/web is:merged merged:>=2026-09-01.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:pull_requests:read`, `repository:pull_requests:reviews:read`

### search\_pull\_requests parameters

| Name        | Type   | Required | Description                                                                                                                                                                       |
| ----------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`     | string | Yes      | GitHub pull request search query, at most 1024 characters, such as org:acme is:open review-requested:@me                                                                          |
| `owner`     | string | No       | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`      | string | No       | Origin repository name within that namespace                                                                                                                                      |
| `pageSize`  | number | No       |                                                                                                                                                                                   |
| `pageToken` | string | No       |                                                                                                                                                                                   |

### search\_pull\_requests limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.
- `query` must be set.
- `query` is at most 1024 characters.

### search\_pull\_requests returns

`pullRequests` (paged), `totalCount`, `totalCountIsLowerBound`, `nextPageToken`

## pull\_request\_read

Read one Origin-hosted pull request through a single view: summary, files, commits, reviews, comments, or threads. view defaults to summary. Summary includes labels, requested reviewers, and stack membership (stack id and parent pull request) when the pull request is stacked. The threads view requires threadIds and pages comments in those threads. Comments and threads carry url, a cursor.com link to that thread or comment on the pull request page. Images and recordings pasted into the description, a review, or a comment appear as cursor.com user-attachments URLs; fetch one with get\_pull\_request\_attachment.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:pull_requests:read`, `repository:pull_requests:reviews:read`

### pull\_request\_read parameters

| Name        | Type      | Required | Description                                                                                                                                                                       |
| ----------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string    | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`      | string    | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number`    | number    | Yes      |                                                                                                                                                                                   |
| `view`      | string    | No       | summary (default), files, commits, reviews, comments, or threads                                                                                                                  |
| `pageSize`  | number    | No       |                                                                                                                                                                                   |
| `pageToken` | string    | No       |                                                                                                                                                                                   |
| `startLine` | number    | No       |                                                                                                                                                                                   |
| `endLine`   | number    | No       |                                                                                                                                                                                   |
| `threadIds` | string\[] | No       | Thread ids for the threads view                                                                                                                                                   |

### pull\_request\_read limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.
- `view` is one of `summary`, `files`, `commits`, `reviews`, `comments`, `stack`, `threads`.
- `threadIds` takes at most 20 items.
- Long `patch` output is returned in chunks.
- A line range covers at most 500 lines.

### pull\_request\_read returns

Set `view` to choose what comes back:

- `summary`: `number`, `title`, `state`, `draft`, `merged`, `author`, `base`, `head`, `createdAt`, `updatedAt`, `closedAt`, `mergedAt`, `body`, `additions`, `deletions`, `changedFiles`, `stack`, `labels` (at most 100), `requestedReviewers` (at most 100)
- `files`: `files` (paged), `path`, `status`, `additions`, `deletions`, `changes`, `patch` (chunked), `truncated`
- `commits`: `commits` (paged)
- `reviews`: `reviews` (paged), `id`, `body`, `verdict`, `author`, `submittedAt`
- `comments`: `comments` (paged), `id`, `body`, `threadId`, `author`, `createdAt`, `updatedAt`, `url`
- `stack` (not yet public): `parent`, `children` (paged), `mergePrefix`, `convergence`
- `threads`: `threads` (paged)

## get\_pull\_request\_attachment

Fetch one image or file attached to an Origin-hosted pull request. url is an attachment URL exactly as pull\_request\_read returns it in the description, a review, or a comment: a cursor.com user-attachments URL, or a legacy upload-bucket URL. Only those upload shapes are accepted, and the URL must appear in that pull request's text; no other URL is ever fetched. An image of at most 3 MiB is returned as an image content block beside the JSON summary (delivery inline, with contentType and byteLength). A larger image, a recording, or another file is answered with delivery url: fetchUrl serves the bytes without further credentials, until expiresAt when the URL is signed, and reason says why (video, too\_large, or not\_an\_image). kind is image, video, or file.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:pull_requests:read`, `repository:pull_requests:reviews:read`

### get\_pull\_request\_attachment parameters

| Name     | Type   | Required | Description                                                                                                                                                                       |
| -------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`  | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`   | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number` | number | Yes      |                                                                                                                                                                                   |
| `url`    | string | Yes      | Attachment URL exactly as pull\_request\_read returns it in the description, a review, or a comment of this pull request                                                          |

### get\_pull\_request\_attachment limits

- `url` must be set.
- `url` is at most 2048 characters.

### get\_pull\_request\_attachment returns

`url`, `kind`, `delivery`, `contentType`, `byteLength`, `fetchUrl`, `expiresAt`, `reason`

## create\_pull\_request

Create a pull request from an already-pushed branch. To stack it, pass parentPullNumber: the base becomes that pull request's head branch (any other base is rejected), and head must have been built on that branch, meaning the two share a commit beyond the parent's own base. A head built off trunk or from unrelated history is rejected with the rebase to run. A head that has since fallen behind the parent is accepted and the response carries needsRestack, because the pull request cannot land until it is restacked; this tool never restacks. stackParent is the stored parent's number, read back after the create.

- **Access:** Writes
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:write`

### create\_pull\_request parameters

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

### create\_pull\_request returns

`number`, `title`, `state`, `draft`, `head`, `base`, `stackParent`, `needsRestack`

## update\_pull\_request

Update a pull request's title, description, and lifecycle through the public fields. Omit title or body to leave that field unchanged; pass an empty body to clear the description. Lifecycle is state (open or closed) plus draft, sent independently: state closed closes and ignores draft; state open reopens, and without draft true marks ready and publishes an existing draft; draft true reopens as a draft, alone or together with state open; draft false marks ready and reopens a closed pull request. Send one lifecycle field, both, or neither, so a metadata-only update is valid. Metadata and lifecycle together send one public UpdatePullRequest. Origin applies present fields in its documented order; a failure can leave some fields applied, so re-read after an error. merged is not writable, and ready is draft false or state open rather than a state value.

- **Access:** Writes
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:write`

### update\_pull\_request parameters

| Name     | Type               | Required | Description                                                                                                                                                                       |
| -------- | ------------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`  | string             | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`   | string             | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number` | number             | Yes      |                                                                                                                                                                                   |
| `title`  | string             | No       | New title. Omit to leave unchanged.                                                                                                                                               |
| `body`   | string             | No       | New description. Omit to leave unchanged. Pass "" to clear.                                                                                                                       |
| `state`  | "open" \| "closed" | No       | open or closed. Omit to leave unchanged.                                                                                                                                          |
| `draft`  | boolean            | No       | Draft flag. Omit to leave unchanged.                                                                                                                                              |

### update\_pull\_request limits

- `state` is one of `open`, `closed`.

### update\_pull\_request returns

`number`, `title`, `body`, `state`, `draft`

## update\_pull\_request\_base

Retarget a pull request's base branch, stack it on another pull request, or move it off its stack. With parentPullNumber, the base becomes that pull request's head branch and the stack parent is set in the same update. With base, the pull request is retargeted to that branch: the head branch of an open pull request makes that pull request the parent, and the default branch or a branch with no open pull request moves it off its stack. Stacking is allowed only when this pull request's branch was built on the parent, meaning the two share a commit beyond the parent's own base; a branch built off trunk or from unrelated history is rejected with the rebase to run. A branch that has fallen behind the parent is accepted and the response carries needsRestack, because the pull request cannot land until it is restacked. This tool stacks and unstacks but never restacks: no commit is rebased or replayed. Returns the stored base and head refs, plus stackParent when stacked.

- **Access:** Writes
- **Asks for confirmation:** Yes
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:write`

### update\_pull\_request\_base parameters

| Name               | Type   | Required | Description                                                                                                                                                                       |
| ------------------ | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`            | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`             | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number`           | number | Yes      |                                                                                                                                                                                   |
| `base`             | string | No       | Branch to retarget onto. The default branch or a branch with no open pull request unstacks; the head branch of an open pull request stacks on it. Send this or parentPullNumber.  |
| `parentPullNumber` | number | No       | Pull request to stack on, by number. Its head branch becomes the base. Send this or base.                                                                                         |

### update\_pull\_request\_base returns

`number`, `base`, `head`, `stackParent`, `needsRestack`

## merge\_pull\_request

Merge a pull request, or a stack up to and including it. On a stacked pull request this lands every open pull request from the stack root through this one in one commit (one squash commit with squash, one merge commit otherwise); Origin checks every member first and lands nothing if one is blocked. Where a merge queue owns the branch, a single pull request is queued instead, and nothing lands yet. If Origin queues a stack as one merge queue entry instead, its members land in one commit or none do. When the call queues, mergeCommitSha and mergedPrefix are empty, because nothing has landed yet. To land a stack one pull request at a time, merge the lowest open one each time; each becomes its own commit, and the ones above usually need a restack after each landing. Requires the expected head SHA of this pull request. Optional mergeMethod (merge or squash); omit it and Origin picks a method the repository accepts. mergedPrefix lists every pull request that landed. Pull requests above the target stay open; skippedDescendants is currently always empty.

- **Access:** Destructive
- **Asks for confirmation:** Yes
- **On the read-only endpoint:** No
- **Required scopes:** `repository:contents:write`

### merge\_pull\_request parameters

| Name              | Type                | Required | Description                                                                                                                                                                       |
| ----------------- | ------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`           | string              | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`            | string              | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number`          | number              | Yes      |                                                                                                                                                                                   |
| `expectedHeadSha` | string              | Yes      |                                                                                                                                                                                   |
| `mergeMethod`     | "merge" \| "squash" | No       | merge or squash. Omit for the repository default.                                                                                                                                 |

### merge\_pull\_request limits

- `expectedHeadSha` must be set.
- `mergeMethod` is one of `merge`, `squash`.

### merge\_pull\_request returns

`mergeCommitSha`, `mergedPrefix` (at most 200), `skippedDescendants` (at most 100)

## create\_pull\_request\_review

Submit a comment, approval, or request-changes review on a pull request. Inline review comments are unsupported.

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### create\_pull\_request\_review parameters

| Name     | Type   | Required | Description                                                                                                                                                                       |
| -------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`  | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`   | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number` | number | Yes      |                                                                                                                                                                                   |
| `event`  | string | Yes      | COMMENT, APPROVE, or REQUEST\_CHANGES                                                                                                                                             |
| `body`   | string | No       |                                                                                                                                                                                   |

### create\_pull\_request\_review limits

- `event` is one of `COMMENT`, `APPROVE`, `REQUEST_CHANGES`.

### create\_pull\_request\_review returns

`id`, `state`, `body`

## update\_pull\_request\_review

Correct the body of an existing pull request review.

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### update\_pull\_request\_review parameters

| Name       | Type   | Required | Description                                                                                                                                                                       |
| ---------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`    | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`     | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number`   | number | Yes      |                                                                                                                                                                                   |
| `reviewId` | string | Yes      |                                                                                                                                                                                   |
| `body`     | string | Yes      |                                                                                                                                                                                   |

### update\_pull\_request\_review returns

`id`, `state`, `body`

## dismiss\_pull\_request\_review

Dismiss a submitted approve or request-changes review.

- **Access:** Destructive
- **Asks for confirmation:** Yes
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### dismiss\_pull\_request\_review parameters

| Name       | Type   | Required | Description                                                                                                                                                                       |
| ---------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`    | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`     | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number`   | number | Yes      |                                                                                                                                                                                   |
| `reviewId` | string | Yes      |                                                                                                                                                                                   |
| `message`  | string | Yes      | Reason recorded with the dismissal                                                                                                                                                |

### dismiss\_pull\_request\_review returns

`id`, `state`, `dismissal`

## create\_pull\_request\_comment

Create a general discussion comment on a pull request.

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### create\_pull\_request\_comment parameters

| Name     | Type   | Required | Description                                                                                                                                                                       |
| -------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`  | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`   | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number` | number | Yes      |                                                                                                                                                                                   |
| `body`   | string | Yes      |                                                                                                                                                                                   |

### create\_pull\_request\_comment returns

`id`, `body`

## create\_pull\_request\_inline\_comment

Create a file-level, single-line, or line-range inline comment, optionally against a specific pull request version.

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### create\_pull\_request\_inline\_comment parameters

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

### create\_pull\_request\_inline\_comment limits

- A line range covers at most 500 lines.

### create\_pull\_request\_inline\_comment returns

`threadId`, `id`, `path`, `line`, `body`

## reply\_pull\_request\_review\_thread

Reply to an existing review thread by thread ID.

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### reply\_pull\_request\_review\_thread parameters

| Name       | Type   | Required | Description                                                                                                                                                                       |
| ---------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`    | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`     | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number`   | number | Yes      |                                                                                                                                                                                   |
| `threadId` | string | Yes      | Thread to reply to, from threadId on pull\_request\_read comments                                                                                                                 |
| `body`     | string | Yes      |                                                                                                                                                                                   |

### reply\_pull\_request\_review\_thread limits

- `threadId` must be set.

### reply\_pull\_request\_review\_thread returns

`id`, `threadId`, `body`, `createdAt`, `updatedAt`

## update\_pull\_request\_review\_thread

Resolve or reopen a review thread by thread ID.

- **Access:** Writes content other people see
- **Asks for confirmation:** Yes
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### update\_pull\_request\_review\_thread parameters

| Name       | Type    | Required | Description                                                                                                                                                                       |
| ---------- | ------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`    | string  | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`     | string  | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `threadId` | string  | Yes      | Thread to resolve or reopen, from threadId on pull\_request\_read comments                                                                                                        |
| `resolved` | boolean | Yes      | True resolves the thread; false reopens it                                                                                                                                        |

### update\_pull\_request\_review\_thread limits

- `threadId` must be set.

### update\_pull\_request\_review\_thread returns

`threadId`, `resolved`

## update\_pull\_request\_comment

Correct an existing pull request comment body.

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### update\_pull\_request\_comment parameters

| Name        | Type   | Required | Description                                                                                                                                                                       |
| ----------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`      | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `commentId` | string | Yes      | Stable comment id from pull\_request\_read with view comments                                                                                                                     |
| `body`      | string | Yes      |                                                                                                                                                                                   |

### update\_pull\_request\_comment returns

`id`, `body`, `threadId`, `createdAt`, `updatedAt`

## update\_pull\_request\_labels

Replace every label on a pull request with the provided names. Each name must be an existing repository label, spelled exactly, including case; this tool never creates labels. For a label that does not exist yet, call create\_label first, then call this tool. Omitted labels are removed. An empty list removes all labels.

- **Access:** Writes
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:write`

### update\_pull\_request\_labels parameters

| Name     | Type      | Required | Description                                                                                                                                                                       |
| -------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`  | string    | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`   | string    | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number` | number    | Yes      |                                                                                                                                                                                   |
| `labels` | string\[] | Yes      | Complete replacement label names. Omitted names are removed. An empty list removes all labels.                                                                                    |

### update\_pull\_request\_labels limits

- `labels` takes at most 100 items.

### update\_pull\_request\_labels returns

`labels` (at most 100)

## create\_label

Create a repository label so update\_pull\_request\_labels can apply it. label is the name: 1-50 characters, trimmed, and unique in the repository by exact, case-sensitive spelling, so Bug and bug are different labels; reuse an existing label that differs only in case instead of creating another. color is six hex digits with an optional leading #, such as d73a4a; it defaults to ededed. description is optional, at most 255 characters. A name that already exists returns a conflict; apply that label instead.

- **Access:** Writes
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:labels:write`

### create\_label parameters

| Name          | Type   | Required | Description                                                                                                                                                                       |
| ------------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`       | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`        | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `label`       | string | Yes      | Label name to create, 1-50 characters                                                                                                                                             |
| `color`       | string | No       | Six hex digits, optional leading #; defaults to ededed                                                                                                                            |
| `description` | string | No       | Label description, at most 255 characters                                                                                                                                         |

### create\_label limits

- `label` must be set.

### create\_label returns

`name`, `color`, `description`

## request\_pull\_request\_reviewers

Request reviewers (users and/or groups) on a pull request. It does not accept service accounts (`sa_…`).

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### request\_pull\_request\_reviewers parameters

| Name     | Type      | Required | Description                                                                                                                                                                       |
| -------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`  | string    | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`   | string    | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number` | number    | Yes      |                                                                                                                                                                                   |
| `users`  | string\[] | No       | User identifiers: public user\_… id or email                                                                                                                                      |
| `groups` | string\[] | No       | Group identifiers: public grp\_… id, qualified slug, or slug                                                                                                                      |

### request\_pull\_request\_reviewers limits

- `users` takes at most 100 items.
- `groups` takes at most 100 items.

### request\_pull\_request\_reviewers returns

`users` (at most 100), `groups` (at most 100)

## remove\_pull\_request\_reviewers

Remove requested reviewers from a pull request.

- **Access:** Writes content other people see
- **Asks for confirmation:** No
- **On the read-only endpoint:** No
- **Required scopes:** `repository:pull_requests:reviews:write`

### remove\_pull\_request\_reviewers parameters

| Name     | Type      | Required | Description                                                                                                                                                                       |
| -------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`  | string    | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`   | string    | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `number` | number    | Yes      |                                                                                                                                                                                   |
| `users`  | string\[] | No       | User identifiers: public user\_… id or email                                                                                                                                      |
| `groups` | string\[] | No       | Group identifiers: public grp\_… id, qualified slug, or slug                                                                                                                      |

### remove\_pull\_request\_reviewers limits

- `users` takes at most 100 items.
- `groups` takes at most 100 items.

### remove\_pull\_request\_reviewers returns

`status`: one of `completed`.

## checks\_read

Read checks for one target in an Origin-hosted repository: a pull request, commit, suite, or run. A top-level ref, sha, or pull number is accepted in place of target. Rollup covers materialized check runs on the current page only and is omitted when nextPageToken is present. Does not fetch external provider logs.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:checks:read`, `repository:pull_requests:read`

### checks\_read parameters

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

### checks\_read limits

- `pageSize` defaults to 30 and is at most 100.
- Pass the previous response's `nextPageToken` as `pageToken` to read the next page.
- `target.type` is one of `pull_request`, `commit`, `suite`, `run`.

### checks\_read returns

`rollupStatus`, `failing` (paged), `suites` (paged), `runs` (paged), `nextPageToken`

## list\_rulesets

List the rulesets on an Origin-hosted repository as summaries: id, name, kind, enforcement, included and excluded ref name patterns, the rule types present, and the bypass actor count. Rulesets past the cap are dropped and truncated is set. get\_ruleset reads one ruleset in full.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:rulesets:read`

### list\_rulesets parameters

| Name    | Type   | Required | Description                                                                                                                                                                       |
| ------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner` | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`  | string | Yes      | Origin repository name within that namespace                                                                                                                                      |

### list\_rulesets returns

`rulesets` (at most 100), `id`, `name`, `kind`, `enforcement`, `includedRefNames` (at most 64), `excludedRefNames` (at most 64), `ruleTypes` (at most 20), `bypassActorCount`, `truncated`

## get\_ruleset

Read one ruleset on an Origin-hosted repository by its id from list\_rulesets: name, description, kind, enforcement, included and excluded ref name patterns, each rule as its ruleType and JSON parameters, and each bypass actor as its kind (user, group, or app), id, and bypassMode. A group is a Cursor organization group, named by its grp\_… id; a pull\_request rule's requiredReviewers name their groups the same way.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:rulesets:read`

### get\_ruleset parameters

| Name        | Type   | Required | Description                                                                                                                                                                       |
| ----------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner`     | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`      | string | Yes      | Origin repository name within that namespace                                                                                                                                      |
| `rulesetId` | string | Yes      | Ruleset id from list\_rulesets                                                                                                                                                    |

### get\_ruleset returns

`id`, `name`, `description`, `kind`, `enforcement`, `includedRefNames` (at most 64), `excludedRefNames` (at most 64), `rules` (at most 20), `ruleType`, `parameters`, `bypassActors` (at most 15), `bypassMode`

## get\_repository\_access

Read who can access an Origin-hosted repository. teamAdmins and teamMembers are the team floor. grants has one row per user or group principal with its kind, id, display name (omitted for a user with no name), and policy names: namespacePolicy is the inherited floor, repoPolicy the repository override, and effectivePolicy the broader of the two. A layer with no grant is omitted. Grants past the cap are dropped and truncated is set.

- **Access:** Read-only
- **Asks for confirmation:** No
- **On the read-only endpoint:** Yes
- **Required scopes:** `repository:settings:read`

### get\_repository\_access parameters

| Name    | Type   | Required | Description                                                                                                                                                                       |
| ------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner` | string | Yes      | Origin namespace (owner) slug, taken from list\_namespaces or an earlier Origin result. A GitHub owner or org name is not an Origin namespace unless list\_namespaces returns it. |
| `name`  | string | Yes      | Origin repository name within that namespace                                                                                                                                      |

### get\_repository\_access returns

`teamAdmins`, `teamMembers`, `grants` (at most 100), `kind`, `id`, `display`, `namespacePolicy`, `repoPolicy`, `effectivePolicy`, `truncated`


---

## Sitemap

[Origin API docs index](https://cursor.com/docs/api/origin/llms.txt)
