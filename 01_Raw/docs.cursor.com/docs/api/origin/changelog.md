---
source_url: https://cursor.com/docs/api/origin/changelog
fetched_at: 2026-08-24T02:18:36.138415+00:00
title: "Origin API Changelog | Cursor Docs"
---

API

# Origin API Changelog

The Origin API is in alpha and subject to change. Review the [OpenAPI specification](https://cursor.com/docs/api/origin/openapi.yaml) when updating an integration.

Changes to the Origin public API, including endpoints, request and response schemas, scopes, and webhooks, grouped by day with the newest first. Each change carries one label: **Breaking**, **Deprecated**, **Added**, **Changed**, or **Removed**. Breaking and deprecated changes include migration guidance inline. The [Origin API reference](https://cursor.com/docs/api/origin) always reflects the latest synced state.

## [August 21, 2026](#aug-21-2026)

- **Breaking.** The `recursive` query parameter on [Get Tree](https://cursor.com/docs/api/origin#get-tree) is a boolean rather than a string, so only `true` and `1` walk the whole tree; every other value, including `false`, `0`, and a bare `?recursive`, lists immediate children only. Migration: send `recursive=true` wherever your integration relied on any non-empty `recursive` value enabling recursion.
- **Breaking.** Pull request lifecycle [webhook payloads](https://cursor.com/docs/api/origin#payload-families) omit the pull request's assigned `labels`, superseding the field announced on [August 20, 2026](https://cursor.com/docs/api/origin/changelog#aug-20-2026). REST responses still carry it. Migration: read labels from [Get Pull Request](https://cursor.com/docs/api/origin#get-pull-request) or [List Pull Requests](https://cursor.com/docs/api/origin#list-pull-requests) instead of the webhook snapshot.
- **Added.** [List Rulesets](https://cursor.com/docs/api/origin#list-rulesets) returns every ruleset configured on a repository plus one shared `repository` reference: `GET /v1/origin/repos/{ownerSlug}/{repoName}/rulesets`. Rulesets are bounded configuration, so the response is not paginated. Reading rulesets requires [`repository:rulesets:read`](https://cursor.com/docs/api/origin#scopes).
- **Added.** [Create Ruleset](https://cursor.com/docs/api/origin#create-ruleset) stores a new ruleset and returns it with the IDs Origin assigns to each rule and bypass actor: `POST /v1/origin/repos/{ownerSlug}/{repoName}/rulesets`. Both ruleset write endpoints require [`repository:rulesets:write`](https://cursor.com/docs/api/origin#scopes).
- **Added.** [Get Ruleset](https://cursor.com/docs/api/origin#get-ruleset) returns a single ruleset by its stable Origin ID: `GET /v1/origin/repos/{ownerSlug}/{repoName}/rulesets/{rulesetId}`.
- **Added.** [Update Ruleset](https://cursor.com/docs/api/origin#update-ruleset) replaces a ruleset's configuration in full, including its `rules` and `bypassActors`: `PUT /v1/origin/repos/{ownerSlug}/{repoName}/rulesets/{rulesetId}`. Send every rule and bypass actor you want to keep, because the stored entries are replaced rather than merged.
- **Added.** Rulesets carry `id`, `name`, `description`, `enforcement` (`active`, `evaluate`, or `disabled`), `kind` (`merge_branch`, `push_branch`, `push_tag`, or `push_repository`), the `includedRefNames` and `excludedRefNames` patterns that accept globs plus the `~ALL` and `~DEFAULT_BRANCH` tokens, `rules`, and `bypassActors`. [Create Ruleset](https://cursor.com/docs/api/origin#create-ruleset) and [Update Ruleset](https://cursor.com/docs/api/origin#update-ruleset) reject more than 64 patterns per list, 20 rules, or 15 bypass actors with `InvalidArgument` (HTTP 400).
- **Added.** [Merge Pull Request](https://cursor.com/docs/api/origin#merge-pull-request) accepts an optional `expectedHeadSha` request field, the full commit SHA the pull request's head must match. When the head has moved, the merge is rejected with `ABORTED` (HTTP 409 Conflict) and nothing merges; a value that is not a full commit SHA is rejected with `InvalidArgument` (HTTP 400). Omit it to merge whatever the current head is.
- **Added.** Owner references carry a `type` string, `team` or `user`, omitted when Origin cannot resolve it. Returned wherever an `owner` or installation `target` appears, including [Get Repo](https://cursor.com/docs/api/origin#get-repo), [List Repos](https://cursor.com/docs/api/origin#list-repos), [List App Installations](https://cursor.com/docs/api/origin#list-app-installations), and the repository reference on check and pull request responses.

## [August 20, 2026](#aug-20-2026)

- **Breaking.** [List Pull Request Labels](https://cursor.com/docs/api/origin#list-pull-request-labels) returns every assigned label in one response and no longer paginates: the `pageSize` and `pageToken` query parameters and the `nextPageToken` response field are gone. Migration: drop `pageSize` and `pageToken` from the request and read the full set from `labels`.
- **Breaking.** A pull request holds at most 100 labels, and [Add Pull Request Labels](https://cursor.com/docs/api/origin#add-pull-request-labels) and [Set Pull Request Labels](https://cursor.com/docs/api/origin#set-pull-request-labels) reject a write that would take it past that limit with `FailedPrecondition` (HTTP 400). Migration: keep each pull request at or under 100 labels, removing labels before adding more.
- **Added.** Pull requests carry a `labels` array of the labels assigned to them, sorted by name and empty when none are assigned. Returned by [List Pull Requests](https://cursor.com/docs/api/origin#list-pull-requests), [Get Pull Request](https://cursor.com/docs/api/origin#get-pull-request), [Create Pull Request](https://cursor.com/docs/api/origin#create-pull-request), [Update Pull Request](https://cursor.com/docs/api/origin#update-pull-request), and [Merge Pull Request](https://cursor.com/docs/api/origin#merge-pull-request), and included on pull request lifecycle [webhook payloads](https://cursor.com/docs/api/origin#payload-families).

## [August 19, 2026](#aug-19-2026)

- **Added.** [List Pull Request Labels](https://cursor.com/docs/api/origin#list-pull-request-labels) returns the labels assigned to a pull request, ordered by name: `GET /v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/labels`. Requires [`repository:pull_requests:read`](https://cursor.com/docs/api/origin#scopes). Results are paginated, 30 labels per page by default, and at most 100 labels per page.
- **Added.** [Add Pull Request Labels](https://cursor.com/docs/api/origin#add-pull-request-labels) assigns existing repository labels to a pull request and leaves the labels already on it in place: `POST /v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/labels`. Every label write endpoint requires [`repository:pull_requests:write`](https://cursor.com/docs/api/origin#scopes).
- **Added.** [Set Pull Request Labels](https://cursor.com/docs/api/origin#set-pull-request-labels) replaces every label on a pull request with the names you send, and an empty list clears them: `PUT /v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/labels`.
- **Added.** [Remove Pull Request Label](https://cursor.com/docs/api/origin#remove-pull-request-label) removes one label by name and returns the labels left on the pull request: `DELETE /v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/labels/{labelName}`.
- **Added.** [Remove All Pull Request Labels](https://cursor.com/docs/api/origin#remove-all-pull-request-labels) clears every label from a pull request and returns `204`: `DELETE /v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/labels`.
- **Added.** Label entries carry `id`, `name`, `color` as a six-character hex value without a leading `#`, and an optional `description`. Returned by every pull request label endpoint.
- **Changed.** The [app JWT rate limit](https://cursor.com/docs/api/origin#rate-limits) budget rose from 600 to 6,000 points per minute, and [Create Installation Access Token](https://cursor.com/docs/api/origin#create-installation-access-token) charges 1 point instead of 5, so an app can mint roughly 100 installation tokens per second.
- **Changed.** Owner eligibility for [Create Repo](https://cursor.com/docs/api/origin#create-repo) and pushes over [Git HTTPS](https://cursor.com/docs/api/origin#git-https-authentication) admits the Pro Student and Start plans alongside Pro, Pro+, and Ultra. Team-owner requirements are unchanged.
- **Changed.** Owner slugs and repository names in [repository paths](https://cursor.com/docs/api/origin#repository-paths) resolve case-insensitively, and responses return the stored casing rather than the casing you sent. [Create Repo](https://cursor.com/docs/api/origin#create-repo) rejects a name that differs only in case from one the owner already has, so compare repository names case-insensitively.

## [August 17, 2026](#aug-17-2026)

- **Breaking.** [Git over HTTPS](https://cursor.com/docs/api/origin#git-https-authentication) rejects a push with `403` when the repository's owner is not eligible to write to Origin. A user owner must be on a Pro, Pro+, or Ultra plan, and a team owner must have an active paid team plan, must not be on Privacy Mode (Legacy), and must not have Origin turned off by a team admin. Clone, fetch, and pull are unaffected. Migration: handle `403` on push as an owner-eligibility failure that a retry cannot clear, and confirm the owner's plan before pushing on its behalf.
- **Changed.** The first push to a repo created through [Create Repo](https://cursor.com/docs/api/origin#create-repo) retargets `defaultBranch` when that push only creates branches and none of them is the stored default: Origin picks the created branch, or `main` or `master` when the push creates several and one of those names is among them. Read the current value from [Get Repo](https://cursor.com/docs/api/origin#get-repo).

## [August 16, 2026](#aug-16-2026)

- **Breaking.** [Create Repo](https://cursor.com/docs/api/origin#create-repo) rejects a request whose owner is not eligible to write to Origin, returning `FailedPrecondition` (HTTP 400). A user owner must be on a Pro, Pro+, or Ultra plan, and a team owner must have an active paid team plan, must not be on Privacy Mode (Legacy), and must not have Origin turned off by a team admin. Migration: handle `400` from [Create Repo](https://cursor.com/docs/api/origin#create-repo) as an owner-eligibility failure that a retry cannot clear, and confirm the owner's plan before creating repositories on its behalf.

## [August 15, 2026](#aug-15-2026)

- **Breaking.** Apps lost access to repositories that Origin mirrors in from GitHub. Those repositories no longer appear in [List App Installation Repositories](https://cursor.com/docs/api/origin#list-app-installation-repositories), [Create Installation Access Token](https://cursor.com/docs/api/origin#create-installation-access-token) rejects them in `repositoryIds`, and a request that names one returns `403` over both the REST API and [Git over HTTPS](https://cursor.com/docs/api/origin#git-https-authentication). Migration: discover repositories from [List App Installation Repositories](https://cursor.com/docs/api/origin#list-app-installation-repositories) instead of a stored repository list, and read a GitHub-sourced repository from GitHub rather than the Origin API.
- **Breaking.** Origin stopped sending webhooks for repositories it mirrors in from GitHub, and installation event payloads dropped those repositories from their selected repository arrays and `repositoriesCount`. Migration: source [events](https://cursor.com/docs/api/origin#events) for a GitHub-sourced repository from GitHub, and treat an installation payload's repository array as the set your app can reach.

## [August 14, 2026](#aug-14-2026)

- **Changed.** Revision parameters accept the symbolic `HEAD` alongside a SHA, branch, or tag: `sha` on [List Commits](https://cursor.com/docs/api/origin#list-commits), [Get Commit](https://cursor.com/docs/api/origin#get-commit), [List Commit Files](https://cursor.com/docs/api/origin#list-commit-files), [Get Git Commit](https://cursor.com/docs/api/origin#get-git-commit), and [Get Tree](https://cursor.com/docs/api/origin#get-tree); `ref` on [Get Contents](https://cursor.com/docs/api/origin#get-contents) and [Batch Get Contents](https://cursor.com/docs/api/origin#batch-get-contents); and either side of `basehead` on [Compare Commits](https://cursor.com/docs/api/origin#compare-commits).
- **Changed.** [Get Git Ref](https://cursor.com/docs/api/origin#get-git-ref) resolves the symbolic `HEAD` and returns it as `ref: "HEAD"` with the tip commit. [List Matching Git Refs](https://cursor.com/docs/api/origin#list-matching-git-refs) and [List Matching Git Refs by Path](https://cursor.com/docs/api/origin#list-matching-git-refs-by-path) match `HEAD` exactly, because it does not sit under `refs/`.
- **Changed.** Removing an installation, or deleting the app, invalidates that installation's access tokens before `expiresAt`. The REST API and [Git over HTTPS](https://cursor.com/docs/api/origin#git-https-authentication) reject a revoked token with `401`, so an app must be reinstalled before it can mint a working one. See [Installation access token](https://cursor.com/docs/api/origin#installation-access-token).

## [August 13, 2026](#aug-13-2026)

- **Breaking.** [Get Contents](https://cursor.com/docs/api/origin#get-contents) rejects files larger than 1 MiB (decoded) with `FailedPrecondition` (HTTP 400), and one oversized file fails an entire [Batch Get Contents](https://cursor.com/docs/api/origin#batch-get-contents) request.
- **Added.** Installation access tokens authenticate Git over HTTPS. Use the token as the HTTP Basic password with username `x-access-token` against the repository `cloneUrl`. Clone, fetch, and pull require [`repository:contents:read`](https://cursor.com/docs/api/origin#scopes); push requires [`repository:contents:write`](https://cursor.com/docs/api/origin#scopes). See [Git HTTPS authentication](https://cursor.com/docs/api/origin#git-https-authentication).
- **Changed.** `cloneUrl` carries the GitHub-shaped root path (`https://origin.cursor.com/OWNER_SLUG/REPO_NAME.git`) in place of the legacy `/git/` path, on [List Repos](https://cursor.com/docs/api/origin#list-repos), [Get Repo](https://cursor.com/docs/api/origin#get-repo), [Create Repo](https://cursor.com/docs/api/origin#create-repo), [List App Installation Repositories](https://cursor.com/docs/api/origin#list-app-installation-repositories), and the [`repository.created`](https://cursor.com/docs/api/origin#events) webhook payload. Both forms clone and `cloneUrl` promises no particular path shape, so a stored value keeps working.
- **Changed.** `size` on [Get Contents](https://cursor.com/docs/api/origin#get-contents) and [Batch Get Contents](https://cursor.com/docs/api/origin#batch-get-contents) responses states the decoded content size in bytes, not the length of the base64 `content` string.

## [August 11, 2026](#aug-11-2026)

- **Breaking.** Reviewer webhook payloads carry a stable external ID in `reviewer.id`: the encoded user ID (`user_…`, the same format as the organization API) when `kind` is `user`, replacing the provider-scoped auth ID; group reviewers keep the group public ID (`grp_…`). Affects [`pull_request.reviewer.added`](https://cursor.com/docs/api/origin#events), [`pull_request.reviewer.removed`](https://cursor.com/docs/api/origin#events), and [`pull_request.reviewer.rerequested`](https://cursor.com/docs/api/origin#events). Migration: match user reviewers by the encoded `user_…` ID wherever your integration compared `reviewer.id` against stored auth IDs.
- **Added.** Apps can hold up to 10 active Ed25519 signing keys, and [app JWT](https://cursor.com/docs/api/origin#app-jwt) verification accepts a token signed with any active key.
- **Added.** [Sync Mirror](https://cursor.com/docs/api/origin#sync-mirror) synchronizes one ref of a mirrored repository from its upstream source: `POST /v1/origin/repos/{ownerSlug}/{repoName}:syncMirror`. Requires [`repository:contents:read`](https://cursor.com/docs/api/origin#scopes) and returns `200` when the sync target is satisfied or `202` while the sync is pending.
- **Added.** Post-install redirects carry an `installation_receipt` query parameter: a five-minute Origin-signed JWT that identifies the installation in its `sub` claim and echoes the publisher's `state` as a claim. Verify it against the published JWKS before trusting the callback. See [Installation receipt](https://cursor.com/docs/api/origin#installation-receipt).
- **Removed.** Origin actor objects no longer include the top-level `kind` and `id` fields, completing the deprecation announced on [August 5, 2026](https://cursor.com/docs/api/origin/changelog#aug-5-2026). Every `actor`, `author`, and `dismissedBy` field across check, commit, and pull request responses is affected. Migration: read the `user`, `app`, or `serviceAccount` variant set on the actor.

## [August 10, 2026](#aug-10-2026)

- **Added.** [Get Rate Limit](https://cursor.com/docs/api/origin#get-rate-limit) returns the authenticated principal's shared per-minute point budget without consuming points: `GET /v1/origin/rate_limit`. See [Rate limits](https://cursor.com/docs/api/origin#rate-limits).

## [August 5, 2026](#aug-5-2026)

- **Deprecated.** `OriginActor.kind` and `OriginActor.id`. Actor identity is a discriminated union of `user`, `app`, and `serviceAccount` variants. Migration: read the selected variant's fields instead of top-level `kind` and `id`.

English

- English
- 简体中文
- Русский
- 日本語
- Português
- Español
