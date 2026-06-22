---
source_url: https://cursor.com/docs/integrations/azure-devops
fetched_at: 2026-06-22T06:23:25.433023+00:00
fetch_method: mintlify_md
---

# Azure DevOps

The Azure DevOps integration connects Azure DevOps Services repositories so Cursor can clone your code, work on branches, and open pull requests from [Cloud Agents](https://cursor.com/docs/cloud-agent.md).

The Azure DevOps integration is in public beta. It supports Azure DevOps Services at `dev.azure.com`. Azure DevOps Server is not supported.

## Setup

Requires access to the Azure DevOps organizations and repositories you want to use with Cursor.

1. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations)
2. Click **Connect** next to Azure DevOps
3. Sign in with the Microsoft account you use for Azure DevOps
4. Review the Microsoft Entra OAuth consent screen and approve access
5. Return to Cursor and select repositories from your Azure DevOps organizations
6. Configure Cloud Agents on the repositories you want Cursor to use

To disconnect your Azure DevOps account, return to the integrations dashboard and click **Disconnect Account**.

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

## Next steps

Once your Azure DevOps integration is connected, configure the features that use it:

- [Cloud Agents](https://cursor.com/docs/cloud-agent.md) - AI agents that run in the cloud on your repositories
- [Cloud Agent setup](https://cursor.com/docs/cloud-agent/setup.md) - saved environments, multi-repo setup, secrets, and Dockerfiles


---

## Sitemap

[Overview of all docs pages](/llms.txt)
