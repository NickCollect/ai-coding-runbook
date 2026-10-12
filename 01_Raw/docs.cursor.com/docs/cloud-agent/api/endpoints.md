---
source_url: https://cursor.com/docs/cloud-agent/api/endpoints
fetched_at: 2026-10-12T06:49:40.873970+00:00
fetch_method: mintlify_md
---

# Cloud Agents API

### Public beta

The Cloud Agents API v1 is in public beta. APIs may change before general
availability.

The Cloud Agents API lets you programmatically launch and manage cloud agents that work on your repositories, along with the [environments](https://cursor.com/docs/cloud-agent/api/endpoints.md#environments) they run in.

- The Cloud Agents API accepts both [Basic and Bearer authentication](https://cursor.com/docs/api.md#authentication). Generate a user API key from [Cursor Dashboard → API Keys](https://cursor.com/dashboard/api), or use a [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md).
- For details on authentication methods, rate limits, and best practices, see the [API Overview](https://cursor.com/docs/api.md).
- View the full [OpenAPI specification](/docs-static/cloud-agents-openapi.yaml) for detailed schemas and examples.
- Webhooks are coming soon. The legacy [v0 API](https://cursor.com/docs/cloud-agent/api/v0.md) still supports them — see [Webhooks](https://cursor.com/docs/cloud-agent/api/webhooks.md).

### Migrating from v0?

This API splits work into a durable agent plus per-prompt runs, replacing the flatter v0 surface. The legacy [v0 reference](https://cursor.com/docs/cloud-agent/api/v0.md) remains available.

The 15 MB image limit below applies to API image inputs. Web attachments at
[cursor.com/agents](https://cursor.com/agents) use separate limits. See
[Cloud Agent web attachment limits](https://cursor.com/help/ai-features/cloud-agents.md#what-are-the-attachment-limits-for-cloud-agents-on-the-web).

## Endpoints

### Create An Agent

POST

`/v1/agents`

Create a Cloud Agent and immediately enqueue its initial run. The response returns both the durable `agent` and the initial `run`.

Repositories can come from any source control provider Cursor supports: GitHub (Cloud and Enterprise Server), GitLab (Cloud and Self-Hosted), Bitbucket Cloud, and Azure DevOps. Pass the repository URL as it appears on your provider, including a self-hosted host such as `gitlab.example.com`. See [Cloud Agents setup](https://cursor.com/docs/cloud-agent/setup.md) for connecting a provider.

#### Request Body

`prompt` object (required)

The task prompt for the agent, including optional images.

`prompt.text` string (required)

The instruction text for the agent.

`prompt.images` array (optional)

Image inputs for the prompt. Each entry must include either `data` (base64-encoded bytes with a required `mimeType`) or `url` (an http or https URL that Cursor fetches). Maximum 5 images, 15 MB each. Supported MIME types: `image/png`, `image/jpeg`, `image/gif`, `image/webp`.

`model` object (optional)

Model selection. Omit this field to use the configured default. When omitted, Cursor resolves your user default model, then your team default model, then a system default.

`model.id` string (required if `model` provided)

An explicit model ID returned by `GET /v1/models` (for example, `claude-4-sonnet-thinking`).

`model.params` array (optional)

Per-model parameters to apply to the run, such as reasoning effort or context window size. Each item has an `id` and `value`. Use only parameters supported by the selected model — call `GET /v1/models` to discover the valid `id`/`params` combinations.

`name` string (optional)

Display name for the agent. Maximum 100 characters. When omitted, Cursor auto-derives a name from the prompt.

`env` object (optional)

Execution environment target. Use a named `cloud` environment, or route to a `pool` or `machine` you host. Mutually exclusive with explicit `repos` when selecting a named Cursor-hosted environment.

`env.type` string (required if `env` provided)

Execution environment type. `cloud` uses Cursor-hosted VMs; `pool` and `machine` route to your own workers.

`env.name` string (optional)

Named Cursor-hosted environment, pool, or machine name. For `env.type: "pool"`, this is the pool name (defaults to `default` when omitted). An unknown pool name returns `400` instead of queueing forever. Name an [any-repo pool](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#any-repo-pools) to send more than one entry in `repos`.

`repos` array (optional)

Repository configuration. Mutually exclusive with a named cloud environment. Omit both `repos` and `env` to start a no-repo agent. You can also omit `repos` when `env.type` is `pool` to target an [any-repo pool](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#any-repo-pools). Maximum 20 repositories.

On self-hosted targets, only a named any-repo pool takes more than one repository. `machine`, the `default` pool, and repo-backed pools take one; sending more returns `400 validation_error` with the message "My Machines and repo-bound pools accept one repo in repos. To start an agent with several repos, set env.name to an any-repo pool."

`repos[0].url` string (required)

Repository URL on any connected source control provider (for example, `https://github.com/your-org/your-repo` or `https://gitlab.example.com/your-group/your-repo`). Required on every repo entry, including when `prUrl` is provided.

`repos[0].startingRef` string (optional)

Branch name or commit SHA to use as the starting point. Ignored when `prUrl` is provided.

`repos[0].prUrl` string (optional)

Pull request URL, called a merge request URL on GitLab. When provided, the agent works on that request's repository and branches; `startingRef` is ignored. `url` must still be set on the same `repos` entry.

`workOnCurrentBranch` boolean (optional, default: false)

When `false` (the default), Cursor pushes commits to a new auto-generated branch (`cursor/...`) based on `repos[0].startingRef` (or the PR base ref when `prUrl` is set). When `true`, Cursor pushes directly to that starting ref — for a non-PR create, that's the branch you passed in `startingRef`; for a `prUrl` create, that's the PR's head branch. The branch the agent pushed shows up in the agent's `git.branches[]`.

`autoCreatePR` boolean (optional)

Whether Cursor should open a pull request when the run completes.

`skipReviewerRequest` boolean (optional)

Whether to skip requesting the user as a reviewer when Cursor opens a PR. Only applies when `autoCreatePR` is `true`.

`envVars` object (optional)

Session-scoped environment variables for the cloud agent. Values are encrypted at rest, injected into the agent's shell, and deleted with the agent. Maximum 50 entries; names up to 255 bytes (can't start with `CURSOR_`), values up to 4096 bytes. Cannot be combined with a client-supplied `agentId`.

On self-hosted targets, `envVars` reach only pool workers that run with `--sync-dashboard-secrets` while a team admin has **Secret sync** on. `machine` targets and other pool workers run without them. See [Environments on Self-Hosted Machines](https://cursor.com/docs/cloud-agent/self-hosted.md#environments-on-self-hosted-machines).

**Beta:** `envVars` is rolling out. If it isn't enabled for your account yet, the field is silently ignored on create rather than failing the request — verify the values are present by inspecting the agent shell on a first run before relying on them in production.

`mcpServers` array (optional)

Inline MCP server definitions available to the agent. Maximum 50 servers. Remote servers support `headers` or OAuth `auth`; stdio servers run inside the cloud VM and can receive `env`. Server names must be unique.

`mcpServers[0].name` string (required)

The MCP server name exposed to the agent.

`mcpServers[0].type` string (optional)

Transport type: `http`, `sse`, or `stdio`. Defaults to `http` for remote servers with `url`, and `stdio` for servers with `command`.

`mcpServers[0].url` string (required for remote MCP)

HTTP or HTTPS URL for a remote MCP server. URLs with username or password are not allowed.

`mcpServers[0].command` string (required for stdio MCP)

Command to start a stdio MCP server inside the cloud agent VM. Use `args` and `env` for arguments and runtime secrets.

`customSubagents` array (optional)

Define custom subagents the main agent can delegate to during the run. Maximum 20 subagents. Each entry requires `name`, `description`, and `prompt`, plus an optional `model` (model ID string, `ModelSelection` object, or `"inherit"`). Names must be unique and cannot collide with built-ins (`explore`, `debug`, `shell`, `computerUse`, etc.).

`mode` string (optional, default: agent)

Initial conversation mode for the agent's first run. `plan` explores and drafts a plan before coding ([Plan mode](https://cursor.com/help/ai-features/plan-mode.md)); `agent` implements changes directly.

`agentId` string (optional)

Client-supplied agent identifier in the form `bc-<uuid>`. Useful for idempotent create flows — re-POSTing the same `agentId` returns `409 agent_id_conflict` rather than creating a duplicate. Cannot be combined with `envVars`; omit `agentId` so the server mints one when you need session secrets.

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
        { "id": "fast", "value": "true" }
      ]
    },
    "repos": [
      {
        "url": "https://github.com/your-org/your-repo",
        "startingRef": "main"
      }
    ],
    "mcpServers": [
      {
        "name": "linear",
        "type": "http",
        "url": "https://mcp.linear.app/sse",
        "headers": {
          "Authorization": "Bearer YOUR_LINEAR_API_KEY"
        }
      },
      {
        "name": "github",
        "type": "stdio",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_TOKEN": "YOUR_GITHUB_TOKEN"
        }
      }
    ],
    "autoCreatePR": true
  }'
```

Self-hosted GitLab repository:

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
    "prompt": {
      "text": "Add a README with setup instructions"
    },
    "repos": [
      {
        "url": "https://gitlab.example.com/your-group/your-repo",
        "startingRef": "main"
      }
    ]
  }'
```

Worker pool (including any-repo):

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
    "prompt": {
      "text": "Clone the payments service and add a health check"
    },
    "env": {
      "type": "pool",
      "name": "sandbox"
    }
  }'
```

Any-repo pool with several repos:

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
    "prompt": {
      "text": "Update the API client and the web app together"
    },
    "env": {
      "type": "pool",
      "name": "my-pool"
    },
    "repos": [
      {
        "url": "https://github.com/your-org/your-api",
        "startingRef": "main"
      },
      {
        "url": "https://github.com/your-org/your-web-app",
        "startingRef": "main"
      }
    ]
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
    "workOnCurrentBranch": false,
    "autoCreatePR": true,
    "url": "https://cursor.com/agents/bc-00000000-0000-0000-0000-000000000001",
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

GET

`/v1/agents`

List agents for the authenticated user, newest first.

#### Query Parameters

`limit` number (optional)

Number of agents to return. Default: 20, Max: 100.

`cursor` string (optional)

Pagination cursor from `nextCursor` on the previous response.

`prUrl` string (optional)

Filter agents by pull request URL, called a merge request URL on GitLab.

`includeArchived` boolean (optional, default: true)

Whether to include archived agents in the response.

List items only include the durable identity fields. Call `GET /v1/agents/{id}` to load the full record (`repos`, `workOnCurrentBranch`, `autoCreatePR`, etc.).

`nextCursor` is **omitted** from the response when there are no more pages — it is not returned as `null`. Treat its absence as "no more results".

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
      "url": "https://cursor.com/agents/bc-00000000-0000-0000-0000-000000000001",
      "createdAt": "2026-04-13T18:30:00.000Z",
      "updatedAt": "2026-04-13T18:45:00.000Z",
      "latestRunId": "run-00000000-0000-0000-0000-000000000001"
    }
  ],
  "nextCursor": "bc-00000000-0000-0000-0000-000000000002"
}
```

### Get An Agent

GET

`/v1/agents/{id}`

Retrieve durable metadata for an agent. Execution status lives on runs — fetch `latestRunId` and call [Get A Run](https://cursor.com/docs/cloud-agent/api/endpoints.md#get-a-run) to read run state.

#### Path Parameters

`id` string

Unique identifier for the agent (for example, `bc-00000000-0000-0000-0000-000000000001`).

#### Response Fields

`status` string

Agent lifecycle status. Controllers use it to decide whether a machine must stay up:

- `ACTIVE` — A turn is running, waiting on background work, or about to start. Keep the agent's machine up.
- `IDLE` — The last turn finished and follow-ups are accepted. The agent's machine may be [hibernated or snapshotted](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#hibernation). Runs that ended in a recoverable error also report `IDLE`; run-level error detail stays on [Get A Run](https://cursor.com/docs/cloud-agent/api/endpoints.md#get-a-run).
- `ARCHIVED` — The agent was archived or expired. Terminal; claims end and workspace state can be deleted.

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
  "workOnCurrentBranch": false,
  "autoCreatePR": true,
  "url": "https://cursor.com/agents/bc-00000000-0000-0000-0000-000000000001",
  "createdAt": "2026-04-13T18:30:00.000Z",
  "updatedAt": "2026-04-13T18:30:00.000Z",
  "latestRunId": "run-00000000-0000-0000-0000-000000000001"
}
```

### Create A Run

POST

`/v1/agents/{id}/runs`

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

Image inputs for the follow-up. Each entry must include either `data` (base64-encoded bytes with a required `mimeType`) or `url`. Maximum 5 images, 15 MB each. Supported MIME types: `image/png`, `image/jpeg`, `image/gif`, `image/webp`.

`mcpServers` array (optional)

Inline MCP server definitions for this follow-up run. When provided, these replace any create-time inline MCP servers for this run. Omit to keep the agent's current MCP configuration.

`mode` string (optional)

Conversation mode override for this follow-up run: `agent` or `plan`. Omit to keep the conversation's current mode from prior runs.

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/runs \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
    "prompt": {
      "text": "Also add troubleshooting steps"
    },
    "mcpServers": [
      {
        "name": "docs",
        "type": "http",
        "url": "https://example.com/mcp"
      }
    ]
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

GET

`/v1/agents/{id}/runs`

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
      "updatedAt": "2026-04-13T18:51:00.000Z",
      "git": {
        "branches": [
          {
            "repoUrl": "github.com/your-org/your-repo",
            "branch": "cursor/add-readme-a1b2"
          }
        ]
      }
    }
  ]
}
```

### Get A Run

GET

`/v1/agents/{id}/runs/{runId}`

Retrieve status, timestamps, and (for terminal runs) the final result, duration, and pushed branches for a specific run.

#### Path Parameters

`id` string

Unique identifier for the agent.

`runId` string

Unique identifier for the run (for example, `run-00000000-0000-0000-0000-000000000001`).

#### Response Fields

The base run fields (`id`, `agentId`, `status`, `createdAt`, `updatedAt`) are always present. The following are populated as soon as data is available:

`durationMs` integer (terminal runs)

Wall-clock duration of the run in milliseconds, computed once the run reaches `FINISHED`, `ERROR`, `CANCELLED`, or `EXPIRED`.

`result` string (terminal runs)

Final assistant reply text for a terminated run.

`git` object (when a branch has been pushed)

The agent's current pushed branches and pull requests. `git.branches[]` contains `{ repoUrl, branch?, prUrl? }` entries — one per branch the agent has pushed (stacked agents produce multiple).

**Per-agent state, not per-run.** Every run on the same agent returns the same `git` snapshot. Use the agent's `latestRunId` or the SSE stream to attribute work to a specific run.

`repoUrl` is returned without the scheme (for example, `github.com/your-org/your-repo`) — different from request `repos[].url`, which keeps the `https://` prefix.

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
  "updatedAt": "2026-04-13T18:45:00.000Z",
  "durationMs": 12357,
  "result": "Added README.md with installation instructions and usage examples.",
  "git": {
    "branches": [
      {
        "repoUrl": "github.com/your-org/your-repo",
        "branch": "cursor/add-readme-a1b2",
        "prUrl": "https://github.com/your-org/your-repo/pull/123"
      }
    ]
  }
}
```

### Stream A Run

GET

`/v1/agents/{id}/runs/{runId}/stream`

Stream Server-Sent Events (SSE) for one run. The stream is scoped to the requested run and does not replay prior runs.

#### Event types

- `status` — run status update. Payload: `{ runId, status }`.
- `assistant` — assistant text delta. Payload: `{ text }`.
- `thinking` — thinking text delta. Payload: `{ text }`.
- `tool_call` — tool call status update. Payload: `{ callId, name, status, args?, result?, truncated? }`.
- `interaction_update` — optional richer event emitted alongside the simplified events above. Payload matches the `InteractionUpdate` shape consumed by the [TypeScript SDK](https://cursor.com/docs/sdk/typescript.md), with subtypes like `text-delta`, `tool-call-started` / `tool-call-completed`, `step-started` / `step-completed`, and `turn-ended`. If you only need plain text and tool calls, handle the simplified events and ignore `interaction_update`. If you want the full SDK-shape stream, handle `interaction_update` and ignore the simplified events.
- `heartbeat` — keepalive event. Payload: `{}`.
- `result` — terminal run status. Payload: `{ runId, status, text?, durationMs?, git? }`. `text` is the final assistant reply, `durationMs` is the wall-clock run duration in milliseconds, and `git` mirrors `Run.git` (the agent's current pushed branches, not just this run's).
- `error` — stream error. Payload: `{ code, message }`.
- `done` — stream complete. Payload: `{}`.

#### Tool call payloads

`tool_call` events use a stable envelope around tool-specific inputs and outputs:

```typescript
type JsonValue =
  | string
  | number
  | boolean
  | null
  | JsonValue[]
  | { [key: string]: JsonValue };

interface ToolCallEventData {
  callId: string;
  name: string;
  status: "running" | "completed";
  args?: JsonValue;
  result?: JsonValue;
  truncated?: {
    args?: true;
    result?: true;
  };
}
```

`callId` identifies one tool invocation across updates. `name` is the public tool name, such as `read_file`, `run_terminal_cmd`, or `mcp`. `args` and `result` are tool-specific JSON values. If `args` or `result` is too large to include in the stream, Cursor omits that field and sets the matching `truncated` flag.

#### Resuming a stream

Most events include an `id` line — an opaque string you should not parse (current format looks like `1713033006000-0`, but treat it as opaque). The leading `status` event has no `id` — it is a sticky framing event that is re-sent at the top of every reconnect.

To resume after a disconnect, reconnect with `Last-Event-ID` set to the most recent received event id. The event id must belong to the requested run; otherwise the request returns `400 invalid_last_event_id`. After a successful resume, expect another `status` event before the resumed range begins.

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

id: 1713033005000-0
event: tool_call
data: {"callId":"call-1","name":"read_file","status":"running","args":{"path":"README.md"}}

id: 1713033006000-0
event: tool_call
data: {"callId":"call-1","name":"read_file","status":"completed","args":{"path":"README.md"},"result":{"success":{"content":"# Project","totalLines":1,"fileSize":9,"path":"README.md"}}}

id: 1713033010000-0
event: result
data: {"runId":"run-00000000-0000-0000-0000-000000000001","status":"FINISHED","text":"Added README.md with installation instructions.","durationMs":12357,"git":{"branches":[{"repoUrl":"github.com/your-org/your-repo","branch":"cursor/add-readme-a1b2"}]}}

id: 1713033010000-0
event: done
data: {}
```

### Cancel A Run

POST

`/v1/agents/{id}/runs/{runId}/cancel`

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

### Get Agent Usage

GET

`/v1/agents/{id}/usage`

Retrieve token usage for an agent, broken down per run. The response totals usage across every run on the agent and lists usage for each individual run. Token usage matches the `tokenUsage` reported by the team [usage events](https://cursor.com/docs/account/teams/admin-api.md#get-usage-events-data) endpoint.

#### Path Parameters

`id` string

Unique identifier for the agent (for example, `bc-00000000-0000-0000-0000-000000000001`).

#### Query Parameters

`runId` string (optional)

Scope the response to a single run (for example, `run-00000000-0000-0000-0000-000000000001`). Omit to return usage for every run on the agent. An unknown `runId` returns `404 run_not_found`.

#### Response Fields

`totalUsage` object

Token usage summed across the returned runs. Contains the same fields as each run's `usage` object.

`runs` array

Per-run usage, one entry per run (or a single entry when `runId` is set). Each object contains:

- `id` string - Run identifier (for example, `run-00000000-0000-0000-0000-000000000001`).
- `usageUuid` string (optional) - Internal usage identifier for the run. Omitted when the run has no recorded usage yet.
- `usage` object - Token usage for this run:
  - `inputTokens` number - Input tokens consumed.
  - `outputTokens` number - Output tokens generated.
  - `cacheWriteTokens` number - Tokens written to cache.
  - `cacheReadTokens` number - Tokens read from cache.
  - `totalTokens` number - Sum of the four token counts above.

Runs without any recorded token usage report zeros across all fields. A run that hasn't produced usage yet still appears in `runs` so you can track it over time.

```bash
# All runs on the agent
curl --request GET \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/usage \
  -u YOUR_API_KEY:

# A single run
curl --request GET \
  --url 'https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/usage?runId=run-00000000-0000-0000-0000-000000000001' \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "totalUsage": {
    "inputTokens": 12480,
    "outputTokens": 3110,
    "cacheWriteTokens": 18200,
    "cacheReadTokens": 42600,
    "totalTokens": 76390
  },
  "runs": [
    {
      "id": "run-00000000-0000-0000-0000-000000000002",
      "usageUuid": "00000000-0000-0000-0000-000000000002",
      "usage": {
        "inputTokens": 6320,
        "outputTokens": 1450,
        "cacheWriteTokens": 7100,
        "cacheReadTokens": 21300,
        "totalTokens": 36170
      }
    },
    {
      "id": "run-00000000-0000-0000-0000-000000000001",
      "usageUuid": "00000000-0000-0000-0000-000000000001",
      "usage": {
        "inputTokens": 6160,
        "outputTokens": 1660,
        "cacheWriteTokens": 11100,
        "cacheReadTokens": 21300,
        "totalTokens": 40220
      }
    }
  ]
}
```

## Artifacts

Artifacts are agent-scoped because the workspace persists across runs.

### List Artifacts

GET

`/v1/agents/{id}/artifacts`

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

GET

`/v1/agents/{id}/artifacts/download`

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

POST

`/v1/agents/{id}/archive`

Archive an agent. Archived agents remain readable but cannot accept new runs until unarchived. Use this for reversible "soft delete" flows.

Archive is idempotent — re-archiving an already-archived agent returns `200` with no change. You don't need to check current state before calling.

#### Path Parameters

`id` string

Unique identifier for the agent.

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/archive \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "id": "bc-00000000-0000-0000-0000-000000000001"
}
```

### Unarchive An Agent

POST

`/v1/agents/{id}/unarchive`

Unarchive an agent so it can accept new runs again.

Unarchive is idempotent — calling it on an already-active agent returns `200` with no change.

#### Path Parameters

`id` string

Unique identifier for the agent.

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/unarchive \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "id": "bc-00000000-0000-0000-0000-000000000001"
}
```

### Delete An Agent Permanently

DELETE

`/v1/agents/{id}`

Permanently delete an agent. This action is irreversible. Use [Archive](https://cursor.com/docs/cloud-agent/api/endpoints.md#archive-an-agent) for reversible removal.

#### Path Parameters

`id` string

Unique identifier for the agent.

```bash
curl --request DELETE \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001 \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "id": "bc-00000000-0000-0000-0000-000000000001"
}
```

## Environments

Environments are the saved [Cloud Agent environments](https://cursor.com/docs/cloud-agent/setup.md) that agents run in: the repositories and `environment.json` configuration you manage in the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#environments). Use these endpoints to script the same work.

### Create An Environment

POST

`/v1/environments`

Create a saved environment. The response is `201` with the new environment.

If the owner already has an environment with the same `name`, the request returns `409 environment_name_conflict`. The error can include the existing environment's ID in `environmentId`.

#### Request Body

`owner` string (required)

`personal` to create an environment for the API key's user, or `team` to create one for the team.

`name` string (required)

Display name, up to 255 characters. It must differ from the names of the owner's other environments.

`repos` array (required)

Repositories for the environment. Each entry has a `url` (for example, `https://github.com/your-org/your-repo`). Maximum 100 repositories. Send an empty array for an environment without repositories. A repository Cursor can't reach through your source control integration returns `400 repository_access`.

`environmentJson` string (required)

The environment's `environment.json`, as a JSON-encoded string. It uses the same [schema](https://cursor.com/docs/cloud-agent/setup.md#configuration-in-code-with-environmentjson) as a `.cursor/environment.json` file. An invalid configuration returns `400 validation_error`.

#### Response Fields

`id` string

Environment ID.

`name` string

Display name.

`owner` string

`personal` for an environment that belongs to one user, or `team` for an environment shared with the team.

`repos` array

Repositories in the environment. Each entry has a `url`.

`createdAt`, `updatedAt` string

When the environment was created and last updated (ISO 8601).

```bash
curl --request POST \
  --url https://api.cursor.com/v1/environments \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
    "owner": "team",
    "name": "Web app",
    "repos": [
      { "url": "https://github.com/your-org/your-web-app" },
      { "url": "https://github.com/your-org/your-api" }
    ],
    "environmentJson": "{\"install\": \"pnpm install\", \"start\": \"sudo service docker start\"}"
  }'
```

**Response:**

```json
{
  "id": "8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c",
  "name": "Web app",
  "owner": "team",
  "repos": [
    { "url": "https://github.com/your-org/your-web-app" },
    { "url": "https://github.com/your-org/your-api" }
  ],
  "createdAt": "2026-09-30T21:40:00.000Z",
  "updatedAt": "2026-09-30T21:40:00.000Z"
}
```

### List Environments

GET

`/v1/environments`

List the saved environments your API key can access, most recently updated first: your personal environments and your team's environments. Team admins don't see members' personal environments in the list.

Team admins and service account API keys see every team environment. Other callers see a team environment only when they can access all of its repositories. A service account API key limited to specific repositories, and user-scoped tokens minted with it, only list environments that have repositories, all within that limit. Drafts and deleted environments aren't included.

#### Query Parameters

`limit` number (optional)

Number of environments to return. Default: 20, Max: 100.

`cursor` string (optional)

Pagination cursor from `nextCursor` on the previous response.

#### Response Fields

`items` array

Environments, with the same fields as [Get An Environment](https://cursor.com/docs/cloud-agent/api/endpoints.md#get-an-environment) except `environmentJson` and `versionId`. Call Get An Environment to load an environment's configuration.

`nextCursor` string (optional)

Cursor for the next page. Omitted when there are no more pages.

A page can come back with fewer items than `limit`. Keep requesting pages until `nextCursor` is absent. It's **omitted** from the response, not returned as `null`, when there are no more pages.

Callers other than team admins and service account API keys see team environments only after Cursor checks their access to the repositories, and those checks can run out of time. A response can then leave out team environments it hasn't verified yet, or stop before the end of the list. Those environments show up in later requests.

The list is ordered by last update, so an environment that changes during a walk moves to the front. A later page can then leave it out and repeat another environment.

```bash
curl --request GET \
  --url 'https://api.cursor.com/v1/environments?limit=20' \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "id": "8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c",
      "name": "Web app",
      "owner": "team",
      "repos": [
        { "url": "https://github.com/your-org/your-web-app" },
        { "url": "https://github.com/your-org/your-api" }
      ],
      "createdAt": "2026-09-01T16:20:00.000Z",
      "updatedAt": "2026-09-29T21:05:00.000Z"
    }
  ],
  "nextCursor": "MjA"
}
```

### Get An Environment

GET

`/v1/environments/{id}`

Retrieve a saved environment and its latest saved configuration.

#### Path Parameters

`id` string

Environment ID (for example, `8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c`).

#### Response Fields

The fields [Create An Environment](https://cursor.com/docs/cloud-agent/api/endpoints.md#create-an-environment) returns, plus:

`repoFile` object (optional)

Set when the environment reads its configuration from a file in a repository, and points at that file: the repository `url` and the file `path`.

`environmentJson` string (optional)

The environment's latest saved configuration, its `environment.json`, as a JSON-encoded string.

`versionId` string (optional)

ID of the latest saved environment version. Omitted when no version has been saved.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/environments/8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "id": "8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c",
  "name": "Web app",
  "owner": "team",
  "repos": [
    { "url": "https://github.com/your-org/your-web-app" },
    { "url": "https://github.com/your-org/your-api" }
  ],
  "environmentJson": "{\"install\": \"pnpm install\", \"start\": \"sudo service docker start\"}",
  "versionId": "c9f0f895-fb98-4b91-8f3e-2a1b0c9d8e7f",
  "createdAt": "2026-09-01T16:20:00.000Z",
  "updatedAt": "2026-09-29T21:05:00.000Z"
}
```

### Update An Environment

PATCH

`/v1/environments/{id}`

Rename an environment, replace its configuration, or both. A request with both fields applies them together, so either both change or neither does. The response is `204` with no body.

Renaming an environment to a name its owner already uses returns `409 environment_name_conflict`.

#### Path Parameters

`id` string

Environment ID.

#### Request Body

`name` string (optional)

New display name, up to 255 characters. It must differ from the names of the owner's other environments.

`environmentJson` string (optional)

Replacement `environment.json`, as a JSON-encoded string. It replaces the whole configuration and uses the same [schema](https://cursor.com/docs/cloud-agent/setup.md#configuration-in-code-with-environmentjson) as a `.cursor/environment.json` file. An invalid configuration returns `400 validation_error`.

```bash
curl --request PATCH \
  --url https://api.cursor.com/v1/environments/8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
    "name": "Web app (staging)",
    "environmentJson": "{\"install\": \"pnpm install --frozen-lockfile\", \"start\": \"sudo service docker start\"}"
  }'
```

**Response:** `204 No Content`

### Delete An Environment

DELETE

`/v1/environments/{id}`

Permanently delete a saved environment. This action is irreversible.

#### Path Parameters

`id` string

Environment ID.

```bash
curl --request DELETE \
  --url https://api.cursor.com/v1/environments/8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "id": "8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c"
}
```

### List Environment History

GET

`/v1/environments/{id}/history`

List the changes to an environment, newest first. These are the events its History tab in the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#environments) shows.

#### Path Parameters

`id` string

Environment ID.

#### Query Parameters

`limit` number (optional)

Number of events to return. Default: 20, Max: 100.

`cursor` string (optional)

Pagination cursor from `nextCursor` on the previous response.

#### Response Fields

`items` array

History events, newest first, with the fields below.

`nextCursor` string (optional)

Cursor for the next page. Omitted when there are no more events.

#### Event Fields

`id` string

Event ID.

`createdAt` string

When the change was made (ISO 8601).

`kind` string

`created`, `updated`, `deleted`, `backfilled`, or `changed`.

`title`, `description` string

The event's summary and details, as the History tab shows them.

`source` string (optional)

Where the change came from: `dashboard`, `setup_flow`, `restore`, `api`, `agent_run`, `repo_file`, or `request_override`.

`current` boolean

`true` for the event that saved the environment's current configuration.

`environmentJson` string (optional)

The `environment.json` the event saved, as a JSON-encoded string.

```bash
curl --request GET \
  --url 'https://api.cursor.com/v1/environments/8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c/history?limit=2' \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "id": "3b7e1f2a-9c4d-4e8b-a1f6-5d2c8e9b0a17",
      "createdAt": "2026-09-29T21:05:00.000Z",
      "kind": "updated",
      "title": "Team environment updated",
      "description": "Install script changed.",
      "source": "api",
      "current": true,
      "environmentJson": "{\"install\": \"pnpm install\", \"start\": \"sudo service docker start\"}"
    },
    {
      "id": "e4a9c2d1-6b3f-4a7e-9d8c-1f0b2a3c4d5e",
      "createdAt": "2026-09-01T16:20:00.000Z",
      "kind": "created",
      "title": "Team environment created",
      "description": "Team environment created.",
      "source": "dashboard",
      "current": false,
      "environmentJson": "{\"install\": \"npm install\"}"
    }
  ],
  "nextCursor": "e4a9c2d1-6b3f-4a7e-9d8c-1f0b2a3c4d5e"
}
```

### List Environment Builds

GET

`/v1/environments/{id}/builds`

List an environment's [Builds](https://cursor.com/docs/cloud-agent/builds.md), newest first, up to 10 per page.

#### Path Parameters

`id` string

Environment ID.

#### Query Parameters

`cursor` string (optional)

Pagination cursor from `nextCursor` on the previous response.

#### Response Fields

`items` array

Up to 10 Builds, newest first. Each has the fields [Get An Environment Build](https://cursor.com/docs/cloud-agent/api/endpoints.md#get-an-environment-build) returns.

`nextCursor` string (optional)

Cursor for the next page. Omitted when there are no more Builds.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/environments/8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c/builds \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "id": "bld-20260930-3c59dc04-8a1d-4b6e-9f2a-7e5d1c0b9a8f",
      "environmentId": "8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c",
      "status": "SUCCEEDED",
      "trigger": "RECURRING",
      "draft": false,
      "createdAt": "2026-09-30T09:00:00.000Z",
      "updatedAt": "2026-09-30T09:12:00.000Z",
      "completedAt": "2026-09-30T09:12:00.000Z"
    },
    {
      "id": "bld-20260929-a87ff679-a2f3-4e1c-8f5b-0c3d2e1f4a5b",
      "environmentId": "8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c",
      "status": "FAILED",
      "trigger": "CONFIG_CHANGE",
      "draft": false,
      "failure": { "type": "TERMINAL_FAILURE", "code": "environment_json_invalid" },
      "createdAt": "2026-09-29T21:05:00.000Z",
      "updatedAt": "2026-09-29T21:06:00.000Z",
      "completedAt": "2026-09-29T21:06:00.000Z"
    }
  ]
}
```

### Get An Environment Build

GET

`/v1/environments/{id}/builds/{buildId}`

Retrieve one of an environment's Builds. A build ID that isn't one of the environment's Builds returns `404 build_not_found`.

#### Path Parameters

`id` string

Environment ID.

`buildId` string

Build ID (for example, `bld-20260930-3c59dc04-8a1d-4b6e-9f2a-7e5d1c0b9a8f`).

#### Response Fields

`id` string

Build ID.

`environmentId` string

ID of the environment the Build belongs to.

`status` string

`IN_PROGRESS`, `SUCCEEDED`, `FAILED`, `CANCELLED`, or `SKIPPED`. A [skipped Build](https://cursor.com/docs/cloud-agent/builds.md#skipped-builds) found nothing to rebuild.

`trigger` string

What started the Build: `RECURRING` for a scheduled Build, `CONFIG_CHANGE` after a configuration or secrets change, or `MANUAL` for one started on request.

`draft` boolean

`true` for a draft Build. Agents don't start from a draft Build until it's activated.

`failure` object (optional)

Why a failed Build failed. `type` is `INSTALL_FAILED` when the `install` command failed, or `TERMINAL_FAILURE` for other failures. `code`, when present, is a machine-readable cause such as `environment_json_invalid`.

`createdAt`, `updatedAt` string

When the Build was created and last updated (ISO 8601).

`completedAt` string (optional)

When the Build finished (ISO 8601). Omitted while it's in progress.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/environments/8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c/builds/bld-20260930-3c59dc04-8a1d-4b6e-9f2a-7e5d1c0b9a8f \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "id": "bld-20260930-3c59dc04-8a1d-4b6e-9f2a-7e5d1c0b9a8f",
  "environmentId": "8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c",
  "status": "SUCCEEDED",
  "trigger": "RECURRING",
  "draft": false,
  "createdAt": "2026-09-30T09:00:00.000Z",
  "updatedAt": "2026-09-30T09:12:00.000Z",
  "completedAt": "2026-09-30T09:12:00.000Z"
}
```

### Get The Active Build

GET

`/v1/environments/{id}/builds/active`

Find out what an agent you start on this environment boots from: one of its Builds, or Cursor's default image.

#### Path Parameters

`id` string

Environment ID.

#### Response Fields

`type` string

`build` when the agent starts from a Build, or `universal_image` when it starts on Cursor's default image.

`buildId` string (optional)

ID of the Build the agent starts from. Set when `type` is `build`.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/environments/8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c/builds/active \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "type": "build",
  "buildId": "bld-20260930-3c59dc04-8a1d-4b6e-9f2a-7e5d1c0b9a8f"
}
```

## Secrets

Secrets are the environment variables Cursor gives cloud agents, the values you also manage in the **Secrets** tab of the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents). The secrets endpoints cover the secrets that belong to one environment and the secrets that belong to your team. To choose a type for a secret, see [Secret protection](https://cursor.com/docs/cloud-agent/security-network.md#secret-protection).

- **Responses never include values.** They list names, types, and repositories.
- **A name can have versions for different repositories.** An environment or team can hold one name several times, each version for repositories the others don't cover. Each version is listed separately and has its own `id`.
- **Use a user API key, an agent-scoped service account API key, or a user-scoped token.** Each works within one team: a user API key in its user's default team, a user-scoped token in the team that minted it, and a service account API key in its own team. User-scoped tokens come from [Create A User-Scoped Worker Token](https://cursor.com/docs/cloud-agent/api/endpoints.md#create-a-user-scoped-worker-token). Team API keys and automation webhook API keys aren't supported, and API keys that start with `grok_` get `403 key_not_supported`.

#### Secret Versions

Every secrets endpoint describes a version of a secret with these fields. No response includes a secret's value.

`id` string

Opaque version ID, such as `secv_3qKx9mT2bV7nR1cW5yZ8aQ`. A version keeps its `id` through changes to its value, type, or repositories.

`name` string

The environment variable name agents see, such as `NPM_TOKEN`.

`type` string

`runtime_secret` for a [Runtime Secret](https://cursor.com/docs/cloud-agent/security-network.md#runtime-secrets), `environment_variable` for an [Environment Variable](https://cursor.com/docs/cloud-agent/security-network.md#environment-variables), or `build_secret` for a [Build Secret](https://cursor.com/docs/cloud-agent/security-network.md#build-secrets).

`repos` array of strings

The only repositories that get this version, such as `github.com/acme/api`, or an empty array when every repository gets it. Repositories are listed the way Cursor stores them: lowercase and sorted, with repository URLs reduced to `host/owner/repo`.

`createdAt` string

When the version was created, in ISO 8601 format.

#### Which Value An Agent Gets

When one name is set in several places, an agent gets the value from the most specific place: values passed when the agent starts, such as `envVars` on [Create An Agent](https://cursor.com/docs/cloud-agent/api/endpoints.md#create-an-agent), then the environment's secrets, then the user's personal secrets, then the team's secrets. A name set at one level hides that name at every level below it.

#### Changing Secrets

- **Changes reach agents that start afterward.** Running agents keep the values they started with. Agents that start from a [Build](https://cursor.com/docs/cloud-agent/builds.md) get the change once a newer Build of their environment finishes.
- **Reads can lag behind writes.** Right after a change, a request can miss it. Leave a moment between writes to the same name, and pass `?id=` to pick a version.

### List Secrets

GET

`/v1/secrets`

List every Cloud Agents secret your API key can list in one paginated list. Each item is a [secret version](https://cursor.com/docs/cloud-agent/api/endpoints.md#secret-versions), with the `id` its owner's own list shows and an `owner`. No item includes a value.

Without `scope` or `environmentId`, the list includes:

- **The team's secrets**, as [List Team Secrets](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-team-secrets) lists them, for an API key with no repository limit.
- **Your personal secrets**, for a user API key or user-scoped token with no repository limit.
- **The secrets of your team's environments** and, with a user API key or user-scoped token, of your personal environments. An API key limited to certain repositories gets only environments whose repositories all sit inside its limit.
- **Other members' secrets, for team admins.** A team admin using their own user API key without `repo` also gets the other members' personal secrets and their personal environments' secrets.

Items aren't sorted by name, and other members' secrets come after the rest. A page can hold fewer than `limit` items, or none, and still have a `nextCursor`. Keep paging until it's `null`, and send the same filters with each `cursor`.

#### Query Parameters

`scope` string (optional)

`team`, `user`, `members`, or `environment`. `team` lists only the team's secrets, refused as [List Team Secrets](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-team-secrets) refuses it. `user` lists only your personal secrets: a key that doesn't act for a user, such as a service account API key, gets `403 user_required`, and a key limited to certain repositories gets `403 repository_access`. `members` lists your personal secrets and, for an explicit team admin using their own user API key or session, every other current member's personal secrets after them, but none of their personal environments' secrets. For everyone else, it returns the same response or refusal as `user`. `environment` lists only environment secrets.

`environmentId` string (optional)

List only this environment's secrets, refused as [List Environment Secrets](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-environment-secrets) refuses it. Can't be combined with `scope=team`, `scope=user`, or `scope=members`; those combinations return `400 validation_error`.

`name` string (optional)

Only versions with this name, ignoring case.

`repo` string (optional)

Only the versions an agent on this repository gets, such as `github.com/acme/api`: versions for that repository and versions for every repository. Combining it with `scope=members` returns `400 validation_error`.

`limit` number (optional)

Maximum items per page, from 1 to 100. Defaults to 100.

`cursor` string (optional)

`nextCursor` from the previous page.

#### Response Fields

`items` array

[Secret versions](https://cursor.com/docs/cloud-agent/api/endpoints.md#secret-versions), each with an `owner`. Every item has `repos`, including other members' versions, and `[]` means every repository gets the version. On another member's version, `repos` can name repositories you can't access.

`items[].owner` object

Who holds the version. `type` is `team`, `user`, or `environment`. An `environment` owner includes `environmentId`. A `user` owner and a personal environment include `user.email`, which is `null` when the user has no email on file.

`nextCursor` string or null

Cursor for the next page, or `null` on the last page.

```bash
curl --request GET \
  --url 'https://api.cursor.com/v1/secrets?limit=100' \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "id": "secv_Hn2kT8wQ5vC1xZ4mB7rP0g",
      "name": "GITHUB_PACKAGES_TOKEN",
      "type": "runtime_secret",
      "repos": [],
      "createdAt": "2026-09-28T10:12:34.000Z",
      "owner": { "type": "team" }
    },
    {
      "id": "secv_3qKx9mT2bV7nR1cW5yZ8aQ",
      "name": "NPM_TOKEN",
      "type": "runtime_secret",
      "repos": ["github.com/acme/api"],
      "createdAt": "2026-10-01T09:15:42.000Z",
      "owner": {
        "type": "environment",
        "environmentId": "8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c"
      }
    },
    {
      "id": "secv_Tb4mK7qW2xN9pR5vC8sJ1e",
      "name": "OPENAI_API_KEY",
      "type": "runtime_secret",
      "repos": [],
      "createdAt": "2026-10-04T13:05:27.000Z",
      "owner": { "type": "user", "user": { "email": "ada@acme.com" } }
    }
  ],
  "nextCursor": null
}
```

### List Environment Secrets

GET

`/v1/environments/{id}/secrets`

List an environment's Cloud Agents secrets. Each item is a [secret version](https://cursor.com/docs/cloud-agent/api/endpoints.md#secret-versions), and no item includes a value. Items are sorted by name, so the versions of one name sit together.

Who can list an environment's secrets:

- **A user API key or user-scoped token** can list its user's personal environments and its team's environments. Any team member can list a team environment's secrets.
- **A service account API key** can list its team's environments.
- **An API key limited to certain repositories**, or a user-scoped token it minted, can list only environments that have repositories, all inside its limit.
- **Everyone else** gets `404 environment_not_found`, including a team admin on a member's personal environment.

The list isn't paginated yet, so `nextCursor` is always `null`. Follow `nextCursor` until it's `null`, so your client keeps working when pages arrive.

#### Path Parameters

`id` string

Environment ID.

#### Response Fields

`items` array

The environment's [secret versions](https://cursor.com/docs/cloud-agent/api/endpoints.md#secret-versions). A name with versions for different repositories appears once per version.

`nextCursor` string or null

Cursor for the next page. Always `null` for now.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/environments/8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c/secrets \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "id": "secv_Qm7pW2xK9cT4vB1nY6hR3w",
      "name": "DOCKER_TOKEN",
      "type": "build_secret",
      "repos": [],
      "createdAt": "2026-09-30T14:02:11.000Z"
    },
    {
      "id": "secv_3qKx9mT2bV7nR1cW5yZ8aQ",
      "name": "NPM_TOKEN",
      "type": "runtime_secret",
      "repos": ["github.com/acme/api"],
      "createdAt": "2026-10-01T09:15:42.000Z"
    },
    {
      "id": "secv_Lw0pE4sJ6hD9fG2kU8tY1g",
      "name": "NPM_TOKEN",
      "type": "runtime_secret",
      "repos": ["github.com/acme/web"],
      "createdAt": "2026-10-02T11:20:05.000Z"
    },
    {
      "id": "secv_Zr5cN8vM1qL4wX7tA2sD9g",
      "name": "SENTRY_ENVIRONMENT",
      "type": "environment_variable",
      "repos": [],
      "createdAt": "2026-10-03T16:45:00.000Z"
    }
  ],
  "nextCursor": null
}
```

### Set An Environment Secret

PUT

`/v1/environments/{id}/secrets/{name}`

Create an environment secret, rotate its value, or change its type or repositories. Every request sends the value, and the response is the [secret version](https://cursor.com/docs/cloud-agent/api/endpoints.md#secret-versions) without it.

Which version the request changes:

- **With `?id=`**, it changes the version with that `id`. An `id` that isn't a version of this name in this environment returns `404 secret_not_found`.
- **Without `?id=`**, a name with no version gets one, and the response is `201`. A name with one version has it changed in place, and the response is `200`. A name with several versions returns `409 secret_name_ambiguous`, listing each version's `id` and `repos`, so you can pass one as `?id=`.

A `PUT` never adds a second version to a name that already has one. To give a name a version for other repositories, use the dashboard.

When you omit `type` or `repos`, the version keeps its current one, so rotating a value never changes its type or widens its repositories. Send `repos: []` to give the version every repository. New `repos` that overlap another version of the name return `409 secret_scope_conflict`. An environment holds at most 1,000 secrets, and creating one more returns `409 secret_limit_reached`.

Build secrets can't be set through the API yet: `type: "build_secret"` returns `400 validation_error`, and so does a change to an existing Build Secret. `DELETE` still removes one.

Who can set an environment's secrets:

- **A user API key or user-scoped token** can set secrets on its user's personal environments and its team's environments.
- **A service account API key** can set secrets on its team's environments.
- **An API key limited to certain repositories**, or a user-scoped token it minted, can set secrets only on environments that have repositories, all inside its limit.
- **When your team lets only admins change secrets**, only team admins can set a team environment's secrets. Everyone else, service account API keys included, gets `403 team_admin_required`.
- **Everyone else** gets `404 environment_not_found`.

Each change is recorded as a [`cloud_agent_secret` event](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#event-types) with the secret's name and repositories but not its value, as the same change in the dashboard is.

#### Path Parameters

`id` string

Environment ID.

`name` string

Secret name, as agents see it: letters, digits, and underscores, not starting with a digit, and at most 255 characters. Names that contain `CURSOR_SANDBOX` are reserved, and so are `HTTP_PROXY`, `HTTPS_PROXY`, and `ALL_PROXY` in any letter case.

Names that differ only in letter case count as the same name. Creating `npm_token` when `NPM_TOKEN` exists returns `409 secret_name_conflict`.

#### Query Parameters

`id` string (optional)

The `id` of the version to change, from the environment's secrets list (`GET /v1/environments/{id}/secrets`) or from a `409 secret_name_ambiguous` response.

#### Request Body

`value` string (required)

The secret's value, 1 to 4,096 bytes of UTF-8 text.

`type` string (optional)

`runtime_secret` or `environment_variable`. A new version defaults to `runtime_secret`. A change without `type` keeps the version's type.

`repos` array of strings (optional)

The only repositories that get this version, up to 100. An empty array, or omitting `repos` on a new version, gives it every repository. A change without `repos` keeps the version's repositories.

Each entry names a repository: `acme/api`, a URL such as `https://github.com/acme/api.git` or `git@github.com:acme/api.git`, or another host's path such as `gitlab.com/group/subgroup/project`.

#### Response Fields

The [secret version](https://cursor.com/docs/cloud-agent/api/endpoints.md#secret-versions) the request created or changed. When the new version isn't readable yet, a `201` leaves out `id` and `createdAt`.

```bash
curl --request PUT \
  --url https://api.cursor.com/v1/environments/8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c/secrets/NPM_TOKEN \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
    "value": "npm_example_token",
    "repos": ["github.com/acme/api"]
  }'
```

**Response:** `201`

```json
{
  "id": "secv_3qKx9mT2bV7nR1cW5yZ8aQ",
  "name": "NPM_TOKEN",
  "type": "runtime_secret",
  "repos": ["github.com/acme/api"],
  "createdAt": "2026-10-04T14:02:11.000Z"
}
```

Rotate the value. The response is `200` with the same `id`, `type`, `repos`, and `createdAt`:

```bash
curl --request PUT \
  --url https://api.cursor.com/v1/environments/8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c/secrets/NPM_TOKEN \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{"value": "npm_rotated_token"}'
```

### Delete An Environment Secret

DELETE

`/v1/environments/{id}/secrets/{name}`

Delete one version of an environment secret. This action is irreversible. Every type can be deleted, Build Secrets included.

Which version the request deletes:

- **With `?id=`**, it deletes the version with that `id`. An `id` that isn't a version of this name in this environment returns `404 secret_not_found`.
- **Without `?id=`**, a name with one version has it deleted. A name with no version returns `404 secret_not_found`, and a name with several versions returns `409 secret_name_ambiguous`, listing each version's `id` and `repos`, and deletes nothing.

`{name}` must match a listed name exactly, letter case included, so a request for `NPM_TOKEN` never deletes `npm_token`. URL-encode characters a path can't carry.

Who can delete an environment's secrets follows the same rules as setting them: a user API key or user-scoped token on its user's personal environments and its team's environments, a service account API key on its team's environments, and an API key limited to certain repositories only on environments that have repositories, all inside its limit. Everyone else gets `404 environment_not_found`. When your team lets only admins change secrets, everyone but team admins gets `403 team_admin_required`, service account API keys included.

Each delete is recorded as a [`cloud_agent_secret` event](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#event-types) with the action `delete`, as a delete in the dashboard is. Agents that start afterward stop getting this version.

#### Path Parameters

`id` string

Environment ID.

`name` string

Secret name, exactly as the environment's secrets list (`GET /v1/environments/{id}/secrets`) shows it.

#### Query Parameters

`id` string (optional)

The `id` of the version to delete, from the environment's secrets list or from a `409 secret_name_ambiguous` response.

#### Response Fields

`name` string

Name of the deleted secret.

```bash
curl --request DELETE \
  --url https://api.cursor.com/v1/environments/8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c/secrets/NPM_TOKEN \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "name": "NPM_TOKEN"
}
```

Delete one version of a name that has several:

```bash
curl --request DELETE \
  --url 'https://api.cursor.com/v1/environments/8f14e45f-ceea-4e6b-9c3a-1d2e3f4a5b6c/secrets/NPM_TOKEN?id=secv_Lw0pE4sJ6hD9fG2kU8tY1g' \
  -u YOUR_API_KEY:
```

### List Team Secrets

GET

`/v1/team/secrets`

List the Cloud Agents secrets of the team your API key works in. Each item is a [secret version](https://cursor.com/docs/cloud-agent/api/endpoints.md#secret-versions), and no item includes a value. Personal secrets, environment secrets, and other teams' secrets aren't included. Items are sorted by name, so the versions of one name sit together.

Who can list team secrets:

- **Any member of the team** can list them with a user API key or user-scoped token, even when the team lets only admins change secrets.
- **A service account API key** lists its own team.
- **An API key limited to certain repositories**, or a user-scoped token it minted, gets `403 repository_access`, because team secrets reach every repository.
- **An API key that isn't working in a team**, or a caller without a seat on the team, gets `403 team_membership_required`.

The list isn't paginated yet, so `nextCursor` is always `null`. Follow `nextCursor` until it's `null`, so your client keeps working when pages arrive.

#### Response Fields

`items` array

The team's [secret versions](https://cursor.com/docs/cloud-agent/api/endpoints.md#secret-versions). A name with versions for different repositories appears once per version.

`nextCursor` string or null

Cursor for the next page. Always `null` for now.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/team/secrets \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "id": "secv_Hn2kT8wQ5vC1xZ4mB7rP0g",
      "name": "GITHUB_PACKAGES_TOKEN",
      "type": "runtime_secret",
      "repos": [],
      "createdAt": "2026-09-28T10:12:34.000Z"
    },
    {
      "id": "secv_Ye6sF3jL9pV2nK5tD8uW1A",
      "name": "SENTRY_DSN",
      "type": "environment_variable",
      "repos": ["github.com/acme/web"],
      "createdAt": "2026-10-02T08:30:00.000Z"
    }
  ],
  "nextCursor": null
}
```

### Set A Team Secret

PUT

`/v1/team/secrets/{name}`

Create a secret for the team your API key works in, rotate its value, or change its type or repositories. Every request sends the value, and the response is the [secret version](https://cursor.com/docs/cloud-agent/api/endpoints.md#secret-versions) without it. Team secrets reach every agent on the team unless a more specific value hides them, as described in [Which Value An Agent Gets](https://cursor.com/docs/cloud-agent/api/endpoints.md#which-value-an-agent-gets).

Which version the request changes:

- **With `?id=`**, it changes the version with that `id`, from the team's secrets list (`GET /v1/team/secrets`). An `id` that isn't a version of this name in your team returns `404 secret_not_found`.
- **Without `?id=`**, a name with no version gets one, and the response is `201`. A name with one version has it changed in place, and the response is `200`. A name with several versions returns `409 secret_name_ambiguous`, listing each version's `id` and `repos`, so you can pass one as `?id=`.

A `PUT` never adds a second version to a name that already has one. To give a name a version for other repositories, use the dashboard.

When you omit `type` or `repos`, the version keeps its current one, so rotating a value never changes its type or widens its repositories. Send `repos: []` to give the version every repository. New `repos` that overlap another version of the name return `409 secret_scope_conflict`, and so does `repos: []` while the name has other versions. A team holds at most 1,000 secrets, and creating one more returns `409 secret_limit_reached`.

Build secrets can't be set through the API yet: `type: "build_secret"` returns `400 validation_error`, and so does a change to an existing Build Secret.

Who can set team secrets:

- **Any member of the team** can, with a user API key or user-scoped token, unless the team lets only admins change secrets. Then everyone but team admins gets `403 team_admin_required`, service account API keys included.
- **A service account API key** sets its own team's secrets.
- **An API key limited to certain repositories**, or a user-scoped token it minted, gets `403 repository_access`, because team secrets reach every repository.
- **An API key that isn't working in a team**, or a caller without a seat on the team, gets `403 team_membership_required`.

Each change is recorded in your team's audit log as a [`cloud_agent_secret` event](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#event-types) with the secret's name and repositories but not its value, as the same change in the dashboard is.

#### Path Parameters

`name` string

Secret name, as agents see it: letters, digits, and underscores, not starting with a digit, and at most 255 characters. Names that contain `CURSOR_SANDBOX` are reserved, and so are `HTTP_PROXY`, `HTTPS_PROXY`, and `ALL_PROXY` in any letter case.

Names that differ only in letter case count as the same name. Creating `npm_token` when the team has `NPM_TOKEN` returns `409 secret_name_conflict`.

#### Query Parameters

`id` string (optional)

The `id` of the version to change, from the team's secrets list or from a `409 secret_name_ambiguous` response.

#### Request Body

`value` string (required)

The secret's value, 1 to 4,096 bytes of UTF-8 text.

`type` string (optional)

`runtime_secret` or `environment_variable`. A new version defaults to `runtime_secret`. A change without `type` keeps the version's type.

`repos` array of strings (optional)

The only repositories that get this version, up to 100. An empty array, or omitting `repos` on a new version, gives it every repository. A change without `repos` keeps the version's repositories.

Each entry names a repository: `acme/api`, a URL such as `https://github.com/acme/api.git` or `git@github.com:acme/api.git`, or another host's path such as `gitlab.com/group/subgroup/project`.

#### Response Fields

The [secret version](https://cursor.com/docs/cloud-agent/api/endpoints.md#secret-versions) the request created or changed. When the new version isn't readable yet, a `201` leaves out `id` and `createdAt`.

```bash
curl --request PUT \
  --url https://api.cursor.com/v1/team/secrets/NPM_TOKEN \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
    "value": "npm_example_token",
    "repos": ["github.com/acme/api"]
  }'
```

**Response:** `201`

```json
{
  "id": "secv_Ub4rJ7nD2kX9qM5wL1sE8Q",
  "name": "NPM_TOKEN",
  "type": "runtime_secret",
  "repos": ["github.com/acme/api"],
  "createdAt": "2026-10-04T14:02:11.000Z"
}
```

Change one version of a name that has several, using its `id` from the team's secrets list:

```bash
curl --request PUT \
  --url 'https://api.cursor.com/v1/team/secrets/NPM_TOKEN?id=secv_Ub4rJ7nD2kX9qM5wL1sE8Q' \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{"value": "npm_rotated_token"}'
```

### Delete A Team Secret

DELETE

`/v1/team/secrets/{name}`

Delete one version of a secret from the team your API key works in. This action is irreversible. Every type can be deleted, Build Secrets included.

Which version the request deletes:

- **With `?id=`**, it deletes the version with that `id`, from the team's secrets list (`GET /v1/team/secrets`). An `id` that isn't a version of this name in your team returns `404 secret_not_found`.
- **Without `?id=`**, a name with one version has it deleted. A name with no version returns `404 secret_not_found`, and a name with several versions returns `409 secret_name_ambiguous`, listing each version's `id` and `repos`, and deletes nothing.

`{name}` must match a listed name exactly, letter case included, so a request for `NPM_TOKEN` never deletes `npm_token`. URL-encode characters a path can't carry.

Who can delete team secrets follows the same rules as setting them: any member of the team with a user API key or user-scoped token, and the team's service account API keys. When the team lets only admins change secrets, everyone but team admins gets `403 team_admin_required`, service account API keys included. An API key limited to certain repositories gets `403 repository_access`, and an API key that isn't working in a team, or a caller without a seat on the team, gets `403 team_membership_required`.

Each delete is recorded in your team's audit log as a [`cloud_agent_secret` event](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#event-types) with the action `delete`, as a delete in the dashboard is. Agents that start afterward stop getting this version.

#### Path Parameters

`name` string

Secret name, exactly as the team's secrets list shows it.

#### Query Parameters

`id` string (optional)

The `id` of the version to delete, from the team's secrets list or from a `409 secret_name_ambiguous` response.

#### Response Fields

`name` string

Name of the deleted secret.

```bash
curl --request DELETE \
  --url https://api.cursor.com/v1/team/secrets/NPM_TOKEN \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "name": "NPM_TOKEN"
}
```

## Worker Tokens

### Create A User-Scoped Worker Token

POST

`/v1/sub-tokens`

Create a one-hour user-scoped token for a worker to run as an active team member.

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

## Workers and Pools

Monitor worker utilization and build autoscaling for your pools. Durable pools stay registered after the last worker disconnects, so you can scale to zero and bring capacity back when [pending requests](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pending-pool-requests) appear.

The endpoint paths keep the older `private-workers` name; they refer to the same [Self-Hosted Machines workers](https://cursor.com/docs/cloud-agent/self-hosted.md).

Authenticate with the pool's service account API key via Basic auth or Bearer token. Other API key types are rejected.

### List Workers

GET

`/v0/private-workers`

List pool workers for the authenticated service account's team, newest first.

#### Query Parameters

`status` string (optional, default: `all`)

Filter by worker status. One of `all`, `in_use`, or `idle`.

`scope` string (optional, default: `all`)

Filter by worker scope. One of `all`, `team_pool`, or `personal`.

`limit` integer (optional, default: 50)

Results per page. Range: 1 to 100.

`pageToken` string (optional)

Pagination cursor. Pass the `nextPageToken` from the previous response.

#### Response Fields

`workers` array

Connected workers. Each entry includes:

- `workerId` string — Unique worker identifier. Auto-generated ids are UUIDs; workers started with `CURSOR_AGENT_WORKER_ID` report that custom id instead.
- `isInUse` boolean — Whether the worker currently has an assigned agent.
- `repoOwner`, `repoName` string — Primary repository metadata when the worker registered a git remote. Empty strings for any-repo workers.
- `repoUrl` string (optional) — Primary repository URL. Omitted for any-repo workers.
- `workspaceRootPath` string — Primary workspace path on the worker.
- `connectedAtMs` integer — Connection time in Unix milliseconds.
- `userId` integer — Owning user id. `0` for workers authenticated with a service account key.
- `teamId` integer (optional) — Team id for team pool workers.
- `serviceAccountId` string (optional) — Service account that authenticated the worker.
- `activeBcId` string (optional) — Id of the agent currently running on the worker, when in use.
- `name` string (optional) — Worker display name (`--name`, defaults to the machine hostname).

`totalCount` integer

Total workers matching the filter, across all pages.

`nextPageToken` string (optional)

Pagination cursor for `pageToken`. Omitted when there are no more pages.

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers?status=idle&scope=team_pool&limit=50" \
  -u "$CURSOR_API_KEY:"
```

**Response:**

```json
{
  "workers": [
    {
      "workerId": "a8574fe8-248e-424a-a078-7584a2b93724",
      "repoOwner": "acme",
      "repoName": "payments-service",
      "repoUrl": "https://github.com/acme/payments-service",
      "workspaceRootPath": "/home/agent/payments-service",
      "connectedAtMs": 1737306880000,
      "userId": 0,
      "teamId": 456,
      "serviceAccountId": "sa_abc123",
      "isInUse": false,
      "name": "gpu-worker-1"
    }
  ],
  "totalCount": 1
}
```

### Get Worker Summary

GET

`/v0/private-workers/summary`

Return connected and in-use worker counts for the authenticated user and their team. Use this to trigger scaling decisions when utilization is high.

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/summary" \
  -u "$CURSOR_API_KEY:"
```

**Example scaling check:**

```typescript
const summary = await response.json();
const team = summary.teamSummary;
if (team && team.totalConnected > 0) {
  const utilization = team.inUse / team.totalConnected;
  if (utilization >= 0.9) {
    // Scale up: provision additional workers
  }
}
```

### Get Worker By ID

GET

`/v0/private-workers/{id}`

Retrieve a single pool worker by its ID.

#### Path Parameters

`id` string

Unique identifier for the worker (for example, `pw_123`).

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/pw_123" \
  -u "$CURSOR_API_KEY:"
```

### List Pools

GET

`/v0/private-workers/pools`

List durable pools for the authenticated service account's team. Pools remain registered after the last worker disconnects, so you can monitor scale-to-zero fleets and decide when to provision capacity.

#### Query Parameters

`scope` string (optional)

Filter by pool list scope. One of `all`, `team_pool`, or `personal`.

`includeStale` boolean (optional, default: false)

When `true`, include pools marked stale after long inactivity.

#### Response Fields

`pools` array

Registered pools. Each entry includes:

- `scope` string — Pool ownership scope (`user` or `team`).
- `ownerId` integer — Owning user or team id for the scope.
- `poolName` string — Pool name (for example, `default` or `gpu`).
- `connectedWorkerCount` integer — Workers currently connected to this pool.
- `inUseWorkerCount` integer — Connected workers that currently have an assigned agent. Idle capacity is `connectedWorkerCount - inUseWorkerCount`.
- `firstSeenAtMs`, `lastSeenAtMs` integer — First and last observation times in Unix milliseconds.
- `isStale` boolean — Whether the pool is marked stale after long inactivity.
- `repoOwner`, `repoName`, `repoUrl` string (optional) — Repository metadata when the pool is tied to a repo. Omitted for [any-repo pools](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#any-repo-pools).
- `workerReadyTimeoutSeconds` integer — Seconds a claimed request waits for this pool's offline worker to reconnect before the claim expires. `0` means follow-ups for an offline worker reacquire from the pool immediately.

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/pools?scope=team_pool&includeStale=false" \
  -u "$CURSOR_API_KEY:"
```

**Response:**

```json
{
  "pools": [
    {
      "scope": "team",
      "ownerId": 456,
      "poolName": "gpu",
      "repoOwner": "acme",
      "repoName": "payments-service",
      "repoUrl": "https://github.com/acme/payments-service",
      "connectedWorkerCount": 2,
      "inUseWorkerCount": 1,
      "firstSeenAtMs": 1737000000000,
      "lastSeenAtMs": 1737306880000,
      "isStale": false,
      "workerReadyTimeoutSeconds": 900
    },
    {
      "scope": "team",
      "ownerId": 456,
      "poolName": "sandbox",
      "connectedWorkerCount": 0,
      "inUseWorkerCount": 0,
      "firstSeenAtMs": 1737100000000,
      "lastSeenAtMs": 1737200000000,
      "isStale": false,
      "workerReadyTimeoutSeconds": 0
    }
  ]
}
```

The `sandbox` entry is any-repo: repo fields are omitted, and the pool stays selectable with zero connected workers.

### Register A Pool

POST

`/v0/private-workers/pools`

Register a durable pool without starting a worker. Use this to make a pool selectable before any worker connects, for example when a controller provisions capacity on demand. Starting a worker with `--pool` registers the pool implicitly; this endpoint is only needed to create the pool up front.

#### Request Body

`scope` string (required)

Pool ownership scope. One of `user` or `team`.

`poolName` string (required)

Pool name to register (for example, `gpu`).

`repoOwner`, `repoName` string (optional)

Repository metadata when the pool is tied to a repo. Provide both together, or omit both for an any-repo pool.

`repoUrl` string (optional)

Repository URL for display. Requires `repoOwner` and `repoName`.

`workerReadyTimeoutSeconds` integer (optional, default: 0)

Seconds a claimed request waits for an offline worker from this pool to reconnect before the claim expires and the request returns to the queue. Set this when machines [hibernate between turns](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#hibernation) and can be revived. With `0`, follow-ups for an offline worker reacquire from the pool immediately. Must be a non-negative integer.

#### Response Fields

`registered` boolean

Whether the pool was registered.

```bash
curl --request POST \
  --url "https://api.cursor.com/v0/private-workers/pools" \
  -u "$CURSOR_API_KEY:" \
  --header 'Content-Type: application/json' \
  --data '{
    "scope": "team",
    "poolName": "payments-pool",
    "repoOwner": "acme",
    "repoName": "payments-service",
    "repoUrl": "https://github.com/acme/payments-service"
  }'
```

**Response:**

```json
{
  "registered": true
}
```

### Deregister A Pool

DELETE

`/v0/private-workers/pools`

Deregister (soft-delete) a durable pool so it no longer appears in pool pickers or [List Pools](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pools). Workers currently connected to the pool are not affected. Team pools require a team admin; user pools require their owner.

#### Query Parameters

`scope` string (required)

Pool ownership scope. One of `user` or `team`.

`pool_name` string (required)

Pool name to deregister.

`repo_owner` string (optional)

Repository owner when deregistering a repo-scoped pool record.

`repo_name` string (optional)

Repository name when deregistering a repo-scoped pool record. Provide `repo_owner` and `repo_name` together, or omit both for an any-repo pool.

```bash
curl --request DELETE \
  --url "https://api.cursor.com/v0/private-workers/pools?scope=team&pool_name=sandbox" \
  -u "$CURSOR_API_KEY:"
```

**Response:**

```json
{
  "deregistered": true
}
```

### List Pending Pool Requests

GET

`/v0/private-workers/pending-requests`

List pool requests that have not been assigned to a worker yet. Use this endpoint to scale capacity when users are waiting for an available pool worker, or pair it with [Claim A Pending Request](https://cursor.com/docs/cloud-agent/api/endpoints.md#claim-a-pending-request) before starting an ephemeral worker.

For pools configured with `workerReadyTimeoutSeconds`, the listing also surfaces claimed-but-offline entries: requests whose claimed worker is offline while a reconnect window is open. These entries carry `claimedWorkerId` and `wakeTimeoutMs` so a controller can [revive the machine](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#hibernation).

This endpoint requires a service account API key. It returns requests for the key's team and excludes My Machines requests. If the key is scoped to specific repositories, pass `repository`; the repository must be in the key's allowed scope.

The response includes a `streamCursor`. Pass it to [Watch Pending Pool Requests](https://cursor.com/docs/cloud-agent/api/endpoints.md#watch-pending-pool-requests) to follow queue changes in real time after this snapshot.

#### Query Parameters

`limit` number (optional)

Number of pending requests to return. Default: 50, Max: 100.

`pageToken` string (optional)

Pagination cursor from the previous response. Page tokens are bound to the `repository` and `pool` filters that issued them.

`repository` string (optional)

Filter by repository URL. Required for repo-scoped service account API keys. Omit for any-repo pending requests.

`pool` string (optional)

Filter by pool name. Exact, case-sensitive match against the request's `pool` label. Omit to list requests for every pool on the team.

#### Response Fields

`requests` array

Pending requests. Each entry includes:

- `id` string — Pending request / agent id (pass to [Claim](https://cursor.com/docs/cloud-agent/api/endpoints.md#claim-a-pending-request) or [Release A Claim](https://cursor.com/docs/cloud-agent/api/endpoints.md#release-a-claim) as `id`).
- `userId` integer — Cursor user id that created the request.
- `userEmail` string (optional) — Email of the requesting user, when available. Use it to select user-affine capacity without another lookup.
- `serviceAccountId` string (optional) — Service account associated with the request, when present.
- `repoOwner`, `repoName`, `repoUrl` string (optional) — Repository metadata when the request targets a repo. Omitted for any-repo pool requests.
- `labels` array — Request labels as `{ key, value }` pairs (includes `repo=` and `pool=` when set).
- `createdAtMs` integer — Request creation time in Unix milliseconds.
- `claimedWorkerId` string (optional) — Present on claimed-but-offline entries: the request is claimed by this worker, which is currently offline. Start a worker with this id (`CURSOR_AGENT_WORKER_ID`) to resume the agent on its machine.
- `wakeTimeoutMs` integer (optional) — Milliseconds left in the reconnect window of a claimed-but-offline entry. When the window lapses, the claim expires and the request is re-advertised as an unclaimed entry.

`nextPageToken` string (optional)

Pagination cursor. Omitted when there are no more pages. To measure queue depth, paginate to completion and count the requests.

`streamCursor` string

Opaque resume position for [Watch Pending Pool Requests](https://cursor.com/docs/cloud-agent/api/endpoints.md#watch-pending-pool-requests). Every page of one logical listing repeats the same `streamCursor`; open the watch from it after you finish paginating. It expires five minutes after the list that issued it.

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/pending-requests?limit=50&repository=https%3A%2F%2Fgithub.com%2Facme%2Fpayments-service" \
  -u "$CURSOR_API_KEY:"
```

**Response:**

```json
{
  "requests": [
    {
      "id": "bc-00000000-0000-0000-0000-000000000002",
      "userId": 321,
      "userEmail": "owner@acme.example",
      "serviceAccountId": "sa_abc123",
      "repoOwner": "acme",
      "repoName": "payments-service",
      "repoUrl": "https://github.com/acme/payments-service",
      "labels": [
        { "key": "repo", "value": "acme/payments-service" },
        { "key": "pool", "value": "gpu" },
        { "key": "env", "value": "production" }
      ],
      "createdAtMs": 1737306880000
    }
  ],
  "nextPageToken": "eyJjcmVhdGVkQXRNcyI6MTczNzMwNjg4MDAwMH0=",
  "streamCursor": "djQuZXhhbXBsZS1vcGFxdWUtY3Vyc29y"
}
```

`repoUrl` omits embedded credentials when the original repository URL includes userinfo.

### Watch Pending Pool Requests

GET

`/v0/private-workers/pending-requests/stream`

Stream pending-request lifecycle events over Server-Sent Events (SSE) so controllers can react to queue changes without polling.

This endpoint requires a service account API key. Controllers list-then-watch: call [List Pending Pool Requests](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pending-pool-requests) to build your view of the queue, keep the response's `streamCursor`, then open the watch from that exact position. Use the same `repository` and `pool` filters for the list and the watch; cursors are bound to the filters that issued them.

#### Query Parameters

`cursor` string (required)

The `streamCursor` from a list response, or the SSE `id:` of the last event you processed. On reconnect, a native `EventSource` resends that id as the `Last-Event-ID` header, which takes precedence over the query parameter.

`repository` string (optional)

Same semantics as [List Pending Pool Requests](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pending-pool-requests). Required for repo-scoped service account API keys. Pagination parameters are not accepted on the stream.

`pool` string (optional)

Watch only events for this pool. Exact, case-sensitive match against the request's `pool` label. Must match the filter used by the list that issued the cursor. Omit to watch every pool on the team.

#### Events

The watch replays the retained transitions after the cursor, then follows live. Every event's SSE `id:` is the cursor to resume from if the connection drops.

- `created` event — A request entered the queue, including a claimed-but-offline request whose reconnect window lapsed and whose claim expired. Payload: the same request object as [List Pending Pool Requests](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pending-pool-requests).
- `claimed` event — A worker claimed the request, or an offline worker reconnected and resumed its claimed request. Payload: `{ id }`.
- `claimed_offline` event — A follow-up arrived for a request whose claimed worker is offline. Payload: the same request object as [List Pending Pool Requests](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pending-pool-requests), including `claimedWorkerId` and `wakeTimeoutMs`. [Revive the machine](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#hibernation) before the window lapses, or the claim expires and the request is re-advertised with a fresh `created` event.
- `expired` event — The request left the queue without being claimed. Payload: `{ id }`.
- `heartbeat` event — Cursor checkpoint with no state change, sent about every 20 seconds on a quiet stream. Payload: `{}`. Heartbeats advance an idle watch's resume position but do not extend the cursor's lifetime.

#### Cursor lifetime

Every cursor in a watch chain expires **five minutes after the list that issued it**. Heartbeats and reconnects do not extend it. When the cursor expires, or the retained event window no longer covers it, the endpoint returns HTTP `410 Gone` with `{"code": "cursor_expired"}`: re-list and watch from the fresh `streamCursor`. This is routine, not an error path. Re-list proactively on a five-minute timer with jitter instead of riding the `410`, so a fleet of controllers does not synchronize its list calls.

#### Delivery guarantees

Delivery is best-effort, and the list is the source of truth. Events are published after each transition commits, with retries, but a rare failure can drop one, and a dropped event is never redelivered. Between re-lists, treat events as low-latency hints: apply them idempotently (upsert `created` and `claimed_offline` requests, remove `claimed` and `expired` requests by `id`) and let the next list correct any drift. A `claimed` event for a request you never saw is a no-op. Claims stay atomic server-side regardless of your local view.

Do not persist cursors. A service account can hold at most four concurrent streams; use one stream per controller and fan out locally.

```bash
curl --request GET --no-buffer \
  --url "https://api.cursor.com/v0/private-workers/pending-requests/stream?cursor=$STREAM_CURSOR" \
  --header 'Accept: text/event-stream' \
  -u "$CURSOR_API_KEY:"
```

**Example stream:**

```
: connected

event: heartbeat
id: djQuY3Vyc29yLWNoZWNrcG9pbnQ
data: {}

event: created
id: djQuY3Vyc29yLWFmdGVyLWNyZWF0ZWQ
data: {"id":"bc-00000000-0000-0000-0000-000000000002","userId":321,"userEmail":"owner@acme.example","repoOwner":"acme","repoName":"payments-service","repoUrl":"https://github.com/acme/payments-service","labels":[{"key":"pool","value":"gpu"}],"createdAtMs":1737306880000}

event: claimed
id: djQuY3Vyc29yLWFmdGVyLWNsYWltZWQ
data: {"id":"bc-00000000-0000-0000-0000-000000000002"}
```

**The controller loop:**

1. [List pending requests](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pending-pool-requests) to completion and replace your local view with the result. Keep the response's `streamCursor`.
2. Open the watch with `?cursor=<streamCursor>` and apply events to your local view. Track the latest event `id:` you processed.
3. On disconnect, reconnect with the latest event id as `?cursor=`, or rely on a native `EventSource`, which resends it as `Last-Event-ID` automatically.
4. On HTTP `410 Gone`, go back to step 1 and re-list.

### Claim A Pending Request

POST

`/v0/private-workers/claim`

Reserve a pending pool request for a specific worker before that worker starts. Controllers use this to atomically assign work across replicas: read [pending requests](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pending-pool-requests), claim one, then start a worker with a stable worker id that matches the claim.

A second claim while a live claim exists is rejected. [Release A Claim](https://cursor.com/docs/cloud-agent/api/endpoints.md#release-a-claim) first, then claim a new `workerId`.

This endpoint requires a service account API key.

#### Request Body

`id` string (required)

Pending request id. Same value as `id` from [List Pending Pool Requests](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pending-pool-requests).

`workerId` string (required)

Worker id to reserve for the request. Start the worker with the same id via `CURSOR_AGENT_WORKER_ID` (or the hidden `--worker-id` flag) so the bridge registers the claimed identity.

`sessionToken` boolean (optional, default: `false`)

Also mint a [session token](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#session-tokens) for this claim, so the worker can start without the service account key. If the token can't be minted, the claim fails and the request stays unclaimed.

#### Response Fields

`id`, `workerId` string

The claimed request and worker id.

`token` string (optional)

Session token that serves only this claim. Present when the request sent `sessionToken: true`. It stops working when the claim is released, or when the API key that minted it is deleted or expires.

`expiresAt` string (optional)

ISO 8601 timestamp, 7 days after minting. Present with `token`.

```bash
curl --request POST \
  --url "https://api.cursor.com/v0/private-workers/claim" \
  -u "$CURSOR_API_KEY:" \
  --header 'Content-Type: application/json' \
  --data '{
    "id": "bc-00000000-0000-0000-0000-000000000002",
    "workerId": "pw_123"
  }'
```

**Response:**

```json
{
  "id": "bc-00000000-0000-0000-0000-000000000002",
  "workerId": "pw_123"
}
```

After a successful claim, start the worker with the reserved id:

```bash
export CURSOR_API_KEY="your-service-account-api-key"
export CURSOR_AGENT_WORKER_ID="pw_123"
agent worker --pool gpu --worker-dir /workspace start
```

If the worker can't start, [Fail A Claim](https://cursor.com/docs/cloud-agent/api/endpoints.md#fail-a-claim) so the agent's turn ends with your reason instead of waiting.

With a session token:

```bash
curl --request POST \
  --url "https://api.cursor.com/v0/private-workers/claim" \
  -u "$CURSOR_API_KEY:" \
  --header 'Content-Type: application/json' \
  --data '{
    "id": "bc-00000000-0000-0000-0000-000000000002",
    "workerId": "pw_123",
    "sessionToken": true
  }'
```

**Response:**

```json
{
  "id": "bc-00000000-0000-0000-0000-000000000002",
  "workerId": "pw_123",
  "token": "eyJ...",
  "expiresAt": "2026-10-02T21:00:00.000Z"
}
```

Start the worker with the token instead of the key:

```bash
printf '%s' "$TOKEN" > /run/cursor/token
export CURSOR_AGENT_WORKER_ID="pw_123"
agent worker --pool gpu --worker-dir /workspace --auth-token-file /run/cursor/token start
```

### Create A Session Token

POST

`/v0/private-workers/tokens`

Mint a [session token](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#session-tokens) for a claim your team already holds. Use it when a worker reconnects to an existing claim, such as a revived hibernated machine, or when a run outlasts its token. `agent worker controller --session-token` calls this for you when it wakes a hibernated machine.

The token serves only this claim. It stops working when the claim is released, or when the API key that minted it is deleted or expires.

This endpoint requires an agent-scoped service account API key from the team that holds the claim. A repository-scoped key can mint tokens only for agents on repositories in its scope.

#### Request Body

`id` string (required)

Agent id the claim is for. Same value as `id` on [Claim A Pending Request](https://cursor.com/docs/cloud-agent/api/endpoints.md#claim-a-pending-request).

`workerId` string (required)

Worker id the claim binds to the agent.

```bash
curl --request POST \
  --url "https://api.cursor.com/v0/private-workers/tokens" \
  -u "$CURSOR_API_KEY:" \
  --header 'Content-Type: application/json' \
  --data '{
    "id": "bc-00000000-0000-0000-0000-000000000002",
    "workerId": "pw_123"
  }'
```

**Response:**

```json
{
  "id": "bc-00000000-0000-0000-0000-000000000002",
  "workerId": "pw_123",
  "token": "eyJ...",
  "expiresAt": "2026-10-02T21:00:00.000Z"
}
```

HTTP `404` means your team holds no claim binding that worker to that agent.

### Release A Claim

POST

`/v0/private-workers/claims/{id}/release`

Release the claim that binds an agent to its self-hosted worker so the worker can serve another agent.

When no turn is using the worker, release frees it immediately. Cursor clears the claim and the agent's worker assignment together, returns a waiting follow-up to the pool queue as an unclaimed request, and tells the worker CLI to exit. The agent's next turn runs on another worker. A replacement worker can claim the agent as soon as release returns.

While a turn is using the worker, release returns HTTP `400` and changes nothing. A turn is using the worker when the agent's [status](https://cursor.com/docs/cloud-agent/api/endpoints.md#get-an-agent) is `ACTIVE`, the worker is connected, and the claim isn't waiting for a [hibernated](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#hibernation) machine to wake. If Cursor can't read the worker's connection state, it counts the worker as connected. Retry after the turn ends, or [cancel the active run](https://cursor.com/docs/cloud-agent/api/endpoints.md#cancel-a-run) and release again.

A second [Claim A Pending Request](https://cursor.com/docs/cloud-agent/api/endpoints.md#claim-a-pending-request) while a live claim exists is rejected. Release first, then claim a new `workerId`.

`--idle-release-timeout` (env var `CURSOR_WORKER_IDLE_RELEASE_TIMEOUT`) makes the worker CLI exit on its own after idle.

This endpoint requires a service account API key.

#### Path Parameters

`id` string

Pending request / agent id. Same value as `id` on [Claim A Pending Request](https://cursor.com/docs/cloud-agent/api/endpoints.md#claim-a-pending-request). No request body.

```bash
curl --request POST \
  --url "https://api.cursor.com/v0/private-workers/claims/bc-00000000-0000-0000-0000-000000000002/release" \
  -u "$CURSOR_API_KEY:"
```

**Response:**

```json
{
  "id": "bc-00000000-0000-0000-0000-000000000002",
  "workerId": "pw_123"
}
```

HTTP `400` means a turn is using the worker. Nothing changed. Retry after the turn ends:

```json
{
  "error": "Worker in use: The agent is mid-turn on this worker; retry after the turn ends, or stop the agent to free the worker now"
}
```

HTTP `404` means there is no live claim: already released, expired, or adopted. Do not retry a 404.

### Fail A Claim

POST

`/v0/private-workers/claims/{id}/fail`

Report that you can't start the worker you claimed for an agent, for example because your infrastructure is out of quota or is missing a permission. Instead of waiting for a worker that won't connect, the agent's turn ends with your reason as its error the next time it checks for the worker.

The person who started the agent sees `Your team's self-hosted pool couldn't start a worker for this agent:` followed by your message. When the agent runs from Slack, Cursor posts the same text in the thread with a **Try Again** button.

Once the turn has ended, Cursor frees the claim. The agent's next turn, including a Try Again, returns to the pool queue as an unclaimed request that any worker can [claim](https://cursor.com/docs/cloud-agent/api/endpoints.md#claim-a-pending-request).

You can fail a claim only while a turn is waiting on it: the agent's [status](https://cursor.com/docs/cloud-agent/api/endpoints.md#get-an-agent) is `ACTIVE` and the claimed worker isn't connected. Otherwise the endpoint returns HTTP `400` and changes nothing. If Cursor can't read the worker's connection state, it counts the worker as connected. To free a claim when no turn is waiting, use [Release A Claim](https://cursor.com/docs/cloud-agent/api/endpoints.md#release-a-claim).

If the claimed worker connects, or the claim ends, before the turn picks up your report, Cursor discards the report.

This endpoint requires an agent-scoped service account API key from the team that holds the claim. A repository-scoped key can fail claims only for agents on repositories in its scope.

#### Path Parameters

`id` string

Agent id the claim is for. Same value as `id` on [Claim A Pending Request](https://cursor.com/docs/cloud-agent/api/endpoints.md#claim-a-pending-request).

#### Request Body

`message` string (required)

Plain-text reason shown to the agent's user. Cursor removes control characters other than newlines and tabs and trims surrounding whitespace. The result must be 1 to 500 characters. Other body fields are rejected.

#### Response Fields

`id`, `workerId` string

The agent and the worker the failed claim was bound to.

```bash
curl --request POST \
  --url "https://api.cursor.com/v0/private-workers/claims/bc-00000000-0000-0000-0000-000000000002/fail" \
  -u "$CURSOR_API_KEY:" \
  --header 'Content-Type: application/json' \
  --data '{
    "message": "The gpu pool has reached its limit of 20 machines. Try again in a few minutes."
  }'
```

**Response:**

```json
{
  "id": "bc-00000000-0000-0000-0000-000000000002",
  "workerId": "pw_123"
}
```

HTTP `400` with `No turn waiting` means the agent isn't `ACTIVE`. Nothing changed. Release the claim instead:

```json
{
  "error": "No turn waiting: The agent is not running, so no turn is waiting on this claim; release the claim instead"
}
```

HTTP `400` with `Worker connected` means the claimed worker is connected and serving the turn. Nothing changed:

```json
{
  "error": "Worker connected: The claimed worker is connected and serving the agent; stop the agent or release the claim after the turn ends"
}
```

HTTP `400` with neither title means the body is invalid: `message` is missing, not a string, empty, or longer than 500 characters, or the body has other fields.

HTTP `404` means the agent isn't a self-hosted agent on your team, or it holds no claim. Do not retry a 400 or 404. Retry a 5xx; reporting the same claim again is safe.

## Metadata Endpoints

### API Key Info

GET

`/v1/me`

Retrieve information about the API key being used for authentication.

#### Response Fields

`apiKeyName` string

Display name of the API key.

`createdAt` string

When the API key was created (ISO 8601).

`userId` integer (user-scoped keys)

Numeric Cursor user ID of the API key's owner. Omitted for service-account / team API keys, which aren't tied to a specific user.

`userEmail` string (user-scoped keys)

Email address of the API key's owner.

`userFirstName`, `userLastName` string (user-scoped keys)

First and last name of the API key's owner, when populated.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/me \
  -u YOUR_API_KEY:
```

**Response (user-scoped key):**

```json
{
  "apiKeyName": "Production API Key",
  "userId": 42,
  "createdAt": "2026-04-13T18:30:00.000Z",
  "userEmail": "developer@example.com",
  "userFirstName": "Alex",
  "userLastName": "Rivera"
}
```

**Response (service-account key):**

```json
{
  "apiKeyName": "Production Service Account",
  "createdAt": "2026-04-13T18:30:00.000Z"
}
```

### List Models

GET

`/v1/models`

Returns the recommended models you can pass to the `model.id` field on [Create An Agent](https://cursor.com/docs/cloud-agent/api/endpoints.md#create-an-agent), along with the parameters and variants each model accepts. Model parameters use the same `model.params` shape as the [TypeScript SDK ModelSelection](https://cursor.com/docs/sdk/typescript.md#modelselection).

To use the configured default model, omit `model` from the request body entirely. Cursor resolves your user default model, then your team default model, then a system default.

#### Response Fields

Each item in `items` describes one model:

`id` string

Pass this value as `model.id` when creating an agent.

`displayName` string

Human-readable name shown in the Cursor UI.

`description` string (optional)

Short description of the model.

`aliases` array (optional)

Alternate IDs that resolve to the same model (for example, `composer-latest`).

`parameters` array (optional)

Per-model parameter definitions. Each entry has an `id`, optional `displayName`, and a `values` array of permitted `{ value, displayName? }` entries. Use these to populate `model.params` on the create request.

`variants` array (optional)

Concrete `id`+`params` combinations the model accepts. Each entry has a `params` array (which may be empty), a `displayName`, an optional `description`, and an optional `isDefault` flag.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/models \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "id": "composer-2",
      "displayName": "Composer 2",
      "aliases": ["composer-latest", "composer"],
      "parameters": [
        {
          "id": "fast",
          "displayName": "Fast",
          "values": [
            { "value": "false" },
            { "value": "true", "displayName": "Fast" }
          ]
        }
      ],
      "variants": [
        {
          "params": [{ "id": "fast", "value": "true" }],
          "displayName": "Composer 2",
          "isDefault": true
        },
        {
          "params": [{ "id": "fast", "value": "false" }],
          "displayName": "Composer 2"
        }
      ]
    },
    {
      "id": "claude-4.6-sonnet-thinking",
      "displayName": "Claude 4.6 Sonnet (Thinking)",
      "variants": [
        {
          "params": [],
          "displayName": "Claude 4.6 Sonnet (Thinking)",
          "isDefault": true
        }
      ]
    }
  ]
}
```

### List GitHub Repositories

GET

`/v1/repositories`

List GitHub repositories accessible to the authenticated user through Cursor's GitHub App installation.

This endpoint returns GitHub repositories only. Repositories on GitLab, Bitbucket Cloud, and Azure DevOps are not listed here, even though you can create agents against them with [Create An Agent](https://cursor.com/docs/cloud-agent/api/endpoints.md#create-an-agent).

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
