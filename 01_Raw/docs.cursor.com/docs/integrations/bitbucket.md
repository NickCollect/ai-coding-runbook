---
source_url: https://cursor.com/docs/integrations/bitbucket
fetched_at: 2026-06-22T06:23:25.498980+00:00
fetch_method: mintlify_md
---

# Bitbucket

The Bitbucket integration connects Bitbucket Cloud repositories so you can use [Cloud Agents](https://cursor.com/docs/cloud-agent.md) and [Bugbot](https://cursor.com/docs/bugbot.md).

The Bitbucket integration is in public beta. Cursor supports Bitbucket Cloud repositories on `bitbucket.org`. Bitbucket Server and Bitbucket Data Center are not supported.

## Setup

Bitbucket setup has two parts:

- Each developer connects their Bitbucket account so Cursor can clone repositories, push branches, and open pull requests as that user.
- A Bitbucket workspace admin installs the Cursor app so Bugbot and Cloud Agent status comments can appear as Cursor.

### Connect your Bitbucket account

Requires access to the Bitbucket workspace repositories you want to use.

1. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations)
2. Click **Connect** next to Bitbucket
3. Authorize Cursor in Bitbucket
4. Return to the dashboard and confirm the integration shows **Connected**

[Bitbucket setup](/docs-static/images/bitbucket/bitbucket-demo.mp4)

Each person who starts Cloud Agents or opens pull requests from Cursor should connect their own Bitbucket account.

### Install the Cursor app in Bitbucket

A Bitbucket workspace admin must install the Cursor app for the workspace. This gives Cursor a stable app identity for repository events, Bugbot review comments, inline comments, and status updates.

1. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations)
2. Find Bitbucket and open the manage menu
3. Click **Install Cursor app**
4. Install the app in your Bitbucket workspace
5. In Bitbucket workspace settings, under **Forge Apps**, select **Cursor**
6. Click **Connect to Cursor** and choose the Cursor team to link

When the workspace is linked, the dashboard shows the Cursor app installed for that Bitbucket workspace.

Bitbucket can take a few minutes to notify Cursor after app installation. If Cursor cannot find the workspace right away, wait and try the link step again.

## How Cursor uses Bitbucket identities

Cursor uses different Bitbucket identities for different actions:

| Action                                                       | Bitbucket identity           |
| ------------------------------------------------------------ | ---------------------------- |
| Bugbot summary comments, inline comments, and build statuses | Cursor app                   |
| Cloud Agent progress comments on pull requests               | Cursor app                   |
| Git clone, branch push, commits, and pull request creation   | The connected Bitbucket user |

This means pull requests opened by Cloud Agents are attributed to the person who started the agent. Bugbot output appears from Cursor when the workspace app is installed.

## Permissions

The Bitbucket integration asks for permissions needed to support Cloud Agents and Bugbot:

| Permission             | Purpose                                    |
| ---------------------- | ------------------------------------------ |
| **Account**            | Identify the connected Bitbucket user      |
| **Repositories**       | List, clone, and read repository content   |
| **Pull requests**      | Read pull request diffs and metadata       |
| **Pull request write** | Create pull requests and post comments     |
| **Webhooks**           | Receive repository and pull request events |

## Disconnect Bitbucket

Disconnecting Bitbucket has two separate effects:

- **Disconnect account** removes your personal Bitbucket OAuth connection from Cursor.
- **Disconnect Cursor app** unlinks the Bitbucket workspace from your Cursor team. The app can remain installed in Bitbucket until a workspace admin removes it there.

To fully stop app events from the workspace, uninstall the Cursor app from Bitbucket workspace settings.

## Troubleshooting

### Cursor cannot find my Bitbucket workspace

Bitbucket app installation events can take a few minutes to sync. Wait and retry the **Connect to Cursor** step from Bitbucket workspace settings.

### Bugbot comments do not appear as Cursor

Install the Cursor app in the Bitbucket workspace and link it to your Cursor team. A personal Bitbucket connection alone is not enough for Cursor app comments.

### Cloud Agent cannot access a Bitbucket repository

- Connect your personal Bitbucket account from the integrations dashboard.
- Confirm your Bitbucket user has read-write access to the repository.
- Confirm the repository is on Bitbucket Cloud at `bitbucket.org`.

## Next steps

Once Bitbucket is connected, configure the features that use it:

- [Bugbot](https://cursor.com/docs/bugbot.md) - automated PR reviews that catch bugs and security issues
- [Cloud Agents](https://cursor.com/docs/cloud-agent.md) - AI agents that run in the cloud on your repositories


---

## Sitemap

[Overview of all docs pages](/llms.txt)
