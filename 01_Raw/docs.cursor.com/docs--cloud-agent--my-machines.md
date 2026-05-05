---
source_url: https://cursor.com/docs/cloud-agent/my-machines
---

# My Machines

My Machines lets you run Cloud Agents on a machine you already use: your laptop, a devbox, or a remote VM. It is the fastest way to give Cloud Agents access to your local repo, dependencies, build cache, and private network.

A worker on your machine opens an outbound connection to Cursor. The agent loop runs in Cursor's cloud, but terminal commands, file edits, browser actions, and other tool calls execute on your machine. No inbound ports or firewall changes are required.

Use My Machines when you want to:

- Use a devbox or remote workstation that already has your repo and tools
- Run Cloud Agents against services only available from your network
- Keep build caches, test outputs, and secrets on your machine
- Try self-hosted Cloud Agents quickly

For org-wide worker fleets, see [Self-Hosted Pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md).

## Quickstart

### 1. Install the CLI

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

### 2. Sign in

For a personal machine, browser login is the easiest path:

```bash
agent login
```

### 3. Start the worker

```bash
agent worker start
```

Keep this process running while you use the machine. By default, a My Machines worker is long-lived: it stays connected until you stop it and can be reused for future Cloud Agent sessions.

### 4. Run an agent

1. Go to [cursor.com/agents](https://cursor.com/agents).
2. The machine should show up in the environment dropdown.
3. Send a task.

## Common options

### Name the machine

Use a friendly name when you have multiple machines for the same repo:

```bash
agent worker start --name "my-devbox"
```

### Run from a different repo directory

```bash
agent worker start --worker-dir /path/to/repo
```

### Use an API key

For shared devboxes or automation, use a service account API key:

```bash
agent worker start --api-key "your-api-key"
```

### Use a user-scoped token

For self-managed per-user workers, mint a short-lived user-scoped token with [`POST /v1/sub-tokens`](https://cursor.com/docs/cloud-agent/api/endpoints.md#create-a-user-scoped-worker-token), then start the worker with that token:

```bash
agent worker start --auth-token "your-user-scoped-token"
```

For long-lived workers, read the token from a file:

```bash
agent worker start --auth-token-file /var/run/cursor/token
```

This is useful in Kubernetes because environment variables from Secrets are fixed when the pod starts. Secret volumes update while the pod runs, while mounted token paths can be live updated within the pod giving you the chance to refresh the token while the pod is running.

## Trigger this machine from a chat surface

Use `worker=` or `machine=` when you want Slack, GitHub, or Linear requests to run on one of your named machines. These are the only trigger options that target My Machines.

Start the machine with [`--name`](https://cursor.com/docs/cloud-agent/my-machines.md#name-the-machine), then include that name in the request:

- In Slack, use `@Cursor worker=my-devbox fix the flaky test` or `@Cursor machine=my-devbox fix the flaky test`.
- In GitHub, comment `@cursoragent worker=my-devbox fix the flaky test` or `@cursoragent machine=my-devbox fix the flaky test`. You must be a trusted repo commenter, and the target machine must belong to the Cursor user linked to your GitHub account.
- In Linear, add `worker=my-devbox` or `machine=my-devbox` to the issue body. You can also use a parent label named `worker` or `machine` with a child label named `my-devbox`.

### How Cursor picks your machine

A `worker=<name>` request runs on a machine only when all three are true:

1. The machine belongs to the Cursor user who triggered the request.
2. The machine's `--name` matches the requested `<name>`.
3. The machine's registered repo matches the trigger's target repo.

The trigger's target repo comes from the surface, not from the machine name:

- **Slack** uses `repo=` in your message if present, then the channel default repo, your user default repo, then the team default repo.
- **Linear** uses the repo resolved from the issue or project (for example `[repo=]`, issue labels, project labels, or the dashboard default). See [Repository selection](https://cursor.com/docs/integrations/linear.md#repository-selection).
- **GitHub** uses the repo of the issue, pull request, or review comment where `@cursoragent` was mentioned.

Each machine's registered repo comes from the git remote in the directory where you started the worker. To serve more than one repo, start a worker in each repo's checkout.

### When a `worker=` request can't run

If you have a machine with that name but it's registered for a different repo, Cursor rejects the request rather than running it on the wrong checkout:

> `worker=<name>` is registered on your machine but for a different repository. Start the worker in a checkout of the target repo first.

The error appears as an ephemeral reply in Slack, an agent activity error in Linear, and a `@cursoragent` reply on GitHub for trusted commenters. The behavior is intentional: a request for repo A should never run on a machine checkout for repo B.

If no machine matches the linked user and target repo, the request fails instead of falling back to another environment. Confirm the machine name, your Cursor account linking, and the worker directory's git remote.

`self_hosted`, `pool=`, and `repo=` on their own don't target My Machines. Use them with [Self-Hosted Pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#triggering-pool-agents) workers. When you pair `repo=` with `worker=`, it sets which repo Cursor matches against your machines.

## Artifacts

Artifact behavior is identical on self-hosted workers and Cursor-hosted agents. The agent produces the artifact inside the worker and the worker uploads it to Cursor-managed storage over HTTPS. Everything downstream (PR embeds, dashboard previews, notification attachments) is handled by Cursor's backend and doesn't depend on where the worker runs.

Artifacts are on by default. See [Capabilities](https://cursor.com/docs/cloud-agent/capabilities.md#demos-and-artifacts) for what they look like in the UI.

To disable artifact uploads, block outbound traffic to `cloud-agent-artifacts.s3.us-east-1.amazonaws.com`. The agent session keeps working; artifacts produced during the session fail to upload.

## Networking

Workers need outbound HTTPS access to:

- `api2.cursor.sh` and `api2direct.cursor.sh` for the agent session
- `cloud-agent-artifacts.s3.us-east-1.amazonaws.com` for [artifact](https://cursor.com/docs/cloud-agent/my-machines.md#artifacts) uploads

If your firewall can only match wildcards, `*.s3.us-east-1.amazonaws.com` covers the artifact host, but also opens every other bucket in the region. Prefer an exact-host rule when the firewall supports it.

No inbound ports, public IPs, or VPN tunnels are required. If you use a proxy, set `HTTPS_PROXY` or `https_proxy` in the worker environment.

### Failure modes

| If you block...                                       | Effect                                                                                                                                                                        |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api2.cursor.sh` or `api2direct.cursor.sh`            | The worker can't start or continue an agent session.                                                                                                                          |
| `cloud-agent-artifacts.s3.us-east-1.amazonaws.com`    | Artifact uploads fail. PR embeds, dashboard previews, and notification attachments that depend on artifacts are missing. The agent session and other tool calls keep working. |
| An outbound host a specific tool or integration needs | Only that tool or integration fails. The agent continues.                                                                                                                     |

## MCP servers

MCP servers are routed by transport type:

| Transport        | Runs on        | Use case                                                                                                  |
| ---------------- | -------------- | --------------------------------------------------------------------------------------------------------- |
| Command (stdio)  | Your machine   | The MCP process starts on your machine and can reach private networks, internal APIs, and local services. |
| HTTP / SSE (url) | Cursor backend | Cursor handles OAuth, session caching, and auth for HTTP-based MCP servers.                               |

If your MCP server needs to reach endpoints on your private network, use the command (stdio) transport. The process runs directly on your machine and shares its network. For HTTP-based MCP servers, Cursor manages the connection from its backend.

## Troubleshooting

Run a preflight debug report:

```bash
agent worker start --debug
```

This checks authentication, privacy routing, repo labels, and whether Cursor can see matching workers.

## Related

- [Self-Hosted Pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md)
- [Cloud Agent security and network](https://cursor.com/docs/cloud-agent/security-network.md)
- [Service accounts](https://cursor.com/docs/account/enterprise/service-accounts.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
