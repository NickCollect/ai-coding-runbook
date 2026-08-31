---
source_url: https://cursor.com/docs/integrations/azure-devops
fetched_at: 2026-08-31T06:29:32.584151+00:00
fetch_method: mintlify_md
---

# Azure DevOps

The Azure DevOps integration connects Azure DevOps Services repositories to [Cloud Agents](https://cursor.com/docs/cloud-agent.md) and [Bugbot](https://cursor.com/docs/bugbot.md).

The Azure DevOps integration is in public beta. It supports Azure DevOps Services at `dev.azure.com`. Azure DevOps Server is not supported.

## Supported features

Cloud Agents clone your code, work on branches, and open pull requests. Bugbot reviews pull requests and posts its findings as comments.

The following features don't support Azure DevOps yet:

- [Automations](https://cursor.com/docs/cloud-agent/automations.md)
- [Bugbot autofix](https://cursor.com/docs/bugbot.md#autofix)
- [Security Agents](https://cursor.com/docs/security-agents.md), including Security Reviewer and Vulnerability Scanner

These features work with [GitHub](https://cursor.com/docs/integrations/github.md) today. Azure DevOps support is on the roadmap.

## Setup

Requires access to the Azure DevOps organizations and repositories you want to use with Cursor.

1. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations)
2. Click **Connect** next to Azure DevOps
3. Sign in with the Microsoft account you use for Azure DevOps
4. Review the Microsoft Entra OAuth consent screen and approve access
5. Return to Cursor and select repositories from your Azure DevOps organizations
6. Configure Cloud Agents on the repositories you want Cursor to use

To disconnect your Azure DevOps account, return to the integrations dashboard and click **Disconnect Account**.

## Set up Bugbot

Bugbot on Azure DevOps is in limited availability. Setup needs a Microsoft Entra ID administrator to grant tenant admin consent, and we walk you through that step. [Contact us](https://cursor.com/contact-sales?source=docs-bugbot-azure-devops) to get started.

Bugbot reviews Azure DevOps pull requests under a Microsoft Entra service principal that Cursor provisions in your tenant. That service principal installs the service hooks Bugbot listens to, reads pull request diffs, and posts review comments and build statuses. Setup runs once per Azure DevOps organization, in this order:

1. A **Project Collection Administrator** connects Azure DevOps from [Integrations in the dashboard](https://cursor.com/dashboard/integrations) and turns Bugbot on for a repository in [Bugbot in Automations](https://cursor.com/automations/from-cursor/bugbot). This discovers your organization's Entra tenant and provisions the Cursor service principal automatically. Provisioning needs the one-time [Microsoft Entra admin consent](https://cursor.com/docs/integrations/azure-devops.md#grant-microsoft-entra-admin-consent).
2. A **project administrator** adds the Cursor service principal to the **Project Administrators** group of [each project you want reviewed](https://cursor.com/docs/integrations/azure-devops.md#add-the-service-principal-to-your-projects). Bugbot needs project administration to manage its service hooks.
3. Azure DevOps applies permission changes with a delay of some minutes. A toggle that fails right after a permission change can succeed unchanged a few minutes later.

When a step is missing, the repository toggle fails with an error that names the missing step. Fix it, then turn the repository on again.

Bugbot on Azure DevOps works on team repositories. Personal-scope repositories aren't supported.

### Grant Microsoft Entra admin consent

Before Cursor's service principal can exist in your directory, a Microsoft Entra ID administrator must grant tenant admin consent once. Consent requires the Global Administrator, Application Administrator, or Cloud Application Administrator role. It applies to the whole tenant, so a repository administrator alone can't complete it.

The enable error tells you when consent is missing. You can also build the consent link yourself:

```text
https://login.microsoftonline.com/{your-tenant-id}/v2.0/adminconsent?client_id=29df4809-337a-4255-bd57-d4a1476b0e65&redirect_uri=https://cursor.com/azure-devops-connected&scope=499b84ac-1321-427f-aa17-267ca6975798/.default%20offline_access%20openid%20profile
```

Replace `{your-tenant-id}` with your tenant ID from the [Microsoft Entra admin center](https://entra.microsoft.com). The `client_id` is Cursor's application ID. The `scope` covers the Azure DevOps API (`499b84ac-1321-427f-aa17-267ca6975798` is Microsoft's identifier for it) plus the standard sign-in scopes. Cursor asks for no Microsoft Graph data. Your tenant keeps the service principal, and you can revoke it in Entra at any time.

After your administrator consents, Microsoft returns them to `cursor.com/azure-devops-connected`, and the page confirms the grant. The grant lives in your tenant, so the next repository enable completes setup.

An earlier consent covers only the permissions Cursor requested at that time. If Cursor has added a permission since your tenant consented, setup fails partway, and reconnecting doesn't fix it. Open the consent link again to refresh the grant.

Azure DevOps organizations backed by a personal Microsoft account can't host the service principal. Connect the organization to Microsoft Entra ID first.

### Give the service principal access to your organization

After consent, Cursor adds the service principal to your Azure DevOps organization and requests a Basic access level for it. Both happen automatically, using the administrator account that connected Azure DevOps. The service principal then appears under **Organization settings** → **Users**.

Two things can stop that:

- **The connected account can't add users to the organization.** Reconnect Azure DevOps as an administrator of the organization.
- **No Basic access level is available.** Free a Basic seat, or assign one to the service principal under **Organization settings** → **Users**.

### Add the service principal to your projects

Service hooks are how Azure DevOps notifies Bugbot about pull requests, and only project administrators can manage them. Add the Cursor service principal to the **Project Administrators** group of each project you want reviewed, under **Project settings** → **Permissions**. Repository read access is not enough.

Permission changes can take a few minutes to apply, so a toggle that fails right after the grant can succeed unchanged a few minutes later.

### Enable Bugbot on repositories

1. Open [Bugbot in Automations](https://cursor.com/automations/from-cursor/bugbot)
2. Find your Azure DevOps repositories in the installations list
3. Turn Bugbot on for each repository you want reviewed

Bugbot installs its service hooks when you turn a repository on, and removes them when you turn it off. Turning Bugbot off for a repository, or disconnecting Azure DevOps, stops reviews for that repository right away.

### How reviews are triggered

Bugbot reviews each pull request as it opens and updates. Someone can also ask for a review on demand by commenting `cursor review` or `bugbot run`.

Comment triggers have one Azure DevOps limit. They work for people whose Azure DevOps sign-in address matches a Cursor account in the team that owns the repository. A comment from anyone else doesn't start a review. Automatic reviews carry no such limit, and they cover every author.

### Filter which authors get reviewed

Bugbot reviews every author by default. To narrow that, turn off **Run for All Authors** in the repository's Bugbot settings, then pick **Only Review PRs by...** or **Skip PRs by...**.

That list takes **Azure DevOps sign-in addresses**, not usernames, and the field is labeled that way. A sign-in address looks like `taylor@contoso.com`, and it's the value your organization administrator reads under **Organization settings** → **Users**. A username matches nobody, so Bugbot stays quiet for that author.

### Differences from other providers

Repository settings and repository rules work on Azure DevOps. These don't:

- **Auto-Enable for New Repositories.** Turn Bugbot on for each new repository yourself.
- **Automatically Learn Rules.** Repository rules you write by hand still apply.
- **Personal Bugbot settings.** Repository settings apply to everyone instead.
- **Autofix.** Bugbot reports its findings without opening fix commits.

### Build statuses and branch policies

Bugbot posts a build status on each reviewed pull request under the context `cursor-bugbot/review`. See [CI check statuses](https://cursor.com/docs/bugbot.md#ci-check-statuses) for what each conclusion means.

If you make that context a required status branch policy, set the policy's **Reset conditions** to **Reset status whenever there are new changes**. Without it, a status from an earlier push keeps satisfying the policy after new commits land.

### Migrating from the earlier Bugbot setup

Organizations that enabled Bugbot for Azure DevOps before August 2026 used an earlier per-repository setup. A repository still on that setup shows "This Azure DevOps repository still uses the earlier Bugbot setup." when you turn it on.

Migration is automatic. Connect Azure DevOps as an administrator of the organization, then turn the repository on again in [Bugbot in Automations](https://cursor.com/automations/from-cursor/bugbot). Cursor removes the earlier service hooks and completes the new setup in one step.

If Cursor reports it could not remove the earlier setup, remove it yourself:

1. In Azure DevOps, open **Project settings** → **Service hooks**
2. Delete the Cursor **Web Hooks** subscriptions that deliver to `https://api2.cursor.sh/azure_devops_webhook`
3. Turn the repository on again in [Bugbot in Automations](https://cursor.com/automations/from-cursor/bugbot)

The new setup prerequisites apply after migration. Your tenant needs the one-time [Microsoft Entra admin consent](https://cursor.com/docs/integrations/azure-devops.md#grant-microsoft-entra-admin-consent), and the service principal needs [a Basic access level in your organization](https://cursor.com/docs/integrations/azure-devops.md#give-the-service-principal-access-to-your-organization) and membership in [each project's Project Administrators group](https://cursor.com/docs/integrations/azure-devops.md#add-the-service-principal-to-your-projects).

## Repository URLs

Cursor supports Azure DevOps Services repository URLs in this format:

```text
https://dev.azure.com/{organization}/{project}/_git/{repository}
```

Azure DevOps uses an organization, project, and repository hierarchy. Cursor shows repositories as `{project}/{repository}` under the Azure DevOps organization.

If your organization still uses a `*.visualstudio.com` URL, open the repository in Azure DevOps and copy the `dev.azure.com` URL before adding it to Cursor.

## Permissions

Cursor connects to Azure DevOps through Microsoft Entra OAuth. The connection lets Cursor:

| Access                         | Purpose                                                                        |
| ------------------------------ | ------------------------------------------------------------------------------ |
| **Organizations and projects** | List the Azure DevOps organizations, projects, and repositories you can access |
| **Code repositories**          | Clone repositories and create working branches                                 |
| **Pull requests**              | Open, update, and merge pull requests created by Cloud Agents                  |

Bugbot adds a second identity. Cursor provisions a Microsoft Entra service principal in your tenant and uses it for every Bugbot action, so reviews keep running when the person who set the integration up changes roles or leaves.

| Action                                                                     | Azure DevOps identity           |
| -------------------------------------------------------------------------- | ------------------------------- |
| Bugbot review comments, inline comments, and build statuses                | Cursor service principal        |
| Bugbot service hook installation and removal                               | Cursor service principal        |
| Git clone, branch push, commits, and pull request creation by Cloud Agents | The connected Azure DevOps user |

## Troubleshooting

### I don't see my Azure DevOps repository

- Confirm the repository is hosted on Azure DevOps Services at `dev.azure.com`.
- Confirm the Microsoft account you connected has access to the organization, project, and repository.
- Reconnect Azure DevOps from the integrations dashboard if your Microsoft access changed.

### Cloud Agent can't open a pull request

- Confirm the selected Azure DevOps repository is connected in Cursor.
- Check that your Azure DevOps account can create branches and pull requests in the target repository.
- Check branch policies if the target branch blocks pull request creation or updates.

### Repository URL is rejected

Use the `dev.azure.com` repository URL from Azure DevOps. Cursor does not accept Azure DevOps Server URLs for this integration.

### Bugbot doesn't review my pull requests

- Confirm the repository is turned on in [Bugbot in Automations](https://cursor.com/automations/from-cursor/bugbot).
- Confirm the repository belongs to a Cursor team. Bugbot on Azure DevOps doesn't review personal-scope repositories.
- Confirm the Cursor service principal is in the project's **Project Administrators** group under **Project settings** → **Permissions**.
- If you filter authors, confirm the pull request author is listed by Azure DevOps sign-in address rather than username.

### Commenting on a pull request doesn't trigger a review

A comment trigger works only when your Azure DevOps sign-in address matches a Cursor account in the team that owns the repository. Two addresses that belong to the same person still count as two people here.

Check the sign-in address on your Azure DevOps profile against the email on your Cursor account, and have a team admin invite that address if it's missing. Automatic reviews keep running either way.

### Bugbot ignores my personal settings

Personal Bugbot settings don't apply to Azure DevOps repositories yet. Repository settings do. Set the behavior you want at the repository level in [Bugbot in Automations](https://cursor.com/automations/from-cursor/bugbot).

### A required Bugbot status stays green after a new push

Open the branch policy for the `cursor-bugbot/review` status and set **Reset conditions** to **Reset status whenever there are new changes**. Azure DevOps keeps the earlier status otherwise, so the policy passes on commits Bugbot hasn't reviewed.

## Next steps

Once your Azure DevOps integration is connected, configure the features that use it:

- [Bugbot](https://cursor.com/docs/bugbot.md) - automated PR reviews that catch bugs and security issues
- [Cloud Agents](https://cursor.com/docs/cloud-agent.md) - AI agents that run in the cloud on your repositories
- [Cloud Agent setup](https://cursor.com/docs/cloud-agent/setup.md) - saved environments, multi-repo setup, secrets, and Dockerfiles


---

## Sitemap

[Overview of all docs pages](/llms.txt)
