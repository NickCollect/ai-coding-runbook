---
source_url: https://cursor.com/docs/cloud-agent/self-hosted/my-machines
fetched_at: 2026-09-07T05:31:27.612393+00:00
fetch_method: mintlify_md
---

# My Machines

My Machines is the personal [Self-Hosted Machines](https://cursor.com/docs/cloud-agent/self-hosted.md) configuration. It lets a specific user run Cloud Agent tool calls on a machine they already use: a laptop, devbox, or remote VM. Use it when that machine is the desired execution environment for a repo.

A worker on your machine opens an outbound connection to Cursor. The agent loop runs in Cursor's cloud, but terminal commands, file edits, browser actions, and other tool calls execute on your machine. No inbound ports or firewall changes are required.

Cursor-managed Cloud Agents are the recommended path for most teams, including
teams that need access to private networks. You can use network allowlists,
Tailscale or similar clients, and private connectivity for supported source
control paths without operating your own worker. See [Choose where Cloud
Agents run](https://cursor.com/docs/cloud-agent/self-hosted/choose-runtime.md).

Use My Machines when you want to:

- Use a devbox or remote workstation that already has your repo and tools
- Execute tool calls on one user's machine for a specific repo
- Reuse machine-local state that you do not want to recreate in a cloud environment
- Try the worker model before building a centrally managed pool

For org-wide worker fleets, see [Team Pools](https://cursor.com/docs/cloud-agent/self-hosted/pool.md).

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

![Cursor's Run on menu with my-devbox highlighted under My Machines](/docs-static/images/cloud-agent/my-machines-picker.png)

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

Register multiple repository roots by repeating `--worker-dir`:

```bash
agent worker \
  --worker-dir "$HOME/repos/app" \
  --worker-dir "$HOME/repos/infra" \
  start
```

Each path must exist. For each root with a Git remote, the worker registers routing metadata so Cursor can match requests to the correct checkout.

### Use an API key

For devboxes or automation where browser login isn't practical, use a personal user API key from [Cursor Dashboard → API Keys](https://cursor.com/dashboard/api):

```bash
agent worker start --api-key "your-user-api-key"
```

My Machines workers require a personal credential: browser login, a personal
user API key, or a user-scoped token. [Service account API
keys](https://cursor.com/docs/account/enterprise/service-accounts.md) only start pool workers
(`--pool`), and team Admin API keys and organization API keys can't start
workers at all. See [Self-Hosted
Pool](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#authenticate-workers) for
team-shared workers.

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

### Enable computer use

Let the agent click, type, take screenshots, and drive apps on this machine by passing `--computer-use` before `start`:

```bash
agent worker --computer-use --name "my-mac" start
```

On macOS, the first start installs the **Cursor Computer Use** helper app. Grant it **Accessibility** and **Screen Recording** in System Settings → Privacy & Security, then test with a task that takes a screenshot. On Linux, install the desktop packages first. See [Computer use and desktop sharing](https://cursor.com/docs/cloud-agent/self-hosted/computer-use.md) for the macOS permission steps, MDM guidance, and the Linux display options.

## Trigger this machine from a chat surface

Use `worker=` or `machine=` when you want Slack, GitHub, or Linear requests to run on one of your named machines. These are the only trigger options that target My Machines.

Start the machine with [`--name`](https://cursor.com/docs/cloud-agent/self-hosted/my-machines.md#name-the-machine), then include that name in the request:

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

Each machine's registered repos come from the git remotes of its worker directories. To serve more than one repo from one machine, pass [`--worker-dir`](https://cursor.com/docs/cloud-agent/self-hosted/my-machines.md#run-from-a-different-repo-directory) once per checkout, or start a worker in each repo's checkout.

### When a `worker=` request can't run

If you have a machine with that name but it's registered for a different repo, Cursor rejects the request rather than running it on the wrong checkout:

> `worker=<name>` is registered on your machine but for a different repository. Start the worker in a checkout of the target repo first.

The error appears as an ephemeral reply in Slack, an agent activity error in Linear, and a `@cursoragent` reply on GitHub for trusted commenters. The behavior is intentional: a request for repo A should never run on a machine checkout for repo B.

If no machine matches the linked user and target repo, the request fails instead of falling back to another environment. Confirm the machine name, your Cursor account linking, and the worker directory's git remote.

`self_hosted`, `pool=`, and `repo=` on their own don't target My Machines. Use them with [Team Pool](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#triggering-pool-agents) workers. When you pair `repo=` with `worker=`, it sets which repo Cursor matches against your machines.

## Hooks

A My Machines worker runs the same hooks as other Self-Hosted Machines workers: command-based hooks from `.cursor/hooks.json` in the workspace you start the worker from. On Enterprise, it also runs team hooks and enterprise-managed hooks.

[Hooks on Pools](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#hooks) covers what applies on workers, including `sessionStart` and `sessionEnd` when a session claims and releases the machine. The [Hooks reference](https://cursor.com/docs/hooks.md) covers the schema, events, and examples.

## Artifacts

Artifact behavior is identical on self-hosted workers and Cursor-hosted agents. The agent produces the artifact inside the worker and the worker uploads it to Cursor-managed storage over HTTPS. Everything downstream (PR embeds, dashboard previews, notification attachments) is handled by Cursor's backend and doesn't depend on where the worker runs.

Artifacts are on by default. See [Capabilities](https://cursor.com/docs/cloud-agent/capabilities.md#demos-and-artifacts) for what they look like in the UI.

To disable artifact uploads, block outbound traffic to `cloud-agent-artifacts.s3.us-east-1.amazonaws.com`. The agent session keeps working; artifacts produced during the session fail to upload.

## Networking

Workers need outbound HTTPS access to:

- `api2.cursor.sh` and `api2direct.cursor.sh` for the agent session
- `downloads.cursor.com` for CLI updates and the first-time [Cursor Computer Use](https://cursor.com/docs/cloud-agent/self-hosted/computer-use.md#macos) install on macOS
- `cloud-agent-artifacts.s3.us-east-1.amazonaws.com` for [artifact](https://cursor.com/docs/cloud-agent/self-hosted/my-machines.md#artifacts) uploads

If your firewall can only match wildcards, `*.s3.us-east-1.amazonaws.com` covers the artifact host, but also opens every other bucket in the region. Prefer an exact-host rule when the firewall supports it.

No inbound ports, public IPs, or VPN tunnels are required. If you use a proxy, set `HTTPS_PROXY` or `https_proxy` in the worker environment.

### Failure modes

| If you block...                                       | Effect                                                                                                                                                                        |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api2.cursor.sh` or `api2direct.cursor.sh`            | The worker can't start or continue an agent session.                                                                                                                          |
| `downloads.cursor.com`                                | CLI updates and the first-time Cursor Computer Use install on macOS fail. A worker that already has both installed keeps running.                                             |
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
agent worker debug
```

This checks authentication, privacy routing, repo labels, and whether Cursor can see matching workers. To print the same diagnostics before starting the worker, use `agent worker start --debug`.

If the machine does not appear in the picker:

- Confirm the worker process is still running.
- Confirm the Cursor app and CLI use the same account.
- Check that the worker directory has the expected Git remote.
- Check outbound access to the hosts listed in [Networking](https://cursor.com/docs/cloud-agent/self-hosted/my-machines.md#networking).

If computer use fails on a Mac, the report confirms whether **Cursor Computer Use** is installed but not whether its permissions are granted. Grant **Accessibility** and **Screen Recording** to Cursor Computer Use in System Settings → Privacy & Security, then retry a screenshot task. See [macOS](https://cursor.com/docs/cloud-agent/self-hosted/computer-use.md#macos).

## Next steps

- [Computer use](https://cursor.com/docs/cloud-agent/self-hosted/computer-use.md): let agents drive a desktop and browser on your machine, and watch or control the agent desktop from Cursor.
- [API reference](https://cursor.com/docs/cloud-agent/api/endpoints.md#workers-and-pools): endpoints for workers, pools, the pending-request queue, and worker tokens.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
