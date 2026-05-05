---
source_url: https://cursor.com/docs/cloud-agent/api/endpoints
---

# Cloud Agents API

### Public beta

The Cloud Agents API v1 is in public beta. APIs may change before general
availability.

The Cloud Agents API lets you programmatically launch and manage cloud agents that work on your repositories.

- The Cloud Agents API uses [Basic Authentication](https://cursor.com/docs/api.md#authentication). Generate a user API key from [Cursor Dashboard → Integrations](https://cursor.com/dashboard/integrations), or use a [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md).
- For details on authentication methods, rate limits, and best practices, see the [API Overview](https://cursor.com/docs/api.md).
- View the full [OpenAPI specification](/docs-static/cloud-agents-openapi.yaml) for detailed schemas and examples.
- Webhooks are coming soon. The legacy [v0 API](https://cursor.com/docs/cloud-agent/api/v0.md) still supports them — see [Webhooks](https://cursor.com/docs/cloud-agent/api/webhooks.md).

### Migrating from v0?

This API splits work into a durable agent plus per-prompt runs, replacing the flatter v0 surface. The legacy [v0 reference](https://cursor.com/docs/cloud-agent/api/v0.md) remains available.

## Endpoints

### Create An Agent

/v1/agents

Create a Cloud Agent and immediately enqueue its initial run. The response returns both the durable `agent` and the initial `run`.

#### Request Body

`prompt` object (required)

The task prompt for the agent, including optional images.

`prompt.text` string (required)

The instruction text for the agent.

`prompt.images` array (optional)

Array of base64-encoded image inputs. Maximum 5 images, 15 MB each.

`model` object (optional)

Model selection. Omit this field to use the configured default. When omitted, Cursor resolves your user default model, then your team default model, then a system default.

`model.id` string (required if `model` provided)

An explicit model ID returned by `GET /v1/models` (for example, `claude-4-sonnet-thinking`).

`model.params` array (optional)

Per-model parameters to apply to the run, such as reasoning effort or max mode. Each item has an `id` and `value`. Use only parameters supported by the selected model.

`repos` array (required)

Repository configuration. v1 currently supports one repository.

`repos[0].url` string (required unless `prUrl` is provided)

GitHub repository URL (for example, `https://github.com/your-org/your-repo`).

`repos[0].startingRef` string (optional)

Branch, tag, or commit hash to use as the starting point.

`repos[0].prUrl` string (optional)

GitHub pull request URL. When provided, the agent works on this PR's repository and branches; `url` and `startingRef` are ignored.

`branchName` string (optional)

Custom branch name for the agent to create.

`autoGenerateBranch` boolean (optional, default: true)

Whether to create a new branch (`true`) or push to an existing head branch (`false`). Only applies when `repos[0].prUrl` is provided.

`autoCreatePR` boolean (optional)

Whether Cursor should open a pull request when the run completes.

`skipReviewerRequest` boolean (optional)

Whether to skip requesting the user as a reviewer when Cursor opens a PR. Only applies when `autoCreatePR` is `true`.

`envVars` object (optional)

Session-scoped environment variables for the cloud agent. Values are encrypted at rest, injected into the agent's shell, and deleted with the agent. Names can't start with `CURSOR_`.

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
    "prompt": {
      "text": "Add a README with setup instructions"
    },
    "model": {
      "id": "composer-2",
      "params": [
        { "id": "thinking", "value": "high" }
      ]
    },
    "repos": [
      {
        "url": "https://github.com/your-org/your-repo",
        "startingRef": "main"
      }
    ],
    "autoCreatePR": true
  }'
```

**Response:**

```json
{
  "agent": {
    "id": "bc-00000000-0000-0000-0000-000000000001",
    "name": "Add README with setup instructions",
    "status": "ACTIVE",
    "env": {
      "type": "cloud"
    },
    "repos": [
      {
        "url": "https://github.com/your-org/your-repo",
        "startingRef": "main"
      }
    ],
    "branchName": "cursor/add-readme",
    "autoGenerateBranch": true,
    "autoCreatePR": true,
    "url": "https://cursor.com/agents?id=bc-00000000-0000-0000-0000-000000000001",
    "createdAt": "2026-04-13T18:30:00.000Z",
    "updatedAt": "2026-04-13T18:30:00.000Z",
    "latestRunId": "run-00000000-0000-0000-0000-000000000001"
  },
  "run": {
    "id": "run-00000000-0000-0000-0000-000000000001",
    "agentId": "bc-00000000-0000-0000-0000-000000000001",
    "status": "CREATING",
    "createdAt": "2026-04-13T18:30:00.000Z",
    "updatedAt": "2026-04-13T18:30:00.000Z"
  }
}
```

### List Agents

/v1/agents

List agents for the authenticated user, newest first.

#### Query Parameters

`limit` number (optional)

Number of agents to return. Default: 20, Max: 100.

`cursor` string (optional)

Pagination cursor from `nextCursor` on the previous response.

`prUrl` string (optional)

Filter agents by GitHub pull request URL.

`includeArchived` boolean (optional, default: true)

Whether to include archived agents in the response.

List items only include the durable identity fields. Call `GET /v1/agents/{id}` to load the full record (`repos`, `branchName`, `autoCreatePR`, etc.).

```bash
curl --request GET \
  --url 'https://api.cursor.com/v1/agents?limit=20' \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "id": "bc-00000000-0000-0000-0000-000000000001",
      "name": "Add README with setup instructions",
      "status": "ACTIVE",
      "env": {
        "type": "cloud"
      },
      "url": "https://cursor.com/agents?id=bc-00000000-0000-0000-0000-000000000001",
      "createdAt": "2026-04-13T18:30:00.000Z",
      "updatedAt": "2026-04-13T18:45:00.000Z",
      "latestRunId": "run-00000000-0000-0000-0000-000000000001"
    }
  ],
  "nextCursor": "bc-00000000-0000-0000-0000-000000000002"
}
```

### Get An Agent

/v1/agents/

Retrieve durable metadata for an agent. Execution status lives on runs — fetch `latestRunId` and call [Get A Run](https://cursor.com/docs/cloud-agent/api/endpoints.md#get-a-run) to read run state.

#### Path Parameters

`id` string

Unique identifier for the agent (for example, `bc-00000000-0000-0000-0000-000000000001`).

```bash
curl --request GET \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001 \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "id": "bc-00000000-0000-0000-0000-000000000001",
  "name": "Add README with setup instructions",
  "status": "ACTIVE",
  "env": {
    "type": "cloud"
  },
  "repos": [
    {
      "url": "https://github.com/your-org/your-repo",
      "startingRef": "main"
    }
  ],
  "branchName": "cursor/add-readme",
  "autoGenerateBranch": true,
  "autoCreatePR": true,
  "url": "https://cursor.com/agents?id=bc-00000000-0000-0000-0000-000000000001",
  "createdAt": "2026-04-13T18:30:00.000Z",
  "updatedAt": "2026-04-13T18:30:00.000Z",
  "latestRunId": "run-00000000-0000-0000-0000-000000000001"
}
```

### Create A Run

/v1/agents//runs

Send a follow-up prompt to an existing active agent. The new run uses the agent's current conversation and workspace state.

Only one run can be active per agent. Calling this while another run is `CREATING` or `RUNNING` returns `409 agent_busy`. Wait for the existing run to terminate, or cancel it.

#### Path Parameters

`id` string

Unique identifier for the agent (for example, `bc-00000000-0000-0000-0000-000000000001`).

#### Request Body

`prompt` object (required)

The follow-up prompt, including optional images.

`prompt.text` string (required)

The follow-up instruction text.

`prompt.images` array (optional)

Array of base64-encoded image inputs. Maximum 5 images, 15 MB each.

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/runs \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
    "prompt": {
      "text": "Also add troubleshooting steps"
    }
  }'
```

**Response:**

```json
{
  "run": {
    "id": "run-00000000-0000-0000-0000-000000000002",
    "agentId": "bc-00000000-0000-0000-0000-000000000001",
    "status": "CREATING",
    "createdAt": "2026-04-13T18:50:00.000Z",
    "updatedAt": "2026-04-13T18:50:00.000Z"
  }
}
```

### List Runs

/v1/agents//runs

List runs for an agent, newest first.

#### Path Parameters

`id` string

Unique identifier for the agent.

#### Query Parameters

`limit` number (optional)

Number of runs to return. Default: 20, Max: 100.

`cursor` string (optional)

Pagination cursor from `nextCursor` on the previous response.

```bash
curl --request GET \
  --url 'https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/runs?limit=20' \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "id": "run-00000000-0000-0000-0000-000000000002",
      "agentId": "bc-00000000-0000-0000-0000-000000000001",
      "status": "RUNNING",
      "createdAt": "2026-04-13T18:50:00.000Z",
      "updatedAt": "2026-04-13T18:51:00.000Z"
    }
  ],
  "nextCursor": null
}
```

### Get A Run

/v1/agents//runs/

Retrieve status and timestamps for a specific run.

#### Path Parameters

`id` string

Unique identifier for the agent.

`runId` string

Unique identifier for the run (for example, `run-00000000-0000-0000-0000-000000000001`).

```bash
curl --request GET \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/runs/run-00000000-0000-0000-0000-000000000001 \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "id": "run-00000000-0000-0000-0000-000000000001",
  "agentId": "bc-00000000-0000-0000-0000-000000000001",
  "status": "FINISHED",
  "createdAt": "2026-04-13T18:30:00.000Z",
  "updatedAt": "2026-04-13T18:45:00.000Z"
}
```

### Stream A Run

/v1/agents//runs//stream

Stream Server-Sent Events (SSE) for one run. The stream is scoped to the requested run and does not replay prior runs.

#### Event types

- `status` — run status update. Payload: `{ runId, status }`.
- `assistant` — assistant text delta. Payload: `{ text }`.
- `thinking` — thinking text delta. Payload: `{ text }`.
- `tool_call` — tool call status update.
- `heartbeat` — keepalive event.
- `result` — terminal run status. Payload: `{ runId, status }`.
- `error` — stream error. Payload: `{ code, message }`.
- `done` — stream complete. Payload: `{}`.

#### Resuming a stream

SSE responses include `id` values when available. To resume after a disconnect, reconnect with `Last-Event-ID` set to the most recent received event id. The event id must belong to the requested run; otherwise the request returns `400 invalid_last_event_id`.

#### Retention

Stream responses include the `X-Cursor-Stream-Retention-Seconds` header. After the retention window elapses, this endpoint may return `410 stream_expired`. Treat that as a signal to read terminal state via [Get A Run](https://cursor.com/docs/cloud-agent/api/endpoints.md#get-a-run) instead of retrying the stream.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/runs/run-00000000-0000-0000-0000-000000000001/stream \
  -u YOUR_API_KEY: \
  --header 'Accept: text/event-stream'
```

**Example stream:**

```text
event: status
data: {"runId":"run-00000000-0000-0000-0000-000000000001","status":"RUNNING"}

id: 1713033000000-0
event: assistant
data: {"text":"I'll update the README now."}

id: 1713033010000-0
event: result
data: {"runId":"run-00000000-0000-0000-0000-000000000001","status":"FINISHED"}

id: 1713033010000-0
event: done
data: {}
```

### Cancel A Run

/v1/agents//runs//cancel

Cancel the active run for an agent. Cancellation is terminal — the run transitions to `CANCELLED` and cannot be resumed. To continue the conversation, create a new run on the same agent.

Cancelling a run that is already in a terminal state, or one that was never active, returns `409 run_not_cancellable`.

#### Path Parameters

`id` string

Unique identifier for the agent.

`runId` string

Unique identifier for the run to cancel.

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/runs/run-00000000-0000-0000-0000-000000000001/cancel \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "id": "run-00000000-0000-0000-0000-000000000001"
}
```

## Artifacts

Artifacts are agent-scoped because the workspace persists across runs.

### List Artifacts

/v1/agents//artifacts

List artifacts produced by an agent. Each artifact's `path` is relative to the workspace's `artifacts/` directory.

Pass the `path` value returned here directly to [Download An Artifact](https://cursor.com/docs/cloud-agent/api/endpoints.md#download-an-artifact). v1 paths are relative; absolute v0 paths (`/opt/cursor/artifacts/...`) are not accepted.

#### Path Parameters

`id` string

Unique identifier for the agent.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/artifacts \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "path": "artifacts/screenshot.png",
      "sizeBytes": 12345,
      "updatedAt": "2026-04-13T18:45:00.000Z"
    }
  ]
}
```

### Download An Artifact

/v1/agents//artifacts/download

Retrieve a temporary 15-minute presigned S3 URL for a specific artifact.

#### Path Parameters

`id` string

Unique identifier for the agent.

#### Query Parameters

`path` string

Relative artifact path returned by [List Artifacts](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-artifacts) (for example, `artifacts/screenshot.png`). Must be under `artifacts/`.

```bash
curl --request GET \
  --url 'https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/artifacts/download?path=artifacts/screenshot.png' \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "url": "https://cloud-agent-artifacts.s3.us-east-1.amazonaws.com/...",
  "expiresAt": "2026-04-13T19:00:00.000Z"
}
```

## Agent Lifecycle

### Archive An Agent

/v1/agents//archive

Archive an agent. Archived agents remain readable but cannot accept new runs until unarchived. Use this for reversible "soft delete" flows.

#### Path Parameters

`id` string

Unique identifier for the agent.

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/archive \
  -u YOUR_API_KEY:
```

### Unarchive An Agent

/v1/agents//unarchive

Unarchive an agent so it can accept new runs again.

#### Path Parameters

`id` string

Unique identifier for the agent.

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/unarchive \
  -u YOUR_API_KEY:
```

### Delete An Agent Permanently

/v1/agents/

Permanently delete an agent. This action is irreversible. Use [Archive](https://cursor.com/docs/cloud-agent/api/endpoints.md#archive-an-agent) for reversible removal.

#### Path Parameters

`id` string

Unique identifier for the agent.

```bash
curl --request DELETE \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001 \
  -u YOUR_API_KEY:
```

## Worker Tokens

### Create A User-Scoped Worker Token

/v1/sub-tokens

Create a one-hour user-scoped token for a [My Machines](https://cursor.com/docs/cloud-agent/my-machines.md) worker to run as an active team member.

Requires an agent-scoped team service account API key. User-scoped tokens can't mint other user-scoped tokens.

The returned token expires after 1 hour and cannot refresh itself. Mint a new token with the service account API key when you need to refresh a running worker.

#### Request Body

Specify exactly one of the following to identify the target user:

`forUserEmail` string (optional)

Active team member email. Case-insensitive.

`forUserId` integer (optional)

Active team member's numeric Cursor user ID.

By email:

```bash
curl --request POST \
  --url https://api.cursor.com/v1/sub-tokens \
  --header "Authorization: Bearer $CURSOR_SERVICE_ACCOUNT_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "forUserEmail": "alice@company.com"
  }'
```

By user ID:

```bash
curl --request POST \
  --url https://api.cursor.com/v1/sub-tokens \
  --header "Authorization: Bearer $CURSOR_SERVICE_ACCOUNT_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "forUserId": 42
  }'
```

**Response:**

```json
{
  "accessToken": "eyJ...",
  "expiresAt": "2026-04-24T19:00:00.000Z",
  "userId": 42,
  "teamId": 456
}
```

## Metadata Endpoints

### API Key Info

/v1/me

Retrieve information about the API key being used for authentication.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/me \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "apiKeyName": "Production API Key",
  "createdAt": "2026-04-13T18:30:00.000Z",
  "userEmail": "developer@example.com"
}
```

### List Models

/v1/models

Returns a recommended set of explicit model IDs you can pass to the `model.id` field on [Create An Agent](https://cursor.com/docs/cloud-agent/api/endpoints.md#create-an-agent). Model parameters use the same `model.params` shape as the [TypeScript SDK ModelSelection](https://cursor.com/docs/sdk/typescript.md#modelselection).

To use the configured default model, omit `model` from the request body. Cursor resolves your user default model, then your team default model, then a system default.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/models \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    "claude-4-sonnet-thinking",
    "gpt-5.2",
    "claude-4.5-sonnet-thinking"
  ]
}
```

### List GitHub Repositories

/v1/repositories

List GitHub repositories accessible to the authenticated user through Cursor's GitHub App installation.

**This endpoint has very strict rate limits.**

Limit requests to **1 / user / minute**, and **30 / user / hour.**

This request can take tens of seconds to respond for users with access to many repositories.

Make sure to handle this information not being available gracefully.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/repositories \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "url": "https://github.com/your-org/your-repo"
    }
  ]
}
```


---

## Sitemap

[Overview of all docs pages](/llms.txt)
