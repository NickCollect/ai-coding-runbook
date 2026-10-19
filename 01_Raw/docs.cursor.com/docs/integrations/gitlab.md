---
source_url: https://cursor.com/docs/integrations/gitlab
fetched_at: 2026-10-19T05:32:44.648166+00:00
fetch_method: mintlify_md
---

# GitLab

The GitLab integration connects your repositories so you can use features like [Cloud Agents](https://cursor.com/docs/cloud-agent.md) and [Bugbot](https://cursor.com/docs/bugbot.md).

## Setup

### GitLab.com

Requires Cursor admin access and GitLab maintainer access.

GitLab integration requires a **paid GitLab plan** (Premium or Ultimate). Project access tokens, which are required for this integration, are not available on GitLab Free.

1. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations)
2. Click **Connect** next to GitLab (or **Manage Connections** if already connected)
3. Follow the GitLab installation flow
4. Back on the Integrations tab, click **Manage** next to your GitLab connection and select **Sync Repos**
5. Return to the dashboard to configure features on your repositories

[GitLab setup](/docs-static/images/bugbot/bugbot-gitlab.mp4)

To disconnect your GitLab account, return to the integrations dashboard and click **Disconnect Account**.

### GitLab Self-Hosted

GitLab integration requires a **paid GitLab plan** (Premium or Ultimate). Project access tokens, which are required for this integration, are not available on GitLab Free.

GitLab Self-Hosted requires a [Teams](https://cursor.com/docs/account/teams/pricing.md) or [Enterprise](https://cursor.com/docs/enterprise.md) plan.

### Networking

- GitLab self-hosted requires secure inbound access from Cursor and outbound access for webhook notifications.
- Your instance's OAuth token endpoint (`/oauth/token`) and token check (`/api/v4/personal_access_tokens/self`) can redirect only within the same scheme, host, and port, for up to 5 redirects. Cursor refuses any other redirect, and the request fails.
- You need admin privileges on your GitLab instance to create the application.

#### IP whitelisting (recommended)

Add these IP addresses to your allowlist:

```text
184.73.225.134
3.209.66.12
52.44.113.131
100.63.97.141
100.63.144.57
18.210.232.136
3.208.51.163
3.224.130.48
3.234.118.132
34.197.19.148
34.198.251.120
34.199.187.247
35.170.160.152
44.215.226.85
52.202.172.69
54.81.109.217
54.204.61.44
54.236.99.119
67.202.63.191
184.193.125.229
184.193.223.40
184.194.140.210
184.194.175.144
184.194.208.56
```

For other connection options beyond IP whitelisting, see [Advanced networking](https://cursor.com/docs/integrations/gitlab.md#advanced-networking).

### Create GitLab application

1. In your GitLab instance, create a new application (Instance level preferred)
2. Set the redirect URI to `https://cursor.com/gitlab-connected`
3. Configure the application:
   - **Trusted**: `true`
   - **Confidential**: `true`
   - **Scopes**: `api` and `write_repository`
4. After creation, you'll receive an **Application ID** and **Secret**

### Register with Cursor

1. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations) → **Advanced** → **GitLab Self-Hosted**
2. Enter your GitLab instance **hostname**
3. Paste the **Application ID** and **Secret**
4. Click **Register**
5. Select your GitLab instance from the dropdown
6. Click **Connect** to complete the installation
7. Back on the Integrations tab, click **Manage** next to your GitLab connection and select **Sync Repos**
8. Return to the dashboard to configure features on your repositories

### Disconnect GitLab Self-Hosted

Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations) → **Advanced** → **GitLab Self-Hosted**, open the registered instance's menu, and select **Delete Instance**. Cursor removes the instance's OAuth credentials, webhook secret, service account and user tokens, and the webhooks it created. Bugbot repository settings, team Bugbot settings, and learned rules are kept and return if you set up the same hostname again.

## Advanced networking

Self-hosted instances support multiple connection methods beyond IP whitelisting. For setup details and supported private networking options, see [Private Connectivity](https://cursor.com/docs/cloud-agent/private-connectivity.md).

### AWS PrivateLink

Available for Enterprise customers. Use AWS PrivateLink when your GitLab instance is in AWS or can sit behind an AWS Network Load Balancer. PrivateLink can cover Cursor accessing GitLab and, when needed, GitLab sending webhooks back to Cursor without public internet egress.

**Best for:** AWS-hosted GitLab instances and teams that want private VPC endpoint connectivity

**Security:** HTTPS encryption, AWS PrivateLink, VPC endpoint policies, service account access tokens

**Drawbacks:** Requires coordination with Cursor and AWS endpoint service setup.

### Cloudflare Tunnel

Available for Enterprise customers. Use Cloudflare Tunnel when AWS PrivateLink is not practical or when you need an outbound-only deployment model. Cursor creates and owns the tunnel, and provides the hostname and token. You run `cloudflared` outbound from your network. You do not need a Cloudflare account or contract.

**Best for:** Environments without inbound network access

**Security:** HTTPS encryption, Cloudflare Tunnel, service account access tokens

**Drawbacks:** Requires running and maintaining `cloudflared` in your environment.

## Protected Git Scopes

Lock your GitLab group or namespace to your Cursor organization so only your teams can use its repositories with Cloud Agents, automations, and Bugbot. Protecting a scope requires the GitLab Owner role. See [Protected Git Scopes](https://cursor.com/docs/enterprise/model-and-integration-management.md#protected-git-scopes).

## Next steps

Once your GitLab integration is connected, configure the features that use it:

- [Bugbot](https://cursor.com/docs/bugbot.md) — automated PR reviews that catch bugs and security issues
- [Cloud Agents](https://cursor.com/docs/cloud-agent.md) — AI agents that run in the cloud on your repositories


---

## Sitemap

[Overview of all docs pages](/llms.txt)
