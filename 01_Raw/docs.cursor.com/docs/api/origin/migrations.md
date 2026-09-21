---
source_url: https://cursor.com/docs/api/origin/migrations
fetched_at: 2026-09-21T05:44:00.814694+00:00
title: "Origin Migration API | Cursor Docs"
---

API

# Origin Migration API

Origin is in Early Beta and subject to change. Review the OpenAPI specification when updating an integration.

The Origin Migration API is for operators migrating repositories between GitHub and Origin mirrors. Call these endpoints from a migration script you run as a Cursor user, not from an Origin App.

Sign in with `origin auth login`, or pass a Cursor API key through `origin api`. See [User-authenticated CLI requests](https://cursor.com/docs/api/origin#user-authenticated-cli-requests).

The endpoints use the [Origin API](https://cursor.com/docs/api/origin) base URL, `https://api.cursor.com/v1/origin`, and the same [error model](https://cursor.com/docs/api/origin#errors).

## [Scopes](#scopes)

`repository:mirror:write`, `repository:mirror:delete`, and `repository:metadata:read` are user policy scopes. [Transition Repo Mirror](#transition-repo-mirror) and [Force Repo Mirror Cutover](#force-repo-mirror-cutover) require Write (`repository:mirror:write`). [Detach Repo Mirror](#detach-repo-mirror) requires Admin (`repository:mirror:delete`). [Get Mirror Transition Job](#get-mirror-transition-job) and [Get Active Mirror Transition Job](#get-active-mirror-transition-job) require `repository:metadata:read`. You must also administer the repository on its upstream GitHub source.

These scopes are not requestable during an Origin App installation. An Origin App cannot call these endpoints.

## [Endpoint reference](#endpoint-reference)

### [Transition Repo Mirror](#transition-repo-mirror)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/mirror:transition`

Scope[repository:mirror:write](#scopes)AuthUser access token

Starts a mirror-state transition on a mirrored repository and returns the job tracking it. The repository enters a transitioning mirror status while the job runs, so poll [Get Active Mirror Transition Job](#get-active-mirror-transition-job) or [Get Mirror Transition Job](#get-mirror-transition-job) until the job reaches a terminal status.

A repository that is not in the transition's expected start state, or that already has an active transition job, returns `FailedPrecondition` (HTTP 400). The caller must administer the repository on the mirror's upstream source; a caller without that access returns `403`.

#### [Path Parameters](#path-parameters)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body)

`transition` string Required

The mirror-state change to start. Allowed values: `initial_to_inbound`, `inbound_to_outbound`, `outbound_to_inbound`.

#### [Response Fields](#response-fields)

`repository` object

The repository, reflecting its transitioning mirror state. Carries the same fields as [Get Repo](https://cursor.com/docs/api/origin#get-repo).

`job` object

The job tracking the transition, carrying the same fields as [Get Mirror Transition Job](#get-mirror-transition-job). Poll it until it reaches a terminal status.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/mirror:transition' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "transition": "inbound_to_outbound"}'
```

**Response shape:**

```
{  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "fullName": "acme/rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    },    "defaultBranch": "main",    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T15:00:00Z",    "pushedAt": "2026-08-02T14:45:00Z",    "cloneUrl": "https://origin.cursor.com/git/acme/rocket.git",    "mirror": {      "source": "github",      "sourceId": "R_kgDOAbc123",      "status": "inbound"    }  },  "job": {    "id": "rmt_01k2ja2000e0080000000000m3",    "transition": "inbound_to_outbound",    "status": "running",    "phase": "draining-writes",    "attemptCount": 1,    "drainUntil": "2026-08-02T15:05:00Z",    "startedAt": "2026-08-02T15:00:00Z",    "createdAt": "2026-08-02T14:59:30Z",    "updatedAt": "2026-08-02T15:01:00Z"  }}
```

### [Force Repo Mirror Cutover](#force-repo-mirror-cutover)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/mirror:forceCutover`

Scope[repository:mirror:write](#scopes)AuthUser access token

Forces an `outbound_to_inbound` cutover without pushing this host's divergent state back to the upstream source. The source is adopted as the source of truth as it stands, and refs that exist only on this host are snapshotted and abandoned. Returns the job tracking the forced cutover.

Accepted only for a repository in `outbound` status, or one stuck in an outbound-to-inbound transition whose active job reports `requires_attention`, in which case that job is superseded. Any other state, including a queued or running transition job, returns `FailedPrecondition` (HTTP 400). The caller must administer the repository on the mirror's upstream source; a caller without that access returns `403`.

#### [Path Parameters](#path-parameters-1)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-1)

The request takes no fields. Send an empty JSON object.

#### [Response Fields](#response-fields-1)

`repository` object

The repository, reflecting its transitioning mirror state. Carries the same fields as [Get Repo](https://cursor.com/docs/api/origin#get-repo).

`job` object

The job tracking the transition, carrying the same fields as [Get Mirror Transition Job](#get-mirror-transition-job). Poll it until it reaches a terminal status.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/mirror:forceCutover' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{}'
```

**Response shape:**

```
{  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "fullName": "acme/rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    },    "defaultBranch": "main",    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T15:00:00Z",    "pushedAt": "2026-08-02T14:45:00Z",    "cloneUrl": "https://origin.cursor.com/git/acme/rocket.git",    "mirror": {      "source": "github",      "sourceId": "R_kgDOAbc123",      "status": "outbound"    }  },  "job": {    "id": "rmt_01k2ja2000e0080000000000m4",    "transition": "outbound_to_inbound",    "status": "running",    "phase": "snapshotting-refs",    "attemptCount": 1,    "startedAt": "2026-08-02T15:00:00Z",    "createdAt": "2026-08-02T14:59:30Z",    "updatedAt": "2026-08-02T15:01:00Z"  }}
```

### [Detach Repo Mirror](#detach-repo-mirror)

DELETE`/v1/origin/repos/{ownerSlug}/{repoName}/mirror`

Scope[repository:mirror:delete](#scopes)AuthUser access token

Permanently disconnects a mirrored repository from its upstream source. The repository keeps its current contents and becomes a native repository, syncing stops in both directions, and the mirror's deploy credential is deleted. The response body is empty.

Detaching is not reversible through this API. A repository that never had a mirror returns `FailedPrecondition` (HTTP 400); detaching an already-detached repository succeeds without effect.

#### [Path Parameters](#path-parameters-2)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Response Fields](#response-fields-2)

Successful requests return no response body.

```
curl --request DELETE \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/mirror' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response:**

```
204 No Content
```

### [Get Mirror Transition Job](#get-mirror-transition-job)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/mirror/transition-jobs/{jobId}`

Scope[repository:metadata:read](#scopes)AuthUser access token

Returns one mirror transition job by id. An unknown job id returns `404`.

#### [Path Parameters](#path-parameters-3)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`jobId` string Required

Identifier of the transition job, as returned in `job.id`.

#### [Response Fields](#response-fields-3)

`id` string

Unique identifier of the job.

`transition` string

The mirror-direction change this job performs. Allowed values: `initial_to_inbound`, `inbound_to_outbound`, `outbound_to_inbound`.

`status` string

Lifecycle state. Allowed values: `queued`, `running`, `succeeded`, `failed_rolled_back`, `requires_attention`, `superseded`. `succeeded`, `failed_rolled_back`, and `superseded` are terminal. `requires_attention` needs operator intervention or a forced cutover.

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

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/mirror/transition-jobs/JOB_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "rmt_01k2ja2000e0080000000000m3",  "transition": "inbound_to_outbound",  "status": "succeeded",  "phase": "completed",  "attemptCount": 1,  "startedAt": "2026-08-02T15:00:00Z",  "completedAt": "2026-08-02T15:12:00Z",  "createdAt": "2026-08-02T14:59:30Z",  "updatedAt": "2026-08-02T15:12:00Z"}
```

### [Get Active Mirror Transition Job](#get-active-mirror-transition-job)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/mirror/transition-jobs:active`

Scope[repository:metadata:read](#scopes)AuthUser access token

Returns the repository's currently active mirror transition job and its most recent terminal one. Both fields are optional, so a repository that has never transitioned returns an empty object. Poll this endpoint to follow a transition: once `activeJob` disappears, `lastJob` tells you how it ended.

#### [Path Parameters](#path-parameters-4)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Response Fields](#response-fields-4)

`activeJob` object

The currently active transition job, carrying the same fields as [Get Mirror Transition Job](#get-mirror-transition-job). Absent when no transition is in progress.

`lastJob` object

The most recent job that reached a terminal status, carrying the same fields as [Get Mirror Transition Job](#get-mirror-transition-job). Absent when the repository has never completed a transition.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/mirror/transition-jobs:active' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "activeJob": {    "id": "rmt_01k2ja2000e0080000000000m4",    "transition": "outbound_to_inbound",    "status": "running",    "phase": "draining-writes",    "attemptCount": 1,    "drainUntil": "2026-08-02T15:05:00Z",    "startedAt": "2026-08-02T15:00:00Z",    "createdAt": "2026-08-02T14:59:30Z",    "updatedAt": "2026-08-02T15:01:00Z"  },  "lastJob": {    "id": "rmt_01k2ja2000e0080000000000m3",    "transition": "inbound_to_outbound",    "status": "succeeded",    "phase": "completed",    "attemptCount": 1,    "startedAt": "2026-08-01T10:00:00Z",    "completedAt": "2026-08-01T10:12:00Z",    "createdAt": "2026-08-01T09:59:30Z",    "updatedAt": "2026-08-01T10:12:00Z"  }}
```

English

- English
- 简体中文
- Русский
- 日本語
- Português
- Español
