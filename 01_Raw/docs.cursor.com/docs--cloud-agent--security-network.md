---
source_url: https://cursor.com/docs/cloud-agent/security-network
---

# Security & Network

Cloud Agents are available in Privacy Mode. We never train on your code and only retain code for running the agent. [Learn more about Privacy mode](https://www.cursor.com/privacy-overview).

## Secret protection

Secrets provided to Cloud Agents are encrypted at rest and in transit. They are not visible to anyone other than the Cloud Agent user.

You can classify secrets as "Redacted" for additional protection. Redacted secrets:

- Are scanned in commit messages and files, which are rejected if they contain the secret
- Are redacted from model tool calls, so they are not shown to the models or stored in chat transcripts

This prevents accidental exposure of credentials in version control and model context.

## Signed commits

Cloud Agents sign every commit with a HSM-backed Ed25519 key. On GitHub and GitLab, these commits display a "Verified" badge so your team can confirm the commit came from Cursor.

This works automatically for all Cloud Agents. No setup is required.

If your repository enforces branch protection rules that require signed commits, Cloud Agent PRs satisfy those rules without extra configuration.

## What you should know

1. Grant read-write privileges to our GitHub app for repos you want to edit. We use this to clone the repo and make changes.
2. Your code runs inside our AWS infrastructure in isolated VMs and is stored on VM disks while the agent is accessible.
3. The agent has internet access by default. You can configure [network egress controls](https://cursor.com/docs/cloud-agent/security-network.md#network-access) to restrict the domains the agent can access.
4. The agent auto-runs all terminal commands, letting it iterate on tests. This differs from the foreground agent, which requires user approval for every command. Auto-running introduces data exfiltration risk: attackers could execute prompt injection attacks, tricking the agent to upload code to malicious websites. See [OpenAI's explanation about risks of prompt injection for cloud agents](https://platform.openai.com/docs/codex/agent-network#risks-of-agent-internet-access).
5. If privacy mode is disabled, we collect prompts and dev environments to improve the product.
6. If you disable privacy mode when starting a cloud agent, then enable it during the agent's run, the agent continues with privacy mode disabled until it completes.

## Network access

Control which network resources your Cloud Agents can reach. These settings are available on the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents) for individual users and team admins.

### Access modes

Three modes control outbound network access for Cloud Agents:

| Mode                         | Behavior                                                                                                                                                            |
| :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Allow all network access** | Cloud Agents can reach any external host. No domain restrictions apply.                                                                                             |
| **Default + allowlist**      | Cloud Agents can reach the [default domains](https://cursor.com/docs/agent/tools/terminal.md#default-network-allowlist) plus any domains you add to your allowlist. |
| **Allowlist only**           | Cloud Agents can only reach the domains you explicitly add to your allowlist.                                                                                       |

Even in **Allowlist only** mode, a small set of domains remain accessible so Cloud Agents can function. These include Cursor's own services and source control management (SCM) providers.

### Artifact uploads

Cloud Agents upload [artifacts](https://cursor.com/docs/cloud-agent/capabilities.md#demos-and-artifacts) (screenshots, videos, and log references shown on PRs) to `cloud-agent-artifacts.s3.us-east-1.amazonaws.com`.

If you use **Default + allowlist** or **Allowlist only**, add the exact host to your allowlist so artifact uploads succeed. Don't broaden the entry to `*.s3.us-east-1.amazonaws.com`: the wildcard opens egress to every bucket in the region and creates an exfiltration path for a prompt-injected agent. Blocking the host disables uploads; agent sessions and other tool calls keep working.

Self-hosted workers upload artifacts over the same host. For self-hosted deployments, allow it through any firewall between the worker and the public internet. See [My Machines networking](https://cursor.com/docs/cloud-agent/my-machines.md#networking) and [Self-Hosted Pool networking](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#networking).

### User-level settings

Individual users can configure their network access mode from the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents) under the **Security** header. Your user-level setting applies to all Cloud Agents you create.

When you select a mode that includes an allowlist (**Default + allowlist** or **Allowlist only**), an allowlist configuration section appears below the setting where you can add your custom domains.

### Team-level settings

Team admins can set a default network access mode for the entire team from the same dashboard. The team-level allowlist is the same allowlist that admins configure for the [sandbox default network allowlist](https://cursor.com/docs/agent/tools/terminal.md#default-network-allowlist). There is no separate allowlist to manage; one allowlist controls both Cloud Agent network access and the sandbox defaults.

When a team-level setting exists:

- If a user has configured their own setting, the **user setting takes precedence**.
- If a user has not configured a setting, the **team default applies**.

### Locking the setting (Enterprise)

Locking is available for Enterprise teams only.

Enterprise team admins can lock the network access setting using the **Lock Network Access Policy** option. When locked:

- The team-level setting applies to every member, regardless of their individual preference.
- Users cannot override the locked setting from their own dashboard.

This gives admins full control over Cloud Agent network access across the organization.

### Relationship to sandbox network policy

The "Default" domains in the **Default + allowlist** mode are the same [default network allowlist](https://cursor.com/docs/agent/tools/terminal.md#default-network-allowlist) used by the desktop Agent's sandbox. The team-level allowlist is also shared: when an admin configures an allowlist on the dashboard, it applies to both Cloud Agent network access and the [sandbox network policy](https://cursor.com/docs/reference/sandbox.md).

## Egress IP ranges

Cloud Agents make network connections from specific IP address ranges when accessing external services, APIs, or repositories.

### API endpoint

The IP ranges are available via a [JSON API endpoint](https://cursor.com/docs/ips.json):

```bash
curl https://cursor.com/docs/ips.json
```

#### Response format

```json
{
  "version": 1,
  "modified": "2025-09-24T16:00:00.000Z",
  "cloudAgents": {
    "us3p": ["100.26.13.169/32", "34.195.201.10/32", "..."],
    "us4p": ["54.184.235.255/32", "35.167.37.158/32", "..."],
    "us5p": ["3.12.82.200/32", "52.14.104.140/32", "..."]
  },
  "gitEgressProxy": ["184.73.225.134/32", "3.209.66.12/32", "52.44.113.131/32"]
}
```

- **version**: Schema version number for the API response
- **modified**: ISO 8601 timestamp of when the IP ranges were last updated
- **cloudAgents**: Object containing IP ranges, keyed by cluster
- **gitEgressProxy**: IP addresses used by the [git egress proxy](https://cursor.com/docs/cloud-agent/security-network.md#git-egress-proxy-and-ip-allow-list)

IP ranges published in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing). You can use an online conversion tool to convert from CIDR notation to IP address ranges if needed.

### Using the IP ranges

These published IP ranges may be used by Cloud Agents to:

- Clone and push to remote repositories (unless using the [git egress proxy](https://cursor.com/docs/integrations/github.md#ip-allow-list-configuration))
- Download packages and dependencies
- Make API calls to external services
- Access web resources during agent execution

If your organization uses firewall rules or IP allowlists to control network access, you may need to allowlist these IP ranges to ensure Cloud Agents can properly access your services.

**Important considerations:**

- We make changes to our IP addresses from time to time for scaling and operational needs.
- We do not recommend allowlisting by IP address as your primary security mechanism.
- If you must use these IP ranges, we strongly encourage regular monitoring of the JSON API endpoint.

### Git egress proxy and IP allow list

Cursor supports a similar but distinct feature to [use a git egress proxy for IP allow lists](https://cursor.com/docs/integrations/github.md#ip-allow-list-configuration). This proxy routes all git traffic through a narrower set of IPs and works across all git hosts, including GitHub and GitLab.

For git hosts specifically, we recommend the IP allow list configuration described in the link above, as it integrates directly with the Cursor GitHub app.

If you need to add the proxy IPs directly to an allowlist, use these addresses:

```text
184.73.225.134
3.209.66.12
52.44.113.131
```

These IP addresses are stable. If the list ever changes, teams using IP allow
lists will get advance notice before any address is added or removed.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
