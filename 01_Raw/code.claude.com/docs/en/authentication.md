---
source_url: https://code.claude.com/docs/en/authentication
fetched_at: 2026-05-04T15:04:27.294871+00:00
fetch_method: mintlify_md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

> Log in to Claude Code and configure authentication for individuals, teams, and organizations.

Claude Code supports multiple authentication methods depending on your setup. Individual users can log in with a Claude.ai account, while teams can use Claude for Teams or Enterprise, the Claude Console, or a cloud provider like Amazon Bedrock, Google Vertex AI, or Microsoft Foundry.

## Log in to Claude Code

After [installing Claude Code](https://code.claude.com/docs/en/installing Claude Code), run `claude` in your terminal. On first launch, Claude Code opens a browser window for you to log in.

If the browser doesn't open automatically, press `c` to copy the login URL to your clipboard, then paste it into your browser.

If your browser shows a login code instead of redirecting back after you sign in, paste it into the terminal at the `Paste code here if prompted` prompt. This happens when the browser can't reach Claude Code's local callback server, which is common in WSL2, SSH sessions, and containers.

You can authenticate with any of these account types:

* **Claude Pro or Max subscription**: log in with your Claude.ai account. Subscribe at [claude.com/pricing](https://code.claude.com/docs/en/claude.com/pricing).
* **Claude for Teams or Enterprise**: log in with the Claude.ai account your team admin invited you to.
* **Claude Console**: log in with your Console credentials. Your admin must have [invited you](https://code.claude.com/docs/en/invited you) first.
* **Cloud providers**: if your organization uses [Amazon Bedrock](https://code.claude.com/docs/en/Amazon Bedrock), [Google Vertex AI](https://code.claude.com/docs/en/Google Vertex AI), or [Microsoft Foundry](https://code.claude.com/docs/en/Microsoft Foundry), set the required environment variables before running `claude`. No browser login is needed.

To log out and re-authenticate, type `/logout` at the Claude Code prompt.

If you're having trouble logging in, see [authentication troubleshooting](https://code.claude.com/docs/en/authentication troubleshooting).

## Set up team authentication

For teams and organizations, you can configure Claude Code access in one of these ways:

* [Claude for Teams or Enterprise](https://code.claude.com/docs/en/Claude for Teams or Enterprise), recommended for most teams
* [Claude Console](https://code.claude.com/docs/en/Claude Console)
* [Amazon Bedrock](https://code.claude.com/docs/en/Amazon Bedrock)
* [Google Vertex AI](https://code.claude.com/docs/en/Google Vertex AI)
* [Microsoft Foundry](https://code.claude.com/docs/en/Microsoft Foundry)

### Claude for Teams or Enterprise

[Claude for Teams](https://code.claude.com/docs/en/Claude for Teams) and [Claude for Enterprise](https://code.claude.com/docs/en/Claude for Enterprise) provide the best experience for organizations using Claude Code. Team members get access to both Claude Code and Claude on the web with centralized billing and team management.

* **Claude for Teams**: self-service plan with collaboration features, admin tools, and billing management. Best for smaller teams.
* **Claude for Enterprise**: adds SSO, domain capture, role-based permissions, compliance API, and managed policy settings for organization-wide Claude Code configurations. Best for larger organizations with security and compliance requirements.

<Steps>
  <Step title="Subscribe">
    Subscribe to [Claude for Teams](https://code.claude.com/docs/en/Claude for Teams) or contact sales for [Claude for Enterprise](https://code.claude.com/docs/en/Claude for Enterprise).
  </Step>

  <Step title="Invite team members">
    Invite team members from the admin dashboard.
  </Step>

  <Step title="Install and log in">
    Team members install Claude Code and log in with their Claude.ai accounts.
  </Step>
</Steps>

### Claude Console authentication

For organizations that prefer API-based billing, you can set up access through the Claude Console.

<Steps>
  <Step title="Create or use a Console account">
    Use your existing Claude Console account or create a new one.
  </Step>

  <Step title="Add users">
    You can add users through either method:

    * Bulk invite users from within the Console: Settings -> Members -> Invite
    * [Set up SSO](https://code.claude.com/docs/en/Set up SSO)
  </Step>

  <Step title="Assign roles">
    When inviting users, assign one of:

    * **Claude Code** role: users can only create Claude Code API keys
    * **Developer** role: users can create any kind of API key
  </Step>

  <Step title="Users complete setup">
    Each invited user needs to:

    * Accept the Console invite
    * [Check system requirements](https://code.claude.com/docs/en/Check system requirements)
    * [Install Claude Code](https://code.claude.com/docs/en/Install Claude Code)
    * Log in with Console account credentials
  </Step>
</Steps>

### Cloud provider authentication

For teams using Amazon Bedrock, Google Vertex AI, or Microsoft Foundry:

<Steps>
  <Step title="Follow provider setup">
    Follow the [Bedrock docs](https://code.claude.com/docs/en/Bedrock docs), [Vertex docs](https://code.claude.com/docs/en/Vertex docs), or [Microsoft Foundry docs](https://code.claude.com/docs/en/Microsoft Foundry docs).
  </Step>

  <Step title="Distribute configuration">
    Distribute the environment variables and instructions for generating cloud credentials to your users. Read more about how to [manage configuration here](https://code.claude.com/docs/en/manage configuration here).
  </Step>

  <Step title="Install Claude Code">
    Users can [install Claude Code](https://code.claude.com/docs/en/install Claude Code).
  </Step>
</Steps>

## Credential management

Claude Code securely manages your authentication credentials:

* **Storage location**: on macOS, credentials are stored in the encrypted macOS Keychain. On Linux and Windows, credentials are stored in `~/.claude/.credentials.json`, or under `$CLAUDE_CONFIG_DIR` if that variable is set. On Linux, the file is written with mode `0600`; on Windows, it inherits the access controls of your user profile directory.
* **Supported authentication types**: Claude.ai credentials, Claude API credentials, Azure Auth, Bedrock Auth, and Vertex Auth.
* **Custom credential scripts**: the [`apiKeyHelper`](https://code.claude.com/docs/en/`apiKeyHelper`) setting can be configured to run a shell script that returns an API key.
* **Refresh intervals**: by default, `apiKeyHelper` is called after 5 minutes or on HTTP 401 response. Set `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` environment variable for custom refresh intervals.
* **Slow helper notice**: if `apiKeyHelper` takes longer than 10 seconds to return a key, Claude Code displays a warning notice in the prompt bar showing the elapsed time. If you see this notice regularly, check whether your credential script can be optimized.

`apiKeyHelper`, `ANTHROPIC_API_KEY`, and `ANTHROPIC_AUTH_TOKEN` apply to terminal CLI sessions only. Claude Desktop and remote sessions use OAuth exclusively and do not call `apiKeyHelper` or read API key environment variables.

### Authentication precedence

When multiple credentials are present, Claude Code chooses one in this order:

1. Cloud provider credentials, when `CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_VERTEX`, or `CLAUDE_CODE_USE_FOUNDRY` is set. See [third-party integrations](https://code.claude.com/docs/en/third-party integrations) for setup.
2. `ANTHROPIC_AUTH_TOKEN` environment variable. Sent as the `Authorization: Bearer` header. Use this when routing through an [LLM gateway or proxy](https://code.claude.com/docs/en/LLM gateway or proxy) that authenticates with bearer tokens rather than Anthropic API keys.
3. `ANTHROPIC_API_KEY` environment variable. Sent as the `X-Api-Key` header. Use this for direct Anthropic API access with a key from the [Claude Console](https://code.claude.com/docs/en/Claude Console). In interactive mode, you are prompted once to approve or decline the key, and your choice is remembered. To change it later, use the "Use custom API key" toggle in `/config`. In non-interactive mode (`-p`), the key is always used when present.
4. [`apiKeyHelper`](https://code.claude.com/docs/en/`apiKeyHelper`) script output. Use this for dynamic or rotating credentials, such as short-lived tokens fetched from a vault.
5. `CLAUDE_CODE_OAUTH_TOKEN` environment variable. A long-lived OAuth token generated by [`claude setup-token`](https://code.claude.com/docs/en/`claude setup-token`). Use this for CI pipelines and scripts where browser login isn't available.
6. Subscription OAuth credentials from `/login`. This is the default for Claude Pro, Max, Team, and Enterprise users.

If you have an active Claude subscription but also have `ANTHROPIC_API_KEY` set in your environment, the API key takes precedence once approved. This can cause authentication failures if the key belongs to a disabled or expired organization. Run `unset ANTHROPIC_API_KEY` to fall back to your subscription, and check `/status` to confirm which method is active.

[Claude Code on the Web](https://code.claude.com/docs/en/Claude Code on the Web) always uses your subscription credentials. `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` in the sandbox environment do not override them.

### Generate a long-lived token

For CI pipelines, scripts, or other environments where interactive browser login isn't available, generate a one-year OAuth token with `claude setup-token`:

```bash theme={null}
claude setup-token
```

The command walks you through OAuth authorization and prints a token to the terminal. It does not save the token anywhere; copy it and set it as the `CLAUDE_CODE_OAUTH_TOKEN` environment variable wherever you want to authenticate:

```bash theme={null}
export CLAUDE_CODE_OAUTH_TOKEN=your-token
```

This token authenticates with your Claude subscription and requires a Pro, Max, Team, or Enterprise plan. It is scoped to inference only and cannot establish [Remote Control](https://code.claude.com/docs/en/Remote Control) sessions.

[Bare mode](https://code.claude.com/docs/en/Bare mode) does not read `CLAUDE_CODE_OAUTH_TOKEN`. If your script passes `--bare`, authenticate with `ANTHROPIC_API_KEY` or an `apiKeyHelper` instead.
