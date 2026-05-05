---
source_url: https://cursor.com/docs/integrations/github
---

# GitHub

The Cursor GitHub app connects your repositories so you can use features like [Cloud Agents](https://cursor.com/docs/cloud-agent.md) and [Bugbot](https://cursor.com/docs/bugbot.md).

## Setup

### GitHub.com

Requires Cursor admin access and GitHub org admin access.

1. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations)
2. Click **Connect** next to GitHub (or **Manage Connections** if already connected)
3. Choose **All repositories** or **Selected repositories**
4. Return to the dashboard to configure features on your repositories

[GitHub setup](/docs-static/images/bugbot/bugbot-install.mp4)

To disconnect your GitHub account, return to the integrations dashboard and click **Disconnect Account**.

### GitHub Enterprise Server

### Prerequisites

- Running a supported version of GitHub Enterprise Server (v3.8 or later recommended)
- Admin privileges on your GHES instance

### Networking

GHES requires secure inbound access from Cursor and outbound access for webhook notifications.

#### IP whitelisting (recommended)

Add these IP addresses to your allowlist:

```text
184.73.225.134
3.209.66.12
52.44.113.131
```

For other connection options beyond IP whitelisting, see [Advanced networking](https://cursor.com/docs/integrations/github.md#advanced-networking).

### Register the Cursor Enterprise App

1. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations) → **Advanced** → **GitHub Enterprise Server**
2. Enter the **base URL** of your GHES instance (e.g., `https://git.yourcompany.com`)
3. Enter the name of the **Organization** that will own the application
   - This should be your company's Organization inside your GHES installation
   - You need administrator privileges for this Organization
   - Other Organizations can access the app once registered
   - Leave blank to use your user account (not recommended)
4. Click **Register**
5. Choose a name for the Cursor Enterprise Application (default recommended)
6. The app will appear under your available GitHub Apps in your GHES instance
7. Return to the dashboard to configure features on your repositories

## IP allow list configuration

If your organization uses GitHub's IP allow list feature to restrict access to your repositories, Cursor can be configured to use a hosted egress proxy with a narrow set of IPs.

Before configuring IP allowlists, contact [hi@cursor.com](mailto:hi@cursor.com) to enable this feature for your team. This is required for either configuration method below.

### Enable IP allow list configuration for installed GitHub Apps (recommended)

The Cursor GitHub app has the IP list already pre-configured. You can enable the allowlist for installed apps to automatically inherit this list. This is the **recommended approach**, as it allows us to update the list and your organization receives updates automatically.

To enable this:

1. Go to your organization's Security settings
2. Navigate to IP allow list settings
3. Check **"Allow access by GitHub Apps"**

For detailed instructions, see [GitHub's documentation](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps).

### Add IPs directly to your allowlist

If your organization uses IdP-defined allowlists in GitHub or otherwise cannot use the pre-configured allowlist, add the proxy IPs listed in [Git egress proxy and IP allow list](https://cursor.com/docs/cloud-agent/security-network.md#git-egress-proxy-and-ip-allow-list).

## Advanced networking

Self-hosted instances support multiple connection methods beyond IP whitelisting.

### PrivateLink (AWS) or Private Service Connect (GCP)

Available for Enterprise customers. Allow Cursor to access your instance over a private network connection. [Contact your Cursor representative](https://cursor.com/contact-sales?source=docs-bugbot-private-network) for setup.

**Best for:** Instances behind a firewall on a private network in AWS, Azure, or GCP

**Security:** HTTPS encryption with optional mTLS, PrivateLink/Service Connect, VPC allowlisting, service account access tokens

**Drawbacks:** Only supports public clouds with private networking connections between VPCs

### Reverse Proxy Tunnel

Available for Enterprise customers. Run a reverse proxy tunnel on-premises that establishes a long-lived websocket connection to Cursor's servers. Network requests are forwarded through to your instance. Requires no inbound network access. [Contact your Cursor representative](https://cursor.com/contact-sales?source=docs-bugbot-on-prem-proxy) for setup.

**Best for:** Environments without inbound network access

**Security:** HTTPS encryption, service account access tokens

**Drawbacks:** Introduces additional complexity, maintenance requirements, and potential security considerations compared to more direct connection methods

## Permissions

The GitHub app requests the following permissions to support Cursor features:

| Permission                | Purpose                                        |
| ------------------------- | ---------------------------------------------- |
| **Repository access**     | Clone your code and create working branches    |
| **Pull requests**         | Create PRs and leave review comments           |
| **Issues**                | Track bugs and tasks discovered during reviews |
| **Checks and statuses**   | Report on code quality and test results        |
| **Actions and workflows** | Monitor CI/CD pipelines and deployment status  |

All permissions follow the principle of least privilege.

## Troubleshooting

### Agent can't access repository

- Install the GitHub app with repository access
- Check repository permissions for private repos
- Verify your GitHub account permissions

### Permission denied for pull requests

- Grant the app write access to pull requests
- Check branch protection rules
- Reinstall if the app installation expired

### App not visible in GitHub settings

- Check if installed at organization level
- Reinstall from [github.com/apps/cursor](https://github.com/apps/cursor)
- Contact support if installation is corrupted

## Next steps

Once your GitHub integration is connected, configure the features that use it:

- [Bugbot](https://cursor.com/docs/bugbot.md) — automated PR reviews that catch bugs and security issues
- [Cloud Agents](https://cursor.com/docs/cloud-agent.md) — AI agents that run in the cloud on your repositories


---

## Sitemap

[Overview of all docs pages](/llms.txt)
