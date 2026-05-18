---
source_url: https://cursor.com/docs/integrations/jira
fetched_at: 2026-05-18T05:02:44.442005+00:00
fetch_method: mintlify_md
---

# Jira

With Cursor's integration for Jira, you can use [Cloud Agents](https://cursor.com/docs/cloud-agent.md) to work on Jira work items by assigning them to Cursor or mentioning `@Cursor` in Jira.

## Get started

### Requirements

Before you install the Jira integration, make sure you have:

- Jira Cloud with Rovo enabled
- Admin access to the Jira site where you want to install the app
- Cursor admin access
- GitHub or GitLab connected to Cursor for repository access and pull requests

The Cursor Jira integration is not currently supported in Atlassian HIPAA or
FedRAMP, including Gov Cloud, instances.

### Installation

1. As a Cursor admin, go to [Cursor integrations](https://www.cursor.com/dashboard/integrations)

2. Click *Connect* next to Jira

3. Continue to the Cursor app listing in the [Atlassian Marketplace](https://marketplace.atlassian.com/)

4. Click *Get app*

5. Select the Jira site where you want to install Cursor

6. Review the requested permissions, then click *Install*

7. After installing in Jira, follow the setup prompt to connect the Jira site to Cursor

8. Complete any remaining Cloud Agent setup in Cursor:

   1. Connect GitHub or GitLab, if you haven't connected a repository provider yet
   2. Enable usage-based pricing
   3. Confirm privacy settings
   4. Choose a default repository, model, and base branch

9. Return to Jira and start using Cursor from a work item

### Opening the configuration page manually

If the setup prompt doesn't open after installation, open the configuration page from Jira:

1. In Jira, go to *Apps*
2. Click *Manage apps*
3. Find *Cursor* in the installed apps list
4. Click *Configure*
5. Connect the Jira site to your Cursor team

### Authentication mode

Choose how Jira authenticates cloud agents once you've connected Jira to your Cursor team.

| Mode                           | How it works                                                                                              | Settings used                                                                              |
| :----------------------------- | :-------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| Service account authentication | Runs all Cloud Agents started from Jira under a service account.                                          | Uses only the team's Cloud Agent settings for routing, models, repositories, and defaults. |
| User-level authentication      | Connects each Jira user to their Cursor account. Users can find their own running Cloud Agents from Jira. | Uses each user's Cloud Agent settings for routing, models, repositories, and defaults.     |

## How to use

Open a Jira work item, then assign it to Cursor or mention `@Cursor` in a comment. Cursor uses the work item title, description, comments, and available repository settings to start a Cloud Agent.

You can ask Cursor to fix bugs, add features, update tests, or investigate a task described in the work item.

### Delegating work items

Assign a Jira work item to Cursor when the ticket already describes the task clearly.

1. Open the Jira work item
2. Click the assignee field
3. Select Cursor
4. Review the Cloud Agent that starts from the work item

### Mentioning Cursor

Mention `@Cursor` in a Jira comment when you want to add specific instructions. You can include a repository, branch, or model in the same comment.

Examples:

- `@Cursor please investigate this regression`
- `@Cursor repo=acme/backend branch=release fix this before the release cut`
- `@Cursor use gpt-5.2 and update the related tests`

### Follow-up instructions

Open Rovo chat from the Jira work item to continue the conversation with Cursor.

### Status updates and handoff

When a Cloud Agent starts, Jira shows agent status on the work item. Cursor posts progress while it works and returns a summary when the task completes.

If Cursor opens a pull request, the completion update links to the PR for review.

## Configuration

Manage default settings and privacy options from [Dashboard -> Cloud Agents](https://www.cursor.com/dashboard/cloud-agents).

### Settings

#### Default model

Used when no model is specified in the Jira work item or comment. See [settings](https://www.cursor.com/dashboard/cloud-agents) for available options.

#### Repository selection

Cursor selects the repository based on:

1. **Explicit values**: `repo`, `branch`, or `model` values in the Jira comment or work item
2. **Work item content**: repository names, service names, or keywords in the title, description, and comments
3. **Recent agent activity**: repositories you've used recently
4. **Default repository**: fallback when no match is found

To use a specific repository, include it in your comment. For example: `@Cursor repo=acme/mobile-app fix the login bug`.

#### Base branch

Starting branch for Cloud Agent. Leave blank to use the repository's default branch, often `main`.

### Options

Customize Cloud Agent behavior with these options:

| Option   | Description         | Example             |
| :------- | :------------------ | :------------------ |
| `repo`   | Specify repository  | `repo=acme/web-app` |
| `branch` | Specify base branch | `branch=main`       |
| `model`  | Specify model       | `model=opus`        |

### Privacy

Cloud Agents support Privacy Mode.

Read more about [Privacy Mode](https://www.cursor.com/privacy-overview) or manage your [privacy settings](https://www.cursor.com/dashboard/cloud-agents).

Privacy Mode (Legacy) is not supported. Cloud Agents require temporary code
storage while running.

## Permissions

During installation, Jira shows the permissions requested by the Cursor app. Cursor uses these permissions to:

- Identify the Jira user starting or managing a Cloud Agent
- Read work item fields, descriptions, comments, and related context
- Post status updates, completion summaries, and pull request links
- Receive events when work items are assigned to Cursor or mention `@Cursor`

Review the permission prompt in Atlassian Marketplace before installing the app.

## FAQ

### Which Jira sites are supported?

The Cursor Jira integration supports Atlassian commercial cloud sites with Rovo enabled. Atlassian HIPAA, FedRAMP, and Gov Cloud instances are not supported.

### Do I need usage-based billing?

Yes. Cloud Agents require usage-based billing. Enable usage-based billing while completing Cloud Agent setup in Cursor.

### Who can install the Jira integration?

You need to be a Jira admin to install the Cursor app in Jira. You also need to be a Cursor admin to connect Jira to your Cursor team from the Cursor dashboard.

### Do users need to connect their own Cursor accounts?

It depends on the authentication mode you choose. Service account authentication runs all Cloud Agents under a service account and uses team settings. User-level authentication connects each Jira user to Cursor, lets users find their own running Cloud Agents from Jira, and uses each user's settings for routing, models, repositories, and defaults.

### What else needs to be set up before Cursor can create PRs?

Connect GitHub or GitLab to Cursor and make sure Cloud Agent settings include the repositories, models, and base branches your team wants to use.

### How do users continue a conversation with Cursor?

Open Rovo chat from the Jira work item to continue the conversation with Cursor.

## Disclaimer

Cursor can make mistakes. Please double-check code and responses.

## Privacy Policy

For information about how Cursor collects, uses, and protects your data, see our [Privacy Policy](https://cursor.com/privacy).


---

## Sitemap

[Overview of all docs pages](/llms.txt)
