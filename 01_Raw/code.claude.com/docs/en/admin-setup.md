---
source_url: https://code.claude.com/docs/en/admin-setup
fetched_at: 2026-05-04T15:03:17.180777+00:00
fetch_method: mintlify_md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up Claude Code for your organization

> A decision map for administrators deploying Claude Code, covering API providers, managed settings, policy enforcement, usage monitoring, and data handling.

Claude Code enforces organization policy through managed settings that take precedence over local developer configuration. You deliver those settings from the Claude admin console, your mobile device management (MDM) system, or a file on disk. The settings control which tools, commands, servers, and network destinations Claude can reach.

This page walks through the deployment decisions in order. Each row links to the section below and to the reference page for that area.

<Note>
  SSO, SCIM provisioning, and seat assignment are configured at the Claude account level. See the [Claude Enterprise Administrator Guide](https://code.claude.com/docs/en/Claude Enterprise Administrator Guide) and [seat assignment](https://code.claude.com/docs/en/seat assignment) for those steps.
</Note>

| Decision                                                                | What you're choosing                                | Reference                                                                                                                                |
| :---------------------------------------------------------------------- | :-------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| [Choose your API provider](https://code.claude.com/docs/en/Choose your API provider)                   | Where Claude Code authenticates and how it's billed | [Authentication](https://code.claude.com/docs/en/Authentication), [Bedrock](https://code.claude.com/docs/en/Bedrock), [Vertex AI](https://code.claude.com/docs/en/Vertex AI), [Foundry](https://code.claude.com/docs/en/Foundry) |
| [Decide how settings reach devices](https://code.claude.com/docs/en/Decide how settings reach devices) | How managed policy reaches developer machines       | [Server-managed settings](https://code.claude.com/docs/en/Server-managed settings), [Settings files](https://code.claude.com/docs/en/Settings files)                                    |
| [Decide what to enforce](https://code.claude.com/docs/en/Decide what to enforce)                       | Which tools, commands, and integrations are allowed | [Permissions](https://code.claude.com/docs/en/Permissions), [Sandboxing](https://code.claude.com/docs/en/Sandboxing)                                                                             |
| [Set up usage visibility](https://code.claude.com/docs/en/Set up usage visibility)                     | How you track spend and adoption                    | [Analytics](https://code.claude.com/docs/en/Analytics), [Monitoring](https://code.claude.com/docs/en/Monitoring), [Costs](https://code.claude.com/docs/en/Costs)                                                       |
| [Review data handling](https://code.claude.com/docs/en/Review data handling)                           | Data retention and compliance posture               | [Data usage](https://code.claude.com/docs/en/Data usage), [Security](https://code.claude.com/docs/en/Security)                                                                                   |

## Choose your API provider

Claude Code connects to Claude through one of several API providers. Your choice affects billing, authentication, and which compliance posture you inherit.

| Provider                      | Choose this when                                                                                                                      |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| Claude for Teams / Enterprise | You want Claude Code and claude.ai under one per-seat subscription with no infrastructure to run. This is the default recommendation. |
| Claude Console                | You're API-first or want pay-as-you-go billing                                                                                        |
| Amazon Bedrock                | You want to inherit existing AWS compliance controls and billing                                                                      |
| Google Vertex AI              | You want to inherit existing GCP compliance controls and billing                                                                      |
| Microsoft Foundry             | You want to inherit existing Azure compliance controls and billing                                                                    |

For the full provider comparison covering authentication, regions, and feature parity, see the [enterprise deployment overview](https://code.claude.com/docs/en/enterprise deployment overview). Each provider's auth setup is in [Authentication](https://code.claude.com/docs/en/Authentication).

Proxy and firewall requirements in [Network configuration](https://code.claude.com/docs/en/Network configuration) apply regardless of provider. If you want a single endpoint in front of multiple providers or centralized request logging, see [LLM gateway](https://code.claude.com/docs/en/LLM gateway).

## Decide how settings reach devices

Managed settings define policy that takes precedence over local developer configuration. Claude Code looks for them in four places and uses the first one it finds on a given device.

| Mechanism               | Delivery                                                                                                                                                                                              | Priority | Platforms      |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- | :------------- |
| Server-managed          | Claude.ai admin console                                                                                                                                                                               | Highest  | All            |
| plist / registry policy | macOS: `com.anthropic.claudecode` plist<br />Windows: `HKLM\SOFTWARE\Policies\ClaudeCode`                                                                                                             | High     | macOS, Windows |
| File-based managed      | macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`<br />Linux and WSL: `/etc/claude-code/managed-settings.json`<br />Windows: `C:\Program Files\ClaudeCode\managed-settings.json` | Medium   | All            |
| Windows user registry   | `HKCU\SOFTWARE\Policies\ClaudeCode`                                                                                                                                                                   | Lowest   | Windows only   |

Server-managed settings reach devices at authentication time and refresh hourly during active sessions, with no endpoint infrastructure. They require a Claude for Teams or Enterprise plan, so deployments on other providers need one of the file-based or OS-level mechanisms instead.

If your organization mixes providers, configure [server-managed settings](https://code.claude.com/docs/en/server-managed settings) for Claude.ai users plus a [file-based or plist/registry fallback](https://code.claude.com/docs/en/file-based or plist/registry fallback) so other users still receive managed policy.

The plist and HKLM registry locations work with any provider and resist tampering because they require admin privileges to write. The Windows user registry at HKCU is writable without elevation, so treat it as a convenience default rather than an enforcement channel.

By default WSL reads only the Linux file path at `/etc/claude-code`. To extend your Windows registry and `C:\Program Files\ClaudeCode` policy to WSL on the same machine, set [`wslInheritsWindowsSettings: true`](https://code.claude.com/docs/en/`wslInheritsWindowsSettings: true`) in either of those admin-only Windows sources.

Whichever mechanism you choose, managed values take precedence over user and project settings. Array settings such as `permissions.allow` and `permissions.deny` merge entries from all sources, so developers can extend managed lists but not remove from them.

See [Server-managed settings](https://code.claude.com/docs/en/Server-managed settings) and [Settings files and precedence](https://code.claude.com/docs/en/Settings files and precedence).

## Decide what to enforce

Managed settings can lock down tools, sandbox execution, restrict MCP servers and plugin sources, and control which hooks run. Each row is a control surface with the setting keys that drive it.

| Control                                                                                | What it does                                                                  | Key settings                                                                  |
| :------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| [Permission rules](https://code.claude.com/docs/en/Permission rules)                                                    | Allow, ask, or deny specific tools and commands                               | `permissions.allow`, `permissions.deny`                                       |
| [Permission lockdown](https://code.claude.com/docs/en/Permission lockdown)                           | Only managed permission rules apply; disable `--dangerously-skip-permissions` | `allowManagedPermissionRulesOnly`, `permissions.disableBypassPermissionsMode` |
| [Sandboxing](https://code.claude.com/docs/en/Sandboxing)                                                           | OS-level filesystem and network isolation with domain allowlists              | `sandbox.enabled`, `sandbox.network.allowedDomains`                           |
| [Managed policy CLAUDE.md](https://code.claude.com/docs/en/Managed policy CLAUDE.md)              | Org-wide instructions loaded in every session, cannot be excluded             | File at the managed policy path                                               |
| [MCP server control](https://code.claude.com/docs/en/MCP server control)                                | Restrict which MCP servers users can add or connect to                        | `allowedMcpServers`, `deniedMcpServers`, `allowManagedMcpServersOnly`         |
| [Plugin marketplace control](https://code.claude.com/docs/en/Plugin marketplace control) | Restrict which marketplace sources users can add and install from             | `strictKnownMarketplaces`, `blockedMarketplaces`                              |
| [Hook restrictions](https://code.claude.com/docs/en/Hook restrictions)                                   | Only managed hooks load; restrict HTTP hook URLs                              | `allowManagedHooksOnly`, `allowedHttpHookUrls`                                |
| [Version floor](https://code.claude.com/docs/en/Version floor)                                                          | Prevent auto-update from installing below an org-wide minimum                 | `minimumVersion`                                                              |

Permission rules and sandboxing cover different layers. Denying WebFetch blocks Claude's fetch tool, but if Bash is allowed, `curl` and `wget` can still reach any URL. Sandboxing closes that gap with a network domain allowlist enforced at the OS level.

For the threat model these controls defend against, see [Security](https://code.claude.com/docs/en/Security).

## Set up usage visibility

Choose monitoring based on what you need to report on.

| Capability          | What you get                                         | Availability   | Where to start                           |
| :------------------ | :--------------------------------------------------- | :------------- | :--------------------------------------- |
| Usage monitoring    | OpenTelemetry export of sessions, tools, and tokens  | All providers  | [Monitoring usage](https://code.claude.com/docs/en/Monitoring usage) |
| Analytics dashboard | Per-user metrics, contribution tracking, leaderboard | Anthropic only | [Analytics](https://code.claude.com/docs/en/Analytics)               |
| Cost tracking       | Spend limits, rate limits, and usage attribution     | Anthropic only | [Costs](https://code.claude.com/docs/en/Costs)                       |

Cloud providers expose spend through AWS Cost Explorer, GCP Billing, or Azure Cost Management. Claude for Teams and Enterprise plans include a usage dashboard at [claude.ai/analytics/claude-code](https://code.claude.com/docs/en/claude.ai/analytics/claude-code).

## Review data handling

On Team, Enterprise, Claude API, and cloud provider plans, Anthropic does not train models on your code or prompts. Your API provider determines retention and compliance posture.

| Topic                     | What to know                                                                    | Where to start                                 |
| :------------------------ | :------------------------------------------------------------------------------ | :--------------------------------------------- |
| Data usage policy         | What Anthropic collects, how long it's retained, what's never used for training | [Data usage](https://code.claude.com/docs/en/Data usage)                   |
| Zero Data Retention (ZDR) | Nothing stored after the request completes. Available on Claude for Enterprise  | [Zero data retention](https://code.claude.com/docs/en/Zero data retention) |
| Security architecture     | Network model, encryption, authentication, audit trail                          | [Security](https://code.claude.com/docs/en/Security)                       |

If you need request-level audit logging or to route traffic by data sensitivity, place an [LLM gateway](https://code.claude.com/docs/en/LLM gateway) between developers and your provider. For regulatory requirements and certifications, see [Legal and compliance](https://code.claude.com/docs/en/Legal and compliance).

## Verify and onboard

After configuring managed settings, have a developer run `/status` inside Claude Code. The output includes a line beginning with `Enterprise managed settings` followed by the source in parentheses, one of `(remote)`, `(plist)`, `(HKLM)`, `(HKCU)`, or `(file)`. See [Verify active settings](https://code.claude.com/docs/en/Verify active settings).

Share these resources to help developers get started:

* [Quickstart](https://code.claude.com/docs/en/Quickstart): first-session walkthrough from install to working with a project
* [Common workflows](https://code.claude.com/docs/en/Common workflows): patterns for everyday tasks like code review, refactoring, and debugging
* [Claude 101](https://code.claude.com/docs/en/Claude 101) and [Claude Code in Action](https://code.claude.com/docs/en/Claude Code in Action): self-paced Anthropic Academy courses

For login issues, point developers to [authentication troubleshooting](https://code.claude.com/docs/en/authentication troubleshooting). The most common fixes are:

* Run `/logout` then `/login` to switch accounts
* Run `claude update` if the enterprise auth option is missing
* Restart the terminal after updating

If a developer sees "You haven't been added to your organization yet," their seat doesn't include Claude Code access and needs to be updated in the admin console.

## Next steps

With provider and delivery mechanism chosen, move on to detailed configuration:

* [Server-managed settings](https://code.claude.com/docs/en/Server-managed settings): deliver managed policy from the Claude admin console
* [Settings reference](https://code.claude.com/docs/en/Settings reference): every setting key, file location, and precedence rule
* [Amazon Bedrock](https://code.claude.com/docs/en/Amazon Bedrock), [Google Vertex AI](https://code.claude.com/docs/en/Google Vertex AI), [Microsoft Foundry](https://code.claude.com/docs/en/Microsoft Foundry): provider-specific deployment
* [Claude Enterprise Administrator Guide](https://code.claude.com/docs/en/Claude Enterprise Administrator Guide): SSO, SCIM, seat management, and rollout playbook
