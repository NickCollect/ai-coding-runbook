---
source_url: https://cursor.com/docs/integrations/slack
fetched_at: 2026-09-21T05:44:02.740818+00:00
fetch_method: mintlify_md
---

# Slack

With Cursor's integration for Slack, you can use [Cloud Agents](https://cursor.com/docs/cloud-agent.md) to work on your tasks directly from Slack by mentioning `@cursor` with a prompt.

[Media](/docs-static/images/cloud-agent/slack/slack-agent.mp4)

## Get started

### Installation

1. Go to [Cursor integrations](https://www.cursor.com/dashboard/integrations)

2. Click *Connect* next to Slack or go to [installation page](https://cursor.com/api/install-slack-app) from here

3. You'll be prompted to install the Cursor app for Slack in your workspace.

4. After installing in Slack, you'll be redirected back to Cursor to finalize setup

   1. Connect a repository provider (if not already connected) and pick a default repository
   2. Enable usage-based pricing
   3. Confirm privacy settings

5. Start using Cloud Agents in Slack by mentioning `@cursor`

## How to use

Mention `@cursor` and give your prompt. Cursor tries to detect a repository, model, base branch, or named [cloud agent environment](https://cursor.com/docs/cloud-agent/setup.md) from your message. It also uses your recent agent activity when selecting a repository.

For a named environment, include its name in your prompt. For example: `@Cursor use the Platform environment to update the shared API`.

### Commands

Run `@Cursor help` for an up-to-date command list.

| Command                      | Description                                                                                                                                                 |
| :--------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `@Cursor [prompt]`           | Start a Cloud Agent. In threads with existing agents, adds follow-up instructions. Who can follow up is controlled by Team follow-ups, not ownership alone. |
| `@Cursor settings`           | Configure defaults and channel's default repository. Also shows the [team default pool](https://cursor.com/docs/integrations/slack.md#team-default-pool)    |
| `@Cursor [options] [prompt]` | Set the target, model, branch, PR behavior, worker, or output channel for a run                                                                             |
| `@Cursor agent [prompt]`     | Force create a new agent in a thread (e.g. `@Cursor start a new agent to fix billing`)                                                                      |
| `@Cursor list my agents`     | Show your running agents                                                                                                                                    |
| `@Cursor pool`               | Show the [team default pool](https://cursor.com/docs/integrations/slack.md#team-default-pool) for Slack launches                                            |
| `@Cursor pool set <name>`    | Set the team default pool (team admins)                                                                                                                     |
| `@Cursor pool unset`         | Clear the team default pool (team admins)                                                                                                                   |

#### Options

Customize Cloud Agent behavior with these options:

| Option                | Description                                                                                                                                                                                                                    | Natural language example       | Inline example      |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------- | :------------------ |
| `repo`                | Use a specific repository                                                                                                                                                                                                      | `in acme/backend`              | `repo=acme/backend` |
| `env` / `environment` | Use a named [cloud agent environment](https://cursor.com/docs/cloud-agent/setup.md)                                                                                                                                            | `use the Platform environment` | `env=Platform`      |
| `branch`              | Use a specific base branch                                                                                                                                                                                                     | `work from the dev branch`     | `branch=dev`        |
| `model`               | Use a specific model                                                                                                                                                                                                           | `with opus`                    | `model=opus`        |
| `autopr`              | Enable or disable automatic PR creation                                                                                                                                                                                        | Inline option required         | `autopr=false`      |
| `worker` / `machine`  | Run on a named [My Machine](https://cursor.com/docs/cloud-agent/self-hosted/my-machines.md)                                                                                                                                    | Inline option required         | `worker=my-devbox`  |
| `pool`                | Run on a named [Team Pool](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#triggering-pool-agents). Optional when your team has a [team default pool](https://cursor.com/docs/integrations/slack.md#team-default-pool) | Inline option required         | `pool=gpu`          |
| `self_hosted`         | Run on one of your Team Pools. Uses the [team default pool](https://cursor.com/docs/integrations/slack.md#team-default-pool) when one is set; `self_hosted=false` skips it                                                     | Inline option required         | `self_hosted=true`  |
| `channel`             | Post agent updates in another channel you and Cursor can access                                                                                                                                                                | Inline option required         | `channel=#eng-bots` |

#### Syntax formats

Natural:

```bash
@Cursor with opus, fix the login bug in backend-api
```

Inline:

```bash
@Cursor env=Platform branch=dev model=opus autopr=false Fix the login bug
```

Use quotes for environment names with spaces:

```bash
@Cursor env="Platform Services" Update the shared API
```

#### Option precedence

When combining options:

- **Explicit values** override defaults
- **Later values** override earlier ones if duplicated
- **Inline options** take precedence over settings modal defaults
- **`env`** takes precedence over `repo` when both are present
- **`pool`, `worker`, `machine`, and `self_hosted=false`** take precedence over the [team default pool](https://cursor.com/docs/integrations/slack.md#team-default-pool)

The bot parses options from anywhere in the message, allowing natural command writing.

#### Using thread context

Cloud Agents understand and use context from existing thread discussions. Useful when your team discusses an issue and you want the agent to implement the solution based on that conversation.

Cloud Agents read the entire thread for context when invoked,
understanding and implementing solutions based on the team's discussion.

#### When to use force commands

**When do I need `@Cursor agent`?**

In threads with existing agents, `@Cursor [prompt]` adds follow-up instructions. Who can follow up is controlled by [Team follow-ups](https://cursor.com/docs/cloud-agent/settings.md#team-follow-ups). If Team follow-ups is Disabled, only the owner can follow up. To launch a separate agent, use `@Cursor agent [prompt]`, or ask in natural language:

```bash
@Cursor start a new agent to refactor billing
```

Phrases like "create a new agent", "launch a fresh agent", or "new agent please" work the same way.

**When do I need `Add follow-up` (from context menu)?**

Use the context menu (⋯) on an agent's response for followup instructions. Useful when multiple agents exist in a thread and you need to specify which one to follow up on.

### Status updates & handoff

Before Cursor starts changing code, it posts a short plan in the thread when you are fixing a bug or when implementation details would help you follow along. Straightforward requests skip that note. While it works, Cursor updates a short status under the thread.

When Cloud Agent runs, you first get an option to *Open in Cursor*.

![Open in Cursor button in Slack](/docs-static/images/cloud-agent/slack/slack-open-in-cursor.png)

When Cloud Agent completes, you get a notification in Slack and an option to view the created PR in GitHub.

![View PR in GitHub in Slack](/docs-static/images/cloud-agent/slack/slack-view-pr.png)

### Managing agents

To see all running agents, run `@Cursor list my agents`.

Manage Cloud Agents using the context menu by clicking the three dots (⋯) on any agent message.

![Slack agent context menu](/docs-static/images/cloud-agent/slack/slack-context-menu.png)

Available options:

- **Add follow-up**: Add instructions to an existing agent
- **Switch repository**: Relaunch the same request against a different repository or [cloud agent environment](https://cursor.com/docs/cloud-agent/setup.md)
- **Delete**: Stop and archive the Cloud Agent
- **View request ID**: View unique request ID for troubleshooting (include when contacting support)
- **Give feedback**: Provide feedback about agent performance

If the agent needs a repository or environment outside the current one, Slack also shows **Switch repository** on the launch message. Choose the new target and Cursor continues from there.

## Configuration

Manage default settings and privacy options from [Dashboard → Cloud Agents](https://www.cursor.com/dashboard/cloud-agents).

### Settings

#### Default Model

Used when no model is specified in your message. See [settings](https://www.cursor.com/dashboard/cloud-agents) for available options.

#### Repository Selection

Cursor automatically selects the right repository based on:

1. **Your message content** — Repository names or keywords in your prompt
2. **Recent agent activity** — Repositories you've used recently
3. **Routing rules** — Custom keyword-to-repo mappings (see below)
4. **Default repository** — Fallback when no match is found

To use a specific repository, include its name in your message. For example: `@Cursor in mobile-app, fix the login bug`.

#### Base Branch

Starting branch for Cloud Agent. Leave blank to use the repository's default branch (often `main`)

### Channel Settings

Configure default settings at the channel level using `@Cursor settings`. These settings are per team and override your personal defaults for that channel.

Channel settings only apply to public channels.

Particularly useful when:

- Different channels work on different repositories
- Teams want consistent settings across all members

To configure channel settings:

1. Run `@Cursor settings` in the desired channel
2. Set the default repository for that channel
3. All team members using Cloud Agents in that channel use these defaults

Channel settings take precedence over personal defaults but can be overridden
by mentioning a specific repo in your message.

### Routing Rules

Routing rules let you define keywords that automatically map to a target. When your message contains a keyword, Cursor routes the agent to the associated repository or [cloud agent environment](https://cursor.com/docs/cloud-agent/setup.md). Environments can bundle multiple repositories, so one keyword can start an agent with every repo it needs already configured.

#### Setting up routing rules

1. Go to [Dashboard → Cloud Agents](https://www.cursor.com/dashboard/cloud-agents)
2. Find the **Routing Rules** section
3. Add keyword-to-target mappings, pointing each keyword at a repository or an environment

#### Example rules

| Keyword    | Target                  |
| :--------- | :---------------------- |
| `frontend` | `acme/web-app`          |
| `mobile`   | `acme/mobile-app`       |
| `api`      | `acme/backend-services` |
| `platform` | `Platform` environment  |

With these rules configured:

- `@Cursor fix the frontend nav bug` → routes to `acme/web-app`
- `@Cursor update the mobile onboarding flow` → routes to `acme/mobile-app`
- `@Cursor add a migration across the platform` → starts in the `Platform` environment, with all its repos ready

Targeting an environment is useful for multi-repo environments. Learn how to
configure one in the [cloud agent docs](https://cursor.com/docs/cloud-agent/setup.md), including
[multi-repo environments](https://cursor.com/docs/cloud-agent/setup.md#multi-repo-environments).

#### How routing works

Cursor evaluates your message in this order:

1. **Your message content** — Repository names or keywords in your prompt
2. **Recent agent activity** — Repositories you've used recently
3. **Routing rules** — Custom keyword-to-target mappings (repository or environment)
4. **Channel default** — The repository set for this channel
5. **Default repository** — Fallback when no match is found

### Team default pool

Team admins can set one [Team Pool](https://cursor.com/docs/cloud-agent/self-hosted/pool.md) as the default for `@Cursor` launches. Members then run on that pool without adding `pool=<name>` or `self_hosted=true` to every mention. The default applies to the whole team, in every channel.

Team Pools require an Enterprise plan. The team default only applies while
**Allow Self-Hosted Machines** is on in the [Cloud Agents
dashboard](https://cursor.com/dashboard/cloud-agents#self-hosted-agents). If
an admin turns it off, Slack ignores the default and mentions run on Cursor's
managed infrastructure.

Manage the default from Slack. Setting or clearing it requires the same permission as changing Self-Hosted settings in the dashboard. Anyone can view it.

```bash
@Cursor pool set gpu
@Cursor pool
@Cursor pool unset
```

`@Cursor settings` also lists the team default pool.

#### How Cursor picks where a mention runs

Options in your message always win. Cursor resolves the target in this order:

1. **Options in your message.** `pool=<name>` targets that pool. `worker=` or `machine=` targets one of your [My Machines](https://cursor.com/docs/cloud-agent/self-hosted/my-machines.md). `self_hosted=false` runs on Cursor's managed infrastructure. Each of these skips the team default. A bare `self_hosted=true` fills in the team default pool.
2. **Your default My Machines worker.** If you have a default worker of your own, it outranks the team default pool.
3. **Team default pool.** Used when your message has none of the options above.

#### Repositories and the team default pool

[Repository selection](https://cursor.com/docs/integrations/slack.md#how-routing-works) works the same way with a team default pool: message content, recent activity, routing rules, channel default, then your default repository and the team's. What happens next depends on how the pool is registered:

- **Any repo pool, no repository resolved.** Slack starts an agent on the pool without a repository. Source control is up to the worker, as with any [any-repo pool](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#any-repo-pools). If a default repository does resolve, the agent gets it as context without limiting which workers can claim the run.
- **Repo-bound pool, no repository resolved.** Slack rejects the mention with an ephemeral reply instead of falling back to managed infrastructure. Add `repo=` or `pool=` to the mention, use `self_hosted=false` to run on managed infrastructure, or check the default with `@Cursor pool` and `@Cursor settings`.
- **Repository resolved and the pool serves it.** Slack launches with `repo=` and `pool=` set, the same as an explicit `pool=<name>` mention.
- **Repository resolved but the pool's workers only serve other repositories.** Slack rejects the mention with an ephemeral reply. Pick a repository the pool serves with `repo=`, or a pool that serves this repository with `pool=`.

### Privacy

Cloud Agents support Privacy Mode.

Read more about [Privacy Mode](https://www.cursor.com/privacy-overview) or manage your [privacy settings](https://www.cursor.com/dashboard/cloud-agents).

Privacy Mode (Legacy) is not supported. Cloud Agents require temporary
code storage while running.

#### Display Agent Summary

Display agent summaries and diff images. May contain file paths or code snippets. Can be turned On/Off.

#### Display Agent Summary in External Channels

For Slack Connect with other workspaces or channels with external members like Guests, choose to display agent summaries in external channels.

## Permissions

Cursor requests these Slack permissions for Cloud Agents to work within your workspace:

| Permission          | Description                                                                         |
| :------------------ | :---------------------------------------------------------------------------------- |
| `app_mentions:read` | Detects @mentions to start Cloud Agents and respond to requests                     |
| `channels:history`  | Reads previous messages in threads for context when adding follow-up instructions   |
| `channels:join`     | Automatically joins public channels when invited or requested                       |
| `channels:read`     | Accesses channel metadata (IDs and names) to post replies and updates               |
| `chat:write`        | Sends status updates, completion notifications, and PR links when agents finish     |
| `files:read`        | Downloads shared files (logs, screenshots, code samples) for additional context     |
| `files:write`       | Uploads visual summaries of agent changes for quick review                          |
| `groups:history`    | Reads previous messages in private channels for context in multi-turn conversations |
| `groups:read`       | Accesses private channel metadata to post responses and maintain conversation flow  |
| `im:history`        | Accesses direct message history for context in continued conversations              |
| `im:read`           | Reads DM metadata to identify participants and maintain proper threading            |
| `im:write`          | Initiates direct messages for private notifications or individual communication     |
| `mpim:history`      | Accesses group DM history for multi-participant conversations                       |
| `mpim:read`         | Reads group DM metadata to address participants and ensure proper delivery          |
| `reactions:read`    | Observes emoji reactions for user feedback and status signals                       |
| `reactions:write`   | Adds emoji reactions to mark status - ⏳ for running, ✅ for completed, ❌ for failed  |
| `team:read`         | Identifies workspace details to separate installations and apply settings           |
| `users:read`        | Matches Slack users with Cursor accounts for permissions and secure access          |

## Disclaimer

Cursor can make mistakes. Please double-check code and responses.

## Privacy Policy

For information about how Cursor collects, uses, and protects your data, see our [Privacy Policy](https://cursor.com/privacy).


---

## Sitemap

[Overview of all docs pages](/llms.txt)
