---
source_url: https://cursor.com/docs/cloud-agent/self-hosted-pool
---

# Self-Hosted Pool

Self-Hosted Pool is for teams that want Cloud Agents to run inside company-managed infrastructure. Instead of each developer starting a worker on a personal machine, admins operate a pool of workers that can be assigned to agents across the organization.

Use a pool when you need:

- Centrally managed workers for a team or organization
- Service account authentication instead of individual browser logins
- Kubernetes, autoscaling, or fleet management
- Labels that route work to the right environment, team, repo, or hardware profile
- Enterprise controls around network access, secrets, build outputs, and monitoring

For a fast personal setup, see [My Machines](https://cursor.com/docs/cloud-agent/my-machines.md).

## How it works

A worker opens a long-lived outbound HTTPS connection to Cursor's cloud. The agent loop (inference and planning) runs in Cursor's cloud and sends tool calls over this connection. The worker executes those tool calls locally in your infrastructure: terminal commands, file edits, browser actions, and access to internal services.

Your repos, build caches, secrets, and tool execution stay in your environment while Cursor handles orchestration, model access, and the Cloud Agent experience. Cloud Agent [artifacts](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#artifacts), like screenshots and videos, are uploaded to Cursor so you can view them in PRs and the dashboard.

Workers only need outbound access. No inbound ports, public IPs, or VPN tunnels are required. See [Networking](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#networking) for the full list of required hosts.

Self-Hosted Cloud Agents support up to 10 workers per user and 50 per team. For larger company-wide deployments, [contact us](https://cursor.com/contact-sales?source=self-hosted-agents) to discuss scaling.

## Prerequisites

- A **Cursor team plan**
- Self-hosted settings configured by a team admin in the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#self-hosted-agents):
  - **Allow Self-Hosted Agents** lets users opt in to self-hosted runs.
  - **Require Self-Hosted Agents** routes every Cloud Agent run to self-hosted workers.
- A [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md) for pool worker authentication
- A worker machine or image with:
  - `agent` CLI installed
  - `git` installed and available on `PATH`
  - A cloned repository with a configured remote
  - Access to the build tools, package registries, secrets, and internal services your agents need

## Install the CLI

```bash
# macOS, Linux, and WSL
curl https://cursor.com/install -fsS | bash

# Windows PowerShell
irm 'https://cursor.com/install?win32=true' | iex
```

Confirm the CLI is available:

```bash
agent --version
```

## Authenticate workers

Pool workers must authenticate with a [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md).

User, personal, team, and organization API keys can't start pool workers. Use personal or user API keys with personal workers on [My Machines](https://cursor.com/docs/cloud-agent/my-machines.md).

```bash
export CURSOR_API_KEY="your-service-account-api-key"
```

You can also pass the key directly:

```bash
agent worker start --api-key "your-service-account-api-key"
```

## Start a pool worker

Run the worker from the git repo it should serve:

```bash
cd /path/to/repo
agent worker start --pool
```

`--pool` registers the worker for pool assignment. Each Cloud Agent session claims one worker at a time. For orchestrated environments, combine it with `--idle-release-timeout` so the process exits cleanly after work completes:

```bash
agent worker start --pool --idle-release-timeout 600
```

`--idle-release-timeout` keeps the worker alive for a window (in seconds) after a session ends to handle follow-up messages. If a follow-up arrives, the timer resets. Once the timeout fires, the CLI exits with code 0.

## Pool names

Group pool workers under a name when you want sessions to route to a specific subset, like GPU machines, a staging fleet, or a team's dedicated build boxes.

The `--pool-name` flag tags the worker with a `pool=<name>` label the backend uses for routing:

```bash
agent worker start --pool --pool-name gpu
```

When `--pool-name` is omitted, the worker joins the `default` pool. Workers from CLI versions that predate the flag also match the default pool, so you can roll out pool names gradually without disrupting existing fleets.

Set the pool name from the environment when an orchestrator injects config:

```bash
export CURSOR_WORKER_POOL_NAME=gpu
agent worker start --pool
```

`--pool-name` requires `--pool` (or the legacy `--single-use` alias). Multi-use workers don't belong to a pool.

From the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents), pick a pool in the worker selector when starting a session or editing an automation. You can also include `pool=<name>` in a Slack, GitHub, or Linear trigger. Sessions route only to workers registered with that pool name.

## Triggering pool agents

Use pool triggers when you want a Cloud Agent to run on your team's shared worker fleet. Pool workers are the right target for centrally managed capacity, autoscaling, CI-like runners, and repo-scoped infrastructure.

Team admins control self-hosted routing from the Self-Hosted section of the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents). **Allow Self-Hosted Agents** lets users opt in per request. Without opt-in, runs use Cursor's managed infrastructure. **Require Self-Hosted Agents** routes Cloud Agent runs to self-hosted workers.

When Cursor starts a pool agent, it matches workers with labels. Every pool request includes a `repo=<owner/repo>` label. Requests for a named pool also include `pool=<name>`.

Pool workers handle:

- Runs covered by **Require Self-Hosted Agents**, unless the request targets a specific My Machines worker with `worker=` or `machine=`
- Requests with `self_hosted=true`, `self_hosted`, or `selfhosted`
- Requests with `pool=<name>`, which also selects that named pool
- Self-hosted requests with repository selection from the trigger surface, such as `repo=<owner/repo>` where supported

`repo=` selects the repository for the run. For self-hosted pool runs, that repository becomes the `repo=<owner/repo>` worker label. It does not target a personal machine.

Use these options from integrations to start pool agents:

- **Slack**: Mention `@Cursor` with `self_hosted=true`, standalone `self_hosted`, `selfhosted`, or `pool=<name>`. Legacy aliases like `private_worker=true`, `useprivateworker`, and `useprivateworkers=false` still work.
- **GitHub**: Comment `@cursoragent self_hosted=true ...` or `@cursoragent pool=<name> ...` on an issue, pull request, or review comment. The legacy `private_worker=true` alias still works.
- **Linear**: Add `pool=<name>` or `[pool=<name>]` to the issue body. You can also use issue or project labels where the parent label is `pool` and the child label is the value. Linear does not parse standalone `self_hosted=true`.

Policy handling depends on where the request starts:

- **Slack** rejects self-hosted opt-in when Allow Self-Hosted Agents is off and replies in Slack. If Require Self-Hosted Agents is on, every Slack mention runs self-hosted.
- **GitHub** lets repo `OWNER` and `COLLABORATOR` users route runs to self-hosted workers. Other commenters run on managed infrastructure when they opt in, or are skipped if Require Self-Hosted Agents is on. This protects public repos where outside contributors can leave comments.
- **Linear** rejects explicit self-hosted requests when Allow Self-Hosted Agents is off. The issue gets an agent activity error that asks an admin to turn on self-hosted workers or remove the hint to run on Cursor's managed infrastructure.

To target one of your own machines by name, use [My Machines](https://cursor.com/docs/cloud-agent/my-machines.md#trigger-this-machine-from-a-chat-surface) with `worker=` or `machine=`.

The Cloud Agent API uses the same resolver with `usePrivateWorker` and `labels` fields. See the [Cloud Agent API docs](https://cursor.com/docs/cloud-agent/api/endpoints.md) for endpoint details.

## Hooks

Self-hosted workers run project hooks committed in your repository through `.cursor/hooks.json`.

If you're on Enterprise, self-hosted workers also support team hooks and enterprise-managed hooks.

See [Hooks](https://cursor.com/docs/hooks.md) for configuration details.

## Labels

Labels are key-value pairs that describe a worker. They control how Cloud Agent sessions route to the right pool.

### CLI flags

Good for quick testing or small pools:

```bash
agent worker start --pool \
  --label team=backend \
  --label env=production
```

### JSON file

Better for production where labels are managed as config:

```json
{
  "team": "backend",
  "env": "production",
  "capabilities": ["docker", "gpu"]
}
```

```bash
agent worker start --pool --labels-file labels.json
```

### TOML file

Same as JSON, different format:

```toml
team = "backend"
env = "production"
capabilities = ["docker", "gpu"]
```

```bash
agent worker start --pool --labels-file labels.toml
```

### Environment variable

Useful when the path is injected by your orchestrator:

```bash
export CURSOR_WORKER_LABELS_FILE=/path/to/labels.json
agent worker start --pool
```

The `repo` and `pool` labels are reserved. `repo` comes from the worker directory's git remote. `pool` is set by [`--pool-name`](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#pool-names). Don't set either manually.

## MCP servers

MCP servers on self-hosted workers are routed by transport type:

| Transport        | Runs on        | Use case                                                                                                               |
| ---------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Command (stdio)  | Worker         | The MCP process starts on the worker and can reach private networks, internal APIs, and services behind your firewall. |
| HTTP / SSE (url) | Cursor backend | Cursor handles OAuth, session caching, and auth for HTTP-based MCP servers.                                            |

If your MCP server needs to access private-network endpoints, use the command (stdio) transport. The process runs directly on the worker and shares its network. For HTTP-based MCP servers, Cursor manages the connection from its backend, handling OAuth and session caching.

## Artifacts

Artifact behavior is identical on self-hosted workers and Cursor-hosted agents. The agent produces the artifact inside the worker and the worker uploads it to Cursor-managed storage over HTTPS. Everything downstream (PR embeds, dashboard previews, notification attachments) is handled by Cursor's backend and doesn't depend on where the worker runs.

Artifacts are on by default. See [Capabilities](https://cursor.com/docs/cloud-agent/capabilities.md#demos-and-artifacts) for what they look like in the UI.

To disable artifact uploads, block outbound traffic to `cloud-agent-artifacts.s3.us-east-1.amazonaws.com`. The agent session keeps working; artifacts produced during the session fail to upload.

## Networking

Workers need outbound HTTPS access to:

- `api2.cursor.sh` and `api2direct.cursor.sh` for the agent session
- `cloud-agent-artifacts.s3.us-east-1.amazonaws.com` for [artifact](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#artifacts) uploads

If your firewall can only match wildcards, `*.s3.us-east-1.amazonaws.com` covers the artifact host, but also opens every other bucket in the region. Prefer an exact-host rule when the firewall supports it.

No inbound ports, public IPs, or VPN tunnels are required. If you use a proxy, set `HTTPS_PROXY` or `https_proxy` in the worker environment.

### Failure modes

| If you block...                                       | Effect                                                                                                                                                                        |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api2.cursor.sh` or `api2direct.cursor.sh`            | The worker can't start or continue an agent session.                                                                                                                          |
| `cloud-agent-artifacts.s3.us-east-1.amazonaws.com`    | Artifact uploads fail. PR embeds, dashboard previews, and notification attachments that depend on artifacts are missing. The agent session and other tool calls keep working. |
| An outbound host a specific tool or integration needs | Only that tool or integration fails. The agent continues.                                                                                                                     |

The [Prerequisites](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#prerequisites) section covers the broader set of hosts a worker needs during agent runs (git hosts, package registries, internal APIs).

## Kubernetes

We provide a Helm chart and Kubernetes operator for managing worker pools at scale. See the [Kubernetes deployment guide](https://cursor.com/docs/cloud-agent/self-hosted-k8s.md) for setup instructions.

## Fleet management API

For non-Kubernetes environments, use the fleet management API to monitor utilization and build autoscaling.

Authenticate with the pool's service account API key via Basic auth or Bearer token. Other API key types can't manage pool worker fleet capacity.

### List workers

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers?status=idle&limit=50" \
  -u "$CURSOR_API_KEY:"
```

\| Parameter | Type | Default | Description |
\|---|---|---|
\| `status` | `all` | `in_use` | `idle` | `all` | Filter by worker status |
\| `limit` | integer (1-100) | 50 | Results per page |
\| `nextPageToken` | string | | Pagination cursor |

### Get summary

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/summary" \
  -u "$CURSOR_API_KEY:"
```

Returns connected and in-use counts for your user and team. Use this to trigger scaling when utilization is high:

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

### Get worker by ID

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/pw_123" \
  -u "$CURSOR_API_KEY:"
```

## Monitoring

The management server exposes `GET /metrics`, `GET /healthz`, and `GET /readyz` when you start a worker with `--management-addr`:

```bash
agent worker start --pool --management-addr ":8080"
```

Scrape metrics from your worker:

```bash
curl http://localhost:8080/metrics
```

### Available metrics

**Gauges**

| Metric                                                 | Type  | Description                                                                                |
| ------------------------------------------------------ | ----- | ------------------------------------------------------------------------------------------ |
| `cursor_self_hosted_worker_connected`                  | Gauge | `1` when the outbound connection to Cursor's cloud is active, `0` otherwise.               |
| `cursor_self_hosted_worker_session_active`             | Gauge | `1` when a cloud agent session is running on this worker, `0` when idle.                   |
| `cursor_self_hosted_worker_last_activity_unix_seconds` | Gauge | Unix timestamp of the last frame or heartbeat from Cursor's cloud. `0` if no activity yet. |

**Counters**

| Metric                                             | Type    | Description                                               |
| -------------------------------------------------- | ------- | --------------------------------------------------------- |
| `cursor_self_hosted_worker_connect_attempts_total` | Counter | Outbound connection attempts to Cursor's cloud.           |
| `cursor_self_hosted_worker_connect_retry_total`    | Counter | Connection retries after a failed attempt.                |
| `cursor_self_hosted_worker_session_ends_total`     | Counter | Agent sessions ended on this worker, labeled by `reason`. |

### Session end reasons

The `cursor_self_hosted_worker_session_ends_total` counter includes a `reason` label with one of these values:

| Reason               | Description                                                      |
| -------------------- | ---------------------------------------------------------------- |
| `stream_end`         | Connection closed normally.                                      |
| `stream_error`       | Connection failed with an error.                                 |
| `session_closed`     | HTTP/2 session closed cleanly.                                   |
| `session_error`      | HTTP/2 session entered an error state.                           |
| `connection_timeout` | Initial connection timed out before streaming started.           |
| `session_aborted`    | Session was aborted, for example because the worker was stopped. |

## Security

**Data flow.** Two things leave your network: file chunks the model reads during inference, and Cloud Agent [artifacts](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#artifacts) (screenshots, videos, and log references) the worker uploads to Cursor-managed storage so they can appear in PRs and the dashboard. Your repos, build caches, and secrets stay on your machines.

**Outbound-only.** Workers connect outbound over HTTPS. No inbound ports or firewall changes required.

**Privacy mode.** Self-hosted Cloud Agents respect Cursor's [privacy mode](/data-use), which enables zero data retention across all model providers. None of your code is stored or used for training.

**Isolation.** Each agent session gets its own dedicated worker. Sessions are not shared across workers.

**Authentication.** Pool workers authenticate with a [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md). Other API key types are rejected.

**Dashboard visibility.** Team admins can see all connected workers. Team members see only workers assigned to them.

## CLI reference

```bash
agent worker start [options]
```

| Flag                           | Env var                              | Description                                                                                                                                                                                     |
| ------------------------------ | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--worker-dir <path>`          |                                      | Working directory. Must be a git repo. Default: current directory.                                                                                                                              |
| `--management-addr <addr>`     |                                      | Address for `/healthz`, `/readyz`, and `/metrics` endpoints, for example `:8080`.                                                                                                               |
| `--label <key=value>`          |                                      | Add a label. Repeatable. Mutually exclusive with `--labels-file`.                                                                                                                               |
| `--labels-file <path>`         | `CURSOR_WORKER_LABELS_FILE`          | Path to JSON or TOML labels file. Mutually exclusive with `--label`.                                                                                                                            |
| `--idle-release-timeout <sec>` | `CURSOR_WORKER_IDLE_RELEASE_TIMEOUT` | Seconds to stay connected after a session ends. Default: no timeout.                                                                                                                            |
| `--pool`                       |                                      | Register for pool assignment. Each session claims one worker at a time.                                                                                                                         |
| `--single-use`                 |                                      | Legacy alias for `--pool`.                                                                                                                                                                      |
| `--pool-name <name>`           | `CURSOR_WORKER_POOL_NAME`            | Pool label for pool-managed workers. Requires `--pool`. Default: `default`.                                                                                                                     |
| `--api-key <key>`              | `CURSOR_API_KEY`                     | Service account API key for pool workers.                                                                                                                                                       |
| `--auth-token <token>`         |                                      | Pre-minted access token. Used by the Kubernetes operator and other automation that exchanges an API key for a short-lived token externally.                                                     |
| `--auth-token-file <path>`     |                                      | File containing an access token. The CLI re-reads this file when reconnecting after an auth failure or disconnect, which lets a controller rotate the mounted token without restarting the pod. |
| `-e, --endpoint <url>`         |                                      | API endpoint. Default: `https://api2.cursor.sh`.                                                                                                                                                |

## FAQ

### How should I size workers?

There is no fixed worker spec. Size each worker the same way you size a CI
runner or devbox for the repo it serves.

Each worker needs enough CPU, memory, disk, and network access to clone the
repo and run the builds, tests, and tools your agents need.

### Can I bake skills into the worker image?

Yes. Project-level skills in `.cursor/skills/` or `.agents/skills/` are
automatically available on self-hosted workers.

To share skills across a team, check them into the repo or bake them into
your custom worker image.

### Do MCP servers work on self-hosted workers?

Yes. Configure MCP servers through the Cloud Agents dashboard. See the
[MCP servers](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#mcp-servers) section for how routing works by transport type.

## Related

- [My Machines](https://cursor.com/docs/cloud-agent/my-machines.md)
- [Kubernetes deployment guide](https://cursor.com/docs/cloud-agent/self-hosted-k8s.md)
- [Cloud Agent security and network](https://cursor.com/docs/cloud-agent/security-network.md)
- [Service accounts](https://cursor.com/docs/account/enterprise/service-accounts.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
