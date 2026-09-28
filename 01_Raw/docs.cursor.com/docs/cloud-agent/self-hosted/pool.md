---
source_url: https://cursor.com/docs/cloud-agent/self-hosted/pool
fetched_at: 2026-09-28T06:10:42.283674+00:00
fetch_method: mintlify_md
---

# Team Pools

A pool is a named routing target that connects requests with [Self-Hosted Machines](https://cursor.com/docs/cloud-agent/self-hosted.md) workers. Requests wait in the pool until an available worker claims them. Create separate pools for different execution environments, such as one for work that needs GPUs and another for work that needs a Mac.

Team Pools are for Enterprise teams that want Cloud Agents to run inside company-managed infrastructure. Instead of each developer starting a worker on a personal machine, admins operate a pool of workers that can be assigned to agents across the organization.

Pools are an infrastructure-ownership choice. They do not move the agent loop out of Cursor's cloud. The worker executes terminal commands, file edits, browser actions, and other tool calls in your infrastructure while Cursor handles orchestration, model access, and the Cloud Agent experience.

Cursor-managed Cloud Agents are the recommended path for most teams, including
teams that need private network access. Use managed environments with network
controls, Tailscale or a similar client, or private connectivity for supported
source control paths before taking on a worker fleet. See [Choose where Cloud
Agents run](https://cursor.com/docs/cloud-agent/self-hosted/choose-runtime.md).

Use a pool when you need:

- Centrally managed workers for a team or organization
- Service account authentication instead of individual browser logins
- Kubernetes, autoscaling, or centrally managed capacity
- Labels that route work to the right environment, team, repo, or hardware profile
- Company-owned hosts for tool execution, build outputs, worker logs, and monitoring

For a fast personal setup, see [My Machines](https://cursor.com/docs/cloud-agent/self-hosted/my-machines.md). See [Requirements](https://cursor.com/docs/cloud-agent/self-hosted.md#requirements) on the Self-Hosted Machines overview for the plan, credential, dashboard settings, and machine dependencies pools need.

## How it works

A worker opens a long-lived outbound HTTPS connection to Cursor's cloud. The agent loop, including inference and planning, runs in Cursor's cloud and sends tool calls over this connection. The worker executes those tool calls in your infrastructure: terminal commands, file edits, browser actions, and access to internal services.

Your repos, build caches, secrets, and tool execution stay in your environment while Cursor handles orchestration, model access, and the Cloud Agent experience. Cloud Agent [artifacts](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#artifacts), like screenshots and videos, are uploaded to Cursor so you can view them in PRs and the dashboard.

Workers only need outbound access. No inbound ports, public IPs, or VPN tunnels are required. See [Networking](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#networking) for the full list of required hosts.

Self-Hosted Machines support up to 200 workers per user and 1000 per team. For larger company-wide deployments, [contact us](https://cursor.com/contact-sales?source=self-hosted-agents) to discuss scaling.

## Prerequisites

- A **Cursor Enterprise plan**
- Self-hosted settings configured by a team admin in the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#self-hosted-agents):
  - **Allow Self-Hosted Machines** lets users opt in to self-hosted runs.
  - **Require Self-Hosted Machines** routes every Cloud Agent run to self-hosted workers.
- A [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md) for pool worker authentication
- A worker machine or image with:
  - `agent` CLI installed
  - `git` installed and available on `PATH` (required when the worker serves git remotes or uses [`--clone-git-repos`](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#any-repo-pools); optional for [any-repo pools](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#any-repo-pools) if your own scripts handle SCM)
  - A workspace directory (a cloned repository with a configured remote, or an [any-repo](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#any-repo-pools) directory)
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

Pool workers authenticate with a [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md), or with a [session token](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#session-tokens) minted from that key for a single claim.

User, personal, team, and organization API keys can't start pool workers. Use personal or user API keys with personal workers on [My Machines](https://cursor.com/docs/cloud-agent/self-hosted/my-machines.md).

```bash
export CURSOR_API_KEY="your-service-account-api-key"
```

You can also pass the key directly:

```bash
agent worker --api-key "your-service-account-api-key" start
```

## Start a pool worker

Run the worker from the workspace it should serve (a git repo root, or an [any-repo](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#any-repo-pools) directory):

```bash
cd /path/to/repo
agent worker --pool start
```

`--pool` registers the worker for pool assignment. Pass an optional name to join a named pool (for example, `--pool my-pool`). When the name is omitted, the worker joins `default`. Each Cloud Agent session claims one worker at a time.

For orchestrated environments, combine it with `--idle-release-timeout` so the process exits cleanly after work completes:

```bash
agent worker --pool my-pool --idle-release-timeout 600 start
```

`--idle-release-timeout` keeps the worker alive for a window (in seconds) after a session ends to handle follow-up messages. The default is `3600` seconds. See [Session lifecycle](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#session-lifecycle) for how release and reconnection work.

### Enable computer use

Pass `--computer-use` so claimed agents can click, type, take screenshots, and drive apps on the worker:

```bash
agent worker --pool my-pool --computer-use start
```

On macOS, the first start installs the **Cursor Computer Use** helper app. Grant it **Accessibility** and **Screen Recording**, verify with a task that takes a screenshot, then snapshot the machine so every worker restored from the image is ready. On Linux, bake the desktop packages into the worker image. See [Computer use and desktop sharing](https://cursor.com/docs/cloud-agent/self-hosted/computer-use.md) for the macOS permission steps, MDM profile guidance, and the Linux display options.

## Register multiple repo roots

Self-hosted multi-repo support is configured at worker startup by registering multiple workspace roots. Pass `--worker-dir` once for each local repo root. The first root is the primary repository for assignment identity and dashboard display. All roots are exposed to the agent runtime, and roots with valid git origins register repository routing metadata.

`--worker-dir` is repeatable up to 20 paths. Each path must already exist and be a directory. If you don't pass `--worker-dir`, the CLI uses the current working directory.

Before you start, enable self-hosted workers in **Dashboard** > **Cloud Agents** > **Self-Hosted**. Use writable paths under `$HOME` unless your own machine image guarantees another writable location.

Example setup:

```bash
export WORKER_ROOT="$HOME/cursor-repos/my-org"
mkdir -p "$WORKER_ROOT"

git clone git@github.com:my-org/app.git "$WORKER_ROOT/app"
git clone git@github.com:my-org/infra.git "$WORKER_ROOT/infra"

export CURSOR_API_KEY="<key>"
```

Run a preflight check before starting the worker:

```bash
agent worker \
  --pool my-pool \
  --name app-infra-worker \
  --worker-dir "$WORKER_ROOT/app" \
  --worker-dir "$WORKER_ROOT/infra" \
  debug --json
```

Start the worker with the same roots:

```bash
agent worker \
  --pool my-pool \
  --name app-infra-worker \
  --worker-dir "$WORKER_ROOT/app" \
  --worker-dir "$WORKER_ROOT/infra" \
  start --verbose
```

Place worker options before `start` or `debug`. Leave the process running under a supervisor like `systemd`, `tmux`, `launchd`, Kubernetes, or your own process manager.

Verbose startup logs are the source of truth for registered roots. A successful multi-repo worker shows each derived repo label, the workspace paths, and the repository URLs:

```text
repo=my-org/app
repo=my-org/infra
workspacePaths: [app, infra]
x-repository-urls: ["git@github.com:my-org/app.git","git@github.com:my-org/infra.git"]
```

The dashboard currently displays a self-hosted worker under its primary repo.
There is no named self-hosted multi-repo environment object in the portal yet.
This can look like only the first repo is registered. Check `workspacePaths`
and `x-repository-urls` in verbose logs to confirm all roots. To make another
repo primary, put its `--worker-dir` first.

Use `--name` and `--pool <name>` to make multi-repo workers recognizable in the dashboard and triggers.

In pool mode, one Cloud Agent claims the worker at a time. Without `--pool`, shared assignment is allowed. Add `--management-addr 0.0.0.0:8080` before `start` when you need `/healthz`, `/readyz`, and `/metrics` for an orchestrator.

Non-git directories can be execution roots, but they don't contribute repo routing metadata. For a multi-repo worker, clone each repository before the worker starts. To start from an empty workspace and let the worker bootstrap source control after assignment, use an [any-repo pool](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#any-repo-pools).

## Any-repo pools

Pools come in two repo configurations. A repo-backed pool ties the pool to one or more repositories: requests carry a `repo=<owner/repo>` label, match workers serving that repo, and appear under the repository in the dashboard. An any-repo pool leaves source control to you: requests match on the pool name alone, and the pool appears under **Any repo** in the dashboard.

If you prefer to manage source control yourself, create a pool without a repo attached. A pool worker does not require a git remote. Point `--worker-dir` at any existing directory when you want the agent (or your own image, hooks, and scripts) to manage cloning and git state:

```bash
mkdir -p "$HOME/cursor-sandboxes/default"
agent worker --pool my-pool --worker-dir "$HOME/cursor-sandboxes/default" start
```

To give every any-repo request repository instructions, create an `.mdc` file under `.cursor/rules` inside the directory passed to `--worker-dir`. The filename is arbitrary. This example uses `repo-info.mdc`:

```md title=".cursor/rules/repo-info.mdc"
---
alwaysApply: true
---

This any-repo worker can clone from `github.acme.internal` with the
pre-authenticated `gh` CLI.

- For requests about payments, billing, or checkout, use
  `platform/payments-service`. If it is missing, run:
  `GH_HOST=github.acme.internal gh repo clone platform/payments-service`
- For requests about the member portal or account settings, use
  `web/member-portal`. If it is missing, run:
  `GH_HOST=github.acme.internal gh repo clone web/member-portal`
- Clone only the repositories needed for the request. Run subsequent commands
  from the cloned repository.
- If no mapping matches the request, report that the repository is not
  configured. Do not guess a repository name, clone URL, or credentials.
```

[`alwaysApply: true`](https://cursor.com/docs/rules.md#rule-anatomy) includes the rule in every request. Keep the file in the worker directory so it is available before cloning, and replace the example mappings with your repositories and SCM commands.

To have the worker check out the claimed agent's repos on claim, pass `--clone-git-repos`. This is opt-in. Default any-repo behavior does not clone.

```bash
agent worker --pool my-pool --clone-git-repos start
```

`--clone-git-repos` implies `--mint-github-token`. Clones and fetches use that minted short-lived GitHub token. A team admin must enable GitHub token minting for Team Pool workers, and `git` must be on `PATH`.

Use this flag only on any-repo pool workers: a named `--pool` other than `default`, with no bound repository (`repo=`) and no bound machine (`name=`). The CLI exits with a clear error on a bound-repo worker, a named machine, the `default` pool, or a personal [My Machines](https://cursor.com/docs/cloud-agent/self-hosted/my-machines.md) worker.

Branch names clone with `--branch`. A full 40-character commit SHA uses a detached checkout after clone. Use HTTPS GitHub remotes so the minted token can authenticate.

If the worker directory, or a folder directly inside it, already has a clean checkout of a claimed repo, the worker reuses it instead of cloning again. The checkout's `origin` remote must point to the same host and `owner/repo`. The worker fetches the requested branch, tag, or commit and checks it out, and only fast-forwards a local branch. It clones into a new folder beside the checkout instead when it can't update the checkout safely, for example when the checkout has:

- Uncommitted changes to tracked files
- Local commits on the requested branch that the remote doesn't have
- A merge, rebase, cherry-pick, revert, or bisect in progress
- Submodules set up
- Git config or hooks that a fresh clone wouldn't have

Reuse needs git 2.26 or later; with older git, the worker clones. The worker log says why it did or didn't reuse each checkout.

When a claim ends, the worker deletes the repos it cloned for that claim and keeps reused checkouts. To avoid cloning a large repo on every claim, clone it into the worker directory before you start the worker.

If clone fails, the request stays in the queue. Operators see a generic clone failure.

`--clone-git-repos`, `--mint-github-token`, and `--sync-dashboard-secrets` assume one worker per container or OS user. Co-locating multiple credential-enabled workers under the same user is unsupported.

Any-repo pools omit `repo=` routing labels. Start agents against them with `env.type: "pool"` and `env.name` set to the pool name, and omit `repos` (see [Create An Agent](https://cursor.com/docs/cloud-agent/api/endpoints.md#create-an-agent)). Pick the pool under **Any repo** on [cursor.com/agents](https://cursor.com/agents). In Slack, an any-repo pool set as the [team default pool](https://cursor.com/docs/integrations/slack.md#team-default-pool) or a [channel default pool](https://cursor.com/docs/integrations/slack.md#channel-default-pool) lets `@Cursor` start an agent even when no repository resolves from the message or defaults.

## Manage pools

Pools are durable. A pool stays registered and selectable after the last worker disconnects, so you can scale to zero and bring capacity back when requests arrive. Starting a worker with a new pool name creates the pool implicitly. Manage pools ahead of time with the [Cloud Agents API](https://cursor.com/docs/cloud-agent/api/endpoints.md#workers-and-pools):

- [`POST /v0/private-workers/pools`](https://cursor.com/docs/cloud-agent/api/endpoints.md#register-a-pool) registers a pool up front, before any worker connects. Include `repoOwner`, `repoName`, and `repoUrl` for a repo-backed pool, or omit them for an any-repo pool.
- [`GET /v0/private-workers/pools`](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pools) lists pools with connected and in-use worker counts.
- [`DELETE /v0/private-workers/pools`](https://cursor.com/docs/cloud-agent/api/endpoints.md#deregister-a-pool) soft-deletes a pool. It does **not** affect machines currently connected to the pool.

Use [List Pools](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pools) and [pending requests](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pending-pool-requests) to decide when to scale workers back up.

## Pool names

Group pool workers under a name when you want sessions to route to a specific subset, like GPU machines, a staging fleet, or a team's dedicated build boxes.

Pass the name to `--pool`:

```bash
agent worker --pool my-pool start
```

When the name is omitted, the worker joins the `default` pool. Older CLI versions that only supported a boolean `--pool` plus separate `--pool-name` continue to work; `--pool-name` is a deprecated alias for `--pool <name>`.

Set the pool name from the environment when an orchestrator injects config:

```bash
export CURSOR_WORKER_POOL_NAME=my-pool
agent worker --pool start
```

Multi-use workers (started without `--pool`) don't belong to a pool.

From the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents), pick a pool in the worker selector when starting a session or editing an automation. You can also include `pool=<name>` in a Slack, GitHub, or Linear trigger. Sessions route only to workers registered with that pool name.

## Triggering pool agents

Use pool triggers when you want a Cloud Agent to run on your team's shared worker fleet. Pool workers are the right target for centrally managed capacity, autoscaling, CI-like runners, and repo-scoped infrastructure.

Team admins control self-hosted routing from the Self-Hosted section of the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents). **Allow Self-Hosted Machines** lets users opt in per request. Without opt-in, runs use Cursor's managed infrastructure. **Require Self-Hosted Machines** routes Cloud Agent runs to self-hosted workers.

When Cursor starts a pool agent, it matches workers with labels. Pool requests for a repository include a `repo=<owner/repo>` label; requests to an [any-repo pool](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#any-repo-pools) without a repository omit it. Requests for a named pool also include `pool=<name>`.

Pool workers handle:

- Runs covered by **Require Self-Hosted Machines**, unless the request targets a specific My Machines worker with `worker=` or `machine=`
- Requests with `self_hosted=true` or its short form, `sh=1`
- Requests with `pool=<name>`, which also selects that named pool
- Self-hosted requests with repository selection from the trigger surface, such as `repo=<owner/repo>` where supported

`repo=` selects the repository for the run. For Team Pool runs, that repository becomes the `repo=<owner/repo>` worker label. It does not target a personal machine.

Use these options from integrations to start pool agents:

- **Slack**: Mention `@Cursor` with `self_hosted=true`, `sh=1`, or `pool=<name>`. Team admins can set a [team default pool](https://cursor.com/docs/integrations/slack.md#team-default-pool) with `@Cursor pool set <name>` so members run on it without an option in each mention. A [channel default pool](https://cursor.com/docs/integrations/slack.md#channel-default-pool), set with `@Cursor pool set <name> channel`, replaces the team default in that channel. Explicit `pool=`, `worker=`, `machine=`, or `self_hosted=false` override both defaults, and an any-repo default pool lets Slack launch without a resolved repository.
- **GitHub**: Comment `@cursoragent self_hosted=true ...`, `@cursoragent sh=1 ...`, or `@cursoragent pool=<name> ...` on an issue, pull request, or review comment.
- **Linear**: Mention `@Cursor` in a comment with `self_hosted=true`, `sh=1`, `pool=<name>`, or `[pool=<name>]`. Cursor reads these options from that comment, not from the issue description. You can also use issue or project labels where the parent label is `pool` and the child label is the pool name. Labels are the only way to pick a pool when you [delegate an issue](https://cursor.com/docs/integrations/linear.md#delegating-issues) to Cursor, because there's no comment to read. A `pool=` in the comment wins over a pool label, and `self_hosted=false` skips pool labels.

Write each option as `key=value`. `self_hosted` and its short form `sh` accept `true`, `t`, or `1` to opt in and `false`, `f`, or `0` to opt out. Anything else stays in your prompt as text. That includes `self_hosted`, `selfhosted`, or `sh` with no value, and other values like `sh=/bin/bash`. Slack, GitHub, and Linear all ignore these options inside a code block, so pasted code doesn't change where the agent runs.

Policy handling depends on where the request starts:

- **Slack** rejects self-hosted opt-in when Allow Self-Hosted Machines is off and replies in Slack. If Require Self-Hosted Machines is on, every Slack mention runs self-hosted.
- **GitHub** lets repo `OWNER` and `COLLABORATOR` users route runs to self-hosted workers. Other commenters run on managed infrastructure when they opt in, or are skipped if Require Self-Hosted Machines is on. This protects public repos where outside contributors can leave comments.
- **Linear** rejects explicit self-hosted requests when Allow Self-Hosted Machines is off. The issue gets an agent activity error that asks an admin to turn on self-hosted workers or remove the hint to run on Cursor's managed infrastructure.

To target one of your own machines by name, use [My Machines](https://cursor.com/docs/cloud-agent/self-hosted/my-machines.md#trigger-this-machine-from-a-chat-surface) with `worker=` or `machine=`.

The Cloud Agent API uses the same resolver with `usePrivateWorker` and `labels` fields. See the [Cloud Agent API docs](https://cursor.com/docs/cloud-agent/api/endpoints.md) for endpoint details.

## Hooks

Self-Hosted Machines workers run command-based [hooks](https://cursor.com/docs/hooks.md) during Cloud Agent sessions. They load configuration from the workspace the worker serves.

- **Project hooks.** Commit `.cursor/hooks.json` and the scripts it references in the repository or workspace directory the worker uses. That is the git checkout, a `--worker-dir` root, or the directory you pass for an [any-repo pool](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#any-repo-pools).
- **Team and enterprise-managed hooks.** On Enterprise, workers also run hooks configured in the [web dashboard](https://cursor.com/dashboard/team-content?section=hooks).

The [Hooks](https://cursor.com/docs/hooks.md) reference covers the schema, events, and examples. [Cloud agent support](https://cursor.com/docs/hooks.md#cloud-agent-support) lists which events the Cloud Agent loop runs.

The Cloud Agent limits that also apply on these tool-execution workers:

- **Command-based hooks only.** Prompt-based hooks do not run.
- **No IDE-only hooks.** Tab hooks (`beforeTabFileRead`, `afterTabFileEdit`) and `workspaceOpen` do not run on workers.

`sessionStart` and `sessionEnd` run on Self-Hosted Machines workers. They fire when a Cloud Agent session claims the worker and when that claim is released. Cursor-managed Cloud Agents skip those hooks.

Workers on [Kubernetes](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#deploy-on-kubernetes) and other orchestrated platforms use this same hooks model.

## Labels

Labels are key-value pairs that describe a worker. They control how Cloud Agent sessions route to the right pool.

### CLI flags

Good for quick testing or small pools:

```bash
agent worker \
  --pool \
  --label team=backend \
  --label env=production \
  start
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
agent worker --pool --labels-file labels.json start
```

### TOML file

Same as JSON, different format:

```toml
team = "backend"
env = "production"
capabilities = ["docker", "gpu"]
```

```bash
agent worker --pool --labels-file labels.toml start
```

### Environment variable

Useful when the path is injected by your orchestrator:

```bash
export CURSOR_WORKER_LABELS_FILE=/path/to/labels.json
agent worker --pool start
```

The `repo` and `pool` labels are reserved. `repo` comes from the worker directory's git remote when present. `pool` is set by [`--pool`](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#pool-names). Don't set either manually.

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
- `downloads.cursor.com` for CLI updates and the first-time [Cursor Computer Use](https://cursor.com/docs/cloud-agent/self-hosted/computer-use.md#macos) install on macOS
- `cloud-agent-artifacts.s3.us-east-1.amazonaws.com` for [artifact](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#artifacts) uploads

If your firewall can only match wildcards, `*.s3.us-east-1.amazonaws.com` covers the artifact host, but also opens every other bucket in the region. Prefer an exact-host rule when the firewall supports it.

No inbound ports, public IPs, or VPN tunnels are required. If you use a proxy, set `HTTPS_PROXY` or `https_proxy` in the worker environment.

### Failure modes

| If you block...                                       | Effect                                                                                                                                                                        |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api2.cursor.sh` or `api2direct.cursor.sh`            | The worker can't start or continue an agent session.                                                                                                                          |
| `downloads.cursor.com`                                | CLI updates and the first-time Cursor Computer Use install on macOS fail. A worker that already has both installed keeps running.                                             |
| `cloud-agent-artifacts.s3.us-east-1.amazonaws.com`    | Artifact uploads fail. PR embeds, dashboard previews, and notification attachments that depend on artifacts are missing. The agent session and other tool calls keep working. |
| An outbound host a specific tool or integration needs | Only that tool or integration fails. The agent continues.                                                                                                                     |

The [Prerequisites](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#prerequisites) section covers the broader set of hosts a worker needs during agent runs (git hosts, package registries, internal APIs).

## Deploy on Kubernetes

Run pool workers on Kubernetes when you want the platform to handle scheduling, health checks, and Pod lifecycle. Start from [anysphere/k8s-workers](https://github.com/anysphere/k8s-workers): a Helm sample that runs the [worker controller](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#worker-controller) in your cluster with `--spawn`. The spawn hook creates one worker Pod per claimed request, or the controller keeps warm idle Pods with `--warm-idle`. No CRD is required.

The Cursor Kubernetes operator and `WorkerDeployment` Helm chart are
deprecated. If your cluster already runs the operator, it keeps working, and
the [operator reference](https://cursor.com/docs/cloud-agent/self-hosted/kubernetes.md) stays
available. New Kubernetes deployments should use the k8s-workers template.

Other hosts work the same way: any VM, container, or bare-metal machine that can install the Cursor CLI and reach Cursor over outbound HTTPS can run a pool worker under `systemd`, Docker, or your own process manager. For partner guides and reference templates covering AWS Lambda, Cloudflare, Namespace, Modal, Daytona, E2B, Vercel, Tensorlake, Coder, and SuperServe, see [Integrations](https://cursor.com/docs/cloud-agent/self-hosted/integrations.md).

## Worker controller

`agent worker controller` starts workers from a `--spawn` hook. The hook can fork a process, start a container, or create a Kubernetes Pod, as the [k8s-workers template](https://github.com/anysphere/k8s-workers) does. `--warm-idle` is the warm-capacity path: the controller runs the hook once per missing idle worker instead of patching a Deployment or HPA. `WorkerDeployment.spec.readyReplicas` belongs to the deprecated [Kubernetes operator](https://cursor.com/docs/cloud-agent/self-hosted/kubernetes.md#scaling); only clusters that already run it need that control.

`--spawn <path>` is required. The hook runs once after a successful claim, or once per missing warm worker. Hook environment includes `CURSOR_API_KEY` (`CURSOR_AUTH_TOKEN` instead with [`--session-token`](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#session-tokens)), `CURSOR_API_URL`, `CURSOR_API_ENDPOINT`, `CURSOR_AGENT_WORKER_ID`, and request fields. Authenticate with a [service account](https://cursor.com/docs/account/enterprise/service-accounts.md) key via `--api-key` or `CURSOR_API_KEY`. The key binds the team. Session login is not used.

| Flag                  | Description                                                                                                                                                                                                |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--spawn <path>`      | Script to run once after a successful claim, or once per missing warm worker. Required.                                                                                                                    |
| `--api-key <key>`     | Service account API key. Also readable from `CURSOR_API_KEY`. Session login is not used.                                                                                                                   |
| `--pool <name>`       | Pool to watch (repeatable). Mutually exclusive with `--all-pools`. Warm mode requires `--pool`.                                                                                                            |
| `--all-pools`         | Team-wide pending-requests list and stream. Does not register pools. Not allowed in warm mode.                                                                                                             |
| `--warm-idle <count>` | Keep `count` idle workers per `--pool` and skip claiming.                                                                                                                                                  |
| `--session-token`     | Claim mode only. Give the spawn hook a [session token](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#session-tokens) for its claim instead of the API key. Can't be combined with `--warm-idle`. |
| `--repository <url>`  | Filter pending requests by repository. Required for repo-scoped keys. In warm mode, also pins the pool idle-count to that repo's row.                                                                      |
| `--endpoint <url>`    | Public API base (default `https://api.cursor.com`). Also readable from `CURSOR_API_ENDPOINT`.                                                                                                              |

The spawn hook receives everything it needs as environment variables:

| Variable                                                   | Set in                            | Description                                                                                                                                      |
| ---------------------------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `CURSOR_REQUEST_ID`                                        | Claim mode                        | Agent id of the claimed request.                                                                                                                 |
| `CURSOR_USER_ID`                                           | Claim mode                        | Cursor user id that created the request.                                                                                                         |
| `CURSOR_REPO_URL`, `CURSOR_REPO_OWNER`, `CURSOR_REPO_NAME` | Claim mode                        | Repository metadata when the request targets a repo. Unset for any-repo requests.                                                                |
| `CURSOR_REPO_URLS`                                         | Claim mode                        | JSON array of repository URLs for multi-repo requests.                                                                                           |
| `CURSOR_POOL`                                              | Both                              | Pool the worker should join.                                                                                                                     |
| `CURSOR_AGENT_WORKER_ID`                                   | Both                              | Worker id the machine must start with. The worker CLI reads this automatically.                                                                  |
| `CURSOR_WORKER_NAME`                                       | Both                              | Display name for the worker.                                                                                                                     |
| `CURSOR_API_KEY`                                           | Both                              | The controller's API key, for the worker process. Unset with `--session-token`.                                                                  |
| `CURSOR_AUTH_TOKEN`, `CURSOR_AUTH_TOKEN_EXPIRES_AT`        | Claim mode with `--session-token` | [Session token](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#session-tokens) for this claim, and its expiry as an ISO 8601 timestamp. |
| `CURSOR_API_URL`, `CURSOR_API_ENDPOINT`                    | Both                              | API base the controller is using.                                                                                                                |

The spawn hook should start a worker with the same worker id:

```bash
#!/usr/bin/env bash
set -euo pipefail
agent worker --pool "$CURSOR_POOL" --worker-id "$CURSOR_AGENT_WORKER_ID" start
```

The worker CLI also reads `CURSOR_AGENT_WORKER_ID` from the environment, so a spawn hook that boots a container can pass the variables through instead:

```bash
#!/usr/bin/env bash
set -euo pipefail

docker run -d \
  -e CURSOR_API_KEY \
  -e CURSOR_AGENT_WORKER_ID \
  -e CURSOR_WORKER_POOL_NAME="$CURSOR_POOL" \
  your-worker-image \
  agent worker --pool start
```

### Claim-then-spawn

Default mode. The controller lists pending requests, watches `GET /v0/private-workers/pending-requests/stream`, claims each request, and execs `--spawn` once per claim.

```bash
agent worker controller --spawn ./spawn.sh --api-key "$CURSOR_API_KEY" --pool my-pool --pool default
```

### Warm pool

`--warm-idle <count>` keeps `<count>` idle workers connected in each `--pool` by pre-spawning unclaimed workers. It never calls claim. Cursor assigns queued agents to those warm workers.

The controller reconciles against `GET /v0/private-workers/pools` every 60 seconds. The pending-requests SSE stream only accelerates backfill.

Warm mode requires `--pool`. You cannot combine it with `--all-pools`. Run one warm controller per pool: there is no server-side spawn lease, so concurrent controllers can transiently over-spawn.

```bash
agent worker controller --spawn ./spawn.sh --api-key "$CURSOR_API_KEY" --pool my-pool --warm-idle 5
```

### Session tokens

By default, every machine the spawn hook starts holds the service account API key. With `--session-token`, the controller asks each claim for a session token and hands the hook that token instead, so the key stays on the controller.

```bash
agent worker controller --spawn ./spawn.sh --api-key "$CURSOR_API_KEY" --pool my-pool --session-token
```

The hook gets `CURSOR_AUTH_TOKEN` and `CURSOR_AUTH_TOKEN_EXPIRES_AT` in place of `CURSOR_API_KEY`. Write the token to a file and start the worker with `--auth-token-file`:

```bash
#!/usr/bin/env bash
set -euo pipefail
printf '%s' "$CURSOR_AUTH_TOKEN" > /run/cursor/token
agent worker --pool "$CURSOR_POOL" --auth-token-file /run/cursor/token start
```

A session token:

- **Serves one claim.** It can connect only the claimed worker id, and Cursor refuses it on every endpoint a worker doesn't call.
- **Ends with its claim.** It stops working when the claim is released, or when the service account key that minted it is deleted or expires. The 7-day expiry in `CURSOR_AUTH_TOKEN_EXPIRES_AT` is a backstop.
- **Can be replaced.** A worker that needs a token for a claim you already hold, such as a revived [hibernated](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#hibernation) machine or a run that outlasts its token, gets one from [Create A Session Token](https://cursor.com/docs/cloud-agent/api/endpoints.md#create-a-session-token). The controller does this for you when it wakes a hibernated machine. Write a replacement to the same file; the worker re-reads the file when it reconnects.

Warm workers start before any claim exists, so `--warm-idle` controllers still hand the hook the API key. When Cursor refuses a session token, the worker exits and prints the reason, such as the token's expiry time or that its claim has ended.

To build a custom controller instead, use the [Cloud Agents API](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#build-your-own-controller).

## Session lifecycle

Once a worker is matched to a request, Cursor forwards all agent tool calls directly to the machine. The connection has an idle timeout that defaults to 1 hour. Configure it as needed:

```bash
agent worker --pool my-pool --idle-release-timeout 600 start
```

`--idle-release-timeout` (env var `CURSOR_WORKER_IDLE_RELEASE_TIMEOUT`) is the number of seconds the worker stays connected after a session ends, waiting for follow-up messages. If a follow-up arrives, the timer resets. When the timeout fires, the CLI exits with code 0 so a supervisor can recycle the machine. Pass `0` to disable idle-based release. [Releasing a claim](https://cursor.com/docs/cloud-agent/api/endpoints.md#release-a-claim) is a separate API: it stops preferring that machine for the agent, and does not exit the worker CLI.

Once a worker times out, Cursor marks it as freed. The machine can reset and re-enter the pool. If a user restarts a chat that has disconnected from its machine, the chat reconnects to a fresh machine from the pool. Workspace state from the original machine does not carry over unless the pool uses [hibernation](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#hibernation).

## Hibernation

A pool machine does not have to stay online while its agent is idle. After a session ends, the worker waits for follow-ups until its [idle timeout](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#session-lifecycle) fires, and keeping every machine up between turns gets expensive.

The tradeoff is workspace locality. Without hibernation, a follow-up that arrives after the machine released reacquires from the pool: the agent lands on a fresh machine and may spend its first minutes reconstructing the workspace it already had. With hibernation, the machine comes back with its workspace intact and the follow-up resumes where the agent left off.

### Give the pool a reconnect window

`workerReadyTimeoutSeconds` controls how long Cursor waits for a claimed machine to reconnect before assigning the request to another worker. The default is `0`: follow-ups reacquire immediately.

```bash
curl --request POST \
  --url "https://api.cursor.com/v0/private-workers/pools" \
  -u "$CURSOR_API_KEY:" \
  --header 'Content-Type: application/json' \
  --data '{
    "scope": "team",
    "poolName": "my-pool",
    "workerReadyTimeoutSeconds": 900
  }'
```

### Snapshot machines when they go idle

Shorten the worker's [`--idle-release-timeout`](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#session-lifecycle) so machines release soon after the agent goes idle. When the worker exits (code 0 on idle release), or while [Get An Agent](https://cursor.com/docs/cloud-agent/api/endpoints.md#get-an-agent) reports a `status` of `IDLE`, snapshot the machine and stop it.

### Recognize the wake-up call

When a follow-up arrives for an agent whose claimed machine is offline, Cursor waits up to the reconnect window and advertises the request as a claimed-but-offline queue entry. Your controller recognizes it two ways: [List Pending Pool Requests](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pending-pool-requests) returns the entry with `claimedWorkerId` and `wakeTimeoutMs`, and the [event stream](https://cursor.com/docs/cloud-agent/api/endpoints.md#watch-pending-pool-requests) emits a `claimed_offline` event with the same fields.

### Bring the machine back up

Restore the snapshot and start a worker with the same id before the window lapses:

```bash
export CURSOR_AGENT_WORKER_ID="<claimedWorkerId>"
agent worker --pool my-pool start
```

The follow-up resumes on the machine with its workspace intact.

### Release the claim if you can't

If the machine is not coming back, for example the snapshot is gone, [release the claim](https://cursor.com/docs/cloud-agent/api/endpoints.md#release-a-claim). The request returns to the queue immediately, and a replacement machine can [claim](https://cursor.com/docs/cloud-agent/api/endpoints.md#claim-a-pending-request) it. If you do nothing, the window lapses on its own: the claim expires and the request is re-advertised as an unclaimed entry (a fresh `created` event) that any worker can serve.

## Build your own controller

The built-in controller covers most setups. If you need custom logic, for example your own scheduling, quotas, or machine placement, build a controller on the [Cloud Agents API](https://cursor.com/docs/cloud-agent/api/endpoints.md#workers-and-pools). A controller does three things: watch the request queue, claim a request, and start a worker for it. The same endpoints work for monitoring utilization and autoscaling outside Kubernetes.

Authenticate with the pool's service account API key via Basic auth or Bearer token. Other API key types can't manage pool worker capacity.

### Monitor the request queue

List the queue once to build your view of pending requests, then follow changes in real time over Server-Sent Events (SSE).

Start with [`GET /v0/private-workers/pending-requests`](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-pending-pool-requests). Add `?pool=<name>` to watch a single pool. Paginate to completion and keep the `streamCursor` from the response:

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/pending-requests?pool=my-pool&limit=50" \
  -u "$CURSOR_API_KEY:"
```

Then open the event stream with [`GET /v0/private-workers/pending-requests/stream`](https://cursor.com/docs/cloud-agent/api/endpoints.md#watch-pending-pool-requests), passing that `streamCursor` and the same filters. Keep your view current as events arrive: add requests from `created` and `claimed_offline` events, and drop requests when you see `claimed` or `expired`:

```bash
curl --request GET --no-buffer \
  --url "https://api.cursor.com/v0/private-workers/pending-requests/stream?pool=my-pool&cursor=$STREAM_CURSOR" \
  --header 'Accept: text/event-stream' \
  -u "$CURSOR_API_KEY:"
```

Cursors expire five minutes after the list that issued them. When the stream returns `410 Gone`, list again and reopen the stream from the fresh `streamCursor`. Better yet, list again every five minutes with some jitter instead of waiting for the `410`.

The number of requests in your view is the pool's queue depth. When it grows, add workers. Treat events as hints and the list as the source of truth: event delivery is best-effort, and each new list corrects any drift. See [Watch Pending Pool Requests](https://cursor.com/docs/cloud-agent/api/endpoints.md#watch-pending-pool-requests) for the full delivery guarantees and cursor rules.

### List workers

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers?status=idle&scope=team_pool&limit=50" \
  -u "$CURSOR_API_KEY:"
```

| Parameter   | Type                               | Default | Description                                                       |
| ----------- | ---------------------------------- | ------- | ----------------------------------------------------------------- |
| `status`    | `all` \| `in_use` \| `idle`        | `all`   | Filter by worker status                                           |
| `scope`     | `all` \| `team_pool` \| `personal` | `all`   | Filter by worker scope                                            |
| `limit`     | integer (1-100)                    | `50`    | Results per page                                                  |
| `pageToken` | string                             |         | Pagination cursor: the `nextPageToken` from the previous response |

Workers include `name`, `isInUse`, connection metadata, and repo fields (`repoOwner`/`repoName` are empty strings for any-repo workers). See the [API reference](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-workers) for the full response.

### List pools

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/pools?scope=team_pool" \
  -u "$CURSOR_API_KEY:"
```

Returns durable pools with `connectedWorkerCount`, `inUseWorkerCount`, `isStale`, and optional repo fields. Any-repo pools omit repo fields. Use this for connected and in-use counts per pool; the team-wide worker summary below is not a substitute for pool-specific demand.

### Get worker summary

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/summary" \
  -u "$CURSOR_API_KEY:"
```

Returns connected and in-use counts for your user and team. See [Get Worker Summary](https://cursor.com/docs/cloud-agent/api/endpoints.md#get-worker-summary). Use this to size your response when queue depth grows, or to trigger scaling when utilization is high:

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

### Claim a pending request

Ephemeral controllers can reserve a queued request before starting a worker:

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

Then start the worker with the same id (`CURSOR_AGENT_WORKER_ID=pw_123`). See [Claim A Pending Request](https://cursor.com/docs/cloud-agent/api/endpoints.md#claim-a-pending-request).

To keep the service account key off the worker, add `"sessionToken": true` to the body. The response then also carries a [session token](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#session-tokens) in `token`, with its expiry in `expiresAt`. Write the token to a file and start the worker with `--auth-token-file` instead of the key.

### Mint a session token

Get a fresh session token for a claim your team already holds, for example to revive a hibernated machine:

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

See [Create A Session Token](https://cursor.com/docs/cloud-agent/api/endpoints.md#create-a-session-token).

### Release a claim

Drop the claim that binds an agent to a self-hosted worker. Cursor then stops preferring that machine for the agent:

```bash
curl --request POST \
  --url "https://api.cursor.com/v0/private-workers/claims/bc-00000000-0000-0000-0000-000000000002/release" \
  -u "$CURSOR_API_KEY:"
```

A second claim while a live claim exists is rejected; release first, then claim a new `workerId`. See [Release A Claim](https://cursor.com/docs/cloud-agent/api/endpoints.md#release-a-claim).

## Monitoring

The management server exposes `GET /metrics`, `GET /healthz`, and `GET /readyz` when you start a worker with `--management-addr`:

```bash
agent worker --pool --management-addr ":8080" start
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

**Data flow.** Two things leave your network: file chunks the model reads during inference, and Cloud Agent [artifacts](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#artifacts) (screenshots, videos, and log references) the worker uploads to Cursor-managed storage so they can appear in PRs and the dashboard. Your repos, build caches, and secrets stay on your machines.

**Outbound-only.** Workers connect outbound over HTTPS. No inbound ports or firewall changes required.

**Privacy mode.** Self-hosted Cloud Agents respect Cursor's [Privacy Mode settings](/data-use). When Privacy Mode is enabled, none of your code is used for training.

**Isolation.** Each agent session gets its own dedicated worker. Sessions are not shared across workers.

**Authentication.** Pool workers authenticate with a [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md), or with a [session token](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#session-tokens) that serves one claim so the key never reaches the worker. Other API key types are rejected.

**Dashboard visibility.** Team admins can see all connected workers. Team members see only workers assigned to them.

## CLI reference

```bash
agent worker [options] start
```

| Flag                           | Description                                                                                                                                                                                                                                                                                                          |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--worker-dir <path>`          | Workspace root to expose to agents. Repeatable up to 20 paths. Each path must exist and be a directory. Git remotes are optional; see [any-repo pools](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#any-repo-pools). Default: current directory.                                                          |
| `--management-addr <addr>`     | Address for `/healthz`, `/readyz`, and `/metrics` endpoints, for example `:8080`.                                                                                                                                                                                                                                    |
| `--label <key=value>`          | Add a label. Repeatable. Mutually exclusive with `--labels-file`.                                                                                                                                                                                                                                                    |
| `--labels-file <path>`         | Path to JSON or TOML labels file. Mutually exclusive with `--label`. Env var: `CURSOR_WORKER_LABELS_FILE`.                                                                                                                                                                                                           |
| `--idle-release-timeout <sec>` | Seconds to stay connected after a session ends. Default: `3600`. Pass `0` to disable idle-based release. Env var: `CURSOR_WORKER_IDLE_RELEASE_TIMEOUT`.                                                                                                                                                              |
| `--computer-use`               | Let claimed agents drive this machine's desktop. On macOS, installs Cursor Computer Use if needed; grant it Accessibility and Screen Recording. See [Computer use](https://cursor.com/docs/cloud-agent/self-hosted/computer-use.md).                                                                                 |
| `--display <display>`          | Linux only. Existing X11 display to require for `--computer-use`, for example `:0`. When omitted, a reachable `DISPLAY` is reused or a managed desktop is started.                                                                                                                                                   |
| `--share-desktop [mode]`       | Linux only. Let authorized viewers watch or control the agent desktop: `view` or `view_and_control` (default). Separate from computer use; see [Share the agent desktop](https://cursor.com/docs/cloud-agent/self-hosted/computer-use.md#share-the-agent-desktop).                                                   |
| `--pool [name]`                | Register for pool assignment. Optional pool name; defaults to `default`. Each session claims one worker at a time. Env var: `CURSOR_WORKER_POOL_NAME`.                                                                                                                                                               |
| `--single-use`                 | Legacy alias for `--pool`.                                                                                                                                                                                                                                                                                           |
| `--pool-name <name>`           | Deprecated alias for `--pool <name>`. Env var: `CURSOR_WORKER_POOL_NAME`.                                                                                                                                                                                                                                            |
| `--api-key <key>`              | Service account API key for pool workers. Env var: `CURSOR_API_KEY`.                                                                                                                                                                                                                                                 |
| `--auth-token <token>`         | Pre-minted access token. Used by the Kubernetes operator and other automation that exchanges an API key for a short-lived token externally.                                                                                                                                                                          |
| `--auth-token-file <path>`     | File containing an access token, such as a [session token](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#session-tokens). The CLI re-reads this file when reconnecting after an auth failure or disconnect, which lets a controller rotate the mounted token without restarting the pod.                   |
| `--clone-git-repos`            | On claim, check out the agent's GitHub repos in the workspace: reuse a clean checkout of the same repo already in the worker directory, and clone the rest. Any-repo named pools only (not `default`, and not a bound repo or named machine). Implies `--mint-github-token`. Requires `git` on `PATH`. Default: off. |
| `--mint-github-token`          | Receive short-lived GitHub tokens during claimed runs. Pool workers only. Requires team-admin enablement. At most one credential-enabled worker per OS user or container.                                                                                                                                            |
| `--sync-dashboard-secrets`     | Receive eligible dashboard Cloud Agent secrets as environment variables during claimed runs. Pool workers only. Same one-worker-per-user rule.                                                                                                                                                                       |
| `--identity-socket`            | Serve a per-claim [OIDC token](https://cursor.com/docs/cloud-agent/identity.md#self-hosted-workers) socket to claimed agents. Sets `CURSOR_AGENT_SOCKET` to the socket's path in their shells. Off by default.                                                                                                       |
| `--worker-id <id>`             | Stable worker id used with [claim](https://cursor.com/docs/cloud-agent/api/endpoints.md#claim-a-pending-request). Prefer the env var so older CLI builds ignore an unknown flag. Env var: `CURSOR_AGENT_WORKER_ID`.                                                                                                  |
| `-e, --endpoint <url>`         | API endpoint. Default: `https://api2.cursor.sh`.                                                                                                                                                                                                                                                                     |

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
your custom worker image. [Personal skill
sync](https://cursor.com/docs/skills.md#use-personal-skills-with-cloud-agents) applies to
managed Cloud Agents, not self-hosted workers.

### Do MCP servers work on self-hosted workers?

Yes. Configure MCP servers through the Cloud Agents dashboard. See the
[MCP servers](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#mcp-servers) section for how routing works by transport type.

### Do hooks run on self-hosted workers?

Yes. Self-Hosted Machines workers run project hooks from
`.cursor/hooks.json`. On Enterprise, they also run team and
enterprise-managed hooks. See [Hooks](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#hooks).

### Can multiple agents use one pool worker?

A pool worker serves one agent at a time. Add workers or scale the pool when
requests wait for capacity.

### Can Mac pool workers run computer use?

Yes. Start them with `--computer-use`. The first start installs the
**Cursor Computer Use** helper app; grant it Accessibility and Screen
Recording, verify with a task that takes a screenshot, then snapshot the
machine. Screen Recording can't be granted silently by MDM, so approve it
once on the template and image from there. See [Computer use and desktop
sharing](https://cursor.com/docs/cloud-agent/self-hosted/computer-use.md#macos).

## Next steps

- [anysphere/k8s-workers](https://github.com/anysphere/k8s-workers): Kubernetes template built on `agent worker controller --spawn`, with claim-then-spawn and `--warm-idle` modes.
- [Integrations](https://cursor.com/docs/cloud-agent/self-hosted/integrations.md): partner guides and reference templates for other platforms.
- [Kubernetes operator (deprecated)](https://cursor.com/docs/cloud-agent/self-hosted/kubernetes.md): reference for clusters that already run the `WorkerDeployment` operator.
- [Computer use](https://cursor.com/docs/cloud-agent/self-hosted/computer-use.md): let agents drive a desktop and browser on your workers.
- [API reference](https://cursor.com/docs/cloud-agent/api/endpoints.md#workers-and-pools): endpoints for workers, pools, the pending-request queue, and worker tokens.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
