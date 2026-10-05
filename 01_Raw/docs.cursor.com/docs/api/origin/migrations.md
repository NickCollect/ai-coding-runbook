---
source_url: https://cursor.com/docs/api/origin/migrations
fetched_at: 2026-10-05T06:27:19.011995+00:00
fetch_method: mintlify_md
---

# Origin Migration API

Origin is in Early Beta and subject to change. Review the OpenAPI specification when updating an integration.

The Origin Migration API is for operators migrating repositories between GitHub and Origin mirrors. Call these endpoints from a migration script you run as a Cursor user, not from an Origin App.

Sign in with `origin auth login`, or pass a Cursor API key through `origin api`. See [User-authenticated CLI requests](https://cursor.com/docs/api/origin/reference/user-authenticated-cli-requests.md).

The endpoints use the [Origin API](https://cursor.com/docs/api/origin.md) base URL, `https://api.cursor.com/v1/origin`, and the same [error model](https://cursor.com/docs/api/origin/reference/errors.md).

## Scopes

`repository:mirror:write`, `repository:mirror:delete`, and `repository:metadata:read` are user policy scopes. [Transition Repo Mirror](https://cursor.com/docs/api/origin/migrations.md#transition-repo-mirror) requires Write (`repository:mirror:write`). [Detach Repo Mirror](https://cursor.com/docs/api/origin/migrations.md#detach-repo-mirror) requires Admin (`repository:mirror:delete`). [Get Mirror Transition Job](https://cursor.com/docs/api/origin/migrations.md#get-mirror-transition-job) and [Get Active Mirror Transition Job](https://cursor.com/docs/api/origin/migrations.md#get-active-mirror-transition-job) require `repository:metadata:read`. You must also administer the repository on its upstream GitHub source.

These scopes are not requestable during an Origin App installation. An Origin App cannot call these endpoints.

## Endpoint reference

### Transition Repo Mirror

POST

`/v1/origin/repos/{ownerSlug}/{repoName}/mirror:transition`

Requires scope `repository:mirror:write` (user access token).

Starts a mirror-state transition on a mirrored repository and returns the job tracking it. The repository enters a transitioning mirror status while the job runs, so poll [Get Active Mirror Transition Job](https://cursor.com/docs/api/origin/migrations.md#get-active-mirror-transition-job) or [Get Mirror Transition Job](https://cursor.com/docs/api/origin/migrations.md#get-mirror-transition-job) until the job reaches a terminal status.

A repository that is not in the transition's expected start state, or that already has an active transition job, returns `FailedPrecondition` (HTTP 400). The caller must administer the repository on the mirror's upstream source; a caller without that access returns `403`.

#### Path Parameters

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### Request Body

`transition` string Required

The mirror-state change to start. Allowed values: `initial_to_inbound`, which retries a mirror whose initial sync failed and brings it to `inbound`.

#### Response Fields

`repository` object

The repository, reflecting its transitioning mirror state. Carries the same fields as [Get Repo](https://cursor.com/docs/api/origin/reference/get-repo.md).

`job` object

The job tracking the transition, carrying the same fields as [Get Mirror Transition Job](https://cursor.com/docs/api/origin/migrations.md#get-mirror-transition-job). Poll it until it reaches a terminal status.

```bash
curl --request POST \
  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/mirror:transition' \
  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \
  --header 'Content-Type: application/json' \
  --data '{
  "transition": "initial_to_inbound"
}'
```

**Response shape:**

```json
{
  "repository": {
    "id": "repo_01k2ja2000e0080000000000q4",
    "name": "rocket",
    "fullName": "acme/rocket",
    "owner": {
      "slug": "acme",
      "id": "ns_01k2ja2000e0080000000000p3",
      "type": "team"
    },
    "defaultBranch": "main",
    "createdAt": "2026-08-01T09:30:00Z",
    "updatedAt": "2026-08-02T15:00:00Z",
    "pushedAt": "2026-08-02T14:45:00Z",
    "cloneUrl": "https://origin.cursor.com/git/acme/rocket.git",
    "mirror": {
      "source": "github",
      "sourceId": "R_kgDOAbc123",
      "status": "inbound"
    }
  },
  "job": {
    "id": "rmt_01k2ja2000e0080000000000m3",
    "transition": "initial_to_inbound",
    "status": "running",
    "phase": "initializing-mirror-fetch",
    "attemptCount": 1,
    "startedAt": "2026-08-02T15:00:00Z",
    "createdAt": "2026-08-02T14:59:30Z",
    "updatedAt": "2026-08-02T15:01:00Z"
  }
}
```

### Detach Repo Mirror

DELETE

`/v1/origin/repos/{ownerSlug}/{repoName}/mirror`

Requires scope `repository:mirror:delete` (user access token).

Permanently disconnects a mirrored repository from its upstream source. The repository keeps its current contents and becomes a native repository, syncing stops in both directions, and the mirror's deploy credential is deleted. The response body is empty.

Detaching is not reversible through this API. A repository that never had a mirror returns `FailedPrecondition` (HTTP 400); detaching an already-detached repository succeeds without effect.

#### Path Parameters

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### Response Fields

Successful requests return no response body.

```bash
curl --request DELETE \
  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/mirror' \
  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response:**

```text
204 No Content
```

### Get Mirror Transition Job

GET

`/v1/origin/repos/{ownerSlug}/{repoName}/mirror/transition-jobs/{jobId}`

Requires scope `repository:metadata:read` (user access token).

Returns one mirror transition job by id. An unknown job id returns `404`.

#### Path Parameters

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`jobId` string Required

Identifier of the transition job, as returned in `job.id`.

#### Response Fields

`id` string

Unique identifier of the job.

`transition` string

The mirror-direction change this job performs. Allowed values: `initial_to_inbound`.

`status` string

Lifecycle state. Allowed values: `queued`, `running`, `succeeded`, `failed_rolled_back`, `requires_attention`, `superseded`. `succeeded`, `failed_rolled_back`, and `superseded` are terminal. `requires_attention` needs operator intervention.

`phase` string

Progress detail within `status`, for display and debugging. One of `queued`, `starting`, `draining-writes`, `initializing-mirror-fetch`, `finalizing-mirror-fetch`, `finalizing-mirror-push`, `snapshotting-refs`, `verifying-integrity`, `reopening-inbound-mirror`, `committing-target-status`, `rolling-back`, or `completed`. New phases can appear as the transition process evolves, so poll `status` for completion rather than matching on phases.

`attemptCount` integer

Number of times this job has been attempted.

`drainUntil` string

RFC 3339 timestamp of when the write-drain window of an in-progress transition ends. Absent outside the draining phase.

`lastErrorCode` string

Stable code identifying why the job last failed, such as `InboundMirrorDrainTimeout` or `MirrorIntegrityMismatch`. Absent while the job has not failed.

`lastErrorMessage` string

Human-readable detail for `lastErrorCode`. Absent while the job has not failed.

`startedAt` string

RFC 3339 timestamp of when the job started running. Absent while queued.

`completedAt` string

RFC 3339 timestamp of when the job reached a terminal status. Absent until then.

`createdAt` string

RFC 3339 job creation timestamp.

`updatedAt` string

RFC 3339 job update timestamp.

```bash
curl --request GET \
  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/mirror/transition-jobs/JOB_ID' \
  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```json
{
  "id": "rmt_01k2ja2000e0080000000000m3",
  "transition": "initial_to_inbound",
  "status": "succeeded",
  "phase": "completed",
  "attemptCount": 1,
  "startedAt": "2026-08-02T15:00:00Z",
  "completedAt": "2026-08-02T15:12:00Z",
  "createdAt": "2026-08-02T14:59:30Z",
  "updatedAt": "2026-08-02T15:12:00Z"
}
```

### Get Active Mirror Transition Job

GET

`/v1/origin/repos/{ownerSlug}/{repoName}/mirror/transition-jobs:active`

Requires scope `repository:metadata:read` (user access token).

Returns the repository's currently active mirror transition job and its most recent terminal one. Both fields are optional, so a repository that has never transitioned returns an empty object. Poll this endpoint to follow a transition: once `activeJob` disappears, `lastJob` tells you how it ended.

#### Path Parameters

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### Response Fields

`activeJob` object

The currently active transition job, carrying the same fields as [Get Mirror Transition Job](https://cursor.com/docs/api/origin/migrations.md#get-mirror-transition-job). Absent when no transition is in progress.

`lastJob` object

The most recent job that reached a terminal status, carrying the same fields as [Get Mirror Transition Job](https://cursor.com/docs/api/origin/migrations.md#get-mirror-transition-job). Absent when the repository has never completed a transition.

```bash
curl --request GET \
  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/mirror/transition-jobs:active' \
  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```json
{
  "activeJob": {
    "id": "rmt_01k2ja2000e0080000000000m4",
    "transition": "initial_to_inbound",
    "status": "running",
    "phase": "initializing-mirror-fetch",
    "attemptCount": 2,
    "startedAt": "2026-08-02T15:00:00Z",
    "createdAt": "2026-08-02T14:59:30Z",
    "updatedAt": "2026-08-02T15:01:00Z"
  },
  "lastJob": {
    "id": "rmt_01k2ja2000e0080000000000m3",
    "transition": "initial_to_inbound",
    "status": "failed-rolled-back",
    "phase": "completed",
    "attemptCount": 1,
    "startedAt": "2026-08-01T10:00:00Z",
    "completedAt": "2026-08-01T10:12:00Z",
    "createdAt": "2026-08-01T09:59:30Z",
    "updatedAt": "2026-08-01T10:12:00Z"
  }
}
```


---

## Sitemap

[Origin API docs index](https://cursor.com/docs/api/origin/llms.txt)
