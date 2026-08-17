---
source_url: https://cursor.com/docs/cloud-agent/capabilities
fetched_at: 2026-08-17T02:15:17.573019+00:00
fetch_method: mintlify_md
---

# Capabilities

## Computer use

Each cloud agent runs in its own isolated VM with a full desktop environment. Agents can use a mouse and keyboard to control the desktop and browser, allowing them to interact with the software they build like a human developer.

This means agents can start dev servers, open the app in a browser, click through UI flows, and verify their changes work before pushing a PR. Read more in the [announcement blog post](/blog/agent-computer-use).

## Demos and Artifacts

Agents create artifacts such as screenshots, videos, and log references to demonstrate their work. These artifacts are attached to the PR so you can quickly validate changes without checking out the branch locally.

### Artifacts in GitHub

You can opt-in to have Cloud Agents embed artifacts directly into GitHub pull request descriptions by enabling the **Allow posting artifacts to GitHub** setting in the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#my-pull-requests).

GitHub's [image proxy](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-anonymized-urls) requires public URLs, so artifacts in PR descriptions use long, unguessable URLs that are viewable without authentication. For context, GitHub used public URLs for all issue and PR attachments until [May 2023](https://github.blog/changelog/2023-05-08-more-secure-private-attachments).

## Remote desktop control

You can take control of the agent's remote desktop to interact with the software the agent is building. Hand control back to the agent at any time to let it keep working.

Cloud agents run in a remote VM that can be fully onboarded with your repo, dependencies, tooling, and setup scripts. This allows you to test changes directly in the agent's VM without checking out the branch on your local machine.

## MCP tools

Cloud agents can use [MCP (Model Context Protocol)](https://cursor.com/docs/mcp.md) servers configured for your team. This gives agents access to external tools and data sources like databases, APIs, and third-party services during their runs.

Add and enable personal MCP servers through the MCP dropdown in [cursor.com/agents](https://cursor.com/agents). Team admins configure shared servers under **Dashboard -> Integrations & MCP**.

Admins can link shared Team MCP servers to the [Default team marketplace](https://cursor.com/docs/plugins.md#migrate-existing-team-mcps). Linking keeps the servers available to Cloud Agents and also makes them available for teammates to install and configure in the Agent Window, IDE, and CLI.

Cloud agents support OAuth for MCP servers that need it. OAuth is per-user, including for MCP servers shared at the team level.

### Custom MCP servers

You can add custom MCP servers using either **HTTP** or **stdio** transport. SSE and `mcp-remote` are not supported.

MCP configurations are encrypted at rest. Sensitive fields are redacted and cannot be read back by any user after saving:

- **`env`** — environment variables for stdio servers
- **`headers`** — request headers for HTTP servers
- **`CLIENT_SECRET`** — OAuth client secret for HTTP servers

### HTTP vs stdio

- **HTTP (recommended)** — server configurations are never present in the cloud agent's VM environment. The agent does not have access to refresh tokens, headers, or other credentials. Tool calls are proxied through the backend.
- **Stdio** — servers run inside the cloud agent's VM, so the agent has access to the server's configuration and environment variables. This is similar to how stdio MCPs work in the Cursor IDE.

Stdio servers depend on the VM environment to execute. We cannot verify that a stdio server will run successfully until a cloud agent is launched. We recommend using HTTP MCPs when possible, and configuring your [environment setup](https://cursor.com/docs/cloud-agent/setup.md) correctly if you use stdio servers.

### Cursor Cloud MCP

The Cursor Cloud MCP is a built-in diagnostics server available during Cloud Agent runs. It lets an agent inspect the current run, browse related runs in the same environment, and fetch transcripts, diff metadata, environment details, run events, and setup logs without manually collecting links and files.

Team admins can disable Cursor Cloud MCP for their team from **MCP Configuration** in [team settings](https://cursor.com/dashboard/settings). See [Team dashboard](https://cursor.com/docs/account/teams/dashboard.md#mcp-configuration) for more on MCP admin controls.

#### Access and permissions

Cloud Agent conversations can include prompts, code, tool output, and secrets. All tools enforce access checks on every request.

| Role       | What you can access                                                                                                                                |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| Team admin | List and fetch details (including transcripts) for Cloud Agent runs across the team, for repositories and environments they already have access to |
| Non-admin  | Only your own runs and transcripts. You cannot view other team members' chats through this MCP                                                     |

Even when listing runs in a shared environment, non-admins only see agents they started or own. Service accounts follow the same rules as the user or team context they run under.

#### What you can inspect

| Category      | Examples                                                                                                                                                                                                                         |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Current run   | Run ID, URL, repo, branch, model, owner, lifecycle status, and where the run was started (Cursor, Slack, GitHub, API, and others)                                                                                                |
| Events        | Setup, pull request, artifact, and MCP authentication outcomes shown on the run dashboard. Use `get-events` for the current run, or `batch-fetch-details` with `include_events` for other runs. See the event kinds under Tools. |
| Related runs  | Other Cloud Agents in the same environment, or on the same repository when no saved environment is attached                                                                                                                      |
| Environment   | Environment version, full environment config, dashboard URL, and effective egress network policy                                                                                                                                 |
| Transcript    | Full user-agent conversation, including tool calls when available                                                                                                                                                                |
| Diff metadata | Whether the agent changed code, how much changed, and whether it opened a PR                                                                                                                                                     |
| Setup logs    | Raw logs from environment setup and image-build steps                                                                                                                                                                            |

#### Tools

Depending on your MCP client, tool names may include a server prefix (for example, `cursor-cloud-run-info`). The underlying tools are:

| Tool                                | Purpose                                                                                                                                                                                                                 |
| :---------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `run-info`                          | Get the current run's identity, metadata, and URL. Start here.                                                                                                                                                          |
| `environment-info`                  | Get the current run's environment version, config, dashboard URL, and effective egress policy.                                                                                                                          |
| `get-events`                        | List the current run's dashboard events, oldest first.                                                                                                                                                                  |
| `list-cloud-agents`                 | Browse Cloud Agent runs visible to you in this environment. Filter by source, status, date, code changes, PR creation, and archived state.                                                                              |
| `batch-fetch-details`               | Fetch details for specific run IDs (`bcId`s). Optionally include transcripts, diff metadata, setup logs, environment info, and run events via `include_events` (writes `events.json` per run; up to 50 runs per batch). |
| `get-automation`                    | Get an automation's details like name and owner from its ID.                                                                                                                                                            |
| `list-environment-builds`           | List recent [Builds](https://cursor.com/docs/cloud-agent/builds.md) for the current environment and inspect their status.                                                                                               |
| `environment-build-logs`            | Download the install and setup logs for a Build.                                                                                                                                                                        |
| `trigger-environment-build`         | Run a test Build with the current configuration or proposed install and start commands.                                                                                                                                 |
| `propose-environment-json`          | Present install and start commands for you to review before saving the environment.                                                                                                                                     |
| `take-environment-snapshot`         | Snapshot a machine after the agent verifies its environment setup.                                                                                                                                                      |
| `check-environment-snapshot`        | Check whether an environment snapshot is ready.                                                                                                                                                                         |
| `request-environment-setup-actions` | Request user actions that block environment setup, such as adding a secret.                                                                                                                                             |

Dashboard event `kind` values from `get-events` and from `batch-fetch-details` with `include_events` are:

| `kind`               | Meaning                                                                          |
| :------------------- | :------------------------------------------------------------------------------- |
| `setup_started`      | Environment setup began.                                                         |
| `setup_completed`    | Environment setup finished.                                                      |
| `setup_failed`       | Environment setup failed.                                                        |
| `pr_created`         | Pull request opened.                                                             |
| `pr_creation_failed` | Pull request creation failed.                                                    |
| `artifact_created`   | Walkthrough artifact uploaded.                                                   |
| `mcp_auth_error`     | MCP server authentication failed; its tools were skipped, and the run continued. |

A typical diagnostics flow is `run-info` → `get-events` → `environment-info` → `list-cloud-agents` → `batch-fetch-details` (set `include_events` when you need other runs' dashboard events).

## Fixing CI Failures

Cloud Agents automatically try to fix CI failures in PRs they create. This currently supports GitHub Actions only.

Cloud Agents skip automatic CI follow-ups if:

- You've pushed a new commit to the branch; cloud agents do not auto-fix CI failures on human commits.
- You've sent a follow-up message to the agent.
- The same check is already failing on the base commit of the PR.
- The PR has already had 10 CI-failure follow-ups.

To disable this feature on all your personal Cloud Agents, go to [Cursor Dashboard → Cloud Agents → My Settings](https://cursor.com/dashboard/cloud-agents) and disable the "Automatically fix CI Failures" option.

To disable this feature on a specific Cloud Agent PR, you can comment `@cursor autofix off` on the PR. To re-enable it, comment `@cursor autofix on`.

If you want cloud agents to fix CI failures in your own PRs, you can simply ask them by tagging Cursor in a comment as normal. For example, `@cursor please fix the CI failures`, or `@cursor fix the CI lint check failure`.

Automatically fixing CI failures is currently only available on Teams; support for non-Teams accounts is coming soon. In the meantime, if you want similar behavior, you can ask the cloud agent explicitly to monitor and fix CI failures on the PR.

## OIDC identity tokens

Cursor-managed Cloud Agent VMs can mint short-lived OIDC JWTs from a local socket. Agents use them to assume cloud roles or call internal APIs without storing long-lived keys. See [OIDC tokens](https://cursor.com/docs/cloud-agent/identity.md).

## Agent metadata

The same socket also serves [agent metadata](https://cursor.com/docs/cloud-agent/metadata.md). Agents, hooks, and scripts can read the agent id, owner, current turn, and workspace as plain text.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
